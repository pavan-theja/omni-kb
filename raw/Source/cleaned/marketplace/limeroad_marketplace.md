# LimeRoad Marketplace Clean Markdown — V9 Manifest-Refactored Unified Edges

```yaml
document_metadata:
  document_id: limeroad_marketplace_clean_md_v9_refactored
  vendor: LimeRoad
  source_docx: /mnt/data/LimeRoad Recon KB.docx
  source_markdown: /mnt/data/limeroad_marketplace_clean_md_v8_unified_edges.md
  manifest: /mnt/data/marketplace_cleanup_manifest_consolidated_v2.md
  generated_on: '2026-05-22'
  frame_of_reference: marketplace_cleanup_manifest_consolidated_v2
  marketplace_only: true
  cleanup_focus:
  - remove segment-only process_variant cards
  - replace lazy workflow steps with source-backed LimeRoad lifecycle steps
  - demote query/reconciliation headings out of metric cards
  - encode NSP-based settlement model and COD sale_return_amount semantics
  - add standalone SQL pattern registry and resolve all sql_ref values
  - preserve group_level_id specs as documented scope metadata only
  - keep external account/bank/logistics/statutory scope out of canonical cards
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - logistics_account
  - external_logistics_lifecycle
  - erp_accounting_mapping
  - statutory_tax_filing
  allowed_scope_identifier_fields:
  - documented_scope_values
  - scope_filter_columns
  - benchmark qualifiers
```

## 0. Parser Instructions

This document is intended to be parsed deterministically. It is not a prose-only summary. Create LimeRoad marketplace semantic cards only; do not create tenant, group, account-binding, bank, external logistics, ERP/accounting, or statutory filing cards from scope identifiers, GSTINs, AWBs, bank-transfer language, or tax-recovery language. Documented `group_level_id = 22` is allowed as scope metadata on tables/columns/platform context and as a source-backed query filter.

```yaml
cleanup_issue_register:
- issue_id: cleanup.limeroad.process_variants_lazy
  problem: V8 promoted NSP model, fulfilment, return, RTO, and cancellation labels
    into process_variant cards.
  resolution: Removed all process_variant cards; kept fulfilment/category/payment
    labels as value profiles/rules and represented return/RTO/cancel as lifecycle
    processes.
  status: resolved
- issue_id: cleanup.limeroad.lazy_workflow_steps
  problem: V8 used generic source_event_created / marketplace_state_updated / financial
    evidence workflow steps.
  resolution: Replaced with source-backed steps referencing limeroad_oms, limeroad_settlement,
    entry_type, order_status, vendor_nsp, settled_amount, settlement_date, and COD
    sale_return_amount semantics.
  status: resolved
- issue_id: cleanup.limeroad.heading_metrics
  problem: V8 created metric cards from query/reconciliation headings such as OMS-settlement
    reconciliation and payout summary.
  resolution: Demoted those to query_pattern, reconciliation_profile, validation_test,
    or output_contract cards; kept only actual metrics.
  status: resolved
- issue_id: cleanup.limeroad.nsp_formula
  problem: V8 did not make the NSP payout model central enough and risked generic
    commission-on-charged_amount semantics.
  resolution: Added explicit NSP payout formula, COD sale_return_amount rule, commission
    validation SQL, and source-backed metric guidance.
  status: resolved
- issue_id: cleanup.limeroad.sql_registry
  problem: V8 embedded SQL in query cards and lacked a clean standalone SQL pattern
    registry.
  resolution: Added sql_pattern blocks for every referenced sql_ref and verified dangling_sql_refs
    = 0.
  status: resolved
- issue_id: cleanup.limeroad.scope_boundary
  problem: group_level_id/GSTIN/seller/bank/logistics/tax recovery mentions risked
    out-of-scope account or statutory cards.
  resolution: Preserved them as documented scope values, columns, value profiles,
    rules, caveats, or out_of_scope items only.
  status: resolved
```

## 1. Source Evidence Registry

```yaml
source_evidence:
- id: ev.limeroad.overview.001
  source_document: LimeRoad Recon KB.docx
  source_section: 1. LimeRoad Marketplace Overview
  evidence_type: prose
  summary: LimeRoad/V-Mart marketplace context, Mensa seller brands, group_level_id
    22, and four seller GSTIN warehouse states.
  supported_semantics:
  - platform context
  - brand scope
  - documented group_level_id values
  - GSTIN warehouse value profiles
  unsupported_semantics:
  - tenant/account binding cards
  - statutory filing cards
  confidence: high
- id: ev.limeroad.nsp_model.001
  source_document: LimeRoad Recon KB.docx
  source_section: 2.2 NSP (Net Selling Price) Model
  evidence_type: business_rule
  summary: LimeRoad seller payout is based on vendor_nsp, not charged_amount; seller
    receives vendor_nsp x 58.7% under a 41.3% commission model.
  supported_semantics:
  - NSP payout formula
  - commission base distinction
  - discount absorption semantics
  unsupported_semantics:
  - generic commission-on-buyer-price formulas
  confidence: high
- id: ev.limeroad.fulfillment.001
  source_document: LimeRoad Recon KB.docx
  source_section: 2.3 Fulfilment Model
  evidence_type: prose
  summary: LimeRoad operates dropship/self-fulfilment; sellers dispatch from their
    own warehouses while LimeRoad manages courier empanelment.
  supported_semantics:
  - fulfilment value/context rules
  unsupported_semantics:
  - external logistics lifecycle/account cards
  - process_variant cards from fulfilment label alone
  confidence: high
- id: ev.limeroad.lifecycle.forward.001
  source_document: LimeRoad Recon KB.docx
  source_section: 3.1 Forward Sale Flow
  evidence_type: workflow
  summary: 'Forward sale flow: OMS forward/eventtype sale, seller GST invoice, dispatch,
    delivered settlement entry ITEM_SALE/ORDER_DELIVERED, settled_amount = vendor_nsp
    x 0.587.'
  supported_semantics:
  - forward business process
  - workflow steps
  - state transitions
  - source filters
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.lifecycle.return.001
  source_document: LimeRoad Recon KB.docx
  source_section: 3.2 Return (ITEM_RETURN) Flow
  evidence_type: workflow
  summary: Buyer return after delivery creates settlement ITEM_RETURN reverse row
    with negative settled_amount and reversed commission; OMS reverse return/credit
    note follows.
  supported_semantics:
  - return reversal process
  - negative settlement semantics
  - state transitions
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.lifecycle.rto_cancel.001
  source_document: LimeRoad Recon KB.docx
  source_section: 3.3 RTO Flow; 3.4 Cancellation Flow
  evidence_type: workflow
  summary: RTO uses settlement ITEM_RTO/RETURNED_TO_ORIGIN and OMS reverse credit
    note; cancellation uses ITEM_CANCEL/ORDER_CANCELLED and may pair forward ITEM_SALE
    with reverse ITEM_CANCEL for same order.
  supported_semantics:
  - RTO process
  - cancellation process
  - reverse settlement semantics
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.relationships.001
  source_document: LimeRoad Recon KB.docx
  source_section: 4. Entity Relationships
  evidence_type: table
  summary: OMS and settlement join on invoice_number + item_id and on order_id with
    98.7% coverage; settlement has 124 additional orders due to older/adjustment records.
  supported_semantics:
  - relationship cards
  - matching logic
  - reconciliation variants
  unsupported_semantics:
  - treating pre-OMS settlement rows as hard mismatches
  confidence: high
- id: ev.limeroad.tax.001
  source_document: LimeRoad Recon KB.docx
  source_section: 5. GST / Tax Framework
  evidence_type: rule_list
  summary: Product GST split by state; TCS ~0.5% and TDS ~1% are collected by V MART
    RETAIL LIMITED and visible in OMS fields.
  supported_semantics:
  - tax metrics
  - TCS/TDS query patterns
  - GST value profiles
  unsupported_semantics:
  - statutory filing cards
  confidence: high
- id: ev.limeroad.metrics.sql.001
  source_document: LimeRoad Recon KB.docx
  source_section: 6. Key Business Metrics (with SQL)
  evidence_type: query_example
  summary: Source SQL defines forward GMV, return/RTO/cancel rates, AOV, net settlement
    after returns, monthly OMS, and brand payout efficiency.
  supported_semantics:
  - metric definitions
  - metric implementations
  - SQL refs
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.recon.sql.001
  source_document: LimeRoad Recon KB.docx
  source_section: 7. Reconciliation Use Cases
  evidence_type: reconciliation_playbook
  summary: Source SQL defines OMS-settlement invoice/item matching with >1 price variance,
    MRP-to-NSP-to-settled waterfall, OMS-only TCS visibility, and reverse entry audit.
  supported_semantics:
  - reconciliation profiles
  - matching logic
  - mismatch categories
  - query patterns
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.quality.001
  source_document: LimeRoad Recon KB.docx
  source_section: 8. Data Quality Observations & Known Issues
  evidence_type: caveat
  summary: Quality caveats include tax-rate dual formats, source_state case, invoicedate
    varchar, duplicate field pairs, settlement historical range, COD sale_return_amount,
    missing brand, reverse eventtype NULL, vendor_nsp not in OMS, and NULL entry_type
    rows.
  supported_semantics:
  - rules
  - validation tests
  - reconciliation variants
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.filters.001
  source_document: LimeRoad Recon KB.docx
  source_section: 9. Mandatory Query Filters
  evidence_type: rule_list
  summary: 'Mandatory filters: both tables is_active=true and group_level_id=22; OMS
    revenue transaction_type=''forward''; settlement sales entry_type=''ITEM_SALE''
    and order_status=''ORDER_DELIVERED''; returns entry_type IN (''ITEM_RETURN'',''ITEM_RTO'').'
  supported_semantics:
  - query filters
  - scope identifier metadata
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.table_summary.001
  source_document: LimeRoad Recon KB.docx
  source_section: 10. Table Summary Reference
  evidence_type: table
  summary: limeroad_oms and limeroad_settlement active row counts, date ranges, primary
    keys, join keys, and group_level_id 22.
  supported_semantics:
  - table cards
  - documented scope values
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.settlement.overview.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad Settlement > Overview'
  evidence_type: schema_reference
  summary: limeroad_settlement is the financial settlement ledger and ground truth
    for NSP-based payout, commission deduction, AWB/courier and product classification.
  supported_semantics:
  - settlement table/columns
  - settlement rules
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.settlement.schema.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad Settlement > Schema Details'
  evidence_type: schema_reference
  summary: Settlement schema documents identity, date, financial, charge, classification,
    system, and metadata columns.
  supported_semantics:
  - settlement column cards
  - schema/type fidelity
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.settlement.values.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad Settlement > Distinct Value Analysis'
  evidence_type: table
  summary: entry_type financial breakdown, entry_type meanings, order_status values,
    couriers, classifications, payment modes, and brand comparison.
  supported_semantics:
  - value profiles
  - benchmark/context guidance
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.settlement.nsp_formula.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad Settlement > NSP-Based Settlement Model'
  evidence_type: formula
  summary: Verified settlement formula validates settled_amount = vendor_nsp x 0.587
    and commission = sale_return_amount - settled_amount.
  supported_semantics:
  - formula templates
  - commission validation SQL
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.settlement.queries.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad Settlement > Common Query Patterns'
  evidence_type: query_example
  summary: Settlement queries include payout by settlement date, financial waterfall,
    settlement-to-OMS match, commission validation, return rate/value, and category
    performance.
  supported_semantics:
  - query patterns
  - SQL registry
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.oms.overview.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad OMS > Overview'
  evidence_type: schema_reference
  summary: limeroad_oms is the GST invoice/order management table for forward and
    reverse invoice lines with GST, TCS, TDS, shipping, raw item value, and seller/operator
    identifiers.
  supported_semantics:
  - OMS table/columns
  - OMS source-of-truth semantics
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.oms.schema.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad OMS > Schema Details'
  evidence_type: schema_reference
  summary: OMS schema documents identity, date, financial, tax, TCS/TDS, classification/status,
    geography, and system metadata columns.
  supported_semantics:
  - OMS column cards
  - schema/type fidelity
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.oms.quality.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad OMS > Data Quality Observations'
  evidence_type: caveat
  summary: OMS quality caveats include dual-format tax rates, varchar invoicedate,
    NULL brand rows, NULL salestype, duplicate field pairs, legacy string CGST/SGST,
    source_state lowercase, and reverse rows with NULL eventtype.
  supported_semantics:
  - quality rules
  - validation tests
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.oms.queries.001
  source_document: LimeRoad Recon KB.docx
  source_section: 'Table: LimeRoad OMS > Common Query Patterns'
  evidence_type: query_example
  summary: OMS query patterns include monthly GMV trend, interstate/intrastate GST
    split, brand-level performance, OMS-settlement join, and TCS/TDS summary.
  supported_semantics:
  - query patterns
  - SQL registry
  unsupported_semantics: []
  confidence: high
- id: ev.limeroad.scope.001
  source_document: LimeRoad Recon KB.docx
  source_section: Scope identifiers across tables
  evidence_type: caveat
  summary: group_level_id 22 is documented for LimeRoad/Mensa rows and may be represented
    as a scope column/documented value, but runtime account binding remains external.
  supported_semantics:
  - documented_scope_values on column/table cards
  unsupported_semantics:
  - tenant/group/platform account/account binding cards
  confidence: high
```

## 2. Out-of-Scope Boundary Items

```yaml
out_of_scope_items:
- id: oos.limeroad.group_account.001
  topic: tenant_or_account_binding
  mention: group_level_id 22, seller entity, GSTINs
  instruction: Allowed as documented scope values and columns only; do not create
    tenant/group/platform_account/account_data_binding cards.
  evidence_refs:
  - ev.limeroad.scope.001
  - ev.limeroad.overview.001
- id: oos.limeroad.bank_payout.001
  topic: bank_or_payout_transfer
  mention: Net payout transferred to seller bank account
  instruction: Allowed as marketplace settlement/cash-flow semantics only; do not
    create bank_account or bank reconciliation cards.
  evidence_refs:
  - ev.limeroad.lifecycle.forward.001
- id: oos.limeroad.external_logistics.001
  topic: external_logistics
  mention: AWB, transporter, courier pickup/failed delivery, LimeRoad courier panel
  instruction: Allowed as marketplace fulfilment/courier labels and fee context only;
    do not create external logistics lifecycle/account cards.
  evidence_refs:
  - ev.limeroad.fulfillment.001
  - ev.limeroad.settlement.values.001
- id: oos.limeroad.tax_filing.001
  topic: statutory_tax_filing
  mention: GSTR-2A matching, Form 26AS recovery, GST/IT return references
  instruction: Allowed as marketplace TCS/TDS columns and cash-flow caveats only;
    do not create statutory filing cards.
  evidence_refs:
  - ev.limeroad.tax.001
```

## 3. Candidate Cards

```yaml
candidate_card:
  card_type: platform
  card_id: platform.limeroad
  name: LimeRoad
  fields:
    display_name: LimeRoad
    aliases:
    - Limeroad
    - V-Mart LimeRoad
    - LimeRoad / V-Mart
    marketplace_type: Indian fashion/social commerce marketplace
    legal_operator_from_dataset: V MART RETAIL LIMITED
    operator_gstin_from_dataset: 06AABCV7206K1Z9
    source_boundary: Marketplace semantic cards only; no tenant/account/bank/statutory
      filing cards.
  evidence_refs:
  - ev.limeroad.overview.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.limeroad.in
  name: LimeRoad India marketplace context
  fields:
    platform_id: platform.limeroad
    country: India
    currency: INR
    seller_entity_from_source: Mensa Brand Technologies Pvt Ltd
    documented_scope_values:
      group_level_id:
      - 22
    brands_in_dataset:
    - Anubhutee
    - Ishin
    - High Star
    scope_policy: Documented group_level_id can appear as column/scope metadata; runtime
      account binding is external.
  evidence_refs:
  - ev.limeroad.overview.001
  - ev.limeroad.scope.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.orders
  name: LimeRoad Orders
  fields:
    domain_key: orders
    domain_family: orders
    description: OMS/invoice-level forward and reverse order semantics
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.oms.overview.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.settlement
  name: LimeRoad Settlement
  fields:
    domain_key: settlement
    domain_family: settlement
    description: NSP-based settlement ledger and payout waterfall semantics
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.settlement.overview.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.returns
  name: LimeRoad Returns
  fields:
    domain_key: returns
    domain_family: returns
    description: ITEM_RETURN, ITEM_RTO, and ITEM_CANCEL reversal semantics
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.lifecycle.return.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.reconciliation
  name: LimeRoad Reconciliation
  fields:
    domain_key: reconciliation
    domain_family: reconciliation
    description: Marketplace-internal OMS-settlement, NSP formula, waterfall, and
      reverse-entry reconciliation
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.nsp_pricing
  name: LimeRoad Nsp Pricing
  fields:
    domain_key: nsp_pricing
    domain_family: pricing
    description: Vendor NSP transfer-price model and LimeRoad discount absorption
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.tax
  name: LimeRoad Tax
  fields:
    domain_key: tax
    domain_family: tax
    description: Marketplace GST, TCS, and TDS deduction evidence as table columns/metrics
      only
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.fulfillment
  name: LimeRoad Fulfillment
  fields:
    domain_key: fulfillment
    domain_family: fulfillment
    description: Dropship/self-fulfilment and courier labels as marketplace context
      only
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.fulfillment.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.product
  name: LimeRoad Product
  fields:
    domain_key: product
    domain_family: product
    description: Brand, SKU, HSN, classification, and warehouse product metadata
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.promotions
  name: LimeRoad Promotions
  fields:
    domain_key: promotions
    domain_family: promotions
    description: Vendor discount and LimeRoad additional discount semantics
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.limeroad.payment_mode
  name: LimeRoad Payment Mode
  fields:
    domain_key: payment_mode
    domain_family: payment_mode
    description: COD and prepaid value profiles, including COD charge handling
    platform_context_id: platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.limeroad_oms
  name: zs_observe.limeroad_oms
  fields:
    schema_name: zs_observe
    table_name: limeroad_oms
    table_role: oms_gst_invoice
    purpose: GST invoice / OMS table for forward and reverse item-level invoice rows.
    grain: one invoice line item
    active_rows: 2255
    documented_date_range: 2025-01-01 to 2025-12-06
    primary_key:
    - invoice_number
    - item_id
    join_keys:
    - invoice_number
    - item_id
    - order_id
    mandatory_filters:
    - is_active = true
    - group_level_id = 22 for documented LimeRoad/Mensa scope
    documented_scope_values:
      group_level_id:
      - 22
    scope_policy: Use as documented marketplace scope metadata; do not create group/account
      cards.
  evidence_refs:
  - ev.limeroad.oms.overview.001
  - ev.limeroad.oms.schema.001
  - ev.limeroad.filters.001
  - ev.limeroad.table_summary.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.limeroad_settlement
  name: zs_observe.limeroad_settlement
  fields:
    schema_name: zs_observe
    table_name: limeroad_settlement
    table_role: settlement_ledger
    purpose: Financial settlement ledger for NSP-based payout, commission, returns/RTO/cancel
      reversal, courier, and product classification.
    grain: one settlement/order item row
    active_rows: 2425
    documented_date_range: created_date 2024-05-12 to 2025-12-06; settlement_date
      2025-01-01 to 2025-12-23
    primary_key:
    - invoice_number
    - item_id
    join_keys:
    - invoice_number
    - item_id
    - order_id
    mandatory_filters:
    - is_active = true
    - group_level_id = 22 for documented LimeRoad/Mensa scope
    documented_scope_values:
      group_level_id:
      - 22
    scope_policy: Use as documented marketplace scope metadata; do not create group/account
      cards.
  evidence_refs:
  - ev.limeroad.settlement.overview.001
  - ev.limeroad.settlement.schema.001
  - ev.limeroad.filters.001
  - ev.limeroad.table_summary.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.unique_id
  name: limeroad_settlement.unique_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: unique_id
    data_type: varchar
    column_group: identity
    semantic_role: identity
    business_meaning: Row identifier
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.txn_uuid
  name: limeroad_settlement.txn_uuid
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: txn_uuid
    data_type: varchar
    column_group: identity
    semantic_role: identity
    business_meaning: Pipeline UUID
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.unique_value
  name: limeroad_settlement.unique_value
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: unique_value
    data_type: varchar
    column_group: identity
    semantic_role: identity
    business_meaning: Deduplication hash
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.invoice_number
  name: limeroad_settlement.invoice_number
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: invoice_number
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: GST invoice number; join key to limeroad_oms
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.order_id
  name: limeroad_settlement.order_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: order_id
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: LimeRoad order ID with sub-order suffix; join key
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.item_id
  name: limeroad_settlement.item_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: item_id
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: Line item UUID; join key to limeroad_oms
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.unique_item_id
  name: limeroad_settlement.unique_item_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: unique_item_id
    data_type: varchar
    column_group: identity
    semantic_role: identity
    business_meaning: Alternate item ID
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.sku_id
  name: limeroad_settlement.sku_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: sku_id
    data_type: varchar
    column_group: identity
    semantic_role: product_key
    business_meaning: Seller SKU/style code
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.style_code
  name: limeroad_settlement.style_code
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: style_code
    data_type: varchar
    column_group: identity
    semantic_role: product_key
    business_meaning: Seller style/SKU code alias
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.variant_id
  name: limeroad_settlement.variant_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: variant_id
    data_type: varchar
    column_group: identity
    semantic_role: product_key
    business_meaning: Product variant ID
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.ui_product_id
  name: limeroad_settlement.ui_product_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: ui_product_id
    data_type: varchar
    column_group: identity
    semantic_role: product_key
    business_meaning: UI-facing product ID
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.awb
  name: limeroad_settlement.awb
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: awb
    data_type: varchar
    column_group: identity
    semantic_role: logistics_reference
    business_meaning: AWB/tracking number as marketplace courier context
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.vendor_invoice_number
  name: limeroad_settlement.vendor_invoice_number
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: vendor_invoice_number
    data_type: decimal
    column_group: identity
    semantic_role: invoice_reference
    business_meaning: Vendor invoice reference
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.vendor_margin_approved_id
  name: limeroad_settlement.vendor_margin_approved_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: vendor_margin_approved_id
    data_type: varchar
    column_group: identity
    semantic_role: reference
    business_meaning: Margin approval reference ID
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.created_date
  name: limeroad_settlement.created_date
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: created_date
    data_type: date
    column_group: date
    semantic_role: date
    business_meaning: Record creation date
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.settlement_date
  name: limeroad_settlement.settlement_date
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: settlement_date
    data_type: date
    column_group: date
    semantic_role: date
    business_meaning: Financial settlement/cash-flow date
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.cycle_date
  name: limeroad_settlement.cycle_date
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: cycle_date
    data_type: timestamp
    column_group: date
    semantic_role: date
    business_meaning: Settlement cycle timestamp
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.order_date
  name: limeroad_settlement.order_date
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: order_date
    data_type: timestamp
    column_group: date
    semantic_role: date
    business_meaning: Original order date
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.invoice_date
  name: limeroad_settlement.invoice_date
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: invoice_date
    data_type: timestamp
    column_group: date
    semantic_role: date
    business_meaning: Invoice date
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.mrp
  name: limeroad_settlement.mrp
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: mrp
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Maximum Retail Price
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.charged_amount
  name: limeroad_settlement.charged_amount
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: charged_amount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Price paid by customer; use for GMV
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.sale_return_amount
  name: limeroad_settlement.sale_return_amount
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: sale_return_amount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: charged_amount minus COD charges; use as commission base
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.vendor_nsp
  name: limeroad_settlement.vendor_nsp
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: vendor_nsp
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Vendor Net Selling Price / transfer price; core payout base
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.gross_commission_perc
  name: limeroad_settlement.gross_commission_perc
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: gross_commission_perc
    data_type: decimal
    column_group: financial
    semantic_role: rate
    business_meaning: LimeRoad commission rate; 41.3% in current data
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.gross_commission
  name: limeroad_settlement.gross_commission
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: gross_commission
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: sale_return_amount minus settled_amount
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.settled_amount
  name: limeroad_settlement.settled_amount
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: settled_amount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Net payout to seller = vendor_nsp * (1 - 0.413) on sale rows
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.transfer_price
  name: limeroad_settlement.transfer_price
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: transfer_price
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Alternate transfer price, mostly zero; not the active NSP model
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.lr_margin
  name: limeroad_settlement.lr_margin__
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: lr_margin__
    data_type: decimal
    column_group: financial
    semantic_role: rate
    business_meaning: LimeRoad margin percentage duplicate/context
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.lr_commission_as_per_tp
  name: limeroad_settlement.lr_commission_as_per_tp
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: lr_commission_as_per_tp
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Commission as per transfer price
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.lr_commission_as_per_non_tp
  name: limeroad_settlement.lr_commission_as_per_non_tp
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: lr_commission_as_per_non_tp
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Commission on non-transfer-price basis
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.lr_margin_amount_after_discount_borne_by_limeroad
  name: limeroad_settlement.lr_margin_amount_after_discount_borne_by_limeroad___
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: lr_margin_amount_after_discount_borne_by_limeroad___
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: LR margin after LR-funded discount
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.lr_margin_paid_acquisition
  name: limeroad_settlement.lr_margin_paid_acquisition
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: lr_margin_paid_acquisition
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Acquisition cost margin
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.margin_model
  name: limeroad_settlement.margin_model
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: margin_model
    data_type: decimal
    column_group: financial
    semantic_role: indicator
    business_meaning: Model indicator; 1.000000 indicates NSP model
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.total_vendor_discount
  name: limeroad_settlement.total_vendor_discount
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: total_vendor_discount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Discount from MRP borne by vendor
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.total_limeroad_discount
  name: limeroad_settlement.total_limeroad_discount
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: total_limeroad_discount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Additional discount funded or retained by LimeRoad; sign-sensitive
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.total_adjustment
  name: limeroad_settlement.total_adjustment
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: total_adjustment
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Miscellaneous adjustments
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.gst_adjustment_amount
  name: limeroad_settlement.gst_adjustment_amount
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: gst_adjustment_amount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: GST-related adjustment
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.vendor_nsp_after_less_ctp_income
  name: limeroad_settlement.vendor_nsp_after_less_ctp_income
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: vendor_nsp_after_less_ctp_income
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Adjusted NSP
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.weight_mapping_to_vendor_cost
  name: limeroad_settlement.weight_mapping_to_vendor_cost
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: weight_mapping_to_vendor_cost
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Weight-based cost mapping
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.reversal_of_margin_on_return_cancellation
  name: limeroad_settlement.reversal_of_margin_on_return_cancellation___
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: reversal_of_margin_on_return_cancellation___
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Margin reversal on returns/cancellations
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.shipping_charge_paid_by_customer
  name: limeroad_settlement.shipping_charge_paid_by_customer
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: shipping_charge_paid_by_customer
    data_type: decimal
    column_group: charges
    semantic_role: amount
    business_meaning: Shipping charge billed to buyer
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.cod_charge_paid_by_customer
  name: limeroad_settlement.cod_charge_paid_by_customer
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: cod_charge_paid_by_customer
    data_type: decimal
    column_group: charges
    semantic_role: amount
    business_meaning: COD collection fee paid by buyer
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.handling_charge_paid_by_customer
  name: limeroad_settlement.handling_charge_paid_by_customer
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: handling_charge_paid_by_customer
    data_type: decimal
    column_group: charges
    semantic_role: amount
    business_meaning: Handling charge paid by buyer
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.shipping_amount
  name: limeroad_settlement.shipping_amount
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: shipping_amount
    data_type: decimal
    column_group: charges
    semantic_role: amount
    business_meaning: Shipping amount in settlement
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.transporter_cost_recovered_from_vendor
  name: limeroad_settlement.transporter_cost_recovered_from_vendor
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: transporter_cost_recovered_from_vendor
    data_type: decimal
    column_group: charges
    semantic_role: amount
    business_meaning: Logistics cost charged to seller
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.transporter_cost_recovered_from_vendor_on_return
  name: limeroad_settlement.transporter_cost_recovered_from_vendor_on_return
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: transporter_cost_recovered_from_vendor_on_return
    data_type: decimal
    column_group: charges
    semantic_role: amount
    business_meaning: Return logistics cost charged to seller
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.collection_charges_recovered_from_vendor
  name: limeroad_settlement.collection_charges_recovered_from_vendor
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: collection_charges_recovered_from_vendor
    data_type: decimal
    column_group: charges
    semantic_role: amount
    business_meaning: Payment collection charge recovered from vendor
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.total_payment_amount_made_to_the_vendor
  name: limeroad_settlement.total_payment_amount_made_to_the_vendor___
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: total_payment_amount_made_to_the_vendor___
    data_type: decimal
    column_group: charges
    semantic_role: amount
    business_meaning: Total payment made to vendor
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.transaction_type
  name: limeroad_settlement.transaction_type
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: transaction_type
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: forward or reverse
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.order_status
  name: limeroad_settlement.order_status
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: order_status
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: ORDER_DELIVERED, ORDER_CANCELLED, RETURNED_TO_ORIGIN
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.entry_type
  name: limeroad_settlement.entry_type
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: entry_type
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: ITEM_SALE, ITEM_RETURN, ITEM_RTO, ITEM_CANCEL, ITEM_ADJUSTMENT,
      NULL old rows
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.sub_order_state
  name: limeroad_settlement.sub_order_state
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: sub_order_state
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: Current sub-order state mirroring order_status
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.payment_mode
  name: limeroad_settlement.payment_mode
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: payment_mode
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: COD or PREPAID
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.brand
  name: limeroad_settlement.brand
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: brand
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: Anubhutee or Ishin in settlement
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.classification
  name: limeroad_settlement.classification
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: classification
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: Full product category path
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.destination_state
  name: limeroad_settlement.destination_state
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: destination_state
    data_type: varchar
    column_group: classification
    semantic_role: geo
    business_meaning: Buyer/customer state
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.customer_state
  name: limeroad_settlement.customer_state
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: customer_state
    data_type: varchar
    column_group: classification
    semantic_role: geo
    business_meaning: Buyer/customer state alias
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.transporter
  name: limeroad_settlement.transporter
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: transporter
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: Courier/transporter label
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.lost
  name: limeroad_settlement.lost
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: lost
    data_type: varchar
    column_group: classification
    semantic_role: flag
    business_meaning: Lost shipment flag, mostly NULL
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.lost_in_transit
  name: limeroad_settlement.lost_in_transit
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: lost_in_transit
    data_type: varchar
    column_group: classification
    semantic_role: flag
    business_meaning: Lost-in-transit flag, mostly NULL
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.short_shipment
  name: limeroad_settlement.short_shipment
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: short_shipment
    data_type: varchar
    column_group: classification
    semantic_role: flag
    business_meaning: Short shipment flag
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.group_level_id
  name: limeroad_settlement.group_level_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: group_level_id
    data_type: integer
    column_group: system
    semantic_role: scope
    business_meaning: Documented LimeRoad/Mensa scope identifier value 22
    documented_scope_values:
    - 22
    scope_policy: Documented LimeRoad/Mensa scope value only; runtime binding external.
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.currency_type
  name: limeroad_settlement.currency_type
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: currency_type
    data_type: varchar
    column_group: system
    semantic_role: currency
    business_meaning: INR
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.is_active
  name: limeroad_settlement.is_active
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: is_active
    data_type: boolean
    column_group: system
    semantic_role: quality_flag
    business_meaning: Active row flag; mandatory true filter
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.brand_id
  name: limeroad_settlement.brand_id
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: brand_id
    data_type: varchar
    column_group: system
    semantic_role: reference
    business_meaning: Brand identifier
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.brand_name
  name: limeroad_settlement.brand_name
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: brand_name
    data_type: varchar
    column_group: system
    semantic_role: reference
    business_meaning: Brand name
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.who_changes_vnsp
  name: limeroad_settlement.who_changes_vnsp
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: who_changes_vnsp
    data_type: varchar
    column_group: system
    semantic_role: audit
    business_meaning: NSP change audit user
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.date_of_change_vnsp
  name: limeroad_settlement.date_of_change_vnsp
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: date_of_change_vnsp
    data_type: varchar
    column_group: system
    semantic_role: audit
    business_meaning: NSP change audit date, source varchar
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.remarks_for_adjustment
  name: limeroad_settlement.remarks_for_adjustment
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: remarks_for_adjustment
    data_type: varchar
    column_group: system
    semantic_role: note
    business_meaning: Reason for adjustment entries
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_settlement.zen_sheet_name
  name: limeroad_settlement.zen_sheet_name
  fields:
    table_id: table.zs_observe.limeroad_settlement
    schema_name: zs_observe
    table_name: limeroad_settlement
    column_name: zen_sheet_name
    data_type: varchar
    column_group: system
    semantic_role: lineage
    business_meaning: Source sheet name
  evidence_refs:
  - ev.limeroad.settlement.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.unique_id
  name: limeroad_oms.unique_id
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: unique_id
    data_type: varchar
    column_group: identity
    semantic_role: identity
    business_meaning: System row identifier
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.txn_uuid
  name: limeroad_oms.txn_uuid
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: txn_uuid
    data_type: varchar
    column_group: identity
    semantic_role: identity
    business_meaning: Pipeline UUID
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.unique_value
  name: limeroad_oms.unique_value
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: unique_value
    data_type: varchar
    column_group: identity
    semantic_role: identity
    business_meaning: Deduplication hash
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.invoice_number
  name: limeroad_oms.invoice_number
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: invoice_number
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: GST invoice number, join key to settlement
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.invoiceid
  name: limeroad_oms.invoiceid
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: invoiceid
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: Raw invoice ID alias of invoice_number
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.order_id
  name: limeroad_oms.order_id
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: order_id
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: LimeRoad order ID with sub-order suffix, join key
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.orderid
  name: limeroad_oms.orderid
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: orderid
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: Base order number without sub-order
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.suborderid
  name: limeroad_oms.suborderid
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: suborderid
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: Sub-order number
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.item_id
  name: limeroad_oms.item_id
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: item_id
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: Line item UUID, join key to settlement
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.uniqueitemid
  name: limeroad_oms.uniqueitemid
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: uniqueitemid
    data_type: varchar
    column_group: identity
    semantic_role: join_key
    business_meaning: Duplicate/alias of item_id
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.other_id_2
  name: limeroad_oms.other_id_2
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: other_id_2
    data_type: varchar
    column_group: identity
    semantic_role: reference
    business_meaning: Additional reference
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.sku_id
  name: limeroad_oms.sku_id
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: sku_id
    data_type: varchar
    column_group: identity
    semantic_role: product_key
    business_meaning: Seller SKU/style code
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.vendorstylecode
  name: limeroad_oms.vendorstylecode
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: vendorstylecode
    data_type: varchar
    column_group: identity
    semantic_role: product_key
    business_meaning: Seller SKU/style code alias
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.source_gst_id
  name: limeroad_oms.source_gst_id
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: source_gst_id
    data_type: varchar
    column_group: identity
    semantic_role: tax_identifier
    business_meaning: Seller GSTIN / dispatch warehouse identifier
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.gstin
  name: limeroad_oms.gstin
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: gstin
    data_type: varchar
    column_group: identity
    semantic_role: tax_identifier
    business_meaning: GSTIN alias/source field
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.created_date
  name: limeroad_oms.created_date
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: created_date
    data_type: date
    column_group: date
    semantic_role: date
    business_meaning: Recommended date dimension/order creation date
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.order_date
  name: limeroad_oms.order_date
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: order_date
    data_type: timestamp
    column_group: date
    semantic_role: date
    business_meaning: Order placement timestamp
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.invoice_date
  name: limeroad_oms.invoice_date
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: invoice_date
    data_type: timestamp
    column_group: date
    semantic_role: date
    business_meaning: Invoice timestamp
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.invoicedate
  name: limeroad_oms.invoicedate
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: invoicedate
    data_type: varchar
    column_group: date
    semantic_role: date_string
    business_meaning: Raw invoice date stored as varchar; cast before date filtering
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.order_shipped_date
  name: limeroad_oms.order_shipped_date
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: order_shipped_date
    data_type: date
    column_group: date
    semantic_role: date
    business_meaning: Shipment date
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.shipment_date
  name: limeroad_oms.shipment_date
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: shipment_date
    data_type: timestamp
    column_group: date
    semantic_role: date
    business_meaning: Shipment timestamp
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.mrp
  name: limeroad_oms.mrp
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: mrp
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: MRP where present
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.charged_amount
  name: limeroad_oms.charged_amount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: charged_amount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Item value charged to buyer; OMS GMV basis
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.charged_amount_excluding_tax
  name: limeroad_oms.charged_amount_excluding_tax
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: charged_amount_excluding_tax
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Tax-exclusive charged amount
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.total_tax
  name: limeroad_oms.total_tax
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: total_tax
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Total GST tax on item
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.shipping_amount
  name: limeroad_oms.shipping_amount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: shipping_amount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: Shipping amount/component where present
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.total_tds
  name: limeroad_oms.total_tds
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: total_tds
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: TDS deducted under IT Section 194-O
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tdsamount
  name: limeroad_oms.tdsamount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tdsamount
    data_type: decimal
    column_group: financial
    semantic_role: amount
    business_meaning: TDS amount raw/alias
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tax_igst_rate
  name: limeroad_oms.tax_igst_rate
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tax_igst_rate
    data_type: decimal
    column_group: tax
    semantic_role: rate
    business_meaning: IGST rate; may appear as decimal or percentage in source rows
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tax_igst_amount
  name: limeroad_oms.tax_igst_amount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tax_igst_amount
    data_type: decimal
    column_group: tax
    semantic_role: amount
    business_meaning: IGST amount
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tax_cgst_rate
  name: limeroad_oms.tax_cgst_rate
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tax_cgst_rate
    data_type: decimal
    column_group: tax
    semantic_role: rate
    business_meaning: CGST rate; may appear as decimal or percentage
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tax_cgst_amount
  name: limeroad_oms.tax_cgst_amount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tax_cgst_amount
    data_type: decimal
    column_group: tax
    semantic_role: amount
    business_meaning: CGST amount
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tax_sgst_rate
  name: limeroad_oms.tax_sgst_rate
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tax_sgst_rate
    data_type: decimal
    column_group: tax
    semantic_role: rate
    business_meaning: SGST rate; mirrors CGST
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tax_sgst_amount
  name: limeroad_oms.tax_sgst_amount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tax_sgst_amount
    data_type: decimal
    column_group: tax
    semantic_role: amount
    business_meaning: SGST amount
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.igst
  name: limeroad_oms.igst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: igst
    data_type: decimal
    column_group: tax
    semantic_role: amount
    business_meaning: IGST duplicate/raw field
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.taxamountforigst
  name: limeroad_oms.taxamountforigst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: taxamountforigst
    data_type: decimal
    column_group: tax
    semantic_role: amount
    business_meaning: Raw tax amount for IGST
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.taxamountforcgst
  name: limeroad_oms.taxamountforcgst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: taxamountforcgst
    data_type: decimal
    column_group: tax
    semantic_role: amount
    business_meaning: Raw tax amount for CGST
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.taxamountforsgst
  name: limeroad_oms.taxamountforsgst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: taxamountforsgst
    data_type: decimal
    column_group: tax
    semantic_role: amount
    business_meaning: Raw tax amount for SGST
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.hsn
  name: limeroad_oms.hsn
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: hsn
    data_type: varchar
    column_group: tax
    semantic_role: tax_code
    business_meaning: Primary HSN code
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.hsncode
  name: limeroad_oms.hsncode
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: hsncode
    data_type: varchar
    column_group: tax
    semantic_role: tax_code
    business_meaning: HSN code alias
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.totalgstrate
  name: limeroad_oms.totalgstrate
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: totalgstrate
    data_type: decimal
    column_group: tax
    semantic_role: rate
    business_meaning: Total GST rate percentage
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tcs_igst_amount
  name: limeroad_oms.tcs_igst_amount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tcs_igst_amount
    data_type: decimal
    column_group: tcs_tds
    semantic_role: amount
    business_meaning: TCS IGST component
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tcs_cgst_amount
  name: limeroad_oms.tcs_cgst_amount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tcs_cgst_amount
    data_type: decimal
    column_group: tcs_tds
    semantic_role: amount
    business_meaning: TCS CGST component
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tcs_sgst_amount
  name: limeroad_oms.tcs_sgst_amount
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tcs_sgst_amount
    data_type: decimal
    column_group: tcs_tds
    semantic_role: amount
    business_meaning: TCS SGST component
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tcsamountforigst
  name: limeroad_oms.tcsamountforigst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tcsamountforigst
    data_type: decimal
    column_group: tcs_tds
    semantic_role: amount
    business_meaning: Raw TCS IGST component
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tcsamountforcgst
  name: limeroad_oms.tcsamountforcgst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tcsamountforcgst
    data_type: decimal
    column_group: tcs_tds
    semantic_role: amount
    business_meaning: Raw TCS CGST component
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.tcsamountforsgst
  name: limeroad_oms.tcsamountforsgst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: tcsamountforsgst
    data_type: decimal
    column_group: tcs_tds
    semantic_role: amount
    business_meaning: Raw TCS SGST component
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.transaction_type
  name: limeroad_oms.transaction_type
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: transaction_type
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: forward sale or reverse return
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.eventtype
  name: limeroad_oms.eventtype
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: eventtype
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: sale or return; some reverse rows NULL
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.salestype
  name: limeroad_oms.salestype
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: salestype
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: Interstate or Intrastate; older rows may be NULL
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.brand
  name: limeroad_oms.brand
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: brand
    data_type: varchar
    column_group: classification
    semantic_role: enum
    business_meaning: Anubhutee, Ishin, High Star; some NULL rows
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.description
  name: limeroad_oms.description
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: description
    data_type: varchar
    column_group: classification
    semantic_role: text
    business_meaning: Product description
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.productdescription
  name: limeroad_oms.productdescription
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: productdescription
    data_type: varchar
    column_group: classification
    semantic_role: text
    business_meaning: Product description alias
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.quantity
  name: limeroad_oms.quantity
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: quantity
    data_type: integer
    column_group: classification
    semantic_role: quantity
    business_meaning: Quantity per line
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.temp
  name: limeroad_oms.temp
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: temp
    data_type: varchar
    column_group: classification
    semantic_role: raw
    business_meaning: Temporary field
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.source_state
  name: limeroad_oms.source_state
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: source_state
    data_type: varchar
    column_group: geography
    semantic_role: geo
    business_meaning: Seller dispatch state, lowercase in OMS
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.vendorstate
  name: limeroad_oms.vendorstate
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: vendorstate
    data_type: varchar
    column_group: geography
    semantic_role: geo
    business_meaning: Vendor/source state alias
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.source_zipcode
  name: limeroad_oms.source_zipcode
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: source_zipcode
    data_type: varchar
    column_group: geography
    semantic_role: geo
    business_meaning: Seller pincode
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.vendorpincode
  name: limeroad_oms.vendorpincode
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: vendorpincode
    data_type: varchar
    column_group: geography
    semantic_role: geo
    business_meaning: Vendor pincode alias
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.destination_state
  name: limeroad_oms.destination_state
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: destination_state
    data_type: varchar
    column_group: geography
    semantic_role: geo
    business_meaning: Buyer state
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.customerstate
  name: limeroad_oms.customerstate
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: customerstate
    data_type: varchar
    column_group: geography
    semantic_role: geo
    business_meaning: Buyer state alias
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.destination_zipcode
  name: limeroad_oms.destination_zipcode
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: destination_zipcode
    data_type: decimal
    column_group: geography
    semantic_role: geo
    business_meaning: Buyer pincode
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.customerpincode
  name: limeroad_oms.customerpincode
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: customerpincode
    data_type: decimal
    column_group: geography
    semantic_role: geo
    business_meaning: Customer pincode alias
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.source_state_code
  name: limeroad_oms.source_state_code
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: source_state_code
    data_type: varchar
    column_group: geography
    semantic_role: geo
    business_meaning: Source state code
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.destination_state_code
  name: limeroad_oms.destination_state_code
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: destination_state_code
    data_type: varchar
    column_group: geography
    semantic_role: geo
    business_meaning: Destination state code
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.group_level_id
  name: limeroad_oms.group_level_id
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: group_level_id
    data_type: integer
    column_group: system
    semantic_role: scope
    business_meaning: Documented LimeRoad/Mensa scope identifier value 22
    documented_scope_values:
    - 22
    scope_policy: Documented LimeRoad/Mensa scope value only; runtime binding external.
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.currency_type
  name: limeroad_oms.currency_type
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: currency_type
    data_type: varchar
    column_group: system
    semantic_role: currency
    business_meaning: INR
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.is_active
  name: limeroad_oms.is_active
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: is_active
    data_type: boolean
    column_group: system
    semantic_role: quality_flag
    business_meaning: Active row flag; mandatory true filter
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.ancestry
  name: limeroad_oms.ancestry
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: ancestry
    data_type: varchar
    column_group: system
    semantic_role: lineage
    business_meaning: Lineage
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.sgst
  name: limeroad_oms.sgst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: sgst
    data_type: varchar
    column_group: system
    semantic_role: legacy
    business_meaning: Legacy SGST string field; use typed tax_sgst_amount instead
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.cgst
  name: limeroad_oms.cgst
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: cgst
    data_type: varchar
    column_group: system
    semantic_role: legacy
    business_meaning: Legacy CGST string field; use typed tax_cgst_amount instead
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.none
  name: limeroad_oms.none
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: none
    data_type: varchar
    column_group: system
    semantic_role: legacy
    business_meaning: Legacy string field
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.failure_reason_order_id
  name: limeroad_oms.failure_reason_order_id
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: failure_reason_order_id
    data_type: varchar
    column_group: system
    semantic_role: reference
    business_meaning: Order ID from failure reason tracking
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.limeroad_oms.zen_sheet_name
  name: limeroad_oms.zen_sheet_name
  fields:
    table_id: table.zs_observe.limeroad_oms
    schema_name: zs_observe
    table_name: limeroad_oms
    column_name: zen_sheet_name
    data_type: varchar
    column_group: system
    semantic_role: lineage
    business_meaning: Source sheet
  evidence_refs:
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.limeroad.oms_settlement.invoice_item
  name: LimeRoad OMS to settlement invoice-item match
  fields:
    left_table: table.zs_observe.limeroad_oms
    right_table: table.zs_observe.limeroad_settlement
    join_keys:
    - left: invoice_number
      right: invoice_number
    - left: item_id
      right: item_id
    documented_coverage: 1,520 / 1,540 = 98.7%
    relationship_grain: invoice item line
    use_for:
    - OMS settlement reconciliation
    - vendor_nsp lookup from settlement
    - brand recovery when OMS brand is NULL
  evidence_refs:
  - ev.limeroad.relationships.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.limeroad.oms_settlement.order_id
  name: LimeRoad OMS to settlement order-id match
  fields:
    left_table: table.zs_observe.limeroad_oms
    right_table: table.zs_observe.limeroad_settlement
    join_keys:
    - left: order_id
      right: order_id
    documented_coverage: 1,520 / 1,540 = 98.7%
    relationship_grain: order/sub-order
    use_for:
    - coverage check
    - fallback matching
  evidence_refs:
  - ev.limeroad.relationships.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.settlement.entry_type
  name: LimeRoad settlement entry_type values
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_settlement
    column_id: column.zs_observe.limeroad_settlement.entry_type
    column_name: entry_type
    documented_values:
      ITEM_SALE: Forward order successfully delivered or in settlement cycle
      ITEM_RETURN: Buyer-initiated return after delivery
      ITEM_RTO: Return-to-Origin courier failed delivery
      ITEM_CANCEL: Order cancelled before/after shipment
      ITEM_ADJUSTMENT: Manual settlement adjustment
      'NULL': Older records; include in totals
    distribution_summary: Settlement entry_type drives sales, returns, RTO, cancels,
      adjustments, and NULL-old-row handling.
  evidence_refs:
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.settlement.order_status
  name: LimeRoad settlement order_status values
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_settlement
    column_id: column.zs_observe.limeroad_settlement.order_status
    column_name: order_status
    documented_values:
      ORDER_DELIVERED: Delivered to buyer
      RETURNED_TO_ORIGIN: Courier returned item to seller
      ORDER_CANCELLED: Order cancelled
    distribution_summary: Status context for delivered sales, RTO, and cancellations.
  evidence_refs:
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.settlement.transaction_type
  name: LimeRoad settlement transaction_type values
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_settlement
    column_id: column.zs_observe.limeroad_settlement.transaction_type
    column_name: transaction_type
    documented_values:
      forward: Forward sale/settlement credit
      reverse: Return/RTO/cancel reversal context
    distribution_summary: Use with entry_type; entry_type is the safer financial classification.
  evidence_refs:
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.settlement.payment_mode
  name: LimeRoad payment modes
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_settlement
    column_id: column.zs_observe.limeroad_settlement.payment_mode
    column_name: payment_mode
    documented_values:
      COD: Cash on Delivery
      PREPAID: Prepaid UPI/card/netbanking
    distribution_summary: COD affects sale_return_amount because COD charge is deducted
      from charged_amount.
  evidence_refs:
  - ev.limeroad.settlement.values.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.settlement.brand
  name: LimeRoad settlement brands
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_settlement
    column_id: column.zs_observe.limeroad_settlement.brand
    column_name: brand
    documented_values:
      Anubhutee: Ethnic wear, kurta sets/kurtis/nightwear
      Ishin: Premium ethnic sets/dresses/sarees
    distribution_summary: Settlement brand comparison shows 41.3% commission for Anubhutee
      and Ishin ITEM_SALE rows.
  evidence_refs:
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.oms.brand
  name: LimeRoad OMS brands
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_oms
    column_id: column.zs_observe.limeroad_oms.brand
    column_name: brand
    documented_values:
      Anubhutee: Ethnic sets/kurtas/kurtis/nightwear
      Ishin: Premium ethnic sets/dresses/sarees
      High Star: Accessories; limited rows
      'NULL': About 25 OMS rows missing brand
    distribution_summary: OMS brand profile includes High Star and NULL brand caveat.
  evidence_refs:
  - ev.limeroad.oms.quality.001
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.settlement.transporter
  name: LimeRoad courier/transporter labels
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_settlement
    column_id: column.zs_observe.limeroad_settlement.transporter
    column_name: transporter
    documented_values:
    - shadowfax
    - delhivery_surface
    - bluedart
    - bluedart_surface
    - ecomexpress
    - ekart_surface
    - xpressbees
    - xpressbees_surface
    - shiprocket_Delhivery_MSP
    - shiprocket_Xpressbees_MSP
    distribution_summary: Courier labels are marketplace fulfilment context only,
      not external logistics cards.
  evidence_refs:
  - ev.limeroad.settlement.values.001
  - ev.limeroad.fulfillment.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.settlement.classification
  name: LimeRoad classification category paths
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_settlement
    column_id: column.zs_observe.limeroad_settlement.classification
    column_name: classification
    documented_values:
    - clothing/ethnic wear/Sets
    - clothing/ethnic wear/Kurta Kurtis/kurtas
    - clothing/ethnic wear/Kurta Kurtis/kurtis
    - clothing/ethnic wear/Ethnic Dresses
    - clothing/western wear/Dresses
    - clothing/western wear/Tunics
    - clothing/ethnic wear/Sarees
    - clothing/lingerie/sleepwear/nightwear sets
    - accessories/fashion jewellery/earrings
    distribution_summary: Classification paths support category-level performance,
      not process variants.
  evidence_refs:
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.oms.transaction_type
  name: LimeRoad OMS transaction_type values
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_oms
    column_id: column.zs_observe.limeroad_oms.transaction_type
    column_name: transaction_type
    documented_values:
      forward: Sale invoice line
      reverse: Return/credit-note invoice line
    distribution_summary: Revenue queries must isolate forward; reverse rows include
      older NULL eventtype cases.
  evidence_refs:
  - ev.limeroad.oms.schema.001
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.oms.eventtype
  name: LimeRoad OMS eventtype values
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_oms
    column_id: column.zs_observe.limeroad_oms.eventtype
    column_name: eventtype
    documented_values:
      sale: Forward sale
      return: Return/reverse row
      'NULL': 26 older reverse rows; transaction_type reverse captures them
    distribution_summary: Do not rely on eventtype alone for reverse filtering.
  evidence_refs:
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.oms.salestype
  name: LimeRoad OMS salestype values
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_oms
    column_id: column.zs_observe.limeroad_oms.salestype
    column_name: salestype
    documented_values:
      Interstate: Source and destination differ; IGST
      Intrastate: Same state; CGST+SGST
      'NULL': Few older rows; infer from states if needed
    distribution_summary: GST split by salestype/source-destination state.
  evidence_refs:
  - ev.limeroad.tax.001
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.oms.source_gst_warehouses
  name: LimeRoad seller GSTIN warehouse mapping
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_oms
    column_id: column.zs_observe.limeroad_oms.source_gst_id
    column_name: source_gst_id
    documented_values:
      29AAOCM5326J1ZY: Karnataka
      27AAOCM5326J1Z2: Maharashtra
      19AAOCM5326J1ZZ: West Bengal
      06AAOCM5326J1Z6: Haryana
    distribution_summary: Four Mensa dispatch GSTIN/warehouse states documented in
      source.
  evidence_refs:
  - ev.limeroad.overview.001
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.oms.hsn_rates
  name: LimeRoad HSN/GST rate profile
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_oms
    column_id: column.zs_observe.limeroad_oms.hsn
    column_name: hsn
    documented_values:
      62063000/62064000: 5% clothing items
      62114290/62114990: 5% or 12% garments
      '62044390': 12% dresses
      '71179010': 3% fashion jewellery
      '998599': 18% marketplace services
    distribution_summary: HSN codes support GST-rate validation.
  evidence_refs:
  - ev.limeroad.tax.001
  - ev.limeroad.oms.schema.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.settlement.discount_sign
  name: LimeRoad discount sign convention
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_settlement
    column_id: column.zs_observe.limeroad_settlement.total_limeroad_discount
    column_name: total_limeroad_discount
    documented_values:
      negative: LimeRoad absorbed extra discount below vendor_nsp
      positive: LimeRoad priced above vendor_nsp / retained surplus
    distribution_summary: Apply ABS carefully; sign carries business meaning.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.limeroad.scope.group_level_id
  name: LimeRoad documented group_level_id
  fields:
    profile_kind: documented_value_profile
    table_id: table.zs_observe.limeroad_oms
    column_id: column.zs_observe.limeroad_oms.group_level_id
    column_name: group_level_id
    documented_values:
      '22': Documented LimeRoad/Mensa account scope in both OMS and settlement
    distribution_summary: Scope identifier is a column/value only; no group/account
      card.
  evidence_refs:
  - ev.limeroad.scope.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.gross_gmv
  name: Gross GMV
  fields:
    metric_key: gross_gmv
    business_definition: Total customer charged amount for forward sales.
    colloquial_names:
    - GMV
    - gross sales
    - total sales
    metric_pattern: sum_charged_amount_forward_sales
    default_grain: settlement_period_or_date
    domain: domain.marketplace.limeroad.orders; domain.marketplace.limeroad.settlement
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      limeroad_settlement_context: ₹16,01,936 on ITEM_SALE rows
      source: docx settlement key statistics / metric SQL
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Total customer charged amount for forward sales.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.vendor_nsp_total
  name: Total Vendor NSP
  fields:
    metric_key: vendor_nsp_total
    business_definition: Total vendor net selling price / transfer-price base for
      settled sale rows.
    colloquial_names:
    - NSP
    - vendor transfer price
    - total NSP
    metric_pattern: sum_vendor_nsp_item_sale
    default_grain: settlement_period_or_date
    domain: domain.marketplace.limeroad.nsp_pricing
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Total vendor net selling price / transfer-price base for settled
    sale rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.net_settled_revenue
  name: Net settled revenue after returns
  fields:
    metric_key: net_settled_revenue
    business_definition: Net seller settlement after sale credits and return/RTO/cancel
      deductions.
    colloquial_names:
    - net settlement
    - net payout
    - seller payout
    metric_pattern: sum_settled_amount_all_entry_types
    default_grain: settlement_date
    domain: domain.marketplace.limeroad.settlement; domain.marketplace.limeroad.returns
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      forward_settled_context: ₹9,35,252 net forward settlement
      returns_settled_context: −₹3,52,250 return/RTO/cancel settlement
      source: docx settlement key statistics
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Net seller settlement after sale credits and return/RTO/cancel
    deductions.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.seller_realization_rate
  name: Seller realization rate
  fields:
    metric_key: seller_realization_rate
    business_definition: Seller payout as a percentage of customer charged GMV or
      NSP, depending on query context.
    colloquial_names:
    - realization rate
    - payout ratio
    - payout percentage
    metric_pattern: settled_amount_over_charged_amount_or_nsp
    default_grain: settlement_period_or_brand
    domain: domain.marketplace.limeroad.settlement; domain.marketplace.limeroad.nsp_pricing
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      nsp_model_payout_rate: 58.7 percent of vendor_nsp under 41.3 percent commission
      guidance: Use vendor_nsp denominator for NSP-model validation; use charged_amount
        denominator for buyer-price realization context.
      source: docx NSP model and waterfall SQL
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Seller payout as a percentage of customer charged GMV or NSP, depending
    on query context.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.effective_commission_rate
  name: Effective commission rate
  fields:
    metric_key: effective_commission_rate
    business_definition: LimeRoad commission as a percentage of vendor NSP for settled
      sale rows.
    colloquial_names:
    - commission rate
    - LR commission
    - take rate
    metric_pattern: gross_commission_over_vendor_nsp
    default_grain: settlement_period_or_brand
    domain: domain.marketplace.limeroad.nsp_pricing; domain.marketplace.limeroad.settlement
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      current_dataset: 41.3 percent flat on vendor_nsp for Anubhutee and Ishin rows
      interpretation: Guidance for current dataset only; validate if new categories/brands
        appear.
      source: docx section 1.3 and settlement value analysis
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: LimeRoad commission as a percentage of vendor NSP for settled sale
    rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.return_rate
  name: Return rate
  fields:
    metric_key: return_rate
    business_definition: Buyer return rows as a percentage of sale rows.
    colloquial_names:
    - return rate
    - buyer return rate
    metric_pattern: count_item_return_over_count_item_sale
    default_grain: brand_or_period
    domain: domain.marketplace.limeroad.returns
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      observed_context: 18.7 percent return rate in source metric SQL comment
      source: docx section 6.2
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Buyer return rows as a percentage of sale rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.rto_rate
  name: RTO rate
  fields:
    metric_key: rto_rate
    business_definition: Return-to-origin rows as a percentage of sale rows.
    colloquial_names:
    - RTO rate
    - return to origin rate
    metric_pattern: count_item_rto_over_count_item_sale
    default_grain: brand_or_period
    domain: domain.marketplace.limeroad.returns; domain.marketplace.limeroad.fulfillment
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      observed_context: 18.1 percent RTO rate in source metric SQL comment
      source: docx section 6.2
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Return-to-origin rows as a percentage of sale rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.cancellation_rate
  name: Cancellation rate
  fields:
    metric_key: cancellation_rate
    business_definition: Cancelled rows as a percentage of sale rows.
    colloquial_names:
    - cancel rate
    - cancellation percentage
    metric_pattern: count_item_cancel_over_count_item_sale
    default_grain: brand_or_period
    domain: domain.marketplace.limeroad.returns
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      observed_context: 9.2 percent cancel rate in source metric SQL comment
      source: docx section 6.2
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Cancelled rows as a percentage of sale rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.average_order_value
  name: Average order value
  fields:
    metric_key: average_order_value
    business_definition: Average charged_amount for settlement ITEM_SALE rows.
    colloquial_names:
    - AOV
    - average selling price
    - average basket value
    metric_pattern: avg_charged_amount_item_sale
    default_grain: settlement_period_or_brand
    domain: domain.marketplace.limeroad.orders; domain.marketplace.limeroad.settlement
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      observed_context: ₹970.87 from source metric SQL comment
      source: docx section 6.3
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Average charged_amount for settlement ITEM_SALE rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.brand_payout_efficiency
  name: Brand payout efficiency
  fields:
    metric_key: brand_payout_efficiency
    business_definition: Brand-level comparison of average MRP, charged amount, NSP,
      payout, and payout percentage.
    colloquial_names:
    - brand efficiency
    - brand payout percentage
    metric_pattern: avg_settled_over_avg_charged_by_brand
    default_grain: brand
    domain: domain.marketplace.limeroad.product; domain.marketplace.limeroad.settlement
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Brand-level comparison of average MRP, charged amount, NSP, payout,
    and payout percentage.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.tcs_deducted
  name: TCS deducted
  fields:
    metric_key: tcs_deducted
    business_definition: Tax collected at source from OMS TCS component fields.
    colloquial_names:
    - TCS
    - tax collected at source
    metric_pattern: sum_tcs_components_forward_oms
    default_grain: month
    domain: domain.marketplace.limeroad.tax
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      observed_total_2025: ₹12,869.96
      rate_context: approximately 0.5 percent of charged_amount_excluding_tax
      source: docx GST/TCS section and OMS statistics
  evidence_refs:
  - ev.limeroad.tax.001
  - ev.limeroad.oms.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Tax collected at source from OMS TCS component fields.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.tds_deducted
  name: TDS deducted
  fields:
    metric_key: tds_deducted
    business_definition: Tax deducted at source from OMS total_tds/tdsamount.
    colloquial_names:
    - TDS
    - tax deducted at source
    metric_pattern: sum_total_tds_forward_oms
    default_grain: month
    domain: domain.marketplace.limeroad.tax
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
    benchmarks:
      observed_total_2025: ₹20,648.13
      rate_context: approximately 1.0 percent of charged_amount_excluding_tax
      source: docx GST/TDS section and OMS statistics
  evidence_refs:
  - ev.limeroad.tax.001
  - ev.limeroad.oms.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Tax deducted at source from OMS total_tds/tdsamount.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.limeroad_discount_absorption
  name: LimeRoad discount absorption
  fields:
    metric_key: limeroad_discount_absorption
    business_definition: Sign-sensitive LimeRoad-funded discount/surplus relative
      to vendor NSP and buyer price.
    colloquial_names:
    - LR discount
    - discount absorption
    metric_pattern: sum_total_limeroad_discount_item_sale
    default_grain: settlement_period_or_brand
    domain: domain.marketplace.limeroad.promotions; domain.marketplace.limeroad.nsp_pricing
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Sign-sensitive LimeRoad-funded discount/surplus relative to vendor
    NSP and buyer price.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.return_reversal_amount
  name: Return reversal amount
  fields:
    metric_key: return_reversal_amount
    business_definition: Negative settlement amount for ITEM_RETURN, ITEM_RTO, and
      ITEM_CANCEL rows.
    colloquial_names:
    - reverse deductions
    - return deduction
    - RTO loss
    metric_pattern: sum_settled_amount_reverse_entries
    default_grain: settlement_date_or_brand
    domain: domain.marketplace.limeroad.returns; domain.marketplace.limeroad.settlement
    scope: generic marketplace metric implemented by LimeRoad-specific metric_implementation
      cards
  evidence_refs:
  - ev.limeroad.lifecycle.return.001
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
  candidate_notes: Negative settlement amount for ITEM_RETURN, ITEM_RTO, and ITEM_CANCEL
    rows.
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.limeroad.nsp_payout
  name: LimeRoad NSP payout formula
  fields:
    formula_key: limeroad_nsp_payout
    formula_expression: settled_amount = ROUND(vendor_nsp * (1 - gross_commission_perc
      / 100), 2); current data uses gross_commission_perc = 41.3 so payout = vendor_nsp
      * 0.587
    platform_context: platform_context.limeroad.in
    notes: Executable SQL references are provided in sql_pattern blocks.
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.settlement.nsp_formula.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.limeroad.gross_commission
  name: LimeRoad gross commission formula
  fields:
    formula_key: limeroad_gross_commission
    formula_expression: gross_commission = sale_return_amount - settled_amount; sale_return_amount,
      not charged_amount, is the COD-adjusted commission base
    platform_context: platform_context.limeroad.in
    notes: Executable SQL references are provided in sql_pattern blocks.
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.limeroad.return_rate
  name: LimeRoad return/RTO/cancel rate formula
  fields:
    formula_key: limeroad_return_rates
    formula_expression: COUNT_IF(entry_type = target_reverse_type) / NULLIF(COUNT_IF(entry_type
      = 'ITEM_SALE'), 0)
    platform_context: platform_context.limeroad.in
    notes: Executable SQL references are provided in sql_pattern blocks.
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.limeroad.net_settlement
  name: LimeRoad net settlement formula
  fields:
    formula_key: limeroad_net_settlement
    formula_expression: SUM(CASE WHEN entry_type='ITEM_SALE' THEN settled_amount ELSE
      0 END) + SUM(CASE WHEN entry_type IN ('ITEM_RETURN','ITEM_RTO','ITEM_CANCEL')
      THEN settled_amount ELSE 0 END)
    platform_context: platform_context.limeroad.in
    notes: Executable SQL references are provided in sql_pattern blocks.
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.limeroad.tax_component_summary
  name: LimeRoad TCS/TDS summary formula
  fields:
    formula_key: limeroad_tcs_tds
    formula_expression: TCS = SUM(tcs_igst_amount + tcs_cgst_amount + tcs_sgst_amount);
      TDS = SUM(total_tds)
    platform_context: platform_context.limeroad.in
    notes: Executable SQL references are provided in sql_pattern blocks.
  evidence_refs:
  - ev.limeroad.tax.001
  - ev.limeroad.oms.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.limeroad.tax_rate_normalization
  name: LimeRoad dual-format tax-rate normalization formula
  fields:
    formula_key: limeroad_tax_rate_normalization
    formula_expression: normalized_rate = CASE WHEN rate > 1 THEN rate / 100 ELSE
      rate END
    platform_context: platform_context.limeroad.in
    notes: Executable SQL references are provided in sql_pattern blocks.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.gross_gmv
  name: LimeRoad gross GMV implementation
  fields:
    metric_id: metric.marketplace.gross_gmv
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.forward_gmv
    implementation_logic: SUM(charged_amount) on limeroad_settlement where entry_type=ITEM_SALE
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.vendor_nsp_total
  name: LimeRoad total NSP implementation
  fields:
    metric_id: metric.marketplace.vendor_nsp_total
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.forward_gmv
    implementation_logic: SUM(vendor_nsp) on ITEM_SALE rows
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.net_settled_revenue
  name: LimeRoad net settlement implementation
  fields:
    metric_id: metric.marketplace.net_settled_revenue
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.net_after_returns
    implementation_logic: SUM(settled_amount) across sales and reverse entries
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.seller_realization_rate
  name: LimeRoad seller realization implementation
  fields:
    metric_id: metric.marketplace.seller_realization_rate
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.recon.nsp_waterfall
    implementation_logic: payout_pct_of_nsp plus charged_amount context by brand
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.effective_commission_rate
  name: LimeRoad effective commission implementation
  fields:
    metric_id: metric.marketplace.effective_commission_rate
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.forward_gmv
    implementation_logic: gross_commission / vendor_nsp on ITEM_SALE rows
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.return_rate
  name: LimeRoad return rate implementation
  fields:
    metric_id: metric.marketplace.return_rate
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.return_rate
    implementation_logic: ITEM_RETURN count over ITEM_SALE count
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.rto_rate
  name: LimeRoad RTO rate implementation
  fields:
    metric_id: metric.marketplace.rto_rate
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.return_rate
    implementation_logic: ITEM_RTO count over ITEM_SALE count
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.cancellation_rate
  name: LimeRoad cancellation rate implementation
  fields:
    metric_id: metric.marketplace.cancellation_rate
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.return_rate
    implementation_logic: ITEM_CANCEL count over ITEM_SALE count
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.average_order_value
  name: LimeRoad AOV implementation
  fields:
    metric_id: metric.marketplace.average_order_value
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.aov
    implementation_logic: AVG(charged_amount) on ITEM_SALE rows
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.brand_payout_efficiency
  name: LimeRoad brand payout efficiency implementation
  fields:
    metric_id: metric.marketplace.brand_payout_efficiency
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.settlement.brand_payout_efficiency
    implementation_logic: Average payout / charged amount by brand
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.tcs_deducted
  name: LimeRoad TCS implementation
  fields:
    metric_id: metric.marketplace.tcs_deducted
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_oms
    formula_sql_ref: sql.limeroad.oms.tcs_tds_summary
    implementation_logic: SUM OMS TCS component fields by month
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.tds_deducted
  name: LimeRoad TDS implementation
  fields:
    metric_id: metric.marketplace.tds_deducted
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_oms
    formula_sql_ref: sql.limeroad.oms.tcs_tds_summary
    implementation_logic: SUM(total_tds) by month
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.discount_absorption
  name: LimeRoad discount absorption implementation
  fields:
    metric_id: metric.marketplace.limeroad_discount_absorption
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.recon.nsp_waterfall
    implementation_logic: SUM(total_limeroad_discount) by brand
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.limeroad.return_reversal_amount
  name: LimeRoad return reversal implementation
  fields:
    metric_id: metric.marketplace.return_reversal_amount
    platform_context: platform_context.limeroad.in
    source_tables:
    - table.zs_observe.limeroad_settlement
    formula_sql_ref: sql.limeroad.recon.reverse_entries_audit
    implementation_logic: Negative settled_amount for ITEM_RETURN/RTO/CANCEL rows
    required_filters:
    - is_active = true
    - group_level_id = 22 documented LimeRoad scope
    scope_policy: documented scope value is permitted; runtime account/scope binding
      remains external
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.limeroad.realization_uses_gmv_and_payout
  name: Realization Uses Gmv And Payout
  fields:
    source_metric: metric.marketplace.seller_realization_rate
    target_metric: metric.marketplace.gross_gmv
    dependency_description: Realization denominator uses charged_amount or NSP context;
      numerator uses settled_amount.
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.limeroad.realization_uses_net_settlement
  name: Realization Uses Net Settlement
  fields:
    source_metric: metric.marketplace.seller_realization_rate
    target_metric: metric.marketplace.net_settled_revenue
    dependency_description: Realization numerator is seller payout / settled_amount.
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.limeroad.return_reversal_uses_return_rate
  name: Return Reversal Uses Return Rate
  fields:
    source_metric: metric.marketplace.return_reversal_amount
    target_metric: metric.marketplace.return_rate
    dependency_description: Return reversal interpretation depends on reverse-entry
      volume.
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.limeroad.commission_rate_uses_nsp
  name: Commission Rate Uses Nsp
  fields:
    source_metric: metric.marketplace.effective_commission_rate
    target_metric: metric.marketplace.vendor_nsp_total
    dependency_description: Commission rate is against vendor_nsp, not charged_amount.
  evidence_refs:
  - ev.limeroad.nsp_model.001
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.limeroad.forward_nsp_settlement
  name: LimeRoad forward NSP settlement
  fields:
    process_family: orders
    business_trigger: Forward order in limeroad_oms becomes delivered settlement ITEM_SALE
      with NSP-based seller payout.
    participating_tables:
    - table.zs_observe.limeroad_oms
    - table.zs_observe.limeroad_settlement
    process_notes: Source-backed process/reconciliation only; no segment-only process
      variants.
  evidence_refs:
  - ev.limeroad.lifecycle.forward.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.limeroad.return_item_settlement_reversal
  name: LimeRoad ITEM_RETURN settlement reversal
  fields:
    process_family: returns
    business_trigger: Buyer return after delivery creates reverse settlement deduction
      and OMS reverse/credit-note evidence.
    participating_tables:
    - table.zs_observe.limeroad_oms
    - table.zs_observe.limeroad_settlement
    process_notes: Source-backed process/reconciliation only; no segment-only process
      variants.
  evidence_refs:
  - ev.limeroad.lifecycle.return.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.limeroad.rto_settlement_reversal
  name: LimeRoad ITEM_RTO settlement reversal
  fields:
    process_family: returns
    business_trigger: Failed delivery creates ITEM_RTO/RETURNED_TO_ORIGIN negative
      settlement and OMS reverse credit-note context.
    participating_tables:
    - table.zs_observe.limeroad_oms
    - table.zs_observe.limeroad_settlement
    process_notes: Source-backed process/reconciliation only; no segment-only process
      variants.
  evidence_refs:
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.limeroad.cancellation_settlement_reversal
  name: LimeRoad ITEM_CANCEL settlement reversal
  fields:
    process_family: returns
    business_trigger: Cancelled orders are represented by ITEM_CANCEL/ORDER_CANCELLED
      negative settlement entries, sometimes alongside original ITEM_SALE rows.
    participating_tables:
    - table.zs_observe.limeroad_settlement
    process_notes: Source-backed process/reconciliation only; no segment-only process
      variants.
  evidence_refs:
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.limeroad.marketplace_internal_reconciliation
  name: LimeRoad marketplace internal reconciliation
  fields:
    process_family: reconciliation
    business_trigger: Marketplace-internal reconciliation among OMS forward rows,
      settlement ledger rows, NSP payout formula, TCS visibility, and reverse entries.
    participating_tables:
    - table.zs_observe.limeroad_oms
    - table.zs_observe.limeroad_settlement
    process_notes: Source-backed process/reconciliation only; no segment-only process
      variants.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.relationships.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.forward.oms_forward_sale_invoice
  name: OMS forward sale invoice recorded
  fields:
    step_order: 1
    step_description: limeroad_oms.transaction_type='forward' and eventtype='sale';
      seller GST invoice generated from source_gst_id/source_state.
    source_specific_fields:
    - limeroad_oms.transaction_type
    - '''forward'''
    - '''sale'''
  evidence_refs:
  - ev.limeroad.lifecycle.forward.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.forward.seller_dispatch_courier_context
  name: Seller dispatch / courier context captured
  fields:
    step_order: 2
    step_description: Seller dispatches from documented Mensa GSTIN warehouse; AWB/transporter
      appear as marketplace courier context only.
    source_specific_fields: []
  evidence_refs:
  - ev.limeroad.lifecycle.forward.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.forward.delivered_item_sale_settlement
  name: Delivered ITEM_SALE settlement row recorded
  fields:
    step_order: 3
    step_description: limeroad_settlement.entry_type='ITEM_SALE' and order_status='ORDER_DELIVERED'
      captures delivered sale in settlement ledger.
    source_specific_fields:
    - limeroad_settlement.entry_type
    - '''ITEM_SALE'''
    - '''ORDER_DELIVERED'''
  evidence_refs:
  - ev.limeroad.lifecycle.forward.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.forward.nsp_payout_calculated
  name: NSP payout calculated
  fields:
    step_order: 4
    step_description: settled_amount is calculated from vendor_nsp x 0.587 under current
      41.3% commission model; charged_amount may differ from sale_return_amount for
      COD.
    source_specific_fields: []
  evidence_refs:
  - ev.limeroad.lifecycle.forward.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.forward.settlement_date_cashflow
  name: Settlement date cash-flow record
  fields:
    step_order: 5
    step_description: settlement_date, not created_date, is used for cash-flow/payout
      reporting.
    source_specific_fields: []
  evidence_refs:
  - ev.limeroad.lifecycle.forward.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.return.item_return_in_settlement
  name: ITEM_RETURN reverse settlement deduction
  fields:
    step_order: 1
    step_description: limeroad_settlement.entry_type='ITEM_RETURN', transaction_type='reverse',
      order_status='ORDER_DELIVERED', with negative settled_amount.
    source_specific_fields:
    - limeroad_settlement.entry_type
    - '''ITEM_RETURN'''
    - '''reverse'''
    - '''ORDER_DELIVERED'''
  evidence_refs:
  - ev.limeroad.lifecycle.return.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.return.commission_reversal_recorded
  name: Commission reversal recorded on return
  fields:
    step_order: 2
    step_description: gross_commission is reversed/credited back on return while seller
      payout is deducted through negative settled_amount.
    source_specific_fields: []
  evidence_refs:
  - ev.limeroad.lifecycle.return.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.return.oms_reverse_credit_note
  name: OMS reverse / credit-note evidence recorded
  fields:
    step_order: 3
    step_description: limeroad_oms.transaction_type='reverse' and eventtype='return'
      captures the credit-note/return invoice; eventtype may be NULL for old reverse
      rows.
    source_specific_fields:
    - limeroad_oms.transaction_type
    - '''reverse'''
    - '''return'''
  evidence_refs:
  - ev.limeroad.lifecycle.return.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.rto.returned_to_origin_settlement
  name: ITEM_RTO returned-to-origin settlement deduction
  fields:
    step_order: 1
    step_description: limeroad_settlement.entry_type='ITEM_RTO', order_status='RETURNED_TO_ORIGIN',
      settled_amount negative.
    source_specific_fields:
    - limeroad_settlement.entry_type
    - '''ITEM_RTO'''
    - '''RETURNED_TO_ORIGIN'''
  evidence_refs:
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.rto.oms_reverse_failed_delivery
  name: OMS reverse credit note for failed delivery
  fields:
    step_order: 2
    step_description: limeroad_oms.transaction_type='reverse' captures credit note
      for failed shipment / RTO.
    source_specific_fields:
    - limeroad_oms.transaction_type
    - '''reverse'''
  evidence_refs:
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.cancel.item_cancel_settlement
  name: ITEM_CANCEL settlement reversal
  fields:
    step_order: 1
    step_description: limeroad_settlement.entry_type='ITEM_CANCEL' and order_status='ORDER_CANCELLED'
      records negative settlement reversal.
    source_specific_fields:
    - limeroad_settlement.entry_type
    - '''ITEM_CANCEL'''
    - '''ORDER_CANCELLED'''
  evidence_refs:
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.limeroad.cancel.sale_and_cancel_pairing
  name: Sale and cancellation pairing for same order
  fields:
    step_order: 2
    step_description: Forward ITEM_SALE entry and reverse ITEM_CANCEL entry may both
      be present for the same order, requiring deliberate netting.
    source_specific_fields: []
  evidence_refs:
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.limeroad.forward_oms_to_settlement_sale
  name: OMS forward sale -> settlement ITEM_SALE
  fields:
    state_column: limeroad_oms.transaction_type
    from_state: forward
    to_state: limeroad_settlement.entry_type=ITEM_SALE/order_status=ORDER_DELIVERED
    trigger: Forward sale has delivered settlement record.
    binding_process: business_process.limeroad.forward_nsp_settlement
  evidence_refs:
  - ev.limeroad.lifecycle.forward.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.limeroad.item_sale_to_item_return
  name: ITEM_SALE -> ITEM_RETURN
  fields:
    state_column: limeroad_settlement.entry_type
    from_state: ITEM_SALE
    to_state: ITEM_RETURN
    trigger: Buyer return after delivery creates reverse settlement deduction.
    binding_process: business_process.limeroad.return_item_settlement_reversal
  evidence_refs:
  - ev.limeroad.lifecycle.return.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.limeroad.item_sale_to_item_rto
  name: ITEM_SALE -> ITEM_RTO
  fields:
    state_column: limeroad_settlement.entry_type
    from_state: ITEM_SALE
    to_state: ITEM_RTO
    trigger: Courier failed delivery / returned-to-origin creates negative settlement.
    binding_process: business_process.limeroad.rto_settlement_reversal
  evidence_refs:
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.limeroad.item_sale_to_item_cancel
  name: ITEM_SALE -> ITEM_CANCEL
  fields:
    state_column: limeroad_settlement.entry_type
    from_state: ITEM_SALE
    to_state: ITEM_CANCEL
    trigger: Cancellation may appear as reverse ITEM_CANCEL paired with original sale.
    binding_process: business_process.limeroad.cancellation_settlement_reversal
  evidence_refs:
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.limeroad.oms_forward_to_reverse
  name: OMS forward -> OMS reverse
  fields:
    state_column: limeroad_oms.transaction_type
    from_state: forward
    to_state: reverse
    trigger: Return/RTO/cancel credit-note context appears as OMS reverse; eventtype
      may be NULL for old rows.
    binding_process: business_process.limeroad.return_item_settlement_reversal
  evidence_refs:
  - ev.limeroad.lifecycle.return.001
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  name: LimeRoad OMS ↔ settlement invoice-item reconciliation
  fields:
    profile_family: marketplace_internal_reconciliation
    unit_grain: invoice_number + item_id
    participating_tables:
    - table.zs_observe.limeroad_oms
    - table.zs_observe.limeroad_settlement
    matching_or_validation_logic: Compare OMS forward invoice value to settlement
      charged_amount; status Not in Settlement, Price Variance (>1), or Matched.
    sql_ref: sql.limeroad.recon.oms_settlement_invoice_item
    scope_boundary: Marketplace tables only; no bank/logistics/ERP/statutory reconciliation.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.relationships.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.limeroad.nsp_payout_validation
  name: LimeRoad NSP payout validation
  fields:
    profile_family: marketplace_internal_reconciliation
    unit_grain: order/item settlement row
    participating_tables:
    - table.zs_observe.limeroad_settlement
    matching_or_validation_logic: Compare actual settled_amount to ROUND(vendor_nsp
      * (1 - gross_commission_perc / 100), 2).
    sql_ref: sql.limeroad.settlement.commission_validation
    scope_boundary: Marketplace tables only; no bank/logistics/ERP/statutory reconciliation.
  evidence_refs:
  - ev.limeroad.settlement.nsp_formula.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.limeroad.waterfall_mrp_nsp_settled
  name: LimeRoad MRP → NSP → settlement waterfall
  fields:
    profile_family: marketplace_internal_reconciliation
    unit_grain: brand/period/item_sale rows
    participating_tables:
    - table.zs_observe.limeroad_settlement
    matching_or_validation_logic: Track MRP, vendor discount, vendor_nsp, buyer charged
      amount, LR discount, gross commission, and net payout.
    sql_ref: sql.limeroad.recon.nsp_waterfall
    scope_boundary: Marketplace tables only; no bank/logistics/ERP/statutory reconciliation.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.limeroad.reverse_entries_audit
  name: LimeRoad reverse entry audit
  fields:
    profile_family: marketplace_internal_reconciliation
    unit_grain: invoice_number + item_id reverse row
    participating_tables:
    - table.zs_observe.limeroad_settlement
    - table.zs_observe.limeroad_oms
    matching_or_validation_logic: Audit ITEM_RETURN, ITEM_RTO, and ITEM_CANCEL rows
      against original OMS line value and reverse evidence.
    sql_ref: sql.limeroad.recon.reverse_entries_audit
    scope_boundary: Marketplace tables only; no bank/logistics/ERP/statutory reconciliation.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.lifecycle.return.001
  - ev.limeroad.lifecycle.rto_cancel.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
  name: LimeRoad OMS-only TCS visibility check
  fields:
    profile_family: marketplace_internal_reconciliation
    unit_grain: month/source
    participating_tables:
    - table.zs_observe.limeroad_oms
    matching_or_validation_logic: TCS is visible in OMS only; do not force a settlement-side
      TCS reconciliation because the source says no TCS field exists in settlement.
    sql_ref: sql.limeroad.oms.tcs_visibility
    scope_boundary: Marketplace tables only; no bank/logistics/ERP/statutory reconciliation.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.limeroad.oms_settlement.expected_oms_forward
  name: Expected Oms Forward
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    side_role: expected
    table_id: table.zs_observe.limeroad_oms
    side_definition: OMS forward rows where is_active=true and transaction_type='forward'.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.limeroad.oms_settlement.actual_settlement
  name: Actual Settlement
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    side_role: actual
    table_id: table.zs_observe.limeroad_settlement
    side_definition: Settlement rows joined by invoice_number + item_id where is_active=true.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.limeroad.nsp.expected_formula
  name: Expected Formula
  fields:
    profile_id: reconciliation_profile.limeroad.nsp_payout_validation
    side_role: expected
    table_id: table.zs_observe.limeroad_settlement
    side_definition: ROUND(vendor_nsp * (1 - gross_commission_perc / 100), 2).
  evidence_refs:
  - ev.limeroad.settlement.nsp_formula.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.limeroad.nsp.actual_settled
  name: Actual Settled
  fields:
    profile_id: reconciliation_profile.limeroad.nsp_payout_validation
    side_role: actual
    table_id: table.zs_observe.limeroad_settlement
    side_definition: Actual settled_amount on ITEM_SALE rows with vendor_nsp > 0.
  evidence_refs:
  - ev.limeroad.settlement.nsp_formula.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.limeroad.reverse.settlement_reverse
  name: Settlement Reverse
  fields:
    profile_id: reconciliation_profile.limeroad.reverse_entries_audit
    side_role: source
    table_id: table.zs_observe.limeroad_settlement
    side_definition: ITEM_RETURN, ITEM_RTO, ITEM_CANCEL rows with negative settlement
      impact.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.limeroad.reverse.oms_original
  name: Oms Original
  fields:
    profile_id: reconciliation_profile.limeroad.reverse_entries_audit
    side_role: comparison
    table_id: table.zs_observe.limeroad_oms
    side_definition: Original/credit-note OMS values joined by invoice_number + item_id.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.limeroad.tcs.oms_only
  name: Oms Only
  fields:
    profile_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
    side_role: source
    table_id: table.zs_observe.limeroad_oms
    side_definition: TCS fields are visible in OMS only.
  evidence_refs:
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.limeroad.invoice_item
  name: Invoice Item
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    unit_definition: invoice_number + item_id; fallback order_id coverage check
  evidence_refs:
  - ev.limeroad.relationships.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.limeroad.nsp_order_item
  name: Nsp Order Item
  fields:
    profile_id: reconciliation_profile.limeroad.nsp_payout_validation
    unit_definition: settlement ITEM_SALE order/item row with vendor_nsp > 0
  evidence_refs:
  - ev.limeroad.settlement.nsp_formula.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.limeroad.reverse_invoice_item
  name: Reverse Invoice Item
  fields:
    profile_id: reconciliation_profile.limeroad.reverse_entries_audit
    unit_definition: reverse settlement row joined to OMS by invoice_number + item_id
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.limeroad.tcs_month
  name: Tcs Month
  fields:
    profile_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
    unit_definition: month/source summary from OMS only
  evidence_refs:
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.limeroad.invoice_item_match
  name: Invoice Item Match
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    logic_text: LEFT JOIN settlement ON o.invoice_number=s.invoice_number AND o.item_id=s.item_id
      AND s.is_active=true; o.is_active=true AND o.transaction_type='forward'.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.limeroad.order_id_coverage
  name: Order Id Coverage
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    logic_text: Use order_id as coverage/fallback check; source states 98.7% coverage
      on both invoice/item and order_id.
  evidence_refs:
  - ev.limeroad.relationships.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.limeroad.nsp_formula_match
  name: Nsp Formula Match
  fields:
    profile_id: reconciliation_profile.limeroad.nsp_payout_validation
    logic_text: Expected settled_amount = ROUND(vendor_nsp * (1 - gross_commission_perc
      / 100), 2); filter entry_type=ITEM_SALE and vendor_nsp > 0.
  evidence_refs:
  - ev.limeroad.settlement.nsp_formula.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.limeroad.reverse_audit_match
  name: Reverse Audit Match
  fields:
    profile_id: reconciliation_profile.limeroad.reverse_entries_audit
    logic_text: Filter settlement entry_type IN ('ITEM_RETURN','ITEM_RTO','ITEM_CANCEL')
      and join OMS by invoice_number + item_id.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.limeroad.tcs_oms_only
  name: Tcs Oms Only
  fields:
    profile_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
    logic_text: Sum TCS component fields from OMS forward rows only; no settlement-side
      TCS field should be expected.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.limeroad.not_in_settlement
  name: Not in Settlement
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    mismatch_key: not_in_settlement
    mismatch_definition: OMS forward row has no joined settlement row; may be pending
      settlement or data gap.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.limeroad.price_variance
  name: Price Variance
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    mismatch_key: price_variance
    mismatch_definition: ABS(OMS charged_amount - settlement charged_amount) > 1 per
      source SQL.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.limeroad.historical_settlement_extra
  name: Historical / adjustment settlement extra
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    mismatch_key: historical_adjustment_settlement_extra
    mismatch_definition: Settlement has older/pre-OMS or adjustment rows; not automatically
      a defect.
  evidence_refs:
  - ev.limeroad.relationships.001
  - ev.limeroad.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.limeroad.nsp_formula_variance
  name: NSP Formula Variance
  fields:
    profile_id: reconciliation_profile.limeroad.nsp_payout_validation
    mismatch_key: nsp_formula_variance
    mismatch_definition: Actual settled_amount differs from rounded vendor_nsp * (1
      - gross_commission_perc/100).
  evidence_refs:
  - ev.limeroad.settlement.nsp_formula.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.limeroad.reverse_without_original_oms
  name: Reverse without original OMS line
  fields:
    profile_id: reconciliation_profile.limeroad.reverse_entries_audit
    mismatch_key: reverse_without_original_oms_line
    mismatch_definition: Return/RTO/cancel settlement row does not join to original/credit-note
      OMS line.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.limeroad.null_entry_type_unclassified
  name: NULL entry_type unclassified
  fields:
    profile_id: reconciliation_profile.limeroad.waterfall_mrp_nsp_settled
    mismatch_key: null_entry_type_unclassified
    mismatch_definition: 14 old settlement rows carry financial data but cannot be
      sale/return-classified; include in totals, exclude from type-specific ratios
      unless explicitly handled.
  evidence_refs:
  - ev.limeroad.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.limeroad.settlement_tcs_absent_expected
  name: Settlement TCS field absent by design
  fields:
    profile_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
    mismatch_key: settlement_tcs_field_absent_by_design
    mismatch_definition: No settlement TCS field exists in source; forcing a settlement-side
      TCS match is wrong.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.limeroad.historical_settlement_pre_oms
  name: Historical settlement rows before OMS range
  fields:
    profile_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
    variant_definition: Settlement starts May 2024 and covers older orders before
      OMS Jan 2025, so extra settlement rows are expected historical data.
    variant_type: source_data_coverage_or_classification_variant
  evidence_refs:
  - ev.limeroad.relationships.001
  - ev.limeroad.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.limeroad.cod_sale_return_amount_base
  name: COD sale_return_amount settlement base
  fields:
    profile_id: reconciliation_profile.limeroad.nsp_payout_validation
    variant_definition: For COD rows sale_return_amount differs from charged_amount
      because COD charge is deducted; use sale_return_amount for commission base and
      charged_amount for GMV.
    variant_type: source_data_coverage_or_classification_variant
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.limeroad.null_entry_type_rows
  name: NULL entry_type old settlement rows
  fields:
    profile_id: reconciliation_profile.limeroad.waterfall_mrp_nsp_settled
    variant_definition: 14 NULL entry_type rows carry financial data; include in total
      settlement but avoid assigning sale/return semantics unless specifically reviewed.
    variant_type: source_data_coverage_or_classification_variant
  evidence_refs:
  - ev.limeroad.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.total_forward_gmv
  name: Total forward GMV
  fields:
    natural_language_patterns:
    - What is LimeRoad GMV?
    - Total forward GMV
    - Forward sales and commission
    primary_metric: metric.marketplace.gross_gmv
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.forward_gmv
    sql_ref: sql.limeroad.settlement.forward_gmv
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.return_rate
  name: Return/RTO/cancel rates
  fields:
    natural_language_patterns:
    - What is the return rate?
    - RTO rate
    - Cancellation rate
    primary_metric: metric.marketplace.return_rate
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.return_rate
    sql_ref: sql.limeroad.settlement.return_rate
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.aov
  name: Average order value
  fields:
    natural_language_patterns:
    - What is AOV?
    - Average order value
    primary_metric: metric.marketplace.average_order_value
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.aov
    sql_ref: sql.limeroad.settlement.aov
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.net_settlement_after_returns
  name: Net settlement after returns
  fields:
    natural_language_patterns:
    - Net seller payout after returns
    - Net settled revenue
    primary_metric: metric.marketplace.net_settled_revenue
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.net_after_returns
    sql_ref: sql.limeroad.settlement.net_after_returns
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.monthly_oms_performance
  name: Monthly OMS performance
  fields:
    natural_language_patterns:
    - Monthly GMV trend
    - Monthly OMS performance
    primary_metric: metric.marketplace.gross_gmv
    source_tables:
    - table.zs_observe.limeroad_oms
    query_logic: Use SQL pattern sql.limeroad.oms.monthly_performance
    sql_ref: sql.limeroad.oms.monthly_performance
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.oms.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.brand_payout_efficiency
  name: Brand-level payout efficiency
  fields:
    natural_language_patterns:
    - Brand payout efficiency
    - Payout percentage by brand
    primary_metric: metric.marketplace.brand_payout_efficiency
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.brand_payout_efficiency
    sql_ref: sql.limeroad.settlement.brand_payout_efficiency
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.oms_settlement_reconciliation
  name: OMS settlement invoice-item reconciliation
  fields:
    natural_language_patterns:
    - OMS settlement reconciliation
    - Not in Settlement
    - Price variance
    primary_metric: metric.marketplace.gross_gmv
    source_tables:
    - table.zs_observe.limeroad_oms
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.recon.oms_settlement_invoice_item
    sql_ref: sql.limeroad.recon.oms_settlement_invoice_item
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.nsp_waterfall
  name: MRP to NSP to settlement waterfall
  fields:
    natural_language_patterns:
    - NSP waterfall
    - MRP to settlement
    - Payout percentage of NSP
    primary_metric: metric.marketplace.seller_realization_rate
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.recon.nsp_waterfall
    sql_ref: sql.limeroad.recon.nsp_waterfall
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.tcs_visibility
  name: TCS visibility from OMS
  fields:
    natural_language_patterns:
    - TCS reconciliation
    - OMS TCS
    - TCS in settlement
    primary_metric: metric.marketplace.tcs_deducted
    source_tables:
    - table.zs_observe.limeroad_oms
    query_logic: Use SQL pattern sql.limeroad.oms.tcs_visibility
    sql_ref: sql.limeroad.oms.tcs_visibility
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.reverse_entry_audit
  name: Return/RTO/cancel reverse entry audit
  fields:
    natural_language_patterns:
    - Return reverse audit
    - RTO deductions
    - cancel reversal
    primary_metric: metric.marketplace.return_reversal_amount
    source_tables:
    - table.zs_observe.limeroad_settlement
    - table.zs_observe.limeroad_oms
    query_logic: Use SQL pattern sql.limeroad.recon.reverse_entries_audit
    sql_ref: sql.limeroad.recon.reverse_entries_audit
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.payout_by_settlement_date
  name: Payout summary by settlement date
  fields:
    natural_language_patterns:
    - Payout by date
    - Settlement date payout
    primary_metric: metric.marketplace.net_settled_revenue
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.payout_by_date
    sql_ref: sql.limeroad.settlement.payout_by_date
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.financial_waterfall_full
  name: Full financial waterfall
  fields:
    natural_language_patterns:
    - Full settlement waterfall
    - Gross to net settlement
    primary_metric: metric.marketplace.net_settled_revenue
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.financial_waterfall_full
    sql_ref: sql.limeroad.settlement.financial_waterfall_full
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.commission_validation
  name: Commission validation
  fields:
    natural_language_patterns:
    - Validate commission
    - Validate settled amount
    - NSP formula variance
    primary_metric: metric.marketplace.effective_commission_rate
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.commission_validation
    sql_ref: sql.limeroad.settlement.commission_validation
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.settlement.nsp_formula.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.return_rate_by_brand
  name: Return rate by brand
  fields:
    natural_language_patterns:
    - Return rate by brand
    - RTO by brand
    primary_metric: metric.marketplace.return_rate
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.return_rate_by_brand
    sql_ref: sql.limeroad.settlement.return_rate_by_brand
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.category_performance
  name: Category-level performance
  fields:
    natural_language_patterns:
    - Category performance
    - Classification GMV
    primary_metric: metric.marketplace.gross_gmv
    source_tables:
    - table.zs_observe.limeroad_settlement
    query_logic: Use SQL pattern sql.limeroad.settlement.category_performance
    sql_ref: sql.limeroad.settlement.category_performance
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.gst_split
  name: Interstate vs intrastate GST split
  fields:
    natural_language_patterns:
    - GST split
    - Interstate vs intrastate
    primary_metric: metric.marketplace.tcs_deducted
    source_tables:
    - table.zs_observe.limeroad_oms
    query_logic: Use SQL pattern sql.limeroad.oms.gst_split
    sql_ref: sql.limeroad.oms.gst_split
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.oms.queries.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.brand_hsn_performance
  name: Brand HSN performance
  fields:
    natural_language_patterns:
    - Brand HSN performance
    - Brand GST
    primary_metric: metric.marketplace.gross_gmv
    source_tables:
    - table.zs_observe.limeroad_oms
    query_logic: Use SQL pattern sql.limeroad.oms.brand_hsn_performance
    sql_ref: sql.limeroad.oms.brand_hsn_performance
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.oms.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.limeroad.tcs_tds_summary
  name: TCS and TDS summary
  fields:
    natural_language_patterns:
    - TCS TDS summary
    - How much TCS and TDS
    primary_metric: metric.marketplace.tcs_deducted
    source_tables:
    - table.zs_observe.limeroad_oms
    query_logic: Use SQL pattern sql.limeroad.oms.tcs_tds_summary
    sql_ref: sql.limeroad.oms.tcs_tds_summary
    scope_policy: Documented LimeRoad group_level_id=22 is included in source-backed
      SQL; runtime may layer external scope resolution.
  evidence_refs:
  - ev.limeroad.oms.queries.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.active_scope_filter
  name: LimeRoad active/scope filter
  fields:
    rule_type: query_filter
    rule_text: Always filter LimeRoad marketplace tables with is_active = true and
      documented group_level_id = 22 unless runtime scope resolution overrides the
      value explicitly.
    severity: high
    related_canonical_ids:
    - table.zs_observe.limeroad_oms
    - table.zs_observe.limeroad_settlement
  evidence_refs:
  - ev.limeroad.filters.001
  - ev.limeroad.scope.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.forward_revenue_filter
  name: LimeRoad forward revenue filter
  fields:
    rule_type: query_filter
    rule_text: Revenue/GMV queries must isolate limeroad_oms.transaction_type='forward'
      or limeroad_settlement.entry_type='ITEM_SALE' depending on source table.
    severity: medium
    related_canonical_ids:
    - metric.marketplace.gross_gmv
  evidence_refs:
  - ev.limeroad.filters.001
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.settlement_delivered_sales_filter
  name: Settlement delivered sales filter
  fields:
    rule_type: query_filter
    rule_text: Delivered settlement sales use entry_type='ITEM_SALE' and order_status='ORDER_DELIVERED'.
    severity: medium
    related_canonical_ids:
    - table.zs_observe.limeroad_settlement
  evidence_refs:
  - ev.limeroad.filters.001
  - ev.limeroad.lifecycle.forward.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.returns_filter
  name: Settlement returns filter
  fields:
    rule_type: query_filter
    rule_text: Return/RTO reporting uses entry_type IN ('ITEM_RETURN','ITEM_RTO');
      cancellations use ITEM_CANCEL separately unless deliberately netted.
    severity: medium
    related_canonical_ids:
    - metric.marketplace.return_rate
    - metric.marketplace.rto_rate
  evidence_refs:
  - ev.limeroad.filters.001
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.vendor_nsp_required
  name: Vendor NSP required for payout validation
  fields:
    rule_type: formula_guard
    rule_text: For settlement validation, filter vendor_nsp IS NOT NULL AND vendor_nsp
      > 0; vendor_nsp is not present in OMS.
    severity: medium
    related_canonical_ids:
    - metric.marketplace.effective_commission_rate
    - metric.marketplace.seller_realization_rate
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.sale_return_amount_commission_base
  name: Use sale_return_amount as commission base
  fields:
    rule_type: formula_guard
    rule_text: For COD rows, sale_return_amount differs from charged_amount because
      COD charge is deducted; use sale_return_amount for gross_commission base and
      charged_amount for GMV.
    severity: medium
    related_canonical_ids:
    - metric.marketplace.effective_commission_rate
    - metric.marketplace.gross_gmv
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.settlement_date_cashflow
  name: Use settlement_date for cash-flow reporting
  fields:
    rule_type: time_dimension_rule
    rule_text: Settlement can occur 2–7 days after order creation; use settlement_date
      for cash-flow/payout reporting.
    severity: medium
    related_canonical_ids:
    - metric.marketplace.net_settled_revenue
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.tcs_tds_oms_only
  name: Use OMS for TCS/TDS visibility
  fields:
    rule_type: source_selection_rule
    rule_text: TCS/TDS are visible in OMS fields; the source TCS reconciliation notes
      no TCS field in settlement.
    severity: medium
    related_canonical_ids:
    - metric.marketplace.tcs_deducted
    - metric.marketplace.tds_deducted
  evidence_refs:
  - ev.limeroad.tax.001
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.tax_rate_normalization
  name: Normalize dual-format tax rates
  fields:
    rule_type: data_quality_rule
    rule_text: Normalize tax rate fields with CASE WHEN rate > 1 THEN rate / 100 ELSE
      rate END before rate validation.
    severity: medium
    related_canonical_ids:
    - table.zs_observe.limeroad_oms
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.source_state_case_normalization
  name: Normalize source_state case for joins
  fields:
    rule_type: data_quality_rule
    rule_text: Use UPPER(source_state) or equivalent when comparing OMS lowercase
      source_state to settlement/source-state labels.
    severity: medium
    related_canonical_ids:
    - table.zs_observe.limeroad_oms
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.primary_duplicate_fields
  name: Use primary duplicate field pairs
  fields:
    rule_type: data_quality_rule
    rule_text: Use primary fields hsn, description, order_id, and item_id instead
      of hsncode/productdescription/orderid/uniqueitemid unless raw alias is required.
    severity: medium
    related_canonical_ids:
    - table.zs_observe.limeroad_oms
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.null_entry_type_include_totals
  name: Include NULL entry_type old settlement rows in totals
  fields:
    rule_type: data_quality_rule
    rule_text: 14 NULL entry_type settlement rows carry financial data; include in
      overall totals but avoid sale/return classification unless explicitly handled.
    severity: medium
    related_canonical_ids:
    - table.zs_observe.limeroad_settlement
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.no_segment_only_process_variants
  name: Do not create segment-only process variants
  fields:
    rule_type: parser_guard
    rule_text: NSP model, fulfilment labels, return/RTO/cancel labels, payment mode,
      brands, and category paths are rules/processes/value profiles, not process_variant
      cards unless a materially different process is documented.
    severity: medium
    related_canonical_ids:
    - platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.fulfillment.001
  - ev.limeroad.nsp_model.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.scope_identifiers_not_account_cards
  name: Scope identifiers are not account cards
  fields:
    rule_type: scope_guardrail
    rule_text: group_level_id, GSTINs, seller entity, AWB, and bank-transfer mentions
      are columns/caveats only; do not create tenant, group, platform_account, bank,
      external logistics, ERP, or statutory-filing cards.
    severity: high
    related_canonical_ids:
    - platform_context.limeroad.in
  evidence_refs:
  - ev.limeroad.scope.001
  - ev.limeroad.overview.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.limeroad.benchmark_guidance_only
  name: Context values are guidance only
  fields:
    rule_type: benchmark_rule
    rule_text: Observed values such as 41.3% commission, 18.7% return rate, 18.1%
      RTO rate, 9.2% cancellation rate, and ₹970.87 AOV are source-backed guidance/context,
      not universal hard-fail thresholds.
    severity: medium
    related_canonical_ids:
    - metric.marketplace.effective_commission_rate
    - metric.marketplace.return_rate
    - metric.marketplace.rto_rate
    - metric.marketplace.average_order_value
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.settlement.values.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.no_process_variant_cards
  name: No process variant cards remain
  fields:
    test_type: semantic_guard
    assertion: COUNT(card_type=process_variant) = 0
    expected_result: pass
    failure_meaning: Prevents segment-only variants from V8.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.sql_refs_resolve
  name: All SQL references resolve
  fields:
    test_type: sql_integrity
    assertion: Every card fields.sql_ref/formula_sql_ref must exist in sql_pattern
      registry.
    expected_result: pass
    failure_meaning: Prevents lazy “see source doc” SQL refs.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.edge_refs_resolve
  name: All edge endpoints resolve
  fields:
    test_type: edge_integrity
    assertion: Every candidate_edge source_card_id and target_card_id must exist as
      a candidate_card.
    expected_result: pass
    failure_meaning: Prevents dangling graph refs after deleting V8 cards.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.active_filters_present
  name: Active filters present in SQL patterns
  fields:
    test_type: query_guard
    assertion: Core SQL patterns include is_active = true.
    expected_result: pass
    failure_meaning: Prevents inactive-row inflation.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.nsp_formula_validation
  name: NSP formula validation executable
  fields:
    test_type: formula_validation
    assertion: Commission validation SQL uses vendor_nsp and gross_commission_perc,
      not charged_amount alone.
    expected_result: pass
    failure_meaning: Prevents wrong commission base.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.oms_settlement_tolerance
  name: OMS settlement reconciliation tolerance encoded
  fields:
    test_type: reconciliation_validation
    assertion: OMS-settlement query marks Price Variance when ABS(o.charged_amount
      - s.charged_amount) > 1.
    expected_result: pass
    failure_meaning: Source-supported variance threshold.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.null_entry_type_totals
  name: NULL entry_type included in totals
  fields:
    test_type: data_quality_guard
    assertion: Overall settlement totals should not exclude NULL entry_type rows unless
      metric intentionally classifies entry_type.
    expected_result: pass
    failure_meaning: Prevents undercounting old rows.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.scope_no_account_cards
  name: No forbidden scope cards from group_level_id/GSTIN
  fields:
    test_type: scope_guard
    assertion: No tenant/group/platform_account/account_data_binding/bank/logistics/statutory
      filing cards are created.
    expected_result: pass
    failure_meaning: Preserves marketplace-only boundary.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.tax_rate_normalization
  name: Tax rate normalization applied
  fields:
    test_type: data_quality_guard
    assertion: Tax-rate validation should normalize values >1 by dividing by 100.
    expected_result: pass
    failure_meaning: Prevents 0.12 vs 12.0 false variance.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.limeroad.reverse_eventtype_not_required
  name: Reverse eventtype NULL handled
  fields:
    test_type: data_quality_guard
    assertion: Return filters use transaction_type='reverse' or settlement entry_type,
      not OMS eventtype alone.
    expected_result: pass
    failure_meaning: Captures 26 older reverse OMS rows with NULL eventtype.
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.filters.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.limeroad.oms_settlement_reconciliation
  name: OMS settlement reconciliation output
  fields:
    query_pattern_id: query_pattern.limeroad.oms_settlement_reconciliation
    output_fields:
    - invoice_number
    - order_id
    - item_id
    - oms_invoice_value
    - stl_charged
    - vendor_nsp
    - settled_amount
    - price_variance
    - recon_status
    must_include:
    - invoice_number
    - order_id
    - item_id
    empty_output_contract: false
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.limeroad.financial_waterfall
  name: Financial waterfall output
  fields:
    query_pattern_id: query_pattern.limeroad.financial_waterfall_full
    output_fields:
    - total_mrp
    - gross_gmv
    - vendor_discount
    - total_vendor_nsp
    - lr_commission
    - forward_settled
    - reverse_settled
    - net_settled
    must_include:
    - total_mrp
    - gross_gmv
    - vendor_discount
    empty_output_contract: false
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.limeroad.return_rate
  name: Return/RTO/cancel rate output
  fields:
    query_pattern_id: query_pattern.limeroad.return_rate
    output_fields:
    - return_rate_pct
    - rto_rate_pct
    - cancel_rate_pct
    must_include:
    - return_rate_pct
    - rto_rate_pct
    - cancel_rate_pct
    empty_output_contract: false
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.limeroad.tcs_tds_summary
  name: TCS/TDS summary output
  fields:
    query_pattern_id: query_pattern.limeroad.tcs_tds_summary
    output_fields:
    - month
    - total_tcs
    - total_tds
    must_include:
    - month
    - total_tcs
    - total_tds
    empty_output_contract: false
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.limeroad.category_performance
  name: Category performance output
  fields:
    query_pattern_id: query_pattern.limeroad.category_performance
    output_fields:
    - classification
    - orders
    - gmv
    - total_nsp
    - seller_payout
    - lr_commission
    - commission_rate
    must_include:
    - classification
    - orders
    - gmv
    empty_output_contract: false
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  create_action: create
  marketplace_only: true
```

## 4. Candidate Edges

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_platform_context.2bd620c1cf
  edge_type: HAS_PLATFORM_CONTEXT
  canonical_edge_type: HAS_PLATFORM_CONTEXT
  source_card_id: platform.limeroad
  target_card_id: platform_context.limeroad.in
  source_type: platform
  target_type: platform_context
  inverse_edge_type: BELONGS_TO_PLATFORM
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.632f2e7231
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.orders
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.89268a67ec
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.settlement
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.11e08242b0
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.returns
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.59ccc7391f
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.reconciliation
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.35f4c27fd7
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.nsp_pricing
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.23fd3a3666
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.tax
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.d5878e26f5
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.fulfillment
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.8c7e00df11
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.product
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.75a7f19e5a
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.promotions
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_domain.4c7e296ad0
  edge_type: HAS_DOMAIN
  canonical_edge_type: HAS_DOMAIN
  source_card_id: platform_context.limeroad.in
  target_card_id: domain.marketplace.limeroad.payment_mode
  source_type: platform_context
  target_type: domain
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_source_table.3311be7f27
  edge_type: HAS_SOURCE_TABLE
  canonical_edge_type: HAS_SOURCE_TABLE
  source_card_id: platform_context.limeroad.in
  target_card_id: table.zs_observe.limeroad_oms
  source_type: platform_context
  target_type: table
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_source_table.da20f78f1c
  edge_type: HAS_SOURCE_TABLE
  canonical_edge_type: HAS_SOURCE_TABLE
  source_card_id: platform_context.limeroad.in
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: platform_context
  target_type: table
  inverse_edge_type: BELONGS_TO_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.8e3c944b58
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.unique_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.5fd5402bbe
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.txn_uuid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.9ecdb261fc
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.unique_value
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.8fc1305e8a
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.invoice_number
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.1211127cbe
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.order_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.dc48764c05
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.item_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.f17e57f5a0
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.unique_item_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.d5b587e35f
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.sku_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ba659c66ff
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.style_code
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.2412bdc644
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.variant_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.e5b42ac75e
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.ui_product_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.c97acd64fe
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.awb
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.def783d1d3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.vendor_invoice_number
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.107056722f
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.vendor_margin_approved_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.e65d2a93de
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.created_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.a0b909d781
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.settlement_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.d6b7353c0d
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.cycle_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.90e3c0eea1
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.order_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.15af2aad00
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.invoice_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.fcae057d4d
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.mrp
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.aeb0788007
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.charged_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.80903483c3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.sale_return_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ab08c8b8b6
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.vendor_nsp
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.51c0bf01ad
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.gross_commission_perc
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.398524935c
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.gross_commission
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.b5efd78bce
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.settled_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.645a0cb5e7
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.transfer_price
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.6033113102
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.lr_margin
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.71c47d1c90
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.lr_commission_as_per_tp
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.b78a2b32df
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.lr_commission_as_per_non_tp
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.c224850f68
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.lr_margin_amount_after_discount_borne_by_limeroad
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.3c527db8a0
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.lr_margin_paid_acquisition
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.e721b1b452
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.margin_model
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.3c583bf256
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.total_vendor_discount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ce410a3258
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.total_limeroad_discount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.e38c183328
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.total_adjustment
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.de04845431
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.gst_adjustment_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.9743dcad41
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.vendor_nsp_after_less_ctp_income
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.9008e00a22
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.weight_mapping_to_vendor_cost
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.648cb44793
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.reversal_of_margin_on_return_cancellation
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.f7f9b43077
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.shipping_charge_paid_by_customer
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.7cfd99511c
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.cod_charge_paid_by_customer
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.a1b151759f
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.handling_charge_paid_by_customer
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.7511bcdeb4
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.shipping_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.afcc57d726
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.transporter_cost_recovered_from_vendor
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.b80adcf986
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.transporter_cost_recovered_from_vendor_on_return
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.57b8084604
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.collection_charges_recovered_from_vendor
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.95363a957e
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.total_payment_amount_made_to_the_vendor
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.db674248ae
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.transaction_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.b655176b9a
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.order_status
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.6fa4a8b038
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.entry_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.49308a7246
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.sub_order_state
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.1f83e5b423
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.payment_mode
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.cfd84b575f
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.brand
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.930d8b80d6
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.classification
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.95768f88d6
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.destination_state
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.1da213ac87
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.customer_state
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.91f33a4763
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.transporter
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.231bd50a8f
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.lost
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.e584a16eec
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.lost_in_transit
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.3693acbf64
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.short_shipment
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.9e876872b3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.group_level_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ed4ecf55c4
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.currency_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.69bfe7f3d4
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.is_active
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.0488271d28
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.brand_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ff72e49cb3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.brand_name
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.5c8ae046dd
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.who_changes_vnsp
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.a9b012b10a
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.date_of_change_vnsp
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.85a8bc323f
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.remarks_for_adjustment
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.1e072133ed
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_settlement
  target_card_id: column.zs_observe.limeroad_settlement.zen_sheet_name
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.297847779e
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.unique_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.eec2b9c6e3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.txn_uuid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.15c5fb6554
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.unique_value
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.909e87cb72
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.invoice_number
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.cd9a7e6951
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.invoiceid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.d3c8369215
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.order_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.f03c6fbe7b
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.orderid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.201553092c
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.suborderid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.1ea4355c73
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.item_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ca8e56b0d9
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.uniqueitemid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.21637691ca
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.other_id_2
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.a6c4974d23
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.sku_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.c58d6aecd7
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.vendorstylecode
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.38bdc514bd
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.source_gst_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.7bfdd1370a
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.gstin
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.0bac5603ee
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.created_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.64e0787c76
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.order_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.14f0f6d82b
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.invoice_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.5c3fb256ca
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.invoicedate
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.2e2538a0c8
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.order_shipped_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.f2ac229cbc
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.shipment_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.5f8660401c
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.mrp
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.8c18aa2c19
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.charged_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.0c139fcb6d
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.charged_amount_excluding_tax
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.3b996da0e6
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.total_tax
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.3d4863712b
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.shipping_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.e51f2ce645
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.total_tds
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.a28e72b1ad
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tdsamount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.c65bc572c3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tax_igst_rate
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ad52f28232
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tax_igst_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.eff91296e9
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tax_cgst_rate
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.4b564b22b3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tax_cgst_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ee33f4646c
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tax_sgst_rate
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.90b4bd087f
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tax_sgst_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.d1597c0e60
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.igst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.4df8922d30
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.taxamountforigst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.8460295b69
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.taxamountforcgst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.db7bf93aec
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.taxamountforsgst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.66b361008c
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.hsn
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.d5e405357c
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.hsncode
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.0bd081ea7e
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.totalgstrate
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.c5f000403b
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tcs_igst_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.3eb7746e59
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tcs_cgst_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.4cc5139cca
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tcs_sgst_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.2388288118
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tcsamountforigst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.cfc97b197a
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tcsamountforcgst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.6efee57fc4
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.tcsamountforsgst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.b616a417d0
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.transaction_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.5d6a5cad27
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.eventtype
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.b1e90d7151
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.salestype
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.ea3ea0024e
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.brand
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.cfa4c073e9
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.description
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.03329ba447
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.productdescription
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.85c06660c3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.quantity
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.76b26721aa
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.temp
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.969d3e84d3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.source_state
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.e4c034d078
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.vendorstate
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.017d763d03
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.source_zipcode
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.e6659cfac9
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.vendorpincode
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.c56f61a941
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.destination_state
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.eec302dfd3
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.customerstate
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.8badc28449
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.destination_zipcode
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.562bcd0a8a
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.customerpincode
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.a865be8bee
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.source_state_code
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.f318a57dc9
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.destination_state_code
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.45f7739410
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.group_level_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.bc9bdf5e6c
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.currency_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.08b62d3054
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.is_active
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.fe8127fb25
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.ancestry
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.c1489eb154
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.sgst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.59e96e4920
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.cgst
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.3c2ab12615
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.none
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.aa6d0860c9
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.failure_reason_order_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_column.055d9aff9b
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.limeroad_oms
  target_card_id: column.zs_observe.limeroad_oms.zen_sheet_name
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.relates_table.725eec083e
  edge_type: RELATES_TABLE
  canonical_edge_type: RELATES_TABLE
  source_card_id: relationship.limeroad.oms_settlement.invoice_item
  target_card_id: table.zs_observe.limeroad_oms
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.relates_table.17a136747c
  edge_type: RELATES_TABLE
  canonical_edge_type: RELATES_TABLE
  source_card_id: relationship.limeroad.oms_settlement.invoice_item
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.relates_table.f86d40e15f
  edge_type: RELATES_TABLE
  canonical_edge_type: RELATES_TABLE
  source_card_id: relationship.limeroad.oms_settlement.order_id
  target_card_id: table.zs_observe.limeroad_oms
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.relates_table.98908d72f5
  edge_type: RELATES_TABLE
  canonical_edge_type: RELATES_TABLE
  source_card_id: relationship.limeroad.oms_settlement.order_id
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.4c5c28c38a
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.settlement.entry_type
  target_card_id: column.zs_observe.limeroad_settlement.entry_type
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.9e0bf57022
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.settlement.order_status
  target_card_id: column.zs_observe.limeroad_settlement.order_status
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.9d6cb33d31
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.settlement.transaction_type
  target_card_id: column.zs_observe.limeroad_settlement.transaction_type
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.58847ab1fa
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.settlement.payment_mode
  target_card_id: column.zs_observe.limeroad_settlement.payment_mode
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.ebdf63af4d
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.settlement.brand
  target_card_id: column.zs_observe.limeroad_settlement.brand
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.b449eadbcf
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.oms.brand
  target_card_id: column.zs_observe.limeroad_oms.brand
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.21426e4c86
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.settlement.transporter
  target_card_id: column.zs_observe.limeroad_settlement.transporter
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.763011772b
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.settlement.classification
  target_card_id: column.zs_observe.limeroad_settlement.classification
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.7276c4bc51
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.oms.transaction_type
  target_card_id: column.zs_observe.limeroad_oms.transaction_type
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.4debf82d49
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.oms.eventtype
  target_card_id: column.zs_observe.limeroad_oms.eventtype
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.865435f0f5
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.oms.salestype
  target_card_id: column.zs_observe.limeroad_oms.salestype
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.6fd949603b
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.oms.source_gst_warehouses
  target_card_id: column.zs_observe.limeroad_oms.source_gst_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.79bbf6dfee
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.oms.hsn_rates
  target_card_id: column.zs_observe.limeroad_oms.hsn
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.7cdc88d34b
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.settlement.discount_sign
  target_card_id: column.zs_observe.limeroad_settlement.total_limeroad_discount
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.describes_column.8ef7d9f5eb
  edge_type: DESCRIBES_COLUMN
  canonical_edge_type: DESCRIBES_COLUMN
  source_card_id: value_profile.limeroad.scope.group_level_id
  target_card_id: column.zs_observe.limeroad_oms.group_level_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.c00ff43b60
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.gross_gmv
  target_card_id: metric_implementation.limeroad.gross_gmv
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.e29cc64f8d
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.vendor_nsp_total
  target_card_id: metric_implementation.limeroad.vendor_nsp_total
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.2835970463
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.net_settled_revenue
  target_card_id: metric_implementation.limeroad.net_settled_revenue
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.8f478c3002
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.seller_realization_rate
  target_card_id: metric_implementation.limeroad.seller_realization_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.680698c45b
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.effective_commission_rate
  target_card_id: metric_implementation.limeroad.effective_commission_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.811acca9b6
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.return_rate
  target_card_id: metric_implementation.limeroad.return_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.4b6c583b92
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.rto_rate
  target_card_id: metric_implementation.limeroad.rto_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.3de11729e8
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.cancellation_rate
  target_card_id: metric_implementation.limeroad.cancellation_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.6a0cbe255d
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.average_order_value
  target_card_id: metric_implementation.limeroad.average_order_value
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.24f01aec11
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.brand_payout_efficiency
  target_card_id: metric_implementation.limeroad.brand_payout_efficiency
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.1157ec4320
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.tcs_deducted
  target_card_id: metric_implementation.limeroad.tcs_deducted
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.222d179259
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.tds_deducted
  target_card_id: metric_implementation.limeroad.tds_deducted
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.6c9f29c790
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.limeroad_discount_absorption
  target_card_id: metric_implementation.limeroad.discount_absorption
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric_implementation.37781f7459
  edge_type: HAS_METRIC_IMPLEMENTATION
  canonical_edge_type: HAS_METRIC_IMPLEMENTATION
  source_card_id: metric.marketplace.return_reversal_amount
  target_card_id: metric_implementation.limeroad.return_reversal_amount
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.depends_on_metric.85934590cd
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_card_id: metric.marketplace.seller_realization_rate
  target_card_id: metric.marketplace.gross_gmv
  source_type: metric
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.depends_on_metric.ca32bbc4ac
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_card_id: metric.marketplace.seller_realization_rate
  target_card_id: metric.marketplace.net_settled_revenue
  source_type: metric
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.depends_on_metric.7b859997c1
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_card_id: metric.marketplace.return_reversal_amount
  target_card_id: metric.marketplace.return_rate
  source_type: metric
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.depends_on_metric.745f8b3fe6
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_card_id: metric.marketplace.effective_commission_rate
  target_card_id: metric.marketplace.vendor_nsp_total
  source_type: metric
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_business_process.67a8f95224
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.marketplace.limeroad.orders
  target_card_id: business_process.limeroad.forward_nsp_settlement
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.40d89437ce
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.forward_nsp_settlement
  target_card_id: table.zs_observe.limeroad_oms
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.1472438bb0
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.forward_nsp_settlement
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_business_process.12dd3ef6a6
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.marketplace.limeroad.returns
  target_card_id: business_process.limeroad.return_item_settlement_reversal
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.37ee9aa206
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.return_item_settlement_reversal
  target_card_id: table.zs_observe.limeroad_oms
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.3b996346e1
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.return_item_settlement_reversal
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_business_process.26c7895ebe
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.marketplace.limeroad.returns
  target_card_id: business_process.limeroad.rto_settlement_reversal
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.002d5d7b8e
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.rto_settlement_reversal
  target_card_id: table.zs_observe.limeroad_oms
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.ec06bee0bc
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.rto_settlement_reversal
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_business_process.d8d27cea14
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.marketplace.limeroad.returns
  target_card_id: business_process.limeroad.cancellation_settlement_reversal
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.8e8c032c2a
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.cancellation_settlement_reversal
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_business_process.ef79be980f
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.marketplace.limeroad.reconciliation
  target_card_id: business_process.limeroad.marketplace_internal_reconciliation
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.79fc9ffd7d
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.marketplace_internal_reconciliation
  target_card_id: table.zs_observe.limeroad_oms
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.2fd2f1534d
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.limeroad.marketplace_internal_reconciliation
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.219d6b710f
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.forward_nsp_settlement
  target_card_id: workflow_step.limeroad.forward.oms_forward_sale_invoice
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.7c50a08422
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.forward_nsp_settlement
  target_card_id: workflow_step.limeroad.forward.seller_dispatch_courier_context
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.269a2c86bb
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.forward_nsp_settlement
  target_card_id: workflow_step.limeroad.forward.delivered_item_sale_settlement
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.178a998bb8
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.forward_nsp_settlement
  target_card_id: workflow_step.limeroad.forward.nsp_payout_calculated
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.4c3d5b3ece
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.forward_nsp_settlement
  target_card_id: workflow_step.limeroad.forward.settlement_date_cashflow
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.de7e624114
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.return_item_settlement_reversal
  target_card_id: workflow_step.limeroad.return.item_return_in_settlement
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.644d78abb9
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.return_item_settlement_reversal
  target_card_id: workflow_step.limeroad.return.commission_reversal_recorded
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.ae0fb740ab
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.return_item_settlement_reversal
  target_card_id: workflow_step.limeroad.return.oms_reverse_credit_note
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.d44adb4651
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.rto_settlement_reversal
  target_card_id: workflow_step.limeroad.rto.returned_to_origin_settlement
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.3454ca67d3
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.rto_settlement_reversal
  target_card_id: workflow_step.limeroad.rto.oms_reverse_failed_delivery
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.e6366b4bb0
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.cancellation_settlement_reversal
  target_card_id: workflow_step.limeroad.cancel.item_cancel_settlement
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_workflow_step.d7553e22f6
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.limeroad.cancellation_settlement_reversal
  target_card_id: workflow_step.limeroad.cancel.sale_and_cancel_pairing
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_state_transition.60a8c3fa89
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_card_id: business_process.limeroad.forward_nsp_settlement
  target_card_id: state_transition.limeroad.forward_oms_to_settlement_sale
  source_type: business_process
  target_type: state_transition
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_state_transition.63476ce2a9
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_card_id: business_process.limeroad.return_item_settlement_reversal
  target_card_id: state_transition.limeroad.item_sale_to_item_return
  source_type: business_process
  target_type: state_transition
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_state_transition.37eb84c218
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_card_id: business_process.limeroad.rto_settlement_reversal
  target_card_id: state_transition.limeroad.item_sale_to_item_rto
  source_type: business_process
  target_type: state_transition
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_state_transition.09b326398c
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_card_id: business_process.limeroad.cancellation_settlement_reversal
  target_card_id: state_transition.limeroad.item_sale_to_item_cancel
  source_type: business_process
  target_type: state_transition
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_state_transition.1b3d27fb8d
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_card_id: business_process.limeroad.return_item_settlement_reversal
  target_card_id: state_transition.limeroad.oms_forward_to_reverse
  source_type: business_process
  target_type: state_transition
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_profile.6130cf3c39
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.limeroad.marketplace_internal_reconciliation
  target_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.827c221576
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: table.zs_observe.limeroad_oms
  source_type: reconciliation_profile
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.ffaf24662b
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: reconciliation_profile
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_profile.a75f493810
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.limeroad.marketplace_internal_reconciliation
  target_card_id: reconciliation_profile.limeroad.nsp_payout_validation
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.a0fbc1ce23
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_profile.limeroad.nsp_payout_validation
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: reconciliation_profile
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_profile.9fa768dd2f
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.limeroad.marketplace_internal_reconciliation
  target_card_id: reconciliation_profile.limeroad.waterfall_mrp_nsp_settled
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.8e8e506c28
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_profile.limeroad.waterfall_mrp_nsp_settled
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: reconciliation_profile
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_profile.22bb366cce
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.limeroad.marketplace_internal_reconciliation
  target_card_id: reconciliation_profile.limeroad.reverse_entries_audit
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.2562e5ee97
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_profile.limeroad.reverse_entries_audit
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: reconciliation_profile
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.f551ab1b8a
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_profile.limeroad.reverse_entries_audit
  target_card_id: table.zs_observe.limeroad_oms
  source_type: reconciliation_profile
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_profile.d1600b2741
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.limeroad.marketplace_internal_reconciliation
  target_card_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.83833f6bfc
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
  target_card_id: table.zs_observe.limeroad_oms
  source_type: reconciliation_profile
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_side.788256d21e
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: reconciliation_side.limeroad.oms_settlement.expected_oms_forward
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_side.f1989e2ca1
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: reconciliation_side.limeroad.oms_settlement.actual_settlement
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_side.64241850b0
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.limeroad.nsp_payout_validation
  target_card_id: reconciliation_side.limeroad.nsp.expected_formula
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_side.b3636dbc7a
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.limeroad.nsp_payout_validation
  target_card_id: reconciliation_side.limeroad.nsp.actual_settled
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_side.ef511df71e
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.limeroad.reverse_entries_audit
  target_card_id: reconciliation_side.limeroad.reverse.settlement_reverse
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_side.8d929d1de6
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.limeroad.reverse_entries_audit
  target_card_id: reconciliation_side.limeroad.reverse.oms_original
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_side.49232f164e
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
  target_card_id: reconciliation_side.limeroad.tcs.oms_only
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_unit.79270fdbca
  edge_type: HAS_RECONCILIATION_UNIT
  canonical_edge_type: HAS_RECONCILIATION_UNIT
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: reconciliation_unit.limeroad.invoice_item
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_unit.c9ecf8cd5a
  edge_type: HAS_RECONCILIATION_UNIT
  canonical_edge_type: HAS_RECONCILIATION_UNIT
  source_card_id: reconciliation_profile.limeroad.nsp_payout_validation
  target_card_id: reconciliation_unit.limeroad.nsp_order_item
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_unit.b572b72742
  edge_type: HAS_RECONCILIATION_UNIT
  canonical_edge_type: HAS_RECONCILIATION_UNIT
  source_card_id: reconciliation_profile.limeroad.reverse_entries_audit
  target_card_id: reconciliation_unit.limeroad.reverse_invoice_item
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_unit.a89607f84d
  edge_type: HAS_RECONCILIATION_UNIT
  canonical_edge_type: HAS_RECONCILIATION_UNIT
  source_card_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
  target_card_id: reconciliation_unit.limeroad.tcs_month
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_matching_logic.22189da6dc
  edge_type: HAS_MATCHING_LOGIC
  canonical_edge_type: HAS_MATCHING_LOGIC
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: matching_logic.limeroad.invoice_item_match
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_matching_logic.d6a2a6138a
  edge_type: HAS_MATCHING_LOGIC
  canonical_edge_type: HAS_MATCHING_LOGIC
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: matching_logic.limeroad.order_id_coverage
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_matching_logic.f26c7ef33d
  edge_type: HAS_MATCHING_LOGIC
  canonical_edge_type: HAS_MATCHING_LOGIC
  source_card_id: reconciliation_profile.limeroad.nsp_payout_validation
  target_card_id: matching_logic.limeroad.nsp_formula_match
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_matching_logic.bcd5d9ec24
  edge_type: HAS_MATCHING_LOGIC
  canonical_edge_type: HAS_MATCHING_LOGIC
  source_card_id: reconciliation_profile.limeroad.reverse_entries_audit
  target_card_id: matching_logic.limeroad.reverse_audit_match
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_matching_logic.d7da74a1db
  edge_type: HAS_MATCHING_LOGIC
  canonical_edge_type: HAS_MATCHING_LOGIC
  source_card_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
  target_card_id: matching_logic.limeroad.tcs_oms_only
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_mismatch_category.4e46fd2d1f
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: mismatch_category.limeroad.not_in_settlement
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_mismatch_category.0571f336d2
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: mismatch_category.limeroad.price_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_mismatch_category.1e66b16322
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: mismatch_category.limeroad.historical_settlement_extra
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_mismatch_category.cd6d24ebc1
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.limeroad.nsp_payout_validation
  target_card_id: mismatch_category.limeroad.nsp_formula_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_mismatch_category.0208267b46
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.limeroad.reverse_entries_audit
  target_card_id: mismatch_category.limeroad.reverse_without_original_oms
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_mismatch_category.992d755daf
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.limeroad.waterfall_mrp_nsp_settled
  target_card_id: mismatch_category.limeroad.null_entry_type_unclassified
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_mismatch_category.4ec6f01a9b
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.limeroad.tcs_oms_visibility_check
  target_card_id: mismatch_category.limeroad.settlement_tcs_absent_expected
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_variant.61a58cb191
  edge_type: HAS_RECONCILIATION_VARIANT
  canonical_edge_type: HAS_RECONCILIATION_VARIANT
  source_card_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  target_card_id: reconciliation_variant.limeroad.historical_settlement_pre_oms
  source_type: reconciliation_profile
  target_type: reconciliation_variant
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_variant.35351e4cc9
  edge_type: HAS_RECONCILIATION_VARIANT
  canonical_edge_type: HAS_RECONCILIATION_VARIANT
  source_card_id: reconciliation_profile.limeroad.nsp_payout_validation
  target_card_id: reconciliation_variant.limeroad.cod_sale_return_amount_base
  source_type: reconciliation_profile
  target_type: reconciliation_variant
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_reconciliation_variant.c78b1cc4c6
  edge_type: HAS_RECONCILIATION_VARIANT
  canonical_edge_type: HAS_RECONCILIATION_VARIANT
  source_card_id: reconciliation_profile.limeroad.waterfall_mrp_nsp_settled
  target_card_id: reconciliation_variant.limeroad.null_entry_type_rows
  source_type: reconciliation_profile
  target_type: reconciliation_variant
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.893e212f01
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.total_forward_gmv
  target_card_id: metric.marketplace.gross_gmv
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.811b283c7c
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.total_forward_gmv
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.91ce00eaac
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.return_rate
  target_card_id: metric.marketplace.return_rate
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.2f4f89c9c6
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.return_rate
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.4e2a82c12e
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.aov
  target_card_id: metric.marketplace.average_order_value
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.60fa0cd63b
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.aov
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.781c5468f9
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.net_settlement_after_returns
  target_card_id: metric.marketplace.net_settled_revenue
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.a2b9156afe
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.net_settlement_after_returns
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.1f867b0e86
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.monthly_oms_performance
  target_card_id: metric.marketplace.gross_gmv
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.c76543cc40
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.monthly_oms_performance
  target_card_id: table.zs_observe.limeroad_oms
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.bc9912eee2
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.brand_payout_efficiency
  target_card_id: metric.marketplace.brand_payout_efficiency
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.c66dc9885b
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.brand_payout_efficiency
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.ad6da2e6ae
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.oms_settlement_reconciliation
  target_card_id: metric.marketplace.gross_gmv
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.722946ce65
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.oms_settlement_reconciliation
  target_card_id: table.zs_observe.limeroad_oms
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.75181e1083
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.oms_settlement_reconciliation
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.8c41b85b54
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.nsp_waterfall
  target_card_id: metric.marketplace.seller_realization_rate
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.89aef65a53
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.nsp_waterfall
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.41525b822e
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.tcs_visibility
  target_card_id: metric.marketplace.tcs_deducted
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.d50151068e
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.tcs_visibility
  target_card_id: table.zs_observe.limeroad_oms
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.1c424527b7
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.reverse_entry_audit
  target_card_id: metric.marketplace.return_reversal_amount
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.6e1e41eced
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.reverse_entry_audit
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.7e430925a0
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.reverse_entry_audit
  target_card_id: table.zs_observe.limeroad_oms
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.b70f3edcc8
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.payout_by_settlement_date
  target_card_id: metric.marketplace.net_settled_revenue
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.f5687ddcc1
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.payout_by_settlement_date
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.8404971574
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.financial_waterfall_full
  target_card_id: metric.marketplace.net_settled_revenue
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.eba36a2d7c
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.financial_waterfall_full
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.23a666930c
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.commission_validation
  target_card_id: metric.marketplace.effective_commission_rate
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.b6a44f4eae
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.commission_validation
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.db62b6c458
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.return_rate_by_brand
  target_card_id: metric.marketplace.return_rate
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.118276bb7d
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.return_rate_by_brand
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.910d0ca121
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.category_performance
  target_card_id: metric.marketplace.gross_gmv
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.9d69dcd604
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.category_performance
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.8db864afce
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.gst_split
  target_card_id: metric.marketplace.tcs_deducted
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.5c72e54115
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.gst_split
  target_card_id: table.zs_observe.limeroad_oms
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.0a9bfb8e68
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.brand_hsn_performance
  target_card_id: metric.marketplace.gross_gmv
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.79d7ecda5d
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.brand_hsn_performance
  target_card_id: table.zs_observe.limeroad_oms
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.supports_metric.e8b5e83790
  edge_type: SUPPORTS_METRIC
  canonical_edge_type: SUPPORTS_METRIC
  source_card_id: query_pattern.limeroad.tcs_tds_summary
  target_card_id: metric.marketplace.tcs_deducted
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.uses_table.9ec97d5a2e
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.limeroad.tcs_tds_summary
  target_card_id: table.zs_observe.limeroad_oms
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.8e5e6cbe57
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.active_scope_filter
  target_card_id: table.zs_observe.limeroad_oms
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.d7f4336a53
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.active_scope_filter
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.9b73f29db2
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.forward_revenue_filter
  target_card_id: metric.marketplace.gross_gmv
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.19f488911e
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.settlement_delivered_sales_filter
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.d6759092f0
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.returns_filter
  target_card_id: metric.marketplace.return_rate
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.b90132b7b0
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.returns_filter
  target_card_id: metric.marketplace.rto_rate
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.e607fa7507
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.vendor_nsp_required
  target_card_id: metric.marketplace.effective_commission_rate
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.b0be89caf2
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.vendor_nsp_required
  target_card_id: metric.marketplace.seller_realization_rate
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.0442c2747e
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.sale_return_amount_commission_base
  target_card_id: metric.marketplace.effective_commission_rate
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.4f2b8067c2
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.sale_return_amount_commission_base
  target_card_id: metric.marketplace.gross_gmv
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.d089e6094f
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.settlement_date_cashflow
  target_card_id: metric.marketplace.net_settled_revenue
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.fe4397aec7
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.tcs_tds_oms_only
  target_card_id: metric.marketplace.tcs_deducted
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.f8ec9d160d
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.tcs_tds_oms_only
  target_card_id: metric.marketplace.tds_deducted
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.2697e8fb20
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.tax_rate_normalization
  target_card_id: table.zs_observe.limeroad_oms
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.7f7c57fe92
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.source_state_case_normalization
  target_card_id: table.zs_observe.limeroad_oms
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.74f86183ee
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.primary_duplicate_fields
  target_card_id: table.zs_observe.limeroad_oms
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.54726c9439
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.null_entry_type_include_totals
  target_card_id: table.zs_observe.limeroad_settlement
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.1b065108db
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.no_segment_only_process_variants
  target_card_id: platform_context.limeroad.in
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.18221a8fa6
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.scope_identifiers_not_account_cards
  target_card_id: platform_context.limeroad.in
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.978ef10b0b
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.benchmark_guidance_only
  target_card_id: metric.marketplace.effective_commission_rate
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.dc18f338ae
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.benchmark_guidance_only
  target_card_id: metric.marketplace.return_rate
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.98df667c09
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.benchmark_guidance_only
  target_card_id: metric.marketplace.rto_rate
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.applies_to.cb114cb501
  edge_type: APPLIES_TO
  canonical_edge_type: APPLIES_TO
  source_card_id: rule.limeroad.benchmark_guidance_only
  target_card_id: metric.marketplace.average_order_value
  source_type: rule
  target_type: null
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_output_contract.079e75dd3e
  edge_type: HAS_OUTPUT_CONTRACT
  canonical_edge_type: HAS_OUTPUT_CONTRACT
  source_card_id: query_pattern.limeroad.oms_settlement_reconciliation
  target_card_id: output_contract.limeroad.oms_settlement_reconciliation
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_output_contract.c4e458cc32
  edge_type: HAS_OUTPUT_CONTRACT
  canonical_edge_type: HAS_OUTPUT_CONTRACT
  source_card_id: query_pattern.limeroad.financial_waterfall_full
  target_card_id: output_contract.limeroad.financial_waterfall
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_output_contract.e4d799f8f1
  edge_type: HAS_OUTPUT_CONTRACT
  canonical_edge_type: HAS_OUTPUT_CONTRACT
  source_card_id: query_pattern.limeroad.return_rate
  target_card_id: output_contract.limeroad.return_rate
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_output_contract.e7955cc3c0
  edge_type: HAS_OUTPUT_CONTRACT
  canonical_edge_type: HAS_OUTPUT_CONTRACT
  source_card_id: query_pattern.limeroad.tcs_tds_summary
  target_card_id: output_contract.limeroad.tcs_tds_summary
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_output_contract.1a73884ec2
  edge_type: HAS_OUTPUT_CONTRACT
  canonical_edge_type: HAS_OUTPUT_CONTRACT
  source_card_id: query_pattern.limeroad.category_performance
  target_card_id: output_contract.limeroad.category_performance
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.4fb1185350
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.gross_gmv
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.bdfb6f9b77
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.vendor_nsp_total
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.7f7eea2963
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.net_settled_revenue
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.04bf30b53e
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.seller_realization_rate
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.2d59fcb1ec
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.effective_commission_rate
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.ae7b75f124
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.return_rate
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.295fa02685
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.rto_rate
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.87d96eb2e9
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.cancellation_rate
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.fdbb57c70a
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.average_order_value
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.a0926effcf
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.brand_payout_efficiency
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.96c7bc4a5c
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.tcs_deducted
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.415f2aef55
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.tds_deducted
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.11623441ee
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.limeroad_discount_absorption
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_metric.63ef88a800
  edge_type: HAS_METRIC
  canonical_edge_type: HAS_METRIC
  source_card_id: platform_context.limeroad.in
  target_card_id: metric.marketplace.return_reversal_amount
  source_type: platform_context
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_formula_template.badf91f162
  edge_type: HAS_FORMULA_TEMPLATE
  canonical_edge_type: HAS_FORMULA_TEMPLATE
  source_card_id: platform_context.limeroad.in
  target_card_id: formula_template.limeroad.nsp_payout
  source_type: platform_context
  target_type: formula_template
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_formula_template.7710967af5
  edge_type: HAS_FORMULA_TEMPLATE
  canonical_edge_type: HAS_FORMULA_TEMPLATE
  source_card_id: platform_context.limeroad.in
  target_card_id: formula_template.limeroad.gross_commission
  source_type: platform_context
  target_type: formula_template
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_formula_template.685c70244a
  edge_type: HAS_FORMULA_TEMPLATE
  canonical_edge_type: HAS_FORMULA_TEMPLATE
  source_card_id: platform_context.limeroad.in
  target_card_id: formula_template.limeroad.return_rate
  source_type: platform_context
  target_type: formula_template
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_formula_template.fbfe51bda4
  edge_type: HAS_FORMULA_TEMPLATE
  canonical_edge_type: HAS_FORMULA_TEMPLATE
  source_card_id: platform_context.limeroad.in
  target_card_id: formula_template.limeroad.net_settlement
  source_type: platform_context
  target_type: formula_template
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_formula_template.8b6f36f0ec
  edge_type: HAS_FORMULA_TEMPLATE
  canonical_edge_type: HAS_FORMULA_TEMPLATE
  source_card_id: platform_context.limeroad.in
  target_card_id: formula_template.limeroad.tax_component_summary
  source_type: platform_context
  target_type: formula_template
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_formula_template.3db18f144c
  edge_type: HAS_FORMULA_TEMPLATE
  canonical_edge_type: HAS_FORMULA_TEMPLATE
  source_card_id: platform_context.limeroad.in
  target_card_id: formula_template.limeroad.tax_rate_normalization
  source_type: platform_context
  target_type: formula_template
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.d72b907d32
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.active_scope_filter
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.e7e6d1ed33
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.forward_revenue_filter
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.6c21eba7f9
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.settlement_delivered_sales_filter
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.bce06a03d6
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.returns_filter
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.a682a6fcde
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.vendor_nsp_required
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.f51308ddd2
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.sale_return_amount_commission_base
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.779c05ff47
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.settlement_date_cashflow
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.57e11fb438
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.tcs_tds_oms_only
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.5c9e00f9be
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.tax_rate_normalization
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.753be85c59
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.source_state_case_normalization
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.f6dd6719cc
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.primary_duplicate_fields
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.3ca77e6b75
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.null_entry_type_include_totals
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.c591b6ee81
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.no_segment_only_process_variants
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.73f8e15418
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.scope_identifiers_not_account_cards
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_rule.9aebb06ce3
  edge_type: HAS_RULE
  canonical_edge_type: HAS_RULE
  source_card_id: platform_context.limeroad.in
  target_card_id: rule.limeroad.benchmark_guidance_only
  source_type: platform_context
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.77e0c6540e
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.no_process_variant_cards
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.1455121bbf
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.sql_refs_resolve
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.3155a67d86
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.edge_refs_resolve
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.1ddea609fe
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.active_filters_present
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.dbe97fc0c6
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.nsp_formula_validation
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.909b4cf983
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.oms_settlement_tolerance
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.9981625add
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.null_entry_type_totals
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.6f8a367894
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.scope_no_account_cards
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.1148ef8c0f
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.tax_rate_normalization
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_validation_test.363d27e5a9
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_card_id: platform_context.limeroad.in
  target_card_id: validation_test.limeroad.reverse_eventtype_not_required
  source_type: platform_context
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.90452d5e31
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.total_forward_gmv
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.1958218415
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.return_rate
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.a5bf16a03e
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.aov
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.93e796ea26
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.net_settlement_after_returns
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.626bc493e7
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.monthly_oms_performance
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.f23cf65163
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.brand_payout_efficiency
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.158984ad3b
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.oms_settlement_reconciliation
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.d3a5335f9b
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.nsp_waterfall
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.a3bc52c5b3
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.tcs_visibility
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.6c2f14cc56
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.reverse_entry_audit
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.eda6bfef08
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.payout_by_settlement_date
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.511cb39cd3
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.financial_waterfall_full
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.a838d4fbed
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.commission_validation
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.43611934d5
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.return_rate_by_brand
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.0cecdff505
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.category_performance
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.33235202fd
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.gst_split
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.ad19b4d395
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.brand_hsn_performance
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

```yaml
candidate_edge:
  edge_id: edge.limeroad.has_query_pattern.def1c1d3c5
  edge_type: HAS_QUERY_PATTERN
  canonical_edge_type: HAS_QUERY_PATTERN
  source_card_id: platform_context.limeroad.in
  target_card_id: query_pattern.limeroad.tcs_tds_summary
  source_type: platform_context
  target_type: query_pattern
  inverse_edge_type: null
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  legacy_edge_aliases: []
  edge_properties: {}
```

## 5. SQL Pattern Registry

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.forward_gmv
  description: Total forward GMV and commission/payout from settlement ITEM_SALE rows
  sql_template: |-
    SELECT
      SUM(charged_amount) AS gross_gmv,
      SUM(vendor_nsp) AS total_nsp,
      SUM(gross_commission) AS lr_commission,
      SUM(settled_amount) AS net_seller_revenue,
      ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(vendor_nsp), 0), 2) AS effective_commission_pct
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22
      AND entry_type = 'ITEM_SALE';
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.return_rate
  description: Return, RTO, and cancellation rates from settlement entry_type counts
  sql_template: |-
    SELECT
      ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_RETURN') / NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS return_rate_pct,
      ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_RTO') / NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS rto_rate_pct,
      ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_CANCEL') / NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS cancel_rate_pct
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22;
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.aov
  description: Average order/item value for settled ITEM_SALE rows
  sql_template: |-
    SELECT AVG(charged_amount) AS aov
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22
      AND entry_type = 'ITEM_SALE';
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.net_after_returns
  description: Net settled revenue after return/RTO/cancel deductions
  sql_template: |-
    SELECT
      SUM(CASE WHEN entry_type = 'ITEM_SALE' THEN settled_amount ELSE 0 END) AS forward_payout,
      SUM(CASE WHEN entry_type IN ('ITEM_RETURN','ITEM_RTO','ITEM_CANCEL') THEN settled_amount ELSE 0 END) AS reverse_deductions,
      SUM(settled_amount) AS net_revenue
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22;
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.oms.monthly_performance
  description: Monthly OMS performance by transaction_type with TCS/TDS
  sql_template: |-
    SELECT
      DATE_TRUNC('month', created_date) AS month,
      transaction_type,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      SUM(tcs_igst_amount + tcs_cgst_amount + tcs_sgst_amount) AS tcs,
      SUM(total_tds) AS tds
    FROM zs_observe.limeroad_oms
    WHERE is_active = true
      AND group_level_id = 22
    GROUP BY 1, 2
    ORDER BY 1, 2;
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  - ev.limeroad.oms.queries.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.brand_payout_efficiency
  description: Brand-level payout efficiency from settlement rows
  sql_template: |-
    SELECT
      brand,
      AVG(mrp) AS avg_mrp,
      AVG(charged_amount) AS avg_charged,
      AVG(vendor_nsp) AS avg_nsp,
      AVG(settled_amount) AS avg_payout,
      ROUND(100.0 * AVG(settled_amount) / NULLIF(AVG(charged_amount), 0), 2) AS payout_as_pct_charged
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22
      AND entry_type = 'ITEM_SALE'
    GROUP BY brand;
  evidence_refs:
  - ev.limeroad.metrics.sql.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.recon.oms_settlement_invoice_item
  description: OMS to settlement reconciliation using invoice_number + item_id and
    price variance
  sql_template: |-
    SELECT
      o.invoice_number,
      o.order_id,
      o.item_id,
      o.charged_amount AS oms_invoice_value,
      o.total_tax AS oms_tax,
      s.charged_amount AS stl_charged,
      s.vendor_nsp,
      s.settled_amount,
      s.entry_type,
      ABS(o.charged_amount - s.charged_amount) AS price_variance,
      CASE
        WHEN s.item_id IS NULL THEN 'Not in Settlement'
        WHEN ABS(o.charged_amount - s.charged_amount) > 1 THEN 'Price Variance'
        ELSE 'Matched'
      END AS recon_status
    FROM zs_observe.limeroad_oms o
    LEFT JOIN zs_observe.limeroad_settlement s
      ON o.invoice_number = s.invoice_number
     AND o.item_id = s.item_id
     AND s.is_active = true
    WHERE o.is_active = true
      AND o.group_level_id = 22
      AND o.transaction_type = 'forward';
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.recon.nsp_waterfall
  description: MRP to NSP to settlement waterfall by brand
  sql_template: |-
    SELECT
      brand,
      SUM(mrp) AS total_mrp,
      SUM(total_vendor_discount) AS vendor_markdown,
      SUM(vendor_nsp) AS total_nsp,
      SUM(charged_amount) AS total_charged_to_buyer,
      SUM(total_limeroad_discount) AS lr_additional_discount,
      SUM(gross_commission) AS lr_commission,
      SUM(settled_amount) AS net_payout,
      ROUND(100.0 * SUM(settled_amount) / NULLIF(SUM(vendor_nsp), 0), 2) AS payout_pct_of_nsp
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22
      AND entry_type = 'ITEM_SALE'
    GROUP BY brand;
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.oms.tcs_visibility
  description: TCS visible in OMS only; do not expect settlement TCS fields
  sql_template: |-
    SELECT
      'OMS TCS' AS source,
      SUM(tcs_igst_amount + tcs_cgst_amount + tcs_sgst_amount) AS total_tcs
    FROM zs_observe.limeroad_oms
    WHERE is_active = true
      AND group_level_id = 22
      AND transaction_type = 'forward';
  evidence_refs:
  - ev.limeroad.recon.sql.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.recon.reverse_entries_audit
  description: Return/RTO/cancel reverse entries audit
  sql_template: |-
    SELECT
      s.order_id,
      s.entry_type,
      s.order_status,
      s.charged_amount AS return_value,
      s.vendor_nsp,
      s.settled_amount AS reversal_amount,
      o.charged_amount AS original_oms_value
    FROM zs_observe.limeroad_settlement s
    LEFT JOIN zs_observe.limeroad_oms o
      ON s.invoice_number = o.invoice_number
     AND s.item_id = o.item_id
     AND o.is_active = true
    WHERE s.is_active = true
      AND s.group_level_id = 22
      AND s.entry_type IN ('ITEM_RETURN', 'ITEM_RTO', 'ITEM_CANCEL');
  evidence_refs:
  - ev.limeroad.recon.sql.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.payout_by_date
  description: Payout summary by settlement_date
  sql_template: |-
    SELECT
      settlement_date,
      COUNT(*) AS line_items,
      SUM(CASE WHEN entry_type='ITEM_SALE' THEN settled_amount ELSE 0 END) AS sales_settled,
      SUM(CASE WHEN entry_type IN ('ITEM_RETURN','ITEM_RTO') THEN settled_amount ELSE 0 END) AS returns_settled,
      SUM(CASE WHEN entry_type='ITEM_CANCEL' THEN settled_amount ELSE 0 END) AS cancels_settled,
      SUM(settled_amount) AS net_payout
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22
    GROUP BY settlement_date
    ORDER BY settlement_date;
  evidence_refs:
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.financial_waterfall_full
  description: Full settlement financial waterfall
  sql_template: |-
    SELECT
      SUM(CASE WHEN entry_type='ITEM_SALE' THEN mrp ELSE 0 END) AS total_mrp,
      SUM(CASE WHEN entry_type='ITEM_SALE' THEN charged_amount ELSE 0 END) AS gross_gmv,
      SUM(CASE WHEN entry_type='ITEM_SALE' THEN total_vendor_discount ELSE 0 END) AS vendor_discount,
      SUM(CASE WHEN entry_type='ITEM_SALE' THEN vendor_nsp ELSE 0 END) AS total_vendor_nsp,
      SUM(CASE WHEN entry_type='ITEM_SALE' THEN gross_commission ELSE 0 END) AS lr_commission,
      SUM(CASE WHEN entry_type='ITEM_SALE' THEN settled_amount ELSE 0 END) AS forward_settled,
      SUM(CASE WHEN entry_type IN ('ITEM_RETURN','ITEM_RTO','ITEM_CANCEL') THEN settled_amount ELSE 0 END) AS reverse_settled,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22;
  evidence_refs:
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.commission_validation
  description: Validate settled_amount from vendor_nsp and commission rate
  sql_template: |-
    SELECT
      order_id,
      vendor_nsp,
      settled_amount,
      ROUND(vendor_nsp * (1 - gross_commission_perc / 100), 2) AS expected_settled,
      ABS(settled_amount - ROUND(vendor_nsp * (1 - gross_commission_perc / 100), 2)) AS variance
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22
      AND entry_type = 'ITEM_SALE'
      AND vendor_nsp > 0
    ORDER BY variance DESC
    LIMIT 20;
  evidence_refs:
  - ev.limeroad.settlement.nsp_formula.001
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.return_rate_by_brand
  description: Return/RTO/cancel rate by brand
  sql_template: |-
    SELECT
      brand,
      COUNT_IF(entry_type = 'ITEM_SALE') AS sales,
      COUNT_IF(entry_type = 'ITEM_RETURN') AS buyer_returns,
      COUNT_IF(entry_type = 'ITEM_RTO') AS rto,
      COUNT_IF(entry_type = 'ITEM_CANCEL') AS cancels,
      ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_RETURN') / NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS return_rate_pct,
      ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_RTO') / NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS rto_rate_pct
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22
    GROUP BY brand;
  evidence_refs:
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.settlement.category_performance
  description: Category-level settlement performance
  sql_template: |-
    SELECT
      classification,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      SUM(vendor_nsp) AS total_nsp,
      SUM(settled_amount) AS seller_payout,
      SUM(gross_commission) AS lr_commission,
      AVG(gross_commission_perc) AS commission_rate
    FROM zs_observe.limeroad_settlement
    WHERE is_active = true
      AND group_level_id = 22
      AND entry_type = 'ITEM_SALE'
    GROUP BY classification
    ORDER BY gmv DESC;
  evidence_refs:
  - ev.limeroad.settlement.queries.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.oms.gst_split
  description: Interstate vs intrastate GST split
  sql_template: |-
    SELECT
      salestype,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      SUM(tax_igst_amount) AS igst,
      SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
    FROM zs_observe.limeroad_oms
    WHERE is_active = true
      AND group_level_id = 22
      AND transaction_type = 'forward'
    GROUP BY salestype;
  evidence_refs:
  - ev.limeroad.oms.queries.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.oms.brand_hsn_performance
  description: OMS brand and HSN performance
  sql_template: |-
    SELECT
      brand,
      hsn,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS avg_price,
      SUM(total_tax) AS gst_collected
    FROM zs_observe.limeroad_oms
    WHERE is_active = true
      AND group_level_id = 22
      AND transaction_type = 'forward'
    GROUP BY brand, hsn
    ORDER BY gmv DESC;
  evidence_refs:
  - ev.limeroad.oms.queries.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.oms.tcs_tds_summary
  description: TCS and TDS monthly summary from OMS
  sql_template: |-
    SELECT
      DATE_TRUNC('month', created_date) AS month,
      SUM(tcs_igst_amount + tcs_cgst_amount + tcs_sgst_amount) AS total_tcs,
      SUM(total_tds) AS total_tds
    FROM zs_observe.limeroad_oms
    WHERE is_active = true
      AND group_level_id = 22
      AND transaction_type = 'forward'
    GROUP BY 1
    ORDER BY 1;
  evidence_refs:
  - ev.limeroad.oms.queries.001
  - ev.limeroad.tax.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

```yaml
sql_pattern:
  sql_ref: sql.limeroad.validation.tax_rate_normalization
  description: Normalize tax rate fields that may be decimal or percentage
  sql_template: |-
    SELECT
      order_id,
      tax_igst_rate,
      CASE WHEN tax_igst_rate > 1 THEN tax_igst_rate / 100 ELSE tax_igst_rate END AS normalized_igst_rate
    FROM zs_observe.limeroad_oms
    WHERE is_active = true
      AND group_level_id = 22;
  evidence_refs:
  - ev.limeroad.quality.001
  - ev.limeroad.oms.quality.001
  confidence: high
  review_status: accepted
  marketplace_only: true
```

## 6. Review Item Registry

```yaml
review_item:
  review_id: review.limeroad.group_scope_external
  review_type: external_runtime_scope_binding
  related_card_type: platform_context
  related_canonical_id: platform_context.limeroad.in
  issue: The DOCX documents group_level_id = 22 for LimeRoad/Mensa data, but user-specific
    runtime account/scope selection remains external to the marketplace canonical
    layer.
  required_resolution: Keep documented_scope_values in table/column/platform_context
    cards; do not create account-binding cards. Runtime must supply/confirm scope
    when necessary.
  severity: medium
  evidence_refs:
  - ev.limeroad.scope.001
  status: open
```

```yaml
review_item:
  review_id: review.limeroad.future_commission_model_variation
  review_type: future_rate_card_variation
  related_card_type: metric
  related_canonical_id: metric.marketplace.effective_commission_rate
  issue: Current data shows flat 41.3% commission on vendor_nsp for Anubhutee and
    Ishin, but the DOCX says LimeRoad supports multiple commission models and warns
    to validate if new categories are added.
  required_resolution: Use 41.3% as source-backed current-context guidance only. If
    new categories/brands/rate cards are ingested, verify commission rate before hard
    validation.
  severity: low
  evidence_refs:
  - ev.limeroad.overview.001
  - ev.limeroad.quality.001
  status: open
```

```yaml
review_item:
  review_id: review.limeroad.reconciliation_tolerance_resolved
  review_type: resolved_source_tolerance
  related_card_type: reconciliation_profile
  related_canonical_id: reconciliation_profile.limeroad.oms_settlement_invoice_item
  issue: OMS-settlement amount tolerance is explicitly encoded in source SQL as ABS(o.charged_amount
    - s.charged_amount) > 1 for Price Variance.
  required_resolution: No open review required for this source-backed reconciliation
    threshold; preserve >1 tolerance unless runtime overrides it.
  severity: low
  evidence_refs:
  - ev.limeroad.recon.sql.001
  status: resolved
```

## 7. Parser Quality Manifest

```yaml
parser_quality_manifest:
  candidate_cards: 314
  candidate_edges: 392
  source_evidence_count: 23
  source_tables: 2
  sql_patterns: 19
  missing_edge_references: 0
  missing_edge_reference_details: []
  dangling_sql_refs: 0
  dangling_sql_ref_details: []
  open_reviews: 2
  lazy_workflow_steps: 0
  lazy_workflow_step_details: []
  placeholder_metric_formulas: 0
  placeholder_metric_formula_details: []
  unsupported_metric_implementations: 0
  process_variant_cards: 0
  process_variants_review_required: 0
  hard_threshold_benchmarks_without_rule: 0
  forbidden_scope_cards_from_scope_ids: 0
  card_type_counts:
    platform: 1
    platform_context: 1
    domain: 10
    table: 2
    column: 144
    relationship: 2
    value_profile: 15
    metric: 14
    formula_template: 6
    metric_implementation: 14
    metric_dependency: 4
    business_process: 5
    workflow_step: 12
    state_transition: 5
    reconciliation_profile: 5
    reconciliation_side: 7
    reconciliation_unit: 4
    matching_logic: 5
    mismatch_category: 7
    reconciliation_variant: 3
    query_pattern: 18
    rule: 15
    validation_test: 10
    output_contract: 5
```

## 8. Full Source Capture Appendix — Normalized DOCX Text

The appendix preserves the source DOCX text used for this refactor. Code fences are normalized to tildes so the markdown remains parse-safe.

```text

Tab 1
# LimeRoad — Business Knowledge Base
## 1. LimeRoad Marketplace Overview
### 1.1 Background
LimeRoad is an Indian online social shopping marketplace focused on women's fashion, lifestyle, and apparel. It was founded in 2012 by Suchi Mukherjee, Prashant Malik, and Ankush Mehra under the legal entity A.M. Marketplaces Pvt. Ltd. The platform pioneered a social commerce model — enabling users to create and share "looks" (styled outfits) and earn affiliate commissions for sales generated from their posts.
**Key corporate fact:** LimeRoad was **acquired by V-Mart Retail Limited** — confirmed in the dataset by `e_commercename = "V MART RETAIL LIMITED"` and `e_commercegstin = "06AABCV7206K1Z9"` in the OMS table. V-Mart is a value-format retail chain in India. The LimeRoad seller portal now operates via `seller.trunkroute.com`.
**Scale:**
* ₹3,270 Cr annual revenue (FY2025)
* Raised $51.9M in total funding (Tiger Global, Lightspeed India, Z47)
* Focus: women's fashion — ethnic wear, western wear, accessories, home décor
### 1.2 Brands in Dataset
| Brand | group_level_id | Category | Price Range | SKUs |
|-------|----------------|----------|-------------|------|
| Anubhutee | 22             | Ethnic kurta sets, kurtis, nightwear | ₹750–₹1,200 | 197+ |
| Ishin | 22             | Premium ethnic sets, dresses, sarees | ₹900–₹1,800 | 152+ |
| High Star | 22             | Accessories (limited) | —           | few  |
### 1.3 Seller Registration and Commission Models
LimeRoad offers multiple commission models; sellers choose during registration. LimeRoad deducts commissions based on product categories, promotional participation, and order value. Additional charges may include shipping fees, discounts, and penalty charges.
**Observed in data:** A flat **41.3% commission on Vendor NSP** for all Anubhutee and Ishin rows — this is the agreed rate for Mensa's brands in the ethnic wear category.
### 1.4 Multi-GSTIN Warehouses
Mensa operates 4 LimeRoad dispatch warehouses:
| GSTIN | State | Vendor State (lowercase in OMS) |
|-------|-------|---------------------------------|
| `29AAOCM5326J1ZY` | Karnataka | `karnataka`                     |
| `27AAOCM5326J1Z2` | Maharashtra | `maharashtra`                   |
| `19AAOCM5326J1ZZ` | West Bengal | `west bengal`                   |
| `06AAOCM5326J1Z6` | Haryana | `haryana`                       |
---
## 2. LimeRoad Business Model
### 2.1 Revenue Sources
LimeRoad (V-Mart) earns from sellers through:
| Revenue Type | Mechanism |
|--------------|-----------|
| **Gross Commission** | 41.3% of vendor_nsp on every sale |
| **LimeRoad Discount Absorption** | When LR prices below vendor_nsp, LR absorbs (visible in `total_limeroad_discount < 0`) |
| **COD Collection Charges** | ₹36–₹100 charged to buyers for cash collection; retained by LimeRoad (not passed to seller) |
| **Shipping Charges** | Seller-borne logistics recovered via `transporter_cost_recovered_from_vendor` |
| **Promotional participation** | Sellers fund discounts via `total_vendor_discount` (MRP markdown) |
### 2.2 NSP (Net Selling Price) Model — Deep Explanation
LimeRoad's settlement is based on a **Vendor NSP model** — unique among Indian marketplaces:
~~~
MRP (Maximum Retail Price)
− Vendor Discount  →  Vendor NSP (transfer price: seller's floor)
− LimeRoad Margin (41.3% of NSP)  →  Seller Payout
~~~
**What this means for sellers:**
* The seller agrees a `vendor_nsp` (e.g., ₹1,029) with LimeRoad
* LimeRoad can sell above or below this price to the buyer
* The seller always receives `vendor_nsp × 58.7%` regardless of buyer price
* LimeRoad absorbs the risk of promotional pricing — if they discount to ₹909, they still pay the seller ₹604
* If LimeRoad charges ₹1,145, they keep the extra margin (₹504.98 vs ₹304.98)
**This is different from Amazon/Snapdeal/Meesho** where commission is a % of the actual buyer price.
### 2.3 Fulfilment Model
LimeRoad operates a **dropship / self-fulfilment model**:
* Sellers dispatch directly from their own warehouses
* LimeRoad manages the courier empanelment (10 courier partners)
* Sellers generate GST invoices in their own name (hence 4 seller GSTINs in OMS)
* LimeRoad acts as the e-commerce operator for TCS/TDS purposes
---
## 3. Transaction Lifecycle
### 3.1 Forward Sale Flow
~~~
Customer places order on LimeRoad app/website
↓
Order created → appears in limeroad_oms
(transaction_type='forward', eventtype='sale')
(invoice generated by seller's GSTIN)
↓
Seller dispatches from nearest warehouse
(courier assigned from LimeRoad panel)
↓
Product delivered to buyer
↓
Settlement cycle runs
→ limeroad_settlement
(entry_type='ITEM_SALE', order_status='ORDER_DELIVERED')
(settled_amount = vendor_nsp × 0.587)
↓
Net payout transferred to seller bank account
~~~
### 3.2 Return (ITEM_RETURN) Flow
~~~
Buyer initiates return after delivery
↓
Return courier picks up from buyer
↓
Item received back at seller warehouse
↓
limeroad_settlement: entry_type='ITEM_RETURN', order_status='ORDER_DELIVERED'
(transaction_type='reverse')
(settled_amount = negative ← deducted from seller)
(gross_commission reversed — LimeRoad credits back 41.3% of NSP)
↓
limeroad_oms: transaction_type='reverse', eventtype='return'
(credit note / return invoice generated)
~~~
### 3.3 RTO (Return-to-Origin) Flow
~~~
Courier attempts delivery but fails
(buyer unavailable, wrong address, refused)
↓
limeroad_settlement: entry_type='ITEM_RTO', order_status='RETURNED_TO_ORIGIN'
(settled_amount = negative)
↓
limeroad_oms: transaction_type='reverse'
(credit note for the failed shipment)
~~~
### 3.4 Cancellation Flow
~~~
Order cancelled (before or after shipment)
↓
limeroad_settlement: entry_type='ITEM_CANCEL', order_status='ORDER_CANCELLED'
(settled_amount = negative ← reversal of initial settlement credit)
(forward ITEM_SALE entry + reverse ITEM_CANCEL entry both present for same order)
~~~
---
## 4. Entity Relationships
### 4.1 Join Map
~~~
limeroad_oms
invoice_number  ←──────────────→  invoice_number  limeroad_settlement
item_id         ←──────────────→  item_id         limeroad_settlement
order_id        ←──────────────→  order_id        limeroad_settlement
~~~
### 4.2 Primary Join Keys
| Join | Left Table | Right Table | Key | Coverage |
|------|------------|-------------|-----|----------|
| OMS → Settlement | limeroad_oms | limeroad_settlement | `invoice_number` + `item_id` | 1,520/1,540 = **98.7%** |
| OMS → Settlement | limeroad_oms | limeroad_settlement | `order_id` | 1,520/1,540 = **98.7%** |
> **98.7% match rate** on both order_id and invoice_number — excellent coverage. The 1.3% gap (20 orders) represents orders in settlement without OMS entries (typically adjustment entries) or OMS entries pending settlement.
### 4.3 Settlement Has More Orders Than OMS
| Table | Distinct Orders |
|-------|-----------------|
| limeroad_oms | 1,540           |
| limeroad_settlement | 1,664           |
The settlement table has 124 additional orders — these represent:
* Orders from before Jan 2025 (settlement date range starts May 2024; OMS starts Jan 2025)
* Adjustment entries without corresponding OMS invoices
---
## 5. GST / Tax Framework
### 5.1 Product GST
| Condition | Tax Type | Rate Range |
|-----------|----------|------------|
| Source state ≠ Destination state | IGST     | 5%, 12%, 18% |
| Source state = Destination state | CGST + SGST | 2.5% + 2.5%, 6% + 6% |
**Observed rates by HSN:**
| HSN | Product | IGST Rate |
|-----|---------|-----------|
| 62063000 / 62064000 | Women's blouses/shirts | 5%        |
| 62114290 / 62114990 | Other garments | 5% or 12% |
| 62044390 | Women's dresses | 12%       |
| 62069000 | Other women's garments | 12%       |
| 71179010 | Fashion jewellery | 3%        |
| 998599 | SAC code — marketplace services | 18%       |
### 5.2 TCS (Tax Collected at Source — GST §52)
* **Collector:** V MART RETAIL LIMITED (LimeRoad operator, GSTIN: `06AABCV7206K1Z9`)
* **Rate:** \~0.5% of `charged_amount_excluding_tax` per order
* **Split:** IGST for inter-state; CGST+SGST for intra-state
* **In OMS:** `tcs_igst_amount`, `tcs_cgst_amount`, `tcs_sgst_amount`
* **Total TCS collected (2025):** ₹12,869.96
* **Seller recovery:** Via GSTR-2A matching
### 5.3 TDS (Tax Deducted at Source — IT §194-O)
* **Collector:** V MART RETAIL LIMITED
* **Rate:** \~1% of `charged_amount_excluding_tax` (2× TCS rate)
* **In OMS:** `total_tds` / `tdsamount`
* **Total TDS collected (2025):** ₹20,648.13
* **Seller recovery:** Via Form 26AS (annual IT return)
### 5.4 TCS vs TDS Rates Observed
| Metric | OMS Field | Total (2025) | Approx Rate |
|--------|-----------|--------------|-------------|
| TCS    | `tcs_igst_amount + tcs_cgst_amount + tcs_sgst_amount` | ₹12,870      | \~0.5%      |
| TDS    | `total_tds` | ₹20,648      | \~1.0%      |
---
## 6. Key Business Metrics (with SQL)
### 6.1 Total Forward GMV
~~~sql
SELECT
SUM(charged_amount) AS gross_gmv,
SUM(vendor_nsp) AS total_nsp,
SUM(gross_commission) AS lr_commission,
SUM(settled_amount) AS net_seller_revenue,
ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(vendor_nsp), 0), 2) AS effective_commission_pct
FROM zs_observe.limeroad_settlement
WHERE is_active = true AND entry_type = 'ITEM_SALE';
-- Observed: GMV ₹16L | NSP ~ | Commission ₹6.5L | Settled ₹9.4L
~~~
### 6.2 Return Rate
~~~sql
SELECT
ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_RETURN')
/ NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS return_rate_pct,
ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_RTO')
/ NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS rto_rate_pct,
ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_CANCEL')
/ NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS cancel_rate_pct
FROM zs_observe.limeroad_settlement
WHERE is_active = true;
-- Observed: Return 18.7% | RTO 18.1% | Cancel 9.2%
~~~
### 6.3 AOV (Average Order Value)
~~~sql
SELECT AVG(charged_amount) AS aov
FROM zs_observe.limeroad_settlement
WHERE is_active = true AND entry_type = 'ITEM_SALE';
-- Observed: ₹970.87
~~~
### 6.4 Net Settled Revenue After Returns
~~~sql
SELECT
SUM(CASE WHEN entry_type = 'ITEM_SALE' THEN settled_amount ELSE 0 END) AS forward_payout,
SUM(CASE WHEN entry_type IN ('ITEM_RETURN','ITEM_RTO','ITEM_CANCEL') THEN settled_amount ELSE 0 END) AS reverse_deductions,
SUM(settled_amount) AS net_revenue
FROM zs_observe.limeroad_settlement
WHERE is_active = true;
~~~
### 6.5 Monthly OMS Performance
~~~sql
SELECT
DATE_TRUNC('month', created_date) AS month,
transaction_type,
COUNT(*) AS orders,
SUM(charged_amount) AS gmv,
SUM(total_tcs_igst + total_tcs_cgst + total_tcs_sgst) AS tcs,
SUM(total_tds) AS tds
FROM zs_observe.limeroad_oms
WHERE is_active = true
GROUP BY 1, 2 ORDER BY 1, 2;
~~~
### 6.6 Brand-Level Payout Efficiency
~~~sql
SELECT
brand,
AVG(mrp) AS avg_mrp,
AVG(charged_amount) AS avg_charged,
AVG(vendor_nsp) AS avg_nsp,
AVG(settled_amount) AS avg_payout,
ROUND(100.0 * AVG(settled_amount) / NULLIF(AVG(charged_amount), 0), 2) AS payout_as_pct_charged
FROM zs_observe.limeroad_settlement
WHERE is_active = true AND entry_type = 'ITEM_SALE'
GROUP BY brand;
~~~
---
## 7. Reconciliation Use Cases
### 7.1 OMS ↔ Settlement Reconciliation (invoice + item match)
~~~sql
SELECT
o.invoice_number, o.order_id, o.item_id,
o.charged_amount AS oms_invoice_value,
o.total_tax AS oms_tax,
s.charged_amount AS stl_charged,
s.vendor_nsp, s.settled_amount,
s.entry_type,
ABS(o.charged_amount - s.charged_amount) AS price_variance,
CASE
WHEN s.item_id IS NULL THEN 'Not in Settlement'
WHEN ABS(o.charged_amount - s.charged_amount) > 1 THEN 'Price Variance'
ELSE 'Matched'
END AS recon_status
FROM zs_observe.limeroad_oms o
LEFT JOIN zs_observe.limeroad_settlement s
ON o.invoice_number = s.invoice_number
AND o.item_id = s.item_id
AND s.is_active = true
WHERE o.is_active = true AND o.transaction_type = 'forward';
~~~
### 7.2 Waterfall: MRP → NSP → Settled → Net
~~~sql
SELECT
brand,
SUM(mrp) AS total_mrp,
SUM(total_vendor_discount) AS vendor_markdown,
SUM(vendor_nsp) AS total_nsp,
SUM(charged_amount) AS total_charged_to_buyer,
SUM(total_limeroad_discount) AS lr_additional_discount,
SUM(gross_commission) AS lr_commission,
SUM(settled_amount) AS net_payout,
ROUND(100.0 * SUM(settled_amount) / NULLIF(SUM(vendor_nsp), 0), 2) AS payout_pct_of_nsp
FROM zs_observe.limeroad_settlement
WHERE is_active = true AND entry_type = 'ITEM_SALE'
GROUP BY brand;
~~~
### 7.3 TCS Reconciliation (OMS vs Settlement)
~~~sql
SELECT
'OMS TCS' AS source,
SUM(tcs_igst_amount + tcs_cgst_amount + tcs_sgst_amount) AS total_tcs
FROM zs_observe.limeroad_oms
WHERE is_active = true AND transaction_type = 'forward'
-- No TCS field in settlement — TCS visible only in OMS
~~~
### 7.4 Return Reverse Entries Audit
~~~sql
SELECT
s.order_id, s.entry_type, s.order_status,
s.charged_amount AS return_value,
s.vendor_nsp, s.settled_amount AS reversal_amount,
o.charged_amount AS original_oms_value
FROM zs_observe.limeroad_settlement s
LEFT JOIN zs_observe.limeroad_oms o
ON s.invoice_number = o.invoice_number
AND s.item_id = o.item_id
AND o.is_active = true
WHERE s.is_active = true
AND s.entry_type IN ('ITEM_RETURN', 'ITEM_RTO', 'ITEM_CANCEL');
~~~
---
## 8. Data Quality Observations & Known Issues
| Issue | Table | Detail | Mitigation |
|-------|-------|--------|------------|
| `tax_igst_rate` dual format | limeroad_oms | Both 0.12 (decimal) and 12.0 (percentage) observed | Normalize: `CASE WHEN tax_igst_rate > 1 THEN tax_igst_rate/100 ELSE tax_igst_rate END` |
| `source_state` lowercase in OMS | limeroad_oms | `karnataka` vs `Karnataka` in settlement | `UPPER(source_state)` for joins |
| `invoicedate` stored as varchar | limeroad_oms | Cannot date-filter natively | `CAST(invoicedate AS TIMESTAMP)` |
| Duplicate field pairs | limeroad_oms | `hsn`/`hsncode`, `item_id`/`uniqueitemid`, etc. | Use primary: `hsn`, `item_id` |
| Settlement starts May 2024 | limeroad_settlement | Covers older orders pre-OMS range | Expected historical data in settlement |
| `sale_return_amount` ≠ `charged_amount` | limeroad_settlement | COD charge deducted for COD orders | Use `sale_return_amount` for commission base; `charged_amount` for GMV |
| 25 OMS rows with NULL brand | limeroad_oms | \~1.6% missing brand | Join settlement on `item_id` or `invoice_number` |
| 26 reverse OMS rows with NULL eventtype | limeroad_oms | Older reverse format | Filter `transaction_type = 'reverse'` captures all |
| `vendor_nsp` not in OMS | limeroad_oms | NSP is only in settlement | Join to settlement for vendor_nsp context |
| NULL entry_type for 14 settlement rows | limeroad_settlement | Old records | Include in totals; not financially significant |
---
## 9. Mandatory Query Filters
~~~sql
-- Both tables
WHERE is_active = true
AND group_level_id = 22
-- OMS: forward sales only
WHERE is_active = true AND transaction_type = 'forward'
-- Settlement: delivered sales only
WHERE is_active = true AND entry_type = 'ITEM_SALE' AND order_status = 'ORDER_DELIVERED'
-- Settlement: returns only
WHERE is_active = true AND entry_type IN ('ITEM_RETURN', 'ITEM_RTO')
~~~
---
## 10. Table Summary Reference
| Table | Purpose | Active Rows | Date Range | Primary Key | Join Key | group_level_id |
|-------|---------|-------------|------------|-------------|----------|----------------|
| `limeroad_oms` | GST invoice / OMS | 2,255       | Jan–Dec 2025 | `invoice_number` + `item_id` | `invoice_number`, `item_id`, `order_id` | 22             |
| `limeroad_settlement` | Financial settlement payout | 2,425       | May 2024–Dec 2025 | `invoice_number` + `item_id` | `invoice_number`, `item_id`, `order_id` | 22             |
Tab 2
# Table : LimeRoad Settlement — Table Knowledge Base
**Schema:** `zs_observe`  **Table:** `limeroad_settlement`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team
## 1. Table Overview
`limeroad_settlement` is the **financial settlement ledger** for LimeRoad. It records the payout calculation for every settled order — capturing the MRP, charged amount, LimeRoad's commission deduction, vendor net settled price (NSP), and the final amount paid to the seller.
**Critical insight — NSP-Based Settlement Model:**\nLimeRoad uses a unique **Vendor NSP (Net Selling Price)** model. The `settled_amount` is derived from `vendor_nsp`, not from `charged_amount`. LimeRoad deducts its commission (41.3%) from the vendor NSP — giving the seller a fixed payout regardless of what discount LimeRoad offers to buyers. This insulates sellers from LimeRoad's promotional pricing.
~~~
settled_amount = vendor_nsp × (1 − 0.413) = vendor_nsp × 0.587
gross_commission = sale_return_amount − settled_amount
~~~
The table also captures full logistics detail — AWB numbers, transporter names, COD charges, and product classification.
---
## 2. Key Statistics
| Metric | Value |
|--------|-------|
| Total rows | 2,425 |
| Active rows (`is_active = true`) | 2,425 (100%) |
| group_level_id | 22    |
| Date range (`created_date`) | 2024-05-12 → 2025-12-06 |
| Settlement date range | 2025-01-01 → 2025-12-23 |
| Distinct orders | 1,664 |
| Distinct SKUs | 357   |
| Total charged (GMV) | ₹16,01,936 (ITEM_SALE rows) |
| Total gross commission | ₹6,54,768 |
| Total settled (net forward) | ₹9,35,252 |
| Total returns settled | −₹3,52,250 (ITEM_RETURN + ITEM_RTO + ITEM_CANCEL) |
| Commission rate | **41.3% flat** (on vendor_nsp) |
| Brands | Anubhutee, Ishin |
| Transporters | 10 courier services |
| Payment modes | COD, PREPAID |
| Currency | INR (100%) |
---
## 3. Schema Details (84 Columns)
### 3.1 Identity Columns
| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `invoice_number` | varchar | GST invoice number — **join key to limeroad_oms** |
| `order_id` | varchar | LimeRoad order ID with sub-order suffix (e.g., `0110673371S2`) |
| `item_id` | varchar | Line item UUID — **join key to limeroad_oms** |
| `unique_item_id` | varchar | Alternate item ID |
| `sku_id` / `style_code` | varchar | Seller style/SKU code |
| `variant_id` | varchar | Product variant ID |
| `ui_product_id` | varchar | UI-facing product ID |
| `awb`  | varchar | **AWB / tracking number** (courier-specific format) |
| `vendor_invoice_number` | decimal | Vendor's own invoice number reference |
| `vendor_margin_approved_id` | varchar | Margin approval reference ID |
### 3.2 Date Columns
| Column | Type | Description |
|--------|------|-------------|
| `created_date` | date | Record creation date |
| `settlement_date` | date | **Date of financial settlement** — payment processing date |
| `cycle_date` | timestamp | Settlement cycle timestamp |
| `order_date` | timestamp | Original order date |
| `invoice_date` | timestamp | Invoice date |
### 3.3 Financial Columns
| Column | Type | Description |
|--------|------|-------------|
| `mrp`  | decimal | Maximum Retail Price |
| `charged_amount` | decimal | **Price paid by customer** |
| `sale_return_amount` | decimal | `charged_amount` minus COD charges — the NSP calculation base |
| `vendor_nsp` | decimal | **Vendor Net Selling Price** — the transfer price agreed between Mensa and LimeRoad. Commission is calculated on this |
| `gross_commission_perc` | decimal | LimeRoad's commission rate — **41.3% flat** for all rows |
| `gross_commission` | decimal | `sale_return_amount − settled_amount` |
| `settled_amount` | decimal | **Net payout to seller** = `vendor_nsp × (1 − 0.413)` |
| `transfer_price` | decimal | Alternate transfer price (mostly 0) |
| `lr_margin__` | decimal | LimeRoad margin percentage (duplicate of `gross_commission_perc`) |
| `lr_commission_as_per_tp` | decimal | Commission as per transfer price |
| `lr_commission_as_per_non_tp` | decimal | Commission on non-transfer-price basis |
| `lr_margin_amount_after_discount_borne_by_limeroad___` | decimal | LR margin after LR-funded discounts |
| `lr_margin_paid_acquisition` | decimal | Acquisition cost margin |
| `margin_model` | decimal | Model indicator: `1.000000` = NSP model |
| `total_vendor_discount` | decimal | Total discount from MRP borne by vendor (MRP − vendor_nsp) |
| `total_limeroad_discount` | decimal | Additional discount funded by LimeRoad |
| `total_adjustment` | decimal | Miscellaneous adjustments (₹0 for most rows) |
| `gst_adjustment_amount` | decimal | GST-related adjustment |
| `vendor_nsp_after_less_ctp_income` | decimal | Adjusted NSP |
| `weight_mapping_to_vendor_cost` | decimal | Weight-based cost mapping |
| `reversal_of_margin_on_return_cancellation___` | decimal | Margin reversal on returns |
### 3.4 Charge Columns (Buyer-Paid)
| Column | Type | Description |
|--------|------|-------------|
| `shipping_charge_paid_by_customer` | decimal | Shipping charge billed to buyer |
| `cod_charge_paid_by_customer` | decimal | COD collection fee paid by buyer |
| `handling_charge_paid_by_customer` | decimal | Handling charge paid by buyer |
| `shipping_amount` | decimal | Shipping amount in settlement |
| `transporter_cost_recovered_from_vendor` | decimal | Logistics cost charged to seller |
| `transporter_cost_recovered_from_vendor_on_return` | decimal | Return logistics cost |
| `collection_charges_recovered_from_vendor` | decimal | Payment collection charges |
| `total_payment_amount_made_to_the_vendor___` | decimal | Total payment made |
### 3.5 Classification Columns
| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward` or `reverse` |
| `order_status` | varchar | `ORDER_DELIVERED`, `ORDER_CANCELLED`, `RETURNED_TO_ORIGIN` |
| `entry_type` | varchar | `ITEM_SALE`, `ITEM_RETURN`, `ITEM_RTO`, `ITEM_CANCEL`, `ITEM_ADJUSTMENT` |
| `sub_order_state` | varchar | Current sub-order state (mirrors `order_status`) |
| `payment_mode` | varchar | `COD` or `PREPAID` |
| `brand` | varchar | `Anubhutee` or `Ishin` |
| `classification` | varchar | Full product category path (see values below) |
| `destination_state` / `customer_state` | varchar | Buyer state |
| `transporter` | varchar | Courier company (see values below) |
| `lost` | varchar | Lost shipment flag |
| `lost_in_transit` | varchar | Lost in transit flag |
| `short_shipment` | varchar | Short shipment flag |
### 3.6 System / Metadata Columns
| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `22`        |
| `currency_type` | varchar | `INR`       |
| `is_active` | boolean | Always `true` |
| `brand_id` / `brand_name` | varchar | Brand identifier and name |
| `who_changes_vnsp` / `date_of_change_vnsp` | varchar | NSP change audit fields |
| `remarks_for_adjustment` | varchar | Reason for adjustment entries |
| `zen_sheet_name` | varchar | Source sheet |
---
## 4. Distinct Value Analysis
### `entry_type` Financial Breakdown
| Entry Type | Count | Total Charged | Commission | Settled | Avg Price |
|------------|-------|---------------|------------|---------|-----------|
| `ITEM_SALE` | 1,650 | ₹16,01,936    | ₹6,54,768  | +₹9,35,252 | ₹970.87   |
| `ITEM_RETURN` | 308   | ₹3,13,148     | ₹1,23,124  | −₹1,88,606 | ₹1,016.71 |
| `ITEM_RTO` | 298   | ₹2,92,637     | ₹1,26,033  | −₹1,63,645 | ₹982.00   |
| `ITEM_CANCEL` | 151   | ₹1,52,899     | ₹65,059    | −₹86,434 | ₹1,012.58 |
| `ITEM_ADJUSTMENT` | 4     | —             | —          | —       | —         |
| NULL       | 14    | ₹16,331       | —          | −₹1,810 | ₹1,166.50 |
### `entry_type` Meanings
| Entry Type | Transaction Type | Meaning |
|------------|------------------|---------|
| `ITEM_SALE` | `forward`        | Forward order successfully delivered or in settlement cycle |
| `ITEM_RETURN` | `reverse`        | Buyer-initiated return after delivery |
| `ITEM_RTO` | `reverse`        | Return-to-Origin — courier failed delivery |
| `ITEM_CANCEL` | `forward`/`reverse` | Order cancelled before or after shipment |
| `ITEM_ADJUSTMENT` | `forward`/`reverse` | Manual settlement adjustment |
### `order_status` Values
| Status | Meaning |
|--------|---------|
| `ORDER_DELIVERED` | Delivered to buyer |
| `RETURNED_TO_ORIGIN` | Courier returned item to seller |
| `ORDER_CANCELLED` | Order cancelled |
### `transporter` (Couriers)
| Transporter | Type |
|-------------|------|
| `shadowfax` | Last-mile courier |
| `delhivery_surface` | Delhivery surface mode |
| `bluedart`  | BlueDart express |
| `bluedart_surface` | BlueDart surface |
| `ecomexpress` | Ecom Express |
| `ekart_surface` | Ekart / Flipkart Logistics surface |
| `xpressbees` | XpressBees express |
| `xpressbees_surface` | XpressBees surface |
| `shiprocket_Delhivery_MSP` | Shiprocket → Delhivery (MSP) |
| `shiprocket_Xpressbees_MSP` | Shiprocket → Xpressbees (MSP) |
### `classification` (Product Categories)
| Category Path | Brand |
|---------------|-------|
| `clothing/ethnic wear/Sets` | Anubhutee, Ishin |
| `clothing/ethnic wear/Kurta Kurtis/kurtas` | Anubhutee, Ishin |
| `clothing/ethnic wear/Kurta Kurtis/kurtis` | Anubhutee |
| `clothing/ethnic wear/Ethnic Dresses` | Ishin |
| `clothing/western wear/Dresses` | Ishin |
| `clothing/western wear/Tunics` | Ishin |
| `clothing/ethnic wear/Sarees` | Ishin |
| `clothing/lingerie/sleepwear/nightwear sets` | Anubhutee |
| `accessories/fashion jewellery/earrings` | Ishin |
### `payment_mode`
| Mode | Meaning |
|------|---------|
| `COD` | Cash on Delivery |
| `PREPAID` | Prepaid (UPI, card, netbanking) |
### Brand Comparison (ITEM_SALE)
| Brand | Orders | Total Charged | Commission | Settled | Avg MRP | Avg Charged | Avg Commission % |
|-------|--------|---------------|------------|---------|---------|-------------|------------------|
| Anubhutee | 1,230  | ₹10,48,805    | ₹4,32,339  | ₹6,05,871 | ₹3,789  | ₹852.69     | 41.3%            |
| Ishin | 420    | ₹5,53,131     | ₹2,22,430  | ₹3,29,381 | ₹5,163  | ₹1,316.98   | 41.3%            |
---
## 5. NSP-Based Settlement Model (Deep Dive)
### How Settlement Is Calculated
LimeRoad's settlement model is unique: **payout is based on Vendor NSP, not on charged_amount**.
~~~
Step 1: MRP                                    ₹5,299
− Vendor Discount (total_vendor_discount)   −₹4,270
= Vendor NSP (vendor_nsp)                   ₹1,029  ← agreed transfer price
Step 2: Seller payout
vendor_nsp × (1 − 0.413)                    = ₹604.02
= settled_amount                             ₹604.02  ← FIXED regardless of buyer price
Step 3: LimeRoad's revenue
sale_return_amount                           = ₹1,109 (charged − COD)
− settled_amount                             −₹604.02
= gross_commission                           ₹504.98  ← varies with buyer price
Step 4: Discount absorption
If LimeRoad discounts below vendor_nsp       → LimeRoad absorbs (total_limeroad_discount < 0)
If LimeRoad prices above vendor_nsp          → LimeRoad retains surplus (total_limeroad_discount > 0)
~~~
**Key insight:** The seller always receives `vendor_nsp × 0.587` regardless of what promotional price LimeRoad offers the buyer. This protects the seller's revenue from LimeRoad's discount campaigns.
### Verified Settlement Formula
~~~sql
-- Validate settled_amount = vendor_nsp × 0.587
SELECT
order_id, vendor_nsp, settled_amount,
ROUND(vendor_nsp * 0.587, 2) AS expected_settled,
ABS(settled_amount - ROUND(vendor_nsp * 0.587, 2)) AS variance
FROM zs_observe.limeroad_settlement
WHERE is_active = true AND entry_type = 'ITEM_SALE'
AND vendor_nsp IS NOT NULL AND vendor_nsp > 0;
~~~
---
## 6. Sample Records
**Forward Sale (COD):**
~~~
order_id              : 0110673371S2
invoice_number        : 0639302526000236
created_date          : 2025-09-25
settlement_date       : 2025-09-30
entry_type            : ITEM_SALE
order_status          : ORDER_DELIVERED
payment_mode          : COD
brand                 : Anubhutee
sku_id                : ANU2111691XL
destination_state     : Delhi
mrp                   : 5299.00
charged_amount        : 1145.00
sale_return_amount    : 1109.00   ← 1145 − 36 (COD charge)
vendor_nsp            : 1029.00
gross_commission_perc : 41.30
gross_commission      : 504.98    ← 1109 − 604.02
settled_amount        : 604.02    ← 1029 × 0.587
total_limeroad_discount: -80.00   ← LimeRoad absorbed ₹80 extra discount
cod_charge_paid_by_customer: 36.00
transporter           : shadowfax
awb                   : SF2167721304LI
classification        : clothing/ethnic wear/Sets
~~~
**Forward Sale (PREPAID, higher price):**
~~~
order_id              : 0110660526S1
payment_mode          : PREPAID
charged_amount        : 909.00
sale_return_amount    : 909.00    ← no COD, so same
vendor_nsp            : 1029.00
settled_amount        : 604.02    ← SAME as COD example — NSP-based
gross_commission      : 304.98    ← 909 − 604.02 (lower than COD — buyer paid less)
total_limeroad_discount: 120.00   ← LimeRoad offered extra ₹120 off to buyer
transporter           : ekart_surface
~~~
**Return (ITEM_RETURN):**
~~~
entry_type            : ITEM_RETURN
transaction_type      : reverse
order_status          : ORDER_DELIVERED
settled_amount        : -188,606  ← negative (refund deducted from seller)
gross_commission      : 123,124   ← commission reversed on return
~~~
---
## 7. Data Quality Observations
| Issue | Detail | Mitigation |
|-------|--------|------------|
| `vendor_nsp` critical for settlement | Core financial field; must not be NULL for settlement validation | Filter `vendor_nsp IS NOT NULL AND vendor_nsp > 0` |
| `sale_return_amount` ≠ `charged_amount` for COD | Differs by COD collection charge (₹36–₹100 typically) | Use `sale_return_amount` as settlement base; `charged_amount` for GMV |
| Entry type NULL for 14 rows | Older settlement format | These 14 rows still carry financial data; include in totals |
| `transfer_price = 0` for most rows | Not the NSP model — indicates standard commission model active | Use `vendor_nsp` for payout calculation |
| `total_limeroad_discount` sign convention | Negative = LimeRoad absorbed extra discount; positive = LimeRoad priced above NSP | Apply `ABS()` carefully |
| Settlement date vs created_date | Settlement can be 2–7 days after order creation | Use `settlement_date` for cash-flow reporting |
| `lost` / `lost_in_transit` mostly NULL | Only populated for flagged orders | NULL = not lost |
| Commission always 41.3% | No category variation in current data | Validate if new categories added with different rates |
---
## 8. Common Query Patterns
### 8.1 Payout Summary by Settlement Date
~~~sql
SELECT
settlement_date,
COUNT(*) AS line_items,
SUM(CASE WHEN entry_type='ITEM_SALE' THEN settled_amount ELSE 0 END) AS sales_settled,
SUM(CASE WHEN entry_type IN ('ITEM_RETURN','ITEM_RTO') THEN settled_amount ELSE 0 END) AS returns_settled,
SUM(CASE WHEN entry_type='ITEM_CANCEL' THEN settled_amount ELSE 0 END) AS cancels_settled,
SUM(settled_amount) AS net_payout
FROM zs_observe.limeroad_settlement
WHERE is_active = true
GROUP BY settlement_date
ORDER BY settlement_date;
~~~
### 8.2 Financial Waterfall (Full View)
~~~sql
SELECT
SUM(CASE WHEN entry_type='ITEM_SALE' THEN mrp ELSE 0 END) AS total_mrp,
SUM(CASE WHEN entry_type='ITEM_SALE' THEN charged_amount ELSE 0 END) AS gross_gmv,
SUM(CASE WHEN entry_type='ITEM_SALE' THEN total_vendor_discount ELSE 0 END) AS vendor_discount,
SUM(CASE WHEN entry_type='ITEM_SALE' THEN vendor_nsp ELSE 0 END) AS total_vendor_nsp,
SUM(CASE WHEN entry_type='ITEM_SALE' THEN gross_commission ELSE 0 END) AS lr_commission,
SUM(CASE WHEN entry_type='ITEM_SALE' THEN settled_amount ELSE 0 END) AS forward_settled,
SUM(CASE WHEN entry_type IN ('ITEM_RETURN','ITEM_RTO','ITEM_CANCEL') THEN settled_amount ELSE 0 END) AS reverse_settled,
SUM(settled_amount) AS net_settled
FROM zs_observe.limeroad_settlement
WHERE is_active = true;
~~~
### 8.3 Settlement ↔ OMS Reconciliation
~~~sql
SELECT
o.invoice_number, o.order_id, o.item_id,
o.charged_amount AS oms_invoice_value,
s.charged_amount AS stl_charged,
s.vendor_nsp, s.settled_amount,
ABS(o.charged_amount - s.charged_amount) AS price_variance,
CASE WHEN s.invoice_number IS NULL THEN 'Not in Settlement' ELSE 'Matched' END AS status
FROM zs_observe.limeroad_oms o
LEFT JOIN zs_observe.limeroad_settlement s
ON o.invoice_number = s.invoice_number
AND o.item_id = s.item_id
AND s.is_active = true
WHERE o.is_active = true AND o.transaction_type = 'forward';
~~~
### 8.4 Commission Validation
~~~sql
SELECT
order_id,
vendor_nsp,
settled_amount,
ROUND(vendor_nsp * (1 - gross_commission_perc / 100), 2) AS expected_settled,
ABS(settled_amount - ROUND(vendor_nsp * (1 - gross_commission_perc / 100), 2)) AS variance
FROM zs_observe.limeroad_settlement
WHERE is_active = true AND entry_type = 'ITEM_SALE'
AND vendor_nsp > 0
ORDER BY variance DESC
LIMIT 20;
~~~
### 8.5 Return Rate and Value
~~~sql
SELECT
brand,
COUNT_IF(entry_type = 'ITEM_SALE') AS sales,
COUNT_IF(entry_type = 'ITEM_RETURN') AS buyer_returns,
COUNT_IF(entry_type = 'ITEM_RTO') AS rto,
COUNT_IF(entry_type = 'ITEM_CANCEL') AS cancels,
ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_RETURN')
/ NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS return_rate_pct,
ROUND(100.0 * COUNT_IF(entry_type = 'ITEM_RTO')
/ NULLIF(COUNT_IF(entry_type = 'ITEM_SALE'), 0), 2) AS rto_rate_pct
FROM zs_observe.limeroad_settlement
WHERE is_active = true
GROUP BY brand;
~~~
### 8.6 Category-Level Performance
~~~sql
SELECT
classification,
COUNT(*) AS orders,
SUM(charged_amount) AS gmv,
SUM(vendor_nsp) AS total_nsp,
SUM(settled_amount) AS seller_payout,
SUM(gross_commission) AS lr_commission,
AVG(gross_commission_perc) AS commission_rate
FROM zs_observe.limeroad_settlement
WHERE is_active = true AND entry_type = 'ITEM_SALE'
GROUP BY classification
ORDER BY gmv DESC;
~~~
Tab 3
# Table: LimeRoad OMS — Table Knowledge Base
**Schema:** `zs_observe`  **Table:** `limeroad_oms`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team
---
## 1. Table Overview
`limeroad_oms` is the **GST invoice / Order Management System (OMS) table** for LimeRoad. It stores the formal GST-compliant invoice records for every item sold or returned on the platform. LimeRoad (owned by V-Mart Retail Limited post-acquisition) is India's social fashion marketplace focused on women's ethnic wear and lifestyle products.
Each row represents one invoice line item — a single product in a forward sale or return transaction. The table provides full tax detail (IGST / CGST+SGST split), TCS (GST §52), TDS (IT §194-O), shipping taxes, and both the raw item value and shipping component.
**Seller entity:** Mensa Brand Technologies Pvt Ltd\n**E-commerce operator:** V MART RETAIL LIMITED (GSTIN: `06AABCV7206K1Z9`)\n**Brands:** Anubhutee, Ishin, High Star\n**Products:** Women's ethnic wear — kurta sets, kurtis, kurtis with palazzo, dresses
---
## 2. Key Statistics
| Metric | Value |
|--------|-------|
| Total rows | 2,255 |
| Active rows (`is_active = true`) | 2,255 (100%) |
| group_level_id | 22    |
| Date range (`created_date`) | 2025-01-01 → 2025-12-06 |
| Distinct orders | 1,540 |
| Distinct SKUs | 337   |
| Distinct HSN codes | 10    |
| Forward transactions | 1,583 |
| Reverse (return) transactions | 672   |
| Source states | 4 (Haryana, Karnataka, Maharashtra, West Bengal) |
| Seller GSTINs | 4     |
| E-commerce operator | V MART RETAIL LIMITED |
| Total GMV | ₹22,47,470 |
| Total TCS | ₹12,869.96 |
| Total TDS | ₹20,648.13 |
| Avg forward order value | ₹971–₹1,026 |
| Brands | Anubhutee, Ishin, High Star |
| Currency | INR (100%) |
---
## 3. Schema Details (102 Columns)
### 3.1 Identity Columns
| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | System row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Deduplication hash |
| `invoice_number` / `invoiceid` | varchar | **GST invoice number** (format: `0629872526000001`). Pattern: `{GSTIN_prefix}{FY_code}{sequence}` — join key to settlement |
| `order_id` | varchar | LimeRoad order ID with sub-order suffix (e.g., `0109109407S4`) — join key to settlement |
| `orderid` | varchar | Base order number without sub-order (e.g., `0109109407`) |
| `suborderid` | varchar | Sub-order number (e.g., `4`) |
| `item_id` | varchar | **Line item UUID** (format: `3d662092-66d0-4a49-bf73-857d68651f42`) — join key to settlement |
| `uniqueitemid` | varchar | Duplicate of `item_id` |
| `other_id_2` | varchar | Additional reference |
| `sku_id` / `vendorstylecode` | varchar | Seller style/SKU code (e.g., `INWTO0244_PN_L`, `Kpldpnk-17038_S`) |
| `source_gst_id` / `gstin` | varchar | Seller GSTIN (4 distinct values) |
| `source_gst_name` | varchar | `Mensa Brand Technologies Pvt Ltd` |
| `e_commercegstin` | varchar | LimeRoad/V-Mart e-commerce GSTIN: `06AABCV7206K1Z9` |
| `e_commercename` | varchar | `V MART RETAIL LIMITED` |
| `vendorname` | varchar | `Mensa Brand Technologies Pvt Ltd` |
| `vendorid` | varchar | Vendor ID on LimeRoad |
### 3.2 Date Columns
| Column | Type | Description |
|--------|------|-------------|
| `created_date` | date | Record creation date — **primary date field** |
| `invoicedate` | varchar | Invoice date-time string (format: `2025-05-21 06:57:05 UTC`) |
| `invoicedate_temp_old` | timestamp | Legacy invoice date |
### 3.3 Financial Columns
| Column | Type | Description |
|--------|------|-------------|
| `charged_amount` / `invoicevalue` | decimal | **Total invoice value (GST inclusive)** |
| `charged_amount_excluding_tax` | decimal | Taxable value (item + shipping, excl. GST) |
| `total_tax` | decimal | Total GST on the transaction |
| `total_tax_perc` | decimal | Effective GST rate (%) |
| `item_amount_excluding_tax` | decimal | Product value excluding GST |
| `shipping_amount_excluding_tax` | decimal | Shipping charge excluding GST |
| `itemtaxableamount` | decimal | Item taxable amount (raw field) |
| `shippingtaxableamount` | decimal | Shipping taxable amount (raw field) |
| `totalsupplytaxableamount` | decimal | Total supply taxable amount |
| `codtaxableamount` | decimal | COD charge taxable amount |
| `taxamount` | decimal | Tax amount (raw field) |
| `cessamount` | decimal | Cess amount |
### 3.4 Tax Columns
| Column | Type | Description |
|--------|------|-------------|
| `tax_igst_rate` | decimal | IGST rate (decimal form: 0.05 = 5%, 0.12 = 12%) |
| `tax_igst_amount` | decimal | IGST amount (inter-state orders) |
| `tax_cgst_rate` | decimal | CGST rate (0.025 = 2.5%, 0.06 = 6%) |
| `tax_cgst_amount` | decimal | CGST amount (intra-state) |
| `tax_sgst_rate` | decimal | SGST rate (mirrors CGST) |
| `tax_sgst_amount` | decimal | SGST amount |
| `igst` | decimal | IGST duplicate |
| `taxamountforigst` / `taxamountforcgst` / `taxamountforsgst` | decimal | Tax amount breakdown (raw) |
| `hsn` / `hsncode` | varchar | HSN code (both fields — see values below) |
| `totalgstrate` | decimal | Total GST rate (%) |
### 3.5 TCS / TDS Columns
| Column | Type | Description |
|--------|------|-------------|
| `tcs_igst_amount` | decimal | TCS IGST component (inter-state) |
| `tcs_cgst_amount` | decimal | TCS CGST component (intra-state) |
| `tcs_sgst_amount` | decimal | TCS SGST component |
| `tcsamountforigst` / `tcsamountforcgst` / `tcsamountforsgst` | decimal | TCS breakdown (raw) |
| `total_tds` | decimal | **Total TDS deducted** (IT §194-O) |
| `tdsamount` | decimal | TDS amount (duplicate of `total_tds`) |
### 3.6 Classification / Status Columns
| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward` (sale) or `reverse` (return) |
| `eventtype` | varchar | `sale` or `return` (mirrors transaction_type) |
| `salestype` | varchar | `Interstate` or `Intrastate` |
| `brand` | varchar | `Anubhutee`, `Ishin`, `High Star` |
| `description` / `productdescription` | varchar | Product description |
| `quantity` | integer | Quantity per line |
| `temp` | varchar | Temporary field |
### 3.7 Geographic Columns
| Column | Type | Description |
|--------|------|-------------|
| `source_state` / `vendorstate` | varchar | Seller dispatch state (lowercase) |
| `source_gst_id` | varchar | Derived source state from GSTIN |
| `source_zipcode` / `vendorpincode` | varchar | Seller pincode |
| `destination_state` / `customerstate` | varchar | Buyer state |
| `destination_zipcode` / `customerpincode` | decimal | Buyer pincode |
| `source_state_code` / `destination_state_code` | varchar | State codes |
### 3.8 System / Metadata Columns
| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `22` — LimeRoad / Mensa account |
| `currency_type` | varchar | `INR`       |
| `is_active` | boolean | Always `true` |
| `ancestry` | varchar | Lineage     |
| `sgst` / `cgst` / `none` | varchar | Legacy string fields |
| `*_temp_old` | various | Migration columns |
| `failure_reason_order_id` | varchar | Order ID from failure reason tracking |
| `zen_sheet_name` | varchar | Source sheet |
| `brand_ref_1` / `brand_ref_2` | not present | Not in OMS — no brand ref columns |
---
## 4. Distinct Value Analysis
### `transaction_type` / `eventtype` / `salestype` Breakdown
| Txn Type | Event Type | Sales Type | Count | Total GMV | Avg Price |
|----------|------------|------------|-------|-----------|-----------|
| `forward` | `sale`     | `Interstate` | 1,320 | ₹12,80,657 | ₹970.19   |
| `forward` | `sale`     | `Intrastate` | 258   | ₹2,64,689 | ₹1,025.93 |
| `reverse` | `return`   | `Interstate` | 545   | ₹5,59,545 | ₹1,026.69 |
| `reverse` | `return`   | `Intrastate` | 101   | ₹1,07,768 | ₹1,067.01 |
| `reverse` | NULL       | NULL       | 26    | ₹29,136   | ₹1,120.62 |
### Seller GSTIN → Warehouse Mapping
| GSTIN | State | Brand Focus |
|-------|-------|-------------|
| `29AAOCM5326J1ZY` | Karnataka | Ishin, Anubhutee |
| `27AAOCM5326J1Z2` | Maharashtra | Anubhutee   |
| `19AAOCM5326J1ZZ` | West Bengal | Ishin       |
| `06AAOCM5326J1Z6` | Haryana | All brands  |
### HSN Code Distribution (Forward Sales)
| HSN | Category | GST Rate | Count |
|-----|----------|----------|-------|
| `62063000` | Women's blouses/shirts (cotton) | 5%       | 578   |
| `62064000` | Women's blouses/shirts (man-made fibre) | 5%       | 565   |
| `62114290` | Other women's garments (man-made fibre) | 5% / 12% | 160   |
| `62044390` | Women's dresses (man-made fibre) | 12%      | 86    |
| `62114990` | Other women's garments | 5% / 12% | 85    |
| `62063000` / `62069000` | Other women's garments | 5%       | \~others |
| `71179010` | Fashion jewellery | 3%       | few   |
| `54075430` | Woven fabric / textiles | 5%       | few   |
| `998599` | Marketplace services (SAC code) | 18%      | few   |
### GST Rates Observed
| Rate | Type | Application |
|------|------|-------------|
| 5% IGST / 2.5% CGST+SGST | Clothing items (HSN 620xx) | Majority of apparel |
| 12% IGST / 6% CGST+SGST | Some garment types | Higher-value items |
| 3% IGST | Fashion jewellery (HSN 7117) | Accessories |
| 18% IGST | Marketplace services (SAC 998599) | Service entries |
### Brand Distribution
| Brand | Forward Orders | Avg Price | Categories |
|-------|----------------|-----------|------------|
| Anubhutee | \~1,143        | ₹942–₹1,030 | Ethnic sets, kurtas, kurtis, nightwear |
| Ishin | \~331          | ₹1,268–₹1,466 | Premium ethnic sets, dresses, sarees |
| High Star | \~few          | —         | Accessories |
---
## 5. Sample Records
**Inter-state Sale (IGST):**
~~~
source_gst_name     : Mensa Brand Technologies Pvt Ltd
source_gst_id       : 19AAOCM5326J1ZZ
invoice_number      : 0629872526000001
created_date        : 2025-05-21
transaction_type    : forward
eventtype           : sale
salestype           : Interstate
order_id            : 0109109407S4
suborderid          : 4
item_id             : 3d662092-66d0-4a49-bf73-857d68651f42
description         : women floral print flared tunic
hsn                 : 62069000
sku_id              : INWTO0244_PN_L
source_state        : west bengal
destination_state   : maharashtra
charged_amount      : 1112.00
charged_amount_excl : 992.86
total_tax           : 119.14
total_tax_perc      : 12.00
tax_igst_rate       : 0.12  ← inter-state IGST
tax_igst_amount     : 119.14
tcs_igst_amount     : 4.96
total_tds           : 9.92
brand               : Ishin
e_commercename      : V MART RETAIL LIMITED
group_level_id      : 22
~~~
**Intra-state Sale (CGST+SGST):**
~~~
source_gst_id       : 29AAOCM5326J1ZY
salestype           : Intrastate
source_state        : karnataka
destination_state   : karnataka   ← same state
tax_igst_rate       : 0.000000    ← no IGST
tax_cgst_rate       : 6.000000    ← CGST 6%
tax_cgst_amount     : 57.803600
tax_sgst_rate       : 6.000000    ← SGST 6%
tax_sgst_amount     : 57.803600
tcs_cgst_amount     : 2.40
tcs_sgst_amount     : 2.40
total_tds           : 9.63
~~~
---
## 6. Data Quality Observations
| Issue | Detail | Mitigation |
|-------|--------|------------|
| `tax_igst_rate` dual format | Stored as both decimal (0.12) and percentage (12.0) across rows | Normalize: values > 1 are percentages; divide by 100 |
| `invoicedate` stored as varchar | Not natively date-filterable | Cast: `CAST(invoicedate AS TIMESTAMP)` |
| 25 rows with `brand = NULL` | \~1.6% of forward rows lack brand | Join settlement on `item_id` for brand |
| `salestype` NULL for 5 rows | Very few older format rows | Default to `Interstate` if source ≠ destination |
| Duplicate field pairs | `hsn` / `hsncode`, `description` / `productdescription`, `order_id` / `orderid`, `item_id` / `uniqueitemid` — use primary fields | Use `hsn`, `description`, `order_id`, `item_id` |
| `cgst` / `sgst` stored as varchar | Legacy string fields | Use typed columns: `tax_cgst_amount`, `tax_sgst_amount` |
| Source state lowercase | `karnataka` (OMS) vs `Karnataka` (settlement) | `UPPER(source_state)` for joins |
| 26 reverse rows with NULL eventtype | Older format reverse entries | Filter `transaction_type = 'reverse'` captures all returns |
---
## 7. Common Query Patterns
### 7.1 Monthly GMV Trend
~~~sql
SELECT
DATE_TRUNC('month', created_date) AS month,
transaction_type,
COUNT(*) AS orders,
SUM(charged_amount) AS gmv,
SUM(tcs_igst_amount + tcs_cgst_amount + tcs_sgst_amount) AS tcs,
SUM(total_tds) AS tds
FROM zs_observe.limeroad_oms
WHERE is_active = true
GROUP BY 1, 2 ORDER BY 1, 2;
~~~
### 7.2 Interstate vs Intrastate GST Split
~~~sql
SELECT
salestype,
COUNT(*) AS cnt,
SUM(charged_amount) AS gmv,
SUM(tax_igst_amount) AS igst,
SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
FROM zs_observe.limeroad_oms
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY salestype;
~~~
### 7.3 Brand-Level Performance
~~~sql
SELECT
brand,
hsn,
COUNT(*) AS orders,
SUM(charged_amount) AS gmv,
AVG(charged_amount) AS avg_price,
SUM(total_tax) AS gst_collected
FROM zs_observe.limeroad_oms
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY brand, hsn
ORDER BY gmv DESC;
~~~
### 7.4 OMS → Settlement Join
~~~sql
SELECT
o.invoice_number, o.order_id, o.item_id,
o.charged_amount AS oms_invoice_value,
o.total_tcs_amount,
s.settled_amount, s.gross_commission, s.vendor_nsp
FROM zs_observe.limeroad_oms o
LEFT JOIN zs_observe.limeroad_settlement s
ON o.invoice_number = s.invoice_number
AND o.item_id = s.item_id
AND s.is_active = true
WHERE o.is_active = true AND o.transaction_type = 'forward';
~~~
### 7.5 TCS + TDS Summary
~~~sql
SELECT
DATE_TRUNC('month', created_date) AS month,
SUM(tcs_igst_amount + tcs_cgst_amount + tcs_sgst_amount) AS total_tcs,
SUM(total_tds) AS total_tds
FROM zs_observe.limeroad_oms
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY 1 ORDER BY 1;
~~~

```
