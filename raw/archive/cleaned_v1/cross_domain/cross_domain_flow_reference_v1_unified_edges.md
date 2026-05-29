# Cross-Domain Flow Reference — V1 Unified Edges
```yaml
document_metadata:
  document_id: cross_domain_flow_reference_v1_unified_edges
  generated_on: '2026-05-21'
  purpose: Reusable cross-domain reference layer linking marketplace, operations, logistics, payment, and bank markdowns.
  input_policy: Use uploaded domain markdowns only; ignore canonical_edge_taxonomy_registry.md.
  build_level: reference_pattern_not_tenant_account_execution
  business_flow_binding_instances_created: false
  why_no_business_flow_binding_instances: Tenant, group, platform_account, account_data_binding, and business_scope_set docs
    were not provided. This build emits reusable process/reconciliation/query/validation cards and defers account-specific
    BusinessFlowBinding creation.
  source_domain_buckets:
  - marketplace
  - operations
  - logistics
  - payment
  - bank
  ignored_files:
  - canonical_edge_taxonomy_registry.md
  candidate_card_count: 244
  candidate_edge_count: 419
  canonical_edge_count: 364
  parser_helper_edge_count: 55
  edges_with_legacy_aliases: 182
  missing_internal_edge_references: 0
```
## 0. Parser Instructions

This file is a cross-domain **reference** build. It should be loaded after or alongside the source domain markdowns. It defines reusable cross-domain processes, reconciliation profiles, matching logic, query patterns, rules, validations, output contracts, and execution constraints. It does **not** create tenant/account-specific `business_flow_binding` instances.

Critical rules:

- Do not create `tenant`, `group`, `platform_account`, `account_data_binding`, or `business_scope_set` cards from this file.
- Do not hardcode `group_level_id`, seller account, courier account, bank account, or payment account filters in this reference layer.
- External anchor-set references point to cards that already exist in the uploaded marketplace, operations, logistics, payment, and bank markdowns.
- Create `business_flow_binding` instances only in a later tenant/account-specific build.
- Preserve all source-domain boundaries: marketplace settlement stays marketplace-owned; operations evidence stays OMS/WMS-owned; logistics evidence stays logistics-owned; bank credits/debits stay bank-owned; payment captures/payouts stay payment-owned.

## 1. Source Document Manifest

```yaml
source_document_manifest:
- domain_bucket: marketplace
  source_document: amazon_marketplace_clean_md_v8_unified_edges.md
  document_key: amazon
  detected_candidate_cards: 352
  reported_candidate_cards: 352
  reported_candidate_edges: 933
  sha256_first_16: 93cd51edd7690e53
  platform_ids:
  - platform.amazon
  platform_context_ids:
  - platform_context.amazon.in
  - platform_context.amazon.international
  table_count: 5
  relationship_count: 7
  reconciliation_profile_count: 4
  query_pattern_count: 13
- domain_bucket: marketplace
  source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
  document_key: flipkart
  detected_candidate_cards: 293
  reported_candidate_cards: 293
  reported_candidate_edges: 889
  sha256_first_16: 9f33a27cdd031fd0
  platform_ids:
  - platform.flipkart
  platform_context_ids:
  - platform_context.flipkart.in
  table_count: 4
  relationship_count: 6
  reconciliation_profile_count: 5
  query_pattern_count: 15
- domain_bucket: marketplace
  source_document: myntra_marketplace_clean_md_v8_unified_edges.md
  document_key: myntra
  detected_candidate_cards: 550
  reported_candidate_cards: 550
  reported_candidate_edges: 1597
  sha256_first_16: 5d5b53d3637a48e2
  platform_ids:
  - platform.myntra
  platform_context_ids:
  - platform_context.myntra.in
  table_count: 9
  relationship_count: 9
  reconciliation_profile_count: 4
  query_pattern_count: 13
- domain_bucket: marketplace
  source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
  document_key: nykaa
  detected_candidate_cards: 793
  reported_candidate_cards: 793
  reported_candidate_edges: 2024
  sha256_first_16: 49f03d2df94c3fa4
  platform_ids:
  - platform.nykaa
  platform_context_ids:
  - platform_context.nykaa_fashion.in
  table_count: 5
  relationship_count: 8
  reconciliation_profile_count: 6
  query_pattern_count: 28
- domain_bucket: marketplace
  source_document: ajio_marketplace_clean_md_v8_unified_edges.md
  document_key: ajio
  detected_candidate_cards: 444
  reported_candidate_cards: 444
  reported_candidate_edges: 1524
  sha256_first_16: d06fec293749e357
  platform_ids:
  - platform.ajio
  platform_context_ids:
  - platform_context.ajio.in
  table_count: 4
  relationship_count: 5
  reconciliation_profile_count: 4
  query_pattern_count: 24
- domain_bucket: marketplace
  source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
  document_key: healthkart
  detected_candidate_cards: 476
  reported_candidate_cards: 476
  reported_candidate_edges: 1640
  sha256_first_16: 6c7c28de6ec47244
  platform_ids:
  - platform.healthkart
  platform_context_ids:
  - platform_context.healthkart.in
  table_count: 3
  relationship_count: 3
  reconciliation_profile_count: 3
  query_pattern_count: 19
- domain_bucket: marketplace
  source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
  document_key: jiomart
  detected_candidate_cards: 458
  reported_candidate_cards: 458
  reported_candidate_edges: 1476
  sha256_first_16: 8e2c02fa5ce2c72f
  platform_ids:
  - platform.jiomart
  platform_context_ids:
  - platform_context.jiomart.in
  table_count: 4
  relationship_count: 5
  reconciliation_profile_count: 4
  query_pattern_count: 29
- domain_bucket: marketplace
  source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
  document_key: limeroad
  detected_candidate_cards: 382
  reported_candidate_cards: 382
  reported_candidate_edges: 1304
  sha256_first_16: 4be9da53b67cd375
  platform_ids:
  - platform.limeroad
  platform_context_ids:
  - platform_context.limeroad.in
  table_count: 2
  relationship_count: 2
  reconciliation_profile_count: 4
  query_pattern_count: 23
- domain_bucket: marketplace
  source_document: meesho_marketplace_clean_md_v8_unified_edges.md
  document_key: meesho
  detected_candidate_cards: 787
  reported_candidate_cards: 787
  reported_candidate_edges: 3910
  sha256_first_16: 15e8ba4f6980ee42
  platform_ids:
  - platform.meesho
  platform_context_ids:
  - platform_context.meesho.in
  table_count: 8
  relationship_count: 12
  reconciliation_profile_count: 8
  query_pattern_count: 45
- domain_bucket: marketplace
  source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
  document_key: snapdeal
  detected_candidate_cards: 862
  reported_candidate_cards: 862
  reported_candidate_edges: 4261
  sha256_first_16: b6579f968d47295d
  platform_ids:
  - platform.snapdeal
  platform_context_ids:
  - platform_context.snapdeal.in
  table_count: 6
  relationship_count: 10
  reconciliation_profile_count: 10
  query_pattern_count: 45
- domain_bucket: marketplace
  source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
  document_key: target_plus
  detected_candidate_cards: 436
  reported_candidate_cards: 436
  reported_candidate_edges: 2351
  sha256_first_16: 7ebd3d63639a67eb
  platform_ids:
  - platform.target_plus
  platform_context_ids:
  - platform_context.target_plus.us
  table_count: 4
  relationship_count: 6
  reconciliation_profile_count: 5
  query_pattern_count: 34
- domain_bucket: marketplace
  source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
  document_key: tatacliq
  detected_candidate_cards: 382
  reported_candidate_cards: 382
  reported_candidate_edges: 1913
  sha256_first_16: 2fe605e2375b4b8b
  platform_ids:
  - platform.tatacliq
  platform_context_ids:
  - platform_context.tatacliq.in
  table_count: 2
  relationship_count: 1
  reconciliation_profile_count: 5
  query_pattern_count: 24
- domain_bucket: operations
  source_document: increff_operations_clean_md_v8_unified_edges (1).md
  document_key: increff
  detected_candidate_cards: 789
  reported_candidate_cards: 789
  reported_candidate_edges: 2908
  sha256_first_16: d085aeafdace819f
  platform_ids:
  - platform.increff
  platform_context_ids:
  - platform_context.increff.in
  table_count: 2
  relationship_count: 3
  reconciliation_profile_count: 11
  query_pattern_count: 19
- domain_bucket: operations
  source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
  document_key: unicommerce
  detected_candidate_cards: 705
  reported_candidate_cards: 705
  reported_candidate_edges: 3301
  sha256_first_16: 0a8e0a71d0db641c
  platform_ids:
  - platform.unicommerce
  platform_context_ids:
  - platform_context.unicommerce.in
  table_count: 2
  relationship_count: 2
  reconciliation_profile_count: 23
  query_pattern_count: 24
- domain_bucket: logistics
  source_document: logistics_domain_overview_parser_ready_v4_unified_edges.md
  document_key: logistics_domain_overview
  detected_candidate_cards: 157
  reported_candidate_cards: 157
  reported_candidate_edges: 363
  sha256_first_16: 2b61d2bd1e63860e
  platform_ids: []
  platform_context_ids: []
  table_count: 1
  relationship_count: 1
  reconciliation_profile_count: 0
  query_pattern_count: 0
- domain_bucket: logistics
  source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
  document_key: logistics_reconciliation_patterns
  detected_candidate_cards: 263
  reported_candidate_cards: 263
  reported_candidate_edges: 684
  sha256_first_16: 70ac468d0ac88413
  platform_ids: []
  platform_context_ids: []
  table_count: 1
  relationship_count: 5
  reconciliation_profile_count: 7
  query_pattern_count: 31
- domain_bucket: logistics
  source_document: delhivery_logistics_parser_ready_v4_unified_edges.md
  document_key: delhivery
  detected_candidate_cards: 114
  reported_candidate_cards: 114
  reported_candidate_edges: 309
  sha256_first_16: 5efc36cace9c3bf2
  platform_ids:
  - platform.delhivery
  platform_context_ids:
  - platform_context.delhivery.in
  table_count: 2
  relationship_count: 2
  reconciliation_profile_count: 0
  query_pattern_count: 0
- domain_bucket: logistics
  source_document: dtdc_logistics_parser_ready_v4_unified_edges.md
  document_key: dtdc
  detected_candidate_cards: 61
  reported_candidate_cards: 61
  reported_candidate_edges: 137
  sha256_first_16: e371d524cd9dadb7
  platform_ids:
  - platform.dtdc
  platform_context_ids:
  - platform_context.dtdc.in
  table_count: 2
  relationship_count: 0
  reconciliation_profile_count: 0
  query_pattern_count: 0
- domain_bucket: logistics
  source_document: ecom_express_logistics_parser_ready_v4_unified_edges.md
  document_key: ecom_express
  detected_candidate_cards: 10
  reported_candidate_cards: 10
  reported_candidate_edges: 27
  sha256_first_16: d890631e9374e769
  platform_ids:
  - platform.ecom_express
  platform_context_ids:
  - platform_context.ecom_express.in
  table_count: 0
  relationship_count: 0
  reconciliation_profile_count: 0
  query_pattern_count: 0
- domain_bucket: logistics
  source_document: ekart_logistics_parser_ready_v4_unified_edges.md
  document_key: ekart
  detected_candidate_cards: 58
  reported_candidate_cards: 58
  reported_candidate_edges: 143
  sha256_first_16: a4a72c8035ac7d4a
  platform_ids:
  - platform.ekart
  platform_context_ids:
  - platform_context.ekart.in
  table_count: 2
  relationship_count: 0
  reconciliation_profile_count: 0
  query_pattern_count: 0
- domain_bucket: logistics
  source_document: shadowfax_logistics_parser_ready_v4_unified_edges.md
  document_key: shadowfax
  detected_candidate_cards: 12
  reported_candidate_cards: 12
  reported_candidate_edges: 28
  sha256_first_16: 24c0aab12440251c
  platform_ids:
  - platform.shadowfax
  platform_context_ids:
  - platform_context.shadowfax.in
  table_count: 0
  relationship_count: 0
  reconciliation_profile_count: 0
  query_pattern_count: 0
- domain_bucket: logistics
  source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
  document_key: shiprocket
  detected_candidate_cards: 181
  reported_candidate_cards: 181
  reported_candidate_edges: 518
  sha256_first_16: 3c141ce4bac0ddb1
  platform_ids:
  - platform.shiprocket
  platform_context_ids:
  - platform_context.shiprocket.in
  table_count: 4
  relationship_count: 14
  reconciliation_profile_count: 0
  query_pattern_count: 0
- domain_bucket: logistics
  source_document: xpressbees_logistics_parser_ready_v4_unified_edges.md
  document_key: xpressbees
  detected_candidate_cards: 34
  reported_candidate_cards: 34
  reported_candidate_edges: 95
  sha256_first_16: 825ed3975758d9ac
  platform_ids:
  - platform.xpressbees
  platform_context_ids:
  - platform_context.xpressbees.in
  table_count: 1
  relationship_count: 0
  reconciliation_profile_count: 0
  query_pattern_count: 0
- domain_bucket: payment
  source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
  document_key: payment_gateway
  detected_candidate_cards: 1169
  reported_candidate_cards: 1169
  reported_candidate_edges: 2500
  sha256_first_16: 334af242d17142f5
  platform_ids:
  - platform.cashfree
  - platform.razorpay
  - platform.paytm
  - platform.phonepe
  - platform.paypal
  - platform.amazon_pay
  - platform.stripe
  - platform.shopify_payments
  - platform.simpl
  - platform.sika
  - platform.tata_digital
  - platform.affirm
  - platform.afterpay
  - platform.klarna
  - platform.flex
  - platform.navi
  - platform.apple_play
  - platform.google_play
  - platform.rbl_bank
  platform_context_ids:
  - platform_context.cashfree.in
  - platform_context.razorpay.in
  - platform_context.paytm.in
  - platform_context.phonepe.in
  - platform_context.paypal.global
  - platform_context.amazon_pay.in
  - platform_context.stripe.global
  - platform_context.shopify_payments.global
  - platform_context.simpl.in
  - platform_context.sika.africa
  - platform_context.tata_digital.in
  - platform_context.affirm.us
  - platform_context.afterpay.global
  - platform_context.klarna.eu_us_uk
  - platform_context.flex.global
  - platform_context.navi.in
  - platform_context.apple_play.global
  - platform_context.google_play.global
  - platform_context.rbl_bank.in
  table_count: 26
  relationship_count: 10
  reconciliation_profile_count: 5
  query_pattern_count: 9
- domain_bucket: bank
  source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
  document_key: bank_statement
  detected_candidate_cards: 437
  reported_candidate_cards: 437
  reported_candidate_edges: 952
  sha256_first_16: 06aa5f1fb5960ba6
  platform_ids:
  - platform.yes_bank
  - platform.idfc_first_bank
  - platform.icici_bank
  - platform.icici_bank_uk
  - platform.hsbc
  - platform.citibank
  - platform.nbf
  - platform.hdfc_bank
  - platform.axis_bank
  platform_context_ids:
  - platform_context.yes_bank.in
  - platform_context.idfc_first_bank.in
  - platform_context.icici_bank.global_inr
  - platform_context.icici_bank_uk.uk
  - platform_context.hsbc.international_multi_currency
  - platform_context.citibank.international_multi_currency
  - platform_context.nbf.uae
  - platform_context.hdfc_bank.in
  - platform_context.axis_bank.in
  table_count: 10
  relationship_count: 15
  reconciliation_profile_count: 6
  query_pattern_count: 8
```
## 2. Cross-Domain Anchor Sets

Anchor sets are non-canonical reference helpers. They group existing source-domain card IDs so cross-domain profiles can point to reusable source evidence without creating tenant/account bindings.

```yaml
external_anchor_set:
  anchor_set_id: anchor_set.marketplace.order_tables
  description: Marketplace-side order / OMS / sales evidence tables.
  domain_bucket: marketplace
  card_type: table
  source_card_count: 16
  source_card_refs:
  - card_id: table.zs_observe.amazon_oms
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.flipkart.oms
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.myntra_non_order_settlement
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.myntra_oms
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.myntra_oms_settlement
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.nykaa_oms
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.ajio_oms
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.healthkart_oms
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.jiomart_oms
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.limeroad_oms
    source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.meesho_sales
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.snapdeal_non_order
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.snapdeal_oms
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.snapdeal_sales_return
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.target_sales
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.tatacliq_oms
    source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.marketplace.settlement_tables
  description: Marketplace settlement, disbursement, commission, cashback, fee, credit-note, and payout evidence tables.
  domain_bucket: marketplace
  card_type: table
  source_card_count: 21
  source_card_refs:
  - card_id: table.zs_observe.amazon_settlement
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.amazon_disbursment
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.amazon_fee_preview
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.flipkart.settlement
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.flipkart.commission
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.flipkart.cashback
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.myntra_non_order_settlement
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.myntra_oms_settlement
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.myntra_settlement
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.nykaa_settlement
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.ajio_settlement
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.ajio_credit_note
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.healthkart_settlement
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.jiomart_settlement
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.limeroad_settlement
    source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.meesho_settlement
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.snapdeal_commission
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.snapdeal_payments
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.snapdeal_settlement
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.target_settlement
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.tatacliq_settlement
    source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.marketplace.return_tables
  description: Marketplace reverse / returns / RTO evidence tables.
  domain_bucket: marketplace
  card_type: table
  source_card_count: 11
  source_card_refs:
  - card_id: table.zs_observe.amazon_returns
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.myntra_seller_report_reverse
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.myntra_reverse
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.ajio_reverse
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.healthkart_return
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.jiomart_returns
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.meesho_returns
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.meesho_reverse
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.meesho_reverse_expenses
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.snapdeal_sales_return
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: table.zs_observe.target_returns
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.marketplace.relationships
  description: Marketplace-internal relationship cards available as source-domain anchors.
  domain_bucket: marketplace
  card_type: relationship
  source_card_count: 74
  source_card_refs:
  - card_id: relationship.amazon.oms_to_disbursment.order_id
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.amazon.oms_to_settlement.order_id
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.amazon.settlement_to_disbursment.order_id_settlement_id
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.amazon.fee_preview_to_disbursment.sku
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.amazon.fee_preview_to_oms.sku
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.amazon.returns_to_oms.order_id
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.amazon.returns_to_settlement.order_id
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.flipkart.oms_settlement
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.flipkart.commission_settlement
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.flipkart.commission_oms
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.flipkart.cashback_settlement
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.flipkart.cashback_commission
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.flipkart.cashback_oms
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_oms.myntra_expenses.order_id
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_oms.myntra_oms_settlement.order_id
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_oms.myntra_receivables.order_id
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_oms.myntra_reverse.order_code_order_id
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_oms.myntra_seller_report_forward.order_id
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_oms.myntra_seller_report_reverse.order_id
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_oms.myntra_settlement.order_code_order_id_invoice
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_settlement.myntra_oms_settlement.order_id
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.myntra_settlement.myntra_reverse.order_id_item_id
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.nykaa.addition_charge_to_mapping.source_gst_name
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.nykaa.oms_to_addition_charge.order_id
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.nykaa.oms_to_mapper_gst.magentoorderno_truncated
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.nykaa.oms_to_mapping.source_gst_name
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.nykaa.oms_to_settlement.invoice_number
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.nykaa.oms_to_settlement.order_id
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.nykaa.settlement_to_addition_charge.order_id
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.nykaa.settlement_to_mapping.source_gst_name
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.ajio.ajio_oms.ajio_settlement.order_id_order_id
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.ajio.ajio_oms.ajio_settlement.purchase_po_no_purchase_po_no
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.ajio.ajio_reverse.ajio_oms.parent_id_order_id
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.ajio.ajio_credit_note.ajio_reverse.purchase_po_no_purchase_po_no
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.ajio.ajio_settlement.ajio_credit_note.credit_note_no_invoice_number
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.healthkart.healthkart_oms.healthkart_settlement.order_id_order_id
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.healthkart.healthkart_return.healthkart_settlement.order_id_order_id
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.healthkart.healthkart_oms.healthkart_return.order_id_order_id
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.jiomart.jiomart_oms.jiomart_settlement.order_id_order_id
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.jiomart.jiomart_oms.jiomart_returns.order_id_order_id
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.jiomart.jiomart_settlement.jiomart_returns.order_id_order_id
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.jiomart.jiomart_oms.jiomart_settlement.invoice_number_invoice_number
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.jiomart.jiomart_shipment.jiomart_oms.order_id_order_id
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.limeroad.limeroad_oms.limeroad_settlement.invoice_number_invoice_number_item_id_item_id
    source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.limeroad.limeroad_oms.limeroad_settlement.order_id_order_id
    source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_brand_mapping.meesho_sales.order_id
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_brand_mapping.meesho_settlement.order_id
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_forward_expenses.meesho_sales.sub_order_num
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_other_charges_expenses.meesho_forward_expenses.sub_order_num
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_other_charges_expenses.meesho_sales.sub_order_num
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_returns.meesho_brand_mapping.order_id
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_returns.meesho_sales.order_id
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_returns.meesho_settlement.order_id
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_reverse_expenses.meesho_forward_expenses.sub_order_num
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_reverse_expenses.meesho_other_charges_expenses.sub_order_num
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_reverse_expenses.meesho_sales.sub_order_num
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.meesho.meesho_settlement.meesho_sales.order_id
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_commission.snapdeal_oms.invoice_number
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_commission.snapdeal_settlement.invoice_number
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_non_order.snapdeal_commission.invoice_number
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_non_order.snapdeal_oms.invoice_number
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_non_order.snapdeal_settlement.invoice_number
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_sales_return.snapdeal_commission.invoice_number
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_sales_return.snapdeal_non_order.invoice_number
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_sales_return.snapdeal_oms.order_id
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_sales_return.snapdeal_settlement.invoice_number
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.snapdeal.snapdeal_settlement.snapdeal_oms.item_id
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.target_plus.target_returns.target_sales.order_id
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.target_plus.target_settlement.target_returns.order_id
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.target_plus.target_settlement.target_sales.order_id
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.target_plus.target_settlement.target_tcin_mapping.sku_id
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.target_plus.target_tcin_mapping.target_returns.sku_id
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.target_plus.target_tcin_mapping.target_sales.sku_id
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: relationship.tatacliq.tatacliq_settlement.tatacliq_oms.order_id
    source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.marketplace.reconciliation_profiles
  description: Marketplace-internal reconciliation profiles from the vendor markdowns.
  domain_bucket: marketplace
  card_type: reconciliation_profile
  source_card_count: 62
  source_card_refs:
  - card_id: reconciliation_profile.amazon.oms_to_settlement
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.amazon.settlement_to_disbursement
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.amazon.returns_to_settlement
    source_document: amazon_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.flipkart.oms_settlement
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.flipkart.settlement_commission
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.flipkart.cashback_settlement_offer
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.flipkart.settlement_waterfall
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.flipkart.cross_table_pipeline
    source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.myntra.non_order_settlement_inclusion
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.myntra.oms_to_settlement_level_1
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.myntra.reverse_to_settlement
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.myntra.settlement_series_to_actual
    source_document: myntra_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.nykaa.mapper_gst_to_oms_enrichment
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.nykaa.oms_settlement_amount_discrepancy
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.nykaa.oms_to_settlement_forward
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.nykaa.reverse_to_settlement_inline
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.nykaa.shipping_charge_true_up
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.nykaa.source_gst_name_mapping
    source_document: nykaa_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.ajio.oms_settlement_matching_unsettled_orders
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.ajio.credit_note_reverse_matching
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.ajio.unmatched_credit_notes_no_return_record
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.ajio.oms_vs_settlement_amount_comparison
    source_document: ajio_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.healthkart.oms_settlement_matching
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.healthkart.oms_vs_settlement_amount_discrepancy
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.healthkart.return_settlement_reconciliation
    source_document: healthkart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.jiomart.7_1_oms_settlement_match_3_way_per_order
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.jiomart.7_2_returns_oms_settlement_full_chain
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.jiomart.7_3_unreconciled_oms_orders_not_in_settlement
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.jiomart.7_4_tcs_reconciliation
    source_document: jiomart_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.limeroad.7_1_oms_settlement_reconciliation_invoice_item_match
    source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.limeroad.7_2_waterfall_mrp_nsp_settled_net
    source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.limeroad.7_3_tcs_reconciliation_oms_vs_settlement
    source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.limeroad.7_4_return_reverse_entries_audit
    source_document: limeroad_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.meesho.brand_level_return_rate
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.meesho.forward_expenses_settlement_validation
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.meesho.join_reverse_settlement_reconciliation
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.meesho.oms_settlement_match
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.meesho.reconcile_with_settlement_return_logistics
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.meesho.return_reverse_logistics_reconciliation
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.meesho.sales_settlement_match
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.meesho.tcs_reconciliation
    source_document: meesho_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.commission_validation
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.oms_settlement_matching
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.oms_settlement_reconciliation
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.payment_vs_settlement_reconciliation
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.payments_settlement_matching
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.reconcile_non_order_vs_settlement_tds_rows
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.return_oms_reconciliation
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.returns_refund_reconciliation
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.tds_reconciliation_non_order_vs_settlement
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.snapdeal.unmatched_returns_return_without_settlement
    source_document: snapdeal_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.target_plus.commission_validation
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.target_plus.payout_reconciliation
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.target_plus.returns_sales_reconciliation
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.target_plus.returns_settlement_refund_match
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.target_plus.sales_settlement_reconciliation
    source_document: target_plus_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.tatacliq.commission_rate_validation
    source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.tatacliq.oms_settlement_reconciliation
    source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.tatacliq.return_oms_settlement_match
    source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.tatacliq.settlement_batch_completeness
    source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
  - card_id: reconciliation_profile.tatacliq.tds_reconciliation
    source_document: tatacliq_marketplace_clean_md_v8_unified_edges.md
    domain_bucket: marketplace
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.operations.tables
  description: Increff and Unicommerce operational evidence tables.
  domain_bucket: operations
  card_type: table
  source_card_count: 4
  source_card_refs:
  - card_id: table.zs_observe.increff_returns
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: table.zs_observe.increff_sales
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: table.zs_observe.unicommerce
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: table.zs_observe.unicommerce_order_sales_report
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.operations.relationships
  description: Increff and Unicommerce operational relationship cards.
  domain_bucket: operations
  card_type: relationship
  source_card_count: 5
  source_card_refs:
  - card_id: relationship.increff.sales_awb_to_returns_awb
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: relationship.increff.sales_to_returns.channel_order_id
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: relationship.increff.sales_to_returns.order_id
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: relationship.unicommerce.invoice_to_osr.order_id_hash_prefix
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: relationship.unicommerce.invoice_to_osr.sku_id
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.operations.reconciliation_profiles
  description: Increff and Unicommerce operational reconciliation profiles.
  domain_bucket: operations
  card_type: reconciliation_profile
  source_card_count: 34
  source_card_refs:
  - card_id: reconciliation_profile.increff.enrich_returns_with_sku_from_sales
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.identity_columns
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.join_coverage_summary
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.join_map
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.return_rate_by_channel_mensa_brands_only
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.return_rate_sales_vs_returns
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.sales_awb_to_returns_awb
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.sales_to_returns_channel_order_id
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.sales_to_returns_order_id
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.table_summary_reference
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.increff.warehouse_dispatch_distribution
    source_document: increff_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.data_quality_observations
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.data_quality_observations_and_known_issues
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.delivery_rate_analysis
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.delivery_rate_by_courier
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.delivery_rate_from_osr
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.full_enriched_order_view
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.full_enriched_view_join_sales_osr
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.full_enriched_view_sales_awb_delivery_status
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.gst_summary
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.identity_columns
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.invoice_to_osr_order_id_hash_prefix
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.invoice_to_osr_sku_id
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.join_to_osr_for_awb_and_delivery_status
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.mrp_vs_selling_price_analysis
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.order_id_format
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.primary_join
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.return_rate_analysis
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.return_rate_by_type
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.return_rate_from_this_table
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.sales_vs_returns_vs_cancels_net_revenue
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.table_summary_reference
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.the_critical_join
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
  - card_id: reconciliation_profile.unicommerce.the_two_table_relationship
    source_document: unicommerce_operations_clean_md_v8_unified_edges (1).md
    domain_bucket: operations
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.logistics.tables
  description: Logistics vendor and overview tables used as AWB/shipment/COD/freight anchors.
  domain_bucket: logistics
  card_type: table
  source_card_count: 13
  source_card_refs:
  - card_id: table.zs_observe.shopify_oms
    source_document: logistics_domain_overview_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.bank_statement
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.delhivery_invoice
    source_document: delhivery_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.delhivery_settlement
    source_document: delhivery_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.dtdc_settlement
    source_document: dtdc_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.dtdc_invoice
    source_document: dtdc_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.ekart_settlement
    source_document: ekart_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.ekart_invoice
    source_document: ekart_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.shiprocket_oms
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.shiprocket_invoice
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.shiprocket_settlement
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.shiprocket_settlement_report
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: table.zs_observe.xpressbees_settlement
    source_document: xpressbees_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.logistics.relationships
  description: Logistics relationship cards, especially AWB, shipment, invoice, COD, and settlement joins.
  domain_bucket: logistics
  card_type: relationship
  source_card_count: 22
  source_card_refs:
  - card_id: relationship.shopify_oms.shiprocket_oms.parsed_order_id
    source_document: logistics_domain_overview_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.dtdc_settlement.bank_statement.utr
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.dtdc_settlement.bank_statement.bank_ref
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.delhivery_settlement.bank_statement.utr
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.ekart_settlement.bank_statement.bank_ref
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.bank_statement.utr
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.delhivery_invoice.delhivery_settlement.awb
    source_document: delhivery_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
    source_document: delhivery_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.shiprocket_invoice.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.shiprocket_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_invoice.shiprocket_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.delhivery_invoice.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.delhivery_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_settlement.delhivery_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.dtdc_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_invoice.dtdc_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.ekart_settlement.shipment_id
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.ekart_settlement.tracking_id
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_invoice.ekart_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_oms.xpressbees_settlement.shipping_id
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_settlement.xpressbees_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: relationship.shiprocket_invoice.xpressbees_settlement.awb
    source_document: shiprocket_logistics_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.logistics.reconciliation_profiles
  description: Logistics reconciliation-pattern profiles from logistics reconciliation reference.
  domain_bucket: logistics
  card_type: reconciliation_profile
  source_card_count: 7
  source_card_refs:
  - card_id: reconciliation_profile.order_to_shipment
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: reconciliation_profile.shipment_to_freight_invoice
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: reconciliation_profile.freight_charge_validation
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: reconciliation_profile.cod_expected_to_courier_remittance
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: reconciliation_profile.courier_batch_to_bank_credit
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: reconciliation_profile.prepaid_pos_logistics_settlement
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
  - card_id: reconciliation_profile.low_confidence_native_to_fallback
    source_document: logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md
    domain_bucket: logistics
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.payment.tables
  description: Payment gateway payin, payout, settlement, refund, and fee tables.
  domain_bucket: payment
  card_type: table
  source_card_count: 26
  source_card_refs:
  - card_id: table.zs_observe.cashfree_payin
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.cashfree_expense_report
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.razorpay_payin
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.razorpay_payout
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.razorpay_transactions
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.paytm_payin
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.paytm_payout
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.phonepe_payin
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.paypal_express_checkout_settlements
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.paypal_express_checkout_reports
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.paypal_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.amazon_payin
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.stripe_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.stripe_transaction_report
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.shopify_payments_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.simpl_payin
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.sika_payin
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.tata_digital_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.affirm_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.after_pay_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.klarna_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.flex_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.navi_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.apple_play
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.google_play
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: table.zs_observe.rbl_oms_payin
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.payment.relationships
  description: Payment gateway relationship cards, including UTR and original payment linkage.
  domain_bucket: payment
  card_type: relationship
  source_card_count: 10
  source_card_refs:
  - card_id: relationship.razorpay.payin_payout.utr
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.razorpay.payin_transactions.order_id
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.paytm.refund_original
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.phonepe.refund_original
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.paypal.refund_original
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.stripe.transaction_report_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.shopify.stripe_payout_reference
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.cashfree.expense_to_bank
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.gateway.settlement_to_rbl_bank
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: relationship.bnpl.bank_recon_keys
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.payment.reconciliation_profiles
  description: Payment gateway reconciliation profiles.
  domain_bucket: payment
  card_type: reconciliation_profile
  source_card_count: 5
  source_card_refs:
  - card_id: reconciliation_profile.pg.gateway_payout_to_bank_credit
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: reconciliation_profile.pg.payin_to_settlement_batch
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: reconciliation_profile.pg.refund_to_original_payment
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: reconciliation_profile.pg.stripe_transaction_to_settlement
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
  - card_id: reconciliation_profile.pg.bnpl_settlement_to_bank
    source_document: payment_gateway_gold_standard_clean_md_v2_unified_edges.md
    domain_bucket: payment
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.bank.tables
  description: Bank statement tables used as bank-credit/debit anchors.
  domain_bucket: bank
  card_type: table
  source_card_count: 10
  source_card_refs:
  - card_id: table.zs_ingest.yesbank_oms_payout
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.idfc_bank
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.idfc_bank_inr
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.icici_bank_global
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.icici_bank
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.hsbc_bank
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.citi_bank
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.nbf_bank
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.hdfc_bank_settlement
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: table.zs_ingest.axis_bank_settlement
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.bank.relationships
  description: Bank statement relationship cards for UTR, narration, cheque/reference extraction.
  domain_bucket: bank
  card_type: relationship
  source_card_count: 15
  source_card_refs:
  - card_id: relationship.bank_statement.hdfc_bank_settlement.chq_ref_no_to_razorpay_payin_settlement_utr
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.axis_bank_settlement.chqno_to_cashfree_payin_utr
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.axis_bank_settlement.chqno_to_paytm_payin_utr_no
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.yesbank_oms_payout.urn_to_yes_biz_payin_rrn
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.yesbank_oms_payout.bankreferencenumber_to_yes_biz_payin_rrn
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.idfc_bank.description_to_parsed_gateway_utr_from_narration
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.idfc_bank.user_narration_to_parsed_gateway_utr_from_user_narration
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.idfc_bank_inr.ref_cheque_no_to_parsed_neft_utr
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.icici_bank_global.cheque_no_ref_no_to_razorpay_payin_settlement_utr
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.icici_bank.chequeno_to_chaps_bacs_fps_reference
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.hsbc_bank.bank_reference_to_swift_or_neft_reference
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.hsbc_bank.customer_reference_to_merchant_payment_reference
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.citi_bank.bank_reference_to_swift_reference
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.citi_bank.customer_reference_to_merchant_payment_reference
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: relationship.bank_statement.nbf_bank.reference_number_to_aed_payment_reference
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
```
```yaml
external_anchor_set:
  anchor_set_id: anchor_set.bank.reconciliation_profiles
  description: Bank statement reconciliation profiles.
  domain_bucket: bank
  card_type: reconciliation_profile
  source_card_count: 6
  source_card_refs:
  - card_id: reconciliation_profile.bank_credit_to_payment_gateway_payout
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: reconciliation_profile.bank_debit_to_payout_file
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: reconciliation_profile.hdfc_bank_credit_to_gateway_settlement
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: reconciliation_profile.axis_bank_credit_to_gateway_settlement
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: reconciliation_profile.bank_statement_to_erp_ledger
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
  - card_id: reconciliation_profile.international_bank_reference_match
    source_document: bank_statement_gold_standard_clean_md_v8_unified_edges.md
    domain_bucket: bank
```
## 3. Cross-Domain Key Normalization Registry

```yaml
cross_domain_key_normalization_registry:
- key: order_id
  domains:
  - marketplace
  - operations
  - payment
  normalization: Preserve source-specific prefixes unless a source markdown explicitly defines a transform.
- key: order_item_id
  domains:
  - marketplace
  - operations
  normalization: Use item-level grain when settlement/order rows are not one row per order.
- key: channel_order_id
  domains:
  - operations
  - marketplace
  normalization: Treat as a cross-channel bridge key; do not assume it equals marketplace order_id without evidence.
- key: sku
  domains:
  - marketplace
  - operations
  - logistics
  normalization: Use source SKU/merchant SKU/platform SKU mapping only when the source card defines it.
- key: awb_tracking_id
  domains:
  - operations
  - logistics
  - marketplace
  normalization: Use AWB/tracking/shipment ID as logistics handoff key; courier account resolution is deferred.
- key: settlement_id
  domains:
  - marketplace
  - payment
  - logistics
  - bank
  normalization: Settlement ID is source-domain owned until linked through a flow-specific matching logic.
- key: utr_rrn_bank_reference
  domains:
  - payment
  - marketplace
  - logistics
  - bank
  normalization: Use bank statement reference extraction before joining to bank-side evidence.
- key: payment_id_transaction_id
  domains:
  - payment
  - operations
  - marketplace
  normalization: Payment identifiers must come from payment gateway cards; order/payment joins require gateway evidence.
- key: refund_id_return_id
  domains:
  - marketplace
  - operations
  - payment
  normalization: Separate customer return, courier return/RTO, cancellation, refund, and chargeback states before matching.
- key: gstin_hsn_tax_fields
  domains:
  - marketplace
  - operations
  - payment
  - bank
  normalization: Tax identifiers/amounts are source fields unless a tax-compliance doc explicitly owns filing semantics.
```
## 4. Candidate Cards

```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.flow_reference
  name: Cross-domain flow reference
  fields:
    domain_family: cross_domain_reference
    description: Reusable cross-domain reconciliation/process reference layer.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.marketplace_operations
  name: Marketplace ↔ operations flows
  fields:
    domain_family: cross_domain_reference
    description: Marketplace order/settlement semantics linked to OMS/WMS operational evidence.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.operations_operations
  name: Operations ↔ operations flows
  fields:
    domain_family: cross_domain_reference
    description: Cross-channel operational alignment between OMS, WMS, invoice, shipment, and return systems.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.operations_logistics
  name: Operations ↔ logistics flows
  fields:
    domain_family: cross_domain_reference
    description: OMS/WMS shipment evidence linked to logistics AWB/status/COD/freight evidence.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.marketplace_logistics
  name: Marketplace ↔ logistics flows
  fields:
    domain_family: cross_domain_reference
    description: Marketplace shipment/return/shipping-fee evidence linked to logistics evidence.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.payment_operations
  name: Payment ↔ order/operations flows
  fields:
    domain_family: cross_domain_reference
    description: Payment gateway pay-in/refund records linked to orders/invoices/returns.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.payment_bank
  name: Payment gateway ↔ bank flows
  fields:
    domain_family: cross_domain_reference
    description: Gateway settlements and payouts linked to bank statement credits/debits.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.marketplace_bank
  name: Marketplace ↔ bank flows
  fields:
    domain_family: cross_domain_reference
    description: Marketplace settlement/disbursement references linked to bank credits.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.logistics_bank
  name: Logistics ↔ bank flows
  fields:
    domain_family: cross_domain_reference
    description: Logistics COD remittance and settlement evidence linked to bank credits.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.cross_domain.refund_chargeback
  name: Refund / chargeback cross-domain flows
  fields:
    domain_family: cross_domain_reference
    description: Reverse/refund/chargeback evidence across marketplace, operations, payment, and bank contexts.
    source_documents: all_uploaded_domain_markdowns
    create_action: create_reference_card
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.marketplace_order_to_unicommerce_invoice
  name: Marketplace order to Unicommerce invoice / OSR alignment
  fields:
    domain_id: domain.cross_domain.marketplace_operations
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Marketplace order / OMS side
    - Unicommerce invoice / order-sales-report side
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.marketplace.relationships
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  name: Marketplace order to Unicommerce invoice / OSR alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.marketplace_order_to_unicommerce_invoice
    source_side_id: reconciliation_side.cross_domain.marketplace_order_to_unicommerce_invoice.source
    target_side_id: reconciliation_side.cross_domain.marketplace_order_to_unicommerce_invoice.target
    primary_unit_id: reconciliation_unit.cross_domain.order_or_order_item
    matching_logic_id: matching_logic.cross_domain.marketplace_order_to_unicommerce_invoice
    primary_keys:
    - order_id
    - order_item_id
    - sku
    - invoice_number
    - channel_order_id
    normalization_rules:
    - 'Preserve source-specific order-id prefixes. For Unicommerce OSR, apply documented hash-prefix join where applicable:
      # || unicommerce.order_id = unicommerce_order_sales_report.order_id.'
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.marketplace.relationships
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_order_to_unicommerce_invoice.source
  name: Marketplace order / OMS side
  fields:
    side_role: source_or_expected
    side_description: Marketplace order / OMS side
    anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.marketplace.relationships
    key_candidates:
    - order_id
    - order_item_id
    - sku
    - invoice_number
    - channel_order_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_order_to_unicommerce_invoice.target
  name: Unicommerce invoice / order-sales-report side
  fields:
    side_role: target_or_actual
    side_description: Unicommerce invoice / order-sales-report side
    anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    key_candidates:
    - order_id
    - order_item_id
    - sku
    - invoice_number
    - channel_order_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.order_or_order_item
  name: order or order item
  fields:
    unit_key: order_or_order_item
    candidate_keys:
    - order_id
    - order_item_id
    - sku
    - invoice_number
    - channel_order_id
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.marketplace_order_to_unicommerce_invoice
  name: Marketplace order to Unicommerce invoice / OSR alignment matching logic
  fields:
    primary_keys:
    - order_id
    - order_item_id
    - sku
    - invoice_number
    - channel_order_id
    normalization_steps:
    - 'Preserve source-specific order-id prefixes. For Unicommerce OSR, apply documented hash-prefix join where applicable:
      # || unicommerce.order_id = unicommerce_order_sales_report.order_id.'
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.missing_in_unicommerce_invoice
  name: missing in unicommerce invoice
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
    category_key: missing_in_unicommerce_invoice
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.missing_in_marketplace_order_table
  name: missing in marketplace order table
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
    category_key: missing_in_marketplace_order_table
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.order_status_mismatch
  name: order status mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
    category_key: order_status_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.amount_or_quantity_variance
  name: amount or quantity variance
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
    category_key: amount_or_quantity_variance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.key_prefix_normalization_gap
  name: key prefix normalization gap
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
    category_key: key_prefix_normalization_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.marketplace_order_to_unicommerce_invoice
  name: Marketplace order to Unicommerce invoice / OSR alignment query pattern
  fields:
    intent: Marketplace order to Unicommerce invoice / OSR alignment
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.marketplace.relationships
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_order_to_unicommerce_invoice.key_normalization
  name: Marketplace order to Unicommerce invoice / OSR alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: 'Preserve source-specific order-id prefixes. For Unicommerce OSR, apply documented hash-prefix join where applicable:
      # || unicommerce.order_id = unicommerce_order_sales_report.order_id.'
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_order_to_unicommerce_invoice.account_scope_deferred
  name: Marketplace order to Unicommerce invoice / OSR alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_order_to_unicommerce_invoice.coverage_and_reference_integrity
  name: Marketplace order to Unicommerce invoice / OSR alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_order_to_unicommerce_invoice.amount_and_status_consistency
  name: Marketplace order to Unicommerce invoice / OSR alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.marketplace_order_to_unicommerce_invoice
  name: Marketplace order to Unicommerce invoice / OSR alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.marketplace_order_to_unicommerce_invoice
  name: Marketplace order to Unicommerce invoice / OSR alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.marketplace_order_to_increff_wms_dispatch
  name: Marketplace order to Increff WMS dispatch alignment
  fields:
    domain_id: domain.cross_domain.marketplace_operations
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Marketplace order side
    - Increff WMS sales / dispatch side
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  name: Marketplace order to Increff WMS dispatch alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.marketplace_order_to_increff_wms_dispatch
    source_side_id: reconciliation_side.cross_domain.marketplace_order_to_increff_wms_dispatch.source
    target_side_id: reconciliation_side.cross_domain.marketplace_order_to_increff_wms_dispatch.target
    primary_unit_id: reconciliation_unit.cross_domain.order_or_shipment_or_item
    matching_logic_id: matching_logic.cross_domain.marketplace_order_to_increff_wms_dispatch
    primary_keys:
    - order_id
    - channel_order_id
    - item_id
    - sku
    - awb
    - other_id
    normalization_rules:
    - Use channel_order_id, system_order_id, order_id, item_id, AWB/other_id as alternative matching keys. Do not infer marketplace
      settlement from Increff operational evidence.
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_order_to_increff_wms_dispatch.source
  name: Marketplace order side
  fields:
    side_role: source_or_expected
    side_description: Marketplace order side
    anchor_sets:
    - anchor_set.marketplace.order_tables
    key_candidates:
    - order_id
    - channel_order_id
    - item_id
    - sku
    - awb
    - other_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_order_to_increff_wms_dispatch.target
  name: Increff WMS sales / dispatch side
  fields:
    side_role: target_or_actual
    side_description: Increff WMS sales / dispatch side
    anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    key_candidates:
    - order_id
    - channel_order_id
    - item_id
    - sku
    - awb
    - other_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.order_or_shipment_or_item
  name: order or shipment or item
  fields:
    unit_key: order_or_shipment_or_item
    candidate_keys:
    - order_id
    - channel_order_id
    - item_id
    - sku
    - awb
    - other_id
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.marketplace_order_to_increff_wms_dispatch
  name: Marketplace order to Increff WMS dispatch alignment matching logic
  fields:
    primary_keys:
    - order_id
    - channel_order_id
    - item_id
    - sku
    - awb
    - other_id
    normalization_steps:
    - Use channel_order_id, system_order_id, order_id, item_id, AWB/other_id as alternative matching keys. Do not infer marketplace
      settlement from Increff operational evidence.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.missing_wms_dispatch
  name: missing wms dispatch
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
    category_key: missing_wms_dispatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.missing_marketplace_order
  name: missing marketplace order
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
    category_key: missing_marketplace_order
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.sku_or_item_mismatch
  name: sku or item mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
    category_key: sku_or_item_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.awb_missing_or_changed
  name: awb missing or changed
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
    category_key: awb_missing_or_changed
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.channel_mapping_gap
  name: channel mapping gap
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
    category_key: channel_mapping_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.marketplace_order_to_increff_wms_dispatch
  name: Marketplace order to Increff WMS dispatch alignment query pattern
  fields:
    intent: Marketplace order to Increff WMS dispatch alignment
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_order_to_increff_wms_dispatch.key_normalization
  name: Marketplace order to Increff WMS dispatch alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Use channel_order_id, system_order_id, order_id, item_id, AWB/other_id as alternative matching keys. Do not
      infer marketplace settlement from Increff operational evidence.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_order_to_increff_wms_dispatch.account_scope_deferred
  name: Marketplace order to Increff WMS dispatch alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_order_to_increff_wms_dispatch.coverage_and_reference_integrity
  name: Marketplace order to Increff WMS dispatch alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_order_to_increff_wms_dispatch.amount_and_status_consistency
  name: Marketplace order to Increff WMS dispatch alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.marketplace_order_to_increff_wms_dispatch
  name: Marketplace order to Increff WMS dispatch alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.marketplace_order_to_increff_wms_dispatch
  name: Marketplace order to Increff WMS dispatch alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.unicommerce_invoice_to_increff_wms_sales
  name: Unicommerce invoice to Increff WMS sales alignment
  fields:
    domain_id: domain.cross_domain.operations_operations
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Unicommerce invoice / OMS side
    - Increff WMS sales side
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  name: Unicommerce invoice to Increff WMS sales alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.unicommerce_invoice_to_increff_wms_sales
    source_side_id: reconciliation_side.cross_domain.unicommerce_invoice_to_increff_wms_sales.source
    target_side_id: reconciliation_side.cross_domain.unicommerce_invoice_to_increff_wms_sales.target
    primary_unit_id: reconciliation_unit.cross_domain.order_or_invoice_or_sku
    matching_logic_id: matching_logic.cross_domain.unicommerce_invoice_to_increff_wms_sales
    primary_keys:
    - order_id
    - channel_order_id
    - system_order_id
    - sku
    - invoice_number
    - awb
    normalization_rules:
    - Use source-specific order-id prefix rules before comparing. Treat both systems as operations-layer evidence, not settlement
      evidence.
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.unicommerce_invoice_to_increff_wms_sales.source
  name: Unicommerce invoice / OMS side
  fields:
    side_role: source_or_expected
    side_description: Unicommerce invoice / OMS side
    anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    key_candidates:
    - order_id
    - channel_order_id
    - system_order_id
    - sku
    - invoice_number
    - awb
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.unicommerce_invoice_to_increff_wms_sales.target
  name: Increff WMS sales side
  fields:
    side_role: target_or_actual
    side_description: Increff WMS sales side
    anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    key_candidates:
    - order_id
    - channel_order_id
    - system_order_id
    - sku
    - invoice_number
    - awb
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.order_or_invoice_or_sku
  name: order or invoice or sku
  fields:
    unit_key: order_or_invoice_or_sku
    candidate_keys:
    - order_id
    - channel_order_id
    - system_order_id
    - sku
    - invoice_number
    - awb
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.unicommerce_invoice_to_increff_wms_sales
  name: Unicommerce invoice to Increff WMS sales alignment matching logic
  fields:
    primary_keys:
    - order_id
    - channel_order_id
    - system_order_id
    - sku
    - invoice_number
    - awb
    normalization_steps:
    - Use source-specific order-id prefix rules before comparing. Treat both systems as operations-layer evidence, not settlement
      evidence.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.invoice_without_wms_dispatch
  name: invoice without wms dispatch
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
    category_key: invoice_without_wms_dispatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.wms_dispatch_without_invoice
  name: wms dispatch without invoice
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
    category_key: wms_dispatch_without_invoice
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.sku_mismatch
  name: sku mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
    category_key: sku_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.quantity_mismatch
  name: quantity mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
    category_key: quantity_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.status_or_return_classification_mismatch
  name: status or return classification mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
    category_key: status_or_return_classification_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.unicommerce_invoice_to_increff_wms_sales
  name: Unicommerce invoice to Increff WMS sales alignment query pattern
  fields:
    intent: Unicommerce invoice to Increff WMS sales alignment
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.unicommerce_invoice_to_increff_wms_sales.key_normalization
  name: Unicommerce invoice to Increff WMS sales alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Use source-specific order-id prefix rules before comparing. Treat both systems as operations-layer evidence,
      not settlement evidence.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.unicommerce_invoice_to_increff_wms_sales.account_scope_deferred
  name: Unicommerce invoice to Increff WMS sales alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.unicommerce_invoice_to_increff_wms_sales.coverage_and_reference_integrity
  name: Unicommerce invoice to Increff WMS sales alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.unicommerce_invoice_to_increff_wms_sales.amount_and_status_consistency
  name: Unicommerce invoice to Increff WMS sales alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.unicommerce_invoice_to_increff_wms_sales
  name: Unicommerce invoice to Increff WMS sales alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.unicommerce_invoice_to_increff_wms_sales
  name: Unicommerce invoice to Increff WMS sales alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.unicommerce_shipment_to_logistics_tracking
  name: Unicommerce shipment evidence to logistics tracking/status alignment
  fields:
    domain_id: domain.cross_domain.operations_logistics
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Unicommerce OSR shipment side
    - Logistics vendor shipment/status side
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  name: Unicommerce shipment evidence to logistics tracking/status alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.unicommerce_shipment_to_logistics_tracking
    source_side_id: reconciliation_side.cross_domain.unicommerce_shipment_to_logistics_tracking.source
    target_side_id: reconciliation_side.cross_domain.unicommerce_shipment_to_logistics_tracking.target
    primary_unit_id: reconciliation_unit.cross_domain.awb_or_shipment
    matching_logic_id: matching_logic.cross_domain.unicommerce_shipment_to_logistics_tracking
    primary_keys:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - courier_partner
    normalization_rules:
    - Use AWB/tracking number from operational source as the primary handoff key. Do not create courier settlement/account
      cards unless the logistics document supplies settlement evidence.
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.unicommerce_shipment_to_logistics_tracking.source
  name: Unicommerce OSR shipment side
  fields:
    side_role: source_or_expected
    side_description: Unicommerce OSR shipment side
    anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    key_candidates:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - courier_partner
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.unicommerce_shipment_to_logistics_tracking.target
  name: Logistics vendor shipment/status side
  fields:
    side_role: target_or_actual
    side_description: Logistics vendor shipment/status side
    anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    key_candidates:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - courier_partner
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.awb_or_shipment
  name: awb or shipment
  fields:
    unit_key: awb_or_shipment
    candidate_keys:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - courier_partner
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.unicommerce_shipment_to_logistics_tracking
  name: Unicommerce shipment evidence to logistics tracking/status alignment matching logic
  fields:
    primary_keys:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - courier_partner
    normalization_steps:
    - Use AWB/tracking number from operational source as the primary handoff key. Do not create courier settlement/account
      cards unless the logistics document supplies settlement evidence.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.awb_missing_in_logistics
  name: awb missing in logistics
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
    category_key: awb_missing_in_logistics
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.delivered_in_logistics_not_delivered_in_operations
  name: delivered in logistics not delivered in operations
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
    category_key: delivered_in_logistics_not_delivered_in_operations
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.rto_status_conflict
  name: rto status conflict
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
    category_key: rto_status_conflict
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.courier_name_normalization_gap
  name: courier name normalization gap
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
    category_key: courier_name_normalization_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.shipment_date_gap
  name: shipment date gap
  fields:
    profile_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
    category_key: shipment_date_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.unicommerce_shipment_to_logistics_tracking
  name: Unicommerce shipment evidence to logistics tracking/status alignment query pattern
  fields:
    intent: Unicommerce shipment evidence to logistics tracking/status alignment
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.unicommerce_shipment_to_logistics_tracking.key_normalization
  name: Unicommerce shipment evidence to logistics tracking/status alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Use AWB/tracking number from operational source as the primary handoff key. Do not create courier settlement/account
      cards unless the logistics document supplies settlement evidence.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.unicommerce_shipment_to_logistics_tracking.account_scope_deferred
  name: Unicommerce shipment evidence to logistics tracking/status alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.unicommerce_shipment_to_logistics_tracking.coverage_and_reference_integrity
  name: Unicommerce shipment evidence to logistics tracking/status alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.unicommerce_shipment_to_logistics_tracking.amount_and_status_consistency
  name: Unicommerce shipment evidence to logistics tracking/status alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.unicommerce_shipment_to_logistics_tracking
  name: Unicommerce shipment evidence to logistics tracking/status alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.unicommerce_shipment_to_logistics_tracking
  name: Unicommerce shipment evidence to logistics tracking/status alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.increff_dispatch_to_logistics_awb
  name: Increff dispatch / AWB evidence to logistics shipment alignment
  fields:
    domain_id: domain.cross_domain.operations_logistics
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Increff WMS dispatch side
    - Logistics vendor shipment/status side
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  name: Increff dispatch / AWB evidence to logistics shipment alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.increff_dispatch_to_logistics_awb
    source_side_id: reconciliation_side.cross_domain.increff_dispatch_to_logistics_awb.source
    target_side_id: reconciliation_side.cross_domain.increff_dispatch_to_logistics_awb.target
    primary_unit_id: reconciliation_unit.cross_domain.awb_or_channel_order
    matching_logic_id: matching_logic.cross_domain.increff_dispatch_to_logistics_awb
    primary_keys:
    - awb
    - other_id
    - channel_order_id
    - order_id
    - shipment_id
    - tracking_id
    normalization_rules:
    - Treat Increff other_id / AWB-style fields as operational tracking identifiers. Link to logistics cards only when logistics
      evidence owns the courier/shipment status.
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.increff_dispatch_to_logistics_awb.source
  name: Increff WMS dispatch side
  fields:
    side_role: source_or_expected
    side_description: Increff WMS dispatch side
    anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    key_candidates:
    - awb
    - other_id
    - channel_order_id
    - order_id
    - shipment_id
    - tracking_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.increff_dispatch_to_logistics_awb.target
  name: Logistics vendor shipment/status side
  fields:
    side_role: target_or_actual
    side_description: Logistics vendor shipment/status side
    anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    key_candidates:
    - awb
    - other_id
    - channel_order_id
    - order_id
    - shipment_id
    - tracking_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.awb_or_channel_order
  name: awb or channel order
  fields:
    unit_key: awb_or_channel_order
    candidate_keys:
    - awb
    - other_id
    - channel_order_id
    - order_id
    - shipment_id
    - tracking_id
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.increff_dispatch_to_logistics_awb
  name: Increff dispatch / AWB evidence to logistics shipment alignment matching logic
  fields:
    primary_keys:
    - awb
    - other_id
    - channel_order_id
    - order_id
    - shipment_id
    - tracking_id
    normalization_steps:
    - Treat Increff other_id / AWB-style fields as operational tracking identifiers. Link to logistics cards only when logistics
      evidence owns the courier/shipment status.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.dispatch_without_logistics_shipment
  name: dispatch without logistics shipment
  fields:
    profile_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
    category_key: dispatch_without_logistics_shipment
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.logistics_shipment_without_dispatch
  name: logistics shipment without dispatch
  fields:
    profile_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
    category_key: logistics_shipment_without_dispatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.awb_reused_or_duplicated
  name: awb reused or duplicated
  fields:
    profile_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
    category_key: awb_reused_or_duplicated
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.status_mismatch
  name: status mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
    category_key: status_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.date_sequence_violation
  name: date sequence violation
  fields:
    profile_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
    category_key: date_sequence_violation
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.increff_dispatch_to_logistics_awb
  name: Increff dispatch / AWB evidence to logistics shipment alignment query pattern
  fields:
    intent: Increff dispatch / AWB evidence to logistics shipment alignment
    source_anchor_sets:
    - anchor_set.operations.tables
    - anchor_set.operations.relationships
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.increff_dispatch_to_logistics_awb.key_normalization
  name: Increff dispatch / AWB evidence to logistics shipment alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Treat Increff other_id / AWB-style fields as operational tracking identifiers. Link to logistics cards only
      when logistics evidence owns the courier/shipment status.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.increff_dispatch_to_logistics_awb.account_scope_deferred
  name: Increff dispatch / AWB evidence to logistics shipment alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.increff_dispatch_to_logistics_awb.coverage_and_reference_integrity
  name: Increff dispatch / AWB evidence to logistics shipment alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.increff_dispatch_to_logistics_awb.amount_and_status_consistency
  name: Increff dispatch / AWB evidence to logistics shipment alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.increff_dispatch_to_logistics_awb
  name: Increff dispatch / AWB evidence to logistics shipment alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.increff_dispatch_to_logistics_awb
  name: Increff dispatch / AWB evidence to logistics shipment alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.marketplace_shipment_to_logistics_tracking
  name: Marketplace shipment identifiers to logistics tracking/status alignment
  fields:
    domain_id: domain.cross_domain.marketplace_logistics
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Marketplace shipment / settlement side
    - Logistics shipment/status side
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.marketplace.settlement_tables
    - anchor_set.marketplace.return_tables
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  name: Marketplace shipment identifiers to logistics tracking/status alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.marketplace_shipment_to_logistics_tracking
    source_side_id: reconciliation_side.cross_domain.marketplace_shipment_to_logistics_tracking.source
    target_side_id: reconciliation_side.cross_domain.marketplace_shipment_to_logistics_tracking.target
    primary_unit_id: reconciliation_unit.cross_domain.awb_or_shipment_or_order_item
    matching_logic_id: matching_logic.cross_domain.marketplace_shipment_to_logistics_tracking
    primary_keys:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - order_item_id
    - return_id
    normalization_rules:
    - Do not turn marketplace shipping fields into logistics-domain cards; use logistics anchors for carrier status and cost
      evidence.
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.marketplace.settlement_tables
    - anchor_set.marketplace.return_tables
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_shipment_to_logistics_tracking.source
  name: Marketplace shipment / settlement side
  fields:
    side_role: source_or_expected
    side_description: Marketplace shipment / settlement side
    anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.marketplace.settlement_tables
    - anchor_set.marketplace.return_tables
    key_candidates:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - order_item_id
    - return_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_shipment_to_logistics_tracking.target
  name: Logistics shipment/status side
  fields:
    side_role: target_or_actual
    side_description: Logistics shipment/status side
    anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    key_candidates:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - order_item_id
    - return_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.awb_or_shipment_or_order_item
  name: awb or shipment or order item
  fields:
    unit_key: awb_or_shipment_or_order_item
    candidate_keys:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - order_item_id
    - return_id
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.marketplace_shipment_to_logistics_tracking
  name: Marketplace shipment identifiers to logistics tracking/status alignment matching logic
  fields:
    primary_keys:
    - awb
    - tracking_id
    - shipment_id
    - order_id
    - order_item_id
    - return_id
    normalization_steps:
    - Do not turn marketplace shipping fields into logistics-domain cards; use logistics anchors for carrier status and cost
      evidence.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.marketplace_shipment_without_logistics_status
  name: marketplace shipment without logistics status
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
    category_key: marketplace_shipment_without_logistics_status
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.logistics_status_without_marketplace_shipment
  name: logistics status without marketplace shipment
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
    category_key: logistics_status_without_marketplace_shipment
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.shipping_identifier_mismatch
  name: shipping identifier mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
    category_key: shipping_identifier_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.delivered_rto_conflict
  name: delivered rto conflict
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
    category_key: delivered_rto_conflict
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.return_event_missing
  name: return event missing
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
    category_key: return_event_missing
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.marketplace_shipment_to_logistics_tracking
  name: Marketplace shipment identifiers to logistics tracking/status alignment query pattern
  fields:
    intent: Marketplace shipment identifiers to logistics tracking/status alignment
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.marketplace.settlement_tables
    - anchor_set.marketplace.return_tables
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_shipment_to_logistics_tracking.key_normalization
  name: Marketplace shipment identifiers to logistics tracking/status alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Do not turn marketplace shipping fields into logistics-domain cards; use logistics anchors for carrier status
      and cost evidence.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_shipment_to_logistics_tracking.account_scope_deferred
  name: Marketplace shipment identifiers to logistics tracking/status alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_shipment_to_logistics_tracking.coverage_and_reference_integrity
  name: Marketplace shipment identifiers to logistics tracking/status alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_shipment_to_logistics_tracking.amount_and_status_consistency
  name: Marketplace shipment identifiers to logistics tracking/status alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.marketplace_shipment_to_logistics_tracking
  name: Marketplace shipment identifiers to logistics tracking/status alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.marketplace_shipment_to_logistics_tracking
  name: Marketplace shipment identifiers to logistics tracking/status alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.marketplace_rto_return_to_logistics_event
  name: Marketplace RTO / return evidence to logistics return event alignment
  fields:
    domain_id: domain.cross_domain.marketplace_logistics
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Marketplace return / reverse side
    - Logistics RTO/return event side
    source_anchor_sets:
    - anchor_set.marketplace.return_tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  name: Marketplace RTO / return evidence to logistics return event alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.marketplace_rto_return_to_logistics_event
    source_side_id: reconciliation_side.cross_domain.marketplace_rto_return_to_logistics_event.source
    target_side_id: reconciliation_side.cross_domain.marketplace_rto_return_to_logistics_event.target
    primary_unit_id: reconciliation_unit.cross_domain.return_or_awb_or_order_item
    matching_logic_id: matching_logic.cross_domain.marketplace_rto_return_to_logistics_event
    primary_keys:
    - return_id
    - order_id
    - order_item_id
    - awb
    - tracking_id
    - rto_status
    normalization_rules:
    - Separate customer return, courier return/RTO, cancellation, and reverse rows before joining.
    source_anchor_sets:
    - anchor_set.marketplace.return_tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_rto_return_to_logistics_event.source
  name: Marketplace return / reverse side
  fields:
    side_role: source_or_expected
    side_description: Marketplace return / reverse side
    anchor_sets:
    - anchor_set.marketplace.return_tables
    - anchor_set.marketplace.reconciliation_profiles
    key_candidates:
    - return_id
    - order_id
    - order_item_id
    - awb
    - tracking_id
    - rto_status
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_rto_return_to_logistics_event.target
  name: Logistics RTO/return event side
  fields:
    side_role: target_or_actual
    side_description: Logistics RTO/return event side
    anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    key_candidates:
    - return_id
    - order_id
    - order_item_id
    - awb
    - tracking_id
    - rto_status
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.return_or_awb_or_order_item
  name: return or awb or order item
  fields:
    unit_key: return_or_awb_or_order_item
    candidate_keys:
    - return_id
    - order_id
    - order_item_id
    - awb
    - tracking_id
    - rto_status
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.marketplace_rto_return_to_logistics_event
  name: Marketplace RTO / return evidence to logistics return event alignment matching logic
  fields:
    primary_keys:
    - return_id
    - order_id
    - order_item_id
    - awb
    - tracking_id
    - rto_status
    normalization_steps:
    - Separate customer return, courier return/RTO, cancellation, and reverse rows before joining.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.return_without_logistics_event
  name: return without logistics event
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
    category_key: return_without_logistics_event
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.logistics_rto_without_marketplace_return
  name: logistics rto without marketplace return
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
    category_key: logistics_rto_without_marketplace_return
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.return_type_conflict
  name: return type conflict
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
    category_key: return_type_conflict
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.amount_or_fee_variance
  name: amount or fee variance
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
    category_key: amount_or_fee_variance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.timing_gap
  name: timing gap
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
    category_key: timing_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.marketplace_rto_return_to_logistics_event
  name: Marketplace RTO / return evidence to logistics return event alignment query pattern
  fields:
    intent: Marketplace RTO / return evidence to logistics return event alignment
    source_anchor_sets:
    - anchor_set.marketplace.return_tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    target_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_rto_return_to_logistics_event.key_normalization
  name: Marketplace RTO / return evidence to logistics return event alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Separate customer return, courier return/RTO, cancellation, and reverse rows before joining.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_rto_return_to_logistics_event.account_scope_deferred
  name: Marketplace RTO / return evidence to logistics return event alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_rto_return_to_logistics_event.coverage_and_reference_integrity
  name: Marketplace RTO / return evidence to logistics return event alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_rto_return_to_logistics_event.amount_and_status_consistency
  name: Marketplace RTO / return evidence to logistics return event alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.marketplace_rto_return_to_logistics_event
  name: Marketplace RTO / return evidence to logistics return event alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.marketplace_rto_return_to_logistics_event
  name: Marketplace RTO / return evidence to logistics return event alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment
  fields:
    domain_id: domain.cross_domain.marketplace_logistics
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Marketplace settlement shipping fee side
    - Logistics freight / invoice / settlement side
    source_anchor_sets:
    - anchor_set.marketplace.settlement_tables
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    source_side_id: reconciliation_side.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.source
    target_side_id: reconciliation_side.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.target
    primary_unit_id: reconciliation_unit.cross_domain.shipment_or_awb_or_order_item
    matching_logic_id: matching_logic.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    primary_keys:
    - awb
    - shipment_id
    - order_id
    - order_item_id
    - invoice_number
    - weight_slab
    normalization_rules:
    - Compare marketplace-side shipping/freight charges to logistics-side freight/invoice evidence only when both domains
      provide amount components and grain.
    source_anchor_sets:
    - anchor_set.marketplace.settlement_tables
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.source
  name: Marketplace settlement shipping fee side
  fields:
    side_role: source_or_expected
    side_description: Marketplace settlement shipping fee side
    anchor_sets:
    - anchor_set.marketplace.settlement_tables
    key_candidates:
    - awb
    - shipment_id
    - order_id
    - order_item_id
    - invoice_number
    - weight_slab
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.target
  name: Logistics freight / invoice / settlement side
  fields:
    side_role: target_or_actual
    side_description: Logistics freight / invoice / settlement side
    anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    key_candidates:
    - awb
    - shipment_id
    - order_id
    - order_item_id
    - invoice_number
    - weight_slab
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.shipment_or_awb_or_order_item
  name: shipment or awb or order item
  fields:
    unit_key: shipment_or_awb_or_order_item
    candidate_keys:
    - awb
    - shipment_id
    - order_id
    - order_item_id
    - invoice_number
    - weight_slab
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment matching logic
  fields:
    primary_keys:
    - awb
    - shipment_id
    - order_id
    - order_item_id
    - invoice_number
    - weight_slab
    normalization_steps:
    - Compare marketplace-side shipping/freight charges to logistics-side freight/invoice evidence only when both domains
      provide amount components and grain.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.shipping_fee_without_logistics_cost
  name: shipping fee without logistics cost
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    category_key: shipping_fee_without_logistics_cost
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.logistics_cost_without_marketplace_charge
  name: logistics cost without marketplace charge
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    category_key: logistics_cost_without_marketplace_charge
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.freight_amount_variance
  name: freight amount variance
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    category_key: freight_amount_variance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.weight_slab_mismatch
  name: weight slab mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    category_key: weight_slab_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.tax_or_fee_component_mismatch
  name: tax or fee component mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    category_key: tax_or_fee_component_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment query pattern
  fields:
    intent: Marketplace shipping fee / freight true-up to logistics freight cost alignment
    source_anchor_sets:
    - anchor_set.marketplace.settlement_tables
    target_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    target_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.key_normalization
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Compare marketplace-side shipping/freight charges to logistics-side freight/invoice evidence only when both
      domains provide amount components and grain.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.account_scope_deferred
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.coverage_and_reference_integrity
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.amount_and_status_consistency
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.payment_gateway_capture_to_order
  name: Payment gateway pay-in capture to order evidence alignment
  fields:
    domain_id: domain.cross_domain.payment_operations
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Order / invoice side
    - Payment gateway pay-in side
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.operations.tables
    target_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  name: Payment gateway pay-in capture to order evidence alignment reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.payment_gateway_capture_to_order
    source_side_id: reconciliation_side.cross_domain.payment_gateway_capture_to_order.source
    target_side_id: reconciliation_side.cross_domain.payment_gateway_capture_to_order.target
    primary_unit_id: reconciliation_unit.cross_domain.order_or_payment_transaction
    matching_logic_id: matching_logic.cross_domain.payment_gateway_capture_to_order
    primary_keys:
    - order_id
    - gateway_order_id
    - payment_id
    - transaction_id
    - rrn
    - payment_mode
    normalization_rules:
    - Gateway order IDs, payment IDs, RRNs, and transaction IDs must be parsed from the relevant payment gateway card family;
      do not infer payment success from marketplace/order status alone.
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.operations.tables
    target_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.payment_gateway_capture_to_order.source
  name: Order / invoice side
  fields:
    side_role: source_or_expected
    side_description: Order / invoice side
    anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.operations.tables
    key_candidates:
    - order_id
    - gateway_order_id
    - payment_id
    - transaction_id
    - rrn
    - payment_mode
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.payment_gateway_capture_to_order.target
  name: Payment gateway pay-in side
  fields:
    side_role: target_or_actual
    side_description: Payment gateway pay-in side
    anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.relationships
    key_candidates:
    - order_id
    - gateway_order_id
    - payment_id
    - transaction_id
    - rrn
    - payment_mode
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.order_or_payment_transaction
  name: order or payment transaction
  fields:
    unit_key: order_or_payment_transaction
    candidate_keys:
    - order_id
    - gateway_order_id
    - payment_id
    - transaction_id
    - rrn
    - payment_mode
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.payment_gateway_capture_to_order
  name: Payment gateway pay-in capture to order evidence alignment matching logic
  fields:
    primary_keys:
    - order_id
    - gateway_order_id
    - payment_id
    - transaction_id
    - rrn
    - payment_mode
    normalization_steps:
    - Gateway order IDs, payment IDs, RRNs, and transaction IDs must be parsed from the relevant payment gateway card family;
      do not infer payment success from marketplace/order status alone.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.order_without_payment_capture
  name: order without payment capture
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
    category_key: order_without_payment_capture
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.payment_without_order
  name: payment without order
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
    category_key: payment_without_order
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.amount_variance
  name: amount variance
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
    category_key: amount_variance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.payment_status_mismatch
  name: payment status mismatch
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
    category_key: payment_status_mismatch
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.gateway_reference_missing
  name: gateway reference missing
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
    category_key: gateway_reference_missing
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.payment_gateway_capture_to_order
  name: Payment gateway pay-in capture to order evidence alignment query pattern
  fields:
    intent: Payment gateway pay-in capture to order evidence alignment
    source_anchor_sets:
    - anchor_set.marketplace.order_tables
    - anchor_set.operations.tables
    target_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.payment_gateway_capture_to_order.key_normalization
  name: Payment gateway pay-in capture to order evidence alignment key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Gateway order IDs, payment IDs, RRNs, and transaction IDs must be parsed from the relevant payment gateway
      card family; do not infer payment success from marketplace/order status alone.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.payment_gateway_capture_to_order.account_scope_deferred
  name: Payment gateway pay-in capture to order evidence alignment account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.payment_gateway_capture_to_order.coverage_and_reference_integrity
  name: Payment gateway pay-in capture to order evidence alignment coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.payment_gateway_capture_to_order.amount_and_status_consistency
  name: Payment gateway pay-in capture to order evidence alignment amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.payment_gateway_capture_to_order
  name: Payment gateway pay-in capture to order evidence alignment output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.payment_gateway_capture_to_order
  name: Payment gateway pay-in capture to order evidence alignment execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.payment_gateway_payout_to_bank_credit
  name: Payment gateway settlement / payout to bank credit reconciliation
  fields:
    domain_id: domain.cross_domain.payment_bank
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Payment gateway payout / settlement side
    - Bank statement credit side
    source_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  name: Payment gateway settlement / payout to bank credit reconciliation reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.payment_gateway_payout_to_bank_credit
    source_side_id: reconciliation_side.cross_domain.payment_gateway_payout_to_bank_credit.source
    target_side_id: reconciliation_side.cross_domain.payment_gateway_payout_to_bank_credit.target
    primary_unit_id: reconciliation_unit.cross_domain.utr_or_payout_batch_or_bank_transaction
    matching_logic_id: matching_logic.cross_domain.payment_gateway_payout_to_bank_credit
    primary_keys:
    - utr
    - rrn
    - payout_id
    - settlement_id
    - bank_reference
    - cheque_no
    - narration_reference
    normalization_rules:
    - Use bank-specific reference extraction before matching gateway payout UTR/RRN to bank credit references or narration
      text.
    source_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.payment_gateway_payout_to_bank_credit.source
  name: Payment gateway payout / settlement side
  fields:
    side_role: source_or_expected
    side_description: Payment gateway payout / settlement side
    anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.reconciliation_profiles
    key_candidates:
    - utr
    - rrn
    - payout_id
    - settlement_id
    - bank_reference
    - cheque_no
    - narration_reference
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.payment_gateway_payout_to_bank_credit.target
  name: Bank statement credit side
  fields:
    side_role: target_or_actual
    side_description: Bank statement credit side
    anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    key_candidates:
    - utr
    - rrn
    - payout_id
    - settlement_id
    - bank_reference
    - cheque_no
    - narration_reference
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.utr_or_payout_batch_or_bank_transaction
  name: utr or payout batch or bank transaction
  fields:
    unit_key: utr_or_payout_batch_or_bank_transaction
    candidate_keys:
    - utr
    - rrn
    - payout_id
    - settlement_id
    - bank_reference
    - cheque_no
    - narration_reference
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.payment_gateway_payout_to_bank_credit
  name: Payment gateway settlement / payout to bank credit reconciliation matching logic
  fields:
    primary_keys:
    - utr
    - rrn
    - payout_id
    - settlement_id
    - bank_reference
    - cheque_no
    - narration_reference
    normalization_steps:
    - Use bank-specific reference extraction before matching gateway payout UTR/RRN to bank credit references or narration
      text.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.gateway_payout_missing_bank_credit
  name: gateway payout missing bank credit
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
    category_key: gateway_payout_missing_bank_credit
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.bank_credit_missing_gateway_payout
  name: bank credit missing gateway payout
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
    category_key: bank_credit_missing_gateway_payout
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.utr_reference_parse_gap
  name: utr reference parse gap
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
    category_key: utr_reference_parse_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.amount_variance
  name: amount variance
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
    category_key: amount_variance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.settlement_timing_gap
  name: settlement timing gap
  fields:
    profile_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
    category_key: settlement_timing_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.payment_gateway_payout_to_bank_credit
  name: Payment gateway settlement / payout to bank credit reconciliation query pattern
  fields:
    intent: Payment gateway settlement / payout to bank credit reconciliation
    source_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.payment_gateway_payout_to_bank_credit.key_normalization
  name: Payment gateway settlement / payout to bank credit reconciliation key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Use bank-specific reference extraction before matching gateway payout UTR/RRN to bank credit references or
      narration text.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.payment_gateway_payout_to_bank_credit.account_scope_deferred
  name: Payment gateway settlement / payout to bank credit reconciliation account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.payment_gateway_payout_to_bank_credit.coverage_and_reference_integrity
  name: Payment gateway settlement / payout to bank credit reconciliation coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.payment_gateway_payout_to_bank_credit.amount_and_status_consistency
  name: Payment gateway settlement / payout to bank credit reconciliation amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.payment_gateway_payout_to_bank_credit
  name: Payment gateway settlement / payout to bank credit reconciliation output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.payment_gateway_payout_to_bank_credit
  name: Payment gateway settlement / payout to bank credit reconciliation execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.marketplace_settlement_to_bank_credit
  name: Marketplace settlement / disbursement to bank credit reconciliation
  fields:
    domain_id: domain.cross_domain.marketplace_bank
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Marketplace settlement / disbursement side
    - Bank statement credit side
    source_anchor_sets:
    - anchor_set.marketplace.settlement_tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  name: Marketplace settlement / disbursement to bank credit reconciliation reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.marketplace_settlement_to_bank_credit
    source_side_id: reconciliation_side.cross_domain.marketplace_settlement_to_bank_credit.source
    target_side_id: reconciliation_side.cross_domain.marketplace_settlement_to_bank_credit.target
    primary_unit_id: reconciliation_unit.cross_domain.settlement_id_or_utr_or_bank_transaction
    matching_logic_id: matching_logic.cross_domain.marketplace_settlement_to_bank_credit
    primary_keys:
    - settlement_id
    - utr
    - disbursement_id
    - bank_reference
    - chq_ref_no
    - narration_reference
    - amount
    - settlement_date
    normalization_rules:
    - Marketplace settlement references and UTR-like values are marketplace columns until linked to bank reference-extraction
      evidence. Tenant/account destination bank selection is deferred.
    source_anchor_sets:
    - anchor_set.marketplace.settlement_tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_settlement_to_bank_credit.source
  name: Marketplace settlement / disbursement side
  fields:
    side_role: source_or_expected
    side_description: Marketplace settlement / disbursement side
    anchor_sets:
    - anchor_set.marketplace.settlement_tables
    - anchor_set.marketplace.reconciliation_profiles
    key_candidates:
    - settlement_id
    - utr
    - disbursement_id
    - bank_reference
    - chq_ref_no
    - narration_reference
    - amount
    - settlement_date
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.marketplace_settlement_to_bank_credit.target
  name: Bank statement credit side
  fields:
    side_role: target_or_actual
    side_description: Bank statement credit side
    anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    key_candidates:
    - settlement_id
    - utr
    - disbursement_id
    - bank_reference
    - chq_ref_no
    - narration_reference
    - amount
    - settlement_date
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.settlement_id_or_utr_or_bank_transaction
  name: settlement id or utr or bank transaction
  fields:
    unit_key: settlement_id_or_utr_or_bank_transaction
    candidate_keys:
    - settlement_id
    - utr
    - disbursement_id
    - bank_reference
    - chq_ref_no
    - narration_reference
    - amount
    - settlement_date
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.marketplace_settlement_to_bank_credit
  name: Marketplace settlement / disbursement to bank credit reconciliation matching logic
  fields:
    primary_keys:
    - settlement_id
    - utr
    - disbursement_id
    - bank_reference
    - chq_ref_no
    - narration_reference
    - amount
    - settlement_date
    normalization_steps:
    - Marketplace settlement references and UTR-like values are marketplace columns until linked to bank reference-extraction
      evidence. Tenant/account destination bank selection is deferred.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.settlement_missing_bank_credit
  name: settlement missing bank credit
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
    category_key: settlement_missing_bank_credit
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.bank_credit_missing_settlement
  name: bank credit missing settlement
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
    category_key: bank_credit_missing_settlement
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.reference_extraction_gap
  name: reference extraction gap
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
    category_key: reference_extraction_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.amount_variance
  name: amount variance
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
    category_key: amount_variance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.bank_date_timing_gap
  name: bank date timing gap
  fields:
    profile_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
    category_key: bank_date_timing_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.marketplace_settlement_to_bank_credit
  name: Marketplace settlement / disbursement to bank credit reconciliation query pattern
  fields:
    intent: Marketplace settlement / disbursement to bank credit reconciliation
    source_anchor_sets:
    - anchor_set.marketplace.settlement_tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_settlement_to_bank_credit.key_normalization
  name: Marketplace settlement / disbursement to bank credit reconciliation key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Marketplace settlement references and UTR-like values are marketplace columns until linked to bank reference-extraction
      evidence. Tenant/account destination bank selection is deferred.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.marketplace_settlement_to_bank_credit.account_scope_deferred
  name: Marketplace settlement / disbursement to bank credit reconciliation account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_settlement_to_bank_credit.coverage_and_reference_integrity
  name: Marketplace settlement / disbursement to bank credit reconciliation coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.marketplace_settlement_to_bank_credit.amount_and_status_consistency
  name: Marketplace settlement / disbursement to bank credit reconciliation amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.marketplace_settlement_to_bank_credit
  name: Marketplace settlement / disbursement to bank credit reconciliation output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.marketplace_settlement_to_bank_credit
  name: Marketplace settlement / disbursement to bank credit reconciliation execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.logistics_cod_remittance_to_bank_credit
  name: Logistics COD remittance to bank credit reconciliation
  fields:
    domain_id: domain.cross_domain.logistics_bank
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Logistics COD remittance / settlement side
    - Bank statement credit side
    source_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  name: Logistics COD remittance to bank credit reconciliation reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.logistics_cod_remittance_to_bank_credit
    source_side_id: reconciliation_side.cross_domain.logistics_cod_remittance_to_bank_credit.source
    target_side_id: reconciliation_side.cross_domain.logistics_cod_remittance_to_bank_credit.target
    primary_unit_id: reconciliation_unit.cross_domain.cod_remittance_or_awb_or_bank_transaction
    matching_logic_id: matching_logic.cross_domain.logistics_cod_remittance_to_bank_credit
    primary_keys:
    - awb
    - remittance_id
    - settlement_id
    - utr
    - bank_reference
    - cod_amount
    - courier_partner
    normalization_rules:
    - Use logistics COD remittance evidence as source side and bank reference extraction as target side. Do not use marketplace
      settlement tables as COD remittance source unless a Business Flow Binding later defines that route.
    source_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.logistics_cod_remittance_to_bank_credit.source
  name: Logistics COD remittance / settlement side
  fields:
    side_role: source_or_expected
    side_description: Logistics COD remittance / settlement side
    anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    key_candidates:
    - awb
    - remittance_id
    - settlement_id
    - utr
    - bank_reference
    - cod_amount
    - courier_partner
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.logistics_cod_remittance_to_bank_credit.target
  name: Bank statement credit side
  fields:
    side_role: target_or_actual
    side_description: Bank statement credit side
    anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    key_candidates:
    - awb
    - remittance_id
    - settlement_id
    - utr
    - bank_reference
    - cod_amount
    - courier_partner
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.cod_remittance_or_awb_or_bank_transaction
  name: cod remittance or awb or bank transaction
  fields:
    unit_key: cod_remittance_or_awb_or_bank_transaction
    candidate_keys:
    - awb
    - remittance_id
    - settlement_id
    - utr
    - bank_reference
    - cod_amount
    - courier_partner
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.logistics_cod_remittance_to_bank_credit
  name: Logistics COD remittance to bank credit reconciliation matching logic
  fields:
    primary_keys:
    - awb
    - remittance_id
    - settlement_id
    - utr
    - bank_reference
    - cod_amount
    - courier_partner
    normalization_steps:
    - Use logistics COD remittance evidence as source side and bank reference extraction as target side. Do not use marketplace
      settlement tables as COD remittance source unless a Business Flow Binding later defines that route.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.cod_remittance_missing_bank_credit
  name: cod remittance missing bank credit
  fields:
    profile_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
    category_key: cod_remittance_missing_bank_credit
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.bank_credit_missing_cod_remittance
  name: bank credit missing cod remittance
  fields:
    profile_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
    category_key: bank_credit_missing_cod_remittance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.awb_or_utr_mapping_gap
  name: awb or utr mapping gap
  fields:
    profile_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
    category_key: awb_or_utr_mapping_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.amount_variance
  name: amount variance
  fields:
    profile_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
    category_key: amount_variance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.remittance_timing_gap
  name: remittance timing gap
  fields:
    profile_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
    category_key: remittance_timing_gap
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.logistics_cod_remittance_to_bank_credit
  name: Logistics COD remittance to bank credit reconciliation query pattern
  fields:
    intent: Logistics COD remittance to bank credit reconciliation
    source_anchor_sets:
    - anchor_set.logistics.tables
    - anchor_set.logistics.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.bank.tables
    - anchor_set.bank.reconciliation_profiles
    - anchor_set.bank.relationships
    target_reconciliation_profile: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.logistics_cod_remittance_to_bank_credit.key_normalization
  name: Logistics COD remittance to bank credit reconciliation key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Use logistics COD remittance evidence as source side and bank reference extraction as target side. Do not use
      marketplace settlement tables as COD remittance source unless a Business Flow Binding later defines that route.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.logistics_cod_remittance_to_bank_credit.account_scope_deferred
  name: Logistics COD remittance to bank credit reconciliation account scope deferred rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.logistics_cod_remittance_to_bank_credit.coverage_and_reference_integrity
  name: Logistics COD remittance to bank credit reconciliation coverage and reference-integrity validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.logistics_cod_remittance_to_bank_credit.amount_and_status_consistency
  name: Logistics COD remittance to bank credit reconciliation amount/status consistency validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.logistics_cod_remittance_to_bank_credit
  name: Logistics COD remittance to bank credit reconciliation output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.logistics_cod_remittance_to_bank_credit
  name: Logistics COD remittance to bank credit reconciliation execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cross_domain.refund_to_payment_gateway_and_marketplace_return
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway
  fields:
    domain_id: domain.cross_domain.refund_chargeback
    process_family: cross_domain_reference_flow
    participant_domain_roles:
    - Marketplace / operations return side
    - Payment gateway refund / chargeback side
    source_anchor_sets:
    - anchor_set.marketplace.return_tables
    - anchor_set.operations.tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.reconciliation_profiles
    cross_domain_only: true
    tenant_account_specific: false
    requires_business_flow_binding_for_execution: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway reconciliation profile
  fields:
    profile_family: cross_domain_reconciliation_reference
    business_process_id: business_process.cross_domain.refund_to_payment_gateway_and_marketplace_return
    source_side_id: reconciliation_side.cross_domain.refund_to_payment_gateway_and_marketplace_return.source
    target_side_id: reconciliation_side.cross_domain.refund_to_payment_gateway_and_marketplace_return.target
    primary_unit_id: reconciliation_unit.cross_domain.refund_or_order_or_payment_transaction
    matching_logic_id: matching_logic.cross_domain.refund_to_payment_gateway_and_marketplace_return
    primary_keys:
    - order_id
    - refund_id
    - payment_id
    - transaction_id
    - return_id
    - original_payment_reference
    normalization_rules:
    - Separate marketplace refunds, operational returns, customer returns, courier returns/RTO, chargebacks, and payment gateway
      refund records before matching.
    source_anchor_sets:
    - anchor_set.marketplace.return_tables
    - anchor_set.operations.tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.reconciliation_profiles
    not_account_specific: true
    business_flow_binding_required_for_runtime: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.refund_to_payment_gateway_and_marketplace_return.source
  name: Marketplace / operations return side
  fields:
    side_role: source_or_expected
    side_description: Marketplace / operations return side
    anchor_sets:
    - anchor_set.marketplace.return_tables
    - anchor_set.operations.tables
    - anchor_set.marketplace.reconciliation_profiles
    key_candidates:
    - order_id
    - refund_id
    - payment_id
    - transaction_id
    - return_id
    - original_payment_reference
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cross_domain.refund_to_payment_gateway_and_marketplace_return.target
  name: Payment gateway refund / chargeback side
  fields:
    side_role: target_or_actual
    side_description: Payment gateway refund / chargeback side
    anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.reconciliation_profiles
    key_candidates:
    - order_id
    - refund_id
    - payment_id
    - transaction_id
    - return_id
    - original_payment_reference
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cross_domain.refund_or_order_or_payment_transaction
  name: refund or order or payment transaction
  fields:
    unit_key: refund_or_order_or_payment_transaction
    candidate_keys:
    - order_id
    - refund_id
    - payment_id
    - transaction_id
    - return_id
    - original_payment_reference
    scope: cross_domain_reference
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cross_domain.refund_to_payment_gateway_and_marketplace_return
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway matching logic
  fields:
    primary_keys:
    - order_id
    - refund_id
    - payment_id
    - transaction_id
    - return_id
    - original_payment_reference
    normalization_steps:
    - Separate marketplace refunds, operational returns, customer returns, courier returns/RTO, chargebacks, and payment gateway
      refund records before matching.
    grain: derived_from_primary_unit
    aggregation_policy: pre_aggregate_each_side_to_reconciliation_unit_before_amount_or_status_comparison
    timing_policy: allow documented settlement, payout, delivery, return, and bank-posting lag windows; exact windows require
      source-specific cards
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.return_without_refund
  name: return without refund
  fields:
    profile_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
    category_key: return_without_refund
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.refund_without_return
  name: refund without return
  fields:
    profile_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
    category_key: refund_without_return
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.refund_amount_variance
  name: refund amount variance
  fields:
    profile_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
    category_key: refund_amount_variance
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.original_payment_missing
  name: original payment missing
  fields:
    profile_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
    category_key: original_payment_missing
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.chargeback_status_conflict
  name: chargeback status conflict
  fields:
    profile_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
    category_key: chargeback_status_conflict
    domain_scope: cross_domain_reference
    interpretation: Exception category to be specialized by the source-domain markdown and account-specific flow binding.
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.cross_domain.refund_to_payment_gateway_and_marketplace_return
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway query pattern
  fields:
    intent: Refund / reverse transaction alignment across marketplace, operations, and payment gateway
    source_anchor_sets:
    - anchor_set.marketplace.return_tables
    - anchor_set.operations.tables
    - anchor_set.marketplace.reconciliation_profiles
    target_anchor_sets:
    - anchor_set.payment.tables
    - anchor_set.payment.reconciliation_profiles
    target_reconciliation_profile: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
    expected_outputs:
    - source_key
    - target_key
    - source_amount_or_status
    - target_amount_or_status
    - variance_or_status_delta
    - exception_category
    - evidence_refs
    not_sql_template: true
    account_filters_deferred_to_business_flow_binding: true
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.refund_to_payment_gateway_and_marketplace_return.key_normalization
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway key normalization rule
  fields:
    rule_type: key_normalization
    rule_text: Separate marketplace refunds, operational returns, customer returns, courier returns/RTO, chargebacks, and
      payment gateway refund records before matching.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.cross_domain.refund_to_payment_gateway_and_marketplace_return.account_scope_deferred
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway account scope deferred
    rule
  fields:
    rule_type: scope_boundary
    rule_text: Do not hardcode tenant, group, account, bank account, courier account, or seller-account filters in this reference
      layer. Resolve them through platform_account, account_data_binding, business_scope_set, or business_flow_binding docs
      when available.
    applies_to_reconciliation_profile: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
    confidence: high
    review_status: accepted
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.refund_to_payment_gateway_and_marketplace_return.coverage_and_reference_integrity
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway coverage and reference-integrity
    validation
  fields:
    validation_type: coverage_and_key_integrity
    checks:
    - each side has at least one configured source anchor at runtime
    - join key is non-null after source-specific normalization
    - source and target grains are pre-aggregated before comparison
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.cross_domain.refund_to_payment_gateway_and_marketplace_return.amount_and_status_consistency
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway amount/status consistency
    validation
  fields:
    validation_type: amount_status_consistency
    checks:
    - amount comparisons use same sign convention and currency
    - status comparisons use normalized status vocabulary
    - timing gaps are labeled before being treated as hard mismatches
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.cross_domain.refund_to_payment_gateway_and_marketplace_return
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway output contract
  fields:
    required_fields:
    - flow_id
    - source_system
    - target_system
    - reconciliation_unit
    - source_key
    - target_key
    - source_value
    - target_value
    - variance_value
    - status_delta
    - exception_category
    - source_evidence_refs
    - target_evidence_refs
    - review_status
    optional_fields:
    - tenant_id
    - group_id
    - platform_account_id
    - business_scope_set_id
    - business_flow_binding_id
    - currency
    - lag_days
    - normalized_key
    - source_anchor_set
    - target_anchor_set
    confidence: high
    review_status: reference_ready
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.cross_domain.refund_to_payment_gateway_and_marketplace_return
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway execution constraints
  fields:
    constraint_family: cross_domain_reference_execution
    requires_account_scope_for_runtime: true
    pre_execution_requirements:
    - select source and target platform accounts
    - resolve account data binding filters
    - select exact source-domain tables and bank/logistics/payment accounts when relevant
    - apply source-specific key normalization before joining
    forbidden_in_reference_layer:
    - tenant-specific account filters
    - bank account IDs
    - seller account IDs
    - courier account IDs
    - runtime SQL with hardcoded group_level_id
    confidence: high
    review_status: reference_ready
```
## 5. Candidate Edges

```yaml
candidate_edge:
  edge_id: edge.cd5004d4c9d68487
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.marketplace_operations
  target_card_id: business_process.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a650607e837ab402
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: domain.cross_domain.marketplace_operations
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.0b24499bc502f88b
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.c8ec41c7baba04c1
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: business_process.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.14efc58425cfc131
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: reconciliation_side.cross_domain.marketplace_order_to_unicommerce_invoice.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.25da2fdc22f49443
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: reconciliation_side.cross_domain.marketplace_order_to_unicommerce_invoice.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.9543d9b1211cc418
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_order_to_unicommerce_invoice.source
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.afdee907dae9de76
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_order_to_unicommerce_invoice.target
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.894e88d908ac1676
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: reconciliation_unit.cross_domain.order_or_order_item
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.1f20e3b7d9d9af58
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: matching_logic.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.9f35d68226e017ba
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.0c9be329dfca130f
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.missing_in_unicommerce_invoice
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.17ea8ea5f4aeeff6
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.missing_in_marketplace_order_table
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.cecc7ba45a84594a
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.order_status_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.ecdddd5f0b7ca93f
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.amount_or_quantity_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.5fb3118d784c3e5c
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_unicommerce_invoice.key_prefix_normalization_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.5e630a5fadd07c70
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.65723edba824a3ae
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: rule.cross_domain.marketplace_order_to_unicommerce_invoice.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.b6618802d27e6ae9
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: rule.cross_domain.marketplace_order_to_unicommerce_invoice.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.4882446920edf339
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: validation_test.cross_domain.marketplace_order_to_unicommerce_invoice.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.fc6fe31a0a61a338
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: validation_test.cross_domain.marketplace_order_to_unicommerce_invoice.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.617bcdc93c8408e4
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: output_contract.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.01e2909519ea9f5a
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: rule.cross_domain.marketplace_order_to_unicommerce_invoice.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.0e0413958437560d
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: rule.cross_domain.marketplace_order_to_unicommerce_invoice.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.78f9599638995f2b
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: validation_test.cross_domain.marketplace_order_to_unicommerce_invoice.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.14e5a4eee4925691
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: validation_test.cross_domain.marketplace_order_to_unicommerce_invoice.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.9d2ce5f5a89cb050
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: output_contract.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.aa48b6ead3f58998
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: query_pattern.cross_domain.marketplace_order_to_unicommerce_invoice
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ad23a014d8ca040d
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: anchor_set.marketplace.order_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.20ef07180d44e18f
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: anchor_set.marketplace.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.2925608b7384fc23
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: anchor_set.operations.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.25743d69e158f9ff
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  target_card_id: anchor_set.operations.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.093f9aa55f8aea41
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.marketplace_operations
  target_card_id: business_process.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.18337b6dd05d5e7d
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: domain.cross_domain.marketplace_operations
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.3451da295e0badd4
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.6c4cd682276c957b
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: business_process.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.e17a353c0bfc57f2
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: reconciliation_side.cross_domain.marketplace_order_to_increff_wms_dispatch.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.6193644f4573f2ab
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: reconciliation_side.cross_domain.marketplace_order_to_increff_wms_dispatch.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.d04d40cc0dd3e7b2
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_order_to_increff_wms_dispatch.source
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.bd7b989afeaa4cc5
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_order_to_increff_wms_dispatch.target
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.9d3b360a11528087
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: reconciliation_unit.cross_domain.order_or_shipment_or_item
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.72eb0c7342096d39
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: matching_logic.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.489eeea147d3698c
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.dba5f8e86441a85e
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.missing_wms_dispatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.984efc599e6f96fa
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.missing_marketplace_order
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.2454740a9bef55d4
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.sku_or_item_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.a2e4434d76ad409f
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.awb_missing_or_changed
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.b6812b528ddfcb7c
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: mismatch_category.cross_domain.marketplace_order_to_increff_wms_dispatch.channel_mapping_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.fc19242c9833e34b
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.b297a11a0e5af5f9
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: rule.cross_domain.marketplace_order_to_increff_wms_dispatch.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.958f8b024e062c0f
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: rule.cross_domain.marketplace_order_to_increff_wms_dispatch.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.271f7c7278e1cae1
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: validation_test.cross_domain.marketplace_order_to_increff_wms_dispatch.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.9e22384f581ddaa9
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: validation_test.cross_domain.marketplace_order_to_increff_wms_dispatch.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.e5077f317f8c800d
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: output_contract.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.01277d6beb5c0979
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: rule.cross_domain.marketplace_order_to_increff_wms_dispatch.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.8bce66bc290ac01f
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: rule.cross_domain.marketplace_order_to_increff_wms_dispatch.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.7bc4dce3357258b3
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: validation_test.cross_domain.marketplace_order_to_increff_wms_dispatch.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.cb195cb90201cc3d
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: validation_test.cross_domain.marketplace_order_to_increff_wms_dispatch.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.228fefdfc95f49f9
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: output_contract.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a5f006b69a3bf609
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: query_pattern.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.6ac2172e83d1392c
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: anchor_set.marketplace.order_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.d13a49bb49dd6fe7
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: anchor_set.operations.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.1ebedc460c1b0ef6
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  target_card_id: anchor_set.operations.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.580ba83cbf9875c2
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.operations_operations
  target_card_id: business_process.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.49ca0ca31bb942a5
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: domain.cross_domain.operations_operations
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.7b82af5864bed3f2
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.c95f03505464d209
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: business_process.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.0c433dfd60d7ab02
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: reconciliation_side.cross_domain.unicommerce_invoice_to_increff_wms_sales.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.cdc49f45d40d9fa8
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: reconciliation_side.cross_domain.unicommerce_invoice_to_increff_wms_sales.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.b91de70209ecb76b
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.unicommerce_invoice_to_increff_wms_sales.source
  target_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.1ff0489bbe5af0d8
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.unicommerce_invoice_to_increff_wms_sales.target
  target_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.179a3a54cbeb8198
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: reconciliation_unit.cross_domain.order_or_invoice_or_sku
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.eed0077c2b6a19b2
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: matching_logic.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.82b658130f20e7c3
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.bd79463ee1ba2cf8
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.invoice_without_wms_dispatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.3696d28bb8719b51
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.wms_dispatch_without_invoice
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.aa8d14148cc79c35
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.sku_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.ef4ed7029c330691
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.quantity_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.6fe9520a9405524e
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: mismatch_category.cross_domain.unicommerce_invoice_to_increff_wms_sales.status_or_return_classification_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.2e03000337117993
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.9279dbec1bed8c2a
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: rule.cross_domain.unicommerce_invoice_to_increff_wms_sales.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.e56b0a1f931ad359
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: rule.cross_domain.unicommerce_invoice_to_increff_wms_sales.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.da009924023c2767
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: validation_test.cross_domain.unicommerce_invoice_to_increff_wms_sales.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ee0d72142bad1cac
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: validation_test.cross_domain.unicommerce_invoice_to_increff_wms_sales.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.55fe0dca5bf3b6dd
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: output_contract.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.9b36e0ce23472374
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: rule.cross_domain.unicommerce_invoice_to_increff_wms_sales.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.c85e0150397f3866
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: rule.cross_domain.unicommerce_invoice_to_increff_wms_sales.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.f39c122ea3968ffd
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: validation_test.cross_domain.unicommerce_invoice_to_increff_wms_sales.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.9ac1052a1871a147
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: validation_test.cross_domain.unicommerce_invoice_to_increff_wms_sales.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.aefe9af9e8377794
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: output_contract.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.4402ff6bfe0ebf83
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: query_pattern.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.3e9764c14a0b0836
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: anchor_set.operations.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.470a6ba5375ffa31
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: anchor_set.operations.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.279c70fbda80db83
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: anchor_set.operations.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.15c065ec2fac23b6
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  target_card_id: anchor_set.operations.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.8a6acff7f09efc1d
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.operations_logistics
  target_card_id: business_process.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.4bb6519499fb048d
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: domain.cross_domain.operations_logistics
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.f36e9578e8bde735
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.547046f5e80022c5
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: business_process.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.bf5e0e31c862f727
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: reconciliation_side.cross_domain.unicommerce_shipment_to_logistics_tracking.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.29da1f694c1ae563
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: reconciliation_side.cross_domain.unicommerce_shipment_to_logistics_tracking.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.8ba8a17e9c1cf07e
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.unicommerce_shipment_to_logistics_tracking.source
  target_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ac588435f390e3ef
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.unicommerce_shipment_to_logistics_tracking.target
  target_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.295ecb1e15dd4c8e
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: reconciliation_unit.cross_domain.awb_or_shipment
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.4a312696b98525a1
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: matching_logic.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.27ff5a52b1a8ca06
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ba08d06ef2d8c951
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.awb_missing_in_logistics
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.e2c66a548a2c8197
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.delivered_in_logistics_not_delivered_in_operations
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.3adbd64754688a65
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.rto_status_conflict
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.a1ed9923379a42ca
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.courier_name_normalization_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.a46eda127b174386
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.unicommerce_shipment_to_logistics_tracking.shipment_date_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.befc40c95a002f39
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.4f5c87988329e9ea
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: rule.cross_domain.unicommerce_shipment_to_logistics_tracking.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.05928f064b3af64d
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: rule.cross_domain.unicommerce_shipment_to_logistics_tracking.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.c5d8afc21f59ca19
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: validation_test.cross_domain.unicommerce_shipment_to_logistics_tracking.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.6e5364b241ce9933
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: validation_test.cross_domain.unicommerce_shipment_to_logistics_tracking.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.2573443f813f6535
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: output_contract.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.7fc9186a27aacfef
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: rule.cross_domain.unicommerce_shipment_to_logistics_tracking.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.41ba1ae042af81b6
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: rule.cross_domain.unicommerce_shipment_to_logistics_tracking.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.7c88781eaec26dc2
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: validation_test.cross_domain.unicommerce_shipment_to_logistics_tracking.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.e9155e5e2071df7c
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: validation_test.cross_domain.unicommerce_shipment_to_logistics_tracking.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.824f88334e3df0da
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: output_contract.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.4b7aa0ff193a5a58
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: query_pattern.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.9c198db93ab22d0f
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: anchor_set.operations.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.bba84a200d83e71a
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: anchor_set.operations.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.e4067452cc8ba841
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: anchor_set.logistics.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.c39f7c6c094a0baa
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  target_card_id: anchor_set.logistics.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.aeb5d588a3b4fcd3
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.operations_logistics
  target_card_id: business_process.cross_domain.increff_dispatch_to_logistics_awb
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.d928f59a714357b0
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: domain.cross_domain.operations_logistics
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.eb169c5d036833b3
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.090c9459f5318931
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: business_process.cross_domain.increff_dispatch_to_logistics_awb
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.d3f2fcf77fdc6cda
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: reconciliation_side.cross_domain.increff_dispatch_to_logistics_awb.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.1fe58b7f74d43a64
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: reconciliation_side.cross_domain.increff_dispatch_to_logistics_awb.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.e8dab2e47599cf5d
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.increff_dispatch_to_logistics_awb.source
  target_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.82c4845ec695ff5c
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.increff_dispatch_to_logistics_awb.target
  target_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.438d2e4ff62eb568
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: reconciliation_unit.cross_domain.awb_or_channel_order
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.727d6939906551b6
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: matching_logic.cross_domain.increff_dispatch_to_logistics_awb
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.aa17acf3ce762d66
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.2aa515dd29002859
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.dispatch_without_logistics_shipment
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.d0915d8cb3030658
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.logistics_shipment_without_dispatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.eb436d3edd09d03d
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.awb_reused_or_duplicated
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.bb595ce3da6d62fd
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.status_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.8d8c61ed88080343
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: mismatch_category.cross_domain.increff_dispatch_to_logistics_awb.date_sequence_violation
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.5c50d894cdd7f50b
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.773a87b01922f6a3
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: rule.cross_domain.increff_dispatch_to_logistics_awb.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.63ca6818996b9771
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: rule.cross_domain.increff_dispatch_to_logistics_awb.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.92838ce02bff6836
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: validation_test.cross_domain.increff_dispatch_to_logistics_awb.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.781c8bebd30f780f
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: validation_test.cross_domain.increff_dispatch_to_logistics_awb.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.e19b6bb21bc28b8c
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: output_contract.cross_domain.increff_dispatch_to_logistics_awb
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.b3ad18965ec3adf0
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: rule.cross_domain.increff_dispatch_to_logistics_awb.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.dc4eb435eb17c6e0
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: rule.cross_domain.increff_dispatch_to_logistics_awb.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.af2e17761ed0bbb8
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: validation_test.cross_domain.increff_dispatch_to_logistics_awb.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.9c568b8afaaed429
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: validation_test.cross_domain.increff_dispatch_to_logistics_awb.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.28b2eb6016a3afc9
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: output_contract.cross_domain.increff_dispatch_to_logistics_awb
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.0101100380c2a768
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: query_pattern.cross_domain.increff_dispatch_to_logistics_awb
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.2e9956bff5e93810
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: anchor_set.operations.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.b73659854f66de09
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: anchor_set.operations.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.4db37ed62995b0b7
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: anchor_set.logistics.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.a743fda6eab6e267
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  target_card_id: anchor_set.logistics.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.c30ad934a2860c41
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.marketplace_logistics
  target_card_id: business_process.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.b2e06196cfa9bc83
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: domain.cross_domain.marketplace_logistics
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.8c232913b38eac78
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a255f474d75416bd
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: business_process.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.9d5adcee23e60c58
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: reconciliation_side.cross_domain.marketplace_shipment_to_logistics_tracking.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.293c015fe6948d0c
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: reconciliation_side.cross_domain.marketplace_shipment_to_logistics_tracking.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.49a6b9cadbbe5857
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_shipment_to_logistics_tracking.source
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.2dc189d1127ff2c3
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_shipment_to_logistics_tracking.target
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.5451e28d60fedef9
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: reconciliation_unit.cross_domain.awb_or_shipment_or_order_item
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.85e7665343a2b011
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: matching_logic.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.d3f05288bd9cb043
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.1e626f4e13e4df30
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.marketplace_shipment_without_logistics_status
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.bb2aa8edd9c25762
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.logistics_status_without_marketplace_shipment
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.25bbad44c965e680
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.shipping_identifier_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.75de6b8c2e441bfd
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.delivered_rto_conflict
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.9f0ddcbde392abb7
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: mismatch_category.cross_domain.marketplace_shipment_to_logistics_tracking.return_event_missing
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.de833dc4711edf29
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.972bec6d8e446058
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: rule.cross_domain.marketplace_shipment_to_logistics_tracking.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.fba010cecf187259
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: rule.cross_domain.marketplace_shipment_to_logistics_tracking.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ffc8a5f42b1d0a4c
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: validation_test.cross_domain.marketplace_shipment_to_logistics_tracking.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.07161e12a8b63340
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: validation_test.cross_domain.marketplace_shipment_to_logistics_tracking.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.82774d141e5bc104
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: output_contract.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.123510e44f460b41
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: rule.cross_domain.marketplace_shipment_to_logistics_tracking.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.8adf770906106ab9
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: rule.cross_domain.marketplace_shipment_to_logistics_tracking.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.48d9a5ea2457b155
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: validation_test.cross_domain.marketplace_shipment_to_logistics_tracking.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.15b0565c926f42b8
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: validation_test.cross_domain.marketplace_shipment_to_logistics_tracking.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.4f3442f432931b5d
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: output_contract.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.eee6125d1ee2819e
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: query_pattern.cross_domain.marketplace_shipment_to_logistics_tracking
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a37519e5acbe4f52
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: anchor_set.marketplace.order_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.ea7a11277539474d
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: anchor_set.marketplace.settlement_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.0a363091180ab0e4
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: anchor_set.marketplace.return_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.d3f3d22ab7d6f5b9
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: anchor_set.logistics.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.ef011d35b7ee234e
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  target_card_id: anchor_set.logistics.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.af3f17e958764a8d
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.marketplace_logistics
  target_card_id: business_process.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ffc95d3c8f0d87bd
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: domain.cross_domain.marketplace_logistics
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.e9e791cfe1dc3e6b
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.9293b8d3ff4f72f7
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: business_process.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ba2ee821d8ec7579
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: reconciliation_side.cross_domain.marketplace_rto_return_to_logistics_event.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.0b6969e7b97120f5
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: reconciliation_side.cross_domain.marketplace_rto_return_to_logistics_event.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.3dcc3ea8c699b544
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_rto_return_to_logistics_event.source
  target_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.16cfa3d445cc68f5
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_rto_return_to_logistics_event.target
  target_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.c1a41b168dc05170
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: reconciliation_unit.cross_domain.return_or_awb_or_order_item
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.3d94ee23285a8124
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: matching_logic.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.14f7424716368db8
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.85d174ea381706c3
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.return_without_logistics_event
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.500f7ea84842fbe5
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.logistics_rto_without_marketplace_return
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.68a55cb976715d4e
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.return_type_conflict
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.c7a8c6937254daa7
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.amount_or_fee_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.c8fddde167b1198d
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: mismatch_category.cross_domain.marketplace_rto_return_to_logistics_event.timing_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.52d5e50d35e6b343
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.a0019355a4192fff
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: rule.cross_domain.marketplace_rto_return_to_logistics_event.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.97aaab515974e99d
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: rule.cross_domain.marketplace_rto_return_to_logistics_event.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.4e61393c94b61f1e
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: validation_test.cross_domain.marketplace_rto_return_to_logistics_event.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.367eb7a5474d268a
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: validation_test.cross_domain.marketplace_rto_return_to_logistics_event.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.074114e4391aa9d2
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: output_contract.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.cc7531da49f0ff1d
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: rule.cross_domain.marketplace_rto_return_to_logistics_event.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.070facba6ebc3b22
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: rule.cross_domain.marketplace_rto_return_to_logistics_event.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.91db4d68587d543b
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: validation_test.cross_domain.marketplace_rto_return_to_logistics_event.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.25c95afd43c8cf36
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: validation_test.cross_domain.marketplace_rto_return_to_logistics_event.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.d225471ac13fd1cc
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: output_contract.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a3d3864162d00cfd
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: query_pattern.cross_domain.marketplace_rto_return_to_logistics_event
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.d90fa1b29f1d4aec
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: anchor_set.marketplace.return_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.2cd16974e6ecfa7c
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: anchor_set.marketplace.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.cc26252bcb0f891b
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: anchor_set.logistics.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.dd567c24ed8b18db
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  target_card_id: anchor_set.logistics.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.9c50e9a3f4bfd18e
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.marketplace_logistics
  target_card_id: business_process.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.1a1c3b8feeb9ac98
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: domain.cross_domain.marketplace_logistics
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.2a38f106ccc23ca9
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.7a26f6eda324ea93
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: business_process.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.77226469cfc380ee
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: reconciliation_side.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.20130607dc5ac93b
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: reconciliation_side.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.3e42803f3de900c1
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.source
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.5b8fdbf0c4383175
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.target
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.b0a1055529df5855
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: reconciliation_unit.cross_domain.shipment_or_awb_or_order_item
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.16c9ef2d18b80bff
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: matching_logic.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.85e74dec18228ec1
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.419e53fe28db0dfb
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.shipping_fee_without_logistics_cost
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.9fd010e38e4de60e
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.logistics_cost_without_marketplace_charge
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.d34dac7a325b788b
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.freight_amount_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.f71128747fa9547b
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.weight_slab_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.2d282435582bd145
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: mismatch_category.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.tax_or_fee_component_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.6c5a8e20d36ad1ce
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.98708dcf6bac7b72
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: rule.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.81b2a28520df3fb7
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: rule.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.c9fe57d2b2a2eaae
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: validation_test.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.15a69ba13ef62d54
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: validation_test.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.6b537f347c8265b8
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: output_contract.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.9ee08a094fdea018
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: rule.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.2270164ad4045e0b
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: rule.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.1b4218a2dfa274e9
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: validation_test.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.9b883ab780092eec
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: validation_test.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.27dd6e2cc68ba2f6
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: output_contract.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a7235eb52b69f89e
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: query_pattern.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.6fc34bdbb3fd0a6f
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: anchor_set.marketplace.settlement_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.7d71dc085dc7762a
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: anchor_set.logistics.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.53b932f0260e0cd0
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  target_card_id: anchor_set.logistics.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.6b497083dcf0d66e
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.payment_operations
  target_card_id: business_process.cross_domain.payment_gateway_capture_to_order
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ff6408f9ac06060a
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.payment_gateway_capture_to_order
  target_card_id: domain.cross_domain.payment_operations
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.68f4704de7e6e0b6
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.payment_gateway_capture_to_order
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.7b0a404d0cf86194
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: business_process.cross_domain.payment_gateway_capture_to_order
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.be6bfc4942bdeeb9
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: reconciliation_side.cross_domain.payment_gateway_capture_to_order.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.c169d52d632bd2e9
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: reconciliation_side.cross_domain.payment_gateway_capture_to_order.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.0dc55ee349713fce
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.payment_gateway_capture_to_order.source
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.3f23a5ebffd36ad9
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.payment_gateway_capture_to_order.target
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.cb61b16df3a78116
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: reconciliation_unit.cross_domain.order_or_payment_transaction
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.fbecc52c694638a4
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: matching_logic.cross_domain.payment_gateway_capture_to_order
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.bb6cec550c7f4963
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.payment_gateway_capture_to_order
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.84f10da277175501
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.order_without_payment_capture
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.89203c2b0a3326d7
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.payment_without_order
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.9ad4336974111b18
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.amount_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.9e180b5a7999c772
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.payment_status_mismatch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.b9ec0805d6048a1b
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: mismatch_category.cross_domain.payment_gateway_capture_to_order.gateway_reference_missing
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.2a28af48ef152eb1
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.payment_gateway_capture_to_order
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.2b9b788cbacf90d2
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.payment_gateway_capture_to_order
  target_card_id: rule.cross_domain.payment_gateway_capture_to_order.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.0160628ef2790a59
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.payment_gateway_capture_to_order
  target_card_id: rule.cross_domain.payment_gateway_capture_to_order.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.72b273d84c002d67
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.payment_gateway_capture_to_order
  target_card_id: validation_test.cross_domain.payment_gateway_capture_to_order.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.4140ddb4925059ad
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.payment_gateway_capture_to_order
  target_card_id: validation_test.cross_domain.payment_gateway_capture_to_order.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.af30cdd7dc33f4cb
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.payment_gateway_capture_to_order
  target_card_id: output_contract.cross_domain.payment_gateway_capture_to_order
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.73c1b0cb7a1cf40a
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_capture_to_order
  target_card_id: rule.cross_domain.payment_gateway_capture_to_order.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.a8c20a759e5d0fbc
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_capture_to_order
  target_card_id: rule.cross_domain.payment_gateway_capture_to_order.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.fa9d56031a6b053c
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_capture_to_order
  target_card_id: validation_test.cross_domain.payment_gateway_capture_to_order.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.03fbd1e22af84c76
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_capture_to_order
  target_card_id: validation_test.cross_domain.payment_gateway_capture_to_order.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.d055043acfe95c4c
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_capture_to_order
  target_card_id: output_contract.cross_domain.payment_gateway_capture_to_order
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a8b039d361103f34
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_capture_to_order
  target_card_id: query_pattern.cross_domain.payment_gateway_capture_to_order
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.95814b4e21a606d3
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: anchor_set.marketplace.order_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.b6eabf298fdfa5c0
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: anchor_set.operations.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.fe511e7c18154eae
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: anchor_set.payment.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.1fce46b7f46a67c2
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  target_card_id: anchor_set.payment.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.536f67931053a4a7
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.payment_bank
  target_card_id: business_process.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a223a6f7b19e314b
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: domain.cross_domain.payment_bank
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.74298db0b5ed1424
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.cf4afda6f666a7db
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: business_process.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.6066e563dcb9fc51
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: reconciliation_side.cross_domain.payment_gateway_payout_to_bank_credit.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.b1442a537b7a4caa
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: reconciliation_side.cross_domain.payment_gateway_payout_to_bank_credit.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.8a56647da422df6e
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.payment_gateway_payout_to_bank_credit.source
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.1340af42b5517aed
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.payment_gateway_payout_to_bank_credit.target
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.cf8f172bb5de12f2
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: reconciliation_unit.cross_domain.utr_or_payout_batch_or_bank_transaction
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.275b0f423f136dc2
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: matching_logic.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.0c1985b246b17955
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a3627f2774bb318c
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.gateway_payout_missing_bank_credit
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.7249606e50573f81
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.bank_credit_missing_gateway_payout
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.2fc49707eab6da70
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.utr_reference_parse_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.1f7e64ce16909184
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.amount_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.b3cbf0d0b687ca6f
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: mismatch_category.cross_domain.payment_gateway_payout_to_bank_credit.settlement_timing_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.0d07bb6cac0aa504
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.698ea64edaed445d
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: rule.cross_domain.payment_gateway_payout_to_bank_credit.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.1b04ed34ba6c12a0
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: rule.cross_domain.payment_gateway_payout_to_bank_credit.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.70c05e9b9896878e
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: validation_test.cross_domain.payment_gateway_payout_to_bank_credit.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.3e74c62c254e12dc
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: validation_test.cross_domain.payment_gateway_payout_to_bank_credit.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a12093ed1795be0a
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: output_contract.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.8dd6951a58270825
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: rule.cross_domain.payment_gateway_payout_to_bank_credit.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.fe6b3f654b839332
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: rule.cross_domain.payment_gateway_payout_to_bank_credit.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.b2823833fb8dc051
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: validation_test.cross_domain.payment_gateway_payout_to_bank_credit.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.52b84f9763f09495
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: validation_test.cross_domain.payment_gateway_payout_to_bank_credit.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.cc598bdcfe449322
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: output_contract.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.ed826329a7e0c333
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: query_pattern.cross_domain.payment_gateway_payout_to_bank_credit
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a2ad942d0618a73a
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: anchor_set.payment.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.ce323fa20c435532
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: anchor_set.payment.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.8eef90d80ca90b1c
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: anchor_set.bank.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.9fb9e83d057f7e09
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: anchor_set.bank.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.e17c33e357fdcf68
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  target_card_id: anchor_set.bank.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.63cdd7c530e192db
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.marketplace_bank
  target_card_id: business_process.cross_domain.marketplace_settlement_to_bank_credit
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.516815e371da0e95
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: domain.cross_domain.marketplace_bank
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.2c95538e31a6b25b
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.54d36bf48c2f9929
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: business_process.cross_domain.marketplace_settlement_to_bank_credit
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.93b4c929c058dfc7
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: reconciliation_side.cross_domain.marketplace_settlement_to_bank_credit.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.fde43f66aa8ff11e
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: reconciliation_side.cross_domain.marketplace_settlement_to_bank_credit.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.42b9906ddeb070d7
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_settlement_to_bank_credit.source
  target_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.cf753ff3433068e3
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.marketplace_settlement_to_bank_credit.target
  target_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.916df884c3171000
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: reconciliation_unit.cross_domain.settlement_id_or_utr_or_bank_transaction
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.51d69012d049fa33
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: matching_logic.cross_domain.marketplace_settlement_to_bank_credit
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.2d969d03715bb97d
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.06366fd0752936da
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.settlement_missing_bank_credit
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.1c235037513f2956
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.bank_credit_missing_settlement
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.0d4f42cf7f8760f6
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.reference_extraction_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.631650b10eeb700b
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.amount_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.6f4057a87525c25d
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: mismatch_category.cross_domain.marketplace_settlement_to_bank_credit.bank_date_timing_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.7f01bb32eb45b508
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.e924c6cfb2ca8277
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: rule.cross_domain.marketplace_settlement_to_bank_credit.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.d51435c03399d101
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: rule.cross_domain.marketplace_settlement_to_bank_credit.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.5b1ac2b1e33074c6
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: validation_test.cross_domain.marketplace_settlement_to_bank_credit.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.273b3fdc22efef39
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: validation_test.cross_domain.marketplace_settlement_to_bank_credit.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.7b1de5f33f0b3b64
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: output_contract.cross_domain.marketplace_settlement_to_bank_credit
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.c48fe242a73ab956
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: rule.cross_domain.marketplace_settlement_to_bank_credit.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.4e85c47dabc4d318
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: rule.cross_domain.marketplace_settlement_to_bank_credit.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.dd60ee8374cd24e9
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: validation_test.cross_domain.marketplace_settlement_to_bank_credit.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.fc6dcdcba496adcf
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: validation_test.cross_domain.marketplace_settlement_to_bank_credit.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.e4876d0db11f63b4
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: output_contract.cross_domain.marketplace_settlement_to_bank_credit
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.8e1274dff0e3c8ed
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: query_pattern.cross_domain.marketplace_settlement_to_bank_credit
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.1ebdeb19b1761d41
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: anchor_set.marketplace.settlement_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.ab4a799f1688c387
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: anchor_set.marketplace.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.d2260bf7ec40584c
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: anchor_set.bank.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.22dc8c5229109931
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: anchor_set.bank.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.aa8a17189dcb742a
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  target_card_id: anchor_set.bank.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.a3a9c962eee11fea
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.logistics_bank
  target_card_id: business_process.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.b7c1982e7e68521e
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: domain.cross_domain.logistics_bank
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.dda69a650132b3e6
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.b587bbef34e92834
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: business_process.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.bc9560da7d4c2635
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: reconciliation_side.cross_domain.logistics_cod_remittance_to_bank_credit.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.1ac17c85e26f6246
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: reconciliation_side.cross_domain.logistics_cod_remittance_to_bank_credit.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.9bf301358928068a
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.logistics_cod_remittance_to_bank_credit.source
  target_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.14169523ef858fdc
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.logistics_cod_remittance_to_bank_credit.target
  target_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.3fe4250aed516551
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: reconciliation_unit.cross_domain.cod_remittance_or_awb_or_bank_transaction
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.4a736c68ef7aee8d
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: matching_logic.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.6b9e2b3c23ae4c3c
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.0649e9d0862555f3
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.cod_remittance_missing_bank_credit
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.f855cd39cfc858d2
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.bank_credit_missing_cod_remittance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.37999fc81df2d5a4
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.awb_or_utr_mapping_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.2528fbd07983ecdb
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.amount_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.becbb9b3d7b326a5
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: mismatch_category.cross_domain.logistics_cod_remittance_to_bank_credit.remittance_timing_gap
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.701a5ad18afc0528
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.bc0a2d6cecd578a7
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: rule.cross_domain.logistics_cod_remittance_to_bank_credit.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.2483875d979d95a7
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: rule.cross_domain.logistics_cod_remittance_to_bank_credit.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.66631e54863e20b7
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: validation_test.cross_domain.logistics_cod_remittance_to_bank_credit.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.e2834103d20ed438
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: validation_test.cross_domain.logistics_cod_remittance_to_bank_credit.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.4c16453e1c1c156d
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: output_contract.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.6afa03f10e2ecfc1
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: rule.cross_domain.logistics_cod_remittance_to_bank_credit.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.d0a340219708ba54
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: rule.cross_domain.logistics_cod_remittance_to_bank_credit.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.2a8e1fd376f81155
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: validation_test.cross_domain.logistics_cod_remittance_to_bank_credit.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.252b19bf2a5dca00
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: validation_test.cross_domain.logistics_cod_remittance_to_bank_credit.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.e7d5149dbab0945a
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: output_contract.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.46eb3421d62fc2f7
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: query_pattern.cross_domain.logistics_cod_remittance_to_bank_credit
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.1e95c782fb070c73
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: anchor_set.logistics.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.a4840b81b5efd71c
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: anchor_set.logistics.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.65cfe0e08f8b6950
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: anchor_set.bank.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.31081500e7f3f3c2
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: anchor_set.bank.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.227fb77e82d4739d
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  target_card_id: anchor_set.bank.relationships
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.7ccc7195bbbe2279
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.cross_domain.refund_chargeback
  target_card_id: business_process.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.9e5561658efe6155
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: domain.cross_domain.refund_chargeback
  source_type: business_process
  target_type: domain
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.bbf699767d842452
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.7f626af9e2ccb297
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: business_process.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.00b7f6c058879920
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: reconciliation_side.cross_domain.refund_to_payment_gateway_and_marketplace_return.source
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_properties:
    side_role: source_or_expected
```
```yaml
candidate_edge:
  edge_id: edge.ec794b3ba4ccdf5c
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: reconciliation_side.cross_domain.refund_to_payment_gateway_and_marketplace_return.target
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_properties:
    side_role: target_or_actual
```
```yaml
candidate_edge:
  edge_id: edge.925ed4866c3c6856
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.refund_to_payment_gateway_and_marketplace_return.source
  target_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.46e51e3fef5c5d91
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.cross_domain.refund_to_payment_gateway_and_marketplace_return.target
  target_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.39e22e15a5f1e3ae
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: reconciliation_unit.cross_domain.refund_or_order_or_payment_transaction
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_unit
```
```yaml
candidate_edge:
  edge_id: edge.678552c1154be961
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: matching_logic.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.a263098a15b942e9
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.45dd39e193df5d8b
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.return_without_refund
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.a28f1bef3c0955de
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.refund_without_return
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.4f71126a07812352
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.refund_amount_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.38a29e657feb046c
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.original_payment_missing
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.b78eb15c65b24efb
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: mismatch_category.cross_domain.refund_to_payment_gateway_and_marketplace_return.chargeback_status_conflict
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - profile_has_mismatch_category
```
```yaml
candidate_edge:
  edge_id: edge.c75e1fc30dc64742
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - query_targets_card
```
```yaml
candidate_edge:
  edge_id: edge.7151108d3df1d5d7
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: rule.cross_domain.refund_to_payment_gateway_and_marketplace_return.key_normalization
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a5b5b338a67a3732
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: rule.cross_domain.refund_to_payment_gateway_and_marketplace_return.account_scope_deferred
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.259b1c4094326993
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: validation_test.cross_domain.refund_to_payment_gateway_and_marketplace_return.coverage_and_reference_integrity
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.1050f7b0ae7dcfb0
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: query_pattern.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: validation_test.cross_domain.refund_to_payment_gateway_and_marketplace_return.amount_and_status_consistency
  source_type: query_pattern
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.c371a72a792c37f0
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: output_contract.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.c99c16f54f14aa53
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: rule.cross_domain.refund_to_payment_gateway_and_marketplace_return.key_normalization
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.48d7c62eb1a2a464
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: rule.cross_domain.refund_to_payment_gateway_and_marketplace_return.account_scope_deferred
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - rule_enforced_by_constraint
```
```yaml
candidate_edge:
  edge_id: edge.cd31f9772673d674
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: validation_test.cross_domain.refund_to_payment_gateway_and_marketplace_return.coverage_and_reference_integrity
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.7d3cc9ae98500b97
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: validation_test.cross_domain.refund_to_payment_gateway_and_marketplace_return.amount_and_status_consistency
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases:
  - validation_enforces_constraint
```
```yaml
candidate_edge:
  edge_id: edge.4af89dfa9c3e87cf
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: output_contract.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.a324c756cb3dfc72
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: query_pattern.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.cc1c689a91f603b5
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: anchor_set.marketplace.return_tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.507a8cc07495a92d
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: anchor_set.operations.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.c715bdb4eef68353
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: anchor_set.marketplace.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: source
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.7ca3a533f27a2410
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: anchor_set.payment.tables
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
```yaml
candidate_edge:
  edge_id: edge.1ab52bfc13753fb7
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_card_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  target_card_id: anchor_set.payment.reconciliation_profiles
  source_type: reconciliation_profile
  target_type: anchor_set
  inverse_edge_type: TARGETED_BY_REFERENCE_PROFILE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  edge_properties:
    anchor_role: target
  external_card_reference: true
```
## 6. Cross-Domain Flow Templates — Deferred BusinessFlowBinding Layer

These helper templates describe what future `business_flow_binding` instances should use once tenant/group/platform-account/account-data-binding docs exist. They are **not** canonical cards in this reference build.

```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.marketplace_order_to_unicommerce_invoice
  name: Marketplace order to Unicommerce invoice / OSR alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.marketplace_order_to_unicommerce_invoice
  reconciliation_profile_id: reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  source_side: Marketplace order / OMS side
  target_side: Unicommerce invoice / order-sales-report side
  source_anchor_sets:
  - anchor_set.marketplace.order_tables
  - anchor_set.marketplace.relationships
  target_anchor_sets:
  - anchor_set.operations.tables
  - anchor_set.operations.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.marketplace_order_to_increff_wms_dispatch
  name: Marketplace order to Increff WMS dispatch alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.marketplace_order_to_increff_wms_dispatch
  reconciliation_profile_id: reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  source_side: Marketplace order side
  target_side: Increff WMS sales / dispatch side
  source_anchor_sets:
  - anchor_set.marketplace.order_tables
  target_anchor_sets:
  - anchor_set.operations.tables
  - anchor_set.operations.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.unicommerce_invoice_to_increff_wms_sales
  name: Unicommerce invoice to Increff WMS sales alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.unicommerce_invoice_to_increff_wms_sales
  reconciliation_profile_id: reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  source_side: Unicommerce invoice / OMS side
  target_side: Increff WMS sales side
  source_anchor_sets:
  - anchor_set.operations.tables
  - anchor_set.operations.relationships
  target_anchor_sets:
  - anchor_set.operations.tables
  - anchor_set.operations.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.unicommerce_shipment_to_logistics_tracking
  name: Unicommerce shipment evidence to logistics tracking/status alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.unicommerce_shipment_to_logistics_tracking
  reconciliation_profile_id: reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  source_side: Unicommerce OSR shipment side
  target_side: Logistics vendor shipment/status side
  source_anchor_sets:
  - anchor_set.operations.tables
  - anchor_set.operations.relationships
  target_anchor_sets:
  - anchor_set.logistics.tables
  - anchor_set.logistics.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.increff_dispatch_to_logistics_awb
  name: Increff dispatch / AWB evidence to logistics shipment alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.increff_dispatch_to_logistics_awb
  reconciliation_profile_id: reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  source_side: Increff WMS dispatch side
  target_side: Logistics vendor shipment/status side
  source_anchor_sets:
  - anchor_set.operations.tables
  - anchor_set.operations.relationships
  target_anchor_sets:
  - anchor_set.logistics.tables
  - anchor_set.logistics.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.marketplace_shipment_to_logistics_tracking
  name: Marketplace shipment identifiers to logistics tracking/status alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.marketplace_shipment_to_logistics_tracking
  reconciliation_profile_id: reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  source_side: Marketplace shipment / settlement side
  target_side: Logistics shipment/status side
  source_anchor_sets:
  - anchor_set.marketplace.order_tables
  - anchor_set.marketplace.settlement_tables
  - anchor_set.marketplace.return_tables
  target_anchor_sets:
  - anchor_set.logistics.tables
  - anchor_set.logistics.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.marketplace_rto_return_to_logistics_event
  name: Marketplace RTO / return evidence to logistics return event alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.marketplace_rto_return_to_logistics_event
  reconciliation_profile_id: reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  source_side: Marketplace return / reverse side
  target_side: Logistics RTO/return event side
  source_anchor_sets:
  - anchor_set.marketplace.return_tables
  - anchor_set.marketplace.reconciliation_profiles
  target_anchor_sets:
  - anchor_set.logistics.tables
  - anchor_set.logistics.reconciliation_profiles
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  name: Marketplace shipping fee / freight true-up to logistics freight cost alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  reconciliation_profile_id: reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  source_side: Marketplace settlement shipping fee side
  target_side: Logistics freight / invoice / settlement side
  source_anchor_sets:
  - anchor_set.marketplace.settlement_tables
  target_anchor_sets:
  - anchor_set.logistics.tables
  - anchor_set.logistics.reconciliation_profiles
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.payment_gateway_capture_to_order
  name: Payment gateway pay-in capture to order evidence alignment
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.payment_gateway_capture_to_order
  reconciliation_profile_id: reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  source_side: Order / invoice side
  target_side: Payment gateway pay-in side
  source_anchor_sets:
  - anchor_set.marketplace.order_tables
  - anchor_set.operations.tables
  target_anchor_sets:
  - anchor_set.payment.tables
  - anchor_set.payment.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.payment_gateway_payout_to_bank_credit
  name: Payment gateway settlement / payout to bank credit reconciliation
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.payment_gateway_payout_to_bank_credit
  reconciliation_profile_id: reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  source_side: Payment gateway payout / settlement side
  target_side: Bank statement credit side
  source_anchor_sets:
  - anchor_set.payment.tables
  - anchor_set.payment.reconciliation_profiles
  target_anchor_sets:
  - anchor_set.bank.tables
  - anchor_set.bank.reconciliation_profiles
  - anchor_set.bank.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.marketplace_settlement_to_bank_credit
  name: Marketplace settlement / disbursement to bank credit reconciliation
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.marketplace_settlement_to_bank_credit
  reconciliation_profile_id: reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  source_side: Marketplace settlement / disbursement side
  target_side: Bank statement credit side
  source_anchor_sets:
  - anchor_set.marketplace.settlement_tables
  - anchor_set.marketplace.reconciliation_profiles
  target_anchor_sets:
  - anchor_set.bank.tables
  - anchor_set.bank.reconciliation_profiles
  - anchor_set.bank.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.logistics_cod_remittance_to_bank_credit
  name: Logistics COD remittance to bank credit reconciliation
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.logistics_cod_remittance_to_bank_credit
  reconciliation_profile_id: reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  source_side: Logistics COD remittance / settlement side
  target_side: Bank statement credit side
  source_anchor_sets:
  - anchor_set.logistics.tables
  - anchor_set.logistics.reconciliation_profiles
  target_anchor_sets:
  - anchor_set.bank.tables
  - anchor_set.bank.reconciliation_profiles
  - anchor_set.bank.relationships
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
```yaml
cross_domain_flow_template:
  template_id: flow_template.cross_domain.refund_to_payment_gateway_and_marketplace_return
  name: Refund / reverse transaction alignment across marketplace, operations, and payment gateway
  create_business_flow_binding_now: false
  canonical_card_type_when_tenant_account_scope_is_available: business_flow_binding
  business_process_id: business_process.cross_domain.refund_to_payment_gateway_and_marketplace_return
  reconciliation_profile_id: reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  source_side: Marketplace / operations return side
  target_side: Payment gateway refund / chargeback side
  source_anchor_sets:
  - anchor_set.marketplace.return_tables
  - anchor_set.operations.tables
  - anchor_set.marketplace.reconciliation_profiles
  target_anchor_sets:
  - anchor_set.payment.tables
  - anchor_set.payment.reconciliation_profiles
  required_future_inputs:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set optional
  - runtime source/target account roles
  why_deferred: This reference build has domain markdowns but not tenant/account binding files. BusinessFlowBinding instances
    must be created only after exact platform accounts and table filters are known.
```
## 7. Review Items

```yaml
review_item:
  id: review.cross_domain.marketplace_order_to_unicommerce_invoice.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Marketplace order to Unicommerce invoice / OSR alignment is defined as a reusable reference flow. Runtime execution
    requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.marketplace_order_to_unicommerce_invoice
  - reconciliation_profile.cross_domain.marketplace_order_to_unicommerce_invoice
  - execution_constraint_set.cross_domain.marketplace_order_to_unicommerce_invoice
```
```yaml
review_item:
  id: review.cross_domain.marketplace_order_to_increff_wms_dispatch.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Marketplace order to Increff WMS dispatch alignment is defined as a reusable reference flow. Runtime execution
    requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.marketplace_order_to_increff_wms_dispatch
  - reconciliation_profile.cross_domain.marketplace_order_to_increff_wms_dispatch
  - execution_constraint_set.cross_domain.marketplace_order_to_increff_wms_dispatch
```
```yaml
review_item:
  id: review.cross_domain.unicommerce_invoice_to_increff_wms_sales.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Unicommerce invoice to Increff WMS sales alignment is defined as a reusable reference flow. Runtime execution requires
    tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.unicommerce_invoice_to_increff_wms_sales
  - reconciliation_profile.cross_domain.unicommerce_invoice_to_increff_wms_sales
  - execution_constraint_set.cross_domain.unicommerce_invoice_to_increff_wms_sales
```
```yaml
review_item:
  id: review.cross_domain.unicommerce_shipment_to_logistics_tracking.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Unicommerce shipment evidence to logistics tracking/status alignment is defined as a reusable reference flow. Runtime
    execution requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.unicommerce_shipment_to_logistics_tracking
  - reconciliation_profile.cross_domain.unicommerce_shipment_to_logistics_tracking
  - execution_constraint_set.cross_domain.unicommerce_shipment_to_logistics_tracking
```
```yaml
review_item:
  id: review.cross_domain.increff_dispatch_to_logistics_awb.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Increff dispatch / AWB evidence to logistics shipment alignment is defined as a reusable reference flow. Runtime
    execution requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.increff_dispatch_to_logistics_awb
  - reconciliation_profile.cross_domain.increff_dispatch_to_logistics_awb
  - execution_constraint_set.cross_domain.increff_dispatch_to_logistics_awb
```
```yaml
review_item:
  id: review.cross_domain.marketplace_shipment_to_logistics_tracking.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Marketplace shipment identifiers to logistics tracking/status alignment is defined as a reusable reference flow.
    Runtime execution requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.marketplace_shipment_to_logistics_tracking
  - reconciliation_profile.cross_domain.marketplace_shipment_to_logistics_tracking
  - execution_constraint_set.cross_domain.marketplace_shipment_to_logistics_tracking
```
```yaml
review_item:
  id: review.cross_domain.marketplace_rto_return_to_logistics_event.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Marketplace RTO / return evidence to logistics return event alignment is defined as a reusable reference flow.
    Runtime execution requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.marketplace_rto_return_to_logistics_event
  - reconciliation_profile.cross_domain.marketplace_rto_return_to_logistics_event
  - execution_constraint_set.cross_domain.marketplace_rto_return_to_logistics_event
```
```yaml
review_item:
  id: review.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Marketplace shipping fee / freight true-up to logistics freight cost alignment is defined as a reusable reference
    flow. Runtime execution requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  - reconciliation_profile.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
  - execution_constraint_set.cross_domain.marketplace_shipping_fee_to_logistics_freight_cost
```
```yaml
review_item:
  id: review.cross_domain.payment_gateway_capture_to_order.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Payment gateway pay-in capture to order evidence alignment is defined as a reusable reference flow. Runtime execution
    requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.payment_gateway_capture_to_order
  - reconciliation_profile.cross_domain.payment_gateway_capture_to_order
  - execution_constraint_set.cross_domain.payment_gateway_capture_to_order
```
```yaml
review_item:
  id: review.cross_domain.payment_gateway_payout_to_bank_credit.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Payment gateway settlement / payout to bank credit reconciliation is defined as a reusable reference flow. Runtime
    execution requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.payment_gateway_payout_to_bank_credit
  - reconciliation_profile.cross_domain.payment_gateway_payout_to_bank_credit
  - execution_constraint_set.cross_domain.payment_gateway_payout_to_bank_credit
```
```yaml
review_item:
  id: review.cross_domain.marketplace_settlement_to_bank_credit.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Marketplace settlement / disbursement to bank credit reconciliation is defined as a reusable reference flow. Runtime
    execution requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.marketplace_settlement_to_bank_credit
  - reconciliation_profile.cross_domain.marketplace_settlement_to_bank_credit
  - execution_constraint_set.cross_domain.marketplace_settlement_to_bank_credit
```
```yaml
review_item:
  id: review.cross_domain.logistics_cod_remittance_to_bank_credit.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Logistics COD remittance to bank credit reconciliation is defined as a reusable reference flow. Runtime execution
    requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.logistics_cod_remittance_to_bank_credit
  - reconciliation_profile.cross_domain.logistics_cod_remittance_to_bank_credit
  - execution_constraint_set.cross_domain.logistics_cod_remittance_to_bank_credit
```
```yaml
review_item:
  id: review.cross_domain.refund_to_payment_gateway_and_marketplace_return.runtime_scope
  severity: required_for_runtime
  topic: business_flow_binding_deferred
  message: Refund / reverse transaction alignment across marketplace, operations, and payment gateway is defined as a reusable
    reference flow. Runtime execution requires tenant/group/platform_account/account_data_binding/business_flow_binding inputs.
  related_cards:
  - business_process.cross_domain.refund_to_payment_gateway_and_marketplace_return
  - reconciliation_profile.cross_domain.refund_to_payment_gateway_and_marketplace_return
  - execution_constraint_set.cross_domain.refund_to_payment_gateway_and_marketplace_return
```
## 8. Validation Summary

```yaml
validation_summary:
  candidate_cards: 244
  candidate_edges: 419
  canonical_edges: 364
  parser_helper_edges: 55
  edges_with_legacy_aliases: 182
  candidate_cards_by_type:
    domain: 10
    business_process: 13
    reconciliation_profile: 13
    reconciliation_side: 26
    reconciliation_unit: 13
    matching_logic: 13
    mismatch_category: 65
    query_pattern: 13
    rule: 26
    validation_test: 26
    output_contract: 13
    execution_constraint_set: 13
  candidate_edges_by_type:
    HAS_BUSINESS_PROCESS: 13
    BELONGS_TO_DOMAIN: 13
    HAS_RECONCILIATION_PROFILE: 13
    SUPPORTS_PROCESS: 13
    HAS_RECONCILIATION_SIDE: 26
    BELONGS_TO_RECONCILIATION_PROFILE: 26
    HAS_PRIMARY_UNIT: 13
    USES_MATCHING_LOGIC: 13
    SUPPORTS_RECONCILIATION_PROFILE: 13
    HAS_MISMATCH_CATEGORY: 65
    USES_RECONCILIATION_PROFILE: 13
    REQUIRES_RULE: 26
    HAS_VALIDATION_TEST: 26
    USES_OUTPUT_CONTRACT: 26
    INCLUDES_RULE: 26
    INCLUDES_VALIDATION_TEST: 26
    APPLIES_TO_QUERY_PATTERN: 13
    TARGETS_CARD: 55
  missing_internal_edge_references: []
  external_anchor_references_are_allowed: true
  business_flow_binding_instances_created: false
  canonical_edge_taxonomy_registry_used: false
```
## 9. Business Scope Clarification

Business scopes mentioned inside marketplace/logistics/payment/bank markdowns are descriptive applicability scopes. They are not the same as canonical `business_scope_set` cards. A `business_scope_set` card is a tenant/group/account-level reusable account selection object and must be created only from tenant/account-scope inputs. This reference build keeps scope references as metadata and review requirements, not as executable account-selection cards.
