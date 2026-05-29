# Ecom Express Logistics Knowledge — Parser Ready v4 Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: ecom_express_logistics_parser_ready_v4_unified_edges
  title: Ecom Express Logistics Knowledge — Parser Ready v4 Unified Edges
  domain: logistics
  vendor: Ecom Express
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style
  generated_on: '2026-05-20'
  version: 4.0-unified-edges
  scope: ecom_express_vendor_logistics_with_unified_edges
  logistics_only: true
  allowed_card_types:
  - metric
  - metric_implementation
  - platform
  - platform_context
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
  id: evidence.ecom_express.vendor_scope
  source_document: Logistics KB Doc.docx
  summary: 'Vendor-specific extracted evidence for ecom_express: table role, coverage status, metrics, caveats, and joins.'
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
  card_id: platform.ecom_express
  name: Ecom Express
  fields:
    name: Ecom Express
    description: Ecom Express logistics platform/vendor in the logistics domain.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    platform_name: Ecom Express
    platform_type: indirect_courier
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
  card_id: platform_context.ecom_express.in
  name: Ecom Express India
  fields:
    name: Ecom Express India
    description: India logistics context for Ecom Express.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    platform_id: platform.ecom_express
    context_name: Ecom Express India
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

### 4.8 metric cards

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
    - see metric_impl blocks in ecom_express_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ecom_express_logistics_parser_ready_v3_expansive.md
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
    - see metric_impl blocks in ecom_express_logistics_parser_ready_v3_expansive.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.9 metric_implementation cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount
  name: Ecom Express Freight Billed Amount Implementation
  fields:
    name: Ecom Express Freight Billed Amount Implementation
    description: Freight Billed Amount implementation for Ecom Express using shiprocket_invoice.
    status: active
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
    implementation_name: Ecom Express Freight Billed Amount
    metric_pattern: indirect_only_filtered_sum
    applicability: platform=ecom_express; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_amount
    - column.zs_observe.shiprocket_invoice.courier_partner
    semantic_filters:
    - courier_partner='Ecom Air 500gm'
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Ecom Express has no native table; evidence appears in Shiprocket invoice.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount
  name: Ecom Express COD Remitted Amount Implementation
  fields:
    name: Ecom Express COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Ecom Express using shiprocket_settlement.
    status: active
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
    implementation_name: Ecom Express COD Remitted Amount
    metric_pattern: indirect_only_filtered_sum
    applicability: platform=ecom_express; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding
      only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.charged_amount
    - column.zs_observe.shiprocket_settlement.courier_partner
    semantic_filters:
    - courier_partner='Ecom Air 500gm'
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Ecom Express has no native table; COD visible via Shiprocket settlement.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.ecom.shipment_count
  name: Ecom Express Shipment Count Implementation
  fields:
    name: Ecom Express Shipment Count Implementation
    description: Shipment Count implementation for Ecom Express using shiprocket_oms.
    status: active
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
    implementation_name: Ecom Express Shipment Count
    metric_pattern: indirect_only_filtered_count
    applicability: platform=ecom_express; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.courier_company
    semantic_filters:
    - courier_company or master_courier identifies Ecom
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only if Ecom courier values are present in Shiprocket OMS.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table
  name: Ecom Express Freight Billed Amount Implementation
  fields:
    name: Ecom Express Freight Billed Amount Implementation
    description: Freight Billed Amount implementation for Ecom Express using shiprocket_oms.
    status: active
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
    implementation_name: Ecom Express Freight Billed Amount
    metric_pattern: unsupported_indirect_only
    applicability: platform=ecom_express; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.courier_company
    semantic_filters: []
    formula_description: UNSUPPORTED_NO_NATIVE_TABLE
    formula_sql: UNSUPPORTED_NO_NATIVE_TABLE
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
    caveats: No separate Ecom Express native table exists in source KB.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table
  name: Ecom Express COD Remitted Amount Implementation
  fields:
    name: Ecom Express COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Ecom Express using shiprocket_oms.
    status: active
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
    implementation_name: Ecom Express COD Remitted Amount
    metric_pattern: unsupported_indirect_only
    applicability: platform=ecom_express; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.courier_company
    semantic_filters: []
    formula_description: UNSUPPORTED_NO_NATIVE_TABLE
    formula_sql: UNSUPPORTED_NO_NATIVE_TABLE
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
    caveats: No separate Ecom Express native table exists in source KB.
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
  edge_id: edge.platform_context.ecom_express.in.belongs_to_platform.platform.ecom_express
  edge_type: BELONGS_TO_PLATFORM
  source: platform_context.ecom_express.in
  target: platform.ecom_express
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
  edge_id: edge.platform.ecom_express.has_platform_context.platform_context.ecom_express.in
  edge_type: HAS_PLATFORM_CONTEXT
  source: platform.ecom_express
  target: platform_context.ecom_express.in
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
    materialized_from: edge.platform_context.ecom_express.in.belongs_to_platform.platform.ecom_express
```

```yaml
candidate_edge:
  edge_id: edge.metric.freight_billed_amount.has_implementation.metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_billed_amount
  target: metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount.implements_metric.metric.freight_billed_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount
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
    materialized_from: edge.metric.freight_billed_amount.has_implementation.metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount.uses_column.column.zs_observe.shiprocket_invoice.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount.uses_column.column.zs_observe.shiprocket_invoice.courier_partner.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.ecom_air.freight_billed_amount
  target: column.zs_observe.shiprocket_invoice.courier_partner
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount.uses_column.column.zs_observe.shiprocket_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount.uses_column.column.zs_observe.shiprocket_settlement.courier_partner.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.ecom_air.cod_remitted_amount
  target: column.zs_observe.shiprocket_settlement.courier_partner
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
  edge_id: edge.metric.shipment_count.has_implementation.metric_impl.shiprocket_oms.ecom.shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.shipment_count
  target: metric_impl.shiprocket_oms.ecom.shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.ecom.shipment_count.implements_metric.metric.shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.ecom.shipment_count
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
    materialized_from: edge.metric.shipment_count.has_implementation.metric_impl.shiprocket_oms.ecom.shipment_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.ecom.shipment_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.ecom.shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.ecom.shipment_count.uses_column.column.zs_observe.shiprocket_oms.courier_company.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.ecom.shipment_count
  target: column.zs_observe.shiprocket_oms.courier_company
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
  edge_id: edge.metric.freight_billed_amount.has_implementation.metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_billed_amount
  target: metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table
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
  edge_id: edge.metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table.implements_metric.metric.freight_billed_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table
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
    materialized_from: edge.metric.freight_billed_amount.has_implementation.metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table
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
  edge_id: edge.metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table.uses_column.column.zs_observe.shiprocket_oms.courier_company.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.ecom_express_native.freight_billed_amount.unsupported_no_table
  target: column.zs_observe.shiprocket_oms.courier_company
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table
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
  edge_id: edge.metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table
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
  edge_id: edge.metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table.uses_column.column.zs_observe.shiprocket_oms.courier_company.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.ecom_express_native.cod_remitted_amount.unsupported_no_table
  target: column.zs_observe.shiprocket_oms.courier_company
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

## 6. Review Items

```yaml
review_item:
  id: review.ecom_express_logistics_parser_ready_v4_unified_edges.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted
    from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```

## 7. Validation Summary

```yaml
validation_summary:
  document_id: ecom_express_logistics_parser_ready_v4_unified_edges
  candidate_cards: 10
  candidate_edges: 27
  card_types:
    metric: 3
    platform: 1
    platform_context: 1
    metric_implementation: 5
  edge_types:
    BELONGS_TO_DOMAIN: 3
    BELONGS_TO_PLATFORM: 1
    HAS_PLATFORM_CONTEXT: 1
    HAS_IMPLEMENTATION: 5
    IMPLEMENTS_METRIC: 5
    USES_TABLE: 5
    USES_COLUMN: 7
  forbidden_card_types_present: []
  parser_boundary: generic logistics reusable knowledge only
```
