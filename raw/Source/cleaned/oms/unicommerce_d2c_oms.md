# Unicommerce D2C OMS Gold Standard Markdown
```yaml
document_metadata:
  document_id: unicommerce_d2c_oms_gold_standard_v2_process_corrected
  system: Unicommerce
  source_docx:
  - /mnt/data/Unicommerce Recon KB.docx
  - /mnt/data/OMS-Business Knowledge Base.docx
  cleanup_manifest: /mnt/data/marketplace_cleanup_manifest_consolidated_v2.md
  structure_reference: /mnt/data/amazon_marketplace.md
  generated_on: '2026-05-24'
  scope: D2C OMS canonical markdown for brands using Unicommerce directly; includes invoice table and directly documented
    OSR shipment complement
  process_correction:
    corrected_on: '2026-05-24'
    correction_reason: User-confirmed Unicommerce lifecycle process IDs must map to source sections 9.1 Forward Sale, 9.2 Return-to-Origin, 9.3 Customer Return, and 9.4 Cancellation.
    corrected_process_ids:
    - business_process.unicommerce.9_1_forward_sale
    - business_process.unicommerce.9_2_return_to_origin_courier_return
    - business_process.unicommerce.9_3_customer_return
    - business_process.unicommerce.9_4_cancellation
  included_source_tables:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
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
    unicommerce_recon_kb_docx: f853b2bb2269766c0c82a12de18ba2d234b3cd10e117a636f9f94399dd22c8a8
    oms_business_kb_docx: abc0ab7d0e06583af426daecc58b85d03cf2517b765c983e8568046e41af4bb9
    manifest: e151167df1ff75a63b6eddaf74f0bfddd8a4741bc67d27988e7455fee8b39661
  quality_summary:
    candidate_cards: 231
    candidate_edges: 163
    source_evidence_count: 15
    sql_patterns: 23
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
  applied_to: Unicommerce
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
  id: ev.unicommerce.scope.001
  source_document: Unicommerce Recon KB.docx
  source_section: 1. What Is Unicommerce?
  evidence_type: scope_boundary
  summary: Unicommerce is an OMS/operations-invoice layer, not a marketplace settlement source; it aggregates marketplace,
    D2C, quick-commerce, courier and accounting integrations while marketplace payout tables remain separate.
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.tables.001
  source_document: Unicommerce Recon KB.docx
  source_section: 2. Table Overview — Two-Table Structure
  evidence_type: schema_reference
  summary: ZenStatement Unicommerce pipeline has zs_observe.unicommerce financial/invoice view for sales, returns and cancellations,
    plus zs_observe.unicommerce_order_sales_report shipment/logistics view with AWB, delivery status, shipping method and
    MRP.
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.join.001
  source_document: Unicommerce Recon KB.docx
  source_section: 2. Table Overview — The Critical Join; Entity Relationships
  evidence_type: relationship
  summary: 'Correct join is # || unicommerce.order_id = unicommerce_order_sales_report.order_id; direct join has low coverage
    while prefixed join reaches 91.1% documented coverage.'
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.metadata.001
  source_document: Unicommerce Recon KB.docx
  source_section: 3. Transaction Types in unicommerce
  evidence_type: value_profile
  summary: 'metadata is the single source of truth: sales for forward sales, reverse for Courier Return/RTO and Customer Return,
    cancel for pre-dispatch cancellations; transaction_type refines COD/PREPAID and return subtype.'
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.metrics.001
  source_document: Unicommerce Recon KB.docx
  source_section: '4. Key Business Metrics; Table: Unicommerce — Key Statistics'
  evidence_type: metric_definition
  summary: Documents Apr-Dec 2025 metrics including 3.25M rows, 1.47M orders, ₹139.4 Cr sales GMV, ₹15.1 Cr returns, ₹8.1
    Cr cancels, COD share about 28.8% and prepaid share about 71.2%.
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.lifecycle.001
  source_document: Unicommerce Recon KB.docx
  source_section: 5. Transaction Lifecycle
  evidence_type: workflow
  summary: Forward sales, Courier Return/RTO, Customer Return and Cancellation lifecycle are represented with metadata and
    transaction_type values in unicommerce, with OSR shipment status complement where applicable.
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.lifecycle.forward_sale.001
  source_document: Unicommerce Recon KB.docx
  source_section: 9.1 Forward Sale
  evidence_type: workflow
  summary: Forward sale starts with customer order through Astrotalk app/website/marketplace, Unicommerce OMS receives the order, GST invoice is generated, unicommerce metadata=sales with COD/PREPAID transaction_type and INSEG-style sales invoice, then OSR moves MANIFESTED to DISPATCHED and finally DELIVERED.
  supported_semantics:
  - process_id business_process.unicommerce.9_1_forward_sale
  - metadata=sales and transaction_type COD/PREPAID for forward sale
  - invoice_number sales invoice pattern such as INSEG-25-26-XXXXX
  - OSR order_status progression MANIFESTED to DISPATCHED to DELIVERED
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.lifecycle.rto.001
  source_document: Unicommerce Recon KB.docx
  source_section: 9.2 Return-to-Origin (RTO / Courier Return)
  evidence_type: workflow
  summary: RTO begins after courier delivery failure, courier triggers Return-to-Origin, unicommerce records metadata=reverse and transaction_type=Courier Return with SRFZ stock-return/credit-note invoice semantics, and OSR may show RESHIPPED or CANCELLED after the item returns.
  supported_semantics:
  - process_id business_process.unicommerce.9_2_return_to_origin_courier_return
  - metadata=reverse and transaction_type=Courier Return for RTO
  - invoice_number SRFZ-style stock return credit-note semantics
  - OSR order_status RESHIPPED if redispatched or CANCELLED if abandoned
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.lifecycle.customer_return.001
  source_document: Unicommerce Recon KB.docx
  source_section: 9.3 Customer Return
  evidence_type: workflow
  summary: Customer return begins after buyer receives the item and initiates return; Unicommerce creates a reverse entry with metadata=reverse, transaction_type=Customer Return, charged_amount as original sale value, followed by item return and refund processing.
  supported_semantics:
  - process_id business_process.unicommerce.9_3_customer_return
  - metadata=reverse and transaction_type=Customer Return for buyer-initiated return
  - charged_amount equals original sale value for customer return analysis
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.lifecycle.cancellation.001
  source_document: Unicommerce Recon KB.docx
  source_section: 9.4 Cancellation
  evidence_type: workflow
  summary: Cancellation occurs after order placement but before dispatch; unicommerce records metadata=cancel, transaction_type COD/PREPAID, cancellation invoice, and OSR order_status=CANCELLED where shipment complement exists.
  supported_semantics:
  - process_id business_process.unicommerce.9_4_cancellation
  - metadata=cancel and transaction_type COD/PREPAID for cancellation
  - invoice_number represents cancellation invoice
  - OSR order_status=CANCELLED
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.gst.001
  source_document: Unicommerce Recon KB.docx
  source_section: 10. GST / Tax Framework
  evidence_type: rule
  summary: GST classification uses source/destination state and IGST versus CGST+SGST tax fields; product HSN fallback may
    be needed.
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.data_quality.001
  source_document: Unicommerce Recon KB.docx
  source_section: 8/12 Data Quality Observations & Known Issues
  evidence_type: caveat
  summary: 'Documents # prefix mismatch, AWB only in OSR other_id, total_tcs_amount=0, brand mostly null, freebie SKU RD_0325_05
    at ₹1, HSN fallback fields, multi-row orders, group_level_id=211 primary and 22 minor.'
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.filters.001
  source_document: Unicommerce Recon KB.docx
  source_section: 9/13 Mandatory Query Filters
  evidence_type: rule
  summary: Mandatory filters include is_active=true, group_level_id=211 for Astrotalk analysis, metadata-specific filters
    for sales/reverse/cancel and charged_amount>1 to exclude freebies from revenue.
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.schema.001
  source_document: Unicommerce Recon KB.docx
  source_section: 'Table: Unicommerce — Schema Details (168 Columns — Key Fields)'
  evidence_type: schema_reference
  summary: Documents key identity, date, financial, tax, classification, product, GST/geography and system columns on zs_observe.unicommerce.
  confidence: high
```
```yaml
source_evidence:
  id: ev.unicommerce.osr.schema.001
  source_document: Unicommerce Recon KB.docx
  source_section: 'Table: Unicommerce Order Sales Report — Schema Details'
  evidence_type: schema_reference
  summary: 'OSR documents order_id with # prefix, sku_id, other_id as AWB, created_date, MRP, shipping_method, order_status,
    weights/dimensions, channel/facility and system columns.'
  confidence: high
```
## 2. Scope Guardrails and Out-of-Scope Registry

```yaml
out_of_scope_item:
  id: oos.unicommerce.tenant_account
  topic: tenant/account binding
  instruction: group_level_id 211 and 22 are documented scope values only; do not create tenant/group/platform_account/account_data_binding
    cards.
  forbidden_card_population:
  - tenant
  - group
  - platform_account
  - account_data_binding
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
```
```yaml
out_of_scope_item:
  id: oos.unicommerce.marketplace_settlement
  topic: marketplace settlement binding
  instruction: Unicommerce is seller OMS/invoice view; marketplace financial/payout tables are separate and runtime/external
    binding is outside this file.
  forbidden_card_population:
  - platform_account
  - bank_account
  - payment_gateway_account
  evidence_refs:
  - ev.unicommerce.scope.001
```
```yaml
out_of_scope_item:
  id: oos.unicommerce.external_courier_account
  topic: courier account operations
  instruction: OSR contains shipment status/AWB/shipping_method complement, but courier labels must not create courier account,
    invoice, or settlement cards.
  forbidden_card_population:
  - courier_account
  - logistics_account
  - carrier_reconciliation
  evidence_refs:
  - ev.unicommerce.tables.001
  - ev.unicommerce.osr.schema.001
```
```yaml
out_of_scope_item:
  id: oos.unicommerce.tax_filing
  topic: statutory tax filing
  instruction: GSTIN, HSN, tax amount and TCS fields are invoice analytics columns only; do not create statutory filing cards.
  forbidden_card_population:
  - statutory_tax_filing
  evidence_refs:
  - ev.unicommerce.gst.001
  - ev.unicommerce.data_quality.001
```
## 3. Candidate Card Registry

### 3.x platform

```yaml
candidate_card:
  card_type: platform
  card_id: platform.unicommerce
  display_name: Unicommerce
  canonical_name: Unicommerce
  platform_category: cross_channel_d2c_oms_wms_platform
  not_marketplace: true
  oms_document_scope: OMS financial/invoice ledger plus directly documented shipment status complement
  evidence_refs:
  - ev.unicommerce.scope.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x platform_context

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.unicommerce.in.d2c_oms
  display_name: Unicommerce India D2C OMS context
  platform_id: platform.unicommerce
  country_code: IN
  currency_context:
  - INR
  timezone: Asia/Kolkata
  platform_model: cross_channel_oms_invoice_and_shipment_tracking
  client_scope_values:
    group_level_id_211: Astrotalk primary
    group_level_id_22: PrettyKrafts/Mensa minor caveat
  scope_filter_columns:
  - group_level_id
  - metadata
  - transaction_type
  - sales_channel
  - source_gst_name
  evidence_refs:
  - ev.unicommerce.scope.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x domain

```yaml
candidate_card:
  card_type: domain
  card_id: domain.unicommerce.invoice_transaction_ledger
  display_name: Unicommerce invoice transaction ledger
  domain_family: oms_invoice_operations
  semantic_scope: Financial/invoice view for sales, returns, cancellations, GST, charged amounts, discounts and invoices in
    zs_observe.unicommerce.
  evidence_refs:
  - ev.unicommerce.tables.001
  - ev.unicommerce.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.unicommerce.shipment_status_complement
  display_name: Unicommerce shipment status complement
  domain_family: oms_shipment_status_complement
  semantic_scope: Directly documented OSR shipment status/AWB/MRP complement used to enrich OMS orders, not external courier-account
    domain.
  evidence_refs:
  - ev.unicommerce.tables.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.unicommerce.returns_cancellations
  display_name: Unicommerce returns and cancellations
  domain_family: oms_returns_cancellations
  semantic_scope: Reverse and cancel semantics in the same unicommerce table, differentiated by metadata and transaction_type.
  evidence_refs:
  - ev.unicommerce.metadata.001
  - ev.unicommerce.lifecycle.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.unicommerce.sales_channel_architecture
  display_name: Unicommerce sales-channel architecture
  domain_family: oms_channel_grouping
  semantic_scope: sales_channel identifies D2C, marketplace and quick-commerce order sources without creating marketplace
    account cards.
  evidence_refs:
  - ev.unicommerce.scope.001
  - ev.unicommerce.metrics.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.unicommerce.gst_invoice_tax_classification
  display_name: Unicommerce GST invoice tax classification
  domain_family: oms_invoice_tax
  semantic_scope: Invoice-side GST classification using source/destination geography, tax columns and HSN fallback.
  evidence_refs:
  - ev.unicommerce.gst.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.unicommerce.reconciliation
  display_name: Unicommerce OMS reconciliation hooks
  domain_family: oms_reconciliation
  semantic_scope: Financial-to-shipment coverage, sales/reverse/cancel netting, GST checks, and external marketplace/PG binding
    hooks.
  evidence_refs:
  - ev.unicommerce.join.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x table

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.unicommerce
  display_name: zs_observe.unicommerce
  schema_name: zs_observe
  table_name: unicommerce
  source_system: Unicommerce OMS
  table_role: oms_financial_invoice_transaction_ledger
  row_scope: Sales, returns and cancellations in one OMS table.
  grain: order_line_invoice_transaction
  active_row_context: 3,253,598 active rows for Apr-Dec 2025 in source document.
  mandatory_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata filter required for sales/reverse/cancel-specific metrics
  primary_key_policy: order_id + invoice_number at OMS invoice/order-line grain; multiple rows per order may exist.
  evidence_refs:
  - ev.unicommerce.tables.001
  - ev.unicommerce.schema.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.unicommerce_order_sales_report
  display_name: zs_observe.unicommerce_order_sales_report
  schema_name: zs_observe
  table_name: unicommerce_order_sales_report
  source_system: Unicommerce OMS/OSR
  table_role: oms_shipment_status_tracking_complement
  row_scope: Shipment-level fulfillment and delivery tracking with AWB, order_status, shipping_method and MRP.
  grain: shipment_or_order_line_status
  active_row_context: 3,017,728 rows for Apr-Dec 2025 in source document.
  mandatory_filters:
  - is_active = true
  - group_level_id = 211
  primary_key_policy: 'order_id with # prefix + sku_id/other_id for tracking context.'
  evidence_refs:
  - ev.unicommerce.tables.001
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x column

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.unique_id
  display_name: unique_id
  column_name: unique_id
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: system_identifier
  description: Row identifier.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: system_identifier
  description: Pipeline UUID.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: dedup_identifier
  description: Dedup/hash identifier.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.group_id
  display_name: group_id
  column_name: group_id
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: scope_identifier
  description: Scope column only; not tenant card.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.tenant_id
  display_name: tenant_id
  column_name: tenant_id
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: scope_identifier
  description: Scope alias column only.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.unicommerce
  data_type: integer
  semantic_role: scope_identifier
  description: 211 Astrotalk primary; 22 PrettyKrafts/Mensa caveat.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.unicommerce
  data_type: boolean
  semantic_role: quality_filter
  description: Mandatory active-row filter.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.is_duplicated
  display_name: is_duplicated
  column_name: is_duplicated
  table_id: table.zs_observe.unicommerce
  data_type: boolean
  semantic_role: quality_filter
  description: Duplicate flag.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.zen_status
  display_name: zen_status
  column_name: zen_status
  table_id: table.zs_observe.unicommerce
  data_type: boolean_or_varchar
  semantic_role: quality_filter
  description: Zen processing status.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: source_sheet
  description: Source sheet name.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: currency
  description: INR in documented Unicommerce context.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: order_identifier
  description: 'Unicommerce order number without # prefix; join to OSR using # || order_id.'
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.invoice_number
  display_name: invoice_number
  column_name: invoice_number
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: invoice_identifier
  description: GST invoice, credit-note or cancellation invoice identifier.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.original_invoice_no
  display_name: original_invoice_no
  column_name: original_invoice_no
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: invoice_reference
  description: Original invoice for reverse/cancel linkage.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.sale_order_number
  display_name: sale_order_number
  column_name: sale_order_number
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: order_reference
  description: Sale order reference, mostly null.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.sku_id
  display_name: sku_id
  column_name: sku_id
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: product_key
  description: Seller SKU code, never null in source.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.product_sku_code
  display_name: product_sku_code
  column_name: product_sku_code
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: product_key
  description: Raw Unicommerce product SKU field.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.awb_num
  display_name: awb_num
  column_name: awb_num
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: awb_reference
  description: AWB is null in this table; use OSR.other_id.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.other_id
  display_name: other_id
  column_name: other_id
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: oms_reference
  description: Additional reference.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.irn
  display_name: irn
  column_name: irn
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: gst_einvoice_identifier
  description: GST e-invoice IRN.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.acknowledgement_number
  display_name: acknowledgement_number
  column_name: acknowledgement_number
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: gst_einvoice_identifier
  description: E-invoice acknowledgement number.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.unicommerce
  data_type: date
  semantic_role: primary_date_dimension
  description: Transaction date.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.date
  display_name: date
  column_name: date
  table_id: table.zs_observe.unicommerce
  data_type: date
  semantic_role: source_date
  description: Alternate date field.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.original_invoice_date
  display_name: original_invoice_date
  column_name: original_invoice_date
  table_id: table.zs_observe.unicommerce
  data_type: date
  semantic_role: invoice_date
  description: Original invoice date.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.dispatch_time
  display_name: dispatch_time
  column_name: dispatch_time
  table_id: table.zs_observe.unicommerce
  data_type: timestamp
  semantic_role: event_timestamp
  description: Dispatch timestamp.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.dispatch_date_cancellation_date
  display_name: dispatch_date_cancellation_date
  column_name: dispatch_date_cancellation_date
  table_id: table.zs_observe.unicommerce
  data_type: timestamp
  semantic_role: event_timestamp
  description: Dispatch/cancellation datetime.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.charged_amount
  display_name: charged_amount
  column_name: charged_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount
  description: Total invoice value/GST inclusive primary GMV amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.charged_amount_excluding_tax
  display_name: charged_amount_excluding_tax
  column_name: charged_amount_excluding_tax
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount_ex_tax
  description: Taxable base.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.item_amount_excluding_tax
  display_name: item_amount_excluding_tax
  column_name: item_amount_excluding_tax
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount_ex_tax
  description: Item value excluding GST.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.shipping_amount
  display_name: shipping_amount
  column_name: shipping_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount
  description: Shipping charged to buyer.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.shipping_amount_excluding_tax
  display_name: shipping_amount_excluding_tax
  column_name: shipping_amount_excluding_tax
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount_ex_tax
  description: Shipping excluding GST.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.cod_charge
  display_name: cod_charge
  column_name: cod_charge
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount
  description: COD collection fee.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.cod_charge_excluding_gst
  display_name: cod_charge_excluding_gst
  column_name: cod_charge_excluding_gst
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount_ex_tax
  description: COD charge excluding GST.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.gift_wrap_amount
  display_name: gift_wrap_amount
  column_name: gift_wrap_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount
  description: Gift wrap amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.discount
  display_name: discount
  column_name: discount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: discount_amount
  description: Discount value.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.discount_amount
  display_name: discount_amount
  column_name: discount_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: discount_amount
  description: Discount amount field.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.total
  display_name: total
  column_name: total
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_total
  description: Total financial amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.unit_price
  display_name: unit_price
  column_name: unit_price
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount
  description: Unit price.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.prepaid_amount
  display_name: prepaid_amount
  column_name: prepaid_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: payment_amount
  description: Prepaid amount component.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.cod_amount
  display_name: cod_amount
  column_name: cod_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: payment_amount
  description: COD amount component.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.other_charges
  display_name: other_charges
  column_name: other_charges
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: financial_amount
  description: Other charges.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.tax_igst_rate
  display_name: tax_igst_rate
  column_name: tax_igst_rate
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_rate
  description: IGST rate.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.tax_igst_amount
  display_name: tax_igst_amount
  column_name: tax_igst_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: IGST amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.tax_cgst_rate
  display_name: tax_cgst_rate
  column_name: tax_cgst_rate
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_rate
  description: CGST rate.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.tax_cgst_amount
  display_name: tax_cgst_amount
  column_name: tax_cgst_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: CGST amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.tax_sgst_rate
  display_name: tax_sgst_rate
  column_name: tax_sgst_rate
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_rate
  description: SGST rate.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.tax_sgst_amount
  display_name: tax_sgst_amount
  column_name: tax_sgst_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: SGST amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.igst
  display_name: igst
  column_name: igst
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: IGST alternate/source amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.cgst
  display_name: cgst
  column_name: cgst
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: CGST alternate/source amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.sgst
  display_name: sgst
  column_name: sgst
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: SGST alternate/source amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.utgst
  display_name: utgst
  column_name: utgst
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: UTGST amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.cess
  display_name: cess
  column_name: cess
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: Cess amount.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.cess_rate
  display_name: cess_rate
  column_name: cess_rate
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_rate
  description: Cess rate.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.total_tcs_amount
  display_name: total_tcs_amount
  column_name: total_tcs_amount
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: tax_amount
  description: TCS amount; documented zero for Astrotalk so no TCS reconciliation from OMS table.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.metadata
  display_name: metadata
  column_name: metadata
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: transaction_classifier
  description: Primary sales/reverse/cancel classifier.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.metadata_2
  display_name: metadata_2
  column_name: metadata_2
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: transaction_classifier_aux
  description: Auxiliary metadata.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.transaction_type
  display_name: transaction_type
  column_name: transaction_type
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: transaction_subtype
  description: PREPAID/COD for sales/cancels; Courier Return/Customer Return for reverse.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.return_type
  display_name: return_type
  column_name: return_type
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: return_subtype
  description: Return subtype when populated.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.payment_mode
  display_name: payment_mode
  column_name: payment_mode
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: payment_classifier
  description: COD/PREPAID label where present.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.voucher_type_name
  display_name: voucher_type_name
  column_name: voucher_type_name
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: invoice_classifier
  description: Voucher/invoice type label, often null.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.sales_channel
  display_name: sales_channel
  column_name: sales_channel
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: channel_classifier
  description: Source channel for grouping, not marketplace account binding.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: product_description
  description: Product description.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.product_name
  display_name: product_name
  column_name: product_name
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: product_description
  description: Product name.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.brand
  display_name: brand
  column_name: brand
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: product_attribute
  description: Often null; use sales_channel/source_gst_name proxy when appropriate.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.quantity
  display_name: quantity
  column_name: quantity
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: quantity
  description: Quantity.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.qty
  display_name: qty
  column_name: qty
  table_id: table.zs_observe.unicommerce
  data_type: decimal
  semantic_role: quantity
  description: Alternate quantity field.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.hsn
  display_name: hsn
  column_name: hsn
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: tax_classification
  description: HSN code; may be null.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.hsn_code
  display_name: hsn_code
  column_name: hsn_code
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: tax_classification
  description: HSN alternate.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.product_hsn_code
  display_name: product_hsn_code
  column_name: product_hsn_code
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: tax_classification
  description: Product HSN fallback.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.hsn_generated
  display_name: hsn_generated
  column_name: hsn_generated
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: tax_classification
  description: Generated HSN fallback.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.source_gst_id
  display_name: source_gst_id
  column_name: source_gst_id
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: invoice_origin_gstin
  description: Invoice issuing source GSTIN; not warehouse account card.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.source_gst_name
  display_name: source_gst_name
  column_name: source_gst_name
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: invoice_origin_name
  description: Invoice origin/source GST name; can group invoice analytics.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.destination_state
  display_name: destination_state
  column_name: destination_state
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: destination_geography
  description: Destination state for GST classification.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.destination_city
  display_name: destination_city
  column_name: destination_city
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: destination_geography
  description: Destination city.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.destination_zipcode
  display_name: destination_zipcode
  column_name: destination_zipcode
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: destination_geography
  description: Destination pincode.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.destination_state_code
  display_name: destination_state_code
  column_name: destination_state_code
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: destination_geography
  description: Destination state code.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.channel_party_gstin
  display_name: channel_party_gstin
  column_name: channel_party_gstin
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: buyer_or_channel_gstin
  description: Channel party GSTIN where present.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce.customer_gstin
  display_name: customer_gstin
  column_name: customer_gstin
  table_id: table.zs_observe.unicommerce
  data_type: varchar
  semantic_role: buyer_gstin
  description: Customer GSTIN where present.
  evidence_refs:
  - ev.unicommerce.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.unique_id
  display_name: unique_id
  column_name: unique_id
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: system_identifier
  description: Row identifier.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.txn_uuid
  display_name: txn_uuid
  column_name: txn_uuid
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: system_identifier
  description: Pipeline UUID.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.unique_value
  display_name: unique_value
  column_name: unique_value
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: dedup_identifier
  description: Dedup hash.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.order_id
  display_name: order_id
  column_name: order_id
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: order_identifier
  description: 'Order ID with # prefix; join to unicommerce using # || order_id.'
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.sku_id
  display_name: sku_id
  column_name: sku_id
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: product_key
  description: Seller SKU code.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.seller_sku_code
  display_name: seller_sku_code
  column_name: seller_sku_code
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: product_key
  description: Alternate seller SKU.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.sku_name
  display_name: sku_name
  column_name: sku_name
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: product_description
  description: SKU name, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.other_id
  display_name: other_id
  column_name: other_id
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: awb_reference
  description: AWB/tracking number in OSR.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.created_date
  display_name: created_date
  column_name: created_date
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: date
  semantic_role: primary_date_dimension
  description: Shipment/record date.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.order_date
  display_name: order_date
  column_name: order_date
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: date_string
  description: Original order date, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.mrp
  display_name: mrp
  column_name: mrp
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: catalogue_amount
  description: Catalogue MRP.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.total_price
  display_name: total_price
  column_name: total_price
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: amount_string
  description: Total selling price, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.discount
  display_name: discount
  column_name: discount
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: discount_amount_string
  description: Discount, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.shipping_method
  display_name: shipping_method
  column_name: shipping_method
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: shipping_method_label
  description: Courier + service type label.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.gross_weight
  display_name: gross_weight
  column_name: gross_weight
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: weight
  description: Gross weight.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.gross_weight_kg
  display_name: gross_weight_kg
  column_name: gross_weight_kg
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: weight
  description: Gross weight kg.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.gross_weight_g
  display_name: gross_weight_g
  column_name: gross_weight_g
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: weight
  description: Gross weight g.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.logistics_length
  display_name: logistics_length
  column_name: logistics_length
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: dimension
  description: Length.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.logistics_height
  display_name: logistics_height
  column_name: logistics_height
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: dimension
  description: Height.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.logistics_width
  display_name: logistics_width
  column_name: logistics_width
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: dimension
  description: Width.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.logistics_length_mm
  display_name: logistics_length_mm
  column_name: logistics_length_mm
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: dimension
  description: Length in mm.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.logistics_height_mm
  display_name: logistics_height_mm
  column_name: logistics_height_mm
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: dimension
  description: Height in mm.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.logistics_width_mm
  display_name: logistics_width_mm
  column_name: logistics_width_mm
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: dimension
  description: Width in mm.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.volumetric_weight
  display_name: volumetric_weight
  column_name: volumetric_weight
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: weight
  description: Volumetric weight.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.volumetric_weight_kg
  display_name: volumetric_weight_kg
  column_name: volumetric_weight_kg
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: weight
  description: Volumetric weight kg.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.item_type_size
  display_name: item_type_size
  column_name: item_type_size
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: item_attribute
  description: Item type size.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.item_type_brand
  display_name: item_type_brand
  column_name: item_type_brand
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: decimal
  semantic_role: item_attribute
  description: Item type brand, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.order_status
  display_name: order_status
  column_name: order_status
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: shipment_status
  description: DELIVERED/DISPATCHED/CANCELLED/RESHIPPED/REPLACED/etc.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.sale_order_status
  display_name: sale_order_status
  column_name: sale_order_status
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: shipment_status
  description: Sale order status, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.description
  display_name: description
  column_name: description
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: product_description
  description: Product description.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.tags
  display_name: tags
  column_name: tags
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: tag
  description: Tags, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.category
  display_name: category
  column_name: category
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: category
  description: Category, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.channel_name
  display_name: channel_name
  column_name: channel_name
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: channel_label
  description: Channel name, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.facility
  display_name: facility
  column_name: facility
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: facility_label
  description: Fulfilment facility, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.billing_address_city
  display_name: billing_address_city
  column_name: billing_address_city
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: geography
  description: Billing city, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.billing_address_state
  display_name: billing_address_state
  column_name: billing_address_state
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: geography
  description: Billing state, mostly null.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
  display_name: group_level_id
  column_name: group_level_id
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: integer
  semantic_role: scope_identifier
  description: 211 in OSR context.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.currency_type
  display_name: currency_type
  column_name: currency_type
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: currency
  description: INR.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.is_active
  display_name: is_active
  column_name: is_active
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: boolean
  semantic_role: quality_filter
  description: Active row flag.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.unicommerce_order_sales_report.zen_sheet_name
  display_name: zen_sheet_name
  column_name: zen_sheet_name
  table_id: table.zs_observe.unicommerce_order_sales_report
  data_type: varchar
  semantic_role: source_sheet
  description: Source sheet name.
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x relationship

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.unicommerce_to_osr.prefixed_order_id
  display_name: Unicommerce financial invoice to OSR shipment status
  from_table: table.zs_observe.unicommerce
  to_table: table.zs_observe.unicommerce_order_sales_report
  join_keys:
  - '''#'' || u.order_id = o.order_id'
  relationship_grain: OMS invoice/order-line transaction to shipment status rows
  join_safety_rule: 'Apply active filters on both sides; prefix unicommerce.order_id with #; expect returns/cancels may lack
    OSR match; use distinct order counts for coverage.'
  documented_coverage: 91.1% matched orders with prefixed join
  business_semantics: Financial invoice view enriched with operational shipment status/AWB/MRP.
  evidence_refs:
  - ev.unicommerce.join.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x value_profile

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.unicommerce.metadata_transaction_types
  display_name: metadata_transaction_types
  table_id: table.zs_observe.unicommerce
  column_names:
  - metadata
  - transaction_type
  values_or_known_values:
  - metadata: sales
    transaction_type: PREPAID
    count: 2122372
    meaning: Forward order paid online
  - metadata: sales
    transaction_type: COD
    count: 860450
    meaning: Forward cash-on-delivery order
  - metadata: reverse
    transaction_type: Courier Return
    count: 233379
    meaning: RTO / failed delivery
  - metadata: reverse
    transaction_type: Customer Return
    count: 28285
    meaning: Buyer-initiated return after delivery
  - metadata: cancel
    transaction_type: COD / PREPAID
    count: 9112
    meaning: Order cancelled before dispatch
  evidence_refs:
  - ev.unicommerce.metadata.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.unicommerce.group_level_id
  display_name: group_level_id
  table_id: table.zs_observe.unicommerce
  column_names:
  - group_level_id
  values_or_known_values:
  - value: 211
    meaning: Astrotalk primary analysis scope
  - value: 22
    meaning: PrettyKrafts/Mensa minor caveat; not account card
  evidence_refs:
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.unicommerce.freebie_sku
  display_name: freebie_sku
  table_id: table.zs_observe.unicommerce
  column_names:
  - sku_id
  - charged_amount
  values_or_known_values:
  - sku: RD_0325_05
    meaning: ₹1 Rudraksha freebie; exclude charged_amount <= 1 from revenue unless requested
  evidence_refs:
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.unicommerce.gst_type
  display_name: gst_type
  table_id: table.zs_observe.unicommerce
  column_names:
  - source_gst_id
  - destination_state
  - tax_igst_rate
  - tax_cgst_rate
  - tax_sgst_rate
  values_or_known_values:
  - scenario: source_state != destination_state or IGST rate > 0
    gst_type: IGST
  - scenario: source_state = destination_state or CGST/SGST rates > 0
    gst_type: CGST+SGST
  evidence_refs:
  - ev.unicommerce.gst.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.unicommerce.hsn_fallback
  display_name: hsn_fallback
  table_id: table.zs_observe.unicommerce
  column_names:
  - hsn
  - hsn_generated
  - product_hsn_code
  - hsn_code
  values_or_known_values:
  - fallback_order:
    - hsn
    - hsn_generated
    - product_hsn_code
    - hsn_code
  evidence_refs:
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.unicommerce.osr_order_status
  display_name: osr_order_status
  table_id: table.zs_observe.unicommerce_order_sales_report
  column_names:
  - order_status
  values_or_known_values:
  - value: DELIVERED
    meaning: Successfully delivered
  - value: DISPATCHED
    meaning: In transit at data cutoff
  - value: CANCELLED
    meaning: Shipment/order cancelled
  - value: RESHIPPED
    meaning: Returned and re-dispatched
  - value: REPLACED
    meaning: Replacement sent
  - value: MANIFESTED/PICKING_FOR_INVOICING
    meaning: Early fulfilment states
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.unicommerce.sales_channel
  display_name: sales_channel
  table_id: table.zs_observe.unicommerce
  column_names:
  - sales_channel
  values_or_known_values:
  - sample_values:
    - Astrotalk_Store
    - CUSTOM
    - Amazon_Astrotalk
    - Shopify-Khazani-new
    - FLIPKART_Astrotalk1
    - MYNTRAPPMP-FZP
    - BLINKIT
    - INSTAMART
    - SHOPIFY_USA
  evidence_refs:
  - ev.unicommerce.scope.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x metric

```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.sales_order_count
  display_name: Sales Order Count
  metric_key: sales_order_count
  business_definition: Distinct orders with metadata=sales.
  default_grain: order
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.total_sales_gmv
  display_name: Total Sales Gmv
  metric_key: total_sales_gmv
  business_definition: Sales GMV from metadata=sales rows.
  default_grain: order_line
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.total_return_value
  display_name: Total Return Value
  metric_key: total_return_value
  business_definition: Return value from metadata=reverse rows.
  default_grain: order_line
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.total_cancel_value
  display_name: Total Cancel Value
  metric_key: total_cancel_value
  business_definition: Cancellation value from metadata=cancel rows.
  default_grain: order_line
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.net_revenue
  display_name: Net Revenue
  metric_key: net_revenue
  business_definition: Sales GMV less reverse value and cancel value.
  default_grain: order_line
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.average_order_value
  display_name: Average Order Value
  metric_key: average_order_value
  business_definition: Sales GMV divided by distinct sales order count.
  default_grain: order
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.cod_share
  display_name: Cod Share
  metric_key: cod_share
  business_definition: COD sales share based on transaction_type/payment_mode.
  default_grain: order
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.prepaid_share
  display_name: Prepaid Share
  metric_key: prepaid_share
  business_definition: Prepaid sales share based on transaction_type/payment_mode.
  default_grain: order
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.rto_rate
  display_name: Rto Rate
  metric_key: rto_rate
  business_definition: Courier Return orders divided by sales orders.
  default_grain: order
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.customer_return_rate
  display_name: Customer Return Rate
  metric_key: customer_return_rate
  business_definition: Customer Return orders divided by sales orders.
  default_grain: order
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.cancellation_rate
  display_name: Cancellation Rate
  metric_key: cancellation_rate
  business_definition: Cancel orders divided by sales orders.
  default_grain: order
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.channel_gmv
  display_name: Channel Gmv
  metric_key: channel_gmv
  business_definition: Sales GMV grouped by sales_channel.
  default_grain: channel
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.sku_revenue
  display_name: Sku Revenue
  metric_key: sku_revenue
  business_definition: Sales GMV grouped by SKU/description.
  default_grain: sku
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.gst_amount
  display_name: Gst Amount
  metric_key: gst_amount
  business_definition: Sum of IGST/CGST/SGST/UTGST/cess tax amounts.
  default_grain: order_line
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.hsn_missing_count
  display_name: Hsn Missing Count
  metric_key: hsn_missing_count
  business_definition: Rows with missing hsn after fallback.
  default_grain: row
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.delivery_rate
  display_name: Delivery Rate
  metric_key: delivery_rate
  business_definition: OSR delivered rows/orders over total shipment rows/orders.
  default_grain: shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.osr_join_coverage
  display_name: Osr Join Coverage
  metric_key: osr_join_coverage
  business_definition: 'Share of OMS orders matched to OSR using # prefix join.'
  default_grain: order
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unicommerce.avg_catalogue_mrp
  display_name: Avg Catalogue Mrp
  metric_key: avg_catalogue_mrp
  business_definition: Average catalogue MRP from OSR.
  default_grain: sku_or_order_line
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x metric_implementation

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.sales_order_count
  display_name: Unicommerce sales_order_count implementation
  metric_id: metric.unicommerce.sales_order_count
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.sales_order_count
  sql_reference_id: sql.unicommerce.metric.sales_order_count
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.total_sales_gmv
  display_name: Unicommerce total_sales_gmv implementation
  metric_id: metric.unicommerce.total_sales_gmv
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.total_sales_gmv
  sql_reference_id: sql.unicommerce.metric.total_sales_gmv
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.total_return_value
  display_name: Unicommerce total_return_value implementation
  metric_id: metric.unicommerce.total_return_value
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.total_return_value
  sql_reference_id: sql.unicommerce.metric.total_return_value
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.total_cancel_value
  display_name: Unicommerce total_cancel_value implementation
  metric_id: metric.unicommerce.total_cancel_value
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.total_cancel_value
  sql_reference_id: sql.unicommerce.metric.total_cancel_value
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.net_revenue
  display_name: Unicommerce net_revenue implementation
  metric_id: metric.unicommerce.net_revenue
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.net_revenue
  sql_reference_id: sql.unicommerce.metric.net_revenue
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.average_order_value
  display_name: Unicommerce average_order_value implementation
  metric_id: metric.unicommerce.average_order_value
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.average_order_value
  sql_reference_id: sql.unicommerce.metric.average_order_value
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.cod_share
  display_name: Unicommerce cod_share implementation
  metric_id: metric.unicommerce.cod_share
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.cod_share
  sql_reference_id: sql.unicommerce.metric.cod_share
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.prepaid_share
  display_name: Unicommerce prepaid_share implementation
  metric_id: metric.unicommerce.prepaid_share
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.prepaid_share
  sql_reference_id: sql.unicommerce.metric.prepaid_share
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.rto_rate
  display_name: Unicommerce rto_rate implementation
  metric_id: metric.unicommerce.rto_rate
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.rto_rate
  sql_reference_id: sql.unicommerce.metric.rto_rate
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.customer_return_rate
  display_name: Unicommerce customer_return_rate implementation
  metric_id: metric.unicommerce.customer_return_rate
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.customer_return_rate
  sql_reference_id: sql.unicommerce.metric.customer_return_rate
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.cancellation_rate
  display_name: Unicommerce cancellation_rate implementation
  metric_id: metric.unicommerce.cancellation_rate
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.cancellation_rate
  sql_reference_id: sql.unicommerce.metric.cancellation_rate
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.channel_gmv
  display_name: Unicommerce channel_gmv implementation
  metric_id: metric.unicommerce.channel_gmv
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.channel_gmv
  sql_reference_id: sql.unicommerce.metric.channel_gmv
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.sku_revenue
  display_name: Unicommerce sku_revenue implementation
  metric_id: metric.unicommerce.sku_revenue
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.sku_revenue
  sql_reference_id: sql.unicommerce.metric.sku_revenue
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.gst_amount
  display_name: Unicommerce gst_amount implementation
  metric_id: metric.unicommerce.gst_amount
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.gst_amount
  sql_reference_id: sql.unicommerce.metric.gst_amount
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.hsn_missing_count
  display_name: Unicommerce hsn_missing_count implementation
  metric_id: metric.unicommerce.hsn_missing_count
  source_table_ids:
  - table.zs_observe.unicommerce
  formula: See sql.unicommerce.metric.hsn_missing_count
  sql_reference_id: sql.unicommerce.metric.hsn_missing_count
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.delivery_rate
  display_name: Unicommerce delivery_rate implementation
  metric_id: metric.unicommerce.delivery_rate
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  formula: See sql.unicommerce.metric.delivery_rate
  sql_reference_id: sql.unicommerce.metric.delivery_rate
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.osr_join_coverage
  display_name: Unicommerce osr_join_coverage implementation
  metric_id: metric.unicommerce.osr_join_coverage
  source_table_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  formula: See sql.unicommerce.metric.osr_join_coverage
  sql_reference_id: sql.unicommerce.metric.osr_join_coverage
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.unicommerce.avg_catalogue_mrp
  display_name: Unicommerce avg_catalogue_mrp implementation
  metric_id: metric.unicommerce.avg_catalogue_mrp
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  formula: See sql.unicommerce.metric.avg_catalogue_mrp
  sql_reference_id: sql.unicommerce.metric.avg_catalogue_mrp
  required_filters:
  - is_active = true
  - group_level_id = 211 for Astrotalk analysis
  - metadata-specific filter where applicable
  grain: order_or_order_line_or_shipment
  evidence_refs:
  - ev.unicommerce.metrics.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x rule

```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.is_active_filter
  display_name: is_active_filter
  rule_text: All production Unicommerce OMS and OSR queries must filter is_active = true.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.group_scope_211
  display_name: group_scope_211
  rule_text: Astrotalk production analysis uses group_level_id = 211; group_level_id=22 is documented minor caveat only.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.metadata_first
  display_name: metadata_first
  rule_text: Sales, returns and cancellations share zs_observe.unicommerce; always filter or partition by metadata first.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.metadata.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.prefixed_join
  display_name: prefixed_join
  rule_text: 'Join OMS to OSR using # || unicommerce.order_id = osr.order_id; direct unprefixed join is incorrect.'
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.freebie_exclusion
  display_name: freebie_exclusion
  rule_text: Exclude charged_amount <= 1 or SKU RD_0325_05 from revenue/AOV/SKU revenue unless freebie analysis is requested.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.data_quality.001
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.hsn_fallback
  display_name: hsn_fallback
  rule_text: Use hsn_generated, product_hsn_code or hsn_code before flagging missing HSN.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.gst.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.tcs_zero_no_reconciliation
  display_name: tcs_zero_no_reconciliation
  rule_text: total_tcs_amount is documented zero for Astrotalk; do not create TCS settlement reconciliation from this OMS
    table.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.awb_only_osr
  display_name: awb_only_osr
  rule_text: AWB is not available in unicommerce.awb_num; use unicommerce_order_sales_report.other_id for tracking enrichment.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.data_quality.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.no_marketplace_account_binding
  display_name: no_marketplace_account_binding
  rule_text: Marketplace channels in sales_channel are labels only; settlement/payout account binding belongs outside this
    OMS document.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.scope.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.unicommerce.osr_included_as_complement_only
  display_name: osr_included_as_complement_only
  rule_text: OSR is included as directly documented OMS shipment/status complement; do not create external courier account,
    courier invoice or logistics settlement cards.
  rule_scope: unicommerce_d2c_oms_execution_and_semantics
  evidence_refs:
  - ev.unicommerce.tables.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x business_process

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.unicommerce.9_1_forward_sale
  display_name: 9.1 Forward Sale
  process_id: unicommerce.9.1.forward_sale
  source_lifecycle_section: 9.1 Forward Sale
  domain_id: domain.unicommerce.invoice_transaction_ledger
  process_summary: Customer order from Astrotalk app/website/marketplace is received by Unicommerce OMS, GST invoice is generated, unicommerce is classified as metadata=sales with COD/PREPAID transaction_type and sales invoice number, then OSR tracks MANIFESTED/DISPATCHED to DELIVERED.
  source_tables:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  lifecycle_cardinality: forward_sale_branch
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.metadata.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  display_name: 9.2 Return-to-Origin / Courier Return
  process_id: unicommerce.9.2.return_to_origin_courier_return
  source_lifecycle_section: 9.2 Return-to-Origin (RTO / Courier Return)
  domain_id: domain.unicommerce.returns_cancellations
  process_summary: Courier delivery failure triggers Return-to-Origin; unicommerce records metadata=reverse and transaction_type=Courier Return with SRFZ/SR-style stock-return credit-note invoice semantics, and OSR can end as RESHIPPED or CANCELLED.
  source_tables:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  lifecycle_cardinality: rto_branch
  evidence_refs:
  - ev.unicommerce.lifecycle.rto.001
  - ev.unicommerce.metadata.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.unicommerce.9_3_customer_return
  display_name: 9.3 Customer Return
  process_id: unicommerce.9.3.customer_return
  source_lifecycle_section: 9.3 Customer Return
  domain_id: domain.unicommerce.returns_cancellations
  process_summary: Buyer receives item and initiates return; Unicommerce creates a reverse entry where metadata=reverse, transaction_type=Customer Return and charged_amount carries original sale value before item return and refund processing.
  source_tables:
  - table.zs_observe.unicommerce
  lifecycle_cardinality: customer_return_branch
  evidence_refs:
  - ev.unicommerce.lifecycle.customer_return.001
  - ev.unicommerce.metadata.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.unicommerce.9_4_cancellation
  display_name: 9.4 Cancellation
  process_id: unicommerce.9.4.cancellation
  source_lifecycle_section: 9.4 Cancellation
  domain_id: domain.unicommerce.returns_cancellations
  process_summary: Order is cancelled before dispatch; unicommerce records metadata=cancel, transaction_type=COD/PREPAID and cancellation invoice, while OSR carries order_status=CANCELLED when the shipment complement exists.
  source_tables:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  lifecycle_cardinality: cancellation_branch
  evidence_refs:
  - ev.unicommerce.lifecycle.cancellation.001
  - ev.unicommerce.metadata.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.unicommerce.osr_status_tracking
  display_name: OSR shipment status tracking
  domain_id: domain.unicommerce.shipment_status_complement
  process_summary: OSR stores order_status, other_id as AWB, shipping_method and MRP for the shipment/status complement; it must not create external courier account or settlement cards.
  evidence_refs:
  - ev.unicommerce.tables.001
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.lifecycle.rto.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.unicommerce.gst_invoice_classification
  display_name: GST invoice classification
  domain_id: domain.unicommerce.invoice_transaction_ledger
  process_summary: GST type is classified from source/destination geography, tax rates/amounts and HSN fallback fields on the invoice ledger.
  evidence_refs:
  - ev.unicommerce.gst.001
  - ev.unicommerce.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x workflow_step

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_1_forward_sale.01_customer_order_created
  display_name: 9.1.1 customer order created
  business_process_id: business_process.unicommerce.9_1_forward_sale
  step_order: 1
  step_description: Customer order is placed through Astrotalk app, website, marketplace, or channel represented by sales_channel.
  source_table_ids:
  - table.zs_observe.unicommerce
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_1_forward_sale.02_unicommerce_receives_order
  display_name: 9.1.2 unicommerce receives order
  business_process_id: business_process.unicommerce.9_1_forward_sale
  step_order: 2
  step_description: Unicommerce OMS receives the order from the source channel and records order_id, sku_id, sales_channel and order identity in zs_observe.unicommerce.
  source_table_ids:
  - table.zs_observe.unicommerce
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_1_forward_sale.03_gst_invoice_generated
  display_name: 9.1.3 gst invoice generated
  business_process_id: business_process.unicommerce.9_1_forward_sale
  step_order: 3
  step_description: Warehouse GSTIN generates sales invoice; unicommerce row has metadata=sales, transaction_type COD/PREPAID and invoice_number such as INSEG-25-26-XXXXX.
  source_table_ids:
  - table.zs_observe.unicommerce
  column_ids:
  - column.zs_observe.unicommerce.metadata
  - column.zs_observe.unicommerce.transaction_type
  - column.zs_observe.unicommerce.invoice_number
  - column.zs_observe.unicommerce.source_gst_id
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.gst.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_1_forward_sale.04_manifest_dispatch
  display_name: 9.1.4 manifest and dispatch
  business_process_id: business_process.unicommerce.9_1_forward_sale
  step_order: 4
  step_description: Warehouse pick-pack-manifest-dispatch sequence is represented in OSR order_status progression from MANIFESTED to DISPATCHED.
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  column_ids:
  - column.zs_observe.unicommerce_order_sales_report.order_status
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_1_forward_sale.05_awb_and_shipping_method_recorded
  display_name: 9.1.5 awb and shipping method recorded
  business_process_id: business_process.unicommerce.9_1_forward_sale
  step_order: 5
  step_description: OSR records other_id as AWB tracking number and shipping_method as courier plus service level for the dispatched order.
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  column_ids:
  - column.zs_observe.unicommerce_order_sales_report.other_id
  - column.zs_observe.unicommerce_order_sales_report.shipping_method
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_1_forward_sale.06_delivered
  display_name: 9.1.6 delivered
  business_process_id: business_process.unicommerce.9_1_forward_sale
  step_order: 6
  step_description: Buyer delivery is represented by unicommerce_order_sales_report.order_status = DELIVERED.
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  column_ids:
  - column.zs_observe.unicommerce_order_sales_report.order_status
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_2_rto.01_delivery_attempt_failed
  display_name: 9.2.1 delivery attempt failed
  business_process_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  step_order: 1
  step_description: Courier delivery attempt fails due buyer absence, wrong address or refusal before Return-to-Origin is triggered.
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.rto.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_2_rto.02_courier_triggers_rto
  display_name: 9.2.2 courier triggers rto
  business_process_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  step_order: 2
  step_description: Courier triggers Return-to-Origin after failed delivery, causing the item to return toward the Astrotalk warehouse.
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.rto.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_2_rto.03_reverse_row_created
  display_name: 9.2.3 reverse row created
  business_process_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  step_order: 3
  step_description: unicommerce records metadata=reverse, transaction_type=Courier Return, invoice_number such as SRFZ-XXXXX and charged_amount as original sale value.
  source_table_ids:
  - table.zs_observe.unicommerce
  column_ids:
  - column.zs_observe.unicommerce.metadata
  - column.zs_observe.unicommerce.transaction_type
  - column.zs_observe.unicommerce.invoice_number
  - column.zs_observe.unicommerce.charged_amount
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.rto.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_2_rto.04_returned_to_warehouse_resolution
  display_name: 9.2.4 returned to warehouse resolution
  business_process_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  step_order: 4
  step_description: Item returns to warehouse; OSR order_status becomes RESHIPPED if redispatched or CANCELLED if abandoned.
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  column_ids:
  - column.zs_observe.unicommerce_order_sales_report.order_status
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.rto.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_3_customer_return.01_buyer_initiates_return
  display_name: 9.3.1 buyer initiates return
  business_process_id: business_process.unicommerce.9_3_customer_return
  step_order: 1
  step_description: Buyer receives the item and initiates a customer return after delivery.
  source_table_ids:
  - table.zs_observe.unicommerce
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.customer_return.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_3_customer_return.02_reverse_entry_created
  display_name: 9.3.2 reverse entry created
  business_process_id: business_process.unicommerce.9_3_customer_return
  step_order: 2
  step_description: Unicommerce creates a reverse entry for the buyer-initiated return.
  source_table_ids:
  - table.zs_observe.unicommerce
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.customer_return.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_3_customer_return.03_customer_return_classified
  display_name: 9.3.3 customer return classified
  business_process_id: business_process.unicommerce.9_3_customer_return
  step_order: 3
  step_description: unicommerce metadata=reverse and transaction_type=Customer Return classify the return; charged_amount carries the original sale value.
  source_table_ids:
  - table.zs_observe.unicommerce
  column_ids:
  - column.zs_observe.unicommerce.metadata
  - column.zs_observe.unicommerce.transaction_type
  - column.zs_observe.unicommerce.charged_amount
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.customer_return.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_3_customer_return.04_item_returned_refund_processed
  display_name: 9.3.4 item returned refund processed
  business_process_id: business_process.unicommerce.9_3_customer_return
  step_order: 4
  step_description: Item is returned and refund is processed; this is kept as OMS return/refund semantics, not payment-gateway account binding.
  source_table_ids:
  - table.zs_observe.unicommerce
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.customer_return.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_4_cancellation.01_order_cancelled_before_dispatch
  display_name: 9.4.1 order cancelled before dispatch
  business_process_id: business_process.unicommerce.9_4_cancellation
  step_order: 1
  step_description: Order is placed but cancelled before dispatch.
  source_table_ids:
  - table.zs_observe.unicommerce
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.cancellation.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_4_cancellation.02_cancel_row_recorded
  display_name: 9.4.2 cancel row recorded
  business_process_id: business_process.unicommerce.9_4_cancellation
  step_order: 2
  step_description: unicommerce records metadata=cancel, transaction_type COD/PREPAID and invoice_number as cancellation invoice.
  source_table_ids:
  - table.zs_observe.unicommerce
  column_ids:
  - column.zs_observe.unicommerce.metadata
  - column.zs_observe.unicommerce.transaction_type
  - column.zs_observe.unicommerce.invoice_number
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.cancellation.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.9_4_cancellation.03_osr_cancelled_status
  display_name: 9.4.3 osr cancelled status
  business_process_id: business_process.unicommerce.9_4_cancellation
  step_order: 3
  step_description: unicommerce_order_sales_report.order_status = CANCELLED represents cancelled shipment/order status in the OSR complement.
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  column_ids:
  - column.zs_observe.unicommerce_order_sales_report.order_status
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.lifecycle.cancellation.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.osr.01_prefixed_order
  display_name: osr prefixed order id
  business_process_id: business_process.unicommerce.osr_status_tracking
  step_order: 1
  step_description: OSR order_id stores # prefix and must join to # || unicommerce.order_id.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.join.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.osr.02_awb_status
  display_name: osr awb and status
  business_process_id: business_process.unicommerce.osr_status_tracking
  step_order: 2
  step_description: OSR other_id stores AWB/tracking number and order_status stores MANIFESTED, DISPATCHED, DELIVERED, RESHIPPED and CANCELLED status values.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.osr.schema.001
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.lifecycle.rto.001
  - ev.unicommerce.lifecycle.cancellation.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.unicommerce.gst.01_classify
  display_name: gst classify
  business_process_id: business_process.unicommerce.gst_invoice_classification
  step_order: 1
  step_description: tax_igst_rate/amount versus tax_cgst/tax_sgst and source/destination fields classify IGST vs CGST+SGST.
  materiality: source_specific_oms_semantic_step
  evidence_refs:
  - ev.unicommerce.gst.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x state_transition

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.unicommerce.osr.manifested_to_dispatched
  display_name: MANIFESTED to DISPATCHED
  state_column: column.zs_observe.unicommerce_order_sales_report.order_status
  from_state: MANIFESTED
  to_state: DISPATCHED
  transition_meaning: Forward sale shipment moves from manifested to dispatched in OSR after warehouse manifest/dispatch.
  business_process_id: business_process.unicommerce.9_1_forward_sale
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.unicommerce.osr.dispatched_to_delivered
  display_name: DISPATCHED to DELIVERED
  state_column: column.zs_observe.unicommerce_order_sales_report.order_status
  from_state: DISPATCHED
  to_state: DELIVERED
  transition_meaning: Forward sale shipment reaches buyer and OSR order_status becomes DELIVERED.
  business_process_id: business_process.unicommerce.9_1_forward_sale
  evidence_refs:
  - ev.unicommerce.lifecycle.forward_sale.001
  - ev.unicommerce.osr.schema.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.unicommerce.osr.rto_to_reshipped
  display_name: RTO resolution to RESHIPPED
  state_column: column.zs_observe.unicommerce_order_sales_report.order_status
  from_state: RTO_returned_to_warehouse
  to_state: RESHIPPED
  transition_meaning: After Courier Return/RTO, OSR order_status may be RESHIPPED if the returned item is re-dispatched.
  business_process_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  evidence_refs:
  - ev.unicommerce.lifecycle.rto.001
  - ev.unicommerce.osr.schema.001
  confidence: medium
  review_status: accepted_with_caveat
  create_action: create
```
```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.unicommerce.osr.rto_or_cancel_to_cancelled
  display_name: RTO/cancellation resolution to CANCELLED
  state_column: column.zs_observe.unicommerce_order_sales_report.order_status
  from_state: RTO_abandoned_or_pre_dispatch_cancel
  to_state: CANCELLED
  transition_meaning: OSR order_status may be CANCELLED when RTO is abandoned or when order is cancelled before dispatch.
  business_process_id:
  - business_process.unicommerce.9_2_return_to_origin_courier_return
  - business_process.unicommerce.9_4_cancellation
  evidence_refs:
  - ev.unicommerce.lifecycle.rto.001
  - ev.unicommerce.lifecycle.cancellation.001
  - ev.unicommerce.osr.schema.001
  confidence: medium
  review_status: accepted_with_caveat
  create_action: create
```
### 3.x reconciliation_profile

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.unicommerce.financial_to_osr_coverage
  display_name: Unicommerce financial-to-OSR coverage
  expected_side: 'unicommerce order_id without #'
  actual_side: 'OSR order_id with # prefix'
  unit: order_or_invoice_line
  matching_logic: prefix join and distinct order coverage; expected ~91.1% due returns/cancels gaps
  reconciliation_scope: Unicommerce internal OMS/OSR reconciliation semantics
  evidence_refs:
  - ev.unicommerce.join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.unicommerce.sales_returns_cancels_net_revenue
  display_name: Sales/returns/cancels net revenue
  expected_side: metadata=sales charged_amount
  actual_side: metadata=reverse and metadata=cancel charged_amount deductions
  unit: order_or_invoice_line
  matching_logic: same table partition by metadata and distinct order grain
  reconciliation_scope: Unicommerce internal OMS/OSR reconciliation semantics
  evidence_refs:
  - ev.unicommerce.metadata.001
  - ev.unicommerce.metrics.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.unicommerce.gst_invoice_consistency
  display_name: GST invoice consistency
  expected_side: charged_amount_excluding_tax and tax rate/amount fields
  actual_side: charged_amount and GST type classification
  unit: order_or_invoice_line
  matching_logic: source/destination tax logic plus HSN fallback
  reconciliation_scope: Unicommerce internal OMS/OSR reconciliation semantics
  evidence_refs:
  - ev.unicommerce.gst.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x query_pattern

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.unicommerce.gmv_by_month_channel
  display_name: gmv_by_month_channel
  natural_language_patterns:
  - GMV by month and channel
  - Show Astrotalk Store GMV
  primary_metric: metric.unicommerce.channel_gmv
  source_table_ids:
  - table.zs_observe.unicommerce
  sql_reference_id: sql.unicommerce.query.gmv_by_month_channel
  output_contract_id: output_contract.unicommerce.standard_metric_result
  required_rules:
  - rule.unicommerce.is_active_filter
  - rule.unicommerce.group_scope_211
  - rule.unicommerce.metadata_first
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.unicommerce.return_rate_by_type
  display_name: return_rate_by_type
  natural_language_patterns:
  - Return rate by type
  - RTO vs customer return rate
  primary_metric: metric.unicommerce.rto_rate
  source_table_ids:
  - table.zs_observe.unicommerce
  sql_reference_id: sql.unicommerce.query.return_rate_by_type
  output_contract_id: output_contract.unicommerce.standard_metric_result
  required_rules:
  - rule.unicommerce.is_active_filter
  - rule.unicommerce.group_scope_211
  - rule.unicommerce.metadata_first
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.unicommerce.full_enriched_order_view
  display_name: full_enriched_order_view
  natural_language_patterns:
  - Full enriched order view
  - Join Unicommerce financial to OSR status
  primary_metric: metric.unicommerce.osr_join_coverage
  source_table_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  sql_reference_id: sql.unicommerce.query.full_enriched_order_view
  output_contract_id: output_contract.unicommerce.standard_metric_result
  required_rules:
  - rule.unicommerce.is_active_filter
  - rule.unicommerce.group_scope_211
  - rule.unicommerce.metadata_first
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.unicommerce.delivery_rate_by_shipping_method
  display_name: delivery_rate_by_shipping_method
  natural_language_patterns:
  - Delivery rate by courier method
  - OSR order status performance
  primary_metric: metric.unicommerce.delivery_rate
  source_table_ids:
  - table.zs_observe.unicommerce_order_sales_report
  sql_reference_id: sql.unicommerce.query.delivery_rate_by_shipping_method
  output_contract_id: output_contract.unicommerce.standard_metric_result
  required_rules:
  - rule.unicommerce.is_active_filter
  - rule.unicommerce.group_scope_211
  - rule.unicommerce.metadata_first
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.join.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.unicommerce.gst_summary
  display_name: gst_summary
  natural_language_patterns:
  - GST summary
  - IGST vs CGST SGST
  primary_metric: metric.unicommerce.gst_amount
  source_table_ids:
  - table.zs_observe.unicommerce
  sql_reference_id: sql.unicommerce.query.gst_summary
  output_contract_id: output_contract.unicommerce.standard_metric_result
  required_rules:
  - rule.unicommerce.is_active_filter
  - rule.unicommerce.group_scope_211
  - rule.unicommerce.metadata_first
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.join.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x validation_test

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.unicommerce.no_dangling_sql_refs
  display_name: no_dangling_sql_refs
  assertion: Every metric_implementation and query_pattern sql_reference_id has a SQL pattern block.
  related_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.unicommerce.prefixed_join
  display_name: prefixed_join
  assertion: 'Any join to OSR uses # || u.order_id = o.order_id.'
  related_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.unicommerce.metadata_filter
  display_name: metadata_filter
  assertion: Sales, return and cancellation metrics filter or CASE on metadata first.
  related_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.unicommerce.freebie_exclusion
  display_name: freebie_exclusion
  assertion: AOV/SKU revenue patterns can exclude charged_amount <= 1 / RD_0325_05.
  related_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.unicommerce.hsn_fallback
  display_name: hsn_fallback
  assertion: Tax classification patterns use HSN fallback fields before flagging missing HSN.
  related_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.unicommerce.awb_only_osr
  display_name: awb_only_osr
  assertion: AWB/tracking columns are sourced from OSR.other_id, not unicommerce.awb_num.
  related_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.unicommerce.no_forbidden_scope_cards
  display_name: no_forbidden_scope_cards
  assertion: group_level_id, sales_channel, source_gst_name and shipping_method do not spawn account/tenant/courier cards.
  related_ids:
  - table.zs_observe.unicommerce
  - table.zs_observe.unicommerce_order_sales_report
  evidence_refs:
  - ev.unicommerce.filters.001
  - ev.unicommerce.data_quality.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x output_contract

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.unicommerce.standard_metric_result
  display_name: Unicommerce standard metric output
  contract_type: metric_result
  output_columns:
  - metric_name
  - metric_value
  - grain
  - group_level_id_or_runtime_scope
  - applied_metadata_filter
  - date_range
  evidence_refs:
  - ev.unicommerce.filters.001
  confidence: high
  review_status: accepted
  create_action: create
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.unicommerce.enriched_order_result
  display_name: Unicommerce enriched order output
  contract_type: enriched_order_view
  output_columns:
  - order_id
  - invoice_number
  - sku_id
  - charged_amount
  - metadata
  - transaction_type
  - sales_channel
  - source_gst_name
  - order_status
  - awb
  - shipping_method
  - catalogue_mrp
  evidence_refs:
  - ev.unicommerce.join.001
  confidence: high
  review_status: accepted
  create_action: create
```
### 3.x review_item

```yaml
candidate_card:
  card_type: review_item
  card_id: review.unicommerce.external_marketplace_settlement_binding
  display_name: External marketplace settlement binding
  issue_type: external_runtime_scope
  question: Which marketplace settlement table should be joined for Amazon/Flipkart/Myntra sales_channel rows at runtime?
  status: open
  blocking_for_core_oms_cards: false
  evidence_refs:
  - ev.unicommerce.scope.001
  confidence: high
```
```yaml
candidate_card:
  card_type: review_item
  card_id: review.unicommerce.reconciliation_tolerance
  display_name: Numeric reconciliation tolerance
  issue_type: missing_evidence
  question: No numeric tolerance is documented for financial-to-OSR or marketplace-settlement variance checks.
  status: open
  blocking_for_core_oms_cards: false
  evidence_refs:
  - ev.unicommerce.join.001
  confidence: high
```
## 4. Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.unique_id
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.unique_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.txn_uuid
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.unique_value
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.group_id
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.group_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.tenant_id
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.tenant_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.group_level_id
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.is_active
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.is_duplicated
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.is_duplicated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.zen_status
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.zen_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.zen_sheet_name
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.currency_type
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.order_id
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.invoice_number
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.invoice_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.original_invoice_no
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.original_invoice_no
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.sale_order_number
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.sale_order_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.sku_id
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.sku_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.product_sku_code
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.product_sku_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.awb_num
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.awb_num
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.other_id
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.other_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.irn
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.irn
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.acknowledgement_number
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.acknowledgement_number
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.created_date
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.date
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.original_invoice_date
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.original_invoice_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.dispatch_time
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.dispatch_time
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.dispatch_date_cancellation_date
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.dispatch_date_cancellation_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.charged_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.charged_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.charged_amount_excluding_tax
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.charged_amount_excluding_tax
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.item_amount_excluding_tax
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.item_amount_excluding_tax
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.shipping_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.shipping_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.shipping_amount_excluding_tax
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.shipping_amount_excluding_tax
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.cod_charge
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.cod_charge
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.cod_charge_excluding_gst
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.cod_charge_excluding_gst
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.gift_wrap_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.gift_wrap_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.discount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.discount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.discount_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.discount_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.total
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.total
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.unit_price
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.unit_price
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.prepaid_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.prepaid_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.cod_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.cod_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.other_charges
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.other_charges
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.tax_igst_rate
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.tax_igst_rate
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.tax_igst_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.tax_igst_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.tax_cgst_rate
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.tax_cgst_rate
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.tax_cgst_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.tax_cgst_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.tax_sgst_rate
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.tax_sgst_rate
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.tax_sgst_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.tax_sgst_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.igst
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.igst
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.cgst
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.cgst
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.sgst
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.sgst
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.utgst
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.utgst
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.cess
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.cess
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.cess_rate
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.cess_rate
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.total_tcs_amount
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.total_tcs_amount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.metadata
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.metadata
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.metadata_2
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.metadata_2
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.transaction_type
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.transaction_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.return_type
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.return_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.payment_mode
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.payment_mode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.voucher_type_name
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.voucher_type_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.sales_channel
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.sales_channel
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.description
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.product_name
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.product_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.brand
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.brand
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.quantity
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.quantity
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.qty
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.qty
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.hsn
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.hsn
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.hsn_code
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.hsn_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.product_hsn_code
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.product_hsn_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.hsn_generated
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.hsn_generated
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.source_gst_id
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.source_gst_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.source_gst_name
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.source_gst_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.destination_state
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.destination_state
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.destination_city
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.destination_city
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.destination_zipcode
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.destination_zipcode
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.destination_state_code
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.destination_state_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.channel_party_gstin
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.channel_party_gstin
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce.has_column.customer_gstin
  source_id: table.zs_observe.unicommerce
  target_id: column.zs_observe.unicommerce.customer_gstin
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.unique_id
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.unique_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.txn_uuid
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.txn_uuid
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.unique_value
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.unique_value
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.order_id
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.order_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.sku_id
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.sku_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.seller_sku_code
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.seller_sku_code
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.sku_name
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.sku_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.other_id
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.other_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.created_date
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.created_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.order_date
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.order_date
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.mrp
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.mrp
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.total_price
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.total_price
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.discount
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.discount
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.shipping_method
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.shipping_method
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.gross_weight
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.gross_weight
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.gross_weight_kg
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.gross_weight_kg
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.gross_weight_g
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.gross_weight_g
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.logistics_length
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.logistics_length
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.logistics_height
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.logistics_height
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.logistics_width
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.logistics_width
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.logistics_length_mm
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.logistics_length_mm
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.logistics_height_mm
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.logistics_height_mm
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.logistics_width_mm
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.logistics_width_mm
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.volumetric_weight
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.volumetric_weight
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.volumetric_weight_kg
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.volumetric_weight_kg
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.item_type_size
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.item_type_size
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.item_type_brand
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.item_type_brand
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.order_status
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.order_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.sale_order_status
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.sale_order_status
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.description
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.description
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.tags
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.tags
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.category
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.category
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.channel_name
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.channel_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.facility
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.facility
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.billing_address_city
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.billing_address_city
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.billing_address_state
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.billing_address_state
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.group_level_id
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.currency_type
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.currency_type
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.is_active
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.is_active
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.unicommerce_order_sales_report.has_column.zen_sheet_name
  source_id: table.zs_observe.unicommerce_order_sales_report
  target_id: column.zs_observe.unicommerce_order_sales_report.zen_sheet_name
  edge_type: HAS_COLUMN
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.unicommerce_to_osr.prefixed_order_id.from.table.zs_observe.unicommerce
  source_id: relationship.unicommerce_to_osr.prefixed_order_id
  target_id: table.zs_observe.unicommerce
  edge_type: FROM_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.relationship.unicommerce_to_osr.prefixed_order_id.to.table.zs_observe.unicommerce_order_sales_report
  source_id: relationship.unicommerce_to_osr.prefixed_order_id
  target_id: table.zs_observe.unicommerce_order_sales_report
  edge_type: TO_TABLE
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.sales_order_count.implements.metric.unicommerce.sales_order_count
  source_id: metric_implementation.unicommerce.sales_order_count
  target_id: metric.unicommerce.sales_order_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.total_sales_gmv.implements.metric.unicommerce.total_sales_gmv
  source_id: metric_implementation.unicommerce.total_sales_gmv
  target_id: metric.unicommerce.total_sales_gmv
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.total_return_value.implements.metric.unicommerce.total_return_value
  source_id: metric_implementation.unicommerce.total_return_value
  target_id: metric.unicommerce.total_return_value
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.total_cancel_value.implements.metric.unicommerce.total_cancel_value
  source_id: metric_implementation.unicommerce.total_cancel_value
  target_id: metric.unicommerce.total_cancel_value
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.net_revenue.implements.metric.unicommerce.net_revenue
  source_id: metric_implementation.unicommerce.net_revenue
  target_id: metric.unicommerce.net_revenue
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.average_order_value.implements.metric.unicommerce.average_order_value
  source_id: metric_implementation.unicommerce.average_order_value
  target_id: metric.unicommerce.average_order_value
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.cod_share.implements.metric.unicommerce.cod_share
  source_id: metric_implementation.unicommerce.cod_share
  target_id: metric.unicommerce.cod_share
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.prepaid_share.implements.metric.unicommerce.prepaid_share
  source_id: metric_implementation.unicommerce.prepaid_share
  target_id: metric.unicommerce.prepaid_share
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.rto_rate.implements.metric.unicommerce.rto_rate
  source_id: metric_implementation.unicommerce.rto_rate
  target_id: metric.unicommerce.rto_rate
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.customer_return_rate.implements.metric.unicommerce.customer_return_rate
  source_id: metric_implementation.unicommerce.customer_return_rate
  target_id: metric.unicommerce.customer_return_rate
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.cancellation_rate.implements.metric.unicommerce.cancellation_rate
  source_id: metric_implementation.unicommerce.cancellation_rate
  target_id: metric.unicommerce.cancellation_rate
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.channel_gmv.implements.metric.unicommerce.channel_gmv
  source_id: metric_implementation.unicommerce.channel_gmv
  target_id: metric.unicommerce.channel_gmv
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.sku_revenue.implements.metric.unicommerce.sku_revenue
  source_id: metric_implementation.unicommerce.sku_revenue
  target_id: metric.unicommerce.sku_revenue
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.gst_amount.implements.metric.unicommerce.gst_amount
  source_id: metric_implementation.unicommerce.gst_amount
  target_id: metric.unicommerce.gst_amount
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.hsn_missing_count.implements.metric.unicommerce.hsn_missing_count
  source_id: metric_implementation.unicommerce.hsn_missing_count
  target_id: metric.unicommerce.hsn_missing_count
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.delivery_rate.implements.metric.unicommerce.delivery_rate
  source_id: metric_implementation.unicommerce.delivery_rate
  target_id: metric.unicommerce.delivery_rate
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.osr_join_coverage.implements.metric.unicommerce.osr_join_coverage
  source_id: metric_implementation.unicommerce.osr_join_coverage
  target_id: metric.unicommerce.osr_join_coverage
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.metric_implementation.unicommerce.avg_catalogue_mrp.implements.metric.unicommerce.avg_catalogue_mrp
  source_id: metric_implementation.unicommerce.avg_catalogue_mrp
  target_id: metric.unicommerce.avg_catalogue_mrp
  edge_type: IMPLEMENTS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_1_forward_sale.has_step.01_customer_order_created
  source_id: business_process.unicommerce.9_1_forward_sale
  target_id: workflow_step.unicommerce.9_1_forward_sale.01_customer_order_created
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_1_forward_sale.has_step.02_unicommerce_receives_order
  source_id: business_process.unicommerce.9_1_forward_sale
  target_id: workflow_step.unicommerce.9_1_forward_sale.02_unicommerce_receives_order
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_1_forward_sale.has_step.03_gst_invoice_generated
  source_id: business_process.unicommerce.9_1_forward_sale
  target_id: workflow_step.unicommerce.9_1_forward_sale.03_gst_invoice_generated
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_1_forward_sale.has_step.04_manifest_dispatch
  source_id: business_process.unicommerce.9_1_forward_sale
  target_id: workflow_step.unicommerce.9_1_forward_sale.04_manifest_dispatch
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_1_forward_sale.has_step.05_awb_and_shipping_method_recorded
  source_id: business_process.unicommerce.9_1_forward_sale
  target_id: workflow_step.unicommerce.9_1_forward_sale.05_awb_and_shipping_method_recorded
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_1_forward_sale.has_step.06_delivered
  source_id: business_process.unicommerce.9_1_forward_sale
  target_id: workflow_step.unicommerce.9_1_forward_sale.06_delivered
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_2_return_to_origin_courier_return.has_step.01_delivery_attempt_failed
  source_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  target_id: workflow_step.unicommerce.9_2_rto.01_delivery_attempt_failed
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_2_return_to_origin_courier_return.has_step.02_courier_triggers_rto
  source_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  target_id: workflow_step.unicommerce.9_2_rto.02_courier_triggers_rto
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_2_return_to_origin_courier_return.has_step.03_reverse_row_created
  source_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  target_id: workflow_step.unicommerce.9_2_rto.03_reverse_row_created
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_2_return_to_origin_courier_return.has_step.04_returned_to_warehouse_resolution
  source_id: business_process.unicommerce.9_2_return_to_origin_courier_return
  target_id: workflow_step.unicommerce.9_2_rto.04_returned_to_warehouse_resolution
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_3_customer_return.has_step.01_buyer_initiates_return
  source_id: business_process.unicommerce.9_3_customer_return
  target_id: workflow_step.unicommerce.9_3_customer_return.01_buyer_initiates_return
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_3_customer_return.has_step.02_reverse_entry_created
  source_id: business_process.unicommerce.9_3_customer_return
  target_id: workflow_step.unicommerce.9_3_customer_return.02_reverse_entry_created
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_3_customer_return.has_step.03_customer_return_classified
  source_id: business_process.unicommerce.9_3_customer_return
  target_id: workflow_step.unicommerce.9_3_customer_return.03_customer_return_classified
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_3_customer_return.has_step.04_item_returned_refund_processed
  source_id: business_process.unicommerce.9_3_customer_return
  target_id: workflow_step.unicommerce.9_3_customer_return.04_item_returned_refund_processed
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_4_cancellation.has_step.01_order_cancelled_before_dispatch
  source_id: business_process.unicommerce.9_4_cancellation
  target_id: workflow_step.unicommerce.9_4_cancellation.01_order_cancelled_before_dispatch
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_4_cancellation.has_step.02_cancel_row_recorded
  source_id: business_process.unicommerce.9_4_cancellation
  target_id: workflow_step.unicommerce.9_4_cancellation.02_cancel_row_recorded
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.9_4_cancellation.has_step.03_osr_cancelled_status
  source_id: business_process.unicommerce.9_4_cancellation
  target_id: workflow_step.unicommerce.9_4_cancellation.03_osr_cancelled_status
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.osr_status_tracking.has_step.01_prefixed_order
  source_id: business_process.unicommerce.osr_status_tracking
  target_id: workflow_step.unicommerce.osr.01_prefixed_order
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.osr_status_tracking.has_step.02_awb_status
  source_id: business_process.unicommerce.osr_status_tracking
  target_id: workflow_step.unicommerce.osr.02_awb_status
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.business_process.unicommerce.gst_invoice_classification.has_step.01_classify
  source_id: business_process.unicommerce.gst_invoice_classification
  target_id: workflow_step.unicommerce.gst.01_classify
  edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.unicommerce.gmv_by_month_channel.answers.metric.unicommerce.channel_gmv
  source_id: query_pattern.unicommerce.gmv_by_month_channel
  target_id: metric.unicommerce.channel_gmv
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.unicommerce.return_rate_by_type.answers.metric.unicommerce.rto_rate
  source_id: query_pattern.unicommerce.return_rate_by_type
  target_id: metric.unicommerce.rto_rate
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.unicommerce.full_enriched_order_view.answers.metric.unicommerce.osr_join_coverage
  source_id: query_pattern.unicommerce.full_enriched_order_view
  target_id: metric.unicommerce.osr_join_coverage
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.unicommerce.delivery_rate_by_shipping_method.answers.metric.unicommerce.delivery_rate
  source_id: query_pattern.unicommerce.delivery_rate_by_shipping_method
  target_id: metric.unicommerce.delivery_rate
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
```yaml
candidate_edge:
  edge_id: edge.query_pattern.unicommerce.gst_summary.answers.metric.unicommerce.gst_amount
  source_id: query_pattern.unicommerce.gst_summary
  target_id: metric.unicommerce.gst_amount
  edge_type: ANSWERS_METRIC
  materialize_inverse: false
```
## 5. SQL Pattern Registry

```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.sales_order_count
  title: unicommerce metric sales_order_count
  evidence_refs: []
  sql: |
    SELECT COUNT(DISTINCT order_id) AS sales_order_count
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata = 'sales' AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.total_sales_gmv
  title: unicommerce metric total_sales_gmv
  evidence_refs: []
  sql: |
    SELECT SUM(charged_amount) AS total_sales_gmv
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata = 'sales' AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.total_return_value
  title: unicommerce metric total_return_value
  evidence_refs: []
  sql: |
    SELECT SUM(charged_amount) AS total_return_value
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata = 'reverse' AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.total_cancel_value
  title: unicommerce metric total_cancel_value
  evidence_refs: []
  sql: |
    SELECT SUM(charged_amount) AS total_cancel_value
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata = 'cancel' AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.net_revenue
  title: unicommerce metric net_revenue
  evidence_refs: []
  sql: |
    SELECT SUM(CASE WHEN metadata='sales' THEN charged_amount ELSE 0 END) - SUM(CASE WHEN metadata='reverse' THEN charged_amount ELSE 0 END) - SUM(CASE WHEN metadata='cancel' THEN charged_amount ELSE 0 END) AS net_revenue
    FROM zs_observe.unicommerce
    WHERE is_active = true AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.average_order_value
  title: unicommerce metric average_order_value
  evidence_refs: []
  sql: |
    SELECT SUM(charged_amount) / NULLIF(COUNT(DISTINCT order_id),0) AS average_order_value
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata = 'sales' AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.cod_share
  title: unicommerce metric cod_share
  evidence_refs: []
  sql: |
    SELECT 100.0 * COUNT(DISTINCT CASE WHEN transaction_type='COD' THEN order_id END) / NULLIF(COUNT(DISTINCT order_id),0) AS cod_share_pct
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata='sales' AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.prepaid_share
  title: unicommerce metric prepaid_share
  evidence_refs: []
  sql: |
    SELECT 100.0 * COUNT(DISTINCT CASE WHEN transaction_type='PREPAID' THEN order_id END) / NULLIF(COUNT(DISTINCT order_id),0) AS prepaid_share_pct
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata='sales' AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.rto_rate
  title: unicommerce metric rto_rate
  evidence_refs: []
  sql: |
    SELECT 100.0 * COUNT(DISTINCT CASE WHEN metadata='reverse' AND transaction_type='Courier Return' THEN order_id END) / NULLIF(COUNT(DISTINCT CASE WHEN metadata='sales' THEN order_id END),0) AS rto_rate_pct
    FROM zs_observe.unicommerce
    WHERE is_active = true AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.customer_return_rate
  title: unicommerce metric customer_return_rate
  evidence_refs: []
  sql: |
    SELECT 100.0 * COUNT(DISTINCT CASE WHEN metadata='reverse' AND transaction_type='Customer Return' THEN order_id END) / NULLIF(COUNT(DISTINCT CASE WHEN metadata='sales' THEN order_id END),0) AS customer_return_rate_pct
    FROM zs_observe.unicommerce
    WHERE is_active = true AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.cancellation_rate
  title: unicommerce metric cancellation_rate
  evidence_refs: []
  sql: |
    SELECT 100.0 * COUNT(DISTINCT CASE WHEN metadata='cancel' THEN order_id END) / NULLIF(COUNT(DISTINCT CASE WHEN metadata='sales' THEN order_id END),0) AS cancellation_rate_pct
    FROM zs_observe.unicommerce
    WHERE is_active = true AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.channel_gmv
  title: unicommerce metric channel_gmv
  evidence_refs: []
  sql: |
    SELECT sales_channel, COUNT(DISTINCT order_id) AS orders, SUM(charged_amount) AS gmv
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata='sales' AND group_level_id = 211
    GROUP BY sales_channel;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.sku_revenue
  title: unicommerce metric sku_revenue
  evidence_refs: []
  sql: |
    SELECT sku_id, description, COUNT(DISTINCT order_id) AS orders, SUM(charged_amount) AS revenue
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata='sales' AND group_level_id = 211 AND charged_amount > 1
    GROUP BY sku_id, description;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.gst_amount
  title: unicommerce metric gst_amount
  evidence_refs: []
  sql: |
    SELECT SUM(COALESCE(tax_igst_amount,0)+COALESCE(tax_cgst_amount,0)+COALESCE(tax_sgst_amount,0)+COALESCE(utgst,0)+COALESCE(cess,0)) AS gst_amount
    FROM zs_observe.unicommerce
    WHERE is_active = true AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.hsn_missing_count
  title: unicommerce metric hsn_missing_count
  evidence_refs: []
  sql: |
    SELECT COUNT(*) AS hsn_missing_count
    FROM zs_observe.unicommerce
    WHERE is_active = true AND group_level_id = 211
      AND COALESCE(hsn, hsn_generated, product_hsn_code, hsn_code) IS NULL;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.delivery_rate
  title: unicommerce metric delivery_rate
  evidence_refs: []
  sql: |
    SELECT 100.0 * COUNT_IF(order_status='DELIVERED') / NULLIF(COUNT(*),0) AS delivery_rate_pct
    FROM zs_observe.unicommerce_order_sales_report
    WHERE is_active = true AND group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.osr_join_coverage
  title: unicommerce metric osr_join_coverage
  evidence_refs: []
  sql: |
    SELECT 100.0 * COUNT(DISTINCT o.order_id) / NULLIF(COUNT(DISTINCT '#' || u.order_id),0) AS osr_join_coverage_pct
    FROM zs_observe.unicommerce u
    LEFT JOIN zs_observe.unicommerce_order_sales_report o
      ON '#' || u.order_id = o.order_id AND o.is_active = true
    WHERE u.is_active = true AND u.group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.metric.avg_catalogue_mrp
  title: unicommerce metric avg_catalogue_mrp
  evidence_refs: []
  sql: |
    SELECT AVG(mrp) AS avg_catalogue_mrp
    FROM zs_observe.unicommerce_order_sales_report
    WHERE is_active = true AND group_level_id = 211 AND order_status='DELIVERED';
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.query.gmv_by_month_channel
  title: unicommerce query gmv_by_month_channel
  evidence_refs: []
  sql: |
    SELECT DATE_TRUNC('month', created_date) AS month, sales_channel, COUNT(DISTINCT order_id) AS orders, SUM(charged_amount) AS gmv, AVG(charged_amount) AS aov
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata='sales' AND group_level_id = 211
    GROUP BY 1,2
    ORDER BY 1,3 DESC;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.query.return_rate_by_type
  title: unicommerce query return_rate_by_type
  evidence_refs: []
  sql: |
    SELECT sales_channel, COUNT(DISTINCT CASE WHEN metadata='sales' THEN order_id END) AS sold, COUNT(DISTINCT CASE WHEN metadata='reverse' AND transaction_type='Courier Return' THEN order_id END) AS rto, COUNT(DISTINCT CASE WHEN metadata='reverse' AND transaction_type='Customer Return' THEN order_id END) AS customer_returns
    FROM zs_observe.unicommerce
    WHERE is_active = true AND group_level_id = 211
    GROUP BY sales_channel;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.query.full_enriched_order_view
  title: unicommerce query full_enriched_order_view
  evidence_refs: []
  sql: |
    SELECT u.order_id, u.invoice_number, u.created_date, u.sku_id, u.description, u.quantity, u.metadata AS txn_type, u.transaction_type AS payment_type, u.charged_amount, u.discount, u.tax_igst_amount, u.sales_channel, u.source_gst_name, u.destination_state, u.destination_city, o.order_status, o.other_id AS awb, o.shipping_method, o.mrp AS catalogue_mrp
    FROM zs_observe.unicommerce u
    LEFT JOIN zs_observe.unicommerce_order_sales_report o
      ON '#' || u.order_id = o.order_id AND o.is_active = true
    WHERE u.is_active = true AND u.metadata='sales' AND u.group_level_id = 211;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.query.delivery_rate_by_shipping_method
  title: unicommerce query delivery_rate_by_shipping_method
  evidence_refs: []
  sql: |
    SELECT shipping_method, COUNT(*) AS shipments, COUNT_IF(order_status='DELIVERED') AS delivered, ROUND(100.0 * COUNT_IF(order_status='DELIVERED') / NULLIF(COUNT(*),0), 1) AS delivery_rate_pct
    FROM zs_observe.unicommerce_order_sales_report
    WHERE is_active = true AND group_level_id = 211 AND shipping_method IS NOT NULL
    GROUP BY shipping_method
    ORDER BY shipments DESC;
```
```yaml
sql_pattern:
  sql_id: sql.unicommerce.query.gst_summary
  title: unicommerce query gst_summary
  evidence_refs: []
  sql: |
    SELECT CASE WHEN tax_igst_rate > 0 THEN 'Interstate (IGST)' ELSE 'Intrastate (CGST+SGST)' END AS gst_type, COUNT(DISTINCT order_id) AS orders, SUM(charged_amount) AS gmv, SUM(tax_igst_amount) AS igst, SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst_total
    FROM zs_observe.unicommerce
    WHERE is_active = true AND metadata='sales' AND group_level_id = 211
    GROUP BY 1;
```
## 6. Parser QA Summary

```yaml
parser_quality_manifest:
  candidate_cards: 219
  candidate_edges: 152
  source_evidence_count: 11
  sql_patterns: 23
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


## 7. Process Correction Register

```yaml
process_correction_register:
  correction_id: correction.unicommerce.lifecycle_process_ids.v2
  correction_type: process_id_and_workflow_remap
  prior_issue: Earlier Unicommerce process cards used generic invoice-entry IDs and compressed the source lifecycle, which could make deterministic parsing confuse RTO, customer return, cancellation and OSR status semantics.
  corrected_process_ids:
  - process_id: unicommerce.9.1.forward_sale
    card_id: business_process.unicommerce.9_1_forward_sale
    source_section: 9.1 Forward Sale
    required_classifier: metadata = 'sales' AND transaction_type IN ('COD','PREPAID')
    osr_status_semantics: MANIFESTED -> DISPATCHED -> DELIVERED
  - process_id: unicommerce.9.2.return_to_origin_courier_return
    card_id: business_process.unicommerce.9_2_return_to_origin_courier_return
    source_section: 9.2 Return-to-Origin (RTO / Courier Return)
    required_classifier: metadata = 'reverse' AND transaction_type = 'Courier Return'
    invoice_semantics: SRFZ/SR stock-return credit-note
    osr_status_semantics: RESHIPPED if re-dispatched; CANCELLED if abandoned
  - process_id: unicommerce.9.3.customer_return
    card_id: business_process.unicommerce.9_3_customer_return
    source_section: 9.3 Customer Return
    required_classifier: metadata = 'reverse' AND transaction_type = 'Customer Return'
    amount_semantics: charged_amount is original sale value
  - process_id: unicommerce.9.4.cancellation
    card_id: business_process.unicommerce.9_4_cancellation
    source_section: 9.4 Cancellation
    required_classifier: metadata = 'cancel' AND transaction_type IN ('COD','PREPAID')
    osr_status_semantics: CANCELLED
  manifest_checks:
    evidence_anchored: true
    lazy_workflow_steps: 0
    process_variants_created: 0
    segment_only_process_variants_created: 0
    edge_references_repaired: true
```

## 7. Deterministic Cleanup Notes

- Evidence anchoring is required before card creation.
- Value labels must not become process variants unless an explicit workflow difference is documented.
- All metric implementations are SQL-like and reference declared source tables/columns.
- Scope identifiers remain scope columns/caveats only.
