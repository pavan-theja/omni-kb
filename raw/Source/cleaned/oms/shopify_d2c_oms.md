# Shopify D2C OMS Gold Standard Markdown
```yaml
document_metadata:
  document_id: shopify_d2c_oms_gold_standard_v1_manifest_ready
  system: Shopify
  source_docx:
  - /mnt/data/Shopify OMS.docx
  - /mnt/data/OMS-Business Knowledge Base.docx
  cleanup_manifest: /mnt/data/marketplace_cleanup_manifest_consolidated_v2.md
  structure_reference: /mnt/data/amazon_marketplace.md
  generated_on: '2026-05-24'
  scope: D2C OMS canonical markdown for brands using Shopify directly
  included_source_tables:
  - table.zs_observe.shopify_oms
  - table.zs_observe.shopify_returns
  reference_only_source_tables:
  - table.zs_observe.shiprocket_oms
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
    shopify_oms_docx: d3411d858cd626dcd5c9377dcc0ff3290a9c2f8b33daa1510c95382cb168fd05
    oms_business_kb_docx: abc0ab7d0e06583af426daecc58b85d03cf2517b765c983e8568046e41af4bb9
    manifest: e151167df1ff75a63b6eddaf74f0bfddd8a4741bc67d27988e7455fee8b39661
  quality_summary:
    candidate_cards: 169
    candidate_edges: 112
    source_evidence_count: 12
    sql_patterns: 18
    missing_edge_references: 0
    dangling_sql_refs: 0
    deleted_card_references: 0
    open_reviews: 2
    lazy_workflow_steps: 0
    placeholder_metric_formulas: 0
    unsupported_metric_implementations: 0
    process_variants_review_required: 0
    unresolved_benchmark_reviews_without_reason: 0
    hard_threshold_benchmarks_without_rule: 0
    forbidden_scope_cards_from_scope_ids: 0
```
## 0. Parser Instructions

This document is intended to be parsed deterministically. Every `candidate_card`, `candidate_edge`, `source_evidence`, `review_item`, and SQL block is machine-readable and evidence-backed. Do not infer tenant, account, bank, courier, ERP, connector, or statutory filing cards from scope identifiers, references, GSTINs, payment labels, or courier labels.

```yaml
manifest_crosswalk:
  source_manifest: marketplace_cleanup_manifest_consolidated_v2.md
  applied_to: Shopify
  required_release_gates:
  - Every card has evidence_refs and source-backed semantics.
  - Segments such as COD/PREPAID, financial_status, sales_channel, and order_status are value_profile cards unless a distinct
    workflow is explicitly documented.
  - Metric implementations use executable SQL-like formulas, existing columns, required filters, and documented sign/grain
    rules.
  - String amount/date fields keep source type and declare cast_required where needed.
  - Every sql_reference_id has a SQL pattern block.
  - Edges reference only existing candidate cards.
  - group_id, tenant_id, group_level_id, GSTINs, payment refs, and channel/courier labels remain columns/caveats, not tenant/account/bank/courier
    cards.
  - Parser QA summary must report zero dangling SQL refs, missing edge refs, lazy workflow steps, placeholder formulas, and
    forbidden scope cards.
```
```yaml
semantic_field_contract:
- card_type: platform
  required_fields:
  - display_name
  - platform_category
  - evidence_refs
  parser_instruction: Create one vendor/system identity card only; never create tenant/account cards.
- card_type: platform_context
  required_fields:
  - platform_id
  - country_code
  - currency_context
  - scope_filter_columns
  - evidence_refs
  parser_instruction: Scope identifiers remain filter columns, not runtime account bindings.
- card_type: domain
  required_fields:
  - domain_family
  - semantic_scope
  - evidence_refs
  parser_instruction: Populate only directly supported semantic domains.
- card_type: table
  required_fields:
  - schema_name
  - table_name
  - table_role
  - row_scope
  - mandatory_filters
  - grain
  - evidence_refs
  parser_instruction: Respect source table grain and data quality filters.
- card_type: column
  required_fields:
  - table_id
  - column_name
  - data_type
  - semantic_role
  - description
  - evidence_refs
  parser_instruction: Preserve source spellings and type fidelity; add cast_required where needed.
- card_type: value_profile
  required_fields:
  - table_id
  - column_names
  - values_or_known_values
  - evidence_refs
  parser_instruction: Do not convert simple values or segments into process variants.
- card_type: metric
  required_fields:
  - metric_key
  - business_definition
  - default_grain
  - evidence_refs
  parser_instruction: Metrics can be generic within the file only when implementation is executable.
- card_type: metric_implementation
  required_fields:
  - metric_id
  - source_table_ids
  - formula
  - sql_reference_id
  - required_filters
  - evidence_refs
  parser_instruction: Formula must be SQL-like and use declared columns.
- card_type: relationship
  required_fields:
  - from_table
  - to_table
  - join_keys
  - join_safety_rule
  - relationship_grain
  - evidence_refs
  parser_instruction: Relationships must include grain and aggregation guardrails.
- card_type: business_process
  required_fields:
  - process_summary
  - domain_id
  - evidence_refs
  parser_instruction: Workflow steps must mention source-specific tables, columns, statuses, or amount fields.
- card_type: reconciliation_profile
  required_fields:
  - expected_side
  - actual_side
  - unit
  - matching_logic
  - evidence_refs
  parser_instruction: Use reconciliation cards when the source describes expected/actual matching or gap analysis.
- card_type: query_pattern
  required_fields:
  - natural_language_patterns
  - primary_metric
  - source_table_ids
  - sql_reference_id
  - output_contract_id
  - evidence_refs
  parser_instruction: Each SQL ref must resolve to a SQL pattern block.
- card_type: validation_test
  required_fields:
  - assertion
  - related_ids
  - evidence_refs
  parser_instruction: Validation tests enforce parser/data-integrity expectations from the source.
```
## 1. Source Evidence Registry

```yaml
source_evidence:
  id: ev.shopify.scope.001
  source_document: Shopify OMS.docx
  source_section: Overview
  evidence_type: prose
  summary: shopify_oms is the D2C top-of-funnel OMS table for customer orders on Shopify storefronts and is the origin for
    downstream shipment, COD settlement and courier invoice analysis.
  supported_semantics:
  - Shopify as D2C OMS/channel order source
  - shiprocket relationship may be reference-only
  unsupported_semantics:
  - external courier account ownership
  - bank account or PG account creation
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.schema.oms.001
  source_document: Shopify OMS.docx
  source_section: Schema (Key Fields)
  evidence_type: schema_reference
  summary: Documents key shopify_oms columns including order_id, transaction_type, financial_status, payment_mode, charged_amount,
    refunded_amount, mrp, sku_id, quantity, destination fields, other_id, created_date, is_active, group_level_id and unique_id.
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.schema.extended.001
  source_document: OMS-Business Knowledge Base.docx
  source_section: 'Table 3: shopify_oms > Key Columns; Tax Columns'
  evidence_type: schema_reference
  summary: Adds extended Shopify OMS fields including internal id/name, order_status, fulfillment_status, payment_id/payment_references,
    detailed tax components, note_attributes, tags_1, risk_level, outstanding_balance, fulfilled_at and currency_type.
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.order_grain.001
  source_document: Shopify OMS.docx
  source_section: Business Logic > Order Identification
  evidence_type: rule
  summary: 'Shopify supports multi-line orders; each line item gets other_id like #HS98296.1 and order-level GMV requires
    summing charged_amount by order_id.'
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.financial_status.001
  source_document: Shopify OMS.docx
  source_section: Business Logic > Financial Status → Payment Type Mapping
  evidence_type: value_profile
  summary: financial_status maps paid to prepaid, pending to COD, partially_paid to PPCOD, and voided to cancelled-before-shipment
    semantics.
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.lifecycle.001
  source_document: Shopify OMS.docx
  source_section: Business Logic > Transaction Type Lifecycle
  evidence_type: workflow
  summary: transaction_type documents fulfilled, pending, and partial fulfillment-state lifecycle values.
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.payment_mode.001
  source_document: Shopify OMS.docx
  source_section: Schema; Payment Mode Distribution
  evidence_type: value_profile
  summary: payment_mode records customer payment method and may include multiple gateway names separated by +; the last gateway
    is considered the successful payment. COD and GoKwik UPI/PPCOD/Cards are major observed values.
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.data_quality.001
  source_document: Shopify OMS.docx
  source_section: Data Quality Notes
  evidence_type: caveat
  summary: charged_amount is varchar and must be cast for aggregation; COD financial_status remains pending until remittance;
    multi-item orders repeat order_id; prefer refunded_amount over refunded_amount_1.
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.shiprocket_join.001
  source_document: Shopify OMS.docx
  source_section: Join Patterns
  evidence_type: query_example
  summary: Shopify order links to Shiprocket shipment using sr.order_id LIKE CONCAT(s.order_id, '-%') with active filters
    on both tables.
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.tax_recon.001
  source_document: OMS-Business Knowledge Base.docx
  source_section: Shopify OMS > Business Rules & Reconciliation Use Cases
  evidence_type: reconciliation_playbook
  summary: Tax columns cover multi-component GST; COD/partial payment, GoKwik/Fastrr note_attributes, PG settlement matching,
    COD remittance mismatches, partial-payment mismatches and refund validation are documented Shopify use cases.
  confidence: high
```
```yaml
source_evidence:
  id: ev.shopify.returns.001
  source_document: OMS-Business Knowledge Base.docx
  source_section: 'Table 4: shopify_returns'
  evidence_type: schema_reference
  summary: shopify_returns captures return/refund transaction events with order_name, transaction_id, payment_gateway, transaction_status,
    order_payment_status, refunded_payments, other_id and currency_type.
  confidence: high
```
```yaml
source_evidence:
  id: ev.platform.universal_columns.001
  source_document: OMS-Business Knowledge Base.docx
  source_section: Platform Overview > Universal System Columns
  evidence_type: schema_reference
  summary: Universal system columns include group_id, tenant_id, group_level_id, file_uuid, txn_uuid, unique_value, is_active,
    is_duplicated, zen_status, zen_sheet_name, created_at, updated_at, deleted_at and currency_type.
  confidence: high
```
## 2. Scope Guardrails and Out-of-Scope Registry

```yaml
out_of_scope_item:
  id: oos.shopify.tenant_account
  topic: tenant/account binding
  instruction: group_id, tenant_id and group_level_id may appear only as columns or documented filter values; do not create
    tenant/account cards.
  forbidden_card_population:
  - tenant
  - group
  - platform_account
  - account_data_binding
  evidence_refs:
  - ev.platform.universal_columns.001
  - ev.shopify.schema.oms.001
```
```yaml
out_of_scope_item:
  id: oos.shopify.pg_account
  topic: payment gateway account binding
  instruction: payment_id, payment_references, payment_gateway and payment_mode are payment references/labels only; exact
    PG settlement source binding remains external runtime scope.
  forbidden_card_population:
  - payment_gateway_account
  - bank_account
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.returns.001
```
```yaml
out_of_scope_item:
  id: oos.shopify.courier_account
  topic: external courier operations
  instruction: Shiprocket join is reference-only for shipment enrichment. Do not create courier accounts, courier invoice
    reconciliation, or external logistics operations cards.
  forbidden_card_population:
  - courier_account
  - logistics_account
  - carrier_reconciliation
  evidence_refs:
  - ev.shopify.shiprocket_join.001
```
```yaml
out_of_scope_item:
  id: oos.shopify.tax_filing
  topic: statutory filing
  instruction: GST tax columns support invoice analytics only; do not create statutory filing or compliance cards.
  forbidden_card_population:
  - statutory_tax_filing
  evidence_refs:
  - ev.shopify.tax_recon.001
```
## 3. Candidate Card Registry

### 3.x platform

```yaml
candidate_card:
  card_type: platform
  card_id: platform.shopify
  display_name: Shopify
  canonical_name: Shopify
  platform_category: d2c_channel_oms
  marketplace_vendor_doc: false
  evidence_refs:
  - ev.shopify.scope.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x platform_context

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.shopify.in.d2c_oms
  display_name: Shopify India D2C OMS context
  platform_id: platform.shopify
  country_code: IN
  currency_context:
  - INR primary; GBP/USD possible via returns/order context
  timezone: Asia/Kolkata
  platform_model: brand_direct_shopify_storefront_oms
  scope_filter_columns:
  - group_level_id
  - currency_type
  - brand
  - payment_mode
  - financial_status
  evidence_refs:
  - ev.shopify.scope.001
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x domain

```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.d2c_order_capture
  display_name: D2C Shopify order capture
  domain_family: d2c_oms_orders
  semantic_scope: Orders placed by customers on brand-owned Shopify storefronts, including line-item grain and customer payment
    state.
  evidence_refs:
  - ev.shopify.scope.001
  - ev.shopify.tax_recon.001
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
  semantic_scope: financial_status and payment_mode semantics for prepaid, COD, PPCOD, GoKwik and partial payment analysis.
  evidence_refs:
  - ev.shopify.scope.001
  - ev.shopify.tax_recon.001
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
  semantic_scope: transaction_type/order_status/fulfillment_status as OMS fulfillment state, not external courier operations.
  evidence_refs:
  - ev.shopify.scope.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.tax_discount_amounts
  display_name: Shopify tax, discount, and amount semantics
  domain_family: d2c_tax_amounts
  semantic_scope: charged_amount, subtotal, shipping, tax component, discount, refund and outstanding-balance fields.
  evidence_refs:
  - ev.shopify.scope.001
  - ev.shopify.tax_recon.001
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
  semantic_scope: shopify_returns refund event semantics and gateway refund reference fields.
  evidence_refs:
  - ev.shopify.scope.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.shopify.reconciliation
  display_name: Shopify OMS reconciliation hooks
  domain_family: d2c_reconciliation
  semantic_scope: Order-to-PG, COD remittance, refund-to-gateway, and Shopify-to-Shiprocket relationship semantics.
  evidence_refs:
  - ev.shopify.scope.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x table

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shopify_oms
  display_name: zs_observe.shopify_oms
  schema_name: zs_observe
  table_name: shopify_oms
  source_system: Shopify OMS
  table_role: d2c_channel_oms_order_line_ledger
  row_scope: One row per Shopify order line item; repeated order_id for multi-SKU orders.
  grain: order_line
  mandatory_filters:
  - is_active = true
  recommended_filters:
  - group_level_id = 22 when reproducing documented Shopify table scope
  primary_date_column: created_date (source varchar in dedicated Shopify doc; cast when date filtering)
  primary_amount_column: charged_amount (source varchar in dedicated Shopify doc; TRY_CAST for aggregation)
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.order_grain.001
  - ev.shopify.data_quality.001
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
  table_role: d2c_channel_oms_refund_event_ledger
  row_scope: Return/refund transaction records with refund payment references and gateway statuses.
  grain: refund_event
  mandatory_filters:
  - is_active = true when universal quality columns are available
  primary_date_column: customer_added_date
  primary_amount_column: refunded_payments
  evidence_refs:
  - ev.shopify.returns.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
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
  row_scope: Reference-only table for Shopify-to-shipment join pattern; do not create courier-account cards from this file.
  grain: shipment
  mandatory_filters:
  - is_active = true
  evidence_refs:
  - ev.shopify.shiprocket_join.001
  confidence: medium
  review_status: accepted_as_reference_only
  create_action: create_reference_only
```
### 3.x column

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.unique_id
  display_name: unique_id
  column_name: unique_id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: system_identifier
  description: ZenStatement internal row id.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  data_type: varchar
  semantic_role: scope_identifier
  description: Source scope column; column only, not tenant card.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  data_type: varchar
  semantic_role: scope_identifier
  description: Alias/scope column; column only.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: scope_identifier
  description: Documented as always 22 for dedicated Shopify table; do not create account card.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.ancestry
  display_name: ancestry
  column_name: ancestry
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: system_lineage
  description: Hierarchical source path.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: file_lineage
  description: Source file UUID.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: system_identifier
  description: Pipeline transaction UUID.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: dedup_identifier
  description: Deduplication key.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: quality_filter
  description: Mandatory active-row filter.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  data_type: boolean
  semantic_role: quality_filter
  description: Duplicate-row flag where present.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: quality_filter
  description: ZenStatement processing status; preserve source type per actual table.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: source_sheet
  description: Source sheet name.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: pipeline_timestamp
  description: Pipeline creation timestamp.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: pipeline_timestamp
  description: Pipeline update timestamp.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: pipeline_timestamp
  description: Soft-delete timestamp.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: currency
  description: Currency code, e.g. INR/GBP/USD.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: order_identifier
  description: Shopify/brand order name such as DL195092, BHIN2628310, HS98296.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: platform_order_identifier
  description: Shopify internal order id.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: platform_order_name
  description: 'Shopify order name with # prefix.'
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.other_id
  display_name: other_id
  column_name: other_id
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: line_item_identifier
  description: 'Shopify line item id such as #HS98296.2; distinguishes multi-line orders.'
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.other_id_2
  display_name: other_id_2
  column_name: other_id_2
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: line_item_identifier
  description: Composite line item reference.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: fulfillment_state
  description: 'Fulfillment lifecycle value: fulfilled, pending, partial, cancelled, refunded as documented.'
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: fulfillment_state
  description: Order fulfillment state such as fulfilled, partially_fulfilled, unfulfilled.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: fulfillment_state
  description: Current fulfillment state.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.fullfilment_status
  display_name: fullfilment_status
  column_name: fullfilment_status
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: fulfillment_state
  description: Source spelling variant in dedicated doc; preserve spelling.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: payment_state
  description: 'Payment state: paid, pending, partially_paid, refunded, voided.'
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.payment_mode
  display_name: payment_mode
  column_name: payment_mode
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: payment_classifier
  description: Payment method; may contain multiple gateways separated by + with last gateway successful.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: payment_classifier
  description: Detailed payment method string.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: payment_reference
  description: Payment gateway reference number.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: payment_reference
  description: All payment references; can be multiple for partial payments.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: customer_attribute
  description: Customer name.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: customer_attribute
  description: Customer email.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: customer_attribute
  description: Customer phone.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: product_attribute
  description: Brand name.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: product_attribute
  description: Product vendor.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: product_key
  description: Product SKU.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: product_description
  description: Product name/description.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: quantity
  description: Line-item quantity; dedicated doc stores as varchar, cast if needed.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
  cast_required: true
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.mrp
  display_name: mrp
  column_name: mrp
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: amount
  description: Maximum retail price; dedicated doc stores as varchar, TRY_CAST for numeric use.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
  cast_required: true
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.lineitem_price
  display_name: lineitem_price
  column_name: lineitem_price
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: amount
  description: Actual selling price per unit.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: amount
  description: Order value/product price plus tax; dedicated doc stores as varchar, TRY_CAST for aggregation.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
  cast_required: true
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.refunded_amount
  display_name: refunded_amount
  column_name: refunded_amount
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: amount
  description: Refund issued if any; prefer over refunded_amount_1.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
  cast_required: true
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.refunded_amount_1
  display_name: refunded_amount_1
  column_name: refunded_amount_1
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: amount
  description: Alternate refund amount field; prefer refunded_amount when both exist.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
  cast_required: true
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.subtotal
  display_name: subtotal
  column_name: subtotal
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: amount
  description: Order subtotal excluding shipping.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.shipping_amount
  display_name: shipping_amount
  column_name: shipping_amount
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: amount
  description: Shipping charges.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.total_tax
  display_name: total_tax
  column_name: total_tax
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: tax_amount
  description: Total tax collected.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.total_tax_perc
  display_name: total_tax_perc
  column_name: total_tax_perc
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: tax_rate
  description: Tax percentage e.g. 0.18 = 18% GST.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.discount_amount
  display_name: discount_amount
  column_name: discount_amount
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: discount_amount
  description: Discount applied.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: tax_component
  description: First tax component name.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  data_type: decimal
  semantic_role: tax_amount
  description: First tax amount.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_2_name
  display_name: tax_2_name
  column_name: tax_2_name
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: tax_component
  description: Second tax component name.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_2_value
  display_name: tax_2_value
  column_name: tax_2_value
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: tax_amount
  description: Second tax amount.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_3_name
  display_name: tax_3_name
  column_name: tax_3_name
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: tax_component
  description: Third tax component name.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_3_value
  display_name: tax_3_value
  column_name: tax_3_value
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: tax_amount
  description: Third tax amount.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_4_name
  display_name: tax_4_name
  column_name: tax_4_name
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: tax_component
  description: Fourth tax component name.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_4_value
  display_name: tax_4_value
  column_name: tax_4_value
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: tax_amount
  description: Fourth tax amount.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_5_name
  display_name: tax_5_name
  column_name: tax_5_name
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: tax_component
  description: Fifth tax component name.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.tax_5_value
  display_name: tax_5_value
  column_name: tax_5_value
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: tax_amount
  description: Fifth tax amount.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: destination_geography
  description: Shipping city.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: destination_geography
  description: Shipping pincode/zipcode.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: destination_geography
  description: Shipping state/province code.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: channel_source
  description: Shopify channel source ID.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: order_tags
  description: Shopify order tags such as CPD, GoKwik, Fastrr.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: order_metadata
  description: Notes containing cart tokens, UTM params or checkout-provider refs.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: risk_signal
  description: Shopify fraud risk level.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: date_string
  description: Order creation date; dedicated doc says varchar, cast for date operations.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
  cast_required: true
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.fulfilled_at
  display_name: fulfilled_at
  column_name: fulfilled_at
  table_id: table.zs_observe.shopify_oms
  data_type: timestamp
  semantic_role: event_timestamp
  description: Fulfillment timestamp.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.cancellation_date
  display_name: cancellation_date
  column_name: cancellation_date
  table_id: table.zs_observe.shopify_oms
  data_type: varchar
  semantic_role: date_string
  description: Date cancelled if applicable.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
  cast_required: true
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.outstanding_balance
  display_name: outstanding_balance
  column_name: outstanding_balance
  table_id: table.zs_observe.shopify_oms
  data_type: decimal
  semantic_role: amount
  description: Amount still owed for COD/partial payment.
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.schema.extended.001
  - ev.shopify.data_quality.001
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
  semantic_role: order_identifier
  description: Original Shopify order name.
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: refund_transaction_id
  description: Shopify refund transaction id.
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: payment_gateway_label
  description: Gateway used for refund; label only, not account card.
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: refund_status
  description: 'Refund gateway transaction status: success, pending, failure.'
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: payment_status
  description: 'Final order payment status: paid, refunded, partially_refunded.'
  evidence_refs:
  - ev.shopify.returns.001
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
  data_type: decimal
  semantic_role: amount
  description: Total amount refunded.
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: date
  description: Original order date.
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: refund_reference
  description: Return/refund reference id from gateway.
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: currency
  description: Currency; GBP for UK examples.
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: source_sheet
  description: Source sheet name, shopify returns.
  evidence_refs:
  - ev.shopify.returns.001
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
  semantic_role: shipment_order_reference
  description: Shiprocket order_id with Shopify order prefix plus -s suffix.
  evidence_refs:
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_oms.awb_code
  display_name: awb_code
  column_name: awb_code
  table_id: table.zs_observe.shiprocket_oms
  data_type: varchar
  semantic_role: awb_reference
  description: AWB tracking code from Shiprocket.
  evidence_refs:
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_oms.courier_company
  display_name: courier_company
  column_name: courier_company
  table_id: table.zs_observe.shiprocket_oms
  data_type: varchar
  semantic_role: courier_label
  description: Courier company label only; do not create courier account card.
  evidence_refs:
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
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
  description: Active row flag for join pattern.
  evidence_refs:
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x relationship

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shopify_oms_to_shiprocket_oms.order_id_suffix
  display_name: Shopify order to Shiprocket shipment
  from_table: table.zs_observe.shopify_oms
  to_table: table.zs_observe.shiprocket_oms
  join_keys:
  - sr.order_id LIKE CONCAT(s.order_id, '-%')
  relationship_grain: Shopify order/order-line to downstream shipment rows
  join_safety_rule: Filter both s.is_active=true and sr.is_active=true; aggregate Shopify to order_id before shipment-level
    joins when computing order value.
  business_semantics: Operational shipment linkage only; not a courier settlement or account binding.
  evidence_refs:
  - ev.shopify.shiprocket_join.001
  - ev.shopify.order_grain.001
  confidence: high
  review_status: accepted
  create_action: create_reference_relationship
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shopify_oms_to_shopify_returns.order_name
  display_name: Shopify order to Shopify return/refund event
  from_table: table.zs_observe.shopify_oms
  to_table: table.zs_observe.shopify_returns
  join_keys:
  - 'shopify_returns.order_name = shopify_oms.order_id OR shopify_returns.order_name = shopify_oms.name after # normalization'
  relationship_grain: Order to refund transaction events
  join_safety_rule: 'Normalize # prefixes and aggregate refunds by order_name before joining to order lines.'
  business_semantics: Refund tracking back to original Shopify order.
  evidence_refs:
  - ev.shopify.returns.001
  - ev.shopify.order_grain.001
  confidence: medium
  review_status: accepted_with_normalization_caveat
  create_action: create
```
### 3.x value_profile

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.financial_status
  display_name: financial status
  table_id: table.zs_observe.shopify_oms
  column_names:
  - financial_status
  values_or_known_values:
  - value: paid
    meaning: Prepaid / digital payment collected
  - value: pending
    meaning: COD cash not yet collected / remitted
  - value: partially_paid
    meaning: PPCOD partial prepaid plus COD balance
  - value: voided
    meaning: Cancelled before shipment
  - value: refunded
    meaning: Refunded payment state
  evidence_refs:
  - ev.shopify.financial_status.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.transaction_type
  display_name: transaction type
  table_id: table.zs_observe.shopify_oms
  column_names:
  - transaction_type
  values_or_known_values:
  - value: fulfilled
    meaning: Order shipped and fulfilled
  - value: pending
    meaning: Placed but not shipped
  - value: partial
    meaning: Some lines fulfilled, some pending
  - value: cancelled/refunded
    meaning: Lifecycle labels from OMS KB
  evidence_refs:
  - ev.shopify.lifecycle.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.payment_mode
  display_name: payment mode
  table_id: table.zs_observe.shopify_oms
  column_names:
  - payment_mode
  values_or_known_values:
  - value: cash_on_delivery
    meaning: COD order
  - value: Gokwik UPI
    meaning: Prepaid UPI via GoKwik
  - value: Gokwik PPCOD
    meaning: Partial prepaid + COD balance
  - value: Gokwik Cards
    meaning: Prepaid card via GoKwik
  - value: gateway1+gateway2
    meaning: When separated by +, last gateway is successful payment
  evidence_refs:
  - ev.shopify.payment_mode.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.group_level_id
  display_name: group level id
  table_id: table.zs_observe.shopify_oms
  column_names:
  - group_level_id
  values_or_known_values:
  - value: '22'
    meaning: Documented Shopify table scope value; scope column only
  evidence_refs:
  - ev.shopify.schema.oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.order_prefixes
  display_name: order prefixes
  table_id: table.zs_observe.shopify_oms
  column_names:
  - order_id
  values_or_known_values:
  - prefix: DL
    meaning: Delhi/specific brand prefix
  - prefix: BHIN
    meaning: Bharat/pan-India brand prefix
  - prefix: HS
    meaning: HealthStore/brand prefix
  evidence_refs:
  - ev.shopify.order_grain.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shopify.return_statuses
  display_name: return statuses
  table_id: table.zs_observe.shopify_returns
  column_names:
  - transaction_status
  - order_payment_status
  values_or_known_values:
  - value: success/pending/failure
    meaning: Refund transaction status
  - value: paid/refunded/partially_refunded
    meaning: Order payment status after return/refund
  evidence_refs:
  - ev.shopify.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x metric

```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.order_count
  display_name: Order Count
  metric_key: order_count
  business_definition: Distinct Shopify order count.
  default_grain: order
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.line_item_count
  display_name: Line Item Count
  metric_key: line_item_count
  business_definition: Count of Shopify line-item rows.
  default_grain: order_line
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.gross_gmv
  display_name: Gross Gmv
  metric_key: gross_gmv
  business_definition: Total Shopify order value after casting charged_amount.
  default_grain: order_line
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.order_level_gmv
  display_name: Order Level Gmv
  metric_key: order_level_gmv
  business_definition: GMV aggregated to order_id grain to avoid multi-line duplication.
  default_grain: order
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.average_order_value
  display_name: Average Order Value
  metric_key: average_order_value
  business_definition: Order-level GMV divided by distinct order count.
  default_grain: order
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.refunded_value
  display_name: Refunded Value
  metric_key: refunded_value
  business_definition: Total refunded amount using preferred refunded_amount field.
  default_grain: order
  evidence_refs:
  - ev.shopify.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.net_gmv
  display_name: Net Gmv
  metric_key: net_gmv
  business_definition: Gross GMV less refunded value.
  default_grain: order
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.cod_order_count
  display_name: Cod Order Count
  metric_key: cod_order_count
  business_definition: Distinct orders with financial_status=pending or payment_mode cash_on_delivery.
  default_grain: order
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.prepaid_order_count
  display_name: Prepaid Order Count
  metric_key: prepaid_order_count
  business_definition: Distinct orders with financial_status=paid.
  default_grain: order
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.ppcod_order_count
  display_name: Ppcod Order Count
  metric_key: ppcod_order_count
  business_definition: Distinct orders with financial_status=partially_paid or GoKwik PPCOD payment mode.
  default_grain: order
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.tax_collected
  display_name: Tax Collected
  metric_key: tax_collected
  business_definition: Total tax collected from total_tax or component tax fields.
  default_grain: order_line
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.outstanding_balance
  display_name: Outstanding Balance
  metric_key: outstanding_balance
  business_definition: Outstanding COD/partial balance still owed.
  default_grain: order
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shopify.refund_success_rate
  display_name: Refund Success Rate
  metric_key: refund_success_rate
  business_definition: Successful refund events divided by refund transaction events.
  default_grain: refund_event
  evidence_refs:
  - ev.shopify.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x metric_implementation

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.order_count
  display_name: Shopify order_count implementation
  metric_id: metric.shopify.order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.order_count
  sql_reference_id: sql.shopify.metric.order_count
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.line_item_count
  display_name: Shopify line_item_count implementation
  metric_id: metric.shopify.line_item_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.line_item_count
  sql_reference_id: sql.shopify.metric.line_item_count
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.gross_gmv
  display_name: Shopify gross_gmv implementation
  metric_id: metric.shopify.gross_gmv
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.gross_gmv
  sql_reference_id: sql.shopify.metric.gross_gmv
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.order_level_gmv
  display_name: Shopify order_level_gmv implementation
  metric_id: metric.shopify.order_level_gmv
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.order_level_gmv
  sql_reference_id: sql.shopify.metric.order_level_gmv
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.average_order_value
  display_name: Shopify average_order_value implementation
  metric_id: metric.shopify.average_order_value
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.average_order_value
  sql_reference_id: sql.shopify.metric.average_order_value
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.refunded_value
  display_name: Shopify refunded_value implementation
  metric_id: metric.shopify.refunded_value
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.refunded_value
  sql_reference_id: sql.shopify.metric.refunded_value
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.net_gmv
  display_name: Shopify net_gmv implementation
  metric_id: metric.shopify.net_gmv
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.net_gmv
  sql_reference_id: sql.shopify.metric.net_gmv
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.cod_order_count
  display_name: Shopify cod_order_count implementation
  metric_id: metric.shopify.cod_order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.cod_order_count
  sql_reference_id: sql.shopify.metric.cod_order_count
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.prepaid_order_count
  display_name: Shopify prepaid_order_count implementation
  metric_id: metric.shopify.prepaid_order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.prepaid_order_count
  sql_reference_id: sql.shopify.metric.prepaid_order_count
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.ppcod_order_count
  display_name: Shopify ppcod_order_count implementation
  metric_id: metric.shopify.ppcod_order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.ppcod_order_count
  sql_reference_id: sql.shopify.metric.ppcod_order_count
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.tax_collected
  display_name: Shopify tax_collected implementation
  metric_id: metric.shopify.tax_collected
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.tax_collected
  sql_reference_id: sql.shopify.metric.tax_collected
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.outstanding_balance
  display_name: Shopify outstanding_balance implementation
  metric_id: metric.shopify.outstanding_balance
  source_table_ids:
  - table.zs_observe.shopify_oms
  formula: See sql.shopify.metric.outstanding_balance
  sql_reference_id: sql.shopify.metric.outstanding_balance
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.shopify.refund_success_rate
  display_name: Shopify refund_success_rate implementation
  metric_id: metric.shopify.refund_success_rate
  source_table_ids:
  - table.zs_observe.shopify_returns
  formula: See sql.shopify.metric.refund_success_rate
  sql_reference_id: sql.shopify.metric.refund_success_rate
  required_filters:
  - is_active = true
  - TRY_CAST varchar amount fields before financial aggregation
  grain: order_or_order_line
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x rule

```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.is_active_filter
  display_name: is active filter
  rule_text: All production Shopify OMS queries must filter is_active = true.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.schema.oms.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.varchar_amount_cast
  display_name: varchar amount cast
  rule_text: charged_amount, refunded_amount, mrp and quantity are varchar in the dedicated Shopify doc; use TRY_CAST before
    aggregation.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.multi_line_order_grain
  display_name: multi line order grain
  rule_text: Multi-item orders repeat order_id; use other_id for line items and aggregate by order_id for order-level GMV/AOV.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.order_grain.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.payment_mode_last_gateway
  display_name: payment mode last gateway
  rule_text: When payment_mode contains gateway names separated by +, treat the last gateway value as the successful payment.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.payment_mode.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.cod_pending_semantics
  display_name: cod pending semantics
  rule_text: COD orders may remain financial_status=pending even after delivery/remittance; do not treat pending as failed
    payment.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.financial_status.001
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.refund_field_preference
  display_name: refund field preference
  rule_text: Prefer refunded_amount over refunded_amount_1 for refund-value analytics when both exist.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.group_level_scope_column_only
  display_name: group level scope column only
  rule_text: group_level_id=22 is a documented source scope value; keep it as a column/filter, not tenant or account card.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.schema.oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.shiprocket_reference_only
  display_name: shiprocket reference only
  rule_text: Shiprocket linkage is operational relationship only; do not create courier account, courier invoice, or courier
    settlement cards in this Shopify OMS file.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.shopify.pg_refs_not_accounts
  display_name: pg refs not accounts
  rule_text: payment_id, payment_references and payment_gateway labels are references/labels only; actual payment-gateway
    account binding is external.
  rule_scope: shopify_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.returns.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x business_process

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.order_capture
  display_name: Shopify OMS order capture
  domain_id: domain.shopify.d2c_order_capture
  process_summary: Customer order appears in zs_observe.shopify_oms at order-line grain with order_id, other_id, sku_id, charged_amount
    and payment/fulfillment status.
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.lifecycle.001
  - ev.shopify.returns.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.payment_state_classification
  display_name: Shopify payment state classification
  domain_id: domain.shopify.d2c_order_capture
  process_summary: financial_status and payment_mode classify prepaid, COD and PPCOD behavior using documented values.
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.lifecycle.001
  - ev.shopify.returns.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.fulfillment_lifecycle
  display_name: Shopify fulfillment lifecycle
  domain_id: domain.shopify.d2c_order_capture
  process_summary: transaction_type/order_status/fulfillment_status represent fulfilled, pending, partial and unfulfilled
    lifecycle state.
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.lifecycle.001
  - ev.shopify.returns.001
  - ev.shopify.shiprocket_join.001
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
  process_summary: shopify_returns records refund transaction_id, payment_gateway, transaction_status, refunded_payments and
    original order_name.
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.lifecycle.001
  - ev.shopify.returns.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shopify.shiprocket_operational_link
  display_name: Shopify to Shiprocket operational link
  domain_id: domain.shopify.d2c_order_capture
  process_summary: Shopify order_id links to Shiprocket order_id suffix for shipment context with active filters.
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.lifecycle.001
  - ev.shopify.returns.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x workflow_step

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.order_capture.01_order_line_created
  display_name: 01_order_line_created
  business_process_id: business_process.shopify.order_capture
  step_order: 1
  step_description: Order line appears in zs_observe.shopify_oms with order_id, other_id, sku_id and source row identifiers.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.order_capture.02_amounts_recorded
  display_name: 02_amounts_recorded
  business_process_id: business_process.shopify.order_capture
  step_order: 2
  step_description: charged_amount/refunded_amount/mrp/quantity are recorded as source varchar fields and cast for financial
    metrics.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.payment_state.01_status_mapped
  display_name: 01_status_mapped
  business_process_id: business_process.shopify.payment_state_classification
  step_order: 1
  step_description: financial_status paid/pending/partially_paid/voided maps to prepaid/COD/PPCOD/cancelled interpretation.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.payment_state.02_gateway_ref_recorded
  display_name: 02_gateway_ref_recorded
  business_process_id: business_process.shopify.payment_state_classification
  step_order: 2
  step_description: payment_id/payment_references/payment_mode note payment references and gateway labels without creating
    PG account cards.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.fulfillment.01_transaction_type_state
  display_name: 01_transaction_type_state
  business_process_id: business_process.shopify.fulfillment_lifecycle
  step_order: 1
  step_description: transaction_type fulfilled/pending/partial captures Shopify fulfillment lifecycle state.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.shiprocket_join.001
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
  step_description: shopify_returns captures transaction_id, payment_gateway, transaction_status and refunded_payments for
    refund event.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shopify.shiprocket.01_suffix_join
  display_name: 01_suffix_join
  business_process_id: business_process.shopify.shiprocket_operational_link
  step_order: 1
  step_description: Shiprocket shipment is linked by sr.order_id LIKE CONCAT(shopify_oms.order_id, '-%') with active filters.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.shopify.order_grain.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x state_transition

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.shopify.financial_status.pending_to_paid
  display_name: pending_to_paid
  state_column: column.zs_observe.shopify_oms.financial_status
  from_state: pending
  to_state: paid
  transition_meaning: COD/pending to paid/remitted interpretation may happen outside Shopify; treat cautiously.
  evidence_refs:
  - ev.shopify.financial_status.001
  - ev.shopify.lifecycle.001
  confidence: medium
  review_status: accepted_with_caveat
  create_action: create
```
```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.shopify.financial_status.paid_to_refunded
  display_name: paid_to_refunded
  state_column: column.zs_observe.shopify_oms.financial_status
  from_state: paid
  to_state: refunded
  transition_meaning: Paid order becomes refunded after return/refund processing.
  evidence_refs:
  - ev.shopify.financial_status.001
  - ev.shopify.lifecycle.001
  confidence: medium
  review_status: accepted_with_caveat
  create_action: create
```
```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.shopify.transaction_type.pending_to_fulfilled
  display_name: pending_to_fulfilled
  state_column: column.zs_observe.shopify_oms.transaction_type
  from_state: pending
  to_state: fulfilled
  transition_meaning: Order progresses from placed/unshipped to shipped/fulfilled.
  evidence_refs:
  - ev.shopify.financial_status.001
  - ev.shopify.lifecycle.001
  confidence: medium
  review_status: accepted_with_caveat
  create_action: create
```
### 3.x reconciliation_profile

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.shopify.oms_to_pg_settlement
  display_name: Shopify OMS to payment gateway settlement
  expected_side: Shopify charged_amount/payment_id/payment_references/order_id
  actual_side: External PG settlement files such as Cashfree, Razorpay or Shopify Payments
  unit: order_or_refund_event
  matching_logic: order_id + payment_id/payment_references + amount + date
  reconciliation_scope: documented as use case; external actual table binding remains runtime/review
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.returns.001
  confidence: medium
  review_status: accepted_with_external_runtime_scope
  create_action: create
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.shopify.cod_remittance
  display_name: Shopify COD remittance expectation
  expected_side: COD/PPCOD orders from financial_status/payment_mode and outstanding_balance
  actual_side: COD remittance/courier/aggregator settlement source external to this file
  unit: order_or_refund_event
  matching_logic: order_id + COD amount + remittance period
  reconciliation_scope: documented as use case; external actual table binding remains runtime/review
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.returns.001
  confidence: medium
  review_status: accepted_with_external_runtime_scope
  create_action: create
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.shopify.refund_to_gateway
  display_name: Shopify refund to gateway credit
  expected_side: shopify_returns.refunded_payments and transaction_status
  actual_side: Gateway refund/settlement credit external to this file
  unit: order_or_refund_event
  matching_logic: order_name/transaction_id/other_id + refund amount
  reconciliation_scope: documented as use case; external actual table binding remains runtime/review
  evidence_refs:
  - ev.shopify.tax_recon.001
  - ev.shopify.returns.001
  confidence: medium
  review_status: accepted_with_external_runtime_scope
  create_action: create
```
### 3.x query_pattern

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.shopify.gmv_by_payment_mode
  display_name: gmv_by_payment_mode
  natural_language_patterns:
  - GMV by payment mode
  - Show COD vs prepaid GMV
  primary_metric: metric.shopify.gross_gmv
  source_table_ids:
  - table.zs_observe.shopify_oms
  sql_reference_id: sql.shopify.query.gmv_by_payment_mode
  output_contract_id: output_contract.shopify.standard_metric_result
  required_rules:
  - rule.shopify.is_active_filter
  - rule.shopify.varchar_amount_cast
  - rule.shopify.multi_line_order_grain
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.shopify.cod_share
  display_name: cod_share
  natural_language_patterns:
  - COD share
  - How many Shopify orders are COD?
  primary_metric: metric.shopify.cod_order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  sql_reference_id: sql.shopify.query.cod_share
  output_contract_id: output_contract.shopify.standard_metric_result
  required_rules:
  - rule.shopify.is_active_filter
  - rule.shopify.varchar_amount_cast
  - rule.shopify.multi_line_order_grain
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.shopify.ppcod_orders
  display_name: ppcod_orders
  natural_language_patterns:
  - PPCOD orders
  - Partially paid orders
  primary_metric: metric.shopify.ppcod_order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  sql_reference_id: sql.shopify.query.ppcod_orders
  output_contract_id: output_contract.shopify.standard_metric_result
  required_rules:
  - rule.shopify.is_active_filter
  - rule.shopify.varchar_amount_cast
  - rule.shopify.multi_line_order_grain
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.shiprocket_join.001
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
  - Refund success rate
  - Shopify refund status summary
  primary_metric: metric.shopify.refund_success_rate
  source_table_ids:
  - table.zs_observe.shopify_returns
  sql_reference_id: sql.shopify.query.refund_events
  output_contract_id: output_contract.shopify.standard_metric_result
  required_rules:
  - rule.shopify.is_active_filter
  - rule.shopify.varchar_amount_cast
  - rule.shopify.multi_line_order_grain
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.shiprocket_join.001
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
  - Join Shopify to Shiprocket
  - Orders with AWB
  primary_metric: metric.shopify.order_count
  source_table_ids:
  - table.zs_observe.shopify_oms
  - table.zs_observe.shiprocket_oms
  sql_reference_id: sql.shopify.query.shiprocket_link
  output_contract_id: output_contract.shopify.standard_metric_result
  required_rules:
  - rule.shopify.is_active_filter
  - rule.shopify.varchar_amount_cast
  - rule.shopify.multi_line_order_grain
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.shiprocket_join.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x validation_test

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.no_dangling_sql_refs
  display_name: no_dangling_sql_refs
  assertion: Every metric_implementation and query_pattern sql_reference_id has a SQL pattern block.
  related_ids:
  - table.zs_observe.shopify_oms
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.schema.oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.cast_amount_fields
  display_name: cast_amount_fields
  assertion: Financial aggregation over charged_amount/refunded_amount/mrp/quantity uses TRY_CAST because source type is varchar.
  related_ids:
  - table.zs_observe.shopify_oms
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.schema.oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.active_filter
  display_name: active_filter
  assertion: Shopify OMS query patterns include s.is_active = true.
  related_ids:
  - table.zs_observe.shopify_oms
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.schema.oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.group_scope_not_account
  display_name: group_scope_not_account
  assertion: group_level_id remains a scope/filter column, not a tenant/account card.
  related_ids:
  - table.zs_observe.shopify_oms
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.schema.oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.shopify.shiprocket_reference_only
  display_name: shiprocket_reference_only
  assertion: Shiprocket relationship does not create courier account or logistics settlement cards.
  related_ids:
  - table.zs_observe.shopify_oms
  evidence_refs:
  - ev.shopify.data_quality.001
  - ev.shopify.schema.oms.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x output_contract

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.shopify.standard_metric_result
  display_name: Shopify standard metric output
  contract_type: metric_result
  output_columns:
  - metric_name
  - metric_value
  - grain
  - date_range_or_runtime_scope
  - applied_filters
  evidence_refs:
  - ev.shopify.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.shopify.reconciliation_result
  display_name: Shopify reconciliation output
  contract_type: reconciliation_result
  output_columns:
  - reconciliation_profile
  - expected_id
  - actual_id
  - expected_amount
  - actual_amount
  - variance
  - status
  - notes
  evidence_refs:
  - ev.shopify.tax_recon.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x review_item

```yaml
candidate_card:
  card_type: review_item
  card_id: review.shopify.external_pg_settlement_table_binding
  display_name: External PG settlement source binding
  issue_type: external_runtime_scope
  question: Which exact payment gateway settlement table(s) should be bound for Shopify-to-PG reconciliation for a tenant/runtime
    scope?
  status: open
  blocking_for_core_oms_cards: false
  evidence_refs:
  - ev.shopify.tax_recon.001
  confidence: high
```
```yaml
candidate_card:
  card_type: review_item
  card_id: review.shopify.refund_order_name_normalization
  display_name: Refund order_name normalization
  issue_type: normalization_choice
  question: 'Confirm whether shopify_returns.order_name always matches shopify_oms.order_id, shopify_oms.name with # prefix,
    or requires brand-specific normalization.'
  status: open
  blocking_for_core_oms_cards: false
  evidence_refs:
  - ev.shopify.returns.001
```
## 4. Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.unique_id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.unique_id
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.zen_status
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.zen_status
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.other_id
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.other_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.other_id_2
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.other_id_2
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.fullfilment_status
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.fullfilment_status
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.vendor
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.vendor
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.refunded_amount
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.refunded_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.refunded_amount_1
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.refunded_amount_1
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_2_name
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_2_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_2_value
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_2_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_3_name
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_3_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_3_value
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_3_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_4_name
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_4_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_4_value
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_4_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_5_name
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_5_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.tax_5_value
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.tax_5_value
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.source
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.source
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.note_attributes
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.note_attributes
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.created_date
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.created_date
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
  edge_id: edge.table.zs_observe.shopify_oms.has_column.cancellation_date
  source_id: table.zs_observe.shopify_oms
  target_id: column.zs_observe.shopify_oms.cancellation_date
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
  edge_id: edge.table.zs_observe.shopify_returns.has_column.currency_type
  source_id: table.zs_observe.shopify_returns
  target_id: column.zs_observe.shopify_returns.currency_type
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
  edge_id: edge.relationship.shopify_oms_to_shiprocket_oms.order_id_suffix.from.table.zs_observe.shopify_oms
  source_id: relationship.shopify_oms_to_shiprocket_oms.order_id_suffix
  target_id: table.zs_observe.shopify_oms
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shopify_oms_to_shiprocket_oms.order_id_suffix.to.table.zs_observe.shiprocket_oms
  source_id: relationship.shopify_oms_to_shiprocket_oms.order_id_suffix
  target_id: table.zs_observe.shiprocket_oms
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shopify_oms_to_shopify_returns.order_name.from.table.zs_observe.shopify_oms
  source_id: relationship.shopify_oms_to_shopify_returns.order_name
  target_id: table.zs_observe.shopify_oms
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shopify_oms_to_shopify_returns.order_name.to.table.zs_observe.shopify_returns
  source_id: relationship.shopify_oms_to_shopify_returns.order_name
  target_id: table.zs_observe.shopify_returns
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.order_count.implements.metric.shopify.order_count
  source_id: metric_implementation.shopify.order_count
  target_id: metric.shopify.order_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.line_item_count.implements.metric.shopify.line_item_count
  source_id: metric_implementation.shopify.line_item_count
  target_id: metric.shopify.line_item_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.gross_gmv.implements.metric.shopify.gross_gmv
  source_id: metric_implementation.shopify.gross_gmv
  target_id: metric.shopify.gross_gmv
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.order_level_gmv.implements.metric.shopify.order_level_gmv
  source_id: metric_implementation.shopify.order_level_gmv
  target_id: metric.shopify.order_level_gmv
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.average_order_value.implements.metric.shopify.average_order_value
  source_id: metric_implementation.shopify.average_order_value
  target_id: metric.shopify.average_order_value
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.refunded_value.implements.metric.shopify.refunded_value
  source_id: metric_implementation.shopify.refunded_value
  target_id: metric.shopify.refunded_value
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.net_gmv.implements.metric.shopify.net_gmv
  source_id: metric_implementation.shopify.net_gmv
  target_id: metric.shopify.net_gmv
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.cod_order_count.implements.metric.shopify.cod_order_count
  source_id: metric_implementation.shopify.cod_order_count
  target_id: metric.shopify.cod_order_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.prepaid_order_count.implements.metric.shopify.prepaid_order_count
  source_id: metric_implementation.shopify.prepaid_order_count
  target_id: metric.shopify.prepaid_order_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.ppcod_order_count.implements.metric.shopify.ppcod_order_count
  source_id: metric_implementation.shopify.ppcod_order_count
  target_id: metric.shopify.ppcod_order_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.tax_collected.implements.metric.shopify.tax_collected
  source_id: metric_implementation.shopify.tax_collected
  target_id: metric.shopify.tax_collected
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.outstanding_balance.implements.metric.shopify.outstanding_balance
  source_id: metric_implementation.shopify.outstanding_balance
  target_id: metric.shopify.outstanding_balance
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.shopify.refund_success_rate.implements.metric.shopify.refund_success_rate
  source_id: metric_implementation.shopify.refund_success_rate
  target_id: metric.shopify.refund_success_rate
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.order_capture.has_step.01_order_line_created
  source_id: business_process.shopify.order_capture
  target_id: workflow_step.shopify.order_capture.01_order_line_created
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.order_capture.has_step.02_amounts_recorded
  source_id: business_process.shopify.order_capture
  target_id: workflow_step.shopify.order_capture.02_amounts_recorded
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.payment_state_classification.has_step.01_status_mapped
  source_id: business_process.shopify.payment_state_classification
  target_id: workflow_step.shopify.payment_state.01_status_mapped
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.payment_state_classification.has_step.02_gateway_ref_recorded
  source_id: business_process.shopify.payment_state_classification
  target_id: workflow_step.shopify.payment_state.02_gateway_ref_recorded
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.fulfillment_lifecycle.has_step.01_transaction_type_state
  source_id: business_process.shopify.fulfillment_lifecycle
  target_id: workflow_step.shopify.fulfillment.01_transaction_type_state
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.refund_event_capture.has_step.01_refund_event
  source_id: business_process.shopify.refund_event_capture
  target_id: workflow_step.shopify.refund.01_refund_event
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.shopify.shiprocket_operational_link.has_step.01_suffix_join
  source_id: business_process.shopify.shiprocket_operational_link
  target_id: workflow_step.shopify.shiprocket.01_suffix_join
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.gmv_by_payment_mode.answers.metric.shopify.gross_gmv
  source_id: query_pattern.shopify.gmv_by_payment_mode
  target_id: metric.shopify.gross_gmv
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.cod_share.answers.metric.shopify.cod_order_count
  source_id: query_pattern.shopify.cod_share
  target_id: metric.shopify.cod_order_count
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.ppcod_orders.answers.metric.shopify.ppcod_order_count
  source_id: query_pattern.shopify.ppcod_orders
  target_id: metric.shopify.ppcod_order_count
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.refund_events.answers.metric.shopify.refund_success_rate
  source_id: query_pattern.shopify.refund_events
  target_id: metric.shopify.refund_success_rate
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.shopify.shiprocket_link.answers.metric.shopify.order_count
  source_id: query_pattern.shopify.shiprocket_link
  target_id: metric.shopify.order_count
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
## 5. SQL Pattern Registry

```yaml
sql_pattern:
  sql_id: sql.shopify.metric.order_count
  title: shopify metric order_count
  evidence_refs: []
  sql: |
    SELECT COUNT(DISTINCT order_id) AS order_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.line_item_count
  title: shopify metric line_item_count
  evidence_refs: []
  sql: |
    SELECT COUNT(*) AS line_item_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.gross_gmv
  title: shopify metric gross_gmv
  evidence_refs: []
  sql: |
    SELECT SUM(TRY_CAST(charged_amount AS DOUBLE)) AS gross_gmv
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.order_level_gmv
  title: shopify metric order_level_gmv
  evidence_refs: []
  sql: |
    WITH order_value AS (
      SELECT order_id, SUM(TRY_CAST(charged_amount AS DOUBLE)) AS order_gmv
      FROM zs_observe.shopify_oms
      WHERE is_active = true
      GROUP BY order_id
    )
    SELECT SUM(order_gmv) AS order_level_gmv FROM order_value;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.average_order_value
  title: shopify metric average_order_value
  evidence_refs: []
  sql: |
    WITH order_value AS (
      SELECT order_id, SUM(TRY_CAST(charged_amount AS DOUBLE)) AS order_gmv
      FROM zs_observe.shopify_oms
      WHERE is_active = true
      GROUP BY order_id
    )
    SELECT AVG(order_gmv) AS average_order_value FROM order_value;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.refunded_value
  title: shopify metric refunded_value
  evidence_refs: []
  sql: |
    SELECT SUM(TRY_CAST(refunded_amount AS DOUBLE)) AS refunded_value
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.net_gmv
  title: shopify metric net_gmv
  evidence_refs: []
  sql: |
    SELECT SUM(TRY_CAST(charged_amount AS DOUBLE)) - SUM(COALESCE(TRY_CAST(refunded_amount AS DOUBLE),0)) AS net_gmv
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.cod_order_count
  title: shopify metric cod_order_count
  evidence_refs: []
  sql: |
    SELECT COUNT(DISTINCT order_id) AS cod_order_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true
      AND (financial_status = 'pending' OR payment_mode = 'cash_on_delivery');
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.prepaid_order_count
  title: shopify metric prepaid_order_count
  evidence_refs: []
  sql: |
    SELECT COUNT(DISTINCT order_id) AS prepaid_order_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true AND financial_status = 'paid';
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.ppcod_order_count
  title: shopify metric ppcod_order_count
  evidence_refs: []
  sql: |
    SELECT COUNT(DISTINCT order_id) AS ppcod_order_count
    FROM zs_observe.shopify_oms
    WHERE is_active = true
      AND (financial_status = 'partially_paid' OR payment_mode LIKE '%PPCOD%');
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.tax_collected
  title: shopify metric tax_collected
  evidence_refs: []
  sql: |
    SELECT SUM(COALESCE(total_tax, tax_1_value + tax_2_value + tax_3_value + tax_4_value + tax_5_value, 0)) AS tax_collected
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.outstanding_balance
  title: shopify metric outstanding_balance
  evidence_refs: []
  sql: |
    SELECT SUM(outstanding_balance) AS outstanding_balance
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.metric.refund_success_rate
  title: shopify metric refund_success_rate
  evidence_refs: []
  sql: |
    SELECT 100.0 * COUNT_IF(transaction_status = 'success') / NULLIF(COUNT(*),0) AS refund_success_rate_pct
    FROM zs_observe.shopify_returns
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.gmv_by_payment_mode
  title: shopify query gmv_by_payment_mode
  evidence_refs: []
  sql: |
    SELECT payment_mode, COUNT(DISTINCT order_id) AS orders, SUM(TRY_CAST(charged_amount AS DOUBLE)) AS gmv
    FROM zs_observe.shopify_oms
    WHERE is_active = true
    GROUP BY payment_mode
    ORDER BY gmv DESC;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.cod_share
  title: shopify query cod_share
  evidence_refs: []
  sql: |
    SELECT
      COUNT(DISTINCT CASE WHEN financial_status='pending' OR payment_mode='cash_on_delivery' THEN order_id END) AS cod_orders,
      COUNT(DISTINCT order_id) AS total_orders,
      100.0 * COUNT(DISTINCT CASE WHEN financial_status='pending' OR payment_mode='cash_on_delivery' THEN order_id END) / NULLIF(COUNT(DISTINCT order_id),0) AS cod_share_pct
    FROM zs_observe.shopify_oms
    WHERE is_active = true;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.ppcod_orders
  title: shopify query ppcod_orders
  evidence_refs: []
  sql: |
    SELECT order_id, payment_mode, financial_status, outstanding_balance, SUM(TRY_CAST(charged_amount AS DOUBLE)) AS order_value
    FROM zs_observe.shopify_oms
    WHERE is_active = true
      AND (financial_status='partially_paid' OR payment_mode LIKE '%PPCOD%')
    GROUP BY order_id, payment_mode, financial_status, outstanding_balance;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.refund_events
  title: shopify query refund_events
  evidence_refs: []
  sql: |
    SELECT transaction_status, order_payment_status, COUNT(*) AS refund_events, SUM(refunded_payments) AS refunded_payments
    FROM zs_observe.shopify_returns
    WHERE is_active = true
    GROUP BY transaction_status, order_payment_status;
```
```yaml
sql_pattern:
  sql_id: sql.shopify.query.shiprocket_link
  title: shopify query shiprocket_link
  evidence_refs: []
  sql: |
    SELECT s.order_id, SUM(TRY_CAST(s.charged_amount AS DOUBLE)) AS shopify_value, sr.awb_code, sr.courier_company
    FROM zs_observe.shopify_oms s
    JOIN zs_observe.shiprocket_oms sr
      ON sr.order_id LIKE CONCAT(s.order_id, '-%')
    WHERE s.is_active = true AND sr.is_active = true
    GROUP BY s.order_id, sr.awb_code, sr.courier_company;
```
## 6. Parser QA Summary

```yaml
parser_quality_manifest:
  candidate_cards: 169
  candidate_edges: 112
  source_evidence_count: 12
  sql_patterns: 18
  missing_edge_references: 0
  dangling_sql_refs: 0
  deleted_card_references: 0
  open_reviews: 2
  lazy_workflow_steps: 0
  placeholder_metric_formulas: 0
  unsupported_metric_implementations: 0
  process_variants_review_required: 0
  unresolved_benchmark_reviews_without_reason: 0
  hard_threshold_benchmarks_without_rule: 0
  forbidden_scope_cards_from_scope_ids: 0
```

## 7. Deterministic Cleanup Notes

- Evidence anchoring is required before card creation.
- Value labels must not become process variants unless an explicit workflow difference is documented.
- All metric implementations are SQL-like and reference declared source tables/columns.
- Scope identifiers remain scope columns/caveats only.
