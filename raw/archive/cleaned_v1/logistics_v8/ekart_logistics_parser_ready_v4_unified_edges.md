# Ekart Logistics Knowledge — Parser Ready v4 Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: ekart_logistics_parser_ready_v4_unified_edges
  title: Ekart Logistics Knowledge — Parser Ready v4 Unified Edges
  domain: logistics
  vendor: Ekart
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style
  generated_on: '2026-05-20'
  version: 4.0-unified-edges
  scope: ekart_vendor_logistics_with_unified_edges
  logistics_only: true
  allowed_card_types:
  - column
  - metric
  - metric_implementation
  - platform
  - platform_context
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
  id: evidence.ekart.vendor_scope
  source_document: Logistics KB Doc.docx
  summary: 'Vendor-specific extracted evidence for ekart: table role, coverage status, metrics, caveats, and joins.'
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
  card_id: platform.ekart
  name: Ekart
  fields:
    name: Ekart
    description: Ekart logistics platform/vendor in the logistics domain.
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
    platform_name: Ekart
    platform_type: marketplace_fulfilment
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
  card_id: platform_context.ekart.in
  name: Ekart India
  fields:
    name: Ekart India
    description: India logistics context for Ekart.
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
    platform_id: platform.ekart
    context_name: Ekart India
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
  card_id: table.zs_observe.ekart_settlement
  name: Ekart Settlement
  fields:
    name: Ekart Settlement
    description: 'Ekart Settlement: One row per Ekart COD/POS settlement shipment or batch-related record.'
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
    table_name: ekart_settlement
    full_reference: zs_observe.ekart_settlement
    engine: Athena v3 / Trino SQL
    table_type: marketplace_fulfilment_settlement
    source_platform_ids:
    - platform.ekart
    source_platform_types:
    - logistics
    business_purpose: One row per Ekart COD/POS settlement shipment or batch-related record.
    grain: One row per Ekart COD/POS settlement shipment or batch-related record.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.ekart; account filters are not defined here
    coverage_status: active
    row_count: '6595'
    period: '-'
    group_ids: 22;203
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
  card_id: table.zs_observe.ekart_invoice
  name: Ekart Invoice
  fields:
    name: Ekart Invoice
    description: 'Ekart Invoice: Ekart invoice table exists but has no loaded freight invoice rows.'
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
    table_name: ekart_invoice
    full_reference: zs_observe.ekart_invoice
    engine: Athena v3 / Trino SQL
    table_type: schema_only_invoice
    source_platform_ids:
    - platform.ekart
    source_platform_types:
    - logistics
    business_purpose: Ekart invoice table exists but has no loaded freight invoice rows.
    grain: Ekart invoice table exists but has no loaded freight invoice rows.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.ekart; account filters are not defined here
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
  card_id: column.zs_observe.ekart_settlement.shipment_id
  name: ekart_settlement.shipment_id
  fields:
    name: ekart_settlement.shipment_id
    description: Ekart AWB/shipment identifier, often MENC prefix.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: shipment_id
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - Ekart AWB/shipment identifier, often MENC prefix.
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
  card_id: column.zs_observe.ekart_settlement.tracking_id
  name: ekart_settlement.tracking_id
  fields:
    name: ekart_settlement.tracking_id
    description: Same as shipment_id.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: tracking_id
    data_type: unknown
    semantic_roles: identifier;join_key
    business_concepts:
    - Same as shipment_id.
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
  card_id: column.zs_observe.ekart_settlement.merchant_id
  name: ekart_settlement.merchant_id
  fields:
    name: ekart_settlement.merchant_id
    description: MEN indicates Mensa.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: merchant_id
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - MEN indicates Mensa.
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
  card_id: column.zs_observe.ekart_settlement.transaction_type
  name: ekart_settlement.transaction_type
  fields:
    name: ekart_settlement.transaction_type
    description: COD or POS.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: transaction_type
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - COD or POS.
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
  card_id: column.zs_observe.ekart_settlement.bank_name
  name: ekart_settlement.bank_name
  fields:
    name: ekart_settlement.bank_name
    description: Bank name such as ICICI BANK.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: bank_name
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - Bank name such as ICICI BANK.
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
  card_id: column.zs_observe.ekart_settlement.transaction_mode
  name: ekart_settlement.transaction_mode
  fields:
    name: ekart_settlement.transaction_mode
    description: COD or POS.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: transaction_mode
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - COD or POS.
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
  card_id: column.zs_observe.ekart_settlement.charged_amount
  name: ekart_settlement.charged_amount
  fields:
    name: ekart_settlement.charged_amount
    description: Per-shipment settlement/product value.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Per-shipment settlement/product value.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: cod_or_product_settlement_value_not_freight
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
  card_id: column.zs_observe.ekart_settlement.cod_amount
  name: ekart_settlement.cod_amount
  fields:
    name: ekart_settlement.cod_amount
    description: COD amount for COD rows.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: cod_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount for COD rows.
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
  card_id: column.zs_observe.ekart_settlement.total_amount_of_batch
  name: ekart_settlement.total_amount_of_batch
  fields:
    name: ekart_settlement.total_amount_of_batch
    description: Batch total amount across shipments.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: total_amount_of_batch
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Batch total amount across shipments.
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
  card_id: column.zs_observe.ekart_settlement.settlement_id
  name: ekart_settlement.settlement_id
  fields:
    name: ekart_settlement.settlement_id
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
    table_id: table.zs_observe.ekart_settlement
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
  card_id: column.zs_observe.ekart_settlement.settlement_date
  name: ekart_settlement.settlement_date
  fields:
    name: ekart_settlement.settlement_date
    description: Settlement/bank transfer date.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: settlement_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Settlement/bank transfer date.
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
  card_id: column.zs_observe.ekart_settlement.delivered_date
  name: ekart_settlement.delivered_date
  fields:
    name: ekart_settlement.delivered_date
    description: Delivery date.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: delivered_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Delivery date.
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
  card_id: column.zs_observe.ekart_settlement.invoice_date
  name: ekart_settlement.invoice_date
  fields:
    name: ekart_settlement.invoice_date
    description: Invoice date.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: invoice_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Invoice date.
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
  card_id: column.zs_observe.ekart_settlement.mp_id
  name: ekart_settlement.mp_id
  fields:
    name: ekart_settlement.mp_id
    description: Marketplace shipment ID.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: mp_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Marketplace shipment ID.
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
  card_id: column.zs_observe.ekart_settlement.actual_date_of_remittance
  name: ekart_settlement.actual_date_of_remittance
  fields:
    name: ekart_settlement.actual_date_of_remittance
    description: Actual remittance date.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: actual_date_of_remittance
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Actual remittance date.
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
  card_id: column.zs_observe.ekart_settlement.due_date_of_remittance
  name: ekart_settlement.due_date_of_remittance
  fields:
    name: ekart_settlement.due_date_of_remittance
    description: Expected remittance date.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: due_date_of_remittance
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Expected remittance date.
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
  card_id: column.zs_observe.ekart_settlement.bank_reference_no
  name: ekart_settlement.bank_reference_no
  fields:
    name: ekart_settlement.bank_reference_no
    description: Bank transaction reference.
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
    table_id: table.zs_observe.ekart_settlement
    column_name: bank_reference_no
    data_type: unknown
    semantic_roles: identifier;bank_bridge
    business_concepts:
    - Bank transaction reference.
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
  card_id: column.zs_observe.ekart_settlement.is_active
  name: ekart_settlement.is_active
  fields:
    name: ekart_settlement.is_active
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
    table_id: table.zs_observe.ekart_settlement
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
  card_id: column.zs_observe.ekart_settlement.group_level_id
  name: ekart_settlement.group_level_id
  fields:
    name: ekart_settlement.group_level_id
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
    table_id: table.zs_observe.ekart_settlement
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
  card_id: column.zs_observe.ekart_invoice.order_id
  name: ekart_invoice.order_id
  fields:
    name: ekart_invoice.order_id
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
    table_id: table.zs_observe.ekart_invoice
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
  card_id: column.zs_observe.ekart_invoice.invoice_number
  name: ekart_invoice.invoice_number
  fields:
    name: ekart_invoice.invoice_number
    description: Ekart invoice reference.
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
    table_id: table.zs_observe.ekart_invoice
    column_name: invoice_number
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Ekart invoice reference.
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
  card_id: column.zs_observe.ekart_invoice.freight_charge
  name: ekart_invoice.freight_charge
  fields:
    name: ekart_invoice.freight_charge
    description: Freight charge if loaded later.
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
    table_id: table.zs_observe.ekart_invoice
    column_name: freight_charge
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Freight charge if loaded later.
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
  card_id: column.zs_observe.ekart_invoice.cod_charge
  name: ekart_invoice.cod_charge
  fields:
    name: ekart_invoice.cod_charge
    description: COD collection fee if loaded later.
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
    table_id: table.zs_observe.ekart_invoice
    column_name: cod_charge
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD collection fee if loaded later.
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
  card_id: column.zs_observe.ekart_invoice.charge_rto
  name: ekart_invoice.charge_rto
  fields:
    name: ekart_invoice.charge_rto
    description: RTO charge if loaded later.
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
    table_id: table.zs_observe.ekart_invoice
    column_name: charge_rto
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - RTO charge if loaded later.
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
  card_id: column.zs_observe.ekart_invoice.zone
  name: ekart_invoice.zone
  fields:
    name: ekart_invoice.zone
    description: Delivery zone.
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
    table_id: table.zs_observe.ekart_invoice
    column_name: zone
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Delivery zone.
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
  card_id: column.zs_observe.ekart_invoice.charged_weight
  name: ekart_invoice.charged_weight
  fields:
    name: ekart_invoice.charged_weight
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
    table_id: table.zs_observe.ekart_invoice
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

### 4.7 value_profile cards

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.ekart_settlement.transaction_type
  name: ekart_settlement.transaction_type Value Profile
  fields:
    name: ekart_settlement.transaction_type Value Profile
    description: Known values and meanings for ekart_settlement.transaction_type.
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
    table_id: table.zs_observe.ekart_settlement
    column_id: column.zs_observe.ekart_settlement.transaction_type
    value_type: enum_or_enum_with_nulls
    values: COD=Cash-on-delivery settlement (cod); POS=Prepaid/digital POS settlement (pos)
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
  card_id: value_profile.ekart_settlement.transaction_mode
  name: ekart_settlement.transaction_mode Value Profile
  fields:
    name: ekart_settlement.transaction_mode Value Profile
    description: Known values and meanings for ekart_settlement.transaction_mode.
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
    table_id: table.zs_observe.ekart_settlement
    column_id: column.zs_observe.ekart_settlement.transaction_mode
    value_type: enum_or_enum_with_nulls
    values: COD=COD mode (cod); POS=POS/prepaid mode (pos)
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
  card_id: value_profile.ekart_settlement.bank_name
  name: ekart_settlement.bank_name Value Profile
  fields:
    name: ekart_settlement.bank_name Value Profile
    description: Known values and meanings for ekart_settlement.bank_name.
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
    table_id: table.zs_observe.ekart_settlement
    column_id: column.zs_observe.ekart_settlement.bank_name
    value_type: enum_or_enum_with_nulls
    values: ICICI BANK=ICICI bank settlement destination as observed (icici); NULL=Raw rows without bank name (unknown)
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
  card_id: value_profile.ekart_settlement.merchant_id
  name: ekart_settlement.merchant_id Value Profile
  fields:
    name: ekart_settlement.merchant_id Value Profile
    description: Known values and meanings for ekart_settlement.merchant_id.
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
    table_id: table.zs_observe.ekart_settlement
    column_id: column.zs_observe.ekart_settlement.merchant_id
    value_type: enum_or_enum_with_nulls
    values: MEN=Mensa merchant identifier (mensa)
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.pos_settled_amount
  name: POS Settled Amount
  fields:
    name: POS Settled Amount
    description: Prepaid/POS amount settled through logistics or marketplace fulfilment rail.
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
    metric_name: POS Settled Amount
    aliases:
    - prepaid POS settlement
    - digital settlement
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - pos_settled_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.settlement_batch_count
  name: Settlement Batch Count
  fields:
    name: Settlement Batch Count
    description: Count of settlement or remittance batches.
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
    metric_name: Settlement Batch Count
    aliases:
    - remittance batch count
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - settlement_batch_count
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ekart_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.9 metric_implementation cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_settlement.cod_collected_amount
  name: Ekart COD Collected Amount Implementation
  fields:
    name: Ekart COD Collected Amount Implementation
    description: COD Collected Amount implementation for Ekart using ekart_settlement.
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
    implementation_name: Ekart COD Collected Amount
    metric_pattern: filtered_sum_or_batch_deduplicated_sum
    applicability: platform=ekart; table=zs_observe.ekart_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_settlement
    required_columns:
    - column.zs_observe.ekart_settlement.cod_amount
    semantic_filters:
    - transaction_type='COD'
    formula_description: SUM(cod_amount)
    formula_sql: SUM(cod_amount)
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
    - actual_date_of_remittance
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: total_amount_of_batch is batch-level and must not be summed at AWB grain without dedupe.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.batch_deduplicated_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_settlement.cod_remitted_amount
  name: Ekart COD Remitted Amount Implementation
  fields:
    name: Ekart COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Ekart using ekart_settlement.
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
    implementation_name: Ekart COD Remitted Amount
    metric_pattern: filtered_sum_or_batch_deduplicated_sum
    applicability: platform=ekart; table=zs_observe.ekart_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_settlement
    required_columns:
    - column.zs_observe.ekart_settlement.charged_amount
    semantic_filters:
    - transaction_type='COD'
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
    - actual_date_of_remittance
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: total_amount_of_batch is batch-level and must not be summed at AWB grain without dedupe.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.batch_deduplicated_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_settlement.pos_settled_amount
  name: Ekart POS Settled Amount Implementation
  fields:
    name: Ekart POS Settled Amount Implementation
    description: POS Settled Amount implementation for Ekart using ekart_settlement.
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
    metric_id: metric.pos_settled_amount
    implementation_name: Ekart POS Settled Amount
    metric_pattern: filtered_sum_or_batch_deduplicated_sum
    applicability: platform=ekart; table=zs_observe.ekart_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_settlement
    required_columns:
    - column.zs_observe.ekart_settlement.charged_amount
    semantic_filters:
    - transaction_type='POS'
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
    - actual_date_of_remittance
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: total_amount_of_batch is batch-level and must not be summed at AWB grain without dedupe.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.batch_deduplicated_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_settlement.batch_settlement_amount
  name: Ekart Batch Settlement Amount Implementation
  fields:
    name: Ekart Batch Settlement Amount Implementation
    description: Batch Settlement Amount implementation for Ekart using ekart_settlement.
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
    implementation_name: Ekart Batch Settlement Amount
    metric_pattern: filtered_sum_or_batch_deduplicated_sum
    applicability: platform=ekart; table=zs_observe.ekart_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_settlement
    required_columns:
    - column.zs_observe.ekart_settlement.total_amount_of_batch
    semantic_filters:
    - aggregate at settlement_id/bank_reference grain
    formula_description: SUM(DISTINCT total_amount_of_batch)
    formula_sql: SUM(DISTINCT total_amount_of_batch)
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
    - actual_date_of_remittance
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: total_amount_of_batch is batch-level and must not be summed at AWB grain without dedupe.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.batch_deduplicated_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_settlement.settlement_batch_count
  name: Ekart Settlement Batch Count Implementation
  fields:
    name: Ekart Settlement Batch Count Implementation
    description: Settlement Batch Count implementation for Ekart using ekart_settlement.
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
    metric_id: metric.settlement_batch_count
    implementation_name: Ekart Settlement Batch Count
    metric_pattern: filtered_sum_or_batch_deduplicated_sum
    applicability: platform=ekart; table=zs_observe.ekart_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_settlement
    required_columns:
    - column.zs_observe.ekart_settlement.settlement_id
    semantic_filters: []
    formula_description: COUNT(DISTINCT settlement_id)
    formula_sql: COUNT(DISTINCT settlement_id)
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
    - actual_date_of_remittance
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: total_amount_of_batch is batch-level and must not be summed at AWB grain without dedupe.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.batch_deduplicated_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_settlement.unique_awb_count
  name: Ekart Unique AWB Count Implementation
  fields:
    name: Ekart Unique AWB Count Implementation
    description: Unique AWB Count implementation for Ekart using ekart_settlement.
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
    implementation_name: Ekart Unique AWB Count
    metric_pattern: filtered_sum_or_batch_deduplicated_sum
    applicability: platform=ekart; table=zs_observe.ekart_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_settlement
    required_columns:
    - column.zs_observe.ekart_settlement.shipment_id
    semantic_filters: []
    formula_description: COUNT(DISTINCT shipment_id)
    formula_sql: COUNT(DISTINCT shipment_id)
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
    - actual_date_of_remittance
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: total_amount_of_batch is batch-level and must not be summed at AWB grain without dedupe.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.batch_deduplicated_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_settlement.cod_remittance_lag_days
  name: Ekart COD Remittance Lag Days Implementation
  fields:
    name: Ekart COD Remittance Lag Days Implementation
    description: COD Remittance Lag Days implementation for Ekart using ekart_settlement.
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
    implementation_name: Ekart COD Remittance Lag Days
    metric_pattern: filtered_sum_or_batch_deduplicated_sum
    applicability: platform=ekart; table=zs_observe.ekart_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_settlement
    required_columns:
    - column.zs_observe.ekart_settlement.delivered_date
    - column.zs_observe.ekart_settlement.actual_date_of_remittance
    semantic_filters:
    - transaction_type='COD'
    formula_description: AVG(DATE_DIFF('day', delivered_date, actual_date_of_remittance))
    formula_sql: AVG(DATE_DIFF('day', delivered_date, actual_date_of_remittance))
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
    - actual_date_of_remittance
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: total_amount_of_batch is batch-level and must not be summed at AWB grain without dedupe.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.batch_deduplicated_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_settlement.declared_product_value
  name: Ekart Declared Product Value Implementation
  fields:
    name: Ekart Declared Product Value Implementation
    description: Declared Product Value implementation for Ekart using ekart_settlement.
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
    implementation_name: Ekart Declared Product Value
    metric_pattern: filtered_sum_or_batch_deduplicated_sum
    applicability: platform=ekart; table=zs_observe.ekart_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_settlement
    required_columns:
    - column.zs_observe.ekart_settlement.charged_amount
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
    - actual_date_of_remittance
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: total_amount_of_batch is batch-level and must not be summed at AWB grain without dedupe.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.batch_deduplicated_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty
  name: Ekart Freight Billed Amount Implementation
  fields:
    name: Ekart Freight Billed Amount Implementation
    description: Freight Billed Amount implementation for Ekart using ekart_invoice.
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
    implementation_name: Ekart Freight Billed Amount
    metric_pattern: unsupported_empty_table
    applicability: platform=ekart; table=zs_observe.ekart_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_invoice
    required_columns:
    - column.zs_observe.ekart_invoice.invoice_number
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
    caveats: ekart_invoice has zero rows; for FBF freight is often embedded in marketplace economics; for Shiprocket-routed
      Ekart use shiprocket_invoice courier_partner=Ekart Logistics Air.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty
  name: Ekart Forward Freight Amount Implementation
  fields:
    name: Ekart Forward Freight Amount Implementation
    description: Forward Freight Amount implementation for Ekart using ekart_invoice.
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
    implementation_name: Ekart Forward Freight Amount
    metric_pattern: unsupported_empty_table
    applicability: platform=ekart; table=zs_observe.ekart_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_invoice
    required_columns:
    - column.zs_observe.ekart_invoice.invoice_number
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
    caveats: ekart_invoice has zero rows; for FBF freight is often embedded in marketplace economics; for Shiprocket-routed
      Ekart use shiprocket_invoice courier_partner=Ekart Logistics Air.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty
  name: Ekart RTO Freight Amount Implementation
  fields:
    name: Ekart RTO Freight Amount Implementation
    description: RTO Freight Amount implementation for Ekart using ekart_invoice.
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
    implementation_name: Ekart RTO Freight Amount
    metric_pattern: unsupported_empty_table
    applicability: platform=ekart; table=zs_observe.ekart_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_invoice
    required_columns:
    - column.zs_observe.ekart_invoice.invoice_number
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
    caveats: ekart_invoice has zero rows; for FBF freight is often embedded in marketplace economics; for Shiprocket-routed
      Ekart use shiprocket_invoice courier_partner=Ekart Logistics Air.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty
  name: Ekart COD Fee Amount Implementation
  fields:
    name: Ekart COD Fee Amount Implementation
    description: COD Fee Amount implementation for Ekart using ekart_invoice.
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
    implementation_name: Ekart COD Fee Amount
    metric_pattern: unsupported_empty_table
    applicability: platform=ekart; table=zs_observe.ekart_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.ekart_invoice
    required_columns:
    - column.zs_observe.ekart_invoice.invoice_number
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
    caveats: ekart_invoice has zero rows; for FBF freight is often embedded in marketplace economics; for Shiprocket-routed
      Ekart use shiprocket_invoice courier_partner=Ekart Logistics Air.
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
  edge_id: edge.metric.pos_settled_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.pos_settled_amount
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
  edge_id: edge.metric.settlement_batch_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.settlement_batch_count
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
  edge_id: edge.platform_context.ekart.in.belongs_to_platform.platform.ekart
  edge_type: BELONGS_TO_PLATFORM
  source: platform_context.ekart.in
  target: platform.ekart
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
  edge_id: edge.platform.ekart.has_platform_context.platform_context.ekart.in
  edge_type: HAS_PLATFORM_CONTEXT
  source: platform.ekart
  target: platform_context.ekart.in
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
    materialized_from: edge.platform_context.ekart.in.belongs_to_platform.platform.ekart
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.sourced_from_platform.platform.ekart
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.ekart_settlement
  target: platform.ekart
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
  edge_id: edge.table.zs_observe.ekart_settlement.applies_to_platform.platform.ekart
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.ekart_settlement
  target: platform.ekart
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
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.shipment_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.shipment_id
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
  edge_id: edge.column.zs_observe.ekart_settlement.shipment_id.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.shipment_id
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.shipment_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.tracking_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.tracking_id
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
  edge_id: edge.column.zs_observe.ekart_settlement.tracking_id.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.tracking_id
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.tracking_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.merchant_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.merchant_id
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
  edge_id: edge.column.zs_observe.ekart_settlement.merchant_id.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.merchant_id
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.merchant_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.transaction_type
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.transaction_type
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
  edge_id: edge.column.zs_observe.ekart_settlement.transaction_type.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.transaction_type
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.bank_name
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.bank_name
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
  edge_id: edge.column.zs_observe.ekart_settlement.bank_name.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.bank_name
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.bank_name
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.transaction_mode
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.transaction_mode
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
  edge_id: edge.column.zs_observe.ekart_settlement.transaction_mode.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.transaction_mode
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.transaction_mode
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.charged_amount
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
  edge_id: edge.column.zs_observe.ekart_settlement.charged_amount.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.charged_amount
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.charged_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.cod_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.cod_amount
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
  edge_id: edge.column.zs_observe.ekart_settlement.cod_amount.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.cod_amount
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.cod_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.total_amount_of_batch
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.total_amount_of_batch
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
  edge_id: edge.column.zs_observe.ekart_settlement.total_amount_of_batch.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.total_amount_of_batch
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.total_amount_of_batch
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.settlement_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.settlement_id
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
  edge_id: edge.column.zs_observe.ekart_settlement.settlement_id.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.settlement_id
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.settlement_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.settlement_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.settlement_date
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
  edge_id: edge.column.zs_observe.ekart_settlement.settlement_date.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.settlement_date
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.settlement_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.delivered_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.delivered_date
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
  edge_id: edge.column.zs_observe.ekart_settlement.delivered_date.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.delivered_date
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.delivered_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.invoice_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.invoice_date
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
  edge_id: edge.column.zs_observe.ekart_settlement.invoice_date.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.invoice_date
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.invoice_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.mp_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.mp_id
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
  edge_id: edge.column.zs_observe.ekart_settlement.mp_id.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.mp_id
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.mp_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.actual_date_of_remittance
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.actual_date_of_remittance
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
  edge_id: edge.column.zs_observe.ekart_settlement.actual_date_of_remittance.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.actual_date_of_remittance
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.actual_date_of_remittance
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.due_date_of_remittance
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.due_date_of_remittance
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
  edge_id: edge.column.zs_observe.ekart_settlement.due_date_of_remittance.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.due_date_of_remittance
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.due_date_of_remittance
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.bank_reference_no
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.bank_reference_no
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
  edge_id: edge.column.zs_observe.ekart_settlement.bank_reference_no.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.bank_reference_no
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.bank_reference_no
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.is_active
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
  edge_id: edge.column.zs_observe.ekart_settlement.is_active.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.is_active
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.is_active
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_settlement
  target: column.zs_observe.ekart_settlement.group_level_id
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
  edge_id: edge.column.zs_observe.ekart_settlement.group_level_id.belongs_to_table.table.zs_observe.ekart_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_settlement.group_level_id
  target: table.zs_observe.ekart_settlement
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
    materialized_from: edge.table.zs_observe.ekart_settlement.has_column.column.zs_observe.ekart_settlement.group_level_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_invoice.sourced_from_platform.platform.ekart
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.ekart_invoice
  target: platform.ekart
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
  edge_id: edge.table.zs_observe.ekart_invoice.applies_to_platform.platform.ekart
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.ekart_invoice
  target: platform.ekart
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
  edge_id: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_invoice
  target: column.zs_observe.ekart_invoice.order_id
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
  edge_id: edge.column.zs_observe.ekart_invoice.order_id.belongs_to_table.table.zs_observe.ekart_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_invoice.order_id
  target: table.zs_observe.ekart_invoice
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
    materialized_from: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.invoice_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_invoice
  target: column.zs_observe.ekart_invoice.invoice_number
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
  edge_id: edge.column.zs_observe.ekart_invoice.invoice_number.belongs_to_table.table.zs_observe.ekart_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_invoice.invoice_number
  target: table.zs_observe.ekart_invoice
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
    materialized_from: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.invoice_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.freight_charge
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_invoice
  target: column.zs_observe.ekart_invoice.freight_charge
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
  edge_id: edge.column.zs_observe.ekart_invoice.freight_charge.belongs_to_table.table.zs_observe.ekart_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_invoice.freight_charge
  target: table.zs_observe.ekart_invoice
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
    materialized_from: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.freight_charge
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.cod_charge
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_invoice
  target: column.zs_observe.ekart_invoice.cod_charge
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
  edge_id: edge.column.zs_observe.ekart_invoice.cod_charge.belongs_to_table.table.zs_observe.ekart_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_invoice.cod_charge
  target: table.zs_observe.ekart_invoice
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
    materialized_from: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.cod_charge
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.charge_rto
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_invoice
  target: column.zs_observe.ekart_invoice.charge_rto
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
  edge_id: edge.column.zs_observe.ekart_invoice.charge_rto.belongs_to_table.table.zs_observe.ekart_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_invoice.charge_rto
  target: table.zs_observe.ekart_invoice
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
    materialized_from: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.charge_rto
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.zone
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_invoice
  target: column.zs_observe.ekart_invoice.zone
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
  edge_id: edge.column.zs_observe.ekart_invoice.zone.belongs_to_table.table.zs_observe.ekart_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_invoice.zone
  target: table.zs_observe.ekart_invoice
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
    materialized_from: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.zone
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.charged_weight
  edge_type: HAS_COLUMN
  source: table.zs_observe.ekart_invoice
  target: column.zs_observe.ekart_invoice.charged_weight
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
  edge_id: edge.column.zs_observe.ekart_invoice.charged_weight.belongs_to_table.table.zs_observe.ekart_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.ekart_invoice.charged_weight
  target: table.zs_observe.ekart_invoice
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
    materialized_from: edge.table.zs_observe.ekart_invoice.has_column.column.zs_observe.ekart_invoice.charged_weight
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_value_profile.value_profile.ekart_settlement.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.ekart_settlement
  target: value_profile.ekart_settlement.transaction_type
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
  edge_id: edge.value_profile.ekart_settlement.transaction_type.profiles_column.column.zs_observe.ekart_settlement.transaction_type
  edge_type: PROFILES_COLUMN
  source: value_profile.ekart_settlement.transaction_type
  target: column.zs_observe.ekart_settlement.transaction_type
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
  edge_id: edge.column.zs_observe.ekart_settlement.transaction_type.has_value_profile.value_profile.ekart_settlement.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.ekart_settlement.transaction_type
  target: value_profile.ekart_settlement.transaction_type
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
    materialized_from: edge.value_profile.ekart_settlement.transaction_type.profiles_column.column.zs_observe.ekart_settlement.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.ekart_settlement.transaction_type.profiles_table.table.zs_observe.ekart_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.ekart_settlement.transaction_type
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.table.zs_observe.ekart_settlement.has_value_profile.value_profile.ekart_settlement.transaction_mode
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.ekart_settlement
  target: value_profile.ekart_settlement.transaction_mode
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
  edge_id: edge.value_profile.ekart_settlement.transaction_mode.profiles_column.column.zs_observe.ekart_settlement.transaction_mode
  edge_type: PROFILES_COLUMN
  source: value_profile.ekart_settlement.transaction_mode
  target: column.zs_observe.ekart_settlement.transaction_mode
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
  edge_id: edge.column.zs_observe.ekart_settlement.transaction_mode.has_value_profile.value_profile.ekart_settlement.transaction_mode
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.ekart_settlement.transaction_mode
  target: value_profile.ekart_settlement.transaction_mode
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
    materialized_from: edge.value_profile.ekart_settlement.transaction_mode.profiles_column.column.zs_observe.ekart_settlement.transaction_mode
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.ekart_settlement.transaction_mode.profiles_table.table.zs_observe.ekart_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.ekart_settlement.transaction_mode
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.table.zs_observe.ekart_settlement.has_value_profile.value_profile.ekart_settlement.bank_name
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.ekart_settlement
  target: value_profile.ekart_settlement.bank_name
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
  edge_id: edge.value_profile.ekart_settlement.bank_name.profiles_column.column.zs_observe.ekart_settlement.bank_name
  edge_type: PROFILES_COLUMN
  source: value_profile.ekart_settlement.bank_name
  target: column.zs_observe.ekart_settlement.bank_name
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
  edge_id: edge.column.zs_observe.ekart_settlement.bank_name.has_value_profile.value_profile.ekart_settlement.bank_name
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.ekart_settlement.bank_name
  target: value_profile.ekart_settlement.bank_name
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
    materialized_from: edge.value_profile.ekart_settlement.bank_name.profiles_column.column.zs_observe.ekart_settlement.bank_name
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.ekart_settlement.bank_name.profiles_table.table.zs_observe.ekart_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.ekart_settlement.bank_name
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.table.zs_observe.ekart_settlement.has_value_profile.value_profile.ekart_settlement.merchant_id
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.ekart_settlement
  target: value_profile.ekart_settlement.merchant_id
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
  edge_id: edge.value_profile.ekart_settlement.merchant_id.profiles_column.column.zs_observe.ekart_settlement.merchant_id
  edge_type: PROFILES_COLUMN
  source: value_profile.ekart_settlement.merchant_id
  target: column.zs_observe.ekart_settlement.merchant_id
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
  edge_id: edge.column.zs_observe.ekart_settlement.merchant_id.has_value_profile.value_profile.ekart_settlement.merchant_id
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.ekart_settlement.merchant_id
  target: value_profile.ekart_settlement.merchant_id
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
    materialized_from: edge.value_profile.ekart_settlement.merchant_id.profiles_column.column.zs_observe.ekart_settlement.merchant_id
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.ekart_settlement.merchant_id.profiles_table.table.zs_observe.ekart_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.ekart_settlement.merchant_id
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric.cod_collected_amount.has_implementation.metric_impl.ekart_settlement.cod_collected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_collected_amount
  target: metric_impl.ekart_settlement.cod_collected_amount
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
  edge_id: edge.metric_impl.ekart_settlement.cod_collected_amount.implements_metric.metric.cod_collected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_settlement.cod_collected_amount
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
    materialized_from: edge.metric.cod_collected_amount.has_implementation.metric_impl.ekart_settlement.cod_collected_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_settlement.cod_collected_amount.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: metric_impl.ekart_settlement.cod_collected_amount
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric_impl.ekart_settlement.cod_collected_amount.uses_column.column.zs_observe.ekart_settlement.cod_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.cod_collected_amount
  target: column.zs_observe.ekart_settlement.cod_amount
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
  edge_id: edge.metric_impl.ekart_settlement.cod_collected_amount.uses_formula_template.formula_template.logistics.batch_deduplicated_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.ekart_settlement.cod_collected_amount
  target: formula_template.logistics.batch_deduplicated_sum
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.ekart_settlement.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.ekart_settlement.cod_remitted_amount
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
  edge_id: edge.metric_impl.ekart_settlement.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_settlement.cod_remitted_amount
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.ekart_settlement.cod_remitted_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_settlement.cod_remitted_amount.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: metric_impl.ekart_settlement.cod_remitted_amount
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric_impl.ekart_settlement.cod_remitted_amount.uses_column.column.zs_observe.ekart_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.cod_remitted_amount
  target: column.zs_observe.ekart_settlement.charged_amount
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
  edge_id: edge.metric_impl.ekart_settlement.cod_remitted_amount.uses_formula_template.formula_template.logistics.batch_deduplicated_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.ekart_settlement.cod_remitted_amount
  target: formula_template.logistics.batch_deduplicated_sum
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
  edge_id: edge.metric.pos_settled_amount.has_implementation.metric_impl.ekart_settlement.pos_settled_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.pos_settled_amount
  target: metric_impl.ekart_settlement.pos_settled_amount
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
  edge_id: edge.metric_impl.ekart_settlement.pos_settled_amount.implements_metric.metric.pos_settled_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_settlement.pos_settled_amount
  target: metric.pos_settled_amount
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
    materialized_from: edge.metric.pos_settled_amount.has_implementation.metric_impl.ekart_settlement.pos_settled_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_settlement.pos_settled_amount.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: metric_impl.ekart_settlement.pos_settled_amount
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric_impl.ekart_settlement.pos_settled_amount.uses_column.column.zs_observe.ekart_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.pos_settled_amount
  target: column.zs_observe.ekart_settlement.charged_amount
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
  edge_id: edge.metric_impl.ekart_settlement.pos_settled_amount.uses_formula_template.formula_template.logistics.batch_deduplicated_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.ekart_settlement.pos_settled_amount
  target: formula_template.logistics.batch_deduplicated_sum
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
  edge_id: edge.metric.batch_settlement_amount.has_implementation.metric_impl.ekart_settlement.batch_settlement_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.batch_settlement_amount
  target: metric_impl.ekart_settlement.batch_settlement_amount
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
  edge_id: edge.metric_impl.ekart_settlement.batch_settlement_amount.implements_metric.metric.batch_settlement_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_settlement.batch_settlement_amount
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
    materialized_from: edge.metric.batch_settlement_amount.has_implementation.metric_impl.ekart_settlement.batch_settlement_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_settlement.batch_settlement_amount.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: metric_impl.ekart_settlement.batch_settlement_amount
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric_impl.ekart_settlement.batch_settlement_amount.uses_column.column.zs_observe.ekart_settlement.total_amount_of_batch.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.batch_settlement_amount
  target: column.zs_observe.ekart_settlement.total_amount_of_batch
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
  edge_id: edge.metric_impl.ekart_settlement.batch_settlement_amount.uses_formula_template.formula_template.logistics.batch_deduplicated_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.ekart_settlement.batch_settlement_amount
  target: formula_template.logistics.batch_deduplicated_sum
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
  edge_id: edge.metric.settlement_batch_count.has_implementation.metric_impl.ekart_settlement.settlement_batch_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.settlement_batch_count
  target: metric_impl.ekart_settlement.settlement_batch_count
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
  edge_id: edge.metric_impl.ekart_settlement.settlement_batch_count.implements_metric.metric.settlement_batch_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_settlement.settlement_batch_count
  target: metric.settlement_batch_count
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
    materialized_from: edge.metric.settlement_batch_count.has_implementation.metric_impl.ekart_settlement.settlement_batch_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_settlement.settlement_batch_count.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: metric_impl.ekart_settlement.settlement_batch_count
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric_impl.ekart_settlement.settlement_batch_count.uses_column.column.zs_observe.ekart_settlement.settlement_id.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.settlement_batch_count
  target: column.zs_observe.ekart_settlement.settlement_id
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
  edge_id: edge.metric_impl.ekart_settlement.settlement_batch_count.uses_formula_template.formula_template.logistics.batch_deduplicated_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.ekart_settlement.settlement_batch_count
  target: formula_template.logistics.batch_deduplicated_sum
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
  edge_id: edge.metric.unique_awb_count.has_implementation.metric_impl.ekart_settlement.unique_awb_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.unique_awb_count
  target: metric_impl.ekart_settlement.unique_awb_count
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
  edge_id: edge.metric_impl.ekart_settlement.unique_awb_count.implements_metric.metric.unique_awb_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_settlement.unique_awb_count
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
    materialized_from: edge.metric.unique_awb_count.has_implementation.metric_impl.ekart_settlement.unique_awb_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_settlement.unique_awb_count.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: metric_impl.ekart_settlement.unique_awb_count
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric_impl.ekart_settlement.unique_awb_count.uses_column.column.zs_observe.ekart_settlement.shipment_id.9e2adfd1
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.unique_awb_count
  target: column.zs_observe.ekart_settlement.shipment_id
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
  edge_id: edge.metric_impl.ekart_settlement.unique_awb_count.uses_formula_template.formula_template.logistics.batch_deduplicated_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.ekart_settlement.unique_awb_count
  target: formula_template.logistics.batch_deduplicated_sum
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
  edge_id: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.ekart_settlement.cod_remittance_lag_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remittance_lag_days
  target: metric_impl.ekart_settlement.cod_remittance_lag_days
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
  edge_id: edge.metric_impl.ekart_settlement.cod_remittance_lag_days.implements_metric.metric.cod_remittance_lag_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_settlement.cod_remittance_lag_days
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
    materialized_from: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.ekart_settlement.cod_remittance_lag_days
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_settlement.cod_remittance_lag_days.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: metric_impl.ekart_settlement.cod_remittance_lag_days
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric_impl.ekart_settlement.cod_remittance_lag_days.uses_column.column.zs_observe.ekart_settlement.delivered_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.cod_remittance_lag_days
  target: column.zs_observe.ekart_settlement.delivered_date
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
  edge_id: edge.metric_impl.ekart_settlement.cod_remittance_lag_days.uses_column.column.zs_observe.ekart_settlement.actual_date_of_remittance.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.cod_remittance_lag_days
  target: column.zs_observe.ekart_settlement.actual_date_of_remittance
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
  edge_id: edge.metric_impl.ekart_settlement.cod_remittance_lag_days.uses_formula_template.formula_template.logistics.batch_deduplicated_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.ekart_settlement.cod_remittance_lag_days
  target: formula_template.logistics.batch_deduplicated_sum
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
  edge_id: edge.metric.declared_product_value.has_implementation.metric_impl.ekart_settlement.declared_product_value
  edge_type: HAS_IMPLEMENTATION
  source: metric.declared_product_value
  target: metric_impl.ekart_settlement.declared_product_value
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
  edge_id: edge.metric_impl.ekart_settlement.declared_product_value.implements_metric.metric.declared_product_value
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_settlement.declared_product_value
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
    materialized_from: edge.metric.declared_product_value.has_implementation.metric_impl.ekart_settlement.declared_product_value
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_settlement.declared_product_value.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: metric_impl.ekart_settlement.declared_product_value
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.metric_impl.ekart_settlement.declared_product_value.uses_column.column.zs_observe.ekart_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.ekart_settlement.declared_product_value
  target: column.zs_observe.ekart_settlement.charged_amount
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
  edge_id: edge.metric_impl.ekart_settlement.declared_product_value.uses_formula_template.formula_template.logistics.batch_deduplicated_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.ekart_settlement.declared_product_value
  target: formula_template.logistics.batch_deduplicated_sum
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
  edge_id: edge.metric.freight_billed_amount.has_implementation.metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_billed_amount
  target: metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty
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
  edge_id: edge.metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty.implements_metric.metric.freight_billed_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty
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
    materialized_from: edge.metric.freight_billed_amount.has_implementation.metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty.uses_table.table.zs_observe.ekart_invoice
  edge_type: USES_TABLE
  source: metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty
  target: table.zs_observe.ekart_invoice
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
  edge_id: edge.metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty.uses_column.column.zs_observe.ekart_invoice.invoice_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.ekart_invoice.freight_billed_amount.unsupported_empty
  target: column.zs_observe.ekart_invoice.invoice_number
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
  edge_id: edge.metric.forward_freight_amount.has_implementation.metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty
  edge_type: HAS_IMPLEMENTATION
  source: metric.forward_freight_amount
  target: metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty
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
  edge_id: edge.metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty.implements_metric.metric.forward_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty
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
    materialized_from: edge.metric.forward_freight_amount.has_implementation.metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty.uses_table.table.zs_observe.ekart_invoice
  edge_type: USES_TABLE
  source: metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty
  target: table.zs_observe.ekart_invoice
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
  edge_id: edge.metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty.uses_column.column.zs_observe.ekart_invoice.invoice_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.ekart_invoice.forward_freight_amount.unsupported_empty
  target: column.zs_observe.ekart_invoice.invoice_number
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
  edge_id: edge.metric.rto_freight_amount.has_implementation.metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_freight_amount
  target: metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty
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
  edge_id: edge.metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty.implements_metric.metric.rto_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty
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
    materialized_from: edge.metric.rto_freight_amount.has_implementation.metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty.uses_table.table.zs_observe.ekart_invoice
  edge_type: USES_TABLE
  source: metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty
  target: table.zs_observe.ekart_invoice
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
  edge_id: edge.metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty.uses_column.column.zs_observe.ekart_invoice.invoice_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.ekart_invoice.rto_freight_amount.unsupported_empty
  target: column.zs_observe.ekart_invoice.invoice_number
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
  edge_id: edge.metric.cod_fee_amount.has_implementation.metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_fee_amount
  target: metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty
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
  edge_id: edge.metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty.implements_metric.metric.cod_fee_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty
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
    materialized_from: edge.metric.cod_fee_amount.has_implementation.metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty.uses_table.table.zs_observe.ekart_invoice
  edge_type: USES_TABLE
  source: metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty
  target: table.zs_observe.ekart_invoice
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
  edge_id: edge.metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty.uses_column.column.zs_observe.ekart_invoice.invoice_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.ekart_invoice.cod_fee_amount.unsupported_empty
  target: column.zs_observe.ekart_invoice.invoice_number
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
  id: review.ekart_logistics_parser_ready_v4_unified_edges.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted
    from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```

## 7. Validation Summary

```yaml
validation_summary:
  document_id: ekart_logistics_parser_ready_v4_unified_edges
  candidate_cards: 58
  candidate_edges: 143
  card_types:
    metric: 12
    platform: 1
    platform_context: 1
    table: 2
    column: 26
    value_profile: 4
    metric_implementation: 12
  edge_types:
    BELONGS_TO_DOMAIN: 12
    BELONGS_TO_PLATFORM: 1
    HAS_PLATFORM_CONTEXT: 1
    SOURCED_FROM_PLATFORM: 2
    APPLIES_TO_PLATFORM: 2
    HAS_COLUMN: 26
    BELONGS_TO_TABLE: 26
    HAS_VALUE_PROFILE: 8
    PROFILES_COLUMN: 4
    PROFILES_TABLE: 4
    HAS_IMPLEMENTATION: 12
    IMPLEMENTS_METRIC: 12
    USES_TABLE: 12
    USES_COLUMN: 13
    USES_FORMULA_TEMPLATE: 8
  forbidden_card_types_present: []
  parser_boundary: generic logistics reusable knowledge only
```
