# Shopify D2C OMS Gold Standard Markdown — V2 Client Tables Canonical

```yaml
document_metadata:
  document_id: shopify_d2c_oms_gold_standard_v2_client_tables_manifest_ready
  system: Shopify
  generated_on: '2026-05-24'
  scope: D2C OMS canonical markdown for Shopify brands, refreshed with Client Tables - Shopify configured adjacent sources
  source_files:
  - /mnt/data/Client Tables - Shopify.md
  - /mnt/data/shopify_d2c_oms.md
  - /mnt/data/Shopify OMS.docx
  - /mnt/data/marketplace_cleanup_manifest_consolidated_v2.md
  core_source_tables:
  - table.zs_observe.shopify_oms
  - table.zs_observe.shopify_returns
  reference_only_source_tables:
  - table.zs_observe.shiprocket_oms
  configured_adjacent_source_tables:
  - table.zs_observe.mpl_oms_withdrawal
  - table.zs_observe.mpl_oms_deposit
  - table.zs_observe.woohoo_oms
  - table.zs_observe.amazon_seller_flex
  - table.zs_observe.amazon_gc_settlement
  - table.zs_observe.gullak_technologies_settlement
  - table.zs_observe.pinelabs_soa
  - table.zs_observe.paytm_giftcard_settlement
  - table.zs_observe.red_giraffe_settlement
  - table.zs_observe.nearby_marketplace
  - table.zs_observe.astrotalk_oda
  - table.zs_observe.first_pay_settlement
  - table.zs_observe.amica_technologies_settlement
  - table.zs_observe.aza_wallet_ledger
  - table.zs_observe.aza_return_dump
  - table.zs_observe.aza_sales_dump
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - courier_account
  - logistics_account
  - erp_accounting_mapping
  - statutory_tax_filing
  - connector_config
  - pipeline_retry_policy
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
  - review_item
  source_sha256:
    Client Tables - Shopify.md: 59b25dc9844fe60d7d504f38aab675b670c924520830e19a306f842c2f8273fc
    shopify_d2c_oms.md: d11e1a7e189960a6d2afa3bfd543f941504757edef5d01648d7f69be5b01dd77
    Shopify OMS.docx: d3411d858cd626dcd5c9377dcc0ff3290a9c2f8b33daa1510c95382cb168fd05
    marketplace_cleanup_manifest_consolidated_v2.md: e151167df1ff75a63b6eddaf74f0bfddd8a4741bc67d27988e7455fee8b39661
  quality_summary:
    candidate_cards: 849
    candidate_edges: 780
    source_evidence_count: 29
    sql_patterns: 18
    open_reviews: 3
    missing_edge_references: 0
    dangling_sql_refs: 0
    deleted_card_references: 0
    lazy_workflow_steps: 0
    placeholder_metric_formulas: 0
    unsupported_metric_implementations: 0
    process_variants_review_required: 0
    unresolved_benchmark_reviews_without_reason: 0
    hard_threshold_benchmarks_without_rule: 0
    forbidden_scope_cards_from_scope_ids: 0
  card_type_counts:
    platform: 1
    platform_context: 1
    domain: 8
    table: 19
    column: 739
    value_profile: 6
    relationship: 6
    metric: 13
    metric_implementation: 13
    output_contract: 3
    query_pattern: 7
    rule: 6
    validation_test: 5
    reconciliation_profile: 5
    business_process: 5
    workflow_step: 9
    review_item: 3
```
## 0. Parser Instructions

This document is intended for deterministic parsing. It refreshes the Shopify canonical using the new `Client Tables - Shopify.md` intake while keeping Shopify OMS as the core platform and treating all non-Shopify tables as configured-adjacent sources. Do not infer tenant, account, bank, courier, ERP, connector, or statutory filing cards from scope identifiers, payment references, settlement references, GSTIN-like values, UTRs, courier labels, or gateway labels.

```yaml
manifest_crosswalk:
  source_manifest: marketplace_cleanup_manifest_consolidated_v2.md
  applied_to: Shopify D2C OMS plus Client Tables configured adjacent sources
  release_gates:
  - Every candidate card has evidence_refs.
  - Core Shopify table type fidelity follows the dedicated Shopify OMS doc where it conflicts with the broader client markdown.
  - Non-Shopify tables remain configured-adjacent sources, not Shopify platform identities.
  - Metric implementations are SQL-like and reference declared tables/columns.
  - Every sql_reference_id resolves to a sql_pattern block.
  - Every candidate_edge resolves to existing card ids.
  - Scope identifiers, UTRs, payment refs, courier labels, GSTIN-like values and bank references remain columns/value profiles/reconciliation
    keys, not account cards.
  scope_identifier_policy: documented group_id/group_level_id values may be represented as scope values only; runtime account
    binding remains external
```
```yaml
semantic_field_contract:
- card_type: platform
  required_fields:
  - display_name
  - platform_category
  - evidence_refs
  parser_instruction: Create the Shopify platform identity only once.
- card_type: platform_context
  required_fields:
  - platform_id
  - country_code
  - currency_context
  - scope_filter_columns
  - evidence_refs
  parser_instruction: Scope values are filters, not account cards.
- card_type: table
  required_fields:
  - schema_name
  - table_name
  - table_role
  - row_scope
  - grain
  - mandatory_filters
  - evidence_refs
  parser_instruction: Configured adjacent tables require runtime selection before they affect Shopify analysis.
- card_type: column
  required_fields:
  - table_id
  - column_name
  - data_type
  - semantic_role
  - description
  - evidence_refs
  parser_instruction: Preserve source names and type caveats; apply cast_required where set.
- card_type: value_profile
  required_fields:
  - table_id
  - column_names
  - values_or_documented_scope_values
  - evidence_refs
  parser_instruction: Segments/statuses remain value profiles unless source gives a different workflow.
- card_type: relationship
  required_fields:
  - from_table
  - to_table
  - join_keys
  - join_safety_rule
  - relationship_grain
  - evidence_refs
  parser_instruction: Use aggregate-before-join guardrails.
- card_type: metric_implementation
  required_fields:
  - metric_id
  - source_table_ids
  - formula
  - sql_reference_id
  - required_filters
  - evidence_refs
  parser_instruction: Formula must resolve to an executable SQL pattern.
- card_type: query_pattern
  required_fields:
  - natural_language_patterns
  - primary_metric
  - source_table_ids
  - sql_reference_id
  - output_contract_id
  - evidence_refs
  parser_instruction: Output contract and SQL ref must resolve.
- card_type: review_item
  required_fields:
  - issue_type
  - question
  - why_open
  - evidence_refs
  parser_instruction: Use only for true source gaps or runtime-scope bindings.
```
## 1. Source Evidence Registry

```yaml
source_evidence:
  id: ev.shopify.client_tables.platform.001
  source_document: Client Tables - Shopify.md
  source_section: Platform Overview; Universal System Columns
  evidence_type: schema_reference
  summary: zs_observe is the observation/ingestion layer for OMS, marketplace, payment gateway and settlement files; universal
    system columns include scope, lineage, quality and currency fields.
  supported_semantics:
  - universal system columns
  - multi-source ingestion scope
  - quality flags
  unsupported_semantics:
  - tenant/account card creation from scope ids
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_tables.core_oms.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 3: shopify_oms'
  evidence_type: schema_reference
  summary: shopify_oms captures forward sales orders from Shopify-powered D2C stores at line-item grain and is reconciled
    against payment gateway settlements.
  supported_semantics:
  - Shopify D2C order source
  - order line grain
  - payment/fulfillment/tax/order columns
  unsupported_semantics:
  - gateway account ownership
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_tables.returns.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 4: shopify_returns'
  evidence_type: schema_reference
  summary: shopify_returns captures return/refund transaction records with order_name, transaction_id, payment_gateway, transaction_status,
    order_payment_status, refunded_payments and other_id.
  supported_semantics:
  - Shopify refund event ledger
  - gateway refund reference fields
  unsupported_semantics:
  - external PG account binding
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_tables.flow.001
  source_document: Client Tables - Shopify.md
  source_section: 'Business Flow Diagrams > Flow 6: Shopify D2C Brand Settlement'
  evidence_type: workflow
  summary: Shopify D2C flow records customer orders in shopify_oms, prepaid gateway settlement via Razorpay/Cashfree, COD
    remittance via Shiprocket/BlueDart, refund events in shopify_returns, and OMS-to-PG-to-bank reconciliation.
  supported_semantics:
  - Shopify order-to-settlement reconciliation profile
  - prepaid and COD settlement timing labels
  - refund event linkage
  unsupported_semantics:
  - bank account cards
  - payment gateway account cards
  - courier account cards
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_tables.group_scope.001
  source_document: Client Tables - Shopify.md
  source_section: Tenant / Group Architecture
  evidence_type: caveat
  summary: Observed group_id values include 8 for Shopify brands and 45 for European Shopify store; these are documented scope
    values only, not tenant or account cards.
  supported_semantics:
  - scope value profile
  - runtime filter hint
  unsupported_semantics:
  - tenant card creation
  - platform account binding
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_tables.common_recon.001
  source_document: Client Tables - Shopify.md
  source_section: Common Reconciliation Patterns
  evidence_type: reconciliation_playbook
  summary: Common patterns include settlement-vs-bank credit by UTR/settlement_id/pg_utr, OMS-vs-settlement by order_id, MPL
    deposit to PG settlement, AZA sales to PG, and AZA return to wallet ledger.
  supported_semantics:
  - configured adjacent reconciliation patterns
  - join key hints
  - settlement/bank matching keys as columns
  unsupported_semantics:
  - bank statement card creation unless source table exists
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_tables.data_quality.001
  source_document: Client Tables - Shopify.md
  source_section: Data Quality Flags
  evidence_type: caveat
  summary: Data quality flags include is_active, is_duplicated, zen_status and false-reason fields across tables.
  supported_semantics:
  - quality filter rules
  unsupported_semantics:
  - pipeline retry policy cards
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.dedicated_oms.schema.001
  source_document: Shopify OMS.docx
  source_section: Schema (Key Fields)
  evidence_type: schema_reference
  summary: Dedicated Shopify OMS doc declares key fields including order_id, transaction_type, financial_status, fullfilment_status,
    payment_mode, charged_amount, refunded_amount, mrp, sku_id, brand, quantity, destination fields, cancellation_date, other_id,
    created_date, is_active, group_level_id and unique_id.
  supported_semantics:
  - dedicated Shopify schema
  - type override for amount/date strings
  unsupported_semantics:
  - generic numeric type assumption for Shopify amount fields
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.dedicated_oms.logic.001
  source_document: Shopify OMS.docx
  source_section: Business Logic
  evidence_type: rule
  summary: Shopify multi-line orders use other_id suffixes; order-level GMV sums charged_amount by order_id. financial_status
    maps paid to prepaid, pending to COD, partially_paid to PPCOD, and voided to cancelled-before-shipment.
  supported_semantics:
  - order-level aggregation
  - payment-state value profile
  - COD/PPCOD semantics
  unsupported_semantics:
  - process variants from payment labels alone
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.dedicated_oms.shiprocket.001
  source_document: Shopify OMS.docx
  source_section: Join Patterns; Data Quality Notes
  evidence_type: query_example
  summary: Shopify order links to Shiprocket shipment with sr.order_id LIKE CONCAT(s.order_id, '-%'); active filters are required
    and charged_amount is varchar requiring cast to DOUBLE.
  supported_semantics:
  - Shopify-to-Shiprocket reference relationship
  - active filter
  - varchar amount cast
  unsupported_semantics:
  - courier account creation
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.manifest.cleanup.001
  source_document: marketplace_cleanup_manifest_consolidated_v2.md
  source_section: Recommended Repeatable Cleanup Sequence; Parser QA Summary Manifest
  evidence_type: cleanup_manifest
  summary: Manifest requires evidence-first cards, type fidelity, executable metric implementations, clean SQL references,
    edge integrity, scope guardrails and parser QA summary.
  supported_semantics:
  - quality gates
  - scope guardrails
  - SQL/edge integrity
  unsupported_semantics:
  - lazy generic workflows
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_table.mpl_oms_withdrawal.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 1: mpl_oms_withdrawal'
  evidence_type: schema_reference
  summary: Documents mpl_oms_withdrawal business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - mpl_oms_withdrawal table card
  - mpl_oms_withdrawal key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.mpl_oms_deposit.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 2: mpl_oms_deposit'
  evidence_type: schema_reference
  summary: Documents mpl_oms_deposit business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - mpl_oms_deposit table card
  - mpl_oms_deposit key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.shopify_oms.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 3: shopify_oms'
  evidence_type: schema_reference
  summary: Documents shopify_oms business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - shopify_oms table card
  - shopify_oms key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_table.shopify_returns.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 4: shopify_returns'
  evidence_type: schema_reference
  summary: Documents shopify_returns business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - shopify_returns table card
  - shopify_returns key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.client_table.woohoo_oms.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 5: woohoo_oms'
  evidence_type: schema_reference
  summary: Documents woohoo_oms business context, key columns, rules and reconciliation use cases as a client-configured source
    table.
  supported_semantics:
  - woohoo_oms table card
  - woohoo_oms key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.amazon_seller_flex.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 6: amazon_seller_flex'
  evidence_type: schema_reference
  summary: Documents amazon_seller_flex business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - amazon_seller_flex table card
  - amazon_seller_flex key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.amazon_gc_settlement.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 7: amazon_gc_settlement'
  evidence_type: schema_reference
  summary: Documents amazon_gc_settlement business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - amazon_gc_settlement table card
  - amazon_gc_settlement key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.gullak_technologies_settlement.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 8: gullak_technologies_settlement'
  evidence_type: schema_reference
  summary: Documents gullak_technologies_settlement business context, key columns, rules and reconciliation use cases as a
    client-configured source table.
  supported_semantics:
  - gullak_technologies_settlement table card
  - gullak_technologies_settlement key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.pinelabs_soa.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 9: pinelabs_soa'
  evidence_type: schema_reference
  summary: Documents pinelabs_soa business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - pinelabs_soa table card
  - pinelabs_soa key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.paytm_giftcard_settlement.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 10: paytm_giftcard_settlement'
  evidence_type: schema_reference
  summary: Documents paytm_giftcard_settlement business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - paytm_giftcard_settlement table card
  - paytm_giftcard_settlement key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.red_giraffe_settlement.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 11: red_giraffe_settlement'
  evidence_type: schema_reference
  summary: Documents red_giraffe_settlement business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - red_giraffe_settlement table card
  - red_giraffe_settlement key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.nearby_marketplace.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 12: nearby_marketplace'
  evidence_type: schema_reference
  summary: Documents nearby_marketplace business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - nearby_marketplace table card
  - nearby_marketplace key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.astrotalk_oda.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 13: astrotalk_oda'
  evidence_type: schema_reference
  summary: Documents astrotalk_oda business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - astrotalk_oda table card
  - astrotalk_oda key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.first_pay_settlement.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 14: first_pay_settlement'
  evidence_type: schema_reference
  summary: Documents first_pay_settlement business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - first_pay_settlement table card
  - first_pay_settlement key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.amica_technologies_settlement.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 15: amica_technologies_settlement'
  evidence_type: schema_reference
  summary: Documents amica_technologies_settlement business context, key columns, rules and reconciliation use cases as a
    client-configured source table.
  supported_semantics:
  - amica_technologies_settlement table card
  - amica_technologies_settlement key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.aza_wallet_ledger.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 16: aza_wallet_ledger'
  evidence_type: schema_reference
  summary: Documents aza_wallet_ledger business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - aza_wallet_ledger table card
  - aza_wallet_ledger key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.aza_return_dump.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 17: aza_return_dump'
  evidence_type: schema_reference
  summary: Documents aza_return_dump business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - aza_return_dump table card
  - aza_return_dump key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
```yaml
source_evidence:
  id: ev.shopify.client_table.aza_sales_dump.001
  source_document: Client Tables - Shopify.md
  source_section: 'Table 18: aza_sales_dump'
  evidence_type: schema_reference
  summary: Documents aza_sales_dump business context, key columns, rules and reconciliation use cases as a client-configured
    source table.
  supported_semantics:
  - aza_sales_dump table card
  - aza_sales_dump key column cards
  unsupported_semantics:
  - tenant/account/bank/courier/payment-gateway account card creation from labels or references
  confidence: medium
```
## 2. Scope Guardrails and Out-of-Scope Registry

```yaml
out_of_scope_item:
  id: oos.shopify.tenant_group
  topic: tenant/group/account scope
  instruction: group_id, tenant_id and group_level_id are scope/filter columns or documented values only. Never create tenant,
    group, platform_account, account_data_binding or business_scope cards from them.
  forbidden_card_population:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.group_scope.001
```
```yaml
out_of_scope_item:
  id: oos.shopify.pg_bank_accounts
  topic: payment gateway and bank accounts
  instruction: payment_id, payment_references, pg_utr, cod_utr, utr_number, settlement_id and gateway labels are reconciliation
    references. Do not create bank_account or payment_gateway_account cards without explicit account source tables.
  forbidden_card_population:
  - bank_account
  - bank_statement
  - payment_gateway_account
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.client_tables.common_recon.001
```
```yaml
out_of_scope_item:
  id: oos.shopify.courier_accounts
  topic: courier/logistics accounts
  instruction: Shiprocket/BlueDart/Delhivery/courier labels and AWB fields are shipment references only in this Shopify canonical.
    Do not create courier/logistics account cards.
  forbidden_card_population:
  - courier_account
  - logistics_account
  - carrier_reconciliation
  evidence_refs:
  - ev.shopify.dedicated_oms.shiprocket.001
  - ev.shopify.client_tables.flow.001
```
```yaml
out_of_scope_item:
  id: oos.shopify.non_shopify_adjacent_tables
  topic: non-Shopify configured adjacent sources
  instruction: MPL, Woohoo, Amazon GC, Pine Labs, Paytm, AZA, and other tables from Client Tables are included as configured-adjacent
    source semantics only. They must not be converted into Shopify platform identity cards.
  forbidden_card_population:
  - platform_alias_as_shopify
  - tenant
  - group
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
```
```yaml
out_of_scope_item:
  id: oos.shopify.statutory_filing
  topic: statutory filing
  instruction: GST/TCS/TDS/tax fields may support invoice or deduction analytics only. Do not create statutory filing cards.
  forbidden_card_population:
  - statutory_tax_filing
  - erp_accounting_mapping
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  - ev.shopify.manifest.cleanup.001
```
## 3. Source Table Intake Summary

```yaml
source_table_summary:
- table_id: table.zs_observe.mpl_oms_withdrawal
  table_name: zs_observe.mpl_oms_withdrawal
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_player_wallet_payout_oms
  grain: source_row
  primary_date_column: txn_date
  primary_amount_column: amount
  column_count: 21
- table_id: table.zs_observe.mpl_oms_deposit
  table_name: zs_observe.mpl_oms_deposit
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_player_wallet_deposit_oms
  grain: source_row
  primary_date_column: txn_date
  primary_amount_column: amount
  column_count: 20
- table_id: table.zs_observe.shopify_oms
  table_name: zs_observe.shopify_oms
  shopify_core_table: true
  configured_adjacent_source_table: false
  role: core_shopify_d2c_order_line_ledger
  grain: order_line
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 41
- table_id: table.zs_observe.shopify_returns
  table_name: zs_observe.shopify_returns
  shopify_core_table: true
  configured_adjacent_source_table: false
  role: core_shopify_refund_event_ledger
  grain: refund_event
  primary_date_column: customer_added_date
  primary_amount_column: refunded_payments
  column_count: 9
- table_id: table.zs_observe.woohoo_oms
  table_name: zs_observe.woohoo_oms
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_gift_card_order_oms
  grain: source_row
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 28
- table_id: table.zs_observe.amazon_seller_flex
  table_name: zs_observe.amazon_seller_flex
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_gift_card_activation_ledger
  grain: source_row
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 28
- table_id: table.zs_observe.amazon_gc_settlement
  table_name: zs_observe.amazon_gc_settlement
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_marketplace_settlement_ledger
  grain: source_row
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 28
- table_id: table.zs_observe.gullak_technologies_settlement
  table_name: zs_observe.gullak_technologies_settlement
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_partner_settlement_ledger
  grain: source_row
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 15
- table_id: table.zs_observe.pinelabs_soa
  table_name: zs_observe.pinelabs_soa
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_ar_statement_ledger
  grain: ar_statement_line
  primary_date_column: transaction_date
  primary_amount_column: charged_amount
  column_count: 33
- table_id: table.zs_observe.paytm_giftcard_settlement
  table_name: zs_observe.paytm_giftcard_settlement
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_marketplace_settlement_ledger
  grain: source_row
  primary_date_column: settlement_date
  primary_amount_column: charged_amount
  column_count: 32
- table_id: table.zs_observe.red_giraffe_settlement
  table_name: zs_observe.red_giraffe_settlement
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_partner_settlement_ledger
  grain: source_row
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 18
- table_id: table.zs_observe.nearby_marketplace
  table_name: zs_observe.nearby_marketplace
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_marketplace_settlement_adjustment_ledger
  grain: source_row
  primary_date_column: settlement_date
  primary_amount_column: charged_amount
  column_count: 29
- table_id: table.zs_observe.astrotalk_oda
  table_name: zs_observe.astrotalk_oda
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_logistics_oda_reference
  grain: oda_reference_row
  primary_date_column: start_date
  primary_amount_column: not_documented
  column_count: 8
- table_id: table.zs_observe.first_pay_settlement
  table_name: zs_observe.first_pay_settlement
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_partner_settlement_ledger
  grain: source_row
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 16
- table_id: table.zs_observe.amica_technologies_settlement
  table_name: zs_observe.amica_technologies_settlement
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_partner_settlement_ledger
  grain: source_row
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 21
- table_id: table.zs_observe.aza_wallet_ledger
  table_name: zs_observe.aza_wallet_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_wallet_ledger
  grain: wallet_ledger_entry
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 6
- table_id: table.zs_observe.aza_return_dump
  table_name: zs_observe.aza_return_dump
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_return_order_ledger
  grain: return_item
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 29
- table_id: table.zs_observe.aza_sales_dump
  table_name: zs_observe.aza_sales_dump
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: configured_adjacent_order_sales_ledger
  grain: order_item
  primary_date_column: created_date
  primary_amount_column: charged_amount
  column_count: 40
- table_id: table.zs_observe.shiprocket_oms
  table_name: zs_observe.shiprocket_oms
  shopify_core_table: false
  configured_adjacent_source_table: true
  role: shipment_relationship_reference_only
  grain: shipment
  primary_date_column: not_documented
  primary_amount_column: not_applicable
  column_count: 4
```
## 4. Candidate Card Registry

### 4.x platform

```yaml
candidate_card:
  card_type: platform
  card_id: platform.shopify
  display_name: Shopify
  canonical_name: Shopify
  platform_category: d2c_channel_oms
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x platform_context

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.shopify.in_and_global.d2c_oms_client_config
  display_name: Shopify D2C OMS with client-configured adjacent sources
  platform_id: platform.shopify
  country_code:
  - IN
  - GB/global where shopify_returns EUK rows are present
  currency_context:
  - INR primary
  - GBP in European Shopify returns context
  - USD possible only where source rows explicitly say so
  timezone: Asia/Kolkata by default for India D2C analysis
  scope_filter_columns:
  - group_id
  - tenant_id
  - group_level_id
  - brand
  - currency_type
  - financial_status
  - payment_mode
  documented_scope_values:
    shopify_brands_group_id: 8
    european_shopify_store_group_id: 45
  configured_adjacent_table_policy: include as source tables only when runtime configuration maps them into the Shopify/client
    reconciliation workflow
  evidence_refs:
  - ev.shopify.client_tables.group_scope.001
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x domain

```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.d2c_order_capture
  display_name: D2C Shopify order capture
  domain_family: d2c_oms_orders
  semantic_scope: Shopify storefront order capture at order-line grain in shopify_oms.
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.payment_state
  display_name: Shopify payment-state semantics
  domain_family: d2c_payment_state
  semantic_scope: financial_status, payment_mode, payment_id and payment_references for prepaid, COD, PPCOD and gateway-reference
    semantics.
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.fulfillment_state
  display_name: Shopify fulfillment-state semantics
  domain_family: d2c_fulfillment_state
  semantic_scope: transaction_type, order_status, fulfillment_status/fullfilment_status and Shiprocket reference link semantics.
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.refunds_returns
  display_name: Shopify refunds and returns
  domain_family: d2c_returns_refunds
  semantic_scope: shopify_returns refund event capture and refund payment status semantics.
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.tax_discount_amounts
  display_name: Shopify tax, discount and amount semantics
  domain_family: d2c_tax_amounts
  semantic_scope: charged_amount, subtotal, shipping, tax, discount, refund and outstanding balance metrics.
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.reconciliation
  display_name: Shopify reconciliation hooks
  domain_family: d2c_reconciliation
  semantic_scope: OMS-to-PG, COD remittance, refund-to-gateway, order-to-bank and configured adjacent reconciliation patterns.
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.configured_adjacent_sources
  display_name: Client-configured adjacent sources
  domain_family: configured_adjacent_sources
  semantic_scope: Non-Shopify tables supplied in the client markdown, retained as source-table semantics and runtime-configurable
    reconciliation inputs.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.data_quality_scope
  display_name: Data quality and scope guardrails
  domain_family: data_quality_scope
  semantic_scope: Universal quality flags, active-row filters, type fidelity and scope-identifier handling.
  evidence_refs:
  - ev.shopify.client_tables.data_quality.001
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x table

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.mpl_oms_withdrawal
  display_name: zs_observe.mpl_oms_withdrawal
  schema_name: zs_observe
  table_name: mpl_oms_withdrawal
  source_system: MPL OMS
  table_role: configured_adjacent_player_wallet_payout_oms
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One player withdrawal / outward money movement from OMS to payment rail or bank.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: txn_date
  primary_amount_column: amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.mpl_oms_deposit
  display_name: zs_observe.mpl_oms_deposit
  schema_name: zs_observe
  table_name: mpl_oms_deposit
  source_system: MPL OMS
  table_role: configured_adjacent_player_wallet_deposit_oms
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One player deposit / inward wallet-credit event from a payment gateway.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: txn_date
  primary_amount_column: amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shopify_oms
  display_name: zs_observe.shopify_oms
  schema_name: zs_observe
  table_name: shopify_oms
  source_system: Shopify OMS
  table_role: core_shopify_d2c_order_line_ledger
  shopify_core_table: true
  configured_adjacent_source_table: false
  row_scope: One Shopify order line item; order_id repeats for multi-SKU orders.
  grain: order_line
  mandatory_filters:
  - is_active = true
  - TRY_CAST varchar amount/date fields before financial/date aggregation
  recommended_filters:
  - group_id IN (8,45) only when runtime scope selects Shopify brand context
  - group_level_id = 22 only when reproducing dedicated Shopify table scope
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shopify_returns
  display_name: zs_observe.shopify_returns
  schema_name: zs_observe
  table_name: shopify_returns
  source_system: Shopify OMS
  table_role: core_shopify_refund_event_ledger
  shopify_core_table: true
  configured_adjacent_source_table: false
  row_scope: One Shopify return/refund payment event with gateway status and original order reference.
  grain: refund_event
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - group_id = 45 for European Shopify store only when runtime scope selects that context
  primary_date_column: customer_added_date
  primary_amount_column: refunded_payments
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.woohoo_oms
  display_name: zs_observe.woohoo_oms
  schema_name: zs_observe
  table_name: woohoo_oms
  source_system: Woohoo / Qwikcilver OMS
  table_role: configured_adjacent_gift_card_order_oms
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One Woohoo gift-card order / issue event, usually from Amazon integration.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.amazon_seller_flex
  display_name: zs_observe.amazon_seller_flex
  schema_name: zs_observe
  table_name: amazon_seller_flex
  source_system: Amazon Seller Flex / Qwikcilver
  table_role: configured_adjacent_gift_card_activation_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One Amazon Seller Flex gift-card activation/deactivation/cancel event.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.amazon_gc_settlement
  display_name: zs_observe.amazon_gc_settlement
  schema_name: zs_observe
  table_name: amazon_gc_settlement
  source_system: Amazon GC Settlement
  table_role: configured_adjacent_marketplace_settlement_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One Amazon gift-card settlement line item within a settlement batch.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.gullak_technologies_settlement
  display_name: zs_observe.gullak_technologies_settlement
  schema_name: zs_observe
  table_name: gullak_technologies_settlement
  source_system: Gullak Technologies settlement
  table_role: configured_adjacent_partner_settlement_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One Gullak partner settlement order line or settlement row.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.pinelabs_soa
  display_name: zs_observe.pinelabs_soa
  schema_name: zs_observe
  table_name: pinelabs_soa
  source_system: Pine Labs / Qwikcilver SOA
  table_role: configured_adjacent_ar_statement_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: 'One Oracle AR statement line: invoice, debit memo, credit memo, or payment.'
  grain: ar_statement_line
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: transaction_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.paytm_giftcard_settlement
  display_name: zs_observe.paytm_giftcard_settlement
  schema_name: zs_observe
  table_name: paytm_giftcard_settlement
  source_system: Paytm marketplace settlement
  table_role: configured_adjacent_marketplace_settlement_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One Paytm gift-card settlement line with PG/COD net settlement amounts.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: settlement_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.red_giraffe_settlement
  display_name: zs_observe.red_giraffe_settlement
  schema_name: zs_observe
  table_name: red_giraffe_settlement
  source_system: Red Giraffe settlement
  table_role: configured_adjacent_partner_settlement_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One Red Giraffe gift-card partner settlement line.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.nearby_marketplace
  display_name: zs_observe.nearby_marketplace
  schema_name: zs_observe
  table_name: nearby_marketplace
  source_system: Nearby marketplace
  table_role: configured_adjacent_marketplace_settlement_adjustment_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One Nearby marketplace order/settlement/adjustment entry.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: settlement_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.astrotalk_oda
  display_name: zs_observe.astrotalk_oda
  schema_name: zs_observe
  table_name: astrotalk_oda
  source_system: Astrotalk ODA reference
  table_role: configured_adjacent_logistics_oda_reference
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One pincode/courier ODA charge reference row.
  grain: oda_reference_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: start_date
  primary_amount_column: not_documented
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.first_pay_settlement
  display_name: zs_observe.first_pay_settlement
  schema_name: zs_observe
  table_name: first_pay_settlement
  source_system: FirstPay settlement
  table_role: configured_adjacent_partner_settlement_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One FirstPay gift-card settlement/order line.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.amica_technologies_settlement
  display_name: zs_observe.amica_technologies_settlement
  schema_name: zs_observe
  table_name: amica_technologies_settlement
  source_system: Amica/Jupiter settlement
  table_role: configured_adjacent_partner_settlement_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One Amica/Jupiter gift-card settlement/order line.
  grain: source_row
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.aza_wallet_ledger
  display_name: zs_observe.aza_wallet_ledger
  schema_name: zs_observe
  table_name: aza_wallet_ledger
  source_system: AZA wallet
  table_role: configured_adjacent_wallet_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One AZA wallet credit or debit ledger entry.
  grain: wallet_ledger_entry
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.aza_wallet_ledger.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.aza_return_dump
  display_name: zs_observe.aza_return_dump
  schema_name: zs_observe
  table_name: aza_return_dump
  source_system: AZA returns
  table_role: configured_adjacent_return_order_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One AZA returned order item / return line.
  grain: return_item
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.aza_sales_dump
  display_name: zs_observe.aza_sales_dump
  schema_name: zs_observe
  table_name: aza_sales_dump
  source_system: AZA sales
  table_role: configured_adjacent_order_sales_ledger
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: One AZA forward sales order item / sales line.
  grain: order_item
  mandatory_filters:
  - is_active = true when column exists
  recommended_filters:
  - Do not include in Shopify core metrics unless runtime client configuration explicitly maps this table into the analysis.
  primary_date_column: created_date
  primary_amount_column: charged_amount
  runtime_scope_policy: scope identifiers remain filter values; no tenant/account card creation
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: medium
  review_status: accepted_as_configured_adjacent_source
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shiprocket_oms
  display_name: zs_observe.shiprocket_oms (reference only)
  schema_name: zs_observe
  table_name: shiprocket_oms
  source_system: Shiprocket
  table_role: shipment_relationship_reference_only
  shopify_core_table: false
  configured_adjacent_source_table: true
  row_scope: Reference-only shipment table used for Shopify order-to-shipment enrichment by order_id suffix.
  grain: shipment
  mandatory_filters:
  - is_active = true
  runtime_scope_policy: do not create courier account cards from this table in Shopify canonical
  evidence_refs:
  - ev.shopify.dedicated_oms.shiprocket.001
  confidence: medium
  review_status: accepted_as_reference_only
  create_action: create_reference_only
```
### 4.x column

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: '`USD` (US market), `INR` (India), `NGN` (Nigeria)'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.txn_date
  display_name: txn_date
  column_name: txn_date
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Date the withdrawal was initiated/settled
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.reference_id
  display_name: reference_id
  column_name: reference_id
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: MPL's internal transaction reference (e.g. `MPLPID_US_4558321`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.pg_ref_id
  display_name: pg_ref_id
  column_name: pg_ref_id
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Payment gateway reference ID (null when PG not involved)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.txn_description
  display_name: txn_description
  column_name: txn_description
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Always `MONEY_OUT` for withdrawals
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.payment_gateway
  display_name: payment_gateway
  column_name: payment_gateway
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: 'PG used: `skrill`, `paypal`, `bank_transfer`, `paytm`, etc.'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.payment_mode
  display_name: payment_mode
  column_name: payment_mode
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Mode within the gateway
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.status
  display_name: status
  column_name: status
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`SUCCESS`, `FAILED`, `PENDING`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.sub_status
  display_name: sub_status
  column_name: sub_status
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: Granular status (error codes, partial)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.txn_type
  display_name: txn_type
  column_name: txn_type
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Transaction sub-type
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.txn_sub_type
  display_name: txn_sub_type
  column_name: txn_sub_type
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Further classification
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.amount
  display_name: amount
  column_name: amount
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Withdrawal amount in the transaction currency
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.dt
  display_name: dt
  column_name: dt
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: date
  source_declared_type: date
  semantic_role: source_attribute
  description: Processing date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.withdrawal_initiated_dt
  display_name: withdrawal_initiated_dt
  column_name: withdrawal_initiated_dt
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: date
  source_declared_type: date
  semantic_role: source_attribute
  description: When player clicked withdraw
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.user_id
  display_name: user_id
  column_name: user_id
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: MPL's internal user/player ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Same as txn_description (`MONEY_OUT`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.kb_transfer_mode
  display_name: kb_transfer_mode
  column_name: kb_transfer_mode
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: KnowledgeBase transfer mode (internal flag)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.kb_status
  display_name: kb_status
  column_name: kb_status
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: KB processing status
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.kb_amount
  display_name: kb_amount
  column_name: kb_amount
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: KB verified amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.kb_dt
  display_name: kb_dt
  column_name: kb_dt
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: date
  source_declared_type: date
  semantic_role: source_attribute
  description: KB processing date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_withdrawal.abt_amount
  display_name: abt_amount
  column_name: abt_amount
  table_id: table.zs_observe.mpl_oms_withdrawal
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Actual bank transfer amount (post-fees)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_withdrawal.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: '`INR` or `USD`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.txn_date
  display_name: txn_date
  column_name: txn_date
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Date of deposit
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.reference_id
  display_name: reference_id
  column_name: reference_id
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: MPL transaction reference (e.g. `MPLPID_IN_1179110416`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.pg_ref_id
  display_name: pg_ref_id
  column_name: pg_ref_id
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Payment gateway reference
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.txn_description
  display_name: txn_description
  column_name: txn_description
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Always `MONEY_IN` for deposits
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.payment_gateway
  display_name: payment_gateway
  column_name: payment_gateway
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`pinelabs_online`, `razorpay`, `paytm`, `phonepe`, `stripe`, etc.'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.payment_mode
  display_name: payment_mode
  column_name: payment_mode
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`Card`, `UPI`, `NetBanking`, `Wallet`, etc.'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.status
  display_name: status
  column_name: status
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`success`, `failed`, `pending`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.txn_type
  display_name: txn_type
  column_name: txn_type
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`Deposit`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.amount
  display_name: amount
  column_name: amount
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount deposited
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.id
  display_name: id
  column_name: id
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Gateway's internal transaction ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.ist_time
  display_name: ist_time
  column_name: ist_time
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: IST datetime of the transaction
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.money_type
  display_name: money_type
  column_name: money_type
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`Deposit`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.payment_gateway2
  display_name: payment_gateway2
  column_name: payment_gateway2
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Secondary PG classification
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.payment_method
  display_name: payment_method
  column_name: payment_method
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`CARD`, `UPI`, `NETBANKING`'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.reference_type
  display_name: reference_type
  column_name: reference_type
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Type of payment reference
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`CREDIT`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.user_id
  display_name: user_id
  column_name: user_id
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Player's MPL user ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.pg_reference_id
  display_name: pg_reference_id
  column_name: pg_reference_id
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Additional PG reference
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.mpl_oms_deposit.transaction_external_key
  display_name: transaction_external_key
  column_name: transaction_external_key
  table_id: table.zs_observe.mpl_oms_deposit
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: External key from PG
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.mpl_oms_deposit.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Client Tables source type=varchar_or_integer; Dedicated Shopify OMS doc declares varchar and always 22 for this table
    scope.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.shopify_oms
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.shopify_oms
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.shopify_oms
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.shopify_oms
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.shopify_oms
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.shopify_oms
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: '`INR`, `GBP`, `USD`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Brand's order number (e.g. `BHIN2628310`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.id
  display_name: id
  column_name: id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Shopify's internal order ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.name
  display_name: name
  column_name: name
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: 'Shopify order name with # prefix (e.g. `#BHIN2628310`)'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Order creation date
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Client Tables source type=date; Dedicated Shopify OMS doc declares varchar; cast before date filtering.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`fulfilled`, `cancelled`, `refunded`, `pending`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.order_status
  display_name: order_status
  column_name: order_status
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: '`fulfilled`, `partially_fulfilled`, `unfulfilled`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.fulfillment_status
  display_name: fulfillment_status
  column_name: fulfillment_status
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: Current fulfillment state
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.financial_status
  display_name: financial_status
  column_name: financial_status
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`paid`, `pending`, `partially_paid`, `refunded`, `voided`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.buyers_name
  display_name: buyers_name
  column_name: buyers_name
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: customer_attribute
  description: Customer name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.email
  display_name: email
  column_name: email
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: customer_attribute
  description: Customer email
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.phone
  display_name: phone
  column_name: phone
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: customer_attribute
  description: Customer phone number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.brand
  display_name: brand
  column_name: brand
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Brand/vendor name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.sku_id
  display_name: sku_id
  column_name: sku_id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product SKU
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product name/description
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.quantity
  display_name: quantity
  column_name: quantity
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: integer
  semantic_role: source_attribute
  description: Line item quantity
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Client Tables source type=integer; Dedicated Shopify OMS doc declares varchar; cast before quantity math.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.mrp
  display_name: mrp
  column_name: mrp
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Maximum Retail Price
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Client Tables source type=numeric; Dedicated Shopify OMS doc declares varchar; cast for numeric calculations.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.lineitem_price
  display_name: lineitem_price
  column_name: lineitem_price
  table_id: table.zs_observe.shopify_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Actual selling price per unit
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Extended Client Tables field documented as numeric; no dedicated-doc conflict found.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total amount charged to customer
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Client Tables source type=numeric; Dedicated Shopify OMS doc declares varchar; TRY_CAST to DOUBLE for aggregation.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.subtotal
  display_name: subtotal
  column_name: subtotal
  table_id: table.zs_observe.shopify_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Order subtotal (excl. shipping)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Extended Client Tables field documented as numeric; no dedicated-doc conflict found.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.shipping_amount
  display_name: shipping_amount
  column_name: shipping_amount
  table_id: table.zs_observe.shopify_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Shipping charges
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Extended Client Tables field documented as numeric; no dedicated-doc conflict found.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.total_tax
  display_name: total_tax
  column_name: total_tax
  table_id: table.zs_observe.shopify_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total tax collected
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Extended Client Tables field documented as numeric; no dedicated-doc conflict found.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.total_tax_perc
  display_name: total_tax_perc
  column_name: total_tax_perc
  table_id: table.zs_observe.shopify_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Tax percentage (e.g. 0.18 = 18% GST)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Extended Client Tables field documented as numeric; no dedicated-doc conflict found.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.discount_amount
  display_name: discount_amount
  column_name: discount_amount
  table_id: table.zs_observe.shopify_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Discount applied
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Extended Client Tables field documented as numeric; no dedicated-doc conflict found.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.refunded_amount
  display_name: refunded_amount
  column_name: refunded_amount
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount refunded (0 for forward orders)
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Client Tables source type=numeric; Dedicated Shopify OMS doc declares varchar; prefer refunded_amount over refunded_amount_1
    and cast for aggregation.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.payment_mode
  display_name: payment_mode
  column_name: payment_mode
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`cash_on_delivery`, `prepaid`, etc.'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.payment_method
  display_name: payment_method
  column_name: payment_method
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Detailed payment method string
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.payment_id
  display_name: payment_id
  column_name: payment_id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: PG payment reference number
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.payment_references
  display_name: payment_references
  column_name: payment_references
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: All payment references (can be multiple for partial)
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.destination_city
  display_name: destination_city
  column_name: destination_city
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Shipping city
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.destination_zipcode
  display_name: destination_zipcode
  column_name: destination_zipcode
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Shipping pincode
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.shipping_province
  display_name: shipping_province
  column_name: shipping_province
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Shipping state code
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tags_1
  display_name: tags_1
  column_name: tags_1
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Shopify order tags (CPD, GoKwik, Fastrr, etc.)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.vendor
  display_name: vendor
  column_name: vendor
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Product vendor
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.source
  display_name: source
  column_name: source
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Shopify channel source ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_1_name
  display_name: tax_1_name
  column_name: tax_1_name
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Tax component name (e.g. `IGST 18%`)
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_1_value
  display_name: tax_1_value
  column_name: tax_1_value
  table_id: table.zs_observe.shopify_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount of tax component 1
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.risk_level
  display_name: risk_level
  column_name: risk_level
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Shopify fraud risk (Low/Medium/High)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.fulfilled_at
  display_name: fulfilled_at
  column_name: fulfilled_at
  table_id: table.zs_observe.shopify_oms
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: Fulfillment timestamp
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.note_attributes
  display_name: note_attributes
  column_name: note_attributes
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Shopify order notes (contains cart tokens, UTM params)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.outstanding_balance
  display_name: outstanding_balance
  column_name: outstanding_balance
  table_id: table.zs_observe.shopify_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount still owed (for COD + partial pay)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_oms.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  type_resolution_notes:
  - Extended Client Tables field documented as numeric; no dedicated-doc conflict found.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.shopify_returns
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.shopify_returns
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.shopify_returns
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.shopify_returns
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.shopify_returns
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.shopify_returns
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.shopify_returns
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.shopify_returns
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.shopify_returns
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: Currency (GBP for UK Shopify stores)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.order_name
  display_name: order_name
  column_name: order_name
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Original order name (e.g. `EUK55773`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.transaction_id
  display_name: transaction_id
  column_name: transaction_id
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Shopify's refund transaction ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.payment_gateway
  display_name: payment_gateway
  column_name: payment_gateway
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Gateway used for refund (`shopify_payments`, `paypal`, `razorpay`)
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.transaction_status
  display_name: transaction_status
  column_name: transaction_status
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`success`, `pending`, `failure`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.order_payment_status
  display_name: order_payment_status
  column_name: order_payment_status
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Final payment status (`paid`, `refunded`, `partially_refunded`)
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.refunded_payments
  display_name: refunded_payments
  column_name: refunded_payments
  table_id: table.zs_observe.shopify_returns
  data_type: numeric
  source_declared_type: numeric
  semantic_role: source_attribute
  description: Total amount refunded
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.customer_added_date
  display_name: customer_added_date
  column_name: customer_added_date
  table_id: table.zs_observe.shopify_returns
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Original order date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_returns.other_id
  display_name: other_id
  column_name: other_id
  table_id: table.zs_observe.shopify_returns
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Return/refund reference ID from gateway
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.shopify_returns.001
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.woohoo_oms
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.woohoo_oms
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.woohoo_oms
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.woohoo_oms
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.woohoo_oms
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.woohoo_oms
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: ISO/source currency code.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Amazon order ID (e.g. `171-7101621-1207520`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.parent_id
  display_name: parent_id
  column_name: parent_id
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Same as order_id (parent reference)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.refno
  display_name: refno
  column_name: refno
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Woohoo reference number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.ordernumber
  display_name: ordernumber
  column_name: ordernumber
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Order number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.store_name
  display_name: store_name
  column_name: store_name
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source store (e.g. `Amazon 3PD Integration API Amazon 3PD Store`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.orderstatus
  display_name: orderstatus
  column_name: orderstatus
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: '`complete`, `pending`, `cancelled`, `failed`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`complete`, `cancelled`, etc.'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.woohoo_oms
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Order date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.invoice_date
  display_name: invoice_date
  column_name: invoice_date
  table_id: table.zs_observe.woohoo_oms
  data_type: date
  source_declared_type: date
  semantic_role: invoice_identifier
  description: Invoice date for the gift card
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.file_date
  display_name: file_date
  column_name: file_date
  table_id: table.zs_observe.woohoo_oms
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Date of the source file
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.file_date_dt
  display_name: file_date_dt
  column_name: file_date_dt
  table_id: table.zs_observe.woohoo_oms
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: File date as datetime
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.closed_date
  display_name: closed_date
  column_name: closed_date
  table_id: table.zs_observe.woohoo_oms
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: When the order was closed/completed
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.couriername
  display_name: couriername
  column_name: couriername
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: shipment_reference
  description: Delivery method (`Email` = digital delivery)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.cardloadamount
  display_name: cardloadamount
  column_name: cardloadamount
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Face value loaded on the gift card
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount charged to the buyer
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.mrp
  display_name: mrp
  column_name: mrp
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: MRP of the gift card
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.adjustment_amount
  display_name: adjustment_amount
  column_name: adjustment_amount
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Any adjustments to the order
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.topup_amount
  display_name: topup_amount
  column_name: topup_amount
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Wallet top-up amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.discount_amount
  display_name: discount_amount
  column_name: discount_amount
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Discount applied
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.reward_amount
  display_name: reward_amount
  column_name: reward_amount
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Reward/loyalty points used
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.handling_charge
  display_name: handling_charge
  column_name: handling_charge
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Handling charges
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.brand_discount
  display_name: brand_discount
  column_name: brand_discount
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Brand-sponsored discount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.qc_discount
  display_name: qc_discount
  column_name: qc_discount
  table_id: table.zs_observe.woohoo_oms
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Qwikcilver/Woohoo discount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.store_id
  display_name: store_id
  column_name: store_id
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Woohoo store identifier
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.po_number
  display_name: po_number
  column_name: po_number
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Purchase Order number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.payment_mode
  display_name: payment_mode
  column_name: payment_mode
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Payment method used
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.metadata_2
  display_name: metadata_2
  column_name: metadata_2
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Integration label (e.g. `amazon nab`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.woohoo_oms.file_name
  display_name: file_name
  column_name: file_name
  table_id: table.zs_observe.woohoo_oms
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source file name (e.g. `Woohoo Amazon NAB Outstanding 2025_04_01.csv`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.woohoo_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.amazon_seller_flex
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.amazon_seller_flex
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.amazon_seller_flex
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.amazon_seller_flex
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.amazon_seller_flex
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.amazon_seller_flex
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: '`INR`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.invoicenumber
  display_name: invoicenumber
  column_name: invoicenumber
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Amazon order/invoice number (e.g. `171-1357218-0333933`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Same as invoice number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`GIFT CARD ACTIVATE`, `GIFT CARD DEACTIVATE`, `GIFT CARD CANCEL`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.transactiondate
  display_name: transactiondate
  column_name: transactiondate
  table_id: table.zs_observe.amazon_seller_flex
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Date of activation
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.transactiontime
  display_name: transactiontime
  column_name: transactiontime
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: date_or_timestamp
  description: Time of activation
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.amount
  display_name: amount
  column_name: amount
  table_id: table.zs_observe.amazon_seller_flex
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Face value of the gift card activated
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.totalamount
  display_name: totalamount
  column_name: totalamount
  table_id: table.zs_observe.amazon_seller_flex
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total amount (should match `amount`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.amazon_seller_flex
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Same as amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.brand
  display_name: brand
  column_name: brand
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Brand name (e.g. `World Of Titan`, `Helios`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Program group / product category
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.productname
  display_name: productname
  column_name: productname
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Full product name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.programgroup
  display_name: programgroup
  column_name: programgroup
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Gift card program (e.g. `WOT B2C eGift Cards`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.merchant
  display_name: merchant
  column_name: merchant
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Always `Amazon`
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.outlet
  display_name: outlet
  column_name: outlet
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`Amazon.in`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.posname
  display_name: posname
  column_name: posname
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Point-of-sale name (`Amazon-POS-22`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.remarks
  display_name: remarks
  column_name: remarks
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`Seller Flex EGV` = Electronic Gift Voucher via Seller Flex'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.responsemessage
  display_name: responsemessage
  column_name: responsemessage
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`Transaction successful.`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.metadata
  display_name: metadata
  column_name: metadata
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: Outlet name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.metadata_2
  display_name: metadata_2
  column_name: metadata_2
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Channel label (`seller flex`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.amazondiscount
  display_name: amazondiscount
  column_name: amazondiscount
  table_id: table.zs_observe.amazon_seller_flex
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amazon-applied discount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.discountadjustment
  display_name: discountadjustment
  column_name: discountadjustment
  table_id: table.zs_observe.amazon_seller_flex
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Discount adjustment
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.qcdiscount
  display_name: qcdiscount
  column_name: qcdiscount
  table_id: table.zs_observe.amazon_seller_flex
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Qwikcilver discount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.storedvaluerspoints
  display_name: storedvaluerspoints
  column_name: storedvaluerspoints
  table_id: table.zs_observe.amazon_seller_flex
  data_type: numeric
  source_declared_type: numeric
  semantic_role: source_attribute
  description: Stored value points
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.pretransactioncardbalance
  display_name: pretransactioncardbalance
  column_name: pretransactioncardbalance
  table_id: table.zs_observe.amazon_seller_flex
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Pre-existing card balance (0 = new activation)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.parentcardnumber
  display_name: parentcardnumber
  column_name: parentcardnumber
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Parent card if it's a derivative card
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.cardnumber
  display_name: cardnumber
  column_name: cardnumber
  table_id: table.zs_observe.amazon_seller_flex
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Physical/virtual card number (usually null for eGV)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_seller_flex.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.amazon_seller_flex
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Date of the record
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_seller_flex.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: Null (using INR by default)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.settlement_id
  display_name: settlement_id
  column_name: settlement_id
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Amazon's settlement batch identifier
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.settlement_date
  display_name: settlement_date
  column_name: settlement_date
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: Date of settlement
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: Transaction/order date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Amazon order ID (e.g. `403-6612367-5153132`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.item_id
  display_name: item_id
  column_name: item_id
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Amazon order item ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.sku_id
  display_name: sku_id
  column_name: sku_id
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product ASIN/SKU
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.other_id
  display_name: other_id
  column_name: other_id
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Settlement line item reference
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.metadata
  display_name: metadata
  column_name: metadata
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: status_or_classifier
  description: Order creation timestamp
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.metadata_2
  display_name: metadata_2
  column_name: metadata_2
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: source_attribute
  description: Settlement posting timestamp
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.metadata_3
  display_name: metadata_3
  column_name: metadata_3
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Marketplace (`amazon_in`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`Order`, `Refund`, `Adjustment`, `FBAFee`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.quantity
  display_name: quantity
  column_name: quantity
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: integer
  source_declared_type: integer
  semantic_role: source_attribute
  description: Number of units
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.fulfillment_channel
  display_name: fulfillment_channel
  column_name: fulfillment_channel
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`MFN` (Merchant Fulfilled) or `AFN` (Amazon Fulfilled)'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.charged_amount_type
  display_name: charged_amount_type
  column_name: charged_amount_type
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: '`Principal` (the price charged to buyer)'
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Principal amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.item_fee_type
  display_name: item_fee_type
  column_name: item_fee_type
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: '`Commission`, `FBAFee`, `ShippingChargeback`'
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.item_fee_amount
  display_name: item_fee_amount
  column_name: item_fee_amount
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Fee amount (negative = deduction)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.item_fee_tax
  display_name: item_fee_tax
  column_name: item_fee_tax
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: GST on the fee (negative)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.total_tcs_amount
  display_name: total_tcs_amount
  column_name: total_tcs_amount
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total TCS deducted by Amazon
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.total_tds_amount
  display_name: total_tds_amount
  column_name: total_tds_amount
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total TDS deducted by Amazon
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.other_transaction_fee_type
  display_name: other_transaction_fee_type
  column_name: other_transaction_fee_type
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Other fee category
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.other_transaction_fees
  display_name: other_transaction_fees
  column_name: other_transaction_fees
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Other miscellaneous fees
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.reimbursement_charges
  display_name: reimbursement_charges
  column_name: reimbursement_charges
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amazon reimbursements (if any)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.reimbursement_type
  display_name: reimbursement_type
  column_name: reimbursement_type
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Type of reimbursement
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.shipment_fee_amount
  display_name: shipment_fee_amount
  column_name: shipment_fee_amount
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Shipping fee charged/credited
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.shipment_fee_type
  display_name: shipment_fee_type
  column_name: shipment_fee_type
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Type of shipment fee
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_gc_settlement.settled_amount
  display_name: settled_amount
  column_name: settled_amount
  table_id: table.zs_observe.amazon_gc_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Net amount after all deductions
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: '`INR`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: 'Gullak''s order reference (HUBL format: `HUBL_01JW...`)'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.parent_id
  display_name: parent_id
  column_name: parent_id
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Qwikcilver's API order ID (APIP format)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.brand
  display_name: brand
  column_name: brand
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Gift card brand (EatSure, BookMyShow, etc.)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.brand_name
  display_name: brand_name
  column_name: brand_name
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Same as brand
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.order_reference_number
  display_name: order_reference_number
  column_name: order_reference_number
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Gullak's order reference
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.qc__pl_order_id
  display_name: qc__pl_order_id
  column_name: qc__pl_order_id
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Qwikcilver/Pine Labs order ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.settlement_date
  display_name: settlement_date
  column_name: settlement_date
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: Date Gullak settled payment to Qwikcilver
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.settled_date
  display_name: settled_date
  column_name: settled_date
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Settlement date (clean date version)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.transaction_date
  display_name: transaction_date
  column_name: transaction_date
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: Original order/transaction date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Order creation date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Face value of the gift card
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.settled_amount
  display_name: settled_amount
  column_name: settled_amount
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount settled (usually = charged_amount for full settlement)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.utr_number
  display_name: utr_number
  column_name: utr_number
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Unique Transaction Reference (bank UTR for NEFT/RTGS/IMPS transfer)
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.gullak_technologies_settlement.settlement_id
  display_name: settlement_id
  column_name: settlement_id
  table_id: table.zs_observe.gullak_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Same as UTR number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.gullak_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.pinelabs_soa
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.pinelabs_soa
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.pinelabs_soa
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.pinelabs_soa
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.pinelabs_soa
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.pinelabs_soa
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: ISO/source currency code.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Transaction/invoice reference number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.transaction_no
  display_name: transaction_no
  column_name: transaction_no
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Oracle AR transaction number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`Invoice`, `Debit Memo`, `Credit Memo`, `Payment`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.transaction_class
  display_name: transaction_class
  column_name: transaction_class
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Same as transaction_type
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.transaction_date
  display_name: transaction_date
  column_name: transaction_date
  table_id: table.zs_observe.pinelabs_soa
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: Date of the transaction
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.gl_date
  display_name: gl_date
  column_name: gl_date
  table_id: table.zs_observe.pinelabs_soa
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: General Ledger posting date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.due_date
  display_name: due_date
  column_name: due_date
  table_id: table.zs_observe.pinelabs_soa
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Payment due date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.item_id
  display_name: item_id
  column_name: item_id
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Document number (internal reference)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.document_no
  display_name: document_no
  column_name: document_no
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: invoice_identifier
  description: Oracle document number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.invoice_number
  display_name: invoice_number
  column_name: invoice_number
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: invoice_identifier
  description: Tax invoice number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.tax_invoice_number
  display_name: tax_invoice_number
  column_name: tax_invoice_number
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: invoice_identifier
  description: GST invoice number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Invoice line description
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.invoice_description
  display_name: invoice_description
  column_name: invoice_description
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: invoice_identifier
  description: Full description of the charge
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.customer_name
  display_name: customer_name
  column_name: customer_name
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: customer_attribute
  description: Enterprise client name (e.g. `PhonePe Private Limited`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.customer_number
  display_name: customer_number
  column_name: customer_number
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: customer_attribute
  description: Customer code in Pine Labs system
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.customer_account
  display_name: customer_account
  column_name: customer_account
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: customer_attribute
  description: Customer account name/entity
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.customer_account_number
  display_name: customer_account_number
  column_name: customer_account_number
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: customer_attribute
  description: Account number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.total_amount
  display_name: total_amount
  column_name: total_amount
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Invoice total amount
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Amount charged
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.tax_amount
  display_name: tax_amount
  column_name: tax_amount
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Tax amount
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.payment_amount
  display_name: payment_amount
  column_name: payment_amount
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Payment received amount
  cast_required: true
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.closing_balance
  display_name: closing_balance
  column_name: closing_balance
  table_id: table.zs_observe.pinelabs_soa
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Outstanding balance after payments
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.conversion_rate
  display_name: conversion_rate
  column_name: conversion_rate
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: FX conversion rate
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.currency
  display_name: currency
  column_name: currency
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: Original currency
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.fc_amount
  display_name: fc_amount
  column_name: fc_amount
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Foreign currency amount
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.month
  display_name: month
  column_name: month
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Statement month (e.g. `Mar-21`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.event_month
  display_name: event_month
  column_name: event_month
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Same as month
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.mode_of_payment
  display_name: mode_of_payment
  column_name: mode_of_payment
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: NEFT, RTGS, IMPS, etc.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.po_number
  display_name: po_number
  column_name: po_number
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Purchase Order number from client
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.po_date
  display_name: po_date
  column_name: po_date
  table_id: table.zs_observe.pinelabs_soa
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: PO date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.business_vertical
  display_name: business_vertical
  column_name: business_vertical
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Business segment
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.sales_person
  display_name: sales_person
  column_name: sales_person
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Relationship manager
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.pinelabs_soa.sl_no
  display_name: sl_no
  column_name: sl_no
  table_id: table.zs_observe.pinelabs_soa
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Serial number in the statement
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: ISO/source currency code.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Paytm's order item ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.order_item_id
  display_name: order_item_id
  column_name: order_item_id
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Same as order_id
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.pg_utr
  display_name: pg_utr
  column_name: pg_utr
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Payment gateway UTR (bank transfer reference)
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.cod_utr
  display_name: cod_utr
  column_name: cod_utr
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: COD payment UTR (if applicable)
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.settlement_date
  display_name: settlement_date
  column_name: settlement_date
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Date of settlement
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`Payout Forward`, `Payout Reverse` (returns)'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.payment_type
  display_name: payment_type
  column_name: payment_type
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: Same as transaction_type
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.fulfillment_type
  display_name: fulfillment_type
  column_name: fulfillment_type
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`Dropship` = Qwikcilver fulfills directly'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.sku_name
  display_name: sku_name
  column_name: sku_name
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product name (e.g. `Spotify Premium 12 Months Subscription Gift Card`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.merchant_sku
  display_name: merchant_sku
  column_name: merchant_sku
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Qwikcilver's SKU code (e.g. `SPGV6934213`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: MRP / face value charged to buyer
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.amount_paid_by
  display_name: amount_paid_by
  column_name: amount_paid_by
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total amount paid by customer
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.amount_paid_by_p_g_mode
  display_name: amount_paid_by_p_g_mode
  column_name: amount_paid_by_p_g_mode
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount paid via PG (non-COD)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.amount_paid_by_c_o_d_mode
  display_name: amount_paid_by_c_o_d_mode
  column_name: amount_paid_by_c_o_d_mode
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount paid via COD
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.gross_commission
  display_name: gross_commission
  column_name: gross_commission
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Paytm's commission (negative = deduction)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.gross_commission_gst_amount
  display_name: gross_commission_gst_amount
  column_name: gross_commission_gst_amount
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: GST on commission (negative)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.total_taxes
  display_name: total_taxes
  column_name: total_taxes
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total tax deductions
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.settled_pg
  display_name: settled_pg
  column_name: settled_pg
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Net PG settlement amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.settled_cod
  display_name: settled_cod
  column_name: settled_cod
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Net COD settlement amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.settled_amount
  display_name: settled_amount
  column_name: settled_amount
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total net settled amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.marketplace_commission
  display_name: marketplace_commission
  column_name: marketplace_commission
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Marketplace commission (same as gross_commission)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.journey
  display_name: journey
  column_name: journey
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: Order journey (`Delivered`, `Returned`, `Cancelled`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.qty_ordered
  display_name: qty_ordered
  column_name: qty_ordered
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: integer
  source_declared_type: integer
  semantic_role: order_identifier
  description: Quantity ordered
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.order_created_at
  display_name: order_created_at
  column_name: order_created_at
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: order_identifier
  description: Order creation timestamp
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.payment_creation_date
  display_name: payment_creation_date
  column_name: payment_creation_date
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: Payment timestamp
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.mid
  display_name: mid
  column_name: mid
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Merchant ID on Paytm
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.wid
  display_name: wid
  column_name: wid
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Warehouse ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.product_id
  display_name: product_id
  column_name: product_id
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Paytm product catalog ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.shipping_zone
  display_name: shipping_zone
  column_name: shipping_zone
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Shipping zone information
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.forward_logistic_charges
  display_name: forward_logistic_charges
  column_name: forward_logistic_charges
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Forward logistics cost
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.reverse_logistic_charges
  display_name: reverse_logistic_charges
  column_name: reverse_logistic_charges
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Return logistics cost
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.paytm_giftcard_settlement.ondc_order_id
  display_name: ondc_order_id
  column_name: ondc_order_id
  table_id: table.zs_observe.paytm_giftcard_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: ONDC protocol order ID (if applicable)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.paytm_giftcard_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: ISO/source currency code.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.common_order_id
  display_name: common_order_id
  column_name: common_order_id
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Red Giraffe order ID (e.g. `REDG-2103030532`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Same as common_order_id
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.product_name
  display_name: product_name
  column_name: product_name
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Gift card product name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Same as product_name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.product_denomination
  display_name: product_denomination
  column_name: product_denomination
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Card denomination (face value)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.total_amount
  display_name: total_amount
  column_name: total_amount
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Face value of the card
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Same as total_amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.discount_percentage
  display_name: discount_percentage
  column_name: discount_percentage
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Discount % applied to face value (e.g. `18.75`)
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.settlement_amount
  display_name: settlement_amount
  column_name: settlement_amount
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Amount Red Giraffe pays = total_amount × (1 - discount%)
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.settled_amount
  display_name: settled_amount
  column_name: settled_amount
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Same as settlement_amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.mp_fees
  display_name: mp_fees
  column_name: mp_fees
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Qwikcilver's margin = charged_amount - settled_amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.utr_number
  display_name: utr_number
  column_name: utr_number
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Bank UTR for the settlement payment
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.settlement_id
  display_name: settlement_id
  column_name: settlement_id
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Same as UTR number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.order_date
  display_name: order_date
  column_name: order_date
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: When the order was placed
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Order date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.settlement_date
  display_name: settlement_date
  column_name: settlement_date
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Payment/settlement date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.quantity
  display_name: quantity
  column_name: quantity
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: integer
  source_declared_type: integer
  semantic_role: source_attribute
  description: Number of cards
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.red_giraffe_settlement.s_no
  display_name: s_no_
  column_name: s_no_
  table_id: table.zs_observe.red_giraffe_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Serial number in the settlement file
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.red_giraffe_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.nearby_marketplace
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.nearby_marketplace
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.nearby_marketplace
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.nearby_marketplace
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.nearby_marketplace
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.nearby_marketplace
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: ISO/source currency code.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Nearby's order reference or `adjustment_...` for adjustments
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.offer_id
  display_name: offer_id
  column_name: offer_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Nearby's offer/deal ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.offer_name
  display_name: offer_name
  column_name: offer_name
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Offer name (e.g. `Amazon Prime Voucher - 12months Membership`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.deal_id
  display_name: deal_id
  column_name: deal_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Deal identifier
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.deal_name
  display_name: deal_name
  column_name: deal_name
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Brand name for the deal
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Same as offer_name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.brand
  display_name: brand
  column_name: brand
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Brand name (e.g. `Amazon Prime Membership Voucher`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.voucher_code
  display_name: voucher_code
  column_name: voucher_code
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: The actual voucher/gift code issued (e.g. `NTTMZBA`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.transaction_id
  display_name: transaction_id
  column_name: transaction_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: UTR/bank transfer reference
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.settlement_id
  display_name: settlement_id
  column_name: settlement_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Same as transaction_id
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.settlement_date
  display_name: settlement_date
  column_name: settlement_date
  table_id: table.zs_observe.nearby_marketplace
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Date of settlement
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.merchant_share
  display_name: merchant_share
  column_name: merchant_share
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Net amount payable to Qwikcilver (can be negative for adjustments)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.net_payable_to_merchant
  display_name: net_payable_to_merchant
  column_name: net_payable_to_merchant
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Final net payable (same as merchant_share)
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.settled_amount
  display_name: settled_amount
  column_name: settled_amount
  table_id: table.zs_observe.nearby_marketplace
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Settlement amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.nearby_marketplace
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Face value of the voucher
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.mp_fees
  display_name: mp_fees
  column_name: mp_fees
  table_id: table.zs_observe.nearby_marketplace
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Nearby's commission
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.paid_date
  display_name: paid_date
  column_name: paid_date
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: date_or_timestamp
  description: Date payment was made
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.payment_initiated_on
  display_name: payment_initiated_on
  column_name: payment_initiated_on
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Date payment initiation
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.business_account_id
  display_name: business_account_id
  column_name: business_account_id
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Qwikcilver's account ID on Nearby
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.account_holder_name
  display_name: account_holder_name
  column_name: account_holder_name
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Bank account holder
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.bank_name
  display_name: bank_name
  column_name: bank_name
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Bank name (AXIS BANK)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.bank_a_c_number
  display_name: bank_a_c_number
  column_name: bank_a_c_number
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Bank account number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.ifsc_code
  display_name: ifsc_code
  column_name: ifsc_code
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: IFSC code
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.memo
  display_name: memo
  column_name: memo
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Transaction memo/reason
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.discount_by_merchant
  display_name: discount_by_merchant
  column_name: discount_by_merchant
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Merchant-provided discount
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.taxable_value_for_tcs
  display_name: taxable_value_for_tcs
  column_name: taxable_value_for_tcs
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: TCS-applicable value
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.tcs_deducted
  display_name: tcs_deducted
  column_name: tcs_deducted
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: TCS amount deducted
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.tds_deducted
  display_name: tds_deducted
  column_name: tds_deducted
  table_id: table.zs_observe.nearby_marketplace
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: TDS amount deducted
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.nearby_marketplace.redemption_date
  display_name: redemption_date
  column_name: redemption_date
  table_id: table.zs_observe.nearby_marketplace
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: When the voucher was redeemed
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.nearby_marketplace.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.astrotalk_oda
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.astrotalk_oda
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.astrotalk_oda
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`"astrotalk oda"`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.astrotalk_oda
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.astrotalk_oda
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.astrotalk_oda
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: ISO/source currency code.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.destination_pincode
  display_name: destination_pincode
  column_name: destination_pincode
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Pincode classified as ODA (e.g. `690504`, `601101`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.source_pincode
  display_name: source_pincode
  column_name: source_pincode
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Origin pincode (null = applies from all origins)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.source_code
  display_name: source_code
  column_name: source_code
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Courier source code
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.other_fee_type
  display_name: other_fee_type
  column_name: other_fee_type
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Always `ODA` — the fee category
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.logistic_partner
  display_name: logistic_partner
  column_name: logistic_partner
  table_id: table.zs_observe.astrotalk_oda
  data_type: varchar
  source_declared_type: varchar
  semantic_role: shipment_reference
  description: Courier partner (`yolojet`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.start_date
  display_name: start_date
  column_name: start_date
  table_id: table.zs_observe.astrotalk_oda
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: When this ODA classification became effective
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.astrotalk_oda.end_date
  display_name: end_date
  column_name: end_date
  table_id: table.zs_observe.astrotalk_oda
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: When it expires (null = still active)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.astrotalk_oda.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.first_pay_settlement
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.first_pay_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.first_pay_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.first_pay_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.first_pay_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.first_pay_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: '`INR`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: FirstPay's order number (e.g. `8581086`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.parent_id
  display_name: parent_id
  column_name: parent_id
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Order reference with prefix (`BRVC-8581086-14308525`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.order_reference_number
  display_name: order_reference_number
  column_name: order_reference_number
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Same as parent_id
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.order_no
  display_name: order_no
  column_name: order_no
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Numeric order number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.sku_id
  display_name: sku_id
  column_name: sku_id
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Qwikcilver's SKU code (e.g. `EGVGBFK001` = Flipkart GV)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.product_sku
  display_name: product_sku
  column_name: product_sku
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Same as sku_id
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.brand_name
  display_name: brand_name
  column_name: brand_name
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Gift card brand (Flipkart, PVR Cinemas, etc.)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.first_pay_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Face value of the gift card
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.settled_amount
  display_name: settled_amount
  column_name: settled_amount
  table_id: table.zs_observe.first_pay_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount settled (= charged_amount for this channel)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.first_pay_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Order date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.settlement_date
  display_name: settlement_date
  column_name: settlement_date
  table_id: table.zs_observe.first_pay_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Payment settlement date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.pre_discount_amount
  display_name: pre_discount_amount
  column_name: pre_discount_amount
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Face value before any discount
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.quantity
  display_name: quantity
  column_name: quantity
  table_id: table.zs_observe.first_pay_settlement
  data_type: integer
  source_declared_type: integer
  semantic_role: source_attribute
  description: Number of cards
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.s__no
  display_name: s__no
  column_name: s__no
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Serial number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.first_pay_settlement.settlement_id
  display_name: settlement_id
  column_name: settlement_id
  table_id: table.zs_observe.first_pay_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Settlement batch ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.first_pay_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: ISO/source currency code.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Jupiter/Amica's order reference (e.g. `JUPITER_67f9de47-5fe0-483`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.reference_number
  display_name: reference_number
  column_name: reference_number
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Same as order_id
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.parent_id
  display_name: parent_id
  column_name: parent_id
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Same as order_id
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.brand_name
  display_name: brand_name
  column_name: brand_name
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Gift card brand (Uber, Pizza Hut, etc.)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.brand
  display_name: brand
  column_name: brand
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Same as brand_name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.denomination
  display_name: denomination
  column_name: denomination
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Face value of the gift card
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.total_amount
  display_name: total_amount
  column_name: total_amount
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Face value
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Face value as numeric
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.commission
  display_name: commission
  column_name: commission
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Jupiter's commission amount
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.mp_fees
  display_name: mp_fees
  column_name: mp_fees
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Commission as numeric
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.gst
  display_name: gst
  column_name: gst
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: tax_attribute
  description: GST on commission
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.mp_fees_gst_amount
  display_name: mp_fees_gst_amount
  column_name: mp_fees_gst_amount
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: GST on commission as numeric
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.payable_to_qwikcilver
  display_name: payable_to_qwikcilver
  column_name: payable_to_qwikcilver
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: financial_amount
  description: Net amount after deducting commission + GST
  cast_required: true
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.settled_amount
  display_name: settled_amount
  column_name: settled_amount
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Net settlement amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.utr_number
  display_name: utr_number
  column_name: utr_number
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Bank UTR for the settlement
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.settlement_id
  display_name: settlement_id
  column_name: settlement_id
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Same as UTR
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.date_of_transaction
  display_name: date_of_transaction
  column_name: date_of_transaction
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: Transaction date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Order date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.settlement_date
  display_name: settlement_date
  column_name: settlement_date
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Settlement date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.quantity
  display_name: quantity
  column_name: quantity
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: integer
  source_declared_type: integer
  semantic_role: source_attribute
  description: Number of cards
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amica_technologies_settlement.comments
  display_name: comments
  column_name: comments
  table_id: table.zs_observe.amica_technologies_settlement
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Additional notes
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.amica_technologies_settlement.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: ISO/source currency code.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: AZA's order number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_wallet_ledger.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.item_id
  display_name: item_id
  column_name: item_id
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Sub-order/item ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_wallet_ledger.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount credited/debited to wallet
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_wallet_ledger.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`Credited` (refund to wallet) or `Debited` (wallet used for payment)'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_wallet_ledger.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: 'Transaction narrative (e.g. `Re-add wallet Rs. 999 used in Order #734916...`)'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_wallet_ledger.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_wallet_ledger.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.aza_wallet_ledger
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: date_or_timestamp
  description: When the wallet transaction occurred
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_wallet_ledger.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.aza_return_dump
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.aza_return_dump
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.aza_return_dump
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.aza_return_dump
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.aza_return_dump
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.aza_return_dump
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: '`INR`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: AZA's order number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.item_id
  display_name: item_id
  column_name: item_id
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Sub-order/line item ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.sku_id
  display_name: sku_id
  column_name: sku_id
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product SKU
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.aza_return_dump
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Return initiation date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`RETURNED`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.quantity
  display_name: quantity
  column_name: quantity
  table_id: table.zs_observe.aza_return_dump
  data_type: integer
  source_declared_type: integer
  semantic_role: source_attribute
  description: Quantity being returned
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.destination_state
  display_name: destination_state
  column_name: destination_state
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: 'Customer''s state (for US: `New York`)'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.destintion_country
  display_name: destintion_country
  column_name: destintion_country
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Customer's country
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.destination_zipcode
  display_name: destination_zipcode
  column_name: destination_zipcode
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Customer's zipcode
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.mrp
  display_name: mrp
  column_name: mrp
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Product MRP
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount the customer paid
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.total_tax_perc
  display_name: total_tax_perc
  column_name: total_tax_perc
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Tax percentage
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.total_tax
  display_name: total_tax
  column_name: total_tax
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Tax amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.shipping_amount
  display_name: shipping_amount
  column_name: shipping_amount
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Shipping cost (can be large for international)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.courier_partner
  display_name: courier_partner
  column_name: courier_partner
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: shipment_reference
  description: Return courier (Bluecard, Bhavani Courier, etc.)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.return_awb_number
  display_name: return_awb_number
  column_name: return_awb_number
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: shipment_reference
  description: Return tracking number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.payment_method
  display_name: payment_method
  column_name: payment_method
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`OTHER`, `UPI`, `CARD`, etc.'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.payment_mode
  display_name: payment_mode
  column_name: payment_mode
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`aza wallet - completely`, `payu`, `COD`, etc.'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.discount_amount
  display_name: discount_amount
  column_name: discount_amount
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Discount that was applied
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.subtotal
  display_name: subtotal
  column_name: subtotal
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Sub-total charged
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.promo_discount
  display_name: promo_discount
  column_name: promo_discount
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Promotional discount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.loyaltybyproduct
  display_name: loyaltybyproduct
  column_name: loyaltybyproduct
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: product_attribute
  description: Loyalty points used
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.aza_cashback
  display_name: aza_cashback
  column_name: aza_cashback
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: source_attribute
  description: AZA cashback applied
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.subtotal_suborder_level
  display_name: subtotal_suborder_level
  column_name: subtotal_suborder_level
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: order_identifier
  description: Item-level subtotal
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.measuring_kit_charges
  display_name: measuring_kit_charges
  column_name: measuring_kit_charges
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Measurement kit charges (for fashion)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.currency_rate
  display_name: currency_rate
  column_name: currency_rate
  table_id: table.zs_observe.aza_return_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: currency
  description: Exchange rate (1.0 for INR, 85 for USD-INR)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_return_dump.other_id___other_id_2
  display_name: other_id / other_id_2
  column_name: other_id / other_id_2
  table_id: table.zs_observe.aza_return_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Additional reference IDs
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_return_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Tenant/scope identifier; column only, never create tenant/group card.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Alias for group_id in some tables; column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar_or_integer
  source_declared_type: varchar_or_integer
  semantic_role: scope_identifier
  description: Sub-entity/file-type identifier; scope filter column only.
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Hierarchical source path in ZenStatement ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.file_uuid
  display_name: file_uuid
  column_name: file_uuid
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Source file UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: ZenStatement generated transaction UUID.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Deduplication key made from business-meaningful fields.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.aza_sales_dump
  data_type: boolean
  source_declared_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag; use is_active = true where available.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.aza_sales_dump
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Duplicate-row flag generated by ingestion.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.is_active_false_reason
  display_name: is_active_false_reason
  column_name: is_active_false_reason
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason row was deactivated.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.aza_sales_dump
  data_type: boolean_or_varchar
  source_declared_type: boolean_or_varchar
  semantic_role: quality_filter
  description: ZenStatement processing status.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.zen_status_false_reason
  display_name: zen_status_false_reason
  column_name: zen_status_false_reason
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: quality_filter
  description: Reason for zen_status=false.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Source Excel/CSV sheet tab name.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.created_at
  display_name: created_at
  column_name: created_at
  table_id: table.zs_observe.aza_sales_dump
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline creation timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.updated_at
  display_name: updated_at
  column_name: updated_at
  table_id: table.zs_observe.aza_sales_dump
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: ZenStatement pipeline update timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.deleted_at
  display_name: deleted_at
  column_name: deleted_at
  table_id: table.zs_observe.aza_sales_dump
  data_type: timestamp
  source_declared_type: timestamp
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.post_process_file_uuid_ls
  display_name: post_process_file_uuid_ls
  column_name: post_process_file_uuid_ls
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: system_identifier
  description: Downstream file UUID list after post-processing.
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_tables.platform.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: currency
  description: '`INR`'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: AZA's master order number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.item_id
  display_name: item_id
  column_name: item_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: order_identifier
  description: Sub-order/line item ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.sku_id
  display_name: sku_id
  column_name: sku_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product SKU
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product name
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.category
  display_name: category
  column_name: category
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Product category (Women, Jewellery, Men)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.sub_category
  display_name: sub_category
  column_name: sub_category
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Sub-category (Tops, Bangles, Blouses)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.sub_category_name
  display_name: sub_category_name
  column_name: sub_category_name
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: product_attribute
  description: Detailed sub-category
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.aza_sales_dump
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Order placement date
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.order_shipped_date
  display_name: order_shipped_date
  column_name: order_shipped_date
  table_id: table.zs_observe.aza_sales_dump
  data_type: date
  source_declared_type: date
  semantic_role: date_or_timestamp
  description: Date item was shipped
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.final_status
  display_name: final_status
  column_name: final_status
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: Final order status
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.current_ship_status
  display_name: current_ship_status
  column_name: current_ship_status
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: Current shipping status (`DELIVERED`, `PICKED FROM BIN`, etc.)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.source_state
  display_name: source_state
  column_name: source_state
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Warehouse/dispatch state
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.source_country
  display_name: source_country
  column_name: source_country
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: geography_or_logistics_attribute
  description: Dispatch country (`India`)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Amount charged to customer
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.subtotal
  display_name: subtotal
  column_name: subtotal
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Sub-total before wallet/promo
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.shipping_amount
  display_name: shipping_amount
  column_name: shipping_amount
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Shipping charges
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.item_promo_discount
  display_name: item_promo_discount
  column_name: item_promo_discount
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Promotional discount per item
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.total_promo_discount
  display_name: total_promo_discount
  column_name: total_promo_discount
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Total promotional discount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.payment_method
  display_name: payment_method
  column_name: payment_method
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: '`UPI`, `CARD`, `OTHER`, `NET_BANKING`'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.payment_mode
  display_name: payment_mode
  column_name: payment_mode
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: 'Gateway used: `payu`, `aza wallet - completely`, `COD`'
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.transaction_id
  display_name: transaction_id
  column_name: transaction_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: Payment transaction ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.payment_id
  display_name: payment_id
  column_name: payment_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: payment_or_settlement_reference
  description: PG payment reference
  cast_required: false
  scope_guardrail: column_only_not_account_card
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.other_id
  display_name: other_id
  column_name: other_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Alternative reference
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.other_id_2
  display_name: other_id_2
  column_name: other_id_2
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: source_attribute
  description: Additional reference
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.courier_partner
  display_name: courier_partner
  column_name: courier_partner
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: shipment_reference
  description: Courier company (DTDC, Shiprocket, BlueDart)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.forward_awb_number
  display_name: forward_awb_number
  column_name: forward_awb_number
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: shipment_reference
  description: Shipment tracking number
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.ship_tracking_id
  display_name: ship_tracking_id
  column_name: ship_tracking_id
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: shipment_reference
  description: Tracking ID
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.weight
  display_name: weight
  column_name: weight
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: source_attribute
  description: Item weight in grams
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.measurement_kit_price
  display_name: measurement_kit_price
  column_name: measurement_kit_price
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Price of measuring kit (if ordered)
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.walletbyproduct
  display_name: walletbyproduct
  column_name: walletbyproduct
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: product_attribute
  description: Wallet amount used for this item
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.loyaltybyproduct
  display_name: loyaltybyproduct
  column_name: loyaltybyproduct
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: product_attribute
  description: Loyalty points redeemed
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.aza_cashback
  display_name: aza_cashback
  column_name: aza_cashback
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: source_attribute
  description: AZA cashback earned
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.emi_discount
  display_name: emi_discount
  column_name: emi_discount
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: EMI discount applied
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.currency_rate
  display_name: currency_rate
  column_name: currency_rate
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: currency
  description: Exchange rate
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.internal_txn_type
  display_name: internal_txn_type
  column_name: internal_txn_type
  table_id: table.zs_observe.aza_sales_dump
  data_type: varchar
  source_declared_type: varchar
  semantic_role: status_or_classifier
  description: '`sales`, `exchange`, etc.'
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.taxbyproduct
  display_name: taxbyproduct
  column_name: taxbyproduct
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Tax per product
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.shipping_charge_by_product
  display_name: shipping_charge_by_product
  column_name: shipping_charge_by_product
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Per-product shipping contribution
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.customization_charges
  display_name: customization_charges
  column_name: customization_charges
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Custom tailoring charges
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.aza_sales_dump.partial_paid_amount
  display_name: partial_paid_amount
  column_name: partial_paid_amount
  table_id: table.zs_observe.aza_sales_dump
  data_type: numeric
  source_declared_type: numeric
  semantic_role: financial_amount
  description: Partial payment amount
  cast_required: false
  scope_guardrail: source_column
  evidence_refs:
  - ev.shopify.client_table.aza_sales_dump.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_oms.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.shiprocket_oms
  data_type: varchar
  semantic_role: order_identifier
  description: Shiprocket order id that may include Shopify order suffix -s{id}.
  cast_required: false
  scope_guardrail: reference_only_not_courier_account
  evidence_refs:
  - ev.shopify.dedicated_oms.shiprocket.001
  confidence: medium
  review_status: accepted_as_reference_only
  create_action: create_reference_only
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_oms.awb_code
  display_name: awb_code
  column_name: awb_code
  table_id: table.zs_observe.shiprocket_oms
  data_type: varchar
  semantic_role: shipment_reference
  description: Shipment AWB tracking code.
  cast_required: false
  scope_guardrail: reference_only_not_courier_account
  evidence_refs:
  - ev.shopify.dedicated_oms.shiprocket.001
  confidence: medium
  review_status: accepted_as_reference_only
  create_action: create_reference_only
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_oms.courier_company
  display_name: courier_company
  column_name: courier_company
  table_id: table.zs_observe.shiprocket_oms
  data_type: varchar
  semantic_role: shipment_reference
  description: Courier company label.
  cast_required: false
  scope_guardrail: reference_only_not_courier_account
  evidence_refs:
  - ev.shopify.dedicated_oms.shiprocket.001
  confidence: medium
  review_status: accepted_as_reference_only
  create_action: create_reference_only
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_oms.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.shiprocket_oms
  data_type: boolean
  semantic_role: quality_filter
  description: Active-row quality flag.
  cast_required: false
  scope_guardrail: reference_only_not_courier_account
  evidence_refs:
  - ev.shopify.dedicated_oms.shiprocket.001
  confidence: medium
  review_status: accepted_as_reference_only
  create_action: create_reference_only
```
### 4.x value_profile

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.financial_status
  display_name: Shopify financial_status payment classifier
  table_id: table.zs_observe.shopify_oms
  column_names:
  - financial_status
  values:
  - value: paid
    meaning: Prepaid / digital payment collected
  - value: pending
    meaning: COD cash not yet collected/remitted
  - value: partially_paid
    meaning: PPCOD partial prepaid + balance COD
  - value: voided
    meaning: Cancelled before shipment
  - value: refunded
    meaning: Refunded payment state where present
  parser_instruction: Do not create process variants from financial_status values alone.
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.client_tables.core_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.transaction_type
  display_name: Shopify transaction_type lifecycle values
  table_id: table.zs_observe.shopify_oms
  column_names:
  - transaction_type
  values:
  - value: fulfilled
    meaning: Order shipped and fulfilled
  - value: pending
    meaning: Order placed, not yet shipped
  - value: partial
    meaning: Multi-line order partly fulfilled
  - value: cancelled
    meaning: Cancelled order where present
  - value: refunded
    meaning: Refunded state where present
  parser_instruction: Use as fulfillment lifecycle value profile, not as material process variant.
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.client_tables.core_oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.payment_mode
  display_name: Shopify payment_mode observed values
  table_id: table.zs_observe.shopify_oms
  column_names:
  - payment_mode
  values:
  - value: cash_on_delivery
    meaning: COD collection/remittance expected after delivery
  - value: Gokwik UPI
    meaning: GoKwik UPI prepaid checkout label
  - value: Gokwik PPCOD
    meaning: GoKwik partial prepaid + COD label
  - value: Gokwik Cards
    meaning: GoKwik card checkout label
  parser_instruction: Gateway labels remain values/columns, not payment-gateway account cards.
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify_returns.status
  display_name: Shopify return/refund status values
  table_id: table.zs_observe.shopify_returns
  column_names:
  - transaction_status
  - order_payment_status
  values:
  - transaction_status: success
    meaning: Refund transaction succeeded
  - transaction_status: pending
    meaning: Refund transaction pending
  - transaction_status: failure
    meaning: Refund transaction failed
  - order_payment_status: refunded
    meaning: Order fully refunded
  - order_payment_status: partially_refunded
    meaning: Order partially refunded
  evidence_refs:
  - ev.shopify.client_tables.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.client_tables.group_id_observed_values
  display_name: Client Tables observed group_id values
  table_id: table.zs_observe.shopify_oms
  column_names:
  - group_id
  - tenant_id
  documented_scope_values:
  - value: 8
    meaning: Shopify brands such as Botanic Hearth and HighStar
  - value: 45
    meaning: European Shopify store with EUK/GBP context
  - value: 2
    meaning: MPL wallet transactions
  - value: 56
    meaning: AZA Fashions
  - value: 391
    meaning: Qwikcilver / Pine Labs gift-card business
  parser_instruction: These are scope values only. Do not create tenant/group/platform_account cards.
  evidence_refs:
  - ev.shopify.client_tables.group_scope.001
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.configured_settlement.utr_keys
  display_name: Configured settlement UTR/reference keys
  table_id: table.zs_observe.paytm_giftcard_settlement
  column_names:
  - utr_number
  - settlement_id
  - pg_utr
  - cod_utr
  - payment_id
  - transaction_id
  profile_scope: Bank/PG matching references across configured adjacent settlement/order tables.
  known_reference_columns_by_table:
    gullak_technologies_settlement:
    - utr_number
    - settlement_id
    paytm_giftcard_settlement:
    - pg_utr
    - cod_utr
    aza_sales_dump:
    - payment_id
    - transaction_id
    shopify_oms:
    - payment_id
    - payment_references
    shopify_returns:
    - transaction_id
    - other_id
  parser_instruction: Reference keys may support reconciliation but must not create bank or PG account cards.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x relationship

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shopify_oms_to_shopify_returns.order_reference
  display_name: shopify_oms to shopify_returns order reference
  from_table: table.zs_observe.shopify_oms
  to_table: table.zs_observe.shopify_returns
  join_keys:
  - shopify_oms.name = shopify_returns.order_name OR normalized shopify_oms.order_id = normalized shopify_returns.order_name
  relationship_grain: order/order_name to refund events
  join_safety_rule: 'Aggregate shopify_oms to order_id/name before joining to refund events; normalize # prefix and brand
    order-name formats at runtime.'
  evidence_refs:
  - ev.shopify.client_tables.returns.001
  - ev.shopify.client_tables.core_oms.001
  confidence: medium
  review_status: accepted_with_join_caveat
  create_action: create
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shopify_oms_to_shiprocket.order_suffix
  display_name: shopify_oms to shiprocket_oms order suffix
  from_table: table.zs_observe.shopify_oms
  to_table: table.zs_observe.shiprocket_oms
  join_keys:
  - shiprocket_oms.order_id LIKE CONCAT(shopify_oms.order_id, '-%')
  relationship_grain: Shopify order to shipment rows
  join_safety_rule: Apply is_active=true on both tables and aggregate Shopify order amounts before joining to multiple shipments.
  evidence_refs:
  - ev.shopify.dedicated_oms.shiprocket.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.amazon_seller_flex_to_amazon_gc_settlement.order_id
  display_name: amazon_seller_flex to amazon_gc_settlement activation settlement
  from_table: table.zs_observe.amazon_seller_flex
  to_table: table.zs_observe.amazon_gc_settlement
  join_keys:
  - order_id
  relationship_grain: gift card activation to settlement order row
  join_safety_rule: Filter amazon_seller_flex.transaction_type='GIFT CARD ACTIVATE' and amazon_gc_settlement.transaction_type='Order'
    for activation settlement checks.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  - ev.shopify.client_table.amazon_seller_flex.001
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: medium
  review_status: accepted_as_configured_adjacent
  create_action: create
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.woohoo_oms_to_amazon_gc_settlement.order_id
  display_name: woohoo_oms to amazon_gc_settlement order settlement
  from_table: table.zs_observe.woohoo_oms
  to_table: table.zs_observe.amazon_gc_settlement
  join_keys:
  - order_id
  relationship_grain: Woohoo completed order to Amazon settlement rows
  join_safety_rule: Use woohoo_oms.orderstatus='complete' for OMS expected side; aggregate settlement by order_id before comparison.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  - ev.shopify.client_table.woohoo_oms.001
  - ev.shopify.client_table.amazon_gc_settlement.001
  confidence: medium
  review_status: accepted_as_configured_adjacent
  create_action: create
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.mpl_deposit_to_pinelabs_soa.reference
  display_name: mpl_oms_deposit to pinelabs_soa PG reference
  from_table: table.zs_observe.mpl_oms_deposit
  to_table: table.zs_observe.pinelabs_soa
  join_keys:
  - mpl_oms_deposit.reference_id = pinelabs_soa.transaction_no
  relationship_grain: deposit transaction to PG/AR reference
  join_safety_rule: Only use when runtime configuration maps MPL deposits to PineLabs SOA/Razorpay settlement; filter successful
    deposits first.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  - ev.shopify.client_table.mpl_oms_deposit.001
  - ev.shopify.client_table.pinelabs_soa.001
  confidence: medium
  review_status: accepted_as_configured_adjacent
  create_action: create
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.aza_return_to_wallet.order_item
  display_name: aza_return_dump to aza_wallet_ledger order item refund
  from_table: table.zs_observe.aza_return_dump
  to_table: table.zs_observe.aza_wallet_ledger
  join_keys:
  - order_id
  - item_id
  relationship_grain: return item to wallet credit/debit entries
  join_safety_rule: Filter aza_return_dump.transaction_type='RETURNED' and aza_wallet_ledger.transaction_type='Credited' for
    refund-credit completeness.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  - ev.shopify.client_table.aza_return_dump.001
  - ev.shopify.client_table.aza_wallet_ledger.001
  confidence: medium
  review_status: accepted_as_configured_adjacent
  create_action: create
```
### 4.x metric

```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.order_count
  display_name: Shopify order count
  metric_key: shopify_order_count
  business_definition: Distinct Shopify orders in shopify_oms after active filter.
  default_grain: order
  colloquial_names:
  - order count
  - shopify_order_count
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.order_line_count
  display_name: Shopify order-line count
  metric_key: shopify_order_line_count
  business_definition: Line-item count in shopify_oms after active filter.
  default_grain: order_line
  colloquial_names:
  - order-line count
  - shopify_order_line_count
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.gross_gmv
  display_name: Shopify gross GMV
  metric_key: shopify_gross_gmv
  business_definition: Sum of Shopify charged_amount at source row/order-line grain; order-level GMV requires grouping by
    order_id.
  default_grain: order_or_order_line
  colloquial_names:
  - gross GMV
  - shopify_gross_gmv
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.aov
  display_name: Shopify AOV
  metric_key: shopify_aov
  business_definition: Gross GMV divided by distinct Shopify orders.
  default_grain: order
  colloquial_names:
  - AOV
  - shopify_aov
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.cod_order_count
  display_name: Shopify COD order count
  metric_key: shopify_cod_order_count
  business_definition: Distinct Shopify orders with financial_status='pending' or payment_mode='cash_on_delivery'.
  default_grain: order
  colloquial_names:
  - COD order count
  - shopify_cod_order_count
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.ppcod_order_count
  display_name: Shopify PPCOD order count
  metric_key: shopify_ppcod_order_count
  business_definition: Distinct Shopify orders with financial_status='partially_paid' or GoKwik PPCOD payment mode.
  default_grain: order
  colloquial_names:
  - PPCOD order count
  - shopify_ppcod_order_count
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.refunded_amount
  display_name: Shopify refunded amount
  metric_key: shopify_refunded_amount
  business_definition: Sum of refunded_amount in shopify_oms or refunded_payments in shopify_returns depending query context.
  default_grain: refund_event
  colloquial_names:
  - refunded amount
  - shopify_refunded_amount
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.tax_collected
  display_name: Shopify tax collected
  metric_key: shopify_tax_collected
  business_definition: Sum of Shopify total_tax or tax component values where present.
  default_grain: order_line
  colloquial_names:
  - tax collected
  - shopify_tax_collected
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.outstanding_balance
  display_name: Shopify outstanding COD/partial balance
  metric_key: shopify_outstanding_balance
  business_definition: Sum of outstanding_balance on COD or partially paid Shopify orders.
  default_grain: order_line
  colloquial_names:
  - outstanding COD/partial balance
  - shopify_outstanding_balance
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.refund_success_rate
  display_name: Shopify refund success rate
  metric_key: shopify_refund_success_rate
  business_definition: Successful refund events divided by all refund events in shopify_returns.
  default_grain: refund_event
  colloquial_names:
  - refund success rate
  - shopify_refund_success_rate
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.configured.settled_amount
  display_name: Configured adjacent settled amount
  metric_key: configured_settled_amount
  business_definition: Sum of settled_amount/payable/net settlement columns in configured settlement source tables.
  default_grain: settlement_line
  colloquial_names:
  - Configured adjacent settled amount
  - configured_settled_amount
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.configured.activation_settlement_gap
  display_name: Gift card activation settlement gap
  metric_key: activation_settlement_gap
  business_definition: Activation/order records missing corresponding settlement rows in configured gift-card flows.
  default_grain: order
  colloquial_names:
  - Gift card activation settlement gap
  - activation_settlement_gap
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.configured.wallet_refund_gap
  display_name: AZA wallet refund gap
  metric_key: wallet_refund_gap
  business_definition: Returned wallet-paid AZA items without corresponding Credited wallet ledger entry.
  default_grain: return_item
  colloquial_names:
  - AZA wallet refund gap
  - wallet_refund_gap
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
### 4.x metric_implementation

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.order_count
  display_name: order_count implementation
  metric_id: metric.shopify.order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.order_count
  sql_reference_id: sql.shopify.metric.order_count
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.order_line_count
  display_name: order_line_count implementation
  metric_id: metric.shopify.order_line_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.order_line_count
  sql_reference_id: sql.shopify.metric.order_line_count
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.gross_gmv
  display_name: gross_gmv implementation
  metric_id: metric.shopify.gross_gmv
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.gross_gmv
  sql_reference_id: sql.shopify.metric.gross_gmv
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.aov
  display_name: aov implementation
  metric_id: metric.shopify.aov
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.aov
  sql_reference_id: sql.shopify.metric.aov
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.cod_order_count
  display_name: cod_order_count implementation
  metric_id: metric.shopify.cod_order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.cod_order_count
  sql_reference_id: sql.shopify.metric.cod_order_count
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.ppcod_order_count
  display_name: ppcod_order_count implementation
  metric_id: metric.shopify.ppcod_order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.ppcod_order_count
  sql_reference_id: sql.shopify.metric.ppcod_order_count
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.refunded_amount
  display_name: refunded_amount implementation
  metric_id: metric.shopify.refunded_amount
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.refunded_amount
  sql_reference_id: sql.shopify.metric.refunded_amount
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.tax_collected
  display_name: tax_collected implementation
  metric_id: metric.shopify.tax_collected
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.tax_collected
  sql_reference_id: sql.shopify.metric.tax_collected
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.outstanding_balance
  display_name: outstanding_balance implementation
  metric_id: metric.shopify.outstanding_balance
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.outstanding_balance
  sql_reference_id: sql.shopify.metric.outstanding_balance
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.refund_success_rate
  display_name: refund_success_rate implementation
  metric_id: metric.shopify.refund_success_rate
  source_table_ids:
  - table.zs_observe.shopify_returns
  formula: See sql.shopify.metric.refund_success_rate
  sql_reference_id: sql.shopify.metric.refund_success_rate
  required_filters:
  - is_active = true
  - TRY_CAST string amount/date fields where source type is varchar
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  - ev.shopify.dedicated_oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.configured.settled_amount
  display_name: settled_amount implementation
  metric_id: metric.configured.settled_amount
  source_table_ids:
  - table.zs_observe.paytm_giftcard_settlement
  formula: See sql.configured.metric.settled_amount_paytm
  sql_reference_id: sql.configured.metric.settled_amount_paytm
  required_filters:
  - is_active = true
  - runtime configuration must include the adjacent table in the client workflow
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.configured.activation_settlement_gap
  display_name: activation_settlement_gap implementation
  metric_id: metric.configured.activation_settlement_gap
  source_table_ids:
  - table.zs_observe.amazon_seller_flex
  - table.zs_observe.amazon_gc_settlement
  formula: See sql.configured.metric.activation_settlement_gap
  sql_reference_id: sql.configured.metric.activation_settlement_gap
  required_filters:
  - is_active = true
  - runtime configuration must include the adjacent table in the client workflow
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.configured.wallet_refund_gap
  display_name: wallet_refund_gap implementation
  metric_id: metric.configured.wallet_refund_gap
  source_table_ids:
  - table.zs_observe.aza_return_dump
  - table.zs_observe.aza_wallet_ledger
  formula: See sql.configured.metric.wallet_refund_gap
  sql_reference_id: sql.configured.metric.wallet_refund_gap
  required_filters:
  - is_active = true
  - runtime configuration must include the adjacent table in the client workflow
  grain: documented in metric card
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
### 4.x output_contract

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.shopify.order_metrics
  display_name: Shopify order metrics output
  contract_type: query_output
  output_columns:
  - metric_name
  - period_or_group
  - metric_value
  - order_count
  evidence_refs:
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.shopify.reconciliation_candidates
  display_name: Shopify reconciliation candidate output
  contract_type: query_output
  output_columns:
  - order_id
  - reference_id
  - expected_amount
  - status_or_gap_reason
  evidence_refs:
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.configured.adjacent_reconciliation
  display_name: Configured adjacent reconciliation output
  contract_type: query_output
  output_columns:
  - source_table
  - business_key
  - expected_amount
  - actual_amount_or_null
  - gap_flag
  evidence_refs:
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x query_pattern

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.shopify.gmv_by_order
  display_name: gmv_by_order
  natural_language_patterns:
  - What is Shopify GMV by order?
  primary_metric: metric.shopify.gross_gmv
  source_table_ids:
  - table.zs_observe.shopify_oms
  sql_reference_id: sql.shopify.metric.gross_gmv
  output_contract_id: output_contract.shopify.order_metrics
  scope_policy: Apply runtime scope filters and preserve out-of-scope account guardrails.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.shopify.payment_mode_mix
  display_name: payment_mode_mix
  natural_language_patterns:
  - What is the payment-mode mix for Shopify orders?
  primary_metric: metric.shopify.order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  sql_reference_id: sql.shopify.query.payment_mode_mix
  output_contract_id: output_contract.shopify.order_metrics
  scope_policy: Apply runtime scope filters and preserve out-of-scope account guardrails.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.shopify.refund_events
  display_name: refund_events
  natural_language_patterns:
  - Show Shopify refund events and refunded amount by status.
  primary_metric: metric.shopify.refunded_amount
  source_table_ids:
  - table.zs_observe.shopify_returns
  sql_reference_id: sql.shopify.query.refund_events
  output_contract_id: output_contract.shopify.order_metrics
  scope_policy: Apply runtime scope filters and preserve out-of-scope account guardrails.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.shopify.shiprocket_link
  display_name: shiprocket_link
  natural_language_patterns:
  - Link Shopify orders to Shiprocket shipments.
  primary_metric: metric.shopify.gross_gmv
  source_table_ids:
  - table.zs_observe.shopify_oms
  - table.zs_observe.shiprocket_oms
  sql_reference_id: sql.shopify.query.shiprocket_link
  output_contract_id: output_contract.shopify.reconciliation_candidates
  scope_policy: Apply runtime scope filters and preserve out-of-scope account guardrails.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.shopify.pg_reconciliation_candidates
  display_name: pg_reconciliation_candidates
  natural_language_patterns:
  - Which Shopify orders should be reconciled to PG settlement?
  primary_metric: metric.shopify.gross_gmv
  source_table_ids:
  - table.zs_observe.shopify_oms
  sql_reference_id: sql.shopify.query.pg_reconciliation_candidates
  output_contract_id: output_contract.shopify.reconciliation_candidates
  scope_policy: Apply runtime scope filters and preserve out-of-scope account guardrails.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.configured.activation_settlement_gap
  display_name: activation_settlement_gap
  natural_language_patterns:
  - Find gift card activations not settled.
  primary_metric: metric.configured.activation_settlement_gap
  source_table_ids:
  - table.zs_observe.amazon_seller_flex
  - table.zs_observe.amazon_gc_settlement
  sql_reference_id: sql.configured.metric.activation_settlement_gap
  output_contract_id: output_contract.configured.adjacent_reconciliation
  scope_policy: Apply runtime scope filters and preserve out-of-scope account guardrails.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.configured.wallet_refund_gap
  display_name: wallet_refund_gap
  natural_language_patterns:
  - Find AZA returns missing wallet refund credits.
  primary_metric: metric.configured.wallet_refund_gap
  source_table_ids:
  - table.zs_observe.aza_return_dump
  - table.zs_observe.aza_wallet_ledger
  sql_reference_id: sql.configured.metric.wallet_refund_gap
  output_contract_id: output_contract.configured.adjacent_reconciliation
  scope_policy: Apply runtime scope filters and preserve out-of-scope account guardrails.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
### 4.x rule

```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.is_active_filter
  display_name: is active filter
  rule_text: All production Shopify/client-table queries must filter is_active = true where the column exists.
  rule_scope: shopify_d2c_oms_client_tables
  evidence_refs:
  - ev.shopify.client_tables.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.varchar_amount_cast
  display_name: varchar amount cast
  rule_text: For shopify_oms, charged_amount, refunded_amount, mrp, quantity and created_date are varchar in the dedicated
    Shopify doc; use TRY_CAST before aggregation/date filtering.
  rule_scope: shopify_d2c_oms_client_tables
  evidence_refs:
  - ev.shopify.dedicated_oms.schema.001
  - ev.shopify.dedicated_oms.shiprocket.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.order_level_aggregation
  display_name: order level aggregation
  rule_text: Aggregate shopify_oms by order_id for order-level GMV because Shopify supports multi-line orders and other_id
    distinguishes line items.
  rule_scope: shopify_d2c_oms_client_tables
  evidence_refs:
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.scope_ids_no_account_cards
  display_name: scope ids no account cards
  rule_text: group_id, tenant_id and group_level_id values are allowed only as scope filters/value profiles; never create
    tenant/group/account cards.
  rule_scope: shopify_d2c_oms_client_tables
  evidence_refs:
  - ev.shopify.client_tables.group_scope.001
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.pg_bank_courier_references_only
  display_name: pg bank courier references only
  rule_text: payment, gateway, UTR, AWB, courier and COD remittance labels are references for reconciliation, not account
    or logistics-domain cards.
  rule_scope: shopify_d2c_oms_client_tables
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.client_tables.common_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.adjacent_tables_runtime_config
  display_name: adjacent tables runtime config
  rule_text: Non-Shopify tables in Client Tables are configured-adjacent sources; include them in queries only when runtime
    client configuration maps them into the requested analysis.
  rule_scope: shopify_d2c_oms_client_tables
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x validation_test

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.no_forbidden_scope_cards
  display_name: no forbidden scope cards
  assertion: No candidate card type may be tenant, group, platform_account, account_data_binding, bank_account, payment_gateway_account,
    courier_account or statutory_tax_filing.
  related_ids:
  - rule.shopify.scope_ids_no_account_cards
  evidence_refs:
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.no_dangling_sql_refs
  display_name: no dangling sql refs
  assertion: Every metric_implementation/query_pattern sql_reference_id must resolve to a sql_pattern block.
  related_ids:
  - ev.shopify.manifest.cleanup.001
  evidence_refs:
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.no_missing_edge_refs
  display_name: no missing edge refs
  assertion: Every candidate_edge source_id and target_id must resolve to an existing candidate_card.
  related_ids:
  - ev.shopify.manifest.cleanup.001
  evidence_refs:
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.amount_cast_required
  display_name: amount cast required
  assertion: Shopify OMS metrics over charged_amount/refunded_amount/mrp/quantity must use TRY_CAST.
  related_ids:
  - rule.shopify.varchar_amount_cast
  evidence_refs:
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.adjacent_not_core
  display_name: adjacent not core
  assertion: Configured-adjacent tables must not be used in Shopify core metrics unless runtime scope explicitly selects them.
  related_ids:
  - rule.shopify.adjacent_tables_runtime_config
  evidence_refs:
  - ev.shopify.manifest.cleanup.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x reconciliation_profile

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.shopify.oms_to_pg_bank
  display_name: Shopify OMS to PG/bank reconciliation
  expected_side: shopify_oms expected order amount
  actual_side: Runtime PG settlement/bank credit
  unit:
  - order_id
  - payment_id
  - payment_references
  - amount
  - date
  matching_logic: Match Shopify expected amounts to PG settlement/bank references; external tables are runtime scope.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.shopify.cod_remittance
  display_name: Shopify COD remittance reconciliation
  expected_side: Shopify COD order expected amount
  actual_side: Runtime Shiprocket/BlueDart COD remittance/bank credit
  unit:
  - order_id
  - payment_mode
  - financial_status
  - amount
  matching_logic: Use financial_status=pending/COD and COD remittance timing labels; do not create courier account cards.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.shopify.refund_to_gateway
  display_name: Shopify refund to gateway reconciliation
  expected_side: shopify_returns refund events
  actual_side: Runtime gateway refund settlements
  unit:
  - order_name
  - transaction_id
  - other_id
  - refunded_payments
  matching_logic: Refund event ledger compared to external gateway refund credits where source table exists.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.configured.activation_settlement
  display_name: Configured gift-card activation to settlement
  expected_side: activation/order source
  actual_side: settlement table
  unit:
  - order_id
  matching_logic: Every activation or complete OMS record should appear in settlement as documented by configured source patterns.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.configured.return_wallet_refund
  display_name: Configured return to wallet refund
  expected_side: return dump returned item
  actual_side: wallet ledger credited entry
  unit:
  - order_id
  - item_id
  matching_logic: Every returned wallet-paid item should have corresponding wallet credit.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: medium
  review_status: accepted
  create_action: create
```
### 4.x business_process

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.order_capture
  display_name: Shopify OMS order capture
  domain_id: domain.shopify.d2c_order_capture
  process_summary: Customer order appears in shopify_oms at order-line grain with order_id/name/other_id, SKU, charged_amount,
    tax, payment and fulfillment fields.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.payment_state_classification
  display_name: Shopify payment state classification
  domain_id: domain.shopify.payment_state
  process_summary: financial_status and payment_mode classify prepaid, COD, PPCOD and refunded/voided semantics.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.refund_event_capture
  display_name: Shopify refund event capture
  domain_id: domain.shopify.refunds_returns
  process_summary: shopify_returns records refund transaction_id, payment_gateway, transaction_status, order_payment_status
    and refunded_payments.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.d2c_settlement_reconciliation
  display_name: Shopify D2C settlement reconciliation
  domain_id: domain.shopify.reconciliation
  process_summary: Shopify expected order/refund amounts reconcile to PG settlement and bank credit; COD remittance is a runtime
    external source.
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.configured_adjacent_source_intake
  display_name: Configured adjacent source intake
  domain_id: domain.shopify.configured_adjacent_sources
  process_summary: Client markdown tables are available as configured source tables but must be selected by runtime context
    before affecting Shopify analysis.
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x workflow_step

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.order_capture.01_order_line
  display_name: 01_order_line
  business_process_id: business_process.shopify.order_capture
  step_order: 1
  step_description: shopify_oms receives a line item with order_id/name/other_id, sku_id, quantity and charged_amount; other_id
    distinguishes multi-line orders.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.order_capture.02_amount_tax_status
  display_name: 02_amount_tax_status
  business_process_id: business_process.shopify.order_capture
  step_order: 2
  step_description: shopify_oms carries amount/tax/payment/fulfillment columns including charged_amount, total_tax, payment_mode,
    financial_status and transaction_type.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.payment_state.01_financial_status
  display_name: 01_financial_status
  business_process_id: business_process.shopify.payment_state_classification
  step_order: 1
  step_description: financial_status values paid, pending, partially_paid and voided map to prepaid, COD, PPCOD and cancelled-before-shipment
    semantics.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.payment_state.02_payment_refs
  display_name: 02_payment_refs
  business_process_id: business_process.shopify.payment_state_classification
  step_order: 2
  step_description: payment_id and payment_references carry gateway references; payment_mode may contain gateway labels but
    does not create PG account cards.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.refund.01_refund_event
  display_name: 01_refund_event
  business_process_id: business_process.shopify.refund_event_capture
  step_order: 1
  step_description: shopify_returns records order_name, transaction_id, payment_gateway, transaction_status, order_payment_status
    and refunded_payments.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.recon.01_expected_side
  display_name: 01_expected_side
  business_process_id: business_process.shopify.d2c_settlement_reconciliation
  step_order: 1
  step_description: Expected side uses shopify_oms charged_amount by order_id for paid/partially_paid orders and shopify_returns
    refunded_payments for refund events.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.recon.02_actual_side_runtime
  display_name: 02_actual_side_runtime
  business_process_id: business_process.shopify.d2c_settlement_reconciliation
  step_order: 2
  step_description: Actual PG/bank/COD remittance sources are runtime external inputs; the canonical file keeps payment_id,
    payment_references and UTR-like values as references only.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.configured.01_table_selected
  display_name: 01_table_selected
  business_process_id: business_process.shopify.configured_adjacent_source_intake
  step_order: 1
  step_description: A configured adjacent table such as paytm_giftcard_settlement, amazon_gc_settlement or aza_wallet_ledger
    can be used only when the runtime client workflow selects it.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.configured.02_guardrail_applied
  display_name: 02_guardrail_applied
  business_process_id: business_process.shopify.configured_adjacent_source_intake
  step_order: 2
  step_description: Before querying adjacent sources, apply is_active=true, table-specific status filters and no account-card
    derivation from group_id, UTR, gateway, bank or courier labels.
  materiality: source_specific_semantic_step
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  - ev.shopify.dedicated_oms.logic.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 4.x review_item

```yaml
candidate_card:
  card_type: review_item
  card_id: review.shopify.runtime_pg_bank_tables
  display_name: Runtime PG/bank source table binding
  issue_type: external_runtime_scope
  question: Which concrete PG settlement and bank statement tables should be bound to Shopify payment_id/payment_references
    for a specific client run?
  why_open: Client Tables documents PG/bank reconciliation behavior but does not provide concrete Razorpay/Cashfree/bank statement
    tables for Shopify core.
  blocking: false
  evidence_refs:
  - ev.shopify.client_tables.flow.001
  confidence: high
  review_status: open
  create_action: create
```
```yaml
candidate_card:
  card_type: review_item
  card_id: review.shopify.returns_order_join_normalization
  display_name: Shopify returns order-name normalization
  issue_type: join_normalization
  question: 'Should shopify_returns.order_name join to shopify_oms.name exactly or to normalized order_id without # prefix
    for each brand?'
  why_open: Source states order_name/original order and Shopify order name patterns but does not give a deterministic join
    SQL.
  blocking: false
  evidence_refs:
  - ev.shopify.client_tables.returns.001
  - ev.shopify.client_tables.core_oms.001
  confidence: medium
  review_status: open
  create_action: create
```
```yaml
candidate_card:
  card_type: review_item
  card_id: review.shopify.adjacent_table_runtime_mapping
  display_name: Adjacent table runtime mapping
  issue_type: runtime_scope_selection
  question: Which non-Shopify Client Tables are actually configured for the Shopify OMS client context in production?
  why_open: The uploaded client markdown lists multiple non-Shopify source families; this canonical includes them as configured-adjacent
    sources but avoids treating them as Shopify core.
  blocking: false
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  - ev.shopify.client_tables.group_scope.001
  confidence: medium
  review_status: open
  create_action: create
```
## 5. Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.group_id
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.tenant_id
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.group_level_id
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.ancestry
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.file_uuid
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.txn_uuid
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.unique_value
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.is_active
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.is_duplicated
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.is_active_false_reason
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.zen_status
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.zen_status_false_reason
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.zen_sheet_name
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.created_at
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.updated_at
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.deleted_at
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.currency_type
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.txn_date
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.txn_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.reference_id
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.reference_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.pg_ref_id
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.pg_ref_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.txn_description
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.txn_description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.payment_gateway
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.payment_gateway
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.payment_mode
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.payment_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.status
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.sub_status
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.sub_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.txn_type
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.txn_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.txn_sub_type
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.txn_sub_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.amount
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.dt
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.dt
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.withdrawal_initiated_dt
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.withdrawal_initiated_dt
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.user_id
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.user_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.description
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.kb_transfer_mode
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.kb_transfer_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.kb_status
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.kb_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.kb_amount
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.kb_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.kb_dt
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.kb_dt
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_withdrawal.has_column.abt_amount
  source_id: table.zs_observe.mpl_oms_withdrawal
  target_id: column.zs_observe.mpl_oms_withdrawal.abt_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.group_id
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.tenant_id
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.group_level_id
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.ancestry
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.file_uuid
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.txn_uuid
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.unique_value
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.is_active
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.is_duplicated
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.is_active_false_reason
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.zen_status
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.zen_status_false_reason
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.zen_sheet_name
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.created_at
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.updated_at
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.deleted_at
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.currency_type
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.txn_date
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.txn_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.reference_id
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.reference_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.pg_ref_id
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.pg_ref_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.txn_description
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.txn_description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.payment_gateway
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.payment_gateway
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.payment_mode
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.payment_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.status
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.txn_type
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.txn_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.amount
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.id
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.ist_time
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.ist_time
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.money_type
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.money_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.payment_gateway2
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.payment_gateway2
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.payment_method
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.payment_method
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.reference_type
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.reference_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.transaction_type
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.user_id
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.user_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.pg_reference_id
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.pg_reference_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.mpl_oms_deposit.has_column.transaction_external_key
  source_id: table.zs_observe.mpl_oms_deposit
  target_id: column.zs_observe.mpl_oms_deposit.transaction_external_key
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.group_id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tenant_id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.group_level_id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.ancestry
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.file_uuid
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.txn_uuid
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.unique_value
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.is_active
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.is_duplicated
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.is_active_false_reason
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.zen_status
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.zen_status_false_reason
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.zen_sheet_name
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.created_at
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.updated_at
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.deleted_at
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.currency_type
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.order_id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.name
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.created_date
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.transaction_type
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.order_status
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.order_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.fulfillment_status
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.fulfillment_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.financial_status
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.financial_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.buyers_name
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.buyers_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.email
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.email
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.phone
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.phone
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.brand
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.brand
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.sku_id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.sku_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.description
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.quantity
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.quantity
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.mrp
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.mrp
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.lineitem_price
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.lineitem_price
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.charged_amount
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.subtotal
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.subtotal
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.shipping_amount
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.shipping_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.total_tax
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.total_tax
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.total_tax_perc
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.total_tax_perc
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.discount_amount
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.discount_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.refunded_amount
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.refunded_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.payment_mode
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.payment_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.payment_method
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.payment_method
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.payment_id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.payment_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.payment_references
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.payment_references
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.destination_city
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.destination_city
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.destination_zipcode
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.destination_zipcode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.shipping_province
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.shipping_province
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tags_1
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tags_1
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.vendor
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.vendor
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.source
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.source
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_1_name
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_1_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_1_value
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_1_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.risk_level
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.risk_level
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.fulfilled_at
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.fulfilled_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.note_attributes
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.note_attributes
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.outstanding_balance
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.outstanding_balance
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.group_id
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.tenant_id
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.group_level_id
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.ancestry
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.file_uuid
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.txn_uuid
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.unique_value
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.is_active
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.is_duplicated
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.is_active_false_reason
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.zen_status
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.zen_status_false_reason
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.zen_sheet_name
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.created_at
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.updated_at
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.deleted_at
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.currency_type
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.order_name
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.order_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.transaction_id
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.transaction_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.payment_gateway
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.payment_gateway
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.transaction_status
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.transaction_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.order_payment_status
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.order_payment_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.refunded_payments
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.refunded_payments
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.customer_added_date
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.customer_added_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_returns.has_column.other_id
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.other_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.group_id
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.tenant_id
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.group_level_id
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.ancestry
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.file_uuid
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.txn_uuid
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.unique_value
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.is_active
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.is_duplicated
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.is_active_false_reason
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.zen_status
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.zen_status_false_reason
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.zen_sheet_name
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.created_at
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.updated_at
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.deleted_at
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.currency_type
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.order_id
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.parent_id
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.parent_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.refno
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.refno
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.ordernumber
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.ordernumber
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.store_name
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.store_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.orderstatus
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.orderstatus
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.transaction_type
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.created_date
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.invoice_date
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.invoice_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.file_date
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.file_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.file_date_dt
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.file_date_dt
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.closed_date
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.closed_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.couriername
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.couriername
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.cardloadamount
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.cardloadamount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.charged_amount
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.mrp
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.mrp
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.adjustment_amount
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.adjustment_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.topup_amount
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.topup_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.discount_amount
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.discount_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.reward_amount
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.reward_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.handling_charge
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.handling_charge
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.brand_discount
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.brand_discount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.qc_discount
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.qc_discount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.store_id
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.store_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.po_number
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.po_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.payment_mode
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.payment_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.metadata_2
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.metadata_2
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.woohoo_oms.has_column.file_name
  source_id: table.zs_observe.woohoo_oms
  target_id: column.zs_observe.woohoo_oms.file_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.group_id
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.tenant_id
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.group_level_id
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.ancestry
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.file_uuid
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.txn_uuid
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.unique_value
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.is_active
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.is_duplicated
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.is_active_false_reason
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.zen_status
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.zen_status_false_reason
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.zen_sheet_name
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.created_at
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.updated_at
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.deleted_at
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.currency_type
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.invoicenumber
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.invoicenumber
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.order_id
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.transaction_type
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.transactiondate
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.transactiondate
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.transactiontime
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.transactiontime
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.amount
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.totalamount
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.totalamount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.charged_amount
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.brand
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.brand
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.description
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.productname
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.productname
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.programgroup
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.programgroup
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.merchant
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.merchant
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.outlet
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.outlet
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.posname
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.posname
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.remarks
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.remarks
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.responsemessage
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.responsemessage
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.metadata
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.metadata
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.metadata_2
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.metadata_2
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.amazondiscount
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.amazondiscount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.discountadjustment
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.discountadjustment
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.qcdiscount
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.qcdiscount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.storedvaluerspoints
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.storedvaluerspoints
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.pretransactioncardbalance
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.pretransactioncardbalance
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.parentcardnumber
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.parentcardnumber
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.cardnumber
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.cardnumber
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_seller_flex.has_column.created_date
  source_id: table.zs_observe.amazon_seller_flex
  target_id: column.zs_observe.amazon_seller_flex.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.group_id
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.tenant_id
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.group_level_id
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.ancestry
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.file_uuid
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.txn_uuid
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.unique_value
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.is_active
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.is_duplicated
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.is_active_false_reason
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.zen_status
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.zen_status_false_reason
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.zen_sheet_name
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.created_at
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.updated_at
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.deleted_at
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.currency_type
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.settlement_id
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.settlement_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.settlement_date
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.settlement_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.created_date
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.order_id
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.item_id
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.item_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.sku_id
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.sku_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.other_id
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.other_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.metadata
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.metadata
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.metadata_2
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.metadata_2
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.metadata_3
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.metadata_3
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.transaction_type
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.quantity
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.quantity
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.fulfillment_channel
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.fulfillment_channel
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.charged_amount_type
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.charged_amount_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.charged_amount
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.item_fee_type
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.item_fee_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.item_fee_amount
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.item_fee_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.item_fee_tax
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.item_fee_tax
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.total_tcs_amount
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.total_tcs_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.total_tds_amount
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.total_tds_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.other_transaction_fee_type
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.other_transaction_fee_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.other_transaction_fees
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.other_transaction_fees
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.reimbursement_charges
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.reimbursement_charges
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.reimbursement_type
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.reimbursement_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.shipment_fee_amount
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.shipment_fee_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.shipment_fee_type
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.shipment_fee_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amazon_gc_settlement.has_column.settled_amount
  source_id: table.zs_observe.amazon_gc_settlement
  target_id: column.zs_observe.amazon_gc_settlement.settled_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.group_id
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.tenant_id
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.group_level_id
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.ancestry
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.file_uuid
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.txn_uuid
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.unique_value
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.is_active
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.is_duplicated
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.is_active_false_reason
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.zen_status
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.zen_status_false_reason
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.zen_sheet_name
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.created_at
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.updated_at
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.deleted_at
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.currency_type
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.order_id
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.parent_id
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.parent_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.brand
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.brand
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.brand_name
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.brand_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.order_reference_number
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.order_reference_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.qc__pl_order_id
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.qc__pl_order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.settlement_date
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.settlement_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.settled_date
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.settled_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.transaction_date
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.transaction_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.created_date
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.charged_amount
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.settled_amount
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.settled_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.utr_number
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.utr_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.gullak_technologies_settlement.has_column.settlement_id
  source_id: table.zs_observe.gullak_technologies_settlement
  target_id: column.zs_observe.gullak_technologies_settlement.settlement_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.group_id
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.tenant_id
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.group_level_id
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.ancestry
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.file_uuid
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.txn_uuid
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.unique_value
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.is_active
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.is_duplicated
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.is_active_false_reason
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.zen_status
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.zen_status_false_reason
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.zen_sheet_name
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.created_at
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.updated_at
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.deleted_at
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.currency_type
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.order_id
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.transaction_no
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.transaction_no
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.transaction_type
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.transaction_class
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.transaction_class
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.transaction_date
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.transaction_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.gl_date
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.gl_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.due_date
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.due_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.item_id
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.item_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.document_no
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.document_no
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.invoice_number
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.invoice_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.tax_invoice_number
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.tax_invoice_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.description
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.invoice_description
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.invoice_description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.customer_name
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.customer_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.customer_number
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.customer_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.customer_account
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.customer_account
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.customer_account_number
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.customer_account_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.total_amount
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.total_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.charged_amount
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.tax_amount
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.tax_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.payment_amount
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.payment_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.closing_balance
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.closing_balance
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.conversion_rate
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.conversion_rate
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.currency
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.currency
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.fc_amount
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.fc_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.month
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.month
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.event_month
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.event_month
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.mode_of_payment
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.mode_of_payment
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.po_number
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.po_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.po_date
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.po_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.business_vertical
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.business_vertical
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.sales_person
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.sales_person
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.pinelabs_soa.has_column.sl_no
  source_id: table.zs_observe.pinelabs_soa
  target_id: column.zs_observe.pinelabs_soa.sl_no
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.group_id
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.tenant_id
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.group_level_id
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.ancestry
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.file_uuid
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.txn_uuid
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.unique_value
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.is_active
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.is_duplicated
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.is_active_false_reason
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.zen_status
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.zen_status_false_reason
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.zen_sheet_name
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.created_at
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.updated_at
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.deleted_at
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.currency_type
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.order_id
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.order_item_id
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.order_item_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.pg_utr
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.pg_utr
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.cod_utr
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.cod_utr
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.settlement_date
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.settlement_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.transaction_type
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.payment_type
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.payment_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.fulfillment_type
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.fulfillment_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.sku_name
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.sku_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.merchant_sku
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.merchant_sku
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.charged_amount
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.amount_paid_by
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.amount_paid_by
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.amount_paid_by_p_g_mode
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.amount_paid_by_p_g_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.amount_paid_by_c_o_d_mode
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.amount_paid_by_c_o_d_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.gross_commission
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.gross_commission
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.gross_commission_gst_amount
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.gross_commission_gst_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.total_taxes
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.total_taxes
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.settled_pg
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.settled_pg
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.settled_cod
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.settled_cod
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.settled_amount
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.settled_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.marketplace_commission
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.marketplace_commission
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.journey
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.journey
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.qty_ordered
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.qty_ordered
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.order_created_at
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.order_created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.payment_creation_date
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.payment_creation_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.mid
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.mid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.wid
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.wid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.product_id
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.product_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.shipping_zone
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.shipping_zone
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.forward_logistic_charges
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.forward_logistic_charges
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.reverse_logistic_charges
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.reverse_logistic_charges
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.paytm_giftcard_settlement.has_column.ondc_order_id
  source_id: table.zs_observe.paytm_giftcard_settlement
  target_id: column.zs_observe.paytm_giftcard_settlement.ondc_order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.group_id
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.tenant_id
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.group_level_id
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.ancestry
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.file_uuid
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.txn_uuid
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.unique_value
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.is_active
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.is_duplicated
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.is_active_false_reason
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.zen_status
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.zen_status_false_reason
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.zen_sheet_name
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.created_at
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.updated_at
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.deleted_at
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.currency_type
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.common_order_id
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.common_order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.order_id
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.product_name
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.product_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.description
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.product_denomination
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.product_denomination
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.total_amount
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.total_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.charged_amount
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.discount_percentage
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.discount_percentage
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.settlement_amount
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.settlement_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.settled_amount
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.settled_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.mp_fees
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.mp_fees
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.utr_number
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.utr_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.settlement_id
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.settlement_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.order_date
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.order_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.created_date
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.settlement_date
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.settlement_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.quantity
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.quantity
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.red_giraffe_settlement.has_column.s_no_
  source_id: table.zs_observe.red_giraffe_settlement
  target_id: column.zs_observe.red_giraffe_settlement.s_no
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.group_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.tenant_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.group_level_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.ancestry
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.file_uuid
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.txn_uuid
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.unique_value
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.is_active
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.is_duplicated
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.is_active_false_reason
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.zen_status
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.zen_status_false_reason
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.zen_sheet_name
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.created_at
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.updated_at
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.deleted_at
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.currency_type
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.order_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.offer_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.offer_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.offer_name
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.offer_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.deal_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.deal_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.deal_name
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.deal_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.description
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.brand
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.brand
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.voucher_code
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.voucher_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.transaction_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.transaction_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.settlement_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.settlement_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.settlement_date
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.settlement_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.merchant_share
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.merchant_share
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.net_payable_to_merchant
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.net_payable_to_merchant
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.settled_amount
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.settled_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.charged_amount
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.mp_fees
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.mp_fees
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.paid_date
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.paid_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.payment_initiated_on
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.payment_initiated_on
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.business_account_id
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.business_account_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.account_holder_name
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.account_holder_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.bank_name
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.bank_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.bank_a_c_number
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.bank_a_c_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.ifsc_code
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.ifsc_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.memo
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.memo
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.discount_by_merchant
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.discount_by_merchant
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.taxable_value_for_tcs
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.taxable_value_for_tcs
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.tcs_deducted
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.tcs_deducted
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.tds_deducted
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.tds_deducted
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.nearby_marketplace.has_column.redemption_date
  source_id: table.zs_observe.nearby_marketplace
  target_id: column.zs_observe.nearby_marketplace.redemption_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.group_id
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.tenant_id
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.group_level_id
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.ancestry
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.file_uuid
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.txn_uuid
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.unique_value
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.is_active
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.is_duplicated
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.is_active_false_reason
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.zen_status
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.zen_status_false_reason
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.zen_sheet_name
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.created_at
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.updated_at
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.deleted_at
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.currency_type
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.destination_pincode
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.destination_pincode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.source_pincode
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.source_pincode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.source_code
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.source_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.other_fee_type
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.other_fee_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.logistic_partner
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.logistic_partner
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.start_date
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.start_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.astrotalk_oda.has_column.end_date
  source_id: table.zs_observe.astrotalk_oda
  target_id: column.zs_observe.astrotalk_oda.end_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.group_id
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.tenant_id
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.group_level_id
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.ancestry
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.file_uuid
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.txn_uuid
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.unique_value
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.is_active
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.is_duplicated
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.is_active_false_reason
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.zen_status
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.zen_status_false_reason
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.zen_sheet_name
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.created_at
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.updated_at
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.deleted_at
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.currency_type
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.order_id
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.parent_id
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.parent_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.order_reference_number
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.order_reference_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.order_no
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.order_no
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.sku_id
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.sku_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.product_sku
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.product_sku
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.brand_name
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.brand_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.charged_amount
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.settled_amount
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.settled_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.created_date
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.settlement_date
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.settlement_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.pre_discount_amount
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.pre_discount_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.quantity
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.quantity
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.s__no
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.s__no
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.first_pay_settlement.has_column.settlement_id
  source_id: table.zs_observe.first_pay_settlement
  target_id: column.zs_observe.first_pay_settlement.settlement_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.group_id
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.tenant_id
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.group_level_id
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.ancestry
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.file_uuid
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.txn_uuid
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.unique_value
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.is_active
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.is_duplicated
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.is_active_false_reason
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.zen_status
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.zen_status_false_reason
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.zen_sheet_name
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.created_at
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.updated_at
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.deleted_at
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.currency_type
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.order_id
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.reference_number
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.reference_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.parent_id
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.parent_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.brand_name
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.brand_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.brand
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.brand
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.denomination
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.denomination
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.total_amount
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.total_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.charged_amount
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.commission
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.commission
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.mp_fees
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.mp_fees
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.gst
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.gst
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.mp_fees_gst_amount
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.mp_fees_gst_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.payable_to_qwikcilver
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.payable_to_qwikcilver
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.settled_amount
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.settled_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.utr_number
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.utr_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.settlement_id
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.settlement_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.date_of_transaction
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.date_of_transaction
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.created_date
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.settlement_date
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.settlement_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.quantity
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.quantity
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.amica_technologies_settlement.has_column.comments
  source_id: table.zs_observe.amica_technologies_settlement
  target_id: column.zs_observe.amica_technologies_settlement.comments
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.group_id
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.tenant_id
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.group_level_id
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.ancestry
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.file_uuid
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.txn_uuid
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.unique_value
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.is_active
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.is_duplicated
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.is_active_false_reason
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.zen_status
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.zen_status_false_reason
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.zen_sheet_name
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.created_at
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.updated_at
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.deleted_at
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.currency_type
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.order_id
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.item_id
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.item_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.charged_amount
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.transaction_type
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.description
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_wallet_ledger.has_column.created_date
  source_id: table.zs_observe.aza_wallet_ledger
  target_id: column.zs_observe.aza_wallet_ledger.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.group_id
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.tenant_id
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.group_level_id
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.ancestry
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.file_uuid
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.txn_uuid
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.unique_value
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.is_active
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.is_duplicated
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.is_active_false_reason
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.zen_status
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.zen_status_false_reason
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.zen_sheet_name
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.created_at
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.updated_at
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.deleted_at
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.currency_type
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.order_id
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.item_id
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.item_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.sku_id
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.sku_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.description
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.created_date
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.transaction_type
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.quantity
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.quantity
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.destination_state
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.destination_state
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.destintion_country
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.destintion_country
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.destination_zipcode
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.destination_zipcode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.mrp
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.mrp
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.charged_amount
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.total_tax_perc
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.total_tax_perc
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.total_tax
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.total_tax
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.shipping_amount
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.shipping_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.courier_partner
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.courier_partner
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.return_awb_number
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.return_awb_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.payment_method
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.payment_method
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.payment_mode
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.payment_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.discount_amount
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.discount_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.subtotal
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.subtotal
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.promo_discount
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.promo_discount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.loyaltybyproduct
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.loyaltybyproduct
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.aza_cashback
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.aza_cashback
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.subtotal_suborder_level
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.subtotal_suborder_level
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.measuring_kit_charges
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.measuring_kit_charges
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.currency_rate
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.currency_rate
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_return_dump.has_column.other_id___other_id_2
  source_id: table.zs_observe.aza_return_dump
  target_id: column.zs_observe.aza_return_dump.other_id___other_id_2
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.group_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.tenant_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.group_level_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.ancestry
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.ancestry
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.file_uuid
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.file_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.txn_uuid
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.unique_value
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.is_active
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.is_duplicated
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.is_active_false_reason
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.is_active_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.zen_status
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.zen_status_false_reason
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.zen_status_false_reason
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.zen_sheet_name
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.created_at
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.created_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.updated_at
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.updated_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.deleted_at
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.deleted_at
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.post_process_file_uuid_ls
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.post_process_file_uuid_ls
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.currency_type
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.order_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.item_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.item_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.sku_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.sku_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.description
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.category
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.category
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.sub_category
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.sub_category
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.sub_category_name
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.sub_category_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.created_date
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.order_shipped_date
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.order_shipped_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.final_status
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.final_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.current_ship_status
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.current_ship_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.source_state
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.source_state
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.source_country
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.source_country
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.charged_amount
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.subtotal
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.subtotal
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.shipping_amount
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.shipping_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.item_promo_discount
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.item_promo_discount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.total_promo_discount
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.total_promo_discount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.payment_method
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.payment_method
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.payment_mode
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.payment_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.transaction_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.transaction_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.payment_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.payment_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.other_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.other_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.other_id_2
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.other_id_2
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.courier_partner
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.courier_partner
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.forward_awb_number
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.forward_awb_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.ship_tracking_id
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.ship_tracking_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.weight
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.weight
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.measurement_kit_price
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.measurement_kit_price
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.walletbyproduct
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.walletbyproduct
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.loyaltybyproduct
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.loyaltybyproduct
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.aza_cashback
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.aza_cashback
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.emi_discount
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.emi_discount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.currency_rate
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.currency_rate
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.internal_txn_type
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.internal_txn_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.taxbyproduct
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.taxbyproduct
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.shipping_charge_by_product
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.shipping_charge_by_product
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.customization_charges
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.customization_charges
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.aza_sales_dump.has_column.partial_paid_amount
  source_id: table.zs_observe.aza_sales_dump
  target_id: column.zs_observe.aza_sales_dump.partial_paid_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.order_id
  source_id: table.zs_observe.shiprocket_oms
  target_id: column.zs_observe.shiprocket_oms.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.awb_code
  source_id: table.zs_observe.shiprocket_oms
  target_id: column.zs_observe.shiprocket_oms.awb_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.courier_company
  source_id: table.zs_observe.shiprocket_oms
  target_id: column.zs_observe.shiprocket_oms.courier_company
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.is_active
  source_id: table.zs_observe.shiprocket_oms
  target_id: column.zs_observe.shiprocket_oms.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shopify_oms_to_shopify_returns.order_reference.from_table
  source_id: relationship.shopify_oms_to_shopify_returns.order_reference
  target_id: table.zs_observe.shopify_oms
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shopify_oms_to_shopify_returns.order_reference.to_table
  source_id: relationship.shopify_oms_to_shopify_returns.order_reference
  target_id: table.zs_observe.shopify_returns
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shopify_oms_to_shiprocket.order_suffix.from_table
  source_id: relationship.shopify_oms_to_shiprocket.order_suffix
  target_id: table.zs_observe.shopify_oms
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shopify_oms_to_shiprocket.order_suffix.to_table
  source_id: relationship.shopify_oms_to_shiprocket.order_suffix
  target_id: table.zs_observe.shiprocket_oms
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.amazon_seller_flex_to_amazon_gc_settlement.order_id.from_table
  source_id: relationship.amazon_seller_flex_to_amazon_gc_settlement.order_id
  target_id: table.zs_observe.amazon_seller_flex
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.amazon_seller_flex_to_amazon_gc_settlement.order_id.to_table
  source_id: relationship.amazon_seller_flex_to_amazon_gc_settlement.order_id
  target_id: table.zs_observe.amazon_gc_settlement
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.woohoo_oms_to_amazon_gc_settlement.order_id.from_table
  source_id: relationship.woohoo_oms_to_amazon_gc_settlement.order_id
  target_id: table.zs_observe.woohoo_oms
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.woohoo_oms_to_amazon_gc_settlement.order_id.to_table
  source_id: relationship.woohoo_oms_to_amazon_gc_settlement.order_id
  target_id: table.zs_observe.amazon_gc_settlement
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.mpl_deposit_to_pinelabs_soa.reference.from_table
  source_id: relationship.mpl_deposit_to_pinelabs_soa.reference
  target_id: table.zs_observe.mpl_oms_deposit
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.mpl_deposit_to_pinelabs_soa.reference.to_table
  source_id: relationship.mpl_deposit_to_pinelabs_soa.reference
  target_id: table.zs_observe.pinelabs_soa
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.aza_return_to_wallet.order_item.from_table
  source_id: relationship.aza_return_to_wallet.order_item
  target_id: table.zs_observe.aza_return_dump
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.aza_return_to_wallet.order_item.to_table
  source_id: relationship.aza_return_to_wallet.order_item
  target_id: table.zs_observe.aza_wallet_ledger
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.order_count.implements_metric
  source_id: metric_implementation.shopify.order_count
  target_id: metric.shopify.order_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.order_line_count.implements_metric
  source_id: metric_implementation.shopify.order_line_count
  target_id: metric.shopify.order_line_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.gross_gmv.implements_metric
  source_id: metric_implementation.shopify.gross_gmv
  target_id: metric.shopify.gross_gmv
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.aov.implements_metric
  source_id: metric_implementation.shopify.aov
  target_id: metric.shopify.aov
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.cod_order_count.implements_metric
  source_id: metric_implementation.shopify.cod_order_count
  target_id: metric.shopify.cod_order_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.ppcod_order_count.implements_metric
  source_id: metric_implementation.shopify.ppcod_order_count
  target_id: metric.shopify.ppcod_order_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.refunded_amount.implements_metric
  source_id: metric_implementation.shopify.refunded_amount
  target_id: metric.shopify.refunded_amount
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.tax_collected.implements_metric
  source_id: metric_implementation.shopify.tax_collected
  target_id: metric.shopify.tax_collected
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.outstanding_balance.implements_metric
  source_id: metric_implementation.shopify.outstanding_balance
  target_id: metric.shopify.outstanding_balance
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.refund_success_rate.implements_metric
  source_id: metric_implementation.shopify.refund_success_rate
  target_id: metric.shopify.refund_success_rate
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.configured.settled_amount.implements_metric
  source_id: metric_implementation.configured.settled_amount
  target_id: metric.configured.settled_amount
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.configured.activation_settlement_gap.implements_metric
  source_id: metric_implementation.configured.activation_settlement_gap
  target_id: metric.configured.activation_settlement_gap
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.configured.wallet_refund_gap.implements_metric
  source_id: metric_implementation.configured.wallet_refund_gap
  target_id: metric.configured.wallet_refund_gap
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.gmv_by_order.answers_metric
  source_id: query_pattern.shopify.gmv_by_order
  target_id: metric.shopify.gross_gmv
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.payment_mode_mix.answers_metric
  source_id: query_pattern.shopify.payment_mode_mix
  target_id: metric.shopify.order_count
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.refund_events.answers_metric
  source_id: query_pattern.shopify.refund_events
  target_id: metric.shopify.refunded_amount
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.shiprocket_link.answers_metric
  source_id: query_pattern.shopify.shiprocket_link
  target_id: metric.shopify.gross_gmv
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.pg_reconciliation_candidates.answers_metric
  source_id: query_pattern.shopify.pg_reconciliation_candidates
  target_id: metric.shopify.gross_gmv
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.configured.activation_settlement_gap.answers_metric
  source_id: query_pattern.configured.activation_settlement_gap
  target_id: metric.configured.activation_settlement_gap
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.configured.wallet_refund_gap.answers_metric
  source_id: query_pattern.configured.wallet_refund_gap
  target_id: metric.configured.wallet_refund_gap
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.order_capture.has_step.1
  source_id: business_process.shopify.order_capture
  target_id: workflow_step.shopify.order_capture.01_order_line
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.order_capture.has_step.2
  source_id: business_process.shopify.order_capture
  target_id: workflow_step.shopify.order_capture.02_amount_tax_status
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.payment_state_classification.has_step.1
  source_id: business_process.shopify.payment_state_classification
  target_id: workflow_step.shopify.payment_state.01_financial_status
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.payment_state_classification.has_step.2
  source_id: business_process.shopify.payment_state_classification
  target_id: workflow_step.shopify.payment_state.02_payment_refs
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.refund_event_capture.has_step.1
  source_id: business_process.shopify.refund_event_capture
  target_id: workflow_step.shopify.refund.01_refund_event
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.d2c_settlement_reconciliation.has_step.1
  source_id: business_process.shopify.d2c_settlement_reconciliation
  target_id: workflow_step.shopify.recon.01_expected_side
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.d2c_settlement_reconciliation.has_step.2
  source_id: business_process.shopify.d2c_settlement_reconciliation
  target_id: workflow_step.shopify.recon.02_actual_side_runtime
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.configured_adjacent_source_intake.has_step.1
  source_id: business_process.shopify.configured_adjacent_source_intake
  target_id: workflow_step.shopify.configured.01_table_selected
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.configured_adjacent_source_intake.has_step.2
  source_id: business_process.shopify.configured_adjacent_source_intake
  target_id: workflow_step.shopify.configured.02_guardrail_applied
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
## 6. SQL Pattern Registry

```yaml
sql_pattern:
  sql_id: sql.shopify.metric.order_count
  title: sql shopify metric order_count
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT COUNT(DISTINCT order_id) AS shopify_order_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.order_line_count
  title: sql shopify metric order_line_count
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT COUNT(*) AS shopify_order_line_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.gross_gmv
  title: sql shopify metric gross_gmv
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT
      order_id,
      SUM(TRY_CAST(charged_amount AS DOUBLE)) AS order_gmv
    FROM zs_observe.shopify_oms
    WHERE is_active = true
    GROUP BY order_id;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.aov
  title: sql shopify metric aov
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    WITH order_gmv AS (
      SELECT order_id, SUM(TRY_CAST(charged_amount AS DOUBLE)) AS order_gmv
      FROM zs_observe.shopify_oms
      WHERE is_active = true
      GROUP BY order_id
    )
    SELECT SUM(order_gmv) / NULLIF(COUNT(DISTINCT order_id), 0) AS shopify_aov
    FROM order_gmv;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.cod_order_count
  title: sql shopify metric cod_order_count
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT COUNT(DISTINCT order_id) AS cod_order_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true
      AND (financial_status = 'pending' OR LOWER(payment_mode) = 'cash_on_delivery');
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.ppcod_order_count
  title: sql shopify metric ppcod_order_count
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT COUNT(DISTINCT order_id) AS ppcod_order_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true
      AND (financial_status = 'partially_paid' OR LOWER(payment_mode) LIKE '%ppcod%');
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.refunded_amount
  title: sql shopify metric refunded_amount
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT SUM(TRY_CAST(refunded_amount AS DOUBLE)) AS refunded_amount
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.tax_collected
  title: sql shopify metric tax_collected
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT SUM(TRY_CAST(total_tax AS DOUBLE)) AS total_tax_collected
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.outstanding_balance
  title: sql shopify metric outstanding_balance
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT SUM(TRY_CAST(outstanding_balance AS DOUBLE)) AS outstanding_balance
    FROM zs_observe.shopify_oms
    WHERE is_active = true
      AND financial_status IN ('pending', 'partially_paid');
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.refund_success_rate
  title: sql shopify metric refund_success_rate
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT
      100.0 * COUNT_IF(transaction_status = 'success') / NULLIF(COUNT(*), 0) AS refund_success_rate_pct
    FROM zs_observe.shopify_returns
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.configured.metric.settled_amount_paytm
  title: sql configured metric settled_amount_paytm
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  sql: |-
    SELECT settlement_date, SUM(settled_amount) AS settled_amount
    FROM zs_observe.paytm_giftcard_settlement
    WHERE is_active = true
    GROUP BY settlement_date;
```
```yaml
sql_pattern:
  sql_id: sql.configured.metric.activation_settlement_gap
  title: sql configured metric activation_settlement_gap
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  sql: |-
    WITH activations AS (
      SELECT DISTINCT order_id
      FROM zs_observe.amazon_seller_flex
      WHERE is_active = true AND transaction_type = 'GIFT CARD ACTIVATE'
    ),
    settlements AS (
      SELECT DISTINCT order_id
      FROM zs_observe.amazon_gc_settlement
      WHERE is_active = true AND transaction_type = 'Order'
    )
    SELECT a.order_id
    FROM activations a
    LEFT JOIN settlements s ON a.order_id = s.order_id
    WHERE s.order_id IS NULL;
```
```yaml
sql_pattern:
  sql_id: sql.configured.metric.wallet_refund_gap
  title: sql configured metric wallet_refund_gap
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  sql: |-
    WITH returns AS (
      SELECT DISTINCT order_id, item_id
      FROM zs_observe.aza_return_dump
      WHERE is_active = true AND transaction_type = 'RETURNED'
    ),
    wallet_credits AS (
      SELECT DISTINCT order_id, item_id
      FROM zs_observe.aza_wallet_ledger
      WHERE is_active = true AND transaction_type = 'Credited'
    )
    SELECT r.order_id, r.item_id
    FROM returns r
    LEFT JOIN wallet_credits w
      ON r.order_id = w.order_id AND r.item_id = w.item_id
    WHERE w.order_id IS NULL;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.payment_mode_mix
  title: sql shopify query payment_mode_mix
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT payment_mode,
           COUNT(DISTINCT order_id) AS orders,
           SUM(TRY_CAST(charged_amount AS DOUBLE)) AS gmv
    FROM zs_observe.shopify_oms
    WHERE is_active = true
    GROUP BY payment_mode
    ORDER BY orders DESC;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.refund_events
  title: sql shopify query refund_events
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT transaction_status, order_payment_status,
           COUNT(*) AS refund_events,
           SUM(TRY_CAST(refunded_payments AS DOUBLE)) AS refunded_payments
    FROM zs_observe.shopify_returns
    WHERE is_active = true
    GROUP BY transaction_status, order_payment_status;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.shiprocket_link
  title: sql shopify query shiprocket_link
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.shiprocket.001
  sql: |-
    SELECT s.order_id,
           SUM(TRY_CAST(s.charged_amount AS DOUBLE)) AS shopify_value,
           sr.awb_code,
           sr.courier_company
    FROM zs_observe.shopify_oms s
    JOIN zs_observe.shiprocket_oms sr
      ON sr.order_id LIKE CONCAT(s.order_id, '-%')
    WHERE s.is_active = true AND sr.is_active = true
    GROUP BY s.order_id, sr.awb_code, sr.courier_company;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.pg_reconciliation_candidates
  title: sql shopify query pg_reconciliation_candidates
  evidence_refs:
  - ev.shopify.client_tables.core_oms.001
  - ev.shopify.dedicated_oms.logic.001
  sql: |-
    SELECT order_id, name, payment_id, payment_references,
           financial_status, payment_mode,
           SUM(TRY_CAST(charged_amount AS DOUBLE)) AS expected_pg_amount
    FROM zs_observe.shopify_oms
    WHERE is_active = true
      AND financial_status IN ('paid', 'partially_paid', 'refunded')
    GROUP BY order_id, name, payment_id, payment_references, financial_status, payment_mode;
```
```yaml
sql_pattern:
  sql_id: sql.configured.query.table_inventory
  title: sql configured query table_inventory
  evidence_refs:
  - ev.shopify.client_tables.common_recon.001
  sql: |-
    SELECT 'shopify_oms' AS table_name, COUNT(*) AS active_rows FROM zs_observe.shopify_oms WHERE is_active = true
    UNION ALL
    SELECT 'shopify_returns' AS table_name, COUNT(*) AS active_rows FROM zs_observe.shopify_returns WHERE is_active = true
    UNION ALL
    SELECT 'paytm_giftcard_settlement' AS table_name, COUNT(*) AS active_rows FROM zs_observe.paytm_giftcard_settlement WHERE is_active = true;
```
## 7. Parser QA Summary

```yaml
parser_quality_manifest:
  candidate_cards: 849
  candidate_edges: 780
  source_evidence_count: 29
  sql_patterns: 18
  missing_edge_references: 0
  dangling_sql_refs: 0
  deleted_card_references: 0
  open_reviews: 3
  lazy_workflow_steps: 0
  placeholder_metric_formulas: 0
  unsupported_metric_implementations: 0
  process_variants_review_required: 0
  unresolved_benchmark_reviews_without_reason: 0
  hard_threshold_benchmarks_without_rule: 0
  forbidden_scope_cards_from_scope_ids: 0
```
## 8. Deterministic Cleanup Notes

- Shopify core remains `shopify_oms` and `shopify_returns`; `shiprocket_oms` is reference-only for documented order-suffix joins.
- The broader client markdown contains MPL, Woohoo, Amazon gift-card, Pine Labs, Paytm, AZA, and other source tables. These are included as configured-adjacent source tables with runtime-selection guardrails, not as Shopify platform identity cards.
- The dedicated Shopify OMS doc wins for Shopify type conflicts: `charged_amount`, `refunded_amount`, `mrp`, `quantity`, and `created_date` remain varchar/cast-required for canonical query generation.
- Payment gateway, bank, UTR, COD remittance, courier, GST, tenant and group labels remain columns, value profiles, reconciliation keys, or open runtime reviews only.
