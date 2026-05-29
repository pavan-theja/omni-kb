# Shiprocket Logistics Knowledge — Parser Ready v4 Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: shiprocket_logistics_parser_ready_v4_unified_edges
  title: Shiprocket Logistics Knowledge — Parser Ready v4 Unified Edges
  domain: logistics
  vendor: Shiprocket
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style
  generated_on: '2026-05-20'
  version: 4.0-unified-edges
  scope: shiprocket_vendor_logistics_with_unified_edges
  logistics_only: true
  allowed_card_types:
  - column
  - metric
  - metric_implementation
  - platform
  - platform_context
  - relationship
  - table
  - value_profile
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

## 0. Parser Instructions

This document is intended to be parsed deterministically. It is not prose-only. The parser should emit `candidate_card` blocks and `candidate_edge` blocks, normalize legacy aliases into the canonical uppercase edge taxonomy, and dedupe repeated cards by `card_id`.

Critical parser rules:

- Create only logistics-scoped reusable cards from this document.
- Do not create tenant, group, platform account, account data binding, business scope set, or business flow binding cards from generic vendor/domain documents.
- Treat scope-like fields such as `group_level_id`, `group_id`, `merchant_id`, `bank_name`, and similar values as columns/caveats only.
- Metric cards own colloquial/business meaning; metric implementation cards own platform/table-specific formulas.
- Process cards must be operational: each workflow step and state transition should identify evidence, expected state, lag/failure logic, or a review item.
- Materialize inverse edges only when `materialize_inverse: true`; otherwise use graph reverse indexes.
- Do not invent domain-specific route-binding edges. Use Business Flow Binding only in separate business-flow applicability docs.

## 1. Source Intake and Evidence Registry

```yaml
source_evidence:
  id: evidence.logistics_kb_doc
  source_document: Logistics KB Doc.docx
  summary: Primary logistics/courier KB covering order flow, money flow, table statuses, join keys, vendor roles, amount semantics,
    and reconciliation hierarchy.
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
  summary: Canonical edge taxonomy, inverse edge policy, legacy edge aliases, and domain-specific use guidance for logistics/payment/bank/ERP
    docs.
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
  summary: Logistics domain authoring boundary, business flow binding handoff, amount semantics, table block structure, and
    logistics card scope.
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
  instruction: Do not create tenant, group, platform_account, account_data_binding, business_scope_set, or business_flow_binding
    cards from generic logistics files. Use business flow applicability docs for that layer.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.account_filters
  topic: Account filters and group_level_id values
  instruction: Treat group_level_id, merchant_id, bank_name, and similar scope fields as source columns or caveats only unless
    a dedicated Account Data Binding doc is being authored.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.bank_statement_execution
  topic: Bank statement execution
  instruction: Generic logistics docs can expose UTR and bank-reference bridge fields, but actual bank account selection and
    bank statement matching require Banking KB plus Business Flow Binding.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.unsupported_native_tables
  topic: Unsupported native courier tables
  instruction: Do not create fake native table evidence for Shadowfax or Ecom Express; use indirect/fallback evidence only
    where documented.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```

## 3. Compact Semantic Field Contract

| card family | required semantic intent |
|---|---|
| `platform/platform_context` | platform identity, region/context, platform_type, source codes, evidence refs |
| `table/column/value_profile` | grain, amount semantics, join/filter roles, coverage status, known values, caveats |
| `relationship` | source/target table, join keys, cardinality, safe usage, aggregation risk |
| `metric/metric_implementation` | colloquial metric meaning vs vendor/table formula, metric_pattern, required columns, filters, allowed grains |
| `business_process/workflow_step/state_transition/process_variant` | lifecycle, evidence-bearing checkpoint, from/to state, lag/failure logic, operating-model variant |
| `reconciliation cards` | profile, expected/actual sides, unit, matching logic, mismatch category, variants |
| `execution guidance` | query pattern, rule, validation test, output contract, constraint set |

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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account,
      account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
```

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shiprocket_invoice
  name: Shiprocket Invoice
  fields:
    name: Shiprocket Invoice
    description: 'Shiprocket Invoice: One row per AWB-level Shiprocket freight invoice.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    schema: zs_observe
    table_name: shiprocket_invoice
    full_reference: zs_observe.shiprocket_invoice
    engine: Athena v3 / Trino SQL
    table_type: freight_invoice
    source_platform_ids:
    - platform.shiprocket
    source_platform_types:
    - logistics
    business_purpose: One row per AWB-level Shiprocket freight invoice.
    grain: One row per AWB-level Shiprocket freight invoice.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.shiprocket; account filters are not defined here
    coverage_status: active
    row_count: '5038'
    period: Jan-Oct 2025
    group_ids: '203'
    schema_coverage: curated_key_fields
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account,
      account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
```

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shiprocket_settlement
  name: Shiprocket Settlement
  fields:
    name: Shiprocket Settlement
    description: 'Shiprocket Settlement: One row per AWB-level Shiprocket COD settlement.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    schema: zs_observe
    table_name: shiprocket_settlement
    full_reference: zs_observe.shiprocket_settlement
    engine: Athena v3 / Trino SQL
    table_type: cod_settlement
    source_platform_ids:
    - platform.shiprocket
    source_platform_types:
    - logistics
    business_purpose: One row per AWB-level Shiprocket COD settlement.
    grain: One row per AWB-level Shiprocket COD settlement.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.shiprocket; account filters are not defined here
    coverage_status: active
    row_count: '1200'
    period: Jan-Nov 2025
    group_ids: '203'
    schema_coverage: curated_key_fields
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account,
      account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
```

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shiprocket_settlement_report
  name: Shiprocket Settlement Report
  fields:
    name: Shiprocket Settlement Report
    description: 'Shiprocket Settlement Report: Schema-only detailed settlement report; zero rows loaded.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    schema: zs_observe
    table_name: shiprocket_settlement_report
    full_reference: zs_observe.shiprocket_settlement_report
    engine: Athena v3 / Trino SQL
    table_type: schema_only_report
    source_platform_ids:
    - platform.shiprocket
    source_platform_types:
    - logistics
    business_purpose: Schema-only detailed settlement report; zero rows loaded.
    grain: Schema-only detailed settlement report; zero rows loaded.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.shiprocket; account filters are not defined here
    coverage_status: empty_schema_only
    row_count: '0'
    period: '-'
    group_ids: '-'
    schema_coverage: schema_only
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account,
      account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.order_id
  name: shiprocket_invoice.order_id
  fields:
    name: shiprocket_invoice.order_id
    description: Shiprocket order ID.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Shiprocket order ID.
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
  card_id: column.zs_observe.shiprocket_invoice.other_id
  name: shiprocket_invoice.other_id
  fields:
    name: shiprocket_invoice.other_id
    description: AWB number; joins to shiprocket_oms.awb_code.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: other_id
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - AWB number
    - joins to shiprocket_oms.awb_code.
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
  card_id: column.zs_observe.shiprocket_invoice.courier_partner
  name: shiprocket_invoice.courier_partner
  fields:
    name: shiprocket_invoice.courier_partner
    description: 'Actual courier used: DTDC Air, Delhivery Air, Xpressbees Air, Ekart Logistics Air, Ecom Air.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: courier_partner
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - 'Actual courier used: DTDC Air, Delhivery Air, Xpressbees Air, Ekart Logistics Air, Ecom Air.'
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
  card_id: column.zs_observe.shiprocket_invoice.order_status
  name: shiprocket_invoice.order_status
  fields:
    name: shiprocket_invoice.order_status
    description: DELIVERED, RTO DELIVERED, LOST.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: order_status
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - DELIVERED, RTO DELIVERED, LOST.
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
  card_id: column.zs_observe.shiprocket_invoice.zone
  name: shiprocket_invoice.zone
  fields:
    name: shiprocket_invoice.zone
    description: Delivery zone a/b/c/d.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: zone
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - Delivery zone a/b/c/d.
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
  card_id: column.zs_observe.shiprocket_invoice.payment_mode
  name: shiprocket_invoice.payment_mode
  fields:
    name: shiprocket_invoice.payment_mode
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
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: payment_mode
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
  card_id: column.zs_observe.shiprocket_invoice.charged_amount
  name: shiprocket_invoice.charged_amount
  fields:
    name: shiprocket_invoice.charged_amount
    description: Total freight bill for this AWB.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Total freight bill for this AWB.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: freight_billed_amount
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
  card_id: column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
  name: shiprocket_invoice.charged_amount_excluding_tax
  fields:
    name: shiprocket_invoice.charged_amount_excluding_tax
    description: Freight before GST.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charged_amount_excluding_tax
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Freight before GST.
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
  card_id: column.zs_observe.shiprocket_invoice.total_tax
  name: shiprocket_invoice.total_tax
  fields:
    name: shiprocket_invoice.total_tax
    description: GST/tax on freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: total_tax
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - GST/tax on freight.
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
  card_id: column.zs_observe.shiprocket_invoice.charge_fsc
  name: shiprocket_invoice.charge_fsc
  fields:
    name: shiprocket_invoice.charge_fsc
    description: Fuel surcharge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_fsc
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Fuel surcharge.
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
  card_id: column.zs_observe.shiprocket_invoice.charge_rto
  name: shiprocket_invoice.charge_rto
  fields:
    name: shiprocket_invoice.charge_rto
    description: RTO charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_rto
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - RTO charge.
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
  card_id: column.zs_observe.shiprocket_invoice.charge_cod
  name: shiprocket_invoice.charge_cod
  fields:
    name: shiprocket_invoice.charge_cod
    description: COD handling fee.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_cod
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD handling fee.
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
  card_id: column.zs_observe.shiprocket_invoice.charge_cod_adjust
  name: shiprocket_invoice.charge_cod_adjust
  fields:
    name: shiprocket_invoice.charge_cod_adjust
    description: COD adjustment.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_cod_adjust
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD adjustment.
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
  card_id: column.zs_observe.shiprocket_invoice.charge_dl
  name: shiprocket_invoice.charge_dl
  fields:
    name: shiprocket_invoice.charge_dl
    description: Delivery charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_dl
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Delivery charge.
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
  card_id: column.zs_observe.shiprocket_invoice.final_weight
  name: shiprocket_invoice.final_weight
  fields:
    name: shiprocket_invoice.final_weight
    description: Actual/final weight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: final_weight
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Actual/final weight.
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
  card_id: column.zs_observe.shiprocket_invoice.charged_weight
  name: shiprocket_invoice.charged_weight
  fields:
    name: shiprocket_invoice.charged_weight
    description: Billable weight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charged_weight
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Billable weight.
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
  card_id: column.zs_observe.shiprocket_invoice.settled_amount
  name: shiprocket_invoice.settled_amount
  fields:
    name: shiprocket_invoice.settled_amount
    description: Net freight settled after deductions.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: settled_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Net freight settled after deductions.
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
  card_id: column.zs_observe.shiprocket_invoice.referal_fee
  name: shiprocket_invoice.referal_fee
  fields:
    name: shiprocket_invoice.referal_fee
    description: Shiprocket referral/platform fee.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: referal_fee
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Shiprocket referral/platform fee.
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
  card_id: column.zs_observe.shiprocket_invoice.mp_sin
  name: shiprocket_invoice.mp_sin
  fields:
    name: shiprocket_invoice.mp_sin
    description: Shiprocket internal order reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: mp_sin
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Shiprocket internal order reference.
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
  card_id: column.zs_observe.shiprocket_invoice.source_zipcode
  name: shiprocket_invoice.source_zipcode
  fields:
    name: shiprocket_invoice.source_zipcode
    description: Origin pincode.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: source_zipcode
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Origin pincode.
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
  card_id: column.zs_observe.shiprocket_invoice.destination_zipcode
  name: shiprocket_invoice.destination_zipcode
  fields:
    name: shiprocket_invoice.destination_zipcode
    description: Destination pincode.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: destination_zipcode
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Destination pincode.
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
  card_id: column.zs_observe.shiprocket_invoice.is_active
  name: shiprocket_invoice.is_active
  fields:
    name: shiprocket_invoice.is_active
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
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
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
  card_id: column.zs_observe.shiprocket_invoice.group_level_id
  name: shiprocket_invoice.group_level_id
  fields:
    name: shiprocket_invoice.group_level_id
    description: Observed account/group scope candidate.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_name: group_level_id
    data_type: unknown
    semantic_roles: scope_filter
    business_concepts:
    - Observed account/group scope candidate.
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
  card_id: column.zs_observe.shiprocket_settlement.order_id
  name: shiprocket_settlement.order_id
  fields:
    name: shiprocket_settlement.order_id
    description: Shiprocket order ID.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Shiprocket order ID.
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
  card_id: column.zs_observe.shiprocket_settlement.awb_number
  name: shiprocket_settlement.awb_number
  fields:
    name: shiprocket_settlement.awb_number
    description: AWB; joins to shiprocket_oms.awb_code and shiprocket_invoice.other_id.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
    column_name: awb_number
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - AWB
    - joins to shiprocket_oms.awb_code and shiprocket_invoice.other_id.
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
  card_id: column.zs_observe.shiprocket_settlement.courier_partner
  name: shiprocket_settlement.courier_partner
  fields:
    name: shiprocket_settlement.courier_partner
    description: Courier that collected COD.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
    column_name: courier_partner
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - Courier that collected COD.
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
  card_id: column.zs_observe.shiprocket_settlement.charged_amount
  name: shiprocket_settlement.charged_amount
  fields:
    name: shiprocket_settlement.charged_amount
    description: COD amount collected/remitted from customer.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount collected/remitted from customer.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: cod_collected_or_remitted_amount
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
  card_id: column.zs_observe.shiprocket_settlement.delivered_date
  name: shiprocket_settlement.delivered_date
  fields:
    name: shiprocket_settlement.delivered_date
    description: Date of delivery.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
    column_name: delivered_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Date of delivery.
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
  card_id: column.zs_observe.shiprocket_settlement.settlement_date
  name: shiprocket_settlement.settlement_date
  fields:
    name: shiprocket_settlement.settlement_date
    description: COD settlement/remittance date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
    column_name: settlement_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - COD settlement/remittance date.
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
  card_id: column.zs_observe.shiprocket_settlement.is_active
  name: shiprocket_settlement.is_active
  fields:
    name: shiprocket_settlement.is_active
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
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
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
  card_id: column.zs_observe.shiprocket_settlement.group_level_id
  name: shiprocket_settlement.group_level_id
  fields:
    name: shiprocket_settlement.group_level_id
    description: Observed account/group scope candidate.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
    column_name: group_level_id
    data_type: unknown
    semantic_roles: scope_filter
    business_concepts:
    - Observed account/group scope candidate.
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
  card_id: column.zs_observe.shiprocket_settlement_report.order_id
  name: shiprocket_settlement_report.order_id
  fields:
    name: shiprocket_settlement_report.order_id
    description: Order reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Order reference.
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
  card_id: column.zs_observe.shiprocket_settlement_report.courier_partner
  name: shiprocket_settlement_report.courier_partner
  fields:
    name: shiprocket_settlement_report.courier_partner
    description: Courier name.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: courier_partner
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Courier name.
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
  card_id: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  name: shiprocket_settlement_report.awb_remittance_status
  fields:
    name: shiprocket_settlement_report.awb_remittance_status
    description: Status of AWB-level remittance.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: awb_remittance_status
    data_type: unknown
    semantic_roles: status
    business_concepts:
    - Status of AWB-level remittance.
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
  card_id: column.zs_observe.shiprocket_settlement_report.courier_received_amount
  name: shiprocket_settlement_report.courier_received_amount
  fields:
    name: shiprocket_settlement_report.courier_received_amount
    description: Amount courier received versus expected.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: courier_received_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Amount courier received versus expected.
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
  card_id: column.zs_observe.shiprocket_settlement_report.settlement_id
  name: shiprocket_settlement_report.settlement_id
  fields:
    name: shiprocket_settlement_report.settlement_id
    description: Batch settlement identifier.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: settlement_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Batch settlement identifier.
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
  card_id: column.zs_observe.shiprocket_settlement_report.source_gst_name
  name: shiprocket_settlement_report.source_gst_name
  fields:
    name: shiprocket_settlement_report.source_gst_name
    description: GST entity name.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: source_gst_name
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - GST entity name.
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
  card_id: column.zs_observe.shiprocket_settlement_report.source_gst_id
  name: shiprocket_settlement_report.source_gst_id
  fields:
    name: shiprocket_settlement_report.source_gst_id
    description: GST identifier.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: source_gst_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - GST identifier.
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
  card_id: column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
  name: shiprocket_settlement_report.offer_adjustment_settled_amount
  fields:
    name: shiprocket_settlement_report.offer_adjustment_settled_amount
    description: Offer adjustment amount settled.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: offer_adjustment_settled_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Offer adjustment amount settled.
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
  card_id: column.zs_observe.shiprocket_settlement_report.parent_id
  name: shiprocket_settlement_report.parent_id
  fields:
    name: shiprocket_settlement_report.parent_id
    description: Parent order reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: parent_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Parent order reference.
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

### 4.6 relationship cards

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_oms.shiprocket_invoice.awb
  name: shiprocket_oms to shiprocket_invoice by awb
  fields:
    name: shiprocket_oms to shiprocket_invoice by awb
    description: Validate shipments have freight invoice evidence.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shiprocket_oms
    target_table: table.zs_observe.shiprocket_invoice
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = other_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Validate shipments have freight invoice evidence.
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
  card_id: relationship.shiprocket_oms.shiprocket_settlement.awb
  name: shiprocket_oms to shiprocket_settlement by awb
  fields:
    name: shiprocket_oms to shiprocket_settlement by awb
    description: Validate COD shipments have COD settlement evidence.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shiprocket_oms
    target_table: table.zs_observe.shiprocket_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = awb_number
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Validate COD shipments have COD settlement evidence.
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
  card_id: relationship.shiprocket_invoice.shiprocket_settlement.awb
  name: shiprocket_invoice to shiprocket_settlement by awb
  fields:
    name: shiprocket_invoice to shiprocket_settlement by awb
    description: Cross-check freight invoice and COD settlement for same AWB.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shiprocket_invoice
    target_table: table.zs_observe.shiprocket_settlement
    relationship_type: join; reconciliation_relation
    join_keys: other_id = awb_number
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check freight invoice and COD settlement for same AWB.
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
  card_id: relationship.shiprocket_settlement.delhivery_settlement.awb
  name: shiprocket_settlement to delhivery_settlement by awb
  fields:
    name: shiprocket_settlement to delhivery_settlement by awb
    description: Compare Shiprocket aggregated Delhivery COD to direct Delhivery settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shiprocket_settlement
    target_table: table.zs_observe.delhivery_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_number = waybill_num
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Compare Shiprocket aggregated Delhivery COD to direct Delhivery settlement.
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
    version: 3.0-expansive
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
  card_id: relationship.shiprocket_invoice.dtdc_settlement.awb
  name: shiprocket_invoice to dtdc_settlement by awb
  fields:
    name: shiprocket_invoice to dtdc_settlement by awb
    description: Cross-check Shiprocket DTDC freight invoices with DTDC COD settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shiprocket_invoice
    target_table: table.zs_observe.dtdc_settlement
    relationship_type: join; reconciliation_relation
    join_keys: other_id = airwaybill_number
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check Shiprocket DTDC freight invoices with DTDC COD settlement.
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
  card_id: relationship.shiprocket_invoice.ekart_settlement.awb
  name: shiprocket_invoice to ekart_settlement by awb
  fields:
    name: shiprocket_invoice to ekart_settlement by awb
    description: Cross-check Shiprocket Ekart freight rows to Ekart settlement when present.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shiprocket_invoice
    target_table: table.zs_observe.ekart_settlement
    relationship_type: join; reconciliation_relation
    join_keys: other_id = shipment_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check Shiprocket Ekart freight rows to Ekart settlement when present.
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
    version: 3.0-expansive
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

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_settlement.xpressbees_settlement.awb
  name: shiprocket_settlement to xpressbees_settlement by awb
  fields:
    name: shiprocket_settlement to xpressbees_settlement by awb
    description: Compare Shiprocket XpressBees COD fallback with sparse native table.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shiprocket_settlement
    target_table: table.zs_observe.xpressbees_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_number = shipping_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Compare Shiprocket XpressBees COD fallback with sparse native table.
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
  card_id: relationship.shiprocket_invoice.xpressbees_settlement.awb
  name: shiprocket_invoice to xpressbees_settlement by awb
  fields:
    name: shiprocket_invoice to xpressbees_settlement by awb
    description: Cross-check Shiprocket XpressBees freight with sparse native table.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shiprocket_invoice
    target_table: table.zs_observe.xpressbees_settlement
    relationship_type: join; reconciliation_relation
    join_keys: other_id = shipping_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check Shiprocket XpressBees freight with sparse native table.
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
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_oms
    column_id: column.zs_observe.shiprocket_oms.transaction_type
    value_type: enum_or_enum_with_nulls
    values: forward=Outbound shipment (forward); return=Customer/reverse return (return); cancelled=Cancelled before dispatch
      (cancel); in transit=Shipment in transit (active); damaged/lost=Damaged or lost shipment (exception)
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
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_oms
    column_id: column.zs_observe.shiprocket_oms.status
    value_type: enum_or_enum_with_nulls
    values: DELIVERED=Delivered to customer (delivered); RTO DELIVERED=Returned to origin (rto); RETURN DELIVERED=Customer
      return delivered (return); CANCELLED=Cancelled (cancel); DAMAGED/LOST=Damaged or lost (exception)
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
    version: 3.0-expansive
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
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_oms
    column_id: column.zs_observe.shiprocket_oms.courier_company
    value_type: enum_or_enum_with_nulls
    values: Ekart_Direct SFC=Ekart direct/FBF-like logistics (ekart); Delhivery_SFC _Direct=Delhivery direct (delhivery);
      Dlv_Direct_SFC=Delhivery direct alternate (delhivery); Xbees_Direct_AIR=XpressBees air (xpressbees); Shadowfax Direct
      Rev QC=Shadowfax reverse QC only (shadowfax)
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
  card_id: value_profile.shiprocket_invoice.courier_partner
  name: shiprocket_invoice.courier_partner Value Profile
  fields:
    name: shiprocket_invoice.courier_partner Value Profile
    description: Known values and meanings for shiprocket_invoice.courier_partner.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_id: column.zs_observe.shiprocket_invoice.courier_partner
    value_type: enum_or_enum_with_nulls
    values: DTDC Air 500gm=DTDC via Shiprocket (dtdc); Delhivery Air=Delhivery via Shiprocket (delhivery); Xpressbees Air=XpressBees
      via Shiprocket (xpressbees); Ekart Logistics Air=Ekart via Shiprocket (ekart); Ecom Air 500gm=Ecom Express via Shiprocket
      (ecom)
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
  card_id: value_profile.shiprocket_invoice.order_status
  name: shiprocket_invoice.order_status Value Profile
  fields:
    name: shiprocket_invoice.order_status Value Profile
    description: Known values and meanings for shiprocket_invoice.order_status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_id: column.zs_observe.shiprocket_invoice.order_status
    value_type: enum_or_enum_with_nulls
    values: DELIVERED=Delivered shipment invoice (delivered); RTO DELIVERED=RTO shipment invoice (rto); LOST=Lost shipment
      invoice (exception)
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
  card_id: value_profile.shiprocket_invoice.payment_mode
  name: shiprocket_invoice.payment_mode Value Profile
  fields:
    name: shiprocket_invoice.payment_mode Value Profile
    description: Known values and meanings for shiprocket_invoice.payment_mode.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_id: column.zs_observe.shiprocket_invoice.payment_mode
    value_type: enum_or_enum_with_nulls
    values: prepaid=Prepaid shipment (prepaid); cod=COD shipment (cod)
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
  card_id: value_profile.shiprocket_invoice.zone
  name: shiprocket_invoice.zone Value Profile
  fields:
    name: shiprocket_invoice.zone Value Profile
    description: Known values and meanings for shiprocket_invoice.zone.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_invoice
    column_id: column.zs_observe.shiprocket_invoice.zone
    value_type: enum_or_enum_with_nulls
    values: a=Local/near zone (zone_a); b=Regional zone (zone_b); c=Medium distance zone (zone_c); d=Farthest/dominant zone
      (zone_d)
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
  card_id: value_profile.shiprocket_settlement.courier_partner
  name: shiprocket_settlement.courier_partner Value Profile
  fields:
    name: shiprocket_settlement.courier_partner Value Profile
    description: Known values and meanings for shiprocket_settlement.courier_partner.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement
    column_id: column.zs_observe.shiprocket_settlement.courier_partner
    value_type: enum_or_enum_with_nulls
    values: Delhivery Air=Delhivery COD via Shiprocket (delhivery); DTDC Air 500gm=DTDC COD via Shiprocket (dtdc); Xpressbees
      Air=XpressBees COD via Shiprocket (xpressbees); Ekart Logistics Air=Ekart COD via Shiprocket (ekart); Ecom Air 500gm=Ecom
      COD via Shiprocket (ecom)
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
  card_id: value_profile.shiprocket_settlement_report.awb_remittance_status
  name: shiprocket_settlement_report.awb_remittance_status Value Profile
  fields:
    name: shiprocket_settlement_report.awb_remittance_status Value Profile
    description: Known values and meanings for shiprocket_settlement_report.awb_remittance_status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shiprocket_settlement_report
    column_id: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
    value_type: enum_or_enum_with_nulls
    values: schema_only=Status values unavailable until rows load (schema_only)
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
  card_id: metric.actual_weight
  name: Actual Weight
  fields:
    name: Actual Weight
    description: Actual or final weight of shipment.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Actual Weight
    aliases:
    - final weight
    - physical weight
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - actual_weight
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.average_freight_per_awb
  name: Average Freight per AWB
  fields:
    name: Average Freight per AWB
    description: Freight billed divided by unique AWB count.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Average Freight per AWB
    aliases:
    - average shipping cost
    - avg freight
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - average_freight_per_awb
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.batch_settlement_amount
  name: Batch Settlement Amount
  fields:
    name: Batch Settlement Amount
    description: Amount for a settlement/remittance batch.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Batch Settlement Amount
    aliases:
    - settlement batch amount
    - batch total
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - batch_settlement_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.billable_weight
  name: Billable Weight
  fields:
    name: Billable Weight
    description: Billable or charged weight used for freight calculation.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Billable Weight
    aliases:
    - charged weight
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - billable_weight
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_collected_amount
  name: COD Collected Amount
  fields:
    name: COD Collected Amount
    description: Cash/COD amount collected by courier from customer.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: COD Collected Amount
    aliases:
    - cash collected
    - COD collected
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_collected_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_fee_amount
  name: COD Fee Amount
  fields:
    name: COD Fee Amount
    description: Fee charged for COD handling or collection.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: COD Fee Amount
    aliases:
    - COD handling fee
    - COD collection charge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_fee_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.forward_freight_amount
  name: Forward Freight Amount
  fields:
    name: Forward Freight Amount
    description: Forward delivery freight amount.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Forward Freight Amount
    aliases:
    - delivery charge
    - forward freight
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - forward_freight_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.freight_billed_amount
  name: Freight Billed Amount
  fields:
    name: Freight Billed Amount
    description: Total freight charged for shipments.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Freight Billed Amount
    aliases:
    - freight charged
    - shipping cost
    - courier charges
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - freight_billed_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.freight_excluding_tax_amount
  name: Freight Excluding Tax Amount
  fields:
    name: Freight Excluding Tax Amount
    description: Freight amount before tax.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Freight Excluding Tax Amount
    aliases:
    - pre GST freight
    - freight before GST
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - freight_excluding_tax_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.fuel_surcharge_amount
  name: Fuel Surcharge Amount
  fields:
    name: Fuel Surcharge Amount
    description: Fuel surcharge component of freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Fuel Surcharge Amount
    aliases:
    - FSC
    - fuel surcharge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - fuel_surcharge_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.gst_on_freight_amount
  name: GST on Freight Amount
  fields:
    name: GST on Freight Amount
    description: GST or tax applied to freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: GST on Freight Amount
    aliases:
    - freight tax
    - GST on courier charges
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - gst_on_freight_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.rto_freight_amount
  name: RTO Freight Amount
  fields:
    name: RTO Freight Amount
    description: Freight amount charged for return-to-origin movement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: RTO Freight Amount
    aliases:
    - return freight
    - RTO charge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - rto_freight_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    - see metric_impl blocks in shiprocket_logistics_parser_ready_v3_expansive.md
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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
    version: 3.0-expansive
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

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.freight_billed_amount
  name: Shiprocket Freight Billed Amount Implementation
  fields:
    name: Shiprocket Freight Billed Amount Implementation
    description: Freight Billed Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.freight_billed_amount
    implementation_name: Shiprocket Freight Billed Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_amount
    semantic_filters: []
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  name: Shiprocket Freight Excluding Tax Amount Implementation
  fields:
    name: Shiprocket Freight Excluding Tax Amount Implementation
    description: Freight Excluding Tax Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.freight_excluding_tax_amount
    implementation_name: Shiprocket Freight Excluding Tax Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
    semantic_filters: []
    formula_description: SUM(charged_amount_excluding_tax)
    formula_sql: SUM(charged_amount_excluding_tax)
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.gst_on_freight_amount
  name: Shiprocket GST on Freight Amount Implementation
  fields:
    name: Shiprocket GST on Freight Amount Implementation
    description: GST on Freight Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.gst_on_freight_amount
    implementation_name: Shiprocket GST on Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.total_tax
    semantic_filters: []
    formula_description: SUM(total_tax)
    formula_sql: SUM(total_tax)
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  name: Shiprocket Fuel Surcharge Amount Implementation
  fields:
    name: Shiprocket Fuel Surcharge Amount Implementation
    description: Fuel Surcharge Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.fuel_surcharge_amount
    implementation_name: Shiprocket Fuel Surcharge Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charge_fsc
    semantic_filters: []
    formula_description: SUM(charge_fsc)
    formula_sql: SUM(charge_fsc)
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.rto_freight_amount
  name: Shiprocket RTO Freight Amount Implementation
  fields:
    name: Shiprocket RTO Freight Amount Implementation
    description: RTO Freight Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.rto_freight_amount
    implementation_name: Shiprocket RTO Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charge_rto
    semantic_filters: []
    formula_description: SUM(charge_rto)
    formula_sql: SUM(charge_rto)
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.cod_fee_amount
  name: Shiprocket COD Fee Amount Implementation
  fields:
    name: Shiprocket COD Fee Amount Implementation
    description: COD Fee Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.cod_fee_amount
    implementation_name: Shiprocket COD Fee Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charge_cod
    semantic_filters: []
    formula_description: SUM(charge_cod)
    formula_sql: SUM(charge_cod)
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.forward_freight_amount
  name: Shiprocket Forward Freight Amount Implementation
  fields:
    name: Shiprocket Forward Freight Amount Implementation
    description: Forward Freight Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.forward_freight_amount
    implementation_name: Shiprocket Forward Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charge_dl
    semantic_filters: []
    formula_description: SUM(charge_dl)
    formula_sql: SUM(charge_dl)
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.actual_weight
  name: Shiprocket Actual Weight Implementation
  fields:
    name: Shiprocket Actual Weight Implementation
    description: Actual Weight implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.actual_weight
    implementation_name: Shiprocket Actual Weight
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.final_weight
    semantic_filters: []
    formula_description: SUM(final_weight)
    formula_sql: SUM(final_weight)
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.billable_weight
  name: Shiprocket Billable Weight Implementation
  fields:
    name: Shiprocket Billable Weight Implementation
    description: Billable Weight implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.billable_weight
    implementation_name: Shiprocket Billable Weight
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_weight
    semantic_filters: []
    formula_description: SUM(charged_weight)
    formula_sql: SUM(charged_weight)
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
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.average_freight_per_awb
  name: Shiprocket Average Freight per AWB Implementation
  fields:
    name: Shiprocket Average Freight per AWB Implementation
    description: Average Freight per AWB implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.average_freight_per_awb
    implementation_name: Shiprocket Average Freight per AWB
    metric_pattern: ratio_sum_to_distinct_awb
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_amount
    - column.zs_observe.shiprocket_invoice.other_id
    semantic_filters: []
    formula_description: SUM(charged_amount)/NULLIF(COUNT(DISTINCT other_id),0)
    formula_sql: SUM(charged_amount)/NULLIF(COUNT(DISTINCT other_id),0)
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
    - invoice_date_or_period
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
  card_id: metric_impl.shiprocket_settlement.cod_collected_amount
  name: Shiprocket COD Collected Amount Implementation
  fields:
    name: Shiprocket COD Collected Amount Implementation
    description: COD Collected Amount implementation for Shiprocket using shiprocket_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.cod_collected_amount
    implementation_name: Shiprocket COD Collected Amount
    metric_pattern: settlement_sum_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.charged_amount
    semantic_filters: []
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
    - settlement_date
    - delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_settlement means COD collected/remitted, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.cod_remitted_amount
  name: Shiprocket COD Remitted Amount Implementation
  fields:
    name: Shiprocket COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Shiprocket using shiprocket_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.cod_remitted_amount
    implementation_name: Shiprocket COD Remitted Amount
    metric_pattern: settlement_sum_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.charged_amount
    semantic_filters: []
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
    - settlement_date
    - delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_settlement means COD collected/remitted, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  name: Shiprocket COD Remittance Lag Days Implementation
  fields:
    name: Shiprocket COD Remittance Lag Days Implementation
    description: COD Remittance Lag Days implementation for Shiprocket using shiprocket_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.cod_remittance_lag_days
    implementation_name: Shiprocket COD Remittance Lag Days
    metric_pattern: settlement_sum_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.delivered_date
    - column.zs_observe.shiprocket_settlement.settlement_date
    semantic_filters: []
    formula_description: AVG(DATE_DIFF('day', delivered_date, settlement_date))
    formula_sql: AVG(DATE_DIFF('day', delivered_date, settlement_date))
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
    - settlement_date
    - delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_settlement means COD collected/remitted, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.unique_awb_count
  name: Shiprocket Unique AWB Count Implementation
  fields:
    name: Shiprocket Unique AWB Count Implementation
    description: Unique AWB Count implementation for Shiprocket using shiprocket_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.unique_awb_count
    implementation_name: Shiprocket Unique AWB Count
    metric_pattern: settlement_sum_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.awb_number
    semantic_filters: []
    formula_description: COUNT(DISTINCT awb_number)
    formula_sql: COUNT(DISTINCT awb_number)
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
    - settlement_date
    - delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_settlement means COD collected/remitted, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  name: Shiprocket COD Remitted Amount Implementation
  fields:
    name: Shiprocket COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Shiprocket using shiprocket_settlement_report.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.cod_remitted_amount
    implementation_name: Shiprocket COD Remitted Amount
    metric_pattern: unsupported_schema_only
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement_report; account filters via Account Data Binding
      only
    base_tables:
    - table.zs_observe.shiprocket_settlement_report
    required_columns:
    - column.zs_observe.shiprocket_settlement_report.settlement_id
    semantic_filters: []
    formula_description: UNSUPPORTED_EMPTY_TABLE
    formula_sql: UNSUPPORTED_EMPTY_TABLE
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
    - none
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: shiprocket_settlement_report has zero rows; retain schema only until data loads.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  name: Shiprocket Batch Settlement Amount Implementation
  fields:
    name: Shiprocket Batch Settlement Amount Implementation
    description: Batch Settlement Amount implementation for Shiprocket using shiprocket_settlement_report.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_id: metric.batch_settlement_amount
    implementation_name: Shiprocket Batch Settlement Amount
    metric_pattern: unsupported_schema_only
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement_report; account filters via Account Data Binding
      only
    base_tables:
    - table.zs_observe.shiprocket_settlement_report
    required_columns:
    - column.zs_observe.shiprocket_settlement_report.settlement_id
    semantic_filters: []
    formula_description: UNSUPPORTED_EMPTY_TABLE
    formula_sql: UNSUPPORTED_EMPTY_TABLE
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
    - none
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: shiprocket_settlement_report has zero rows; retain schema only until data loads.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
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
  generic_logistics_boundary: Generic vendor/domain docs must not emit tenant, group, platform account, account data binding,
    business scope set, or business flow binding cards.
```

### 5.1 Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.metric.actual_weight.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.actual_weight
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
  edge_id: edge.metric.average_freight_per_awb.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.average_freight_per_awb
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
  edge_id: edge.metric.batch_settlement_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.batch_settlement_amount
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
  edge_id: edge.metric.billable_weight.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.billable_weight
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
  edge_id: edge.metric.cod_collected_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_collected_amount
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
  edge_id: edge.metric.cod_fee_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_fee_amount
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
  edge_id: edge.metric.forward_freight_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.forward_freight_amount
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
  edge_id: edge.metric.freight_billed_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.freight_billed_amount
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
  edge_id: edge.metric.freight_excluding_tax_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.freight_excluding_tax_amount
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
  edge_id: edge.metric.fuel_surcharge_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.fuel_surcharge_amount
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
  edge_id: edge.metric.gst_on_freight_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.gst_on_freight_amount
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
  edge_id: edge.metric.rto_freight_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.rto_freight_amount
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.sourced_from_platform.platform.shiprocket
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.applies_to_platform.platform.shiprocket
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.order_id
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.order_id.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.order_id
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.other_id
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.other_id.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.other_id
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.other_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.courier_partner
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.courier_partner
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.courier_partner.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.courier_partner
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.courier_partner
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.order_status
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.order_status
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.order_status.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.order_status
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.order_status
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.zone
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.zone
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.zone.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.zone
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.zone
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.payment_mode
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.payment_mode
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.payment_mode.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.payment_mode
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.payment_mode
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charged_amount
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.charged_amount.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charged_amount
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.total_tax
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.total_tax
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.total_tax.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.total_tax
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.total_tax
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_fsc
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_fsc
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_fsc.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_fsc
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_fsc
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_rto
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_rto
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_rto.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_rto
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_rto
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_cod
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_cod
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_cod.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_cod
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_cod
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_cod_adjust
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_cod_adjust
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_cod_adjust.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_cod_adjust
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_cod_adjust
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_dl
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_dl
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_dl.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_dl
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_dl
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.final_weight
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.final_weight
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.final_weight.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.final_weight
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.final_weight
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_weight
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charged_weight
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.charged_weight.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charged_weight
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_weight
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.settled_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.settled_amount
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.settled_amount.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.settled_amount
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.settled_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.referal_fee
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.referal_fee
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.referal_fee.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.referal_fee
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.referal_fee
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.mp_sin
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.mp_sin
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.mp_sin.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.mp_sin
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.mp_sin
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.source_zipcode
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.source_zipcode
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.source_zipcode.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.source_zipcode
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.source_zipcode
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.destination_zipcode
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.destination_zipcode
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.destination_zipcode.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.destination_zipcode
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.destination_zipcode
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.is_active
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.is_active.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.is_active
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.is_active
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.group_level_id
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.group_level_id.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.group_level_id
  target: table.zs_observe.shiprocket_invoice
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
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.group_level_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.sourced_from_platform.platform.shiprocket
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.table.zs_observe.shiprocket_settlement.applies_to_platform.platform.shiprocket
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.order_id
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.order_id.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.order_id
  target: table.zs_observe.shiprocket_settlement
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.awb_number
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.awb_number.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.awb_number
  target: table.zs_observe.shiprocket_settlement
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.awb_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.courier_partner
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.courier_partner
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.courier_partner.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.courier_partner
  target: table.zs_observe.shiprocket_settlement
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.courier_partner
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.charged_amount
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.charged_amount.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.charged_amount
  target: table.zs_observe.shiprocket_settlement
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.charged_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.delivered_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.delivered_date
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.delivered_date.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.delivered_date
  target: table.zs_observe.shiprocket_settlement
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.delivered_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.settlement_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.settlement_date
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.settlement_date.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.settlement_date
  target: table.zs_observe.shiprocket_settlement
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.settlement_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.is_active
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.is_active.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.is_active
  target: table.zs_observe.shiprocket_settlement
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.is_active
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.group_level_id
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.group_level_id.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.group_level_id
  target: table.zs_observe.shiprocket_settlement
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.group_level_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.sourced_from_platform.platform.shiprocket
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.shiprocket_settlement_report
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
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.applies_to_platform.platform.shiprocket
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.shiprocket_settlement_report
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
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.order_id
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.order_id.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.order_id
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.courier_partner
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.courier_partner
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.courier_partner.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.courier_partner
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.courier_partner
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.awb_remittance_status.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.awb_remittance_status
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.courier_received_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.courier_received_amount
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.courier_received_amount.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.courier_received_amount
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.courier_received_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.settlement_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.settlement_id
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.settlement_id.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.settlement_id
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.settlement_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.source_gst_name
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.source_gst_name
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.source_gst_name.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.source_gst_name
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.source_gst_name
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.source_gst_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.source_gst_id
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.source_gst_id.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.source_gst_id
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.source_gst_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.parent_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.parent_id
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.parent_id.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.parent_id
  target: table.zs_observe.shiprocket_settlement_report
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
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.parent_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.shiprocket_invoice.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.shiprocket_invoice.awb
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
  edge_id: edge.relationship.shiprocket_oms.shiprocket_invoice.awb.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.shiprocket_invoice.awb
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_oms.shiprocket_invoice.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_oms.shiprocket_invoice.awb
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
  edge_id: edge.relationship.shiprocket_oms.shiprocket_invoice.awb.target_table.table.zs_observe.shiprocket_invoice
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.shiprocket_invoice.awb
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.relationship.shiprocket_oms.shiprocket_invoice.awb.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.shiprocket_invoice.awb
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
  edge_id: edge.relationship.shiprocket_oms.shiprocket_invoice.awb.uses_target_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.shiprocket_invoice.awb
  target: column.zs_observe.shiprocket_invoice.other_id
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.shiprocket_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.shiprocket_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.shiprocket_settlement.awb.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.shiprocket_settlement.awb
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
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_relationship.relationship.shiprocket_oms.shiprocket_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_settlement
  target: relationship.shiprocket_oms.shiprocket_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.shiprocket_settlement.awb.target_table.table.zs_observe.shiprocket_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.shiprocket_settlement.awb
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.relationship.shiprocket_oms.shiprocket_settlement.awb.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.shiprocket_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.shiprocket_settlement.awb.uses_target_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.shiprocket_settlement.awb
  target: column.zs_observe.shiprocket_settlement.awb_number
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_invoice.shiprocket_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_invoice.shiprocket_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.shiprocket_settlement.awb.source_table.table.zs_observe.shiprocket_invoice
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_invoice.shiprocket_settlement.awb
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_relationship.relationship.shiprocket_invoice.shiprocket_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_settlement
  target: relationship.shiprocket_invoice.shiprocket_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.shiprocket_settlement.awb.target_table.table.zs_observe.shiprocket_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_invoice.shiprocket_settlement.awb
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.relationship.shiprocket_invoice.shiprocket_settlement.awb.uses_source_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_invoice.shiprocket_settlement.awb
  target: column.zs_observe.shiprocket_invoice.other_id
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
  edge_id: edge.relationship.shiprocket_invoice.shiprocket_settlement.awb.uses_target_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_invoice.shiprocket_settlement.awb
  target: column.zs_observe.shiprocket_settlement.awb_number
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
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_relationship.relationship.shiprocket_settlement.delhivery_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_settlement
  target: relationship.shiprocket_settlement.delhivery_settlement.awb
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
  edge_id: edge.relationship.shiprocket_settlement.delhivery_settlement.awb.source_table.table.zs_observe.shiprocket_settlement
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_settlement.delhivery_settlement.awb
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.table.zs_observe.delhivery_settlement.has_relationship.relationship.shiprocket_settlement.delhivery_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.delhivery_settlement
  target: relationship.shiprocket_settlement.delhivery_settlement.awb
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
  edge_id: edge.relationship.shiprocket_settlement.delhivery_settlement.awb.target_table.table.zs_observe.delhivery_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_settlement.delhivery_settlement.awb
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
  edge_id: edge.relationship.shiprocket_settlement.delhivery_settlement.awb.uses_source_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_settlement.delhivery_settlement.awb
  target: column.zs_observe.shiprocket_settlement.awb_number
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
  edge_id: edge.relationship.shiprocket_settlement.delhivery_settlement.awb.uses_target_column.column.zs_observe.delhivery_settlement.waybill_num
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_settlement.delhivery_settlement.awb
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_invoice.dtdc_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_invoice.dtdc_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.dtdc_settlement.awb.source_table.table.zs_observe.shiprocket_invoice
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_invoice.dtdc_settlement.awb
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.dtdc_settlement.has_relationship.relationship.shiprocket_invoice.dtdc_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.dtdc_settlement
  target: relationship.shiprocket_invoice.dtdc_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.dtdc_settlement.awb.target_table.table.zs_observe.dtdc_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_invoice.dtdc_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.dtdc_settlement.awb.uses_source_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_invoice.dtdc_settlement.awb
  target: column.zs_observe.shiprocket_invoice.other_id
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
  edge_id: edge.relationship.shiprocket_invoice.dtdc_settlement.awb.uses_target_column.column.zs_observe.dtdc_settlement.airwaybill_number
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_invoice.dtdc_settlement.awb
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_invoice.ekart_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_invoice.ekart_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.ekart_settlement.awb.source_table.table.zs_observe.shiprocket_invoice
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_invoice.ekart_settlement.awb
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.ekart_settlement.has_relationship.relationship.shiprocket_invoice.ekart_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.ekart_settlement
  target: relationship.shiprocket_invoice.ekart_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.ekart_settlement.awb.target_table.table.zs_observe.ekart_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_invoice.ekart_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.ekart_settlement.awb.uses_source_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_invoice.ekart_settlement.awb
  target: column.zs_observe.shiprocket_invoice.other_id
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
  edge_id: edge.relationship.shiprocket_invoice.ekart_settlement.awb.uses_target_column.column.zs_observe.ekart_settlement.shipment_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_invoice.ekart_settlement.awb
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
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_relationship.relationship.shiprocket_settlement.xpressbees_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_settlement
  target: relationship.shiprocket_settlement.xpressbees_settlement.awb
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
  edge_id: edge.relationship.shiprocket_settlement.xpressbees_settlement.awb.source_table.table.zs_observe.shiprocket_settlement
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_settlement.xpressbees_settlement.awb
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_relationship.relationship.shiprocket_settlement.xpressbees_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.xpressbees_settlement
  target: relationship.shiprocket_settlement.xpressbees_settlement.awb
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
  edge_id: edge.relationship.shiprocket_settlement.xpressbees_settlement.awb.target_table.table.zs_observe.xpressbees_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_settlement.xpressbees_settlement.awb
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
  edge_id: edge.relationship.shiprocket_settlement.xpressbees_settlement.awb.uses_source_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_settlement.xpressbees_settlement.awb
  target: column.zs_observe.shiprocket_settlement.awb_number
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
  edge_id: edge.relationship.shiprocket_settlement.xpressbees_settlement.awb.uses_target_column.column.zs_observe.xpressbees_settlement.shipping_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_settlement.xpressbees_settlement.awb
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_invoice.xpressbees_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_invoice.xpressbees_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.xpressbees_settlement.awb.source_table.table.zs_observe.shiprocket_invoice
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_invoice.xpressbees_settlement.awb
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_relationship.relationship.shiprocket_invoice.xpressbees_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.xpressbees_settlement
  target: relationship.shiprocket_invoice.xpressbees_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.xpressbees_settlement.awb.target_table.table.zs_observe.xpressbees_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_invoice.xpressbees_settlement.awb
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
  edge_id: edge.relationship.shiprocket_invoice.xpressbees_settlement.awb.uses_source_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_invoice.xpressbees_settlement.awb
  target: column.zs_observe.shiprocket_invoice.other_id
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
  edge_id: edge.relationship.shiprocket_invoice.xpressbees_settlement.awb.uses_target_column.column.zs_observe.xpressbees_settlement.shipping_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_invoice.xpressbees_settlement.awb
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_value_profile.value_profile.shiprocket_invoice.courier_partner
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_invoice
  target: value_profile.shiprocket_invoice.courier_partner
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
  edge_id: edge.value_profile.shiprocket_invoice.courier_partner.profiles_column.column.zs_observe.shiprocket_invoice.courier_partner
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_invoice.courier_partner
  target: column.zs_observe.shiprocket_invoice.courier_partner
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.courier_partner.has_value_profile.value_profile.shiprocket_invoice.courier_partner
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_invoice.courier_partner
  target: value_profile.shiprocket_invoice.courier_partner
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
    materialized_from: edge.value_profile.shiprocket_invoice.courier_partner.profiles_column.column.zs_observe.shiprocket_invoice.courier_partner
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.courier_partner.profiles_table.table.zs_observe.shiprocket_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_invoice.courier_partner
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_value_profile.value_profile.shiprocket_invoice.order_status
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_invoice
  target: value_profile.shiprocket_invoice.order_status
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
  edge_id: edge.value_profile.shiprocket_invoice.order_status.profiles_column.column.zs_observe.shiprocket_invoice.order_status
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_invoice.order_status
  target: column.zs_observe.shiprocket_invoice.order_status
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.order_status.has_value_profile.value_profile.shiprocket_invoice.order_status
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_invoice.order_status
  target: value_profile.shiprocket_invoice.order_status
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
    materialized_from: edge.value_profile.shiprocket_invoice.order_status.profiles_column.column.zs_observe.shiprocket_invoice.order_status
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.order_status.profiles_table.table.zs_observe.shiprocket_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_invoice.order_status
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_value_profile.value_profile.shiprocket_invoice.payment_mode
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_invoice
  target: value_profile.shiprocket_invoice.payment_mode
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
  edge_id: edge.value_profile.shiprocket_invoice.payment_mode.profiles_column.column.zs_observe.shiprocket_invoice.payment_mode
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_invoice.payment_mode
  target: column.zs_observe.shiprocket_invoice.payment_mode
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.payment_mode.has_value_profile.value_profile.shiprocket_invoice.payment_mode
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_invoice.payment_mode
  target: value_profile.shiprocket_invoice.payment_mode
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
    materialized_from: edge.value_profile.shiprocket_invoice.payment_mode.profiles_column.column.zs_observe.shiprocket_invoice.payment_mode
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.payment_mode.profiles_table.table.zs_observe.shiprocket_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_invoice.payment_mode
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_value_profile.value_profile.shiprocket_invoice.zone
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_invoice
  target: value_profile.shiprocket_invoice.zone
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
  edge_id: edge.value_profile.shiprocket_invoice.zone.profiles_column.column.zs_observe.shiprocket_invoice.zone
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_invoice.zone
  target: column.zs_observe.shiprocket_invoice.zone
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
  edge_id: edge.column.zs_observe.shiprocket_invoice.zone.has_value_profile.value_profile.shiprocket_invoice.zone
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_invoice.zone
  target: value_profile.shiprocket_invoice.zone
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
    materialized_from: edge.value_profile.shiprocket_invoice.zone.profiles_column.column.zs_observe.shiprocket_invoice.zone
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.zone.profiles_table.table.zs_observe.shiprocket_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_invoice.zone
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_value_profile.value_profile.shiprocket_settlement.courier_partner
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_settlement
  target: value_profile.shiprocket_settlement.courier_partner
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
  edge_id: edge.value_profile.shiprocket_settlement.courier_partner.profiles_column.column.zs_observe.shiprocket_settlement.courier_partner
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_settlement.courier_partner
  target: column.zs_observe.shiprocket_settlement.courier_partner
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
  edge_id: edge.column.zs_observe.shiprocket_settlement.courier_partner.has_value_profile.value_profile.shiprocket_settlement.courier_partner
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_settlement.courier_partner
  target: value_profile.shiprocket_settlement.courier_partner
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
    materialized_from: edge.value_profile.shiprocket_settlement.courier_partner.profiles_column.column.zs_observe.shiprocket_settlement.courier_partner
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_settlement.courier_partner.profiles_table.table.zs_observe.shiprocket_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_settlement.courier_partner
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_value_profile.value_profile.shiprocket_settlement_report.awb_remittance_status
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_settlement_report
  target: value_profile.shiprocket_settlement_report.awb_remittance_status
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
  edge_id: edge.value_profile.shiprocket_settlement_report.awb_remittance_status.profiles_column.column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_settlement_report.awb_remittance_status
  target: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
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
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.awb_remittance_status.has_value_profile.value_profile.shiprocket_settlement_report.awb_remittance_status
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  target: value_profile.shiprocket_settlement_report.awb_remittance_status
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
    materialized_from: edge.value_profile.shiprocket_settlement_report.awb_remittance_status.profiles_column.column.zs_observe.shiprocket_settlement_report.awb_remittance_status
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_settlement_report.awb_remittance_status.profiles_table.table.zs_observe.shiprocket_settlement_report
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_settlement_report.awb_remittance_status
  target: table.zs_observe.shiprocket_settlement_report
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

```yaml
candidate_edge:
  edge_id: edge.metric.freight_billed_amount.has_implementation.metric_impl.shiprocket_invoice.freight_billed_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_billed_amount
  target: metric_impl.shiprocket_invoice.freight_billed_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.freight_billed_amount.implements_metric.metric.freight_billed_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.freight_billed_amount
  target: metric.freight_billed_amount
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
    materialized_from: edge.metric.freight_billed_amount.has_implementation.metric_impl.shiprocket_invoice.freight_billed_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_billed_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.freight_billed_amount
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.freight_billed_amount.uses_column.column.zs_observe.shiprocket_invoice.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.freight_billed_amount
  target: column.zs_observe.shiprocket_invoice.charged_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.freight_billed_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.freight_billed_amount
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.freight_excluding_tax_amount.has_implementation.metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_excluding_tax_amount
  target: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.freight_excluding_tax_amount.implements_metric.metric.freight_excluding_tax_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  target: metric.freight_excluding_tax_amount
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
    materialized_from: edge.metric.freight_excluding_tax_amount.has_implementation.metric_impl.shiprocket_invoice.freight_excluding_tax_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_excluding_tax_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.freight_excluding_tax_amount.uses_column.column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  target: column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
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
  edge_id: edge.metric_impl.shiprocket_invoice.freight_excluding_tax_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.gst_on_freight_amount.has_implementation.metric_impl.shiprocket_invoice.gst_on_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.gst_on_freight_amount
  target: metric_impl.shiprocket_invoice.gst_on_freight_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.gst_on_freight_amount.implements_metric.metric.gst_on_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.gst_on_freight_amount
  target: metric.gst_on_freight_amount
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
    materialized_from: edge.metric.gst_on_freight_amount.has_implementation.metric_impl.shiprocket_invoice.gst_on_freight_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.gst_on_freight_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.gst_on_freight_amount
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.gst_on_freight_amount.uses_column.column.zs_observe.shiprocket_invoice.total_tax.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.gst_on_freight_amount
  target: column.zs_observe.shiprocket_invoice.total_tax
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
  edge_id: edge.metric_impl.shiprocket_invoice.gst_on_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.gst_on_freight_amount
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.fuel_surcharge_amount.has_implementation.metric_impl.shiprocket_invoice.fuel_surcharge_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.fuel_surcharge_amount
  target: metric_impl.shiprocket_invoice.fuel_surcharge_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.fuel_surcharge_amount.implements_metric.metric.fuel_surcharge_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  target: metric.fuel_surcharge_amount
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
    materialized_from: edge.metric.fuel_surcharge_amount.has_implementation.metric_impl.shiprocket_invoice.fuel_surcharge_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.fuel_surcharge_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.fuel_surcharge_amount.uses_column.column.zs_observe.shiprocket_invoice.charge_fsc.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  target: column.zs_observe.shiprocket_invoice.charge_fsc
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
  edge_id: edge.metric_impl.shiprocket_invoice.fuel_surcharge_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.rto_freight_amount.has_implementation.metric_impl.shiprocket_invoice.rto_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_freight_amount
  target: metric_impl.shiprocket_invoice.rto_freight_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.rto_freight_amount.implements_metric.metric.rto_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.rto_freight_amount
  target: metric.rto_freight_amount
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
    materialized_from: edge.metric.rto_freight_amount.has_implementation.metric_impl.shiprocket_invoice.rto_freight_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.rto_freight_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.rto_freight_amount
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.rto_freight_amount.uses_column.column.zs_observe.shiprocket_invoice.charge_rto.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.rto_freight_amount
  target: column.zs_observe.shiprocket_invoice.charge_rto
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
  edge_id: edge.metric_impl.shiprocket_invoice.rto_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.rto_freight_amount
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.cod_fee_amount.has_implementation.metric_impl.shiprocket_invoice.cod_fee_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_fee_amount
  target: metric_impl.shiprocket_invoice.cod_fee_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.cod_fee_amount.implements_metric.metric.cod_fee_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.cod_fee_amount
  target: metric.cod_fee_amount
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
    materialized_from: edge.metric.cod_fee_amount.has_implementation.metric_impl.shiprocket_invoice.cod_fee_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.cod_fee_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.cod_fee_amount
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.cod_fee_amount.uses_column.column.zs_observe.shiprocket_invoice.charge_cod.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.cod_fee_amount
  target: column.zs_observe.shiprocket_invoice.charge_cod
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
  edge_id: edge.metric_impl.shiprocket_invoice.cod_fee_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.cod_fee_amount
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.forward_freight_amount.has_implementation.metric_impl.shiprocket_invoice.forward_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.forward_freight_amount
  target: metric_impl.shiprocket_invoice.forward_freight_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.forward_freight_amount.implements_metric.metric.forward_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.forward_freight_amount
  target: metric.forward_freight_amount
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
    materialized_from: edge.metric.forward_freight_amount.has_implementation.metric_impl.shiprocket_invoice.forward_freight_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.forward_freight_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.forward_freight_amount
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.forward_freight_amount.uses_column.column.zs_observe.shiprocket_invoice.charge_dl.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.forward_freight_amount
  target: column.zs_observe.shiprocket_invoice.charge_dl
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
  edge_id: edge.metric_impl.shiprocket_invoice.forward_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.forward_freight_amount
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.actual_weight.has_implementation.metric_impl.shiprocket_invoice.actual_weight
  edge_type: HAS_IMPLEMENTATION
  source: metric.actual_weight
  target: metric_impl.shiprocket_invoice.actual_weight
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
  edge_id: edge.metric_impl.shiprocket_invoice.actual_weight.implements_metric.metric.actual_weight
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.actual_weight
  target: metric.actual_weight
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
    materialized_from: edge.metric.actual_weight.has_implementation.metric_impl.shiprocket_invoice.actual_weight
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.actual_weight.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.actual_weight
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.actual_weight.uses_column.column.zs_observe.shiprocket_invoice.final_weight.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.actual_weight
  target: column.zs_observe.shiprocket_invoice.final_weight
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
  edge_id: edge.metric_impl.shiprocket_invoice.actual_weight.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.actual_weight
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.billable_weight.has_implementation.metric_impl.shiprocket_invoice.billable_weight
  edge_type: HAS_IMPLEMENTATION
  source: metric.billable_weight
  target: metric_impl.shiprocket_invoice.billable_weight
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
  edge_id: edge.metric_impl.shiprocket_invoice.billable_weight.implements_metric.metric.billable_weight
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.billable_weight
  target: metric.billable_weight
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
    materialized_from: edge.metric.billable_weight.has_implementation.metric_impl.shiprocket_invoice.billable_weight
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.billable_weight.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.billable_weight
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.billable_weight.uses_column.column.zs_observe.shiprocket_invoice.charged_weight.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.billable_weight
  target: column.zs_observe.shiprocket_invoice.charged_weight
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
  edge_id: edge.metric_impl.shiprocket_invoice.billable_weight.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.billable_weight
  target: formula_template.logistics.component_sum
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
  edge_id: edge.metric.average_freight_per_awb.has_implementation.metric_impl.shiprocket_invoice.average_freight_per_awb
  edge_type: HAS_IMPLEMENTATION
  source: metric.average_freight_per_awb
  target: metric_impl.shiprocket_invoice.average_freight_per_awb
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
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.implements_metric.metric.average_freight_per_awb
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: metric.average_freight_per_awb
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
    materialized_from: edge.metric.average_freight_per_awb.has_implementation.metric_impl.shiprocket_invoice.average_freight_per_awb
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: table.zs_observe.shiprocket_invoice
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
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.uses_column.column.zs_observe.shiprocket_invoice.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: column.zs_observe.shiprocket_invoice.charged_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.uses_column.column.zs_observe.shiprocket_invoice.other_id.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: column.zs_observe.shiprocket_invoice.other_id
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
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
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
  edge_id: edge.metric.cod_collected_amount.has_implementation.metric_impl.shiprocket_settlement.cod_collected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_collected_amount
  target: metric_impl.shiprocket_settlement.cod_collected_amount
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
  edge_id: edge.metric_impl.shiprocket_settlement.cod_collected_amount.implements_metric.metric.cod_collected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.cod_collected_amount
  target: metric.cod_collected_amount
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
    materialized_from: edge.metric.cod_collected_amount.has_implementation.metric_impl.shiprocket_settlement.cod_collected_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_collected_amount.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.cod_collected_amount
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.metric_impl.shiprocket_settlement.cod_collected_amount.uses_column.column.zs_observe.shiprocket_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.cod_collected_amount
  target: column.zs_observe.shiprocket_settlement.charged_amount
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.shiprocket_settlement.cod_remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.cod_remitted_amount
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement.cod_remitted_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remitted_amount.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.cod_remitted_amount
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remitted_amount.uses_column.column.zs_observe.shiprocket_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.cod_remitted_amount
  target: column.zs_observe.shiprocket_settlement.charged_amount
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
  edge_id: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.shiprocket_settlement.cod_remittance_lag_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remittance_lag_days
  target: metric_impl.shiprocket_settlement.cod_remittance_lag_days
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
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remittance_lag_days.implements_metric.metric.cod_remittance_lag_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.cod_remittance_lag_days
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
    materialized_from: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.shiprocket_settlement.cod_remittance_lag_days
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remittance_lag_days.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remittance_lag_days.uses_column.column.zs_observe.shiprocket_settlement.delivered_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  target: column.zs_observe.shiprocket_settlement.delivered_date
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
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remittance_lag_days.uses_column.column.zs_observe.shiprocket_settlement.settlement_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  target: column.zs_observe.shiprocket_settlement.settlement_date
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
  edge_id: edge.metric.unique_awb_count.has_implementation.metric_impl.shiprocket_settlement.unique_awb_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.unique_awb_count
  target: metric_impl.shiprocket_settlement.unique_awb_count
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
  edge_id: edge.metric_impl.shiprocket_settlement.unique_awb_count.implements_metric.metric.unique_awb_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.unique_awb_count
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
    materialized_from: edge.metric.unique_awb_count.has_implementation.metric_impl.shiprocket_settlement.unique_awb_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.unique_awb_count.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.unique_awb_count
  target: table.zs_observe.shiprocket_settlement
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
  edge_id: edge.metric_impl.shiprocket_settlement.unique_awb_count.uses_column.column.zs_observe.shiprocket_settlement.awb_number.9e2adfd1
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.unique_awb_count
  target: column.zs_observe.shiprocket_settlement.awb_number
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
      column_role: key
```

```yaml
candidate_edge:
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
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
  edge_id: edge.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded.uses_table.table.zs_observe.shiprocket_settlement_report
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  target: table.zs_observe.shiprocket_settlement_report
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
  edge_id: edge.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded.uses_column.column.zs_observe.shiprocket_settlement_report.settlement_id.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  target: column.zs_observe.shiprocket_settlement_report.settlement_id
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
  edge_id: edge.metric.batch_settlement_amount.has_implementation.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  edge_type: HAS_IMPLEMENTATION
  source: metric.batch_settlement_amount
  target: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
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
  edge_id: edge.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded.implements_metric.metric.batch_settlement_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  target: metric.batch_settlement_amount
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
    materialized_from: edge.metric.batch_settlement_amount.has_implementation.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded.uses_table.table.zs_observe.shiprocket_settlement_report
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  target: table.zs_observe.shiprocket_settlement_report
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
  edge_id: edge.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded.uses_column.column.zs_observe.shiprocket_settlement_report.settlement_id.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  target: column.zs_observe.shiprocket_settlement_report.settlement_id
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

## 6. Review Items

```yaml
review_item:
  id: review.shiprocket_logistics_parser_ready_v4_unified_edges.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted
    from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```

## 7. Validation Summary

```yaml
validation_summary:
  document_id: shiprocket_logistics_parser_ready_v4_unified_edges
  candidate_cards: 181
  candidate_edges: 518
  card_types:
    metric: 33
    platform: 1
    platform_context: 1
    table: 4
    column: 81
    relationship: 14
    value_profile: 10
    metric_implementation: 37
  edge_types:
    BELONGS_TO_DOMAIN: 33
    BELONGS_TO_PLATFORM: 1
    HAS_PLATFORM_CONTEXT: 1
    SOURCED_FROM_PLATFORM: 4
    APPLIES_TO_PLATFORM: 4
    HAS_COLUMN: 81
    BELONGS_TO_TABLE: 81
    HAS_RELATIONSHIP: 28
    SOURCE_TABLE: 14
    TARGET_TABLE: 14
    USES_SOURCE_COLUMN: 14
    USES_TARGET_COLUMN: 14
    HAS_VALUE_PROFILE: 20
    PROFILES_COLUMN: 10
    PROFILES_TABLE: 10
    HAS_IMPLEMENTATION: 37
    IMPLEMENTS_METRIC: 37
    USES_TABLE: 37
    USES_COLUMN: 47
    USES_FORMULA_TEMPLATE: 31
  forbidden_card_types_present: []
  parser_boundary: generic logistics reusable knowledge only
```
