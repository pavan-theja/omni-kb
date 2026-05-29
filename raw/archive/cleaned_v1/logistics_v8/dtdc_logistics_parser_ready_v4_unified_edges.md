# DTDC Logistics Knowledge — Parser Ready v4 Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: dtdc_logistics_parser_ready_v4_unified_edges
  title: DTDC Logistics Knowledge — Parser Ready v4 Unified Edges
  domain: logistics
  vendor: DTDC
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style
  generated_on: '2026-05-20'
  version: 4.0-unified-edges
  scope: dtdc_vendor_logistics_with_unified_edges
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
  id: evidence.dtdc.vendor_scope
  source_document: Logistics KB Doc.docx
  summary: 'Vendor-specific extracted evidence for dtdc: table role, coverage status, metrics, caveats, and joins.'
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
  card_id: platform.dtdc
  name: DTDC
  fields:
    name: DTDC
    description: DTDC logistics platform/vendor in the logistics domain.
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
    platform_name: DTDC
    platform_type: courier
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
  card_id: platform_context.dtdc.in
  name: DTDC India
  fields:
    name: DTDC India
    description: India logistics context for DTDC.
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
    platform_id: platform.dtdc
    context_name: DTDC India
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
  card_id: table.zs_observe.dtdc_settlement
  name: DTDC Settlement
  fields:
    name: DTDC Settlement
    description: 'DTDC Settlement: One row per DTDC AWB-level COD remittance.'
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
    table_name: dtdc_settlement
    full_reference: zs_observe.dtdc_settlement
    engine: Athena v3 / Trino SQL
    table_type: cod_settlement
    source_platform_ids:
    - platform.dtdc
    source_platform_types:
    - logistics
    business_purpose: One row per DTDC AWB-level COD remittance.
    grain: One row per DTDC AWB-level COD remittance.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.dtdc; account filters are not defined here
    coverage_status: active
    row_count: '3130'
    period: '-'
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
  card_id: table.zs_observe.dtdc_invoice
  name: DTDC Invoice
  fields:
    name: DTDC Invoice
    description: 'DTDC Invoice: DTDC invoice table exists but has no loaded freight billing rows.'
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
    table_name: dtdc_invoice
    full_reference: zs_observe.dtdc_invoice
    engine: Athena v3 / Trino SQL
    table_type: schema_only_invoice
    source_platform_ids:
    - platform.dtdc
    source_platform_types:
    - logistics
    business_purpose: DTDC invoice table exists but has no loaded freight billing rows.
    grain: DTDC invoice table exists but has no loaded freight billing rows.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.dtdc; account filters are not defined here
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
  card_id: column.zs_observe.dtdc_settlement.order_id
  name: dtdc_settlement.order_id
  fields:
    name: dtdc_settlement.order_id
    description: Merchant order ID, often I-prefix pattern.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Merchant order ID, often I-prefix pattern.
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
  card_id: column.zs_observe.dtdc_settlement.airwaybill_number
  name: dtdc_settlement.airwaybill_number
  fields:
    name: dtdc_settlement.airwaybill_number
    description: DTDC AWB number.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: airwaybill_number
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - DTDC AWB number.
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
  card_id: column.zs_observe.dtdc_settlement.order_status
  name: dtdc_settlement.order_status
  fields:
    name: dtdc_settlement.order_status
    description: Delivery status.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: order_status
    data_type: unknown
    semantic_roles: status
    business_concepts:
    - Delivery status.
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
  card_id: column.zs_observe.dtdc_settlement.charged_amount
  name: dtdc_settlement.charged_amount
  fields:
    name: dtdc_settlement.charged_amount
    description: COD amount remitted/product value, not freight.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount remitted/product value, not freight.
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
  card_id: column.zs_observe.dtdc_settlement.cod_amount
  name: dtdc_settlement.cod_amount
  fields:
    name: dtdc_settlement.cod_amount
    description: COD amount collected.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: cod_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount collected.
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
  card_id: column.zs_observe.dtdc_settlement.cod_due
  name: dtdc_settlement.cod_due
  fields:
    name: dtdc_settlement.cod_due
    description: COD amount yet to be remitted.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: cod_due
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount yet to be remitted.
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
  card_id: column.zs_observe.dtdc_settlement.transaction_type
  name: dtdc_settlement.transaction_type
  fields:
    name: dtdc_settlement.transaction_type
    description: Remitted for COD remittance rows.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: transaction_type
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - Remitted for COD remittance rows.
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
  card_id: column.zs_observe.dtdc_settlement.settlement_date
  name: dtdc_settlement.settlement_date
  fields:
    name: dtdc_settlement.settlement_date
    description: Date of DTDC-to-seller transfer.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: settlement_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Date of DTDC-to-seller transfer.
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
  card_id: column.zs_observe.dtdc_settlement.created_date
  name: dtdc_settlement.created_date
  fields:
    name: dtdc_settlement.created_date
    description: Original shipment date.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: created_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Original shipment date.
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
  card_id: column.zs_observe.dtdc_settlement.invoice_number
  name: dtdc_settlement.invoice_number
  fields:
    name: dtdc_settlement.invoice_number
    description: DTDC invoice reference.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: invoice_number
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - DTDC invoice reference.
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
  card_id: column.zs_observe.dtdc_settlement.utr_no
  name: dtdc_settlement.utr_no
  fields:
    name: dtdc_settlement.utr_no
    description: Bank UTR for remittance.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: utr_no
    data_type: unknown
    semantic_roles: identifier;bank_bridge
    business_concepts:
    - Bank UTR for remittance.
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
  card_id: column.zs_observe.dtdc_settlement.utr_date
  name: dtdc_settlement.utr_date
  fields:
    name: dtdc_settlement.utr_date
    description: UTR transaction date.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: utr_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - UTR transaction date.
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
  card_id: column.zs_observe.dtdc_settlement.delivery_date
  name: dtdc_settlement.delivery_date
  fields:
    name: dtdc_settlement.delivery_date
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: delivery_date
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
  card_id: column.zs_observe.dtdc_settlement.pickup_date
  name: dtdc_settlement.pickup_date
  fields:
    name: dtdc_settlement.pickup_date
    description: Pickup date.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: pickup_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Pickup date.
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
  card_id: column.zs_observe.dtdc_settlement.zone_name
  name: dtdc_settlement.zone_name
  fields:
    name: dtdc_settlement.zone_name
    description: Delivery zone name.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: zone_name
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Delivery zone name.
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
  card_id: column.zs_observe.dtdc_settlement.shipment_no
  name: dtdc_settlement.shipment_no
  fields:
    name: dtdc_settlement.shipment_no
    description: DTDC internal shipment number.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: shipment_no
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - DTDC internal shipment number.
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
  card_id: column.zs_observe.dtdc_settlement.bank_ref_number
  name: dtdc_settlement.bank_ref_number
  fields:
    name: dtdc_settlement.bank_ref_number
    description: Bank remittance batch/reference number.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: bank_ref_number
    data_type: unknown
    semantic_roles: identifier;bank_bridge
    business_concepts:
    - Bank remittance batch/reference number.
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
  card_id: column.zs_observe.dtdc_settlement.reference_no
  name: dtdc_settlement.reference_no
  fields:
    name: dtdc_settlement.reference_no
    description: Merchant reference number.
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
    table_id: table.zs_observe.dtdc_settlement
    column_name: reference_no
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Merchant reference number.
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
  card_id: column.zs_observe.dtdc_settlement.is_active
  name: dtdc_settlement.is_active
  fields:
    name: dtdc_settlement.is_active
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
    table_id: table.zs_observe.dtdc_settlement
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
  card_id: column.zs_observe.dtdc_settlement.group_level_id
  name: dtdc_settlement.group_level_id
  fields:
    name: dtdc_settlement.group_level_id
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
    table_id: table.zs_observe.dtdc_settlement
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
  card_id: column.zs_observe.dtdc_invoice.order_id
  name: dtdc_invoice.order_id
  fields:
    name: dtdc_invoice.order_id
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
    table_id: table.zs_observe.dtdc_invoice
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
  card_id: column.zs_observe.dtdc_invoice.invoice_number
  name: dtdc_invoice.invoice_number
  fields:
    name: dtdc_invoice.invoice_number
    description: DTDC invoice number.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: invoice_number
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - DTDC invoice number.
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
  card_id: column.zs_observe.dtdc_invoice.transaction_type
  name: dtdc_invoice.transaction_type
  fields:
    name: dtdc_invoice.transaction_type
    description: Freight transaction type.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: transaction_type
    data_type: unknown
    semantic_roles: status
    business_concepts:
    - Freight transaction type.
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
  card_id: column.zs_observe.dtdc_invoice.fulfilment_channel
  name: dtdc_invoice.fulfilment_channel
  fields:
    name: dtdc_invoice.fulfilment_channel
    description: Fulfilment method.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: fulfilment_channel
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Fulfilment method.
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
  card_id: column.zs_observe.dtdc_invoice.destination_city
  name: dtdc_invoice.destination_city
  fields:
    name: dtdc_invoice.destination_city
    description: Destination city.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: destination_city
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Destination city.
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
  card_id: column.zs_observe.dtdc_invoice.source_city
  name: dtdc_invoice.source_city
  fields:
    name: dtdc_invoice.source_city
    description: Source city.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: source_city
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Source city.
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
  card_id: column.zs_observe.dtdc_invoice.mp_fees
  name: dtdc_invoice.mp_fees
  fields:
    name: dtdc_invoice.mp_fees
    description: Marketplace fees if applicable.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: mp_fees
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Marketplace fees if applicable.
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
  card_id: column.zs_observe.dtdc_invoice.mp_fees_gst_amount
  name: dtdc_invoice.mp_fees_gst_amount
  fields:
    name: dtdc_invoice.mp_fees_gst_amount
    description: GST on marketplace fees.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: mp_fees_gst_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - GST on marketplace fees.
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
  card_id: column.zs_observe.dtdc_invoice.freight_charge
  name: dtdc_invoice.freight_charge
  fields:
    name: dtdc_invoice.freight_charge
    description: Forward freight.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: freight_charge
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Forward freight.
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
  card_id: column.zs_observe.dtdc_invoice.cod_charge
  name: dtdc_invoice.cod_charge
  fields:
    name: dtdc_invoice.cod_charge
    description: COD collection fee.
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
    table_id: table.zs_observe.dtdc_invoice
    column_name: cod_charge
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD collection fee.
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
  card_id: column.zs_observe.dtdc_invoice.charge_rto
  name: dtdc_invoice.charge_rto
  fields:
    name: dtdc_invoice.charge_rto
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
    table_id: table.zs_observe.dtdc_invoice
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
  card_id: column.zs_observe.dtdc_invoice.zone
  name: dtdc_invoice.zone
  fields:
    name: dtdc_invoice.zone
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
    table_id: table.zs_observe.dtdc_invoice
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
  card_id: column.zs_observe.dtdc_invoice.charged_weight
  name: dtdc_invoice.charged_weight
  fields:
    name: dtdc_invoice.charged_weight
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
    table_id: table.zs_observe.dtdc_invoice
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
  card_id: value_profile.dtdc_settlement.transaction_type
  name: dtdc_settlement.transaction_type Value Profile
  fields:
    name: dtdc_settlement.transaction_type Value Profile
    description: Known values and meanings for dtdc_settlement.transaction_type.
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
    table_id: table.zs_observe.dtdc_settlement
    column_id: column.zs_observe.dtdc_settlement.transaction_type
    value_type: enum_or_enum_with_nulls
    values: Remitted=COD remitted by DTDC (cod_remitted)
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
  card_id: value_profile.dtdc_settlement.order_id
  name: dtdc_settlement.order_id Value Profile
  fields:
    name: dtdc_settlement.order_id Value Profile
    description: Known values and meanings for dtdc_settlement.order_id.
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
    table_id: table.zs_observe.dtdc_settlement
    column_id: column.zs_observe.dtdc_settlement.order_id
    value_type: enum_or_enum_with_nulls
    values: I########=I-prefix order pattern likely marketplace/internal (marketplace_like)
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_due_amount
  name: COD Due Amount
  fields:
    name: COD Due Amount
    description: COD amount still due or not remitted.
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
    metric_name: COD Due Amount
    aliases:
    - COD outstanding
    - unremitted COD
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_due_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in dtdc_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.9 metric_implementation cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_settlement.cod_collected_amount
  name: DTDC COD Collected Amount Implementation
  fields:
    name: DTDC COD Collected Amount Implementation
    description: COD Collected Amount implementation for DTDC using dtdc_settlement.
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
    implementation_name: DTDC COD Collected Amount
    metric_pattern: filtered_sum_or_lag
    applicability: platform=dtdc; table=zs_observe.dtdc_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_settlement
    required_columns:
    - column.zs_observe.dtdc_settlement.cod_amount
    semantic_filters:
    - transaction_type='Remitted'
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
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: DTDC settlement is COD remittance; dtdc_invoice is empty for freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_settlement.cod_remitted_amount
  name: DTDC COD Remitted Amount Implementation
  fields:
    name: DTDC COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for DTDC using dtdc_settlement.
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
    implementation_name: DTDC COD Remitted Amount
    metric_pattern: filtered_sum_or_lag
    applicability: platform=dtdc; table=zs_observe.dtdc_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_settlement
    required_columns:
    - column.zs_observe.dtdc_settlement.charged_amount
    semantic_filters:
    - transaction_type='Remitted'
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
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: DTDC settlement is COD remittance; dtdc_invoice is empty for freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_settlement.cod_due_amount
  name: DTDC COD Due Amount Implementation
  fields:
    name: DTDC COD Due Amount Implementation
    description: COD Due Amount implementation for DTDC using dtdc_settlement.
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
    metric_id: metric.cod_due_amount
    implementation_name: DTDC COD Due Amount
    metric_pattern: filtered_sum_or_lag
    applicability: platform=dtdc; table=zs_observe.dtdc_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_settlement
    required_columns:
    - column.zs_observe.dtdc_settlement.cod_due
    semantic_filters:
    - transaction_type='Remitted'
    formula_description: SUM(cod_due)
    formula_sql: SUM(cod_due)
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
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: DTDC settlement is COD remittance; dtdc_invoice is empty for freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_settlement.unique_awb_count
  name: DTDC Unique AWB Count Implementation
  fields:
    name: DTDC Unique AWB Count Implementation
    description: Unique AWB Count implementation for DTDC using dtdc_settlement.
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
    implementation_name: DTDC Unique AWB Count
    metric_pattern: filtered_sum_or_lag
    applicability: platform=dtdc; table=zs_observe.dtdc_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_settlement
    required_columns:
    - column.zs_observe.dtdc_settlement.airwaybill_number
    semantic_filters:
    - transaction_type='Remitted'
    formula_description: COUNT(DISTINCT airwaybill_number)
    formula_sql: COUNT(DISTINCT airwaybill_number)
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
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: DTDC settlement is COD remittance; dtdc_invoice is empty for freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_settlement.settlement_batch_count
  name: DTDC Settlement Batch Count Implementation
  fields:
    name: DTDC Settlement Batch Count Implementation
    description: Settlement Batch Count implementation for DTDC using dtdc_settlement.
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
    implementation_name: DTDC Settlement Batch Count
    metric_pattern: filtered_sum_or_lag
    applicability: platform=dtdc; table=zs_observe.dtdc_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_settlement
    required_columns:
    - column.zs_observe.dtdc_settlement.bank_ref_number
    semantic_filters:
    - transaction_type='Remitted'
    formula_description: COUNT(DISTINCT bank_ref_number)
    formula_sql: COUNT(DISTINCT bank_ref_number)
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
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: DTDC settlement is COD remittance; dtdc_invoice is empty for freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_settlement.cod_remittance_lag_days
  name: DTDC COD Remittance Lag Days Implementation
  fields:
    name: DTDC COD Remittance Lag Days Implementation
    description: COD Remittance Lag Days implementation for DTDC using dtdc_settlement.
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
    implementation_name: DTDC COD Remittance Lag Days
    metric_pattern: filtered_sum_or_lag
    applicability: platform=dtdc; table=zs_observe.dtdc_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_settlement
    required_columns:
    - column.zs_observe.dtdc_settlement.delivery_date
    - column.zs_observe.dtdc_settlement.settlement_date
    semantic_filters:
    - transaction_type='Remitted'
    formula_description: AVG(DATE_DIFF('day', delivery_date, settlement_date))
    formula_sql: AVG(DATE_DIFF('day', delivery_date, settlement_date))
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
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: DTDC settlement is COD remittance; dtdc_invoice is empty for freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_settlement.delivery_tat_days
  name: DTDC Delivery TAT Days Implementation
  fields:
    name: DTDC Delivery TAT Days Implementation
    description: Delivery TAT Days implementation for DTDC using dtdc_settlement.
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
    implementation_name: DTDC Delivery TAT Days
    metric_pattern: filtered_sum_or_lag
    applicability: platform=dtdc; table=zs_observe.dtdc_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_settlement
    required_columns:
    - column.zs_observe.dtdc_settlement.pickup_date
    - column.zs_observe.dtdc_settlement.delivery_date
    semantic_filters:
    - transaction_type='Remitted'
    formula_description: AVG(DATE_DIFF('day', pickup_date, delivery_date))
    formula_sql: AVG(DATE_DIFF('day', pickup_date, delivery_date))
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
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: DTDC settlement is COD remittance; dtdc_invoice is empty for freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty
  name: DTDC Freight Billed Amount Implementation
  fields:
    name: DTDC Freight Billed Amount Implementation
    description: Freight Billed Amount implementation for DTDC using dtdc_invoice.
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
    implementation_name: DTDC Freight Billed Amount
    metric_pattern: unsupported_empty_table
    applicability: platform=dtdc; table=zs_observe.dtdc_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_invoice
    required_columns:
    - column.zs_observe.dtdc_invoice.invoice_number
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
    caveats: dtdc_invoice has zero rows; use shiprocket_invoice courier_partner=DTDC Air 500gm where aggregator evidence is
      valid.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty
  name: DTDC Forward Freight Amount Implementation
  fields:
    name: DTDC Forward Freight Amount Implementation
    description: Forward Freight Amount implementation for DTDC using dtdc_invoice.
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
    implementation_name: DTDC Forward Freight Amount
    metric_pattern: unsupported_empty_table
    applicability: platform=dtdc; table=zs_observe.dtdc_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_invoice
    required_columns:
    - column.zs_observe.dtdc_invoice.invoice_number
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
    caveats: dtdc_invoice has zero rows; use shiprocket_invoice courier_partner=DTDC Air 500gm where aggregator evidence is
      valid.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty
  name: DTDC RTO Freight Amount Implementation
  fields:
    name: DTDC RTO Freight Amount Implementation
    description: RTO Freight Amount implementation for DTDC using dtdc_invoice.
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
    implementation_name: DTDC RTO Freight Amount
    metric_pattern: unsupported_empty_table
    applicability: platform=dtdc; table=zs_observe.dtdc_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_invoice
    required_columns:
    - column.zs_observe.dtdc_invoice.invoice_number
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
    caveats: dtdc_invoice has zero rows; use shiprocket_invoice courier_partner=DTDC Air 500gm where aggregator evidence is
      valid.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty
  name: DTDC COD Fee Amount Implementation
  fields:
    name: DTDC COD Fee Amount Implementation
    description: COD Fee Amount implementation for DTDC using dtdc_invoice.
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
    implementation_name: DTDC COD Fee Amount
    metric_pattern: unsupported_empty_table
    applicability: platform=dtdc; table=zs_observe.dtdc_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.dtdc_invoice
    required_columns:
    - column.zs_observe.dtdc_invoice.invoice_number
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
    caveats: dtdc_invoice has zero rows; use shiprocket_invoice courier_partner=DTDC Air 500gm where aggregator evidence is
      valid.
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
  edge_id: edge.metric.cod_due_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_due_amount
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
  edge_id: edge.platform_context.dtdc.in.belongs_to_platform.platform.dtdc
  edge_type: BELONGS_TO_PLATFORM
  source: platform_context.dtdc.in
  target: platform.dtdc
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
  edge_id: edge.platform.dtdc.has_platform_context.platform_context.dtdc.in
  edge_type: HAS_PLATFORM_CONTEXT
  source: platform.dtdc
  target: platform_context.dtdc.in
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
    materialized_from: edge.platform_context.dtdc.in.belongs_to_platform.platform.dtdc
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.sourced_from_platform.platform.dtdc
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.dtdc_settlement
  target: platform.dtdc
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
  edge_id: edge.table.zs_observe.dtdc_settlement.applies_to_platform.platform.dtdc
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.dtdc_settlement
  target: platform.dtdc
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
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.order_id
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
  edge_id: edge.column.zs_observe.dtdc_settlement.order_id.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.order_id
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.airwaybill_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.airwaybill_number
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
  edge_id: edge.column.zs_observe.dtdc_settlement.airwaybill_number.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.airwaybill_number
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.airwaybill_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.order_status
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.order_status
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
  edge_id: edge.column.zs_observe.dtdc_settlement.order_status.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.order_status
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.order_status
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.charged_amount
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
  edge_id: edge.column.zs_observe.dtdc_settlement.charged_amount.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.charged_amount
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.charged_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.cod_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.cod_amount
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
  edge_id: edge.column.zs_observe.dtdc_settlement.cod_amount.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.cod_amount
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.cod_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.cod_due
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.cod_due
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
  edge_id: edge.column.zs_observe.dtdc_settlement.cod_due.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.cod_due
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.cod_due
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.transaction_type
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.transaction_type
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
  edge_id: edge.column.zs_observe.dtdc_settlement.transaction_type.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.transaction_type
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.settlement_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.settlement_date
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
  edge_id: edge.column.zs_observe.dtdc_settlement.settlement_date.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.settlement_date
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.settlement_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.created_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.created_date
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
  edge_id: edge.column.zs_observe.dtdc_settlement.created_date.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.created_date
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.created_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.invoice_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.invoice_number
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
  edge_id: edge.column.zs_observe.dtdc_settlement.invoice_number.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.invoice_number
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.invoice_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.utr_no
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.utr_no
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
  edge_id: edge.column.zs_observe.dtdc_settlement.utr_no.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.utr_no
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.utr_no
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.utr_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.utr_date
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
  edge_id: edge.column.zs_observe.dtdc_settlement.utr_date.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.utr_date
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.utr_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.delivery_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.delivery_date
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
  edge_id: edge.column.zs_observe.dtdc_settlement.delivery_date.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.delivery_date
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.delivery_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.pickup_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.pickup_date
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
  edge_id: edge.column.zs_observe.dtdc_settlement.pickup_date.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.pickup_date
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.pickup_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.zone_name
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.zone_name
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
  edge_id: edge.column.zs_observe.dtdc_settlement.zone_name.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.zone_name
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.zone_name
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.shipment_no
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.shipment_no
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
  edge_id: edge.column.zs_observe.dtdc_settlement.shipment_no.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.shipment_no
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.shipment_no
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.bank_ref_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.bank_ref_number
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
  edge_id: edge.column.zs_observe.dtdc_settlement.bank_ref_number.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.bank_ref_number
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.bank_ref_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.reference_no
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.reference_no
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
  edge_id: edge.column.zs_observe.dtdc_settlement.reference_no.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.reference_no
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.reference_no
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.is_active
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
  edge_id: edge.column.zs_observe.dtdc_settlement.is_active.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.is_active
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.is_active
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_settlement
  target: column.zs_observe.dtdc_settlement.group_level_id
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
  edge_id: edge.column.zs_observe.dtdc_settlement.group_level_id.belongs_to_table.table.zs_observe.dtdc_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_settlement.group_level_id
  target: table.zs_observe.dtdc_settlement
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
    materialized_from: edge.table.zs_observe.dtdc_settlement.has_column.column.zs_observe.dtdc_settlement.group_level_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.sourced_from_platform.platform.dtdc
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.dtdc_invoice
  target: platform.dtdc
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
  edge_id: edge.table.zs_observe.dtdc_invoice.applies_to_platform.platform.dtdc
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.dtdc_invoice
  target: platform.dtdc
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
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.order_id
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
  edge_id: edge.column.zs_observe.dtdc_invoice.order_id.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.order_id
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.invoice_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.invoice_number
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
  edge_id: edge.column.zs_observe.dtdc_invoice.invoice_number.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.invoice_number
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.invoice_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.transaction_type
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.transaction_type
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
  edge_id: edge.column.zs_observe.dtdc_invoice.transaction_type.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.transaction_type
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.fulfilment_channel
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.fulfilment_channel
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
  edge_id: edge.column.zs_observe.dtdc_invoice.fulfilment_channel.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.fulfilment_channel
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.fulfilment_channel
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.destination_city
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.destination_city
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
  edge_id: edge.column.zs_observe.dtdc_invoice.destination_city.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.destination_city
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.destination_city
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.source_city
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.source_city
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
  edge_id: edge.column.zs_observe.dtdc_invoice.source_city.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.source_city
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.source_city
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.mp_fees
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.mp_fees
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
  edge_id: edge.column.zs_observe.dtdc_invoice.mp_fees.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.mp_fees
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.mp_fees
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.mp_fees_gst_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.mp_fees_gst_amount
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
  edge_id: edge.column.zs_observe.dtdc_invoice.mp_fees_gst_amount.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.mp_fees_gst_amount
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.mp_fees_gst_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.freight_charge
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.freight_charge
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
  edge_id: edge.column.zs_observe.dtdc_invoice.freight_charge.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.freight_charge
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.freight_charge
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.cod_charge
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.cod_charge
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
  edge_id: edge.column.zs_observe.dtdc_invoice.cod_charge.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.cod_charge
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.cod_charge
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.charge_rto
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.charge_rto
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
  edge_id: edge.column.zs_observe.dtdc_invoice.charge_rto.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.charge_rto
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.charge_rto
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.zone
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.zone
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
  edge_id: edge.column.zs_observe.dtdc_invoice.zone.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.zone
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.zone
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.charged_weight
  edge_type: HAS_COLUMN
  source: table.zs_observe.dtdc_invoice
  target: column.zs_observe.dtdc_invoice.charged_weight
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
  edge_id: edge.column.zs_observe.dtdc_invoice.charged_weight.belongs_to_table.table.zs_observe.dtdc_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.dtdc_invoice.charged_weight
  target: table.zs_observe.dtdc_invoice
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
    materialized_from: edge.table.zs_observe.dtdc_invoice.has_column.column.zs_observe.dtdc_invoice.charged_weight
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_value_profile.value_profile.dtdc_settlement.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.dtdc_settlement
  target: value_profile.dtdc_settlement.transaction_type
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
  edge_id: edge.value_profile.dtdc_settlement.transaction_type.profiles_column.column.zs_observe.dtdc_settlement.transaction_type
  edge_type: PROFILES_COLUMN
  source: value_profile.dtdc_settlement.transaction_type
  target: column.zs_observe.dtdc_settlement.transaction_type
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
  edge_id: edge.column.zs_observe.dtdc_settlement.transaction_type.has_value_profile.value_profile.dtdc_settlement.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.dtdc_settlement.transaction_type
  target: value_profile.dtdc_settlement.transaction_type
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
    materialized_from: edge.value_profile.dtdc_settlement.transaction_type.profiles_column.column.zs_observe.dtdc_settlement.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.dtdc_settlement.transaction_type.profiles_table.table.zs_observe.dtdc_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.dtdc_settlement.transaction_type
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.table.zs_observe.dtdc_settlement.has_value_profile.value_profile.dtdc_settlement.order_id
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.dtdc_settlement
  target: value_profile.dtdc_settlement.order_id
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
  edge_id: edge.value_profile.dtdc_settlement.order_id.profiles_column.column.zs_observe.dtdc_settlement.order_id
  edge_type: PROFILES_COLUMN
  source: value_profile.dtdc_settlement.order_id
  target: column.zs_observe.dtdc_settlement.order_id
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
  edge_id: edge.column.zs_observe.dtdc_settlement.order_id.has_value_profile.value_profile.dtdc_settlement.order_id
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.dtdc_settlement.order_id
  target: value_profile.dtdc_settlement.order_id
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
    materialized_from: edge.value_profile.dtdc_settlement.order_id.profiles_column.column.zs_observe.dtdc_settlement.order_id
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.dtdc_settlement.order_id.profiles_table.table.zs_observe.dtdc_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.dtdc_settlement.order_id
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.metric.cod_collected_amount.has_implementation.metric_impl.dtdc_settlement.cod_collected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_collected_amount
  target: metric_impl.dtdc_settlement.cod_collected_amount
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_collected_amount.implements_metric.metric.cod_collected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_settlement.cod_collected_amount
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
    materialized_from: edge.metric.cod_collected_amount.has_implementation.metric_impl.dtdc_settlement.cod_collected_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_settlement.cod_collected_amount.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: metric_impl.dtdc_settlement.cod_collected_amount
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_collected_amount.uses_column.column.zs_observe.dtdc_settlement.cod_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.cod_collected_amount
  target: column.zs_observe.dtdc_settlement.cod_amount
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.dtdc_settlement.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.dtdc_settlement.cod_remitted_amount
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_settlement.cod_remitted_amount
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.dtdc_settlement.cod_remitted_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_settlement.cod_remitted_amount.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: metric_impl.dtdc_settlement.cod_remitted_amount
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_remitted_amount.uses_column.column.zs_observe.dtdc_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.cod_remitted_amount
  target: column.zs_observe.dtdc_settlement.charged_amount
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
  edge_id: edge.metric.cod_due_amount.has_implementation.metric_impl.dtdc_settlement.cod_due_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_due_amount
  target: metric_impl.dtdc_settlement.cod_due_amount
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_due_amount.implements_metric.metric.cod_due_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_settlement.cod_due_amount
  target: metric.cod_due_amount
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
    materialized_from: edge.metric.cod_due_amount.has_implementation.metric_impl.dtdc_settlement.cod_due_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_settlement.cod_due_amount.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: metric_impl.dtdc_settlement.cod_due_amount
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_due_amount.uses_column.column.zs_observe.dtdc_settlement.cod_due.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.cod_due_amount
  target: column.zs_observe.dtdc_settlement.cod_due
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
  edge_id: edge.metric.unique_awb_count.has_implementation.metric_impl.dtdc_settlement.unique_awb_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.unique_awb_count
  target: metric_impl.dtdc_settlement.unique_awb_count
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
  edge_id: edge.metric_impl.dtdc_settlement.unique_awb_count.implements_metric.metric.unique_awb_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_settlement.unique_awb_count
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
    materialized_from: edge.metric.unique_awb_count.has_implementation.metric_impl.dtdc_settlement.unique_awb_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_settlement.unique_awb_count.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: metric_impl.dtdc_settlement.unique_awb_count
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.metric_impl.dtdc_settlement.unique_awb_count.uses_column.column.zs_observe.dtdc_settlement.airwaybill_number.9e2adfd1
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.unique_awb_count
  target: column.zs_observe.dtdc_settlement.airwaybill_number
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
  edge_id: edge.metric.settlement_batch_count.has_implementation.metric_impl.dtdc_settlement.settlement_batch_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.settlement_batch_count
  target: metric_impl.dtdc_settlement.settlement_batch_count
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
  edge_id: edge.metric_impl.dtdc_settlement.settlement_batch_count.implements_metric.metric.settlement_batch_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_settlement.settlement_batch_count
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
    materialized_from: edge.metric.settlement_batch_count.has_implementation.metric_impl.dtdc_settlement.settlement_batch_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_settlement.settlement_batch_count.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: metric_impl.dtdc_settlement.settlement_batch_count
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.metric_impl.dtdc_settlement.settlement_batch_count.uses_column.column.zs_observe.dtdc_settlement.bank_ref_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.settlement_batch_count
  target: column.zs_observe.dtdc_settlement.bank_ref_number
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
  edge_id: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.dtdc_settlement.cod_remittance_lag_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remittance_lag_days
  target: metric_impl.dtdc_settlement.cod_remittance_lag_days
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_remittance_lag_days.implements_metric.metric.cod_remittance_lag_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_settlement.cod_remittance_lag_days
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
    materialized_from: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.dtdc_settlement.cod_remittance_lag_days
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_settlement.cod_remittance_lag_days.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: metric_impl.dtdc_settlement.cod_remittance_lag_days
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_remittance_lag_days.uses_column.column.zs_observe.dtdc_settlement.delivery_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.cod_remittance_lag_days
  target: column.zs_observe.dtdc_settlement.delivery_date
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
  edge_id: edge.metric_impl.dtdc_settlement.cod_remittance_lag_days.uses_column.column.zs_observe.dtdc_settlement.settlement_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.cod_remittance_lag_days
  target: column.zs_observe.dtdc_settlement.settlement_date
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
  edge_id: edge.metric.delivery_tat_days.has_implementation.metric_impl.dtdc_settlement.delivery_tat_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.delivery_tat_days
  target: metric_impl.dtdc_settlement.delivery_tat_days
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
  edge_id: edge.metric_impl.dtdc_settlement.delivery_tat_days.implements_metric.metric.delivery_tat_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_settlement.delivery_tat_days
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
    materialized_from: edge.metric.delivery_tat_days.has_implementation.metric_impl.dtdc_settlement.delivery_tat_days
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_settlement.delivery_tat_days.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: metric_impl.dtdc_settlement.delivery_tat_days
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.metric_impl.dtdc_settlement.delivery_tat_days.uses_column.column.zs_observe.dtdc_settlement.pickup_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.delivery_tat_days
  target: column.zs_observe.dtdc_settlement.pickup_date
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
  edge_id: edge.metric_impl.dtdc_settlement.delivery_tat_days.uses_column.column.zs_observe.dtdc_settlement.delivery_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_settlement.delivery_tat_days
  target: column.zs_observe.dtdc_settlement.delivery_date
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
  edge_id: edge.metric.freight_billed_amount.has_implementation.metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_billed_amount
  target: metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty
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
  edge_id: edge.metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty.implements_metric.metric.freight_billed_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty
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
    materialized_from: edge.metric.freight_billed_amount.has_implementation.metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty.uses_table.table.zs_observe.dtdc_invoice
  edge_type: USES_TABLE
  source: metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty
  target: table.zs_observe.dtdc_invoice
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
  edge_id: edge.metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty.uses_column.column.zs_observe.dtdc_invoice.invoice_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_invoice.freight_billed_amount.unsupported_empty
  target: column.zs_observe.dtdc_invoice.invoice_number
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
  edge_id: edge.metric.forward_freight_amount.has_implementation.metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty
  edge_type: HAS_IMPLEMENTATION
  source: metric.forward_freight_amount
  target: metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty
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
  edge_id: edge.metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty.implements_metric.metric.forward_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty
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
    materialized_from: edge.metric.forward_freight_amount.has_implementation.metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty.uses_table.table.zs_observe.dtdc_invoice
  edge_type: USES_TABLE
  source: metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty
  target: table.zs_observe.dtdc_invoice
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
  edge_id: edge.metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty.uses_column.column.zs_observe.dtdc_invoice.invoice_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_invoice.forward_freight_amount.unsupported_empty
  target: column.zs_observe.dtdc_invoice.invoice_number
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
  edge_id: edge.metric.rto_freight_amount.has_implementation.metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_freight_amount
  target: metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty
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
  edge_id: edge.metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty.implements_metric.metric.rto_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty
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
    materialized_from: edge.metric.rto_freight_amount.has_implementation.metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty.uses_table.table.zs_observe.dtdc_invoice
  edge_type: USES_TABLE
  source: metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty
  target: table.zs_observe.dtdc_invoice
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
  edge_id: edge.metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty.uses_column.column.zs_observe.dtdc_invoice.invoice_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_invoice.rto_freight_amount.unsupported_empty
  target: column.zs_observe.dtdc_invoice.invoice_number
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
  edge_id: edge.metric.cod_fee_amount.has_implementation.metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_fee_amount
  target: metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty
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
  edge_id: edge.metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty.implements_metric.metric.cod_fee_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty
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
    materialized_from: edge.metric.cod_fee_amount.has_implementation.metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty.uses_table.table.zs_observe.dtdc_invoice
  edge_type: USES_TABLE
  source: metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty
  target: table.zs_observe.dtdc_invoice
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
  edge_id: edge.metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty.uses_column.column.zs_observe.dtdc_invoice.invoice_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.dtdc_invoice.cod_fee_amount.unsupported_empty
  target: column.zs_observe.dtdc_invoice.invoice_number
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
  id: review.dtdc_logistics_parser_ready_v4_unified_edges.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted
    from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```

## 7. Validation Summary

```yaml
validation_summary:
  document_id: dtdc_logistics_parser_ready_v4_unified_edges
  candidate_cards: 61
  candidate_edges: 137
  card_types:
    metric: 11
    platform: 1
    platform_context: 1
    table: 2
    column: 33
    value_profile: 2
    metric_implementation: 11
  edge_types:
    BELONGS_TO_DOMAIN: 11
    BELONGS_TO_PLATFORM: 1
    HAS_PLATFORM_CONTEXT: 1
    SOURCED_FROM_PLATFORM: 2
    APPLIES_TO_PLATFORM: 2
    HAS_COLUMN: 33
    BELONGS_TO_TABLE: 33
    HAS_VALUE_PROFILE: 4
    PROFILES_COLUMN: 2
    PROFILES_TABLE: 2
    HAS_IMPLEMENTATION: 11
    IMPLEMENTS_METRIC: 11
    USES_TABLE: 11
    USES_COLUMN: 13
  forbidden_card_types_present: []
  parser_boundary: generic logistics reusable knowledge only
```
