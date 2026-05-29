# Logistics Domain Overview — Parser Ready v4 Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: logistics_domain_overview_parser_ready_v4_unified_edges
  title: Logistics Domain Overview — Parser Ready v4 Unified Edges
  domain: logistics
  vendor: shared_logistics
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style
  generated_on: '2026-05-20'
  version: 4.0-unified-edges
  scope: logistics_domain_overview_with_operational_process_layer_and_unified_edges
  logistics_only: true
  allowed_card_types:
  - business_process
  - column
  - domain
  - formula_template
  - metric
  - metric_dependency
  - process_variant
  - relationship
  - state_transition
  - table
  - workflow_step
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

## 3.1 Metric Implementation Coverage Index

This index is readability-only. It does not create metric implementation cards in the domain overview; it points to vendor docs that own table-specific implementations.

| metric_id | implementations | implementation docs |
|---|---|---|
| `metric.actual_weight` | 1 | shiprocket_logistics |
| `metric.average_delivery_attempts` | 1 | shiprocket_logistics |
| `metric.average_freight_per_awb` | 2 | delhivery_logistics, shiprocket_logistics |
| `metric.batch_settlement_amount` | 2 | ekart_logistics, shiprocket_logistics |
| `metric.billable_weight` | 2 | delhivery_logistics, shiprocket_logistics |
| `metric.cancelled_shipment_count` | 1 | shiprocket_logistics |
| `metric.cod_collected_amount` | 6 | delhivery_logistics, dtdc_logistics, ekart_logistics, shiprocket_logistics, xpressbees_logistics |
| `metric.cod_due_amount` | 1 | dtdc_logistics |
| `metric.cod_expected_amount` | 2 | delhivery_logistics, shiprocket_logistics |
| `metric.cod_fee_amount` | 4 | delhivery_logistics, dtdc_logistics, ekart_logistics, shiprocket_logistics |
| `metric.cod_gap_amount` | 1 | delhivery_logistics |
| `metric.cod_remittance_lag_days` | 4 | dtdc_logistics, ekart_logistics, shiprocket_logistics |
| `metric.cod_remitted_amount` | 11 | delhivery_logistics, dtdc_logistics, ecom_express_logistics, ekart_logistics, shadowfax_logistics, shiprocket_logistics, xpressbees_logistics |
| `metric.damaged_lost_shipment_count` | 1 | shiprocket_logistics |
| `metric.declared_product_value` | 4 | delhivery_logistics, ekart_logistics, shadowfax_logistics, shiprocket_logistics |
| `metric.delivered_shipment_count` | 3 | delhivery_logistics, shiprocket_logistics, xpressbees_logistics |
| `metric.delivery_success_rate` | 1 | shiprocket_logistics |
| `metric.delivery_tat_days` | 2 | dtdc_logistics, shiprocket_logistics |
| `metric.dto_freight_amount` | 1 | delhivery_logistics |
| `metric.forward_freight_amount` | 4 | delhivery_logistics, dtdc_logistics, ekart_logistics, shiprocket_logistics |
| `metric.forward_shipment_count` | 1 | shiprocket_logistics |
| `metric.fov_insurance_amount` | 1 | delhivery_logistics |
| `metric.freight_billed_amount` | 8 | delhivery_logistics, dtdc_logistics, ecom_express_logistics, ekart_logistics, shadowfax_logistics, shiprocket_logistics, xpressbees_logistics |
| `metric.freight_excluding_tax_amount` | 1 | shiprocket_logistics |
| `metric.fuel_surcharge_amount` | 2 | delhivery_logistics, shiprocket_logistics |
| `metric.gst_on_freight_amount` | 2 | delhivery_logistics, shiprocket_logistics |
| `metric.in_transit_shipment_count` | 1 | shiprocket_logistics |
| `metric.ndr_attempt_count` | 1 | shiprocket_logistics |
| `metric.order_total_amount` | 1 | shiprocket_logistics |
| `metric.payable_amount` | 1 | delhivery_logistics |
| `metric.peak_surcharge_amount` | 1 | delhivery_logistics |
| `metric.pickup_charge_amount` | 1 | delhivery_logistics |
| `metric.populated_native_record_count` | 1 | xpressbees_logistics |
| `metric.pos_settled_amount` | 1 | ekart_logistics |
| `metric.qr_cod_remitted_amount` | 1 | delhivery_logistics |
| `metric.return_shipment_count` | 2 | shadowfax_logistics, shiprocket_logistics |
| `metric.rto_count` | 2 | delhivery_logistics, shiprocket_logistics |
| `metric.rto_freight_amount` | 4 | delhivery_logistics, dtdc_logistics, ekart_logistics, shiprocket_logistics |
| `metric.rto_rate` | 1 | shiprocket_logistics |
| `metric.rto_tat_days` | 1 | shiprocket_logistics |
| `metric.settlement_batch_count` | 3 | delhivery_logistics, dtdc_logistics, ekart_logistics |
| `metric.shipment_count` | 4 | delhivery_logistics, ecom_express_logistics, shadowfax_logistics, shiprocket_logistics |
| `metric.shipment_pickup_lag_days` | 1 | shiprocket_logistics |
| `metric.sparse_native_record_count` | 1 | xpressbees_logistics |
| `metric.unique_awb_count` | 6 | delhivery_logistics, dtdc_logistics, ekart_logistics, shiprocket_logistics, xpressbees_logistics |


## 4. Candidate Cards

### 4.3 domain cards

```yaml
candidate_card:
  card_type: domain
  card_id: domain.logistics_reconciliation
  name: Logistics Reconciliation Domain
  fields:
    name: Logistics Reconciliation Domain
    description: Operational and financial logistics domain covering orders, shipments, AWBs, freight, COD, courier remittance,
      and bank bridge evidence.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    domain_name: Logistics Reconciliation
    domain_type: analytics; reconciliation; diagnostics; operations
    platform_types: marketplace; ecommerce_store; logistics; courier_aggregator; courier; marketplace_fulfilment; banking
    common_metrics:
    - metric.shipment_count
    - metric.unique_awb_count
    - metric.forward_shipment_count
    - metric.delivered_shipment_count
    - metric.rto_count
    - metric.return_shipment_count
    - metric.cancelled_shipment_count
    - metric.in_transit_shipment_count
    - metric.damaged_lost_shipment_count
    - metric.delivery_success_rate
    - metric.rto_rate
    - metric.return_rate
    - metric.ndr_attempt_count
    - metric.average_delivery_attempts
    - metric.shipment_pickup_lag_days
    - metric.delivery_tat_days
    - metric.rto_tat_days
    - metric.freight_billed_amount
    - metric.forward_freight_amount
    - metric.rto_freight_amount
    - metric.dto_freight_amount
    - metric.cod_fee_amount
    - metric.fuel_surcharge_amount
    - metric.fov_insurance_amount
    - metric.pickup_charge_amount
    - metric.peak_surcharge_amount
    - metric.gst_on_freight_amount
    - metric.freight_excluding_tax_amount
    - metric.average_freight_per_awb
    - metric.billable_weight
    - metric.actual_weight
    - metric.freight_overcharge_amount
    - metric.declared_product_value
    - metric.order_total_amount
    - metric.cod_expected_amount
    - metric.cod_collected_amount
    - metric.cod_remitted_amount
    - metric.cod_due_amount
    - metric.cod_gap_amount
    - metric.cod_remittance_lag_days
    - metric.payable_amount
    - metric.net_payment_amount
    - metric.batch_settlement_amount
    - metric.settlement_batch_count
    - metric.bank_credit_matched_amount
    - metric.unmatched_awb_count
    - metric.unmatched_bank_credit_amount
    - metric.sparse_native_record_count
    - metric.populated_native_record_count
    - metric.pos_settled_amount
    - metric.qr_cod_remitted_amount
    common_questions:
    - Which orders were not shipped?
    - Which delivered COD orders were not remitted?
    - Which AWBs are missing freight invoices?
    - Which courier batches do not match bank credits?
    - Which charges are freight, COD, product value, or batch amounts?
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    business_processes:
    - business_process.order_to_shipment_flow
    - business_process.warehouse_to_courier_handoff
    - business_process.shipment_tracking_and_delivery
    - business_process.delivery_rto_return_resolution
    - business_process.shipment_to_freight_invoice
    - business_process.freight_charge_validation
    - business_process.cod_delivery_to_courier_remittance
    - business_process.prepaid_pos_logistics_settlement
    - business_process.courier_batch_to_bank_reconciliation
```

### 4.4 table cards

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shopify_oms
  name: Shopify OMS
  fields:
    name: Shopify OMS
    description: D2C order source table used as upstream order evidence before Shiprocket logistics handoff.
    status: active
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
    table_name: shopify_oms
    full_reference: zs_observe.shopify_oms
    table_type: order_ledger
    source_platform_ids:
    - platform.shopify
    business_purpose: D2C order source for order-to-shipment reconciliation
    grain: one order row
    grain_keys:
    - order_id
    date_columns:
    - created_date
    recommended_date_columns:
    - created_date
    coverage_status: active
    row_count: '77683'
    period: Jan-Sep 2025
    group_ids: '22'
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
  card_id: column.zs_observe.shopify_oms.order_id
  name: shopify_oms.order_id
  fields:
    name: shopify_oms.order_id
    description: Shopify/D2C order identifier.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shopify_oms
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier; join_key
    business_concepts:
    - Shopify/D2C order identifier.
    default_aggregation: none
    sign_convention: not_applicable
    amount_semantics: not_applicable_or_source_specific
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.charged_amount
  name: shopify_oms.charged_amount
  fields:
    name: shopify_oms.charged_amount
    description: Order value or amount depending on source order schema.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shopify_oms
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Order value or amount depending on source order schema.
    default_aggregation: none
    sign_convention: not_applicable
    amount_semantics: not_applicable_or_source_specific
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.group_level_id
  name: shopify_oms.group_level_id
  fields:
    name: shopify_oms.group_level_id
    description: Observed group/account scope candidate; must be applied through Account Data Binding.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shopify_oms
    column_name: group_level_id
    data_type: unknown
    semantic_roles: scope_filter
    business_concepts:
    - Observed group/account scope candidate
    - must be applied through Account Data Binding.
    default_aggregation: none
    sign_convention: not_applicable
    amount_semantics: not_applicable_or_source_specific
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shopify_oms.is_active
  name: shopify_oms.is_active
  fields:
    name: shopify_oms.is_active
    description: Active row indicator when present.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    table_id: table.zs_observe.shopify_oms
    column_name: is_active
    data_type: unknown
    semantic_roles: filter
    business_concepts:
    - Active row indicator when present.
    default_aggregation: none
    sign_convention: not_applicable
    amount_semantics: not_applicable_or_source_specific
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.6 relationship cards

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shopify_oms.shiprocket_oms.parsed_order_id
  name: Shopify OMS to Shiprocket OMS Parsed Order ID
  fields:
    name: Shopify OMS to Shiprocket OMS Parsed Order ID
    description: Joins Shopify order ID to the Shopify portion of Shiprocket composite order_id before the -s suffix.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    source_table: table.zs_observe.shopify_oms
    target_table: table.zs_observe.shiprocket_oms
    relationship_type: join; reconciliation_relation
    join_keys: shopify_oms.order_id = split(shiprocket_oms.order_id, -s)[0]
    cardinality: one_to_many_possible
    join_type_recommendation: left_join
    business_use: order-to-shipment reconciliation
    safe_for_metrics: false
    safe_for_reconciliation: true
    aggregation_risk: parse and pre-aggregate by order and awb
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.8 metric cards

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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.return_rate
  name: Return Rate
  fields:
    name: Return Rate
    description: Customer return shipments divided by eligible shipments.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Return Rate
    aliases:
    - reverse return rate
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - return_rate
    domain_ids:
    - domain.logistics_reconciliation
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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.dto_freight_amount
  name: DTO Freight Amount
  fields:
    name: DTO Freight Amount
    description: Freight amount charged for DTO or dispatch-to-origin movement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: DTO Freight Amount
    aliases:
    - dispatch to origin charge
    - DTO charge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - dto_freight_amount
    domain_ids:
    - domain.logistics_reconciliation
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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.fov_insurance_amount
  name: FOV or Insurance Amount
  fields:
    name: FOV or Insurance Amount
    description: Insurance/FOV component of freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: FOV or Insurance Amount
    aliases:
    - insurance charge
    - freight on value
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - fov_insurance_amount
    domain_ids:
    - domain.logistics_reconciliation
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.pickup_charge_amount
  name: Pickup Charge Amount
  fields:
    name: Pickup Charge Amount
    description: Pickup charge component of freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Pickup Charge Amount
    aliases:
    - pickup fee
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - pickup_charge_amount
    domain_ids:
    - domain.logistics_reconciliation
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.peak_surcharge_amount
  name: Peak Surcharge Amount
  fields:
    name: Peak Surcharge Amount
    description: Peak season surcharge component of freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Peak Surcharge Amount
    aliases:
    - peak season fee
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - peak_surcharge_amount
    domain_ids:
    - domain.logistics_reconciliation
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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.freight_overcharge_amount
  name: Freight Overcharge Amount
  fields:
    name: Freight Overcharge Amount
    description: Actual freight minus expected freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Freight Overcharge Amount
    aliases:
    - freight variance
    - shipping overcharge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - freight_overcharge_amount
    domain_ids:
    - domain.logistics_reconciliation
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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_gap_amount
  name: COD Gap Amount
  fields:
    name: COD Gap Amount
    description: Difference between COD expected and COD remitted/collected.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: COD Gap Amount
    aliases:
    - COD shortfall
    - COD mismatch
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_gap_amount
    domain_ids:
    - domain.logistics_reconciliation
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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.payable_amount
  name: Payable Amount
  fields:
    name: Payable Amount
    description: Net amount payable to seller after deductions.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Payable Amount
    aliases:
    - net payable
    - courier payable
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - payable_amount
    domain_ids:
    - domain.logistics_reconciliation
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.net_payment_amount
  name: Net Payment Amount
  fields:
    name: Net Payment Amount
    description: Net payment amount in settlement record.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Net Payment Amount
    aliases:
    - net remitted
    - net settlement payment
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - net_payment_amount
    domain_ids:
    - domain.logistics_reconciliation
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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.bank_credit_matched_amount
  name: Bank Credit Matched Amount
  fields:
    name: Bank Credit Matched Amount
    description: Settlement amount matched to bank credit.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Bank Credit Matched Amount
    aliases:
    - matched bank credit
    - bank matched settlement
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - bank_credit_matched_amount
    domain_ids:
    - domain.logistics_reconciliation
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.unmatched_awb_count
  name: Unmatched AWB Count
  fields:
    name: Unmatched AWB Count
    description: Count of AWBs missing invoice or settlement evidence.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Unmatched AWB Count
    aliases:
    - AWBs without evidence
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - unmatched_awb_count
    domain_ids:
    - domain.logistics_reconciliation
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.unmatched_bank_credit_amount
  name: Unmatched Bank Credit Amount
  fields:
    name: Unmatched Bank Credit Amount
    description: Bank credit amount without matching courier settlement evidence.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Unmatched Bank Credit Amount
    aliases:
    - unidentified bank credit
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - unmatched_bank_credit_amount
    domain_ids:
    - domain.logistics_reconciliation
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.sparse_native_record_count
  name: Sparse Native Record Count
  fields:
    name: Sparse Native Record Count
    description: Count of native vendor rows missing key operational/financial fields.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Sparse Native Record Count
    aliases:
    - records with missing key fields
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - sparse_native_record_count
    domain_ids:
    - domain.logistics_reconciliation
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.populated_native_record_count
  name: Populated Native Record Count
  fields:
    name: Populated Native Record Count
    description: Count of native vendor rows with populated key fields.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: Populated Native Record Count
    aliases:
    - usable native rows
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - populated_native_record_count
    domain_ids:
    - domain.logistics_reconciliation
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
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.qr_cod_remitted_amount
  name: QR COD Remitted Amount
  fields:
    name: QR COD Remitted Amount
    description: COD remitted where payment mode indicates QR or at-door digital collection.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 3.0-expansive
    metric_name: QR COD Remitted Amount
    aliases:
    - QR based COD
    - digital COD collection
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - qr_cod_remitted_amount
    domain_ids:
    - domain.logistics_reconciliation
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.10 formula_template cards

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.logistics.filtered_count
  name: Filtered Count
  fields:
    description: Reusable count or count-distinct pattern with semantic filters.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    template_name: filtered_count
    formula_type: count
    required_inputs:
    - table
    - key_or_row
    - semantic_filter
    formula_sql_pattern: COUNT(*) or COUNT(DISTINCT key) FILTER (WHERE semantic_filter)
    denominator_handling: not_applicable
    null_handling: exclude null key only when count-distinct requires it
    output_unit_logic: count
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.logistics.filtered_sum_amount
  name: Filtered Sum Amount
  fields:
    description: Reusable sum pattern for table-specific financial amount columns.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    template_name: filtered_sum_amount
    formula_type: sum
    required_inputs:
    - amount_column
    - semantic_filter
    formula_sql_pattern: SUM(CAST(amount_column AS DOUBLE)) FILTER (WHERE semantic_filter)
    denominator_handling: not_applicable
    null_handling: treat null amount as zero only if source semantics allow
    output_unit_logic: currency
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.logistics.component_sum
  name: Component Sum
  fields:
    description: Reusable freight component summation pattern.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    template_name: component_sum
    formula_type: sum
    required_inputs:
    - component_columns
    formula_sql_pattern: SUM(component_1 + component_2 + ... + tax_component)
    denominator_handling: not_applicable
    null_handling: COALESCE nullable components to zero only after verifying component semantics
    output_unit_logic: currency
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.logistics.ratio_rate
  name: Ratio or Rate
  fields:
    description: Reusable numerator/denominator rate formula.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    template_name: ratio_rate
    formula_type: rate
    required_inputs:
    - numerator_metric
    - denominator_metric
    formula_sql_pattern: SUM(numerator) / NULLIF(SUM(denominator), 0)
    denominator_handling: NULLIF denominator to zero; return null rather than divide-by-zero
    null_handling: null denominator produces null rate
    output_unit_logic: percentage_or_ratio
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.logistics.variance_amount
  name: Variance Amount
  fields:
    description: Reusable expected vs actual amount gap formula.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    template_name: variance_amount
    formula_type: variance
    required_inputs:
    - expected_amount
    - actual_amount
    formula_sql_pattern: actual_amount - expected_amount
    denominator_handling: not_applicable
    null_handling: missing side should be classified before numeric variance
    output_unit_logic: currency
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.logistics.average_lag_days
  name: Average Lag Days
  fields:
    description: Reusable date-difference lag formula.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    template_name: average_lag_days
    formula_type: lag
    required_inputs:
    - start_date
    - end_date
    formula_sql_pattern: AVG(DATE_DIFF('day', start_date, end_date))
    denominator_handling: not_applicable
    null_handling: exclude rows missing either date and classify as incomplete for diagnostics
    output_unit_logic: days
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.logistics.batch_deduplicated_sum
  name: Batch Deduplicated Sum
  fields:
    description: Reusable pattern for settlement batch amounts repeated across AWB rows.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    template_name: batch_deduplicated_sum
    formula_type: sum
    required_inputs:
    - batch_id
    - batch_amount
    formula_sql_pattern: SUM(batch_amount) over DISTINCT batch_id or pre-aggregate one row per batch before joining
    denominator_handling: not_applicable
    null_handling: batch_id null requires review
    output_unit_logic: currency
```

### 4.11 metric_dependency cards

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.logistics.rto_rate
  name: RTO Rate Depends on RTO and Shipment Counts
  fields:
    description: RTO Rate Depends on RTO and Shipment Counts
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    parent_metric_id: metric.rto_rate
    dependent_metric_ids:
    - metric.rto_count
    - metric.shipment_count
    dependency_type: rate
    formula_template_id: formula_template.logistics.ratio_rate
    grain_alignment_required: true
    time_alignment_required: true
    scope_alignment_required: true
    missing_dependency_behavior: return null and emit review item
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.logistics.delivery_success_rate
  name: Delivery Success Rate Depends on Delivered and Shipment Counts
  fields:
    description: Delivery Success Rate Depends on Delivered and Shipment Counts
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    parent_metric_id: metric.delivery_success_rate
    dependent_metric_ids:
    - metric.delivered_shipment_count
    - metric.shipment_count
    dependency_type: rate
    formula_template_id: formula_template.logistics.ratio_rate
    grain_alignment_required: true
    time_alignment_required: true
    scope_alignment_required: true
    missing_dependency_behavior: return null and emit review item
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.logistics.average_freight_per_awb
  name: Average Freight per AWB Depends on Freight and AWB Count
  fields:
    description: Average Freight per AWB Depends on Freight and AWB Count
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    parent_metric_id: metric.average_freight_per_awb
    dependent_metric_ids:
    - metric.freight_billed_amount
    - metric.unique_awb_count
    dependency_type: average
    formula_template_id: formula_template.logistics.ratio_rate
    grain_alignment_required: true
    time_alignment_required: true
    scope_alignment_required: true
    missing_dependency_behavior: return null and emit review item
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.logistics.cod_gap_amount
  name: COD Gap Depends on Expected and Remitted COD
  fields:
    description: COD Gap Depends on Expected and Remitted COD
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    parent_metric_id: metric.cod_gap_amount
    dependent_metric_ids:
    - metric.cod_expected_amount
    - metric.cod_remitted_amount
    dependency_type: variance
    formula_template_id: formula_template.logistics.variance_amount
    grain_alignment_required: true
    time_alignment_required: true
    scope_alignment_required: true
    missing_dependency_behavior: classify missing side before computing variance
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.logistics.freight_overcharge_amount
  name: Freight Overcharge Depends on Expected and Actual Freight
  fields:
    description: Freight Overcharge Depends on Expected and Actual Freight
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    parent_metric_id: metric.freight_overcharge_amount
    dependent_metric_ids:
    - metric.expected_freight_amount
    - metric.freight_billed_amount
    dependency_type: variance
    formula_template_id: formula_template.logistics.variance_amount
    grain_alignment_required: true
    time_alignment_required: true
    scope_alignment_required: true
    missing_dependency_behavior: classify missing expected or actual freight before computing variance
```

### 4.12 business_process cards

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.order_to_shipment_flow
  name: Order to Shipment Flow
  fields:
    description: Reusable lifecycle where a channel or marketplace order becomes a logistics shipment with an AWB and courier
      assignment.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: Order to Shipment Flow
    domain_id: domain.logistics_reconciliation
    process_type: operational_workflow_and_reconciliation
    participating_platform_types: &id001
    - marketplace
    - ecommerce_store
    - logistics
    - courier_aggregator
    - courier
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - order
    - shipment
    - awb
    - courier_partner
    expected_start_state: order_confirmed
    expected_end_state: awb_assigned
    workflow_steps:
    - workflow_step.order_confirmed
    - workflow_step.shipment_created
    - workflow_step.awb_assigned
    - workflow_step.courier_assigned
    state_transitions:
    - state_transition.order_ready_for_fulfilment_to_shipment_created
    - state_transition.shipment_created_to_awb_assigned
    - state_transition.awb_assigned_to_courier_assigned
    process_variants:
    - process_variant.aggregator_routed_shiprocket
    - process_variant.platform_fulfilled_ekart
    - process_variant.direct_courier_delhivery
    common_metrics:
    - metric.shipment_count
    - metric.unique_awb_count
    - metric.shipment_missing_invoice_count
    common_failure_modes:
    - order_missing_shipment
    - shipment_without_awb
    - duplicate_shipment_for_order
    - shipment_generated_late
    reconciliation_profiles:
    - reconciliation_profile.order_to_shipment
    operational_test: A downstream system should be able to decide whether an object moved from order_confirmed to awb_assigned
      using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.warehouse_to_courier_handoff
  name: Warehouse to Courier Handoff
  fields:
    description: Reusable lifecycle for pick-pack-manifest, pickup scheduling, and courier pickup confirmation.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: Warehouse to Courier Handoff
    domain_id: domain.logistics_reconciliation
    process_type: operational_workflow
    participating_platform_types: &id001
    - ecommerce_store
    - warehouse
    - logistics
    - courier
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - shipment
    - pickup
    - manifest
    - awb
    expected_start_state: shipment_created
    expected_end_state: courier_handoff_confirmed
    workflow_steps:
    - workflow_step.shipment_manifested
    - workflow_step.pickup_scheduled
    - workflow_step.shipment_picked_up
    - workflow_step.courier_handoff_confirmed
    state_transitions:
    - state_transition.shipment_manifested_to_pickup_scheduled
    - state_transition.pickup_scheduled_to_shipment_picked_up
    - state_transition.shipment_picked_up_to_courier_handoff_confirmed
    process_variants:
    - process_variant.aggregator_routed_shiprocket
    - process_variant.marketplace_assisted_pickup
    common_metrics:
    - metric.pickup_lag_days
    - metric.shipment_count
    common_failure_modes:
    - pickup_not_scheduled
    - pickup_delayed
    - handoff_not_confirmed
    reconciliation_profiles: []
    operational_test: A downstream system should be able to decide whether an object moved from shipment_created to courier_handoff_confirmed
      using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shipment_tracking_and_delivery
  name: Shipment Tracking and Delivery
  fields:
    description: Reusable lifecycle for in-transit movement, delivery attempts, delivered status, and delivery exceptions.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: Shipment Tracking and Delivery
    domain_id: domain.logistics_reconciliation
    process_type: operational_workflow_and_analytics
    participating_platform_types: &id001
    - logistics
    - courier
    - courier_aggregator
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - shipment
    - awb
    - delivery_attempt
    - delivery_status
    expected_start_state: awb_assigned
    expected_end_state: delivery_outcome_recorded
    workflow_steps:
    - workflow_step.shipment_in_transit
    - workflow_step.delivery_attempted
    - workflow_step.shipment_delivered
    - workflow_step.delivery_exception_recorded
    state_transitions:
    - state_transition.shipment_in_transit_to_delivery_attempted
    - state_transition.delivery_attempted_to_shipment_delivered
    - state_transition.shipment_delivered_to_delivery_exception_recorded
    process_variants:
    - process_variant.reverse_only_shadowfax
    - process_variant.low_confidence_native_xpressbees
    common_metrics:
    - metric.delivered_shipment_count
    - metric.delivery_success_rate
    - metric.rto_rate
    - metric.average_delivery_attempts
    common_failure_modes:
    - delivery_delayed
    - delivery_exception
    - ndr_without_resolution
    - status_unclear
    reconciliation_profiles: []
    operational_test: A downstream system should be able to decide whether an object moved from awb_assigned to delivery_outcome_recorded
      using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.delivery_rto_return_resolution
  name: Delivery, RTO, and Return Resolution
  fields:
    description: Reusable lifecycle for non-delivery reports, return-to-origin, customer returns, reverse pickup, and QC completion.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: Delivery, RTO, and Return Resolution
    domain_id: domain.logistics_reconciliation
    process_type: operational_workflow_and_diagnostics
    participating_platform_types: &id001
    - logistics
    - courier
    - reverse_logistics
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - shipment
    - rto_event
    - return_event
    - reverse_pickup
    - qc
    expected_start_state: delivery_exception_recorded
    expected_end_state: rto_or_return_resolved
    workflow_steps:
    - workflow_step.ndr_recorded
    - workflow_step.rto_initiated
    - workflow_step.rto_delivered
    - workflow_step.reverse_qc_completed
    - workflow_step.return_delivered
    state_transitions:
    - state_transition.ndr_recorded_to_rto_initiated
    - state_transition.rto_initiated_to_rto_delivered
    - state_transition.rto_delivered_to_reverse_qc_completed
    - state_transition.reverse_qc_completed_to_return_delivered
    process_variants:
    - process_variant.reverse_only_shadowfax
    - process_variant.platform_fulfilled_ekart
    common_metrics:
    - metric.rto_count
    - metric.return_shipment_count
    - metric.rto_freight_amount
    - metric.reverse_qc_count
    common_failure_modes:
    - rto_not_recorded
    - return_not_resolved
    - reverse_qc_missing
    - unexpected_rto_charge
    reconciliation_profiles:
    - reconciliation_profile.freight_charge_validation
    operational_test: A downstream system should be able to decide whether an object moved from delivery_exception_recorded
      to rto_or_return_resolved using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.shipment_to_freight_invoice
  name: Shipment to Freight Invoice
  fields:
    description: Reusable lifecycle where a shipment/AWB receives freight invoice evidence and freight component charges.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: Shipment to Freight Invoice
    domain_id: domain.logistics_reconciliation
    process_type: reconciliation
    participating_platform_types: &id001
    - logistics
    - courier_aggregator
    - courier
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - awb
    - freight_invoice
    - freight_component
    - gst_on_freight
    expected_start_state: awb_assigned
    expected_end_state: freight_invoice_available
    workflow_steps:
    - workflow_step.awb_ready_for_billing
    - workflow_step.freight_invoice_created
    - workflow_step.freight_components_calculated
    - workflow_step.freight_tax_applied
    state_transitions:
    - state_transition.awb_ready_for_billing_to_freight_invoice_available
    - state_transition.freight_invoice_available_to_freight_components_calculated
    - state_transition.freight_components_calculated_to_freight_tax_applied
    process_variants:
    - process_variant.aggregator_routed_shiprocket
    - process_variant.direct_courier_delhivery
    - process_variant.settlement_only_dtdc
    - process_variant.indirect_only_ecom_express
    common_metrics:
    - metric.freight_billed_amount
    - metric.average_freight_per_awb
    - metric.cod_fee_amount
    - metric.gst_on_freight_amount
    common_failure_modes:
    - shipment_missing_freight_invoice
    - invoice_without_shipment
    - wrong_courier_partner
    - wrong_zone_or_weight
    reconciliation_profiles:
    - reconciliation_profile.shipment_to_freight_invoice
    operational_test: A downstream system should be able to decide whether an object moved from awb_assigned to freight_invoice_available
      using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.freight_charge_validation
  name: Freight Charge Validation
  fields:
    description: Reusable process for comparing actual freight billed against expected freight based on components, zone,
      weight, COD, RTO, DTO, and taxes.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: Freight Charge Validation
    domain_id: domain.logistics_reconciliation
    process_type: reconciliation_and_diagnostics
    participating_platform_types: &id001
    - logistics
    - courier_aggregator
    - courier
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - freight_invoice
    - freight_component
    - zone
    - weight
    - variance
    expected_start_state: expected_freight_basis_identified
    expected_end_state: freight_variance_classified
    workflow_steps:
    - workflow_step.expected_freight_basis_identified
    - workflow_step.actual_freight_extracted
    - workflow_step.component_sum_validated
    - workflow_step.freight_variance_classified
    state_transitions:
    - state_transition.expected_freight_basis_identified_to_actual_freight_extracted
    - state_transition.actual_freight_extracted_to_component_sum_validated
    - state_transition.component_sum_validated_to_freight_variance_classified
    process_variants:
    - process_variant.aggregator_routed_shiprocket
    - process_variant.direct_courier_delhivery
    common_metrics:
    - metric.freight_billed_amount
    - metric.expected_freight_amount
    - metric.freight_overcharge_amount
    - metric.freight_variance_amount
    common_failure_modes:
    - freight_overcharge
    - cod_charge_on_prepaid
    - unexpected_rto_charge
    - gst_mismatch
    reconciliation_profiles:
    - reconciliation_profile.freight_charge_validation
    operational_test: A downstream system should be able to decide whether an object moved from expected_freight_basis_identified
      to freight_variance_classified using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.cod_delivery_to_courier_remittance
  name: COD Delivery to Courier Remittance
  fields:
    description: Reusable lifecycle where delivered COD shipments are expected to produce courier or aggregator remittance
      evidence.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: COD Delivery to Courier Remittance
    domain_id: domain.logistics_reconciliation
    process_type: reconciliation
    participating_platform_types: &id001
    - ecommerce_store
    - logistics
    - courier
    - courier_aggregator
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - shipment
    - awb
    - cod_expected
    - cod_collected
    - cod_remittance
    expected_start_state: delivered_cod_shipment
    expected_end_state: cod_remittance_recorded
    workflow_steps:
    - workflow_step.cod_order_identified
    - workflow_step.cod_delivery_confirmed
    - workflow_step.cod_collected_by_courier
    - workflow_step.cod_remittance_record_created
    - workflow_step.settlement_date_or_utr_recorded
    state_transitions:
    - state_transition.cod_order_expected_to_delivered_cod_shipment
    - state_transition.delivered_cod_shipment_to_cod_collected_by_courier
    - state_transition.cod_collected_by_courier_to_cod_remittance_recorded
    - state_transition.cod_remittance_recorded_to_remittance_reference_available
    process_variants:
    - process_variant.aggregator_routed_shiprocket
    - process_variant.direct_courier_delhivery
    - process_variant.settlement_only_dtdc
    - process_variant.platform_fulfilled_ekart
    - process_variant.low_confidence_native_xpressbees
    common_metrics:
    - metric.cod_expected_amount
    - metric.cod_collected_amount
    - metric.cod_remitted_amount
    - metric.cod_gap_amount
    - metric.cod_remittance_lag_days
    common_failure_modes:
    - delivered_cod_not_remitted
    - remitted_amount_differs_from_expected_cod
    - remittance_delayed
    - missing_awb_in_settlement
    reconciliation_profiles:
    - reconciliation_profile.cod_expected_to_courier_remittance
    operational_test: A downstream system should be able to decide whether an object moved from delivered_cod_shipment to
      cod_remittance_recorded using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.prepaid_pos_logistics_settlement
  name: Prepaid or POS Logistics Settlement
  fields:
    description: Reusable lifecycle for prepaid/POS logistics or marketplace-fulfilment settlement rows, especially Ekart
      POS rows.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: Prepaid or POS Logistics Settlement
    domain_id: domain.logistics_reconciliation
    process_type: reconciliation_and_cash_flow
    participating_platform_types: &id001
    - marketplace_fulfilment
    - logistics
    - banking
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - shipment
    - pos_settlement
    - settlement_batch
    - bank_reference
    expected_start_state: prepaid_or_pos_shipment
    expected_end_state: pos_settlement_reference_recorded
    workflow_steps:
    - workflow_step.prepaid_pos_shipment_identified
    - workflow_step.pos_settlement_created
    - workflow_step.pos_batch_created
    - workflow_step.pos_bank_reference_assigned
    state_transitions:
    - state_transition.prepaid_or_pos_shipment_to_pos_settlement_created
    - state_transition.pos_settlement_created_to_pos_batch_created
    - state_transition.pos_batch_created_to_pos_settlement_reference_recorded
    process_variants:
    - process_variant.platform_fulfilled_ekart
    common_metrics:
    - metric.pos_settled_amount
    - metric.batch_settlement_amount
    - metric.bank_reference_amount
    common_failure_modes:
    - pos_settlement_missing
    - batch_reference_missing
    - bank_reference_missing
    reconciliation_profiles:
    - reconciliation_profile.prepaid_pos_settlement
    operational_test: A downstream system should be able to decide whether an object moved from prepaid_or_pos_shipment to
      pos_settlement_reference_recorded using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.courier_batch_to_bank_reconciliation
  name: Courier Batch to Bank Reconciliation
  fields:
    description: Reusable lifecycle for aggregating AWB-level remittance into settlement batches or UTRs and matching them
      to bank credits.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    process_name: Courier Batch to Bank Reconciliation
    domain_id: domain.logistics_reconciliation
    process_type: cross_domain_reconciliation
    participating_platform_types: &id001
    - logistics
    - courier
    - banking
    typical_platform_roles:
    - order_source
    - operational_evidence
    - logistics_source
    - settlement_source
    - bank_destination_when_cross_domain
    business_objects:
    - settlement_batch
    - utr
    - bank_reference
    - bank_credit
    - variance
    expected_start_state: courier_remittance_batch_created
    expected_end_state: bank_credit_matched_or_exceptioned
    workflow_steps:
    - workflow_step.remittance_batch_created
    - workflow_step.utr_or_reference_assigned
    - workflow_step.awb_amounts_aggregated
    - workflow_step.bank_credit_expected
    - workflow_step.bank_credit_matched
    state_transitions:
    - state_transition.courier_remittance_batch_created_to_utr_reference_available
    - state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch
    - state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected
    - state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned
    process_variants:
    - process_variant.logistics_to_bank_with_utr
    - process_variant.batch_without_utr_review_required
    common_metrics:
    - metric.batch_settlement_amount
    - metric.bank_credit_matched_amount
    - metric.unmatched_bank_credit_amount
    - metric.reconciliation_gap_amount
    common_failure_modes:
    - courier_settlement_batch_has_no_bank_credit
    - bank_credit_has_no_courier_detail
    - batch_amount_differs_from_awb_sum
    - missing_or_malformed_utr
    reconciliation_profiles:
    - reconciliation_profile.courier_batch_to_bank_credit
    operational_test: A downstream system should be able to decide whether an object moved from courier_remittance_batch_created
      to bank_credit_matched_or_exceptioned using evidence cards and relationships, not prose alone.
    applicability_scope:
      scope_level: platform_type
      platform_types: *id001
      notes:
      - Tenant/group-specific account participation is resolved through Business Flow Binding.
```

### 4.13 workflow_step cards

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.order_confirmed
  name: Order Confirmed
  fields:
    description: 'Evidence-bearing checkpoint in Order to Shipment Flow: Order Confirmed.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.order_to_shipment_flow
    step_order: 1
    step_name: Order Confirmed
    platform_type: marketplace; ecommerce_store; logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: order
    expected_input: order_confirmed
    expected_output: order_ready_for_fulfilment
    expected_state: order_ready_for_fulfilment
    required_evidence:
    - channel order id or marketplace order id
    failure_modes:
    - order_missing_shipment
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shipment_created
  name: Shipment Created
  fields:
    description: 'Evidence-bearing checkpoint in Order to Shipment Flow: Shipment Created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.order_to_shipment_flow
    step_order: 2
    step_name: Shipment Created
    platform_type: marketplace; ecommerce_store; logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: shipment
    expected_input: order_ready_for_fulfilment
    expected_output: shipment_created
    expected_state: shipment_created
    required_evidence:
    - table.zs_observe.shiprocket_oms
    - column.zs_observe.shiprocket_oms.order_id
    - column.zs_observe.shiprocket_oms.created_date
    failure_modes:
    - shipment_not_created
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.awb_assigned
  name: AWB Assigned
  fields:
    description: 'Evidence-bearing checkpoint in Order to Shipment Flow: AWB Assigned.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.order_to_shipment_flow
    step_order: 3
    step_name: AWB Assigned
    platform_type: marketplace; ecommerce_store; logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: awb
    expected_input: shipment_created
    expected_output: awb_assigned
    expected_state: awb_assigned
    required_evidence:
    - column.zs_observe.shiprocket_oms.awb_code
    - column.zs_observe.shiprocket_oms.awb_assigned_date
    failure_modes:
    - awb_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.courier_assigned
  name: Courier Assigned
  fields:
    description: 'Evidence-bearing checkpoint in Order to Shipment Flow: Courier Assigned.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.order_to_shipment_flow
    step_order: 4
    step_name: Courier Assigned
    platform_type: marketplace; ecommerce_store; logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: courier_partner
    expected_input: awb_assigned
    expected_output: courier_assigned
    expected_state: courier_assigned
    required_evidence:
    - column.zs_observe.shiprocket_oms.courier_company
    - column.zs_observe.shiprocket_oms.master_courier
    failure_modes:
    - courier_not_assigned
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shipment_manifested
  name: Shipment Manifested
  fields:
    description: 'Evidence-bearing checkpoint in Warehouse to Courier Handoff: Shipment Manifested.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.warehouse_to_courier_handoff
    step_order: 1
    step_name: Shipment Manifested
    platform_type: ecommerce_store; warehouse; logistics; courier
    platform_role: source_or_evidence_provider
    business_object: shipment
    expected_input: shipment_created
    expected_output: shipment_manifested
    expected_state: shipment_manifested
    required_evidence:
    - manifest or shipment created evidence
    failure_modes:
    - manifest_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.pickup_scheduled
  name: Pickup Scheduled
  fields:
    description: 'Evidence-bearing checkpoint in Warehouse to Courier Handoff: Pickup Scheduled.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.warehouse_to_courier_handoff
    step_order: 2
    step_name: Pickup Scheduled
    platform_type: ecommerce_store; warehouse; logistics; courier
    platform_role: source_or_evidence_provider
    business_object: pickup
    expected_input: shipment_manifested
    expected_output: pickup_scheduled
    expected_state: pickup_scheduled
    required_evidence:
    - column.zs_observe.shiprocket_oms.pickup_scheduled_date
    failure_modes:
    - pickup_not_scheduled
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shipment_picked_up
  name: Shipment Picked Up
  fields:
    description: 'Evidence-bearing checkpoint in Warehouse to Courier Handoff: Shipment Picked Up.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.warehouse_to_courier_handoff
    step_order: 3
    step_name: Shipment Picked Up
    platform_type: ecommerce_store; warehouse; logistics; courier
    platform_role: source_or_evidence_provider
    business_object: shipment
    expected_input: pickup_scheduled
    expected_output: shipment_picked_up
    expected_state: shipment_picked_up
    required_evidence:
    - column.zs_observe.shiprocket_oms.order_picked_up_date
    failure_modes:
    - pickup_delayed
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.courier_handoff_confirmed
  name: Courier Handoff Confirmed
  fields:
    description: 'Evidence-bearing checkpoint in Warehouse to Courier Handoff: Courier Handoff Confirmed.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.warehouse_to_courier_handoff
    step_order: 4
    step_name: Courier Handoff Confirmed
    platform_type: ecommerce_store; warehouse; logistics; courier
    platform_role: source_or_evidence_provider
    business_object: awb
    expected_input: shipment_picked_up
    expected_output: courier_handoff_confirmed
    expected_state: courier_handoff_confirmed
    required_evidence:
    - awb and pickup evidence
    failure_modes:
    - handoff_unconfirmed
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shipment_in_transit
  name: Shipment In Transit
  fields:
    description: 'Evidence-bearing checkpoint in Shipment Tracking and Delivery: Shipment In Transit.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_tracking_and_delivery
    step_order: 1
    step_name: Shipment In Transit
    platform_type: logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: shipment
    expected_input: awb_assigned
    expected_output: shipment_in_transit
    expected_state: shipment_in_transit
    required_evidence:
    - column.zs_observe.shiprocket_oms.status
    failure_modes:
    - tracking_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.delivery_attempted
  name: Delivery Attempted
  fields:
    description: 'Evidence-bearing checkpoint in Shipment Tracking and Delivery: Delivery Attempted.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_tracking_and_delivery
    step_order: 2
    step_name: Delivery Attempted
    platform_type: logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: delivery_attempt
    expected_input: shipment_in_transit
    expected_output: delivery_attempted
    expected_state: delivery_attempted
    required_evidence:
    - column.zs_observe.shiprocket_oms.attempt_count
    - column.zs_observe.shiprocket_oms.latest_ndr_date
    failure_modes:
    - attempt_not_recorded
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.shipment_delivered
  name: Shipment Delivered
  fields:
    description: 'Evidence-bearing checkpoint in Shipment Tracking and Delivery: Shipment Delivered.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_tracking_and_delivery
    step_order: 3
    step_name: Shipment Delivered
    platform_type: logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: shipment
    expected_input: delivery_attempted
    expected_output: shipment_delivered
    expected_state: shipment_delivered
    required_evidence:
    - column.zs_observe.shiprocket_oms.status
    - column.zs_observe.shiprocket_oms.order_delivered_date
    failure_modes:
    - not_delivered
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.delivery_exception_recorded
  name: Delivery Exception Recorded
  fields:
    description: 'Evidence-bearing checkpoint in Shipment Tracking and Delivery: Delivery Exception Recorded.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_tracking_and_delivery
    step_order: 4
    step_name: Delivery Exception Recorded
    platform_type: logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: delivery_exception
    expected_input: delivery_attempted
    expected_output: delivery_exception_recorded
    expected_state: delivery_exception_recorded
    required_evidence:
    - column.zs_observe.shiprocket_oms.latest_ndr_reason
    - column.zs_observe.shiprocket_oms.rto_reason
    failure_modes:
    - exception_missing_reason
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.ndr_recorded
  name: NDR Recorded
  fields:
    description: 'Evidence-bearing checkpoint in Delivery, RTO, and Return Resolution: NDR Recorded.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    step_order: 1
    step_name: NDR Recorded
    platform_type: logistics; courier; reverse_logistics
    platform_role: source_or_evidence_provider
    business_object: ndr
    expected_input: delivery_attempted
    expected_output: ndr_recorded
    expected_state: ndr_recorded
    required_evidence:
    - column.zs_observe.shiprocket_oms.latest_ndr_date
    - column.zs_observe.shiprocket_oms.latest_ndr_reason
    failure_modes:
    - ndr_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.rto_initiated
  name: RTO Initiated
  fields:
    description: 'Evidence-bearing checkpoint in Delivery, RTO, and Return Resolution: RTO Initiated.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    step_order: 2
    step_name: RTO Initiated
    platform_type: logistics; courier; reverse_logistics
    platform_role: source_or_evidence_provider
    business_object: rto_event
    expected_input: ndr_recorded
    expected_output: rto_initiated
    expected_state: rto_initiated
    required_evidence:
    - column.zs_observe.shiprocket_oms.rto_initiated_date
    failure_modes:
    - rto_not_initiated
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.rto_delivered
  name: RTO Delivered
  fields:
    description: 'Evidence-bearing checkpoint in Delivery, RTO, and Return Resolution: RTO Delivered.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    step_order: 3
    step_name: RTO Delivered
    platform_type: logistics; courier; reverse_logistics
    platform_role: source_or_evidence_provider
    business_object: rto_event
    expected_input: rto_initiated
    expected_output: rto_delivered
    expected_state: rto_delivered
    required_evidence:
    - column.zs_observe.shiprocket_oms.rto_delivered_date
    failure_modes:
    - rto_not_delivered
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.reverse_qc_completed
  name: Reverse QC Completed
  fields:
    description: 'Evidence-bearing checkpoint in Delivery, RTO, and Return Resolution: Reverse QC Completed.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    step_order: 4
    step_name: Reverse QC Completed
    platform_type: logistics; courier; reverse_logistics
    platform_role: source_or_evidence_provider
    business_object: reverse_pickup
    expected_input: return_pickup_requested
    expected_output: reverse_qc_completed
    expected_state: reverse_qc_completed
    required_evidence:
    - Shadowfax reverse QC evidence through Shiprocket courier_company
    failure_modes:
    - reverse_qc_not_confirmed
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.return_delivered
  name: Return Delivered
  fields:
    description: 'Evidence-bearing checkpoint in Delivery, RTO, and Return Resolution: Return Delivered.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    step_order: 5
    step_name: Return Delivered
    platform_type: logistics; courier; reverse_logistics
    platform_role: source_or_evidence_provider
    business_object: return_event
    expected_input: reverse_qc_completed
    expected_output: return_delivered
    expected_state: return_delivered
    required_evidence:
    - column.zs_observe.shiprocket_oms.status
    failure_modes:
    - return_not_delivered
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.awb_ready_for_billing
  name: AWB Ready for Billing
  fields:
    description: 'Evidence-bearing checkpoint in Shipment to Freight Invoice: AWB Ready for Billing.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_to_freight_invoice
    step_order: 1
    step_name: AWB Ready for Billing
    platform_type: logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: awb
    expected_input: awb_assigned
    expected_output: awb_ready_for_billing
    expected_state: awb_ready_for_billing
    required_evidence:
    - relationship.shiprocket_oms.shiprocket_invoice.awb
    failure_modes:
    - awb_not_billable
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.freight_invoice_created
  name: Freight Invoice Created
  fields:
    description: 'Evidence-bearing checkpoint in Shipment to Freight Invoice: Freight Invoice Created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_to_freight_invoice
    step_order: 2
    step_name: Freight Invoice Created
    platform_type: logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: freight_invoice
    expected_input: awb_ready_for_billing
    expected_output: freight_invoice_available
    expected_state: freight_invoice_available
    required_evidence:
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.delhivery_invoice
    failure_modes:
    - missing_freight_invoice
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.freight_components_calculated
  name: Freight Components Calculated
  fields:
    description: 'Evidence-bearing checkpoint in Shipment to Freight Invoice: Freight Components Calculated.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_to_freight_invoice
    step_order: 3
    step_name: Freight Components Calculated
    platform_type: logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: freight_component
    expected_input: freight_invoice_available
    expected_output: freight_components_calculated
    expected_state: freight_components_calculated
    required_evidence:
    - charge_dl, charge_rto, charge_cod, charge_fsc fields
    failure_modes:
    - component_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.freight_tax_applied
  name: Freight Tax Applied
  fields:
    description: 'Evidence-bearing checkpoint in Shipment to Freight Invoice: Freight Tax Applied.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_to_freight_invoice
    step_order: 4
    step_name: Freight Tax Applied
    platform_type: logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: gst_on_freight
    expected_input: freight_components_calculated
    expected_output: freight_tax_applied
    expected_state: freight_tax_applied
    required_evidence:
    - column.zs_observe.shiprocket_invoice.total_tax
    - delhivery tax fields
    failure_modes:
    - tax_missing_or_mismatched
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.expected_freight_basis_identified
  name: Expected Freight Basis Identified
  fields:
    description: 'Evidence-bearing checkpoint in Freight Charge Validation: Expected Freight Basis Identified.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.freight_charge_validation
    step_order: 1
    step_name: Expected Freight Basis Identified
    platform_type: logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: freight_rate_basis
    expected_input: freight_invoice_available
    expected_output: expected_freight_basis_identified
    expected_state: expected_freight_basis_identified
    required_evidence:
    - zone, weight, payment_mode, transaction_type
    failure_modes:
    - rate_basis_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.actual_freight_extracted
  name: Actual Freight Extracted
  fields:
    description: 'Evidence-bearing checkpoint in Freight Charge Validation: Actual Freight Extracted.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.freight_charge_validation
    step_order: 2
    step_name: Actual Freight Extracted
    platform_type: logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: freight_invoice
    expected_input: expected_freight_basis_identified
    expected_output: actual_freight_extracted
    expected_state: actual_freight_extracted
    required_evidence:
    - charged_amount or component charges in invoice table
    failure_modes:
    - actual_freight_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.component_sum_validated
  name: Component Sum Validated
  fields:
    description: 'Evidence-bearing checkpoint in Freight Charge Validation: Component Sum Validated.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.freight_charge_validation
    step_order: 3
    step_name: Component Sum Validated
    platform_type: logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: freight_component
    expected_input: actual_freight_extracted
    expected_output: component_sum_validated
    expected_state: component_sum_validated
    required_evidence:
    - component sum formula
    failure_modes:
    - component_sum_mismatch
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.freight_variance_classified
  name: Freight Variance Classified
  fields:
    description: 'Evidence-bearing checkpoint in Freight Charge Validation: Freight Variance Classified.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.freight_charge_validation
    step_order: 4
    step_name: Freight Variance Classified
    platform_type: logistics; courier_aggregator; courier
    platform_role: source_or_evidence_provider
    business_object: variance
    expected_input: component_sum_validated
    expected_output: freight_variance_classified
    expected_state: freight_variance_classified
    required_evidence:
    - mismatch categories
    failure_modes:
    - freight_variance_unclassified
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.cod_order_identified
  name: COD Order Identified
  fields:
    description: 'Evidence-bearing checkpoint in COD Delivery to Courier Remittance: COD Order Identified.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    step_order: 1
    step_name: COD Order Identified
    platform_type: ecommerce_store; logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: order
    expected_input: shipment_created
    expected_output: cod_order_expected
    expected_state: cod_order_expected
    required_evidence:
    - column.zs_observe.shiprocket_oms.payment_method
    - column.zs_observe.shiprocket_oms.cod_payble_amount
    failure_modes:
    - cod_payment_mode_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.cod_delivery_confirmed
  name: COD Delivery Confirmed
  fields:
    description: 'Evidence-bearing checkpoint in COD Delivery to Courier Remittance: COD Delivery Confirmed.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    step_order: 2
    step_name: COD Delivery Confirmed
    platform_type: ecommerce_store; logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: shipment
    expected_input: cod_order_expected
    expected_output: delivered_cod_shipment
    expected_state: delivered_cod_shipment
    required_evidence:
    - column.zs_observe.shiprocket_oms.status
    - column.zs_observe.shiprocket_oms.order_delivered_date
    failure_modes:
    - delivered_status_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.cod_collected_by_courier
  name: COD Collected by Courier
  fields:
    description: 'Evidence-bearing checkpoint in COD Delivery to Courier Remittance: COD Collected by Courier.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    step_order: 3
    step_name: COD Collected by Courier
    platform_type: ecommerce_store; logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: cod_collected
    expected_input: delivered_cod_shipment
    expected_output: cod_collected_by_courier
    expected_state: cod_collected_by_courier
    required_evidence:
    - courier settlement COD amount evidence
    failure_modes:
    - cod_collection_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.cod_remittance_record_created
  name: COD Remittance Record Created
  fields:
    description: 'Evidence-bearing checkpoint in COD Delivery to Courier Remittance: COD Remittance Record Created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    step_order: 4
    step_name: COD Remittance Record Created
    platform_type: ecommerce_store; logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: cod_remittance
    expected_input: cod_collected_by_courier
    expected_output: cod_remittance_recorded
    expected_state: cod_remittance_recorded
    required_evidence:
    - table.zs_observe.shiprocket_settlement
    - table.zs_observe.delhivery_settlement
    - table.zs_observe.dtdc_settlement
    - table.zs_observe.ekart_settlement
    - table.zs_observe.xpressbees_settlement
    failure_modes:
    - delivered_cod_not_remitted
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.settlement_date_or_utr_recorded
  name: Settlement Date or UTR Recorded
  fields:
    description: 'Evidence-bearing checkpoint in COD Delivery to Courier Remittance: Settlement Date or UTR Recorded.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    step_order: 5
    step_name: Settlement Date or UTR Recorded
    platform_type: ecommerce_store; logistics; courier; courier_aggregator
    platform_role: source_or_evidence_provider
    business_object: remittance_reference
    expected_input: cod_remittance_recorded
    expected_output: remittance_reference_available
    expected_state: remittance_reference_available
    required_evidence:
    - settlement_date, utr_no, bank_reference_no fields
    failure_modes:
    - bank_bridge_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.prepaid_pos_shipment_identified
  name: Prepaid/POS Shipment Identified
  fields:
    description: 'Evidence-bearing checkpoint in Prepaid or POS Logistics Settlement: Prepaid/POS Shipment Identified.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.prepaid_pos_logistics_settlement
    step_order: 1
    step_name: Prepaid/POS Shipment Identified
    platform_type: marketplace_fulfilment; logistics; banking
    platform_role: source_or_evidence_provider
    business_object: shipment
    expected_input: shipment_delivered
    expected_output: prepaid_or_pos_shipment
    expected_state: prepaid_or_pos_shipment
    required_evidence:
    - column.zs_observe.ekart_settlement.transaction_type
    failure_modes:
    - prepaid_pos_type_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.pos_settlement_created
  name: POS Settlement Created
  fields:
    description: 'Evidence-bearing checkpoint in Prepaid or POS Logistics Settlement: POS Settlement Created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.prepaid_pos_logistics_settlement
    step_order: 2
    step_name: POS Settlement Created
    platform_type: marketplace_fulfilment; logistics; banking
    platform_role: source_or_evidence_provider
    business_object: pos_settlement
    expected_input: prepaid_or_pos_shipment
    expected_output: pos_settlement_created
    expected_state: pos_settlement_created
    required_evidence:
    - table.zs_observe.ekart_settlement
    failure_modes:
    - pos_settlement_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.pos_batch_created
  name: POS Batch Created
  fields:
    description: 'Evidence-bearing checkpoint in Prepaid or POS Logistics Settlement: POS Batch Created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.prepaid_pos_logistics_settlement
    step_order: 3
    step_name: POS Batch Created
    platform_type: marketplace_fulfilment; logistics; banking
    platform_role: source_or_evidence_provider
    business_object: settlement_batch
    expected_input: pos_settlement_created
    expected_output: pos_batch_created
    expected_state: pos_batch_created
    required_evidence:
    - column.zs_observe.ekart_settlement.total_amount_of_batch
    - column.zs_observe.ekart_settlement.settlement_id
    failure_modes:
    - batch_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.pos_bank_reference_assigned
  name: POS Bank Reference Assigned
  fields:
    description: 'Evidence-bearing checkpoint in Prepaid or POS Logistics Settlement: POS Bank Reference Assigned.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.prepaid_pos_logistics_settlement
    step_order: 4
    step_name: POS Bank Reference Assigned
    platform_type: marketplace_fulfilment; logistics; banking
    platform_role: source_or_evidence_provider
    business_object: bank_reference
    expected_input: pos_batch_created
    expected_output: pos_settlement_reference_recorded
    expected_state: pos_settlement_reference_recorded
    required_evidence:
    - column.zs_observe.ekart_settlement.bank_reference_no
    failure_modes:
    - bank_reference_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.remittance_batch_created
  name: Remittance Batch Created
  fields:
    description: 'Evidence-bearing checkpoint in Courier Batch to Bank Reconciliation: Remittance Batch Created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    step_order: 1
    step_name: Remittance Batch Created
    platform_type: logistics; courier; banking
    platform_role: source_or_evidence_provider
    business_object: settlement_batch
    expected_input: cod_remittance_recorded
    expected_output: courier_remittance_batch_created
    expected_state: courier_remittance_batch_created
    required_evidence:
    - settlement_id, remittance_number, total_amount_of_batch
    failure_modes:
    - batch_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.utr_or_reference_assigned
  name: UTR or Bank Reference Assigned
  fields:
    description: 'Evidence-bearing checkpoint in Courier Batch to Bank Reconciliation: UTR or Bank Reference Assigned.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    step_order: 2
    step_name: UTR or Bank Reference Assigned
    platform_type: logistics; courier; banking
    platform_role: source_or_evidence_provider
    business_object: utr
    expected_input: courier_remittance_batch_created
    expected_output: utr_reference_available
    expected_state: utr_reference_available
    required_evidence:
    - utr_no, bank_reference_no, remittance_number
    failure_modes:
    - utr_missing
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.awb_amounts_aggregated
  name: AWB Amounts Aggregated
  fields:
    description: 'Evidence-bearing checkpoint in Courier Batch to Bank Reconciliation: AWB Amounts Aggregated.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    step_order: 3
    step_name: AWB Amounts Aggregated
    platform_type: logistics; courier; banking
    platform_role: source_or_evidence_provider
    business_object: settlement_batch
    expected_input: utr_reference_available
    expected_output: awb_amounts_aggregated_to_batch
    expected_state: awb_amounts_aggregated_to_batch
    required_evidence:
    - aggregate AWB-level COD by settlement/UTR
    failure_modes:
    - batch_amount_differs_from_awb_sum
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.bank_credit_expected
  name: Bank Credit Expected
  fields:
    description: 'Evidence-bearing checkpoint in Courier Batch to Bank Reconciliation: Bank Credit Expected.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    step_order: 4
    step_name: Bank Credit Expected
    platform_type: logistics; courier; banking
    platform_role: source_or_evidence_provider
    business_object: bank_credit
    expected_input: awb_amounts_aggregated_to_batch
    expected_output: bank_credit_expected
    expected_state: bank_credit_expected
    required_evidence:
    - bank bridge evidence; Business Flow Binding required for bank account
    failure_modes:
    - bank_credit_not_expected_without_bfb
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.bank_credit_matched
  name: Bank Credit Matched
  fields:
    description: 'Evidence-bearing checkpoint in Courier Batch to Bank Reconciliation: Bank Credit Matched.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    step_order: 5
    step_name: Bank Credit Matched
    platform_type: logistics; courier; banking
    platform_role: source_or_evidence_provider
    business_object: bank_credit
    expected_input: bank_credit_expected
    expected_output: bank_credit_matched_or_exceptioned
    expected_state: bank_credit_matched_or_exceptioned
    required_evidence:
    - banking KB provides bank statement evidence
    failure_modes:
    - bank_credit_missing_or_variance
    parser_use: Retrieve this step when the user asks whether this checkpoint occurred, what evidence confirms it, or why
      the next state is missing.
```

### 4.14 state_transition cards

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.order_ready_for_fulfilment_to_shipment_created
  name: order_ready_for_fulfilment to shipment_created
  fields:
    description: 'Expected state movement in Order to Shipment Flow: order_ready_for_fulfilment → shipment_created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.order_to_shipment_flow
    from_state: order_ready_for_fulfilment
    to_state: shipment_created
    triggering_step_id: workflow_step.shipment_created
    business_object: shipment
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - table.zs_observe.shiprocket_oms
    - column.zs_observe.shiprocket_oms.order_id
    - column.zs_observe.shiprocket_oms.created_date
    failure_if_missing: shipment_not_created
    severity_if_breached: medium
    deterministic_rule: If evidence for order_ready_for_fulfilment exists but confirmation evidence for shipment_created is
      missing after the applicable lag window, classify as shipment_not_created.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.shipment_created_to_awb_assigned
  name: shipment_created to awb_assigned
  fields:
    description: 'Expected state movement in Order to Shipment Flow: shipment_created → awb_assigned.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.order_to_shipment_flow
    from_state: shipment_created
    to_state: awb_assigned
    triggering_step_id: workflow_step.awb_assigned
    business_object: awb
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.awb_code
    - column.zs_observe.shiprocket_oms.awb_assigned_date
    failure_if_missing: awb_missing
    severity_if_breached: high
    deterministic_rule: If evidence for shipment_created exists but confirmation evidence for awb_assigned is missing after
      the applicable lag window, classify as awb_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.awb_assigned_to_courier_assigned
  name: awb_assigned to courier_assigned
  fields:
    description: 'Expected state movement in Order to Shipment Flow: awb_assigned → courier_assigned.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.order_to_shipment_flow
    from_state: awb_assigned
    to_state: courier_assigned
    triggering_step_id: workflow_step.courier_assigned
    business_object: courier_partner
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.courier_company
    - column.zs_observe.shiprocket_oms.master_courier
    failure_if_missing: courier_not_assigned
    severity_if_breached: medium
    deterministic_rule: If evidence for awb_assigned exists but confirmation evidence for courier_assigned is missing after
      the applicable lag window, classify as courier_not_assigned.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.shipment_manifested_to_pickup_scheduled
  name: shipment_manifested to pickup_scheduled
  fields:
    description: 'Expected state movement in Warehouse to Courier Handoff: shipment_manifested → pickup_scheduled.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.warehouse_to_courier_handoff
    from_state: shipment_manifested
    to_state: pickup_scheduled
    triggering_step_id: workflow_step.pickup_scheduled
    business_object: pickup
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.pickup_scheduled_date
    failure_if_missing: pickup_not_scheduled
    severity_if_breached: medium
    deterministic_rule: If evidence for shipment_manifested exists but confirmation evidence for pickup_scheduled is missing
      after the applicable lag window, classify as pickup_not_scheduled.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.pickup_scheduled_to_shipment_picked_up
  name: pickup_scheduled to shipment_picked_up
  fields:
    description: 'Expected state movement in Warehouse to Courier Handoff: pickup_scheduled → shipment_picked_up.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.warehouse_to_courier_handoff
    from_state: pickup_scheduled
    to_state: shipment_picked_up
    triggering_step_id: workflow_step.shipment_picked_up
    business_object: shipment
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.order_picked_up_date
    failure_if_missing: pickup_delayed
    severity_if_breached: medium
    deterministic_rule: If evidence for pickup_scheduled exists but confirmation evidence for shipment_picked_up is missing
      after the applicable lag window, classify as pickup_delayed.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.shipment_picked_up_to_courier_handoff_confirmed
  name: shipment_picked_up to courier_handoff_confirmed
  fields:
    description: 'Expected state movement in Warehouse to Courier Handoff: shipment_picked_up → courier_handoff_confirmed.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.warehouse_to_courier_handoff
    from_state: shipment_picked_up
    to_state: courier_handoff_confirmed
    triggering_step_id: workflow_step.courier_handoff_confirmed
    business_object: awb
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - awb and pickup evidence
    failure_if_missing: handoff_unconfirmed
    severity_if_breached: medium
    deterministic_rule: If evidence for shipment_picked_up exists but confirmation evidence for courier_handoff_confirmed
      is missing after the applicable lag window, classify as handoff_unconfirmed.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.shipment_in_transit_to_delivery_attempted
  name: shipment_in_transit to delivery_attempted
  fields:
    description: 'Expected state movement in Shipment Tracking and Delivery: shipment_in_transit → delivery_attempted.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_tracking_and_delivery
    from_state: shipment_in_transit
    to_state: delivery_attempted
    triggering_step_id: workflow_step.delivery_attempted
    business_object: delivery_attempt
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.attempt_count
    - column.zs_observe.shiprocket_oms.latest_ndr_date
    failure_if_missing: attempt_not_recorded
    severity_if_breached: medium
    deterministic_rule: If evidence for shipment_in_transit exists but confirmation evidence for delivery_attempted is missing
      after the applicable lag window, classify as attempt_not_recorded.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.delivery_attempted_to_shipment_delivered
  name: delivery_attempted to shipment_delivered
  fields:
    description: 'Expected state movement in Shipment Tracking and Delivery: delivery_attempted → shipment_delivered.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_tracking_and_delivery
    from_state: delivery_attempted
    to_state: shipment_delivered
    triggering_step_id: workflow_step.shipment_delivered
    business_object: shipment
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.status
    - column.zs_observe.shiprocket_oms.order_delivered_date
    failure_if_missing: not_delivered
    severity_if_breached: medium
    deterministic_rule: If evidence for delivery_attempted exists but confirmation evidence for shipment_delivered is missing
      after the applicable lag window, classify as not_delivered.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.shipment_delivered_to_delivery_exception_recorded
  name: shipment_delivered to delivery_exception_recorded
  fields:
    description: 'Expected state movement in Shipment Tracking and Delivery: shipment_delivered → delivery_exception_recorded.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_tracking_and_delivery
    from_state: shipment_delivered
    to_state: delivery_exception_recorded
    triggering_step_id: workflow_step.delivery_exception_recorded
    business_object: delivery_exception
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.latest_ndr_reason
    - column.zs_observe.shiprocket_oms.rto_reason
    failure_if_missing: exception_missing_reason
    severity_if_breached: high
    deterministic_rule: If evidence for shipment_delivered exists but confirmation evidence for delivery_exception_recorded
      is missing after the applicable lag window, classify as exception_missing_reason.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.ndr_recorded_to_rto_initiated
  name: ndr_recorded to rto_initiated
  fields:
    description: 'Expected state movement in Delivery, RTO, and Return Resolution: ndr_recorded → rto_initiated.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    from_state: ndr_recorded
    to_state: rto_initiated
    triggering_step_id: workflow_step.rto_initiated
    business_object: rto_event
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.rto_initiated_date
    failure_if_missing: rto_not_initiated
    severity_if_breached: medium
    deterministic_rule: If evidence for ndr_recorded exists but confirmation evidence for rto_initiated is missing after the
      applicable lag window, classify as rto_not_initiated.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.rto_initiated_to_rto_delivered
  name: rto_initiated to rto_delivered
  fields:
    description: 'Expected state movement in Delivery, RTO, and Return Resolution: rto_initiated → rto_delivered.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    from_state: rto_initiated
    to_state: rto_delivered
    triggering_step_id: workflow_step.rto_delivered
    business_object: rto_event
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.rto_delivered_date
    failure_if_missing: rto_not_delivered
    severity_if_breached: medium
    deterministic_rule: If evidence for rto_initiated exists but confirmation evidence for rto_delivered is missing after
      the applicable lag window, classify as rto_not_delivered.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.rto_delivered_to_reverse_qc_completed
  name: rto_delivered to reverse_qc_completed
  fields:
    description: 'Expected state movement in Delivery, RTO, and Return Resolution: rto_delivered → reverse_qc_completed.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    from_state: rto_delivered
    to_state: reverse_qc_completed
    triggering_step_id: workflow_step.reverse_qc_completed
    business_object: reverse_pickup
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - Shadowfax reverse QC evidence through Shiprocket courier_company
    failure_if_missing: reverse_qc_not_confirmed
    severity_if_breached: medium
    deterministic_rule: If evidence for rto_delivered exists but confirmation evidence for reverse_qc_completed is missing
      after the applicable lag window, classify as reverse_qc_not_confirmed.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.reverse_qc_completed_to_return_delivered
  name: reverse_qc_completed to return_delivered
  fields:
    description: 'Expected state movement in Delivery, RTO, and Return Resolution: reverse_qc_completed → return_delivered.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.delivery_rto_return_resolution
    from_state: reverse_qc_completed
    to_state: return_delivered
    triggering_step_id: workflow_step.return_delivered
    business_object: return_event
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.status
    failure_if_missing: return_not_delivered
    severity_if_breached: medium
    deterministic_rule: If evidence for reverse_qc_completed exists but confirmation evidence for return_delivered is missing
      after the applicable lag window, classify as return_not_delivered.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.awb_ready_for_billing_to_freight_invoice_available
  name: awb_ready_for_billing to freight_invoice_available
  fields:
    description: 'Expected state movement in Shipment to Freight Invoice: awb_ready_for_billing → freight_invoice_available.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_to_freight_invoice
    from_state: awb_ready_for_billing
    to_state: freight_invoice_available
    triggering_step_id: workflow_step.freight_invoice_created
    business_object: freight_invoice
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.delhivery_invoice
    failure_if_missing: missing_freight_invoice
    severity_if_breached: high
    deterministic_rule: If evidence for awb_ready_for_billing exists but confirmation evidence for freight_invoice_available
      is missing after the applicable lag window, classify as missing_freight_invoice.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.freight_invoice_available_to_freight_components_calculated
  name: freight_invoice_available to freight_components_calculated
  fields:
    description: 'Expected state movement in Shipment to Freight Invoice: freight_invoice_available → freight_components_calculated.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_to_freight_invoice
    from_state: freight_invoice_available
    to_state: freight_components_calculated
    triggering_step_id: workflow_step.freight_components_calculated
    business_object: freight_component
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - charge_dl, charge_rto, charge_cod, charge_fsc fields
    failure_if_missing: component_missing
    severity_if_breached: high
    deterministic_rule: If evidence for freight_invoice_available exists but confirmation evidence for freight_components_calculated
      is missing after the applicable lag window, classify as component_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.freight_components_calculated_to_freight_tax_applied
  name: freight_components_calculated to freight_tax_applied
  fields:
    description: 'Expected state movement in Shipment to Freight Invoice: freight_components_calculated → freight_tax_applied.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.shipment_to_freight_invoice
    from_state: freight_components_calculated
    to_state: freight_tax_applied
    triggering_step_id: workflow_step.freight_tax_applied
    business_object: gst_on_freight
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_invoice.total_tax
    - delhivery tax fields
    failure_if_missing: tax_missing_or_mismatched
    severity_if_breached: high
    deterministic_rule: If evidence for freight_components_calculated exists but confirmation evidence for freight_tax_applied
      is missing after the applicable lag window, classify as tax_missing_or_mismatched.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.expected_freight_basis_identified_to_actual_freight_extracted
  name: expected_freight_basis_identified to actual_freight_extracted
  fields:
    description: 'Expected state movement in Freight Charge Validation: expected_freight_basis_identified → actual_freight_extracted.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.freight_charge_validation
    from_state: expected_freight_basis_identified
    to_state: actual_freight_extracted
    triggering_step_id: workflow_step.actual_freight_extracted
    business_object: freight_invoice
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - charged_amount or component charges in invoice table
    failure_if_missing: actual_freight_missing
    severity_if_breached: high
    deterministic_rule: If evidence for expected_freight_basis_identified exists but confirmation evidence for actual_freight_extracted
      is missing after the applicable lag window, classify as actual_freight_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.actual_freight_extracted_to_component_sum_validated
  name: actual_freight_extracted to component_sum_validated
  fields:
    description: 'Expected state movement in Freight Charge Validation: actual_freight_extracted → component_sum_validated.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.freight_charge_validation
    from_state: actual_freight_extracted
    to_state: component_sum_validated
    triggering_step_id: workflow_step.component_sum_validated
    business_object: freight_component
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - component sum formula
    failure_if_missing: component_sum_mismatch
    severity_if_breached: medium
    deterministic_rule: If evidence for actual_freight_extracted exists but confirmation evidence for component_sum_validated
      is missing after the applicable lag window, classify as component_sum_mismatch.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.component_sum_validated_to_freight_variance_classified
  name: component_sum_validated to freight_variance_classified
  fields:
    description: 'Expected state movement in Freight Charge Validation: component_sum_validated → freight_variance_classified.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.freight_charge_validation
    from_state: component_sum_validated
    to_state: freight_variance_classified
    triggering_step_id: workflow_step.freight_variance_classified
    business_object: variance
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - mismatch categories
    failure_if_missing: freight_variance_unclassified
    severity_if_breached: medium
    deterministic_rule: If evidence for component_sum_validated exists but confirmation evidence for freight_variance_classified
      is missing after the applicable lag window, classify as freight_variance_unclassified.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.cod_order_expected_to_delivered_cod_shipment
  name: cod_order_expected to delivered_cod_shipment
  fields:
    description: 'Expected state movement in COD Delivery to Courier Remittance: cod_order_expected → delivered_cod_shipment.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    from_state: cod_order_expected
    to_state: delivered_cod_shipment
    triggering_step_id: workflow_step.cod_delivery_confirmed
    business_object: shipment
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.shiprocket_oms.status
    - column.zs_observe.shiprocket_oms.order_delivered_date
    failure_if_missing: delivered_status_missing
    severity_if_breached: high
    deterministic_rule: If evidence for cod_order_expected exists but confirmation evidence for delivered_cod_shipment is
      missing after the applicable lag window, classify as delivered_status_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.delivered_cod_shipment_to_cod_collected_by_courier
  name: delivered_cod_shipment to cod_collected_by_courier
  fields:
    description: 'Expected state movement in COD Delivery to Courier Remittance: delivered_cod_shipment → cod_collected_by_courier.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    from_state: delivered_cod_shipment
    to_state: cod_collected_by_courier
    triggering_step_id: workflow_step.cod_collected_by_courier
    business_object: cod_collected
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - courier settlement COD amount evidence
    failure_if_missing: cod_collection_missing
    severity_if_breached: high
    deterministic_rule: If evidence for delivered_cod_shipment exists but confirmation evidence for cod_collected_by_courier
      is missing after the applicable lag window, classify as cod_collection_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.cod_collected_by_courier_to_cod_remittance_recorded
  name: cod_collected_by_courier to cod_remittance_recorded
  fields:
    description: 'Expected state movement in COD Delivery to Courier Remittance: cod_collected_by_courier → cod_remittance_recorded.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    from_state: cod_collected_by_courier
    to_state: cod_remittance_recorded
    triggering_step_id: workflow_step.cod_remittance_record_created
    business_object: cod_remittance
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - table.zs_observe.shiprocket_settlement
    - table.zs_observe.delhivery_settlement
    - table.zs_observe.dtdc_settlement
    - table.zs_observe.ekart_settlement
    - table.zs_observe.xpressbees_settlement
    failure_if_missing: delivered_cod_not_remitted
    severity_if_breached: high
    deterministic_rule: If evidence for cod_collected_by_courier exists but confirmation evidence for cod_remittance_recorded
      is missing after the applicable lag window, classify as delivered_cod_not_remitted.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.cod_remittance_recorded_to_remittance_reference_available
  name: cod_remittance_recorded to remittance_reference_available
  fields:
    description: 'Expected state movement in COD Delivery to Courier Remittance: cod_remittance_recorded → remittance_reference_available.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.cod_delivery_to_courier_remittance
    from_state: cod_remittance_recorded
    to_state: remittance_reference_available
    triggering_step_id: workflow_step.settlement_date_or_utr_recorded
    business_object: remittance_reference
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - settlement_date, utr_no, bank_reference_no fields
    failure_if_missing: bank_bridge_missing
    severity_if_breached: high
    deterministic_rule: If evidence for cod_remittance_recorded exists but confirmation evidence for remittance_reference_available
      is missing after the applicable lag window, classify as bank_bridge_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.prepaid_or_pos_shipment_to_pos_settlement_created
  name: prepaid_or_pos_shipment to pos_settlement_created
  fields:
    description: 'Expected state movement in Prepaid or POS Logistics Settlement: prepaid_or_pos_shipment → pos_settlement_created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.prepaid_pos_logistics_settlement
    from_state: prepaid_or_pos_shipment
    to_state: pos_settlement_created
    triggering_step_id: workflow_step.pos_settlement_created
    business_object: pos_settlement
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - table.zs_observe.ekart_settlement
    failure_if_missing: pos_settlement_missing
    severity_if_breached: high
    deterministic_rule: If evidence for prepaid_or_pos_shipment exists but confirmation evidence for pos_settlement_created
      is missing after the applicable lag window, classify as pos_settlement_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.pos_settlement_created_to_pos_batch_created
  name: pos_settlement_created to pos_batch_created
  fields:
    description: 'Expected state movement in Prepaid or POS Logistics Settlement: pos_settlement_created → pos_batch_created.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.prepaid_pos_logistics_settlement
    from_state: pos_settlement_created
    to_state: pos_batch_created
    triggering_step_id: workflow_step.pos_batch_created
    business_object: settlement_batch
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.ekart_settlement.total_amount_of_batch
    - column.zs_observe.ekart_settlement.settlement_id
    failure_if_missing: batch_missing
    severity_if_breached: high
    deterministic_rule: If evidence for pos_settlement_created exists but confirmation evidence for pos_batch_created is missing
      after the applicable lag window, classify as batch_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.pos_batch_created_to_pos_settlement_reference_recorded
  name: pos_batch_created to pos_settlement_reference_recorded
  fields:
    description: 'Expected state movement in Prepaid or POS Logistics Settlement: pos_batch_created → pos_settlement_reference_recorded.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.prepaid_pos_logistics_settlement
    from_state: pos_batch_created
    to_state: pos_settlement_reference_recorded
    triggering_step_id: workflow_step.pos_bank_reference_assigned
    business_object: bank_reference
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - column.zs_observe.ekart_settlement.bank_reference_no
    failure_if_missing: bank_reference_missing
    severity_if_breached: high
    deterministic_rule: If evidence for pos_batch_created exists but confirmation evidence for pos_settlement_reference_recorded
      is missing after the applicable lag window, classify as bank_reference_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.courier_remittance_batch_created_to_utr_reference_available
  name: courier_remittance_batch_created to utr_reference_available
  fields:
    description: 'Expected state movement in Courier Batch to Bank Reconciliation: courier_remittance_batch_created → utr_reference_available.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    from_state: courier_remittance_batch_created
    to_state: utr_reference_available
    triggering_step_id: workflow_step.utr_or_reference_assigned
    business_object: utr
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - utr_no, bank_reference_no, remittance_number
    failure_if_missing: utr_missing
    severity_if_breached: high
    deterministic_rule: If evidence for courier_remittance_batch_created exists but confirmation evidence for utr_reference_available
      is missing after the applicable lag window, classify as utr_missing.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch
  name: utr_reference_available to awb_amounts_aggregated_to_batch
  fields:
    description: 'Expected state movement in Courier Batch to Bank Reconciliation: utr_reference_available → awb_amounts_aggregated_to_batch.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    from_state: utr_reference_available
    to_state: awb_amounts_aggregated_to_batch
    triggering_step_id: workflow_step.awb_amounts_aggregated
    business_object: settlement_batch
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - aggregate AWB-level COD by settlement/UTR
    failure_if_missing: batch_amount_differs_from_awb_sum
    severity_if_breached: medium
    deterministic_rule: If evidence for utr_reference_available exists but confirmation evidence for awb_amounts_aggregated_to_batch
      is missing after the applicable lag window, classify as batch_amount_differs_from_awb_sum.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected
  name: awb_amounts_aggregated_to_batch to bank_credit_expected
  fields:
    description: 'Expected state movement in Courier Batch to Bank Reconciliation: awb_amounts_aggregated_to_batch → bank_credit_expected.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    from_state: awb_amounts_aggregated_to_batch
    to_state: bank_credit_expected
    triggering_step_id: workflow_step.bank_credit_expected
    business_object: bank_credit
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - bank bridge evidence; Business Flow Binding required for bank account
    failure_if_missing: bank_credit_not_expected_without_bfb
    severity_if_breached: high
    deterministic_rule: If evidence for awb_amounts_aggregated_to_batch exists but confirmation evidence for bank_credit_expected
      is missing after the applicable lag window, classify as bank_credit_not_expected_without_bfb.
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned
  name: bank_credit_expected to bank_credit_matched_or_exceptioned
  fields:
    description: 'Expected state movement in Courier Batch to Bank Reconciliation: bank_credit_expected → bank_credit_matched_or_exceptioned.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    from_state: bank_credit_expected
    to_state: bank_credit_matched_or_exceptioned
    triggering_step_id: workflow_step.bank_credit_matched
    business_object: bank_credit
    expected_lag: source_specific_or_bfb_override
    lag_type: configurable
    confirmation_evidence:
    - banking KB provides bank statement evidence
    failure_if_missing: bank_credit_missing_or_variance
    severity_if_breached: high
    deterministic_rule: If evidence for bank_credit_expected exists but confirmation evidence for bank_credit_matched_or_exceptioned
      is missing after the applicable lag window, classify as bank_credit_missing_or_variance.
```

### 4.15 process_variant cards

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.aggregator_routed_shiprocket
  name: Aggregator-routed via Shiprocket
  fields:
    description: Shiprocket owns aggregator OMS, freight invoice, and COD settlement evidence while underlying courier can
      be Delhivery, DTDC, XpressBees, Ekart, Shadowfax, or Ecom.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.order_to_shipment_flow
    variant_name: Aggregator-routed via Shiprocket
    variant_condition: fulfilment_ownership_model = aggregator_routed
    affected_business_processes:
    - business_process.order_to_shipment_flow
    - business_process.shipment_to_freight_invoice
    - business_process.cod_delivery_to_courier_remittance
    variant_effect: Shiprocket owns aggregator OMS, freight invoice, and COD settlement evidence while underlying courier
      can be Delhivery, DTDC, XpressBees, Ekart, Shadowfax, or Ecom.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
```

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.platform_fulfilled_ekart
  name: Platform-fulfilled via Ekart
  fields:
    description: Ekart / Flipkart fulfilment owns warehousing and courier settlement; freight can be embedded in marketplace
      economics rather than a separate invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.order_to_shipment_flow
    variant_name: Platform-fulfilled via Ekart
    variant_condition: fulfilment_ownership_model = platform_fulfilled
    affected_business_processes:
    - business_process.order_to_shipment_flow
    - business_process.prepaid_pos_logistics_settlement
    - business_process.delivery_rto_return_resolution
    variant_effect: Ekart / Flipkart fulfilment owns warehousing and courier settlement; freight can be embedded in marketplace
      economics rather than a separate invoice.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
```

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.direct_courier_delhivery
  name: Direct courier via Delhivery
  fields:
    description: Delhivery can provide direct freight invoice and direct COD settlement evidence at AWB level.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.shipment_to_freight_invoice
    variant_name: Direct courier via Delhivery
    variant_condition: fulfilment_ownership_model = direct_courier
    affected_business_processes:
    - business_process.shipment_to_freight_invoice
    - business_process.cod_delivery_to_courier_remittance
    variant_effect: Delhivery can provide direct freight invoice and direct COD settlement evidence at AWB level.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
```

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.settlement_only_dtdc
  name: Settlement-only DTDC
  fields:
    description: DTDC native settlement exists but invoice table is empty; freight evidence should fall back to Shiprocket
      invoice only when documented.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.cod_delivery_to_courier_remittance
    variant_name: Settlement-only DTDC
    variant_condition: fulfilment_ownership_model = settlement_only
    affected_business_processes:
    - business_process.cod_delivery_to_courier_remittance
    - business_process.shipment_to_freight_invoice
    variant_effect: DTDC native settlement exists but invoice table is empty; freight evidence should fall back to Shiprocket
      invoice only when documented.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
```

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.low_confidence_native_xpressbees
  name: Low-confidence native XpressBees
  fields:
    description: Native XpressBees settlement is sparse; prefer Shiprocket fallback for reliable courier-level COD evidence
      unless validating native ingestion quality.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.shipment_tracking_and_delivery
    variant_name: Low-confidence native XpressBees
    variant_condition: fulfilment_ownership_model = low_confidence_native
    affected_business_processes:
    - business_process.shipment_tracking_and_delivery
    - business_process.cod_delivery_to_courier_remittance
    variant_effect: Native XpressBees settlement is sparse; prefer Shiprocket fallback for reliable courier-level COD evidence
      unless validating native ingestion quality.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
```

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.reverse_only_shadowfax
  name: Reverse-only Shadowfax
  fields:
    description: Shadowfax appears as reverse/QC courier through Shiprocket evidence and has no native settlement/invoice
      table.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.delivery_rto_return_resolution
    variant_name: Reverse-only Shadowfax
    variant_condition: fulfilment_ownership_model = reverse_only
    affected_business_processes:
    - business_process.delivery_rto_return_resolution
    - business_process.shipment_tracking_and_delivery
    variant_effect: Shadowfax appears as reverse/QC courier through Shiprocket evidence and has no native settlement/invoice
      table.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
```

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.indirect_only_ecom_express
  name: Indirect-only Ecom Express
  fields:
    description: Ecom Express appears through Shiprocket courier partner fields and should not be queried as a native table
      until source evidence exists.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.shipment_to_freight_invoice
    variant_name: Indirect-only Ecom Express
    variant_condition: fulfilment_ownership_model = indirect_only
    affected_business_processes:
    - business_process.shipment_to_freight_invoice
    - business_process.cod_delivery_to_courier_remittance
    variant_effect: Ecom Express appears through Shiprocket courier partner fields and should not be queried as a native table
      until source evidence exists.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
```

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.logistics_to_bank_with_utr
  name: Logistics-to-bank with UTR
  fields:
    description: Courier settlement has UTR or bank reference fields, enabling downstream bank matching when Business Flow
      Binding provides the bank account.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.courier_batch_to_bank_reconciliation
    variant_name: Logistics-to-bank with UTR
    variant_condition: bank_bridge = utr_or_bank_reference_available
    affected_business_processes:
    - business_process.courier_batch_to_bank_reconciliation
    variant_effect: Courier settlement has UTR or bank reference fields, enabling downstream bank matching when Business Flow
      Binding provides the bank account.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
```

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.batch_without_utr_review_required
  name: Batch without UTR review required
  fields:
    description: Batch amount exists but UTR or bank reference is absent or unreliable; bank matching requires review and
      broader date/amount matching.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 4.0-unified-edges
    base_business_process_id: business_process.courier_batch_to_bank_reconciliation
    variant_name: Batch without UTR review required
    variant_condition: bank_bridge = missing_or_low_confidence
    affected_business_processes:
    - business_process.courier_batch_to_bank_reconciliation
    variant_effect: Batch amount exists but UTR or bank reference is absent or unreliable; bank matching requires review and
      broader date/amount matching.
    affected_metrics:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    affected_reconciliation:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    tenant_group_boundary: This is an operating-model variant only. Tenant/group-specific route participation belongs to Business
      Flow Binding.
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
  edge_id: edge.metric.return_rate.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.return_rate
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
  edge_id: edge.metric.dto_freight_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.dto_freight_amount
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
  edge_id: edge.metric.fov_insurance_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.fov_insurance_amount
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
  edge_id: edge.metric.pickup_charge_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.pickup_charge_amount
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
  edge_id: edge.metric.peak_surcharge_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.peak_surcharge_amount
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
  edge_id: edge.metric.freight_overcharge_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.freight_overcharge_amount
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
  edge_id: edge.metric.cod_gap_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_gap_amount
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
  edge_id: edge.metric.payable_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.payable_amount
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
  edge_id: edge.metric.net_payment_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.net_payment_amount
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
  edge_id: edge.metric.bank_credit_matched_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.bank_credit_matched_amount
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
  edge_id: edge.metric.unmatched_awb_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.unmatched_awb_count
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
  edge_id: edge.metric.unmatched_bank_credit_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.unmatched_bank_credit_amount
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
  edge_id: edge.metric.sparse_native_record_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.sparse_native_record_count
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
  edge_id: edge.metric.populated_native_record_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.populated_native_record_count
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
  edge_id: edge.metric.qr_cod_remitted_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.qr_cod_remitted_amount
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
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.order_to_shipment_flow
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.order_to_shipment_flow
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.order_to_shipment_flow
```

```yaml
candidate_edge:
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.warehouse_to_courier_handoff
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.warehouse_to_courier_handoff
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.warehouse_to_courier_handoff
```

```yaml
candidate_edge:
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.shipment_tracking_and_delivery
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.shipment_tracking_and_delivery
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.shipment_tracking_and_delivery
```

```yaml
candidate_edge:
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.delivery_rto_return_resolution
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.delivery_rto_return_resolution
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.delivery_rto_return_resolution
```

```yaml
candidate_edge:
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.shipment_to_freight_invoice
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.shipment_to_freight_invoice
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.shipment_to_freight_invoice
```

```yaml
candidate_edge:
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.freight_charge_validation
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.freight_charge_validation
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.freight_charge_validation
```

```yaml
candidate_edge:
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.cod_delivery_to_courier_remittance
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.cod_delivery_to_courier_remittance
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.cod_delivery_to_courier_remittance
```

```yaml
candidate_edge:
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.prepaid_pos_logistics_settlement
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.prepaid_pos_logistics_settlement
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.prepaid_pos_logistics_settlement
```

```yaml
candidate_edge:
  edge_id: edge.domain.logistics_reconciliation.has_business_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.logistics_reconciliation
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: domain.fields.business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.courier_batch_to_bank_reconciliation
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_BUSINESS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
    materialized_from: edge.domain.logistics_reconciliation.has_business_process.business_process.courier_batch_to_bank_reconciliation
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.column.zs_observe.shopify_oms.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shopify_oms
  target: column.zs_observe.shopify_oms.order_id
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
  edge_id: edge.column.zs_observe.shopify_oms.order_id.belongs_to_table.table.zs_observe.shopify_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shopify_oms.order_id
  target: table.zs_observe.shopify_oms
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
    materialized_from: edge.table.zs_observe.shopify_oms.has_column.column.zs_observe.shopify_oms.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.column.zs_observe.shopify_oms.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shopify_oms
  target: column.zs_observe.shopify_oms.charged_amount
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
  edge_id: edge.column.zs_observe.shopify_oms.charged_amount.belongs_to_table.table.zs_observe.shopify_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shopify_oms.charged_amount
  target: table.zs_observe.shopify_oms
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
    materialized_from: edge.table.zs_observe.shopify_oms.has_column.column.zs_observe.shopify_oms.charged_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.column.zs_observe.shopify_oms.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shopify_oms
  target: column.zs_observe.shopify_oms.group_level_id
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
  edge_id: edge.column.zs_observe.shopify_oms.group_level_id.belongs_to_table.table.zs_observe.shopify_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shopify_oms.group_level_id
  target: table.zs_observe.shopify_oms
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
    materialized_from: edge.table.zs_observe.shopify_oms.has_column.column.zs_observe.shopify_oms.group_level_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_column.column.zs_observe.shopify_oms.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.shopify_oms
  target: column.zs_observe.shopify_oms.is_active
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
  edge_id: edge.column.zs_observe.shopify_oms.is_active.belongs_to_table.table.zs_observe.shopify_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shopify_oms.is_active
  target: table.zs_observe.shopify_oms
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
    materialized_from: edge.table.zs_observe.shopify_oms.has_column.column.zs_observe.shopify_oms.is_active
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shopify_oms.has_relationship.relationship.shopify_oms.shiprocket_oms.parsed_order_id
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shopify_oms
  target: relationship.shopify_oms.shiprocket_oms.parsed_order_id
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
  edge_id: edge.relationship.shopify_oms.shiprocket_oms.parsed_order_id.source_table.table.zs_observe.shopify_oms
  edge_type: SOURCE_TABLE
  source: relationship.shopify_oms.shiprocket_oms.parsed_order_id
  target: table.zs_observe.shopify_oms
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shopify_oms.shiprocket_oms.parsed_order_id
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shopify_oms.shiprocket_oms.parsed_order_id
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
  edge_id: edge.relationship.shopify_oms.shiprocket_oms.parsed_order_id.target_table.table.zs_observe.shiprocket_oms
  edge_type: TARGET_TABLE
  source: relationship.shopify_oms.shiprocket_oms.parsed_order_id
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.relationship.shopify_oms.shiprocket_oms.parsed_order_id.uses_source_column.column.zs_observe.shopify_oms.order_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shopify_oms.shiprocket_oms.parsed_order_id
  target: column.zs_observe.shopify_oms.order_id
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
  edge_id: edge.relationship.shopify_oms.shiprocket_oms.parsed_order_id.uses_target_column.column.zs_observe.shiprocket_oms.order_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shopify_oms.shiprocket_oms.parsed_order_id
  target: column.zs_observe.shiprocket_oms.order_id
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
  edge_id: edge.metric_dependency.logistics.rto_rate.parent_metric.metric.rto_rate
  edge_type: PARENT_METRIC
  source: metric_dependency.logistics.rto_rate
  target: metric.rto_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.parent_metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.rto_rate.depends_on_metric.metric.rto_count
  edge_type: DEPENDS_ON_METRIC
  source: metric.rto_rate
  target: metric.rto_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.rto_rate.uses_dependent_metric.metric.rto_count
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.rto_rate
  target: metric.rto_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.rto_rate.depends_on_metric.metric.shipment_count
  edge_type: DEPENDS_ON_METRIC
  source: metric.rto_rate
  target: metric.shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.rto_rate.uses_dependent_metric.metric.shipment_count
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.rto_rate
  target: metric.shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.rto_rate.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_dependency.logistics.rto_rate
  target: formula_template.logistics.ratio_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.delivery_success_rate.parent_metric.metric.delivery_success_rate
  edge_type: PARENT_METRIC
  source: metric_dependency.logistics.delivery_success_rate
  target: metric.delivery_success_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.parent_metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.delivery_success_rate.depends_on_metric.metric.delivered_shipment_count
  edge_type: DEPENDS_ON_METRIC
  source: metric.delivery_success_rate
  target: metric.delivered_shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.delivery_success_rate.uses_dependent_metric.metric.delivered_shipment_count
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.delivery_success_rate
  target: metric.delivered_shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.delivery_success_rate.depends_on_metric.metric.shipment_count
  edge_type: DEPENDS_ON_METRIC
  source: metric.delivery_success_rate
  target: metric.shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.delivery_success_rate.uses_dependent_metric.metric.shipment_count
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.delivery_success_rate
  target: metric.shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.delivery_success_rate.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_dependency.logistics.delivery_success_rate
  target: formula_template.logistics.ratio_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.average_freight_per_awb.parent_metric.metric.average_freight_per_awb
  edge_type: PARENT_METRIC
  source: metric_dependency.logistics.average_freight_per_awb
  target: metric.average_freight_per_awb
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.parent_metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.average_freight_per_awb.depends_on_metric.metric.freight_billed_amount
  edge_type: DEPENDS_ON_METRIC
  source: metric.average_freight_per_awb
  target: metric.freight_billed_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.average_freight_per_awb.uses_dependent_metric.metric.freight_billed_amount
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.average_freight_per_awb
  target: metric.freight_billed_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.average_freight_per_awb.depends_on_metric.metric.unique_awb_count
  edge_type: DEPENDS_ON_METRIC
  source: metric.average_freight_per_awb
  target: metric.unique_awb_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.average_freight_per_awb.uses_dependent_metric.metric.unique_awb_count
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.average_freight_per_awb
  target: metric.unique_awb_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.average_freight_per_awb.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_dependency.logistics.average_freight_per_awb
  target: formula_template.logistics.ratio_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.cod_gap_amount.parent_metric.metric.cod_gap_amount
  edge_type: PARENT_METRIC
  source: metric_dependency.logistics.cod_gap_amount
  target: metric.cod_gap_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.parent_metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.cod_gap_amount.depends_on_metric.metric.cod_expected_amount
  edge_type: DEPENDS_ON_METRIC
  source: metric.cod_gap_amount
  target: metric.cod_expected_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.cod_gap_amount.uses_dependent_metric.metric.cod_expected_amount
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.cod_gap_amount
  target: metric.cod_expected_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.cod_gap_amount.depends_on_metric.metric.cod_remitted_amount
  edge_type: DEPENDS_ON_METRIC
  source: metric.cod_gap_amount
  target: metric.cod_remitted_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.cod_gap_amount.uses_dependent_metric.metric.cod_remitted_amount
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.cod_gap_amount
  target: metric.cod_remitted_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.cod_gap_amount.uses_formula_template.formula_template.logistics.variance_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_dependency.logistics.cod_gap_amount
  target: formula_template.logistics.variance_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.freight_overcharge_amount.parent_metric.metric.freight_overcharge_amount
  edge_type: PARENT_METRIC
  source: metric_dependency.logistics.freight_overcharge_amount
  target: metric.freight_overcharge_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.parent_metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.freight_overcharge_amount.depends_on_metric.metric.freight_billed_amount
  edge_type: DEPENDS_ON_METRIC
  source: metric.freight_overcharge_amount
  target: metric.freight_billed_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.freight_overcharge_amount.uses_dependent_metric.metric.freight_billed_amount
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.logistics.freight_overcharge_amount
  target: metric.freight_billed_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.dependent_metric_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.logistics.freight_overcharge_amount.uses_formula_template.formula_template.logistics.variance_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_dependency.logistics.freight_overcharge_amount
  target: formula_template.logistics.variance_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_workflow_step.workflow_step.order_confirmed
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.order_to_shipment_flow
  target: workflow_step.order_confirmed
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.order_confirmed.belongs_to_process.business_process.order_to_shipment_flow
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.order_confirmed
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_workflow_step.workflow_step.order_confirmed
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_workflow_step.workflow_step.shipment_created
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.order_to_shipment_flow
  target: workflow_step.shipment_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.shipment_created.belongs_to_process.business_process.order_to_shipment_flow
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.shipment_created
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_workflow_step.workflow_step.shipment_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_workflow_step.workflow_step.awb_assigned
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.order_to_shipment_flow
  target: workflow_step.awb_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.awb_assigned.belongs_to_process.business_process.order_to_shipment_flow
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.awb_assigned
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_workflow_step.workflow_step.awb_assigned
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_workflow_step.workflow_step.courier_assigned
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.order_to_shipment_flow
  target: workflow_step.courier_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.courier_assigned.belongs_to_process.business_process.order_to_shipment_flow
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.courier_assigned
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_workflow_step.workflow_step.courier_assigned
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_state_transition.state_transition.order_ready_for_fulfilment_to_shipment_created
  edge_type: HAS_STATE_TRANSITION
  source: business_process.order_to_shipment_flow
  target: state_transition.order_ready_for_fulfilment_to_shipment_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.order_ready_for_fulfilment_to_shipment_created.belongs_to_process.business_process.order_to_shipment_flow
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.order_ready_for_fulfilment_to_shipment_created
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_state_transition.state_transition.order_ready_for_fulfilment_to_shipment_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_state_transition.state_transition.shipment_created_to_awb_assigned
  edge_type: HAS_STATE_TRANSITION
  source: business_process.order_to_shipment_flow
  target: state_transition.shipment_created_to_awb_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_created_to_awb_assigned.belongs_to_process.business_process.order_to_shipment_flow
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.shipment_created_to_awb_assigned
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_state_transition.state_transition.shipment_created_to_awb_assigned
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_state_transition.state_transition.awb_assigned_to_courier_assigned
  edge_type: HAS_STATE_TRANSITION
  source: business_process.order_to_shipment_flow
  target: state_transition.awb_assigned_to_courier_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.awb_assigned_to_courier_assigned.belongs_to_process.business_process.order_to_shipment_flow
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.awb_assigned_to_courier_assigned
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_state_transition.state_transition.awb_assigned_to_courier_assigned
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_process_variant.process_variant.aggregator_routed_shiprocket
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.order_to_shipment_flow
  target: process_variant.aggregator_routed_shiprocket
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.aggregator_routed_shiprocket.extends_process.business_process.order_to_shipment_flow
  edge_type: EXTENDS_PROCESS
  source: process_variant.aggregator_routed_shiprocket
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_process_variant.process_variant.aggregator_routed_shiprocket
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_process_variant.process_variant.platform_fulfilled_ekart
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.order_to_shipment_flow
  target: process_variant.platform_fulfilled_ekart
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.platform_fulfilled_ekart.extends_process.business_process.order_to_shipment_flow
  edge_type: EXTENDS_PROCESS
  source: process_variant.platform_fulfilled_ekart
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_process_variant.process_variant.platform_fulfilled_ekart
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_process_variant.process_variant.direct_courier_delhivery
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.order_to_shipment_flow
  target: process_variant.direct_courier_delhivery
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.direct_courier_delhivery.extends_process.business_process.order_to_shipment_flow
  edge_type: EXTENDS_PROCESS
  source: process_variant.direct_courier_delhivery
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_process_variant.process_variant.direct_courier_delhivery
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.uses_metric.metric.shipment_count
  edge_type: USES_METRIC
  source: business_process.order_to_shipment_flow
  target: metric.shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.uses_metric.metric.unique_awb_count
  edge_type: USES_METRIC
  source: business_process.order_to_shipment_flow
  target: metric.unique_awb_count
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_reconciliation_profile.reconciliation_profile.order_to_shipment
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.order_to_shipment_flow
  target: reconciliation_profile.order_to_shipment
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: business_process.fields.reconciliation_profiles
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.supports_process.business_process.order_to_shipment_flow
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.order_to_shipment
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_reconciliation_profile.reconciliation_profile.order_to_shipment
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.order_ready_for_fulfilment_to_shipment_created.triggered_by_step.workflow_step.shipment_created
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.order_ready_for_fulfilment_to_shipment_created
  target: workflow_step.shipment_created
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_created_to_awb_assigned.triggered_by_step.workflow_step.awb_assigned
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.shipment_created_to_awb_assigned
  target: workflow_step.awb_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.awb_assigned_to_courier_assigned.triggered_by_step.workflow_step.courier_assigned
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.awb_assigned_to_courier_assigned
  target: workflow_step.courier_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.has_workflow_step.workflow_step.shipment_manifested
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.warehouse_to_courier_handoff
  target: workflow_step.shipment_manifested
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.shipment_manifested.belongs_to_process.business_process.warehouse_to_courier_handoff
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.shipment_manifested
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.warehouse_to_courier_handoff.has_workflow_step.workflow_step.shipment_manifested
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.has_workflow_step.workflow_step.pickup_scheduled
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.warehouse_to_courier_handoff
  target: workflow_step.pickup_scheduled
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.pickup_scheduled.belongs_to_process.business_process.warehouse_to_courier_handoff
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.pickup_scheduled
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.warehouse_to_courier_handoff.has_workflow_step.workflow_step.pickup_scheduled
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.has_workflow_step.workflow_step.shipment_picked_up
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.warehouse_to_courier_handoff
  target: workflow_step.shipment_picked_up
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.shipment_picked_up.belongs_to_process.business_process.warehouse_to_courier_handoff
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.shipment_picked_up
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.warehouse_to_courier_handoff.has_workflow_step.workflow_step.shipment_picked_up
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.has_workflow_step.workflow_step.courier_handoff_confirmed
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.warehouse_to_courier_handoff
  target: workflow_step.courier_handoff_confirmed
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.courier_handoff_confirmed.belongs_to_process.business_process.warehouse_to_courier_handoff
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.courier_handoff_confirmed
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.warehouse_to_courier_handoff.has_workflow_step.workflow_step.courier_handoff_confirmed
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.has_state_transition.state_transition.shipment_manifested_to_pickup_scheduled
  edge_type: HAS_STATE_TRANSITION
  source: business_process.warehouse_to_courier_handoff
  target: state_transition.shipment_manifested_to_pickup_scheduled
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_manifested_to_pickup_scheduled.belongs_to_process.business_process.warehouse_to_courier_handoff
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.shipment_manifested_to_pickup_scheduled
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.warehouse_to_courier_handoff.has_state_transition.state_transition.shipment_manifested_to_pickup_scheduled
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.has_state_transition.state_transition.pickup_scheduled_to_shipment_picked_up
  edge_type: HAS_STATE_TRANSITION
  source: business_process.warehouse_to_courier_handoff
  target: state_transition.pickup_scheduled_to_shipment_picked_up
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.pickup_scheduled_to_shipment_picked_up.belongs_to_process.business_process.warehouse_to_courier_handoff
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.pickup_scheduled_to_shipment_picked_up
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.warehouse_to_courier_handoff.has_state_transition.state_transition.pickup_scheduled_to_shipment_picked_up
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.has_state_transition.state_transition.shipment_picked_up_to_courier_handoff_confirmed
  edge_type: HAS_STATE_TRANSITION
  source: business_process.warehouse_to_courier_handoff
  target: state_transition.shipment_picked_up_to_courier_handoff_confirmed
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_picked_up_to_courier_handoff_confirmed.belongs_to_process.business_process.warehouse_to_courier_handoff
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.shipment_picked_up_to_courier_handoff_confirmed
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.warehouse_to_courier_handoff.has_state_transition.state_transition.shipment_picked_up_to_courier_handoff_confirmed
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.has_process_variant.process_variant.aggregator_routed_shiprocket
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.warehouse_to_courier_handoff
  target: process_variant.aggregator_routed_shiprocket
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.aggregator_routed_shiprocket.extends_process.business_process.warehouse_to_courier_handoff
  edge_type: EXTENDS_PROCESS
  source: process_variant.aggregator_routed_shiprocket
  target: business_process.warehouse_to_courier_handoff
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.warehouse_to_courier_handoff.has_process_variant.process_variant.aggregator_routed_shiprocket
```

```yaml
candidate_edge:
  edge_id: edge.business_process.warehouse_to_courier_handoff.uses_metric.metric.shipment_count
  edge_type: USES_METRIC
  source: business_process.warehouse_to_courier_handoff
  target: metric.shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_manifested_to_pickup_scheduled.triggered_by_step.workflow_step.pickup_scheduled
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.shipment_manifested_to_pickup_scheduled
  target: workflow_step.pickup_scheduled
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.pickup_scheduled_to_shipment_picked_up.triggered_by_step.workflow_step.shipment_picked_up
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.pickup_scheduled_to_shipment_picked_up
  target: workflow_step.shipment_picked_up
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_picked_up_to_courier_handoff_confirmed.triggered_by_step.workflow_step.courier_handoff_confirmed
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.shipment_picked_up_to_courier_handoff_confirmed
  target: workflow_step.courier_handoff_confirmed
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_workflow_step.workflow_step.shipment_in_transit
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.shipment_tracking_and_delivery
  target: workflow_step.shipment_in_transit
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.shipment_in_transit.belongs_to_process.business_process.shipment_tracking_and_delivery
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.shipment_in_transit
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_workflow_step.workflow_step.shipment_in_transit
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_workflow_step.workflow_step.delivery_attempted
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.shipment_tracking_and_delivery
  target: workflow_step.delivery_attempted
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.delivery_attempted.belongs_to_process.business_process.shipment_tracking_and_delivery
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.delivery_attempted
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_workflow_step.workflow_step.delivery_attempted
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_workflow_step.workflow_step.shipment_delivered
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.shipment_tracking_and_delivery
  target: workflow_step.shipment_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.shipment_delivered.belongs_to_process.business_process.shipment_tracking_and_delivery
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.shipment_delivered
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_workflow_step.workflow_step.shipment_delivered
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_workflow_step.workflow_step.delivery_exception_recorded
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.shipment_tracking_and_delivery
  target: workflow_step.delivery_exception_recorded
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.delivery_exception_recorded.belongs_to_process.business_process.shipment_tracking_and_delivery
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.delivery_exception_recorded
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_workflow_step.workflow_step.delivery_exception_recorded
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_state_transition.state_transition.shipment_in_transit_to_delivery_attempted
  edge_type: HAS_STATE_TRANSITION
  source: business_process.shipment_tracking_and_delivery
  target: state_transition.shipment_in_transit_to_delivery_attempted
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_in_transit_to_delivery_attempted.belongs_to_process.business_process.shipment_tracking_and_delivery
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.shipment_in_transit_to_delivery_attempted
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_state_transition.state_transition.shipment_in_transit_to_delivery_attempted
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_state_transition.state_transition.delivery_attempted_to_shipment_delivered
  edge_type: HAS_STATE_TRANSITION
  source: business_process.shipment_tracking_and_delivery
  target: state_transition.delivery_attempted_to_shipment_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.delivery_attempted_to_shipment_delivered.belongs_to_process.business_process.shipment_tracking_and_delivery
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.delivery_attempted_to_shipment_delivered
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_state_transition.state_transition.delivery_attempted_to_shipment_delivered
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_state_transition.state_transition.shipment_delivered_to_delivery_exception_recorded
  edge_type: HAS_STATE_TRANSITION
  source: business_process.shipment_tracking_and_delivery
  target: state_transition.shipment_delivered_to_delivery_exception_recorded
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_delivered_to_delivery_exception_recorded.belongs_to_process.business_process.shipment_tracking_and_delivery
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.shipment_delivered_to_delivery_exception_recorded
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_state_transition.state_transition.shipment_delivered_to_delivery_exception_recorded
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_process_variant.process_variant.reverse_only_shadowfax
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.shipment_tracking_and_delivery
  target: process_variant.reverse_only_shadowfax
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.reverse_only_shadowfax.extends_process.business_process.shipment_tracking_and_delivery
  edge_type: EXTENDS_PROCESS
  source: process_variant.reverse_only_shadowfax
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_process_variant.process_variant.reverse_only_shadowfax
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.has_process_variant.process_variant.low_confidence_native_xpressbees
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.shipment_tracking_and_delivery
  target: process_variant.low_confidence_native_xpressbees
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.low_confidence_native_xpressbees.extends_process.business_process.shipment_tracking_and_delivery
  edge_type: EXTENDS_PROCESS
  source: process_variant.low_confidence_native_xpressbees
  target: business_process.shipment_tracking_and_delivery
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.shipment_tracking_and_delivery.has_process_variant.process_variant.low_confidence_native_xpressbees
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.uses_metric.metric.delivered_shipment_count
  edge_type: USES_METRIC
  source: business_process.shipment_tracking_and_delivery
  target: metric.delivered_shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.uses_metric.metric.delivery_success_rate
  edge_type: USES_METRIC
  source: business_process.shipment_tracking_and_delivery
  target: metric.delivery_success_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.uses_metric.metric.rto_rate
  edge_type: USES_METRIC
  source: business_process.shipment_tracking_and_delivery
  target: metric.rto_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_tracking_and_delivery.uses_metric.metric.average_delivery_attempts
  edge_type: USES_METRIC
  source: business_process.shipment_tracking_and_delivery
  target: metric.average_delivery_attempts
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_in_transit_to_delivery_attempted.triggered_by_step.workflow_step.delivery_attempted
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.shipment_in_transit_to_delivery_attempted
  target: workflow_step.delivery_attempted
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.delivery_attempted_to_shipment_delivered.triggered_by_step.workflow_step.shipment_delivered
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.delivery_attempted_to_shipment_delivered
  target: workflow_step.shipment_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.shipment_delivered_to_delivery_exception_recorded.triggered_by_step.workflow_step.delivery_exception_recorded
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.shipment_delivered_to_delivery_exception_recorded
  target: workflow_step.delivery_exception_recorded
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.ndr_recorded
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.delivery_rto_return_resolution
  target: workflow_step.ndr_recorded
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.ndr_recorded.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.ndr_recorded
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.ndr_recorded
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.rto_initiated
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.delivery_rto_return_resolution
  target: workflow_step.rto_initiated
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.rto_initiated.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.rto_initiated
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.rto_initiated
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.rto_delivered
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.delivery_rto_return_resolution
  target: workflow_step.rto_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.rto_delivered.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.rto_delivered
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.rto_delivered
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.reverse_qc_completed
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.delivery_rto_return_resolution
  target: workflow_step.reverse_qc_completed
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.reverse_qc_completed.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.reverse_qc_completed
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.reverse_qc_completed
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.return_delivered
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.delivery_rto_return_resolution
  target: workflow_step.return_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.return_delivered.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.return_delivered
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_workflow_step.workflow_step.return_delivered
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_state_transition.state_transition.ndr_recorded_to_rto_initiated
  edge_type: HAS_STATE_TRANSITION
  source: business_process.delivery_rto_return_resolution
  target: state_transition.ndr_recorded_to_rto_initiated
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.ndr_recorded_to_rto_initiated.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.ndr_recorded_to_rto_initiated
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_state_transition.state_transition.ndr_recorded_to_rto_initiated
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_state_transition.state_transition.rto_initiated_to_rto_delivered
  edge_type: HAS_STATE_TRANSITION
  source: business_process.delivery_rto_return_resolution
  target: state_transition.rto_initiated_to_rto_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.rto_initiated_to_rto_delivered.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.rto_initiated_to_rto_delivered
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_state_transition.state_transition.rto_initiated_to_rto_delivered
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_state_transition.state_transition.rto_delivered_to_reverse_qc_completed
  edge_type: HAS_STATE_TRANSITION
  source: business_process.delivery_rto_return_resolution
  target: state_transition.rto_delivered_to_reverse_qc_completed
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.rto_delivered_to_reverse_qc_completed.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.rto_delivered_to_reverse_qc_completed
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_state_transition.state_transition.rto_delivered_to_reverse_qc_completed
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_state_transition.state_transition.reverse_qc_completed_to_return_delivered
  edge_type: HAS_STATE_TRANSITION
  source: business_process.delivery_rto_return_resolution
  target: state_transition.reverse_qc_completed_to_return_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.reverse_qc_completed_to_return_delivered.belongs_to_process.business_process.delivery_rto_return_resolution
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.reverse_qc_completed_to_return_delivered
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_state_transition.state_transition.reverse_qc_completed_to_return_delivered
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_process_variant.process_variant.reverse_only_shadowfax
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.delivery_rto_return_resolution
  target: process_variant.reverse_only_shadowfax
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.reverse_only_shadowfax.extends_process.business_process.delivery_rto_return_resolution
  edge_type: EXTENDS_PROCESS
  source: process_variant.reverse_only_shadowfax
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_process_variant.process_variant.reverse_only_shadowfax
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_process_variant.process_variant.platform_fulfilled_ekart
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.delivery_rto_return_resolution
  target: process_variant.platform_fulfilled_ekart
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.platform_fulfilled_ekart.extends_process.business_process.delivery_rto_return_resolution
  edge_type: EXTENDS_PROCESS
  source: process_variant.platform_fulfilled_ekart
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_process_variant.process_variant.platform_fulfilled_ekart
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.uses_metric.metric.rto_count
  edge_type: USES_METRIC
  source: business_process.delivery_rto_return_resolution
  target: metric.rto_count
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.uses_metric.metric.return_shipment_count
  edge_type: USES_METRIC
  source: business_process.delivery_rto_return_resolution
  target: metric.return_shipment_count
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.uses_metric.metric.rto_freight_amount
  edge_type: USES_METRIC
  source: business_process.delivery_rto_return_resolution
  target: metric.rto_freight_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.delivery_rto_return_resolution.has_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.delivery_rto_return_resolution
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: business_process.fields.reconciliation_profiles
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.supports_process.business_process.delivery_rto_return_resolution
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.freight_charge_validation
  target: business_process.delivery_rto_return_resolution
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.delivery_rto_return_resolution.has_reconciliation_profile.reconciliation_profile.freight_charge_validation
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.ndr_recorded_to_rto_initiated.triggered_by_step.workflow_step.rto_initiated
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.ndr_recorded_to_rto_initiated
  target: workflow_step.rto_initiated
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.rto_initiated_to_rto_delivered.triggered_by_step.workflow_step.rto_delivered
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.rto_initiated_to_rto_delivered
  target: workflow_step.rto_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.rto_delivered_to_reverse_qc_completed.triggered_by_step.workflow_step.reverse_qc_completed
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.rto_delivered_to_reverse_qc_completed
  target: workflow_step.reverse_qc_completed
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.reverse_qc_completed_to_return_delivered.triggered_by_step.workflow_step.return_delivered
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.reverse_qc_completed_to_return_delivered
  target: workflow_step.return_delivered
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_workflow_step.workflow_step.awb_ready_for_billing
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.shipment_to_freight_invoice
  target: workflow_step.awb_ready_for_billing
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.awb_ready_for_billing.belongs_to_process.business_process.shipment_to_freight_invoice
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.awb_ready_for_billing
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_workflow_step.workflow_step.awb_ready_for_billing
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_workflow_step.workflow_step.freight_invoice_created
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.shipment_to_freight_invoice
  target: workflow_step.freight_invoice_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.freight_invoice_created.belongs_to_process.business_process.shipment_to_freight_invoice
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.freight_invoice_created
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_workflow_step.workflow_step.freight_invoice_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_workflow_step.workflow_step.freight_components_calculated
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.shipment_to_freight_invoice
  target: workflow_step.freight_components_calculated
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.freight_components_calculated.belongs_to_process.business_process.shipment_to_freight_invoice
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.freight_components_calculated
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_workflow_step.workflow_step.freight_components_calculated
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_workflow_step.workflow_step.freight_tax_applied
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.shipment_to_freight_invoice
  target: workflow_step.freight_tax_applied
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.freight_tax_applied.belongs_to_process.business_process.shipment_to_freight_invoice
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.freight_tax_applied
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_workflow_step.workflow_step.freight_tax_applied
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_state_transition.state_transition.awb_ready_for_billing_to_freight_invoice_available
  edge_type: HAS_STATE_TRANSITION
  source: business_process.shipment_to_freight_invoice
  target: state_transition.awb_ready_for_billing_to_freight_invoice_available
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.awb_ready_for_billing_to_freight_invoice_available.belongs_to_process.business_process.shipment_to_freight_invoice
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.awb_ready_for_billing_to_freight_invoice_available
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_state_transition.state_transition.awb_ready_for_billing_to_freight_invoice_available
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_state_transition.state_transition.freight_invoice_available_to_freight_components_calculated
  edge_type: HAS_STATE_TRANSITION
  source: business_process.shipment_to_freight_invoice
  target: state_transition.freight_invoice_available_to_freight_components_calculated
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.freight_invoice_available_to_freight_components_calculated.belongs_to_process.business_process.shipment_to_freight_invoice
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.freight_invoice_available_to_freight_components_calculated
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_state_transition.state_transition.freight_invoice_available_to_freight_components_calculated
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_state_transition.state_transition.freight_components_calculated_to_freight_tax_applied
  edge_type: HAS_STATE_TRANSITION
  source: business_process.shipment_to_freight_invoice
  target: state_transition.freight_components_calculated_to_freight_tax_applied
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.freight_components_calculated_to_freight_tax_applied.belongs_to_process.business_process.shipment_to_freight_invoice
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.freight_components_calculated_to_freight_tax_applied
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_state_transition.state_transition.freight_components_calculated_to_freight_tax_applied
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_process_variant.process_variant.aggregator_routed_shiprocket
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.shipment_to_freight_invoice
  target: process_variant.aggregator_routed_shiprocket
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.aggregator_routed_shiprocket.extends_process.business_process.shipment_to_freight_invoice
  edge_type: EXTENDS_PROCESS
  source: process_variant.aggregator_routed_shiprocket
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_process_variant.process_variant.aggregator_routed_shiprocket
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_process_variant.process_variant.direct_courier_delhivery
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.shipment_to_freight_invoice
  target: process_variant.direct_courier_delhivery
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.direct_courier_delhivery.extends_process.business_process.shipment_to_freight_invoice
  edge_type: EXTENDS_PROCESS
  source: process_variant.direct_courier_delhivery
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_process_variant.process_variant.direct_courier_delhivery
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_process_variant.process_variant.settlement_only_dtdc
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.shipment_to_freight_invoice
  target: process_variant.settlement_only_dtdc
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.settlement_only_dtdc.extends_process.business_process.shipment_to_freight_invoice
  edge_type: EXTENDS_PROCESS
  source: process_variant.settlement_only_dtdc
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_process_variant.process_variant.settlement_only_dtdc
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_process_variant.process_variant.indirect_only_ecom_express
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.shipment_to_freight_invoice
  target: process_variant.indirect_only_ecom_express
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.indirect_only_ecom_express.extends_process.business_process.shipment_to_freight_invoice
  edge_type: EXTENDS_PROCESS
  source: process_variant.indirect_only_ecom_express
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_process_variant.process_variant.indirect_only_ecom_express
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.uses_metric.metric.freight_billed_amount
  edge_type: USES_METRIC
  source: business_process.shipment_to_freight_invoice
  target: metric.freight_billed_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.uses_metric.metric.average_freight_per_awb
  edge_type: USES_METRIC
  source: business_process.shipment_to_freight_invoice
  target: metric.average_freight_per_awb
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.uses_metric.metric.cod_fee_amount
  edge_type: USES_METRIC
  source: business_process.shipment_to_freight_invoice
  target: metric.cod_fee_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.uses_metric.metric.gst_on_freight_amount
  edge_type: USES_METRIC
  source: business_process.shipment_to_freight_invoice
  target: metric.gst_on_freight_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.shipment_to_freight_invoice
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: business_process.fields.reconciliation_profiles
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.supports_process.business_process.shipment_to_freight_invoice
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.shipment_to_freight_invoice
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.awb_ready_for_billing_to_freight_invoice_available.triggered_by_step.workflow_step.freight_invoice_created
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.awb_ready_for_billing_to_freight_invoice_available
  target: workflow_step.freight_invoice_created
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.freight_invoice_available_to_freight_components_calculated.triggered_by_step.workflow_step.freight_components_calculated
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.freight_invoice_available_to_freight_components_calculated
  target: workflow_step.freight_components_calculated
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.freight_components_calculated_to_freight_tax_applied.triggered_by_step.workflow_step.freight_tax_applied
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.freight_components_calculated_to_freight_tax_applied
  target: workflow_step.freight_tax_applied
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_workflow_step.workflow_step.expected_freight_basis_identified
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.freight_charge_validation
  target: workflow_step.expected_freight_basis_identified
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.expected_freight_basis_identified.belongs_to_process.business_process.freight_charge_validation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.expected_freight_basis_identified
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_workflow_step.workflow_step.expected_freight_basis_identified
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_workflow_step.workflow_step.actual_freight_extracted
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.freight_charge_validation
  target: workflow_step.actual_freight_extracted
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.actual_freight_extracted.belongs_to_process.business_process.freight_charge_validation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.actual_freight_extracted
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_workflow_step.workflow_step.actual_freight_extracted
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_workflow_step.workflow_step.component_sum_validated
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.freight_charge_validation
  target: workflow_step.component_sum_validated
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.component_sum_validated.belongs_to_process.business_process.freight_charge_validation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.component_sum_validated
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_workflow_step.workflow_step.component_sum_validated
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_workflow_step.workflow_step.freight_variance_classified
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.freight_charge_validation
  target: workflow_step.freight_variance_classified
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.freight_variance_classified.belongs_to_process.business_process.freight_charge_validation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.freight_variance_classified
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_workflow_step.workflow_step.freight_variance_classified
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_state_transition.state_transition.expected_freight_basis_identified_to_actual_freight_extracted
  edge_type: HAS_STATE_TRANSITION
  source: business_process.freight_charge_validation
  target: state_transition.expected_freight_basis_identified_to_actual_freight_extracted
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.expected_freight_basis_identified_to_actual_freight_extracted.belongs_to_process.business_process.freight_charge_validation
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.expected_freight_basis_identified_to_actual_freight_extracted
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_state_transition.state_transition.expected_freight_basis_identified_to_actual_freight_extracted
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_state_transition.state_transition.actual_freight_extracted_to_component_sum_validated
  edge_type: HAS_STATE_TRANSITION
  source: business_process.freight_charge_validation
  target: state_transition.actual_freight_extracted_to_component_sum_validated
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.actual_freight_extracted_to_component_sum_validated.belongs_to_process.business_process.freight_charge_validation
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.actual_freight_extracted_to_component_sum_validated
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_state_transition.state_transition.actual_freight_extracted_to_component_sum_validated
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_state_transition.state_transition.component_sum_validated_to_freight_variance_classified
  edge_type: HAS_STATE_TRANSITION
  source: business_process.freight_charge_validation
  target: state_transition.component_sum_validated_to_freight_variance_classified
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.component_sum_validated_to_freight_variance_classified.belongs_to_process.business_process.freight_charge_validation
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.component_sum_validated_to_freight_variance_classified
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_state_transition.state_transition.component_sum_validated_to_freight_variance_classified
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_process_variant.process_variant.aggregator_routed_shiprocket
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.freight_charge_validation
  target: process_variant.aggregator_routed_shiprocket
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.aggregator_routed_shiprocket.extends_process.business_process.freight_charge_validation
  edge_type: EXTENDS_PROCESS
  source: process_variant.aggregator_routed_shiprocket
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_process_variant.process_variant.aggregator_routed_shiprocket
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_process_variant.process_variant.direct_courier_delhivery
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.freight_charge_validation
  target: process_variant.direct_courier_delhivery
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.direct_courier_delhivery.extends_process.business_process.freight_charge_validation
  edge_type: EXTENDS_PROCESS
  source: process_variant.direct_courier_delhivery
  target: business_process.freight_charge_validation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_process_variant.process_variant.direct_courier_delhivery
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.uses_metric.metric.freight_billed_amount
  edge_type: USES_METRIC
  source: business_process.freight_charge_validation
  target: metric.freight_billed_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.uses_metric.metric.freight_overcharge_amount
  edge_type: USES_METRIC
  source: business_process.freight_charge_validation
  target: metric.freight_overcharge_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.freight_charge_validation
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: business_process.fields.reconciliation_profiles
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.supports_process.business_process.freight_charge_validation
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.freight_charge_validation
  target: business_process.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_reconciliation_profile.reconciliation_profile.freight_charge_validation
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.expected_freight_basis_identified_to_actual_freight_extracted.triggered_by_step.workflow_step.actual_freight_extracted
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.expected_freight_basis_identified_to_actual_freight_extracted
  target: workflow_step.actual_freight_extracted
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.actual_freight_extracted_to_component_sum_validated.triggered_by_step.workflow_step.component_sum_validated
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.actual_freight_extracted_to_component_sum_validated
  target: workflow_step.component_sum_validated
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.component_sum_validated_to_freight_variance_classified.triggered_by_step.workflow_step.freight_variance_classified
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.component_sum_validated_to_freight_variance_classified
  target: workflow_step.freight_variance_classified
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.cod_order_identified
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.cod_delivery_to_courier_remittance
  target: workflow_step.cod_order_identified
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.cod_order_identified.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.cod_order_identified
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.cod_order_identified
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.cod_delivery_confirmed
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.cod_delivery_to_courier_remittance
  target: workflow_step.cod_delivery_confirmed
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.cod_delivery_confirmed.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.cod_delivery_confirmed
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.cod_delivery_confirmed
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.cod_collected_by_courier
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.cod_delivery_to_courier_remittance
  target: workflow_step.cod_collected_by_courier
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.cod_collected_by_courier.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.cod_collected_by_courier
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.cod_collected_by_courier
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.cod_remittance_record_created
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.cod_delivery_to_courier_remittance
  target: workflow_step.cod_remittance_record_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.cod_remittance_record_created.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.cod_remittance_record_created
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.cod_remittance_record_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.settlement_date_or_utr_recorded
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.cod_delivery_to_courier_remittance
  target: workflow_step.settlement_date_or_utr_recorded
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.settlement_date_or_utr_recorded.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.settlement_date_or_utr_recorded
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_workflow_step.workflow_step.settlement_date_or_utr_recorded
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_state_transition.state_transition.cod_order_expected_to_delivered_cod_shipment
  edge_type: HAS_STATE_TRANSITION
  source: business_process.cod_delivery_to_courier_remittance
  target: state_transition.cod_order_expected_to_delivered_cod_shipment
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.cod_order_expected_to_delivered_cod_shipment.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.cod_order_expected_to_delivered_cod_shipment
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_state_transition.state_transition.cod_order_expected_to_delivered_cod_shipment
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_state_transition.state_transition.delivered_cod_shipment_to_cod_collected_by_courier
  edge_type: HAS_STATE_TRANSITION
  source: business_process.cod_delivery_to_courier_remittance
  target: state_transition.delivered_cod_shipment_to_cod_collected_by_courier
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.delivered_cod_shipment_to_cod_collected_by_courier.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.delivered_cod_shipment_to_cod_collected_by_courier
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_state_transition.state_transition.delivered_cod_shipment_to_cod_collected_by_courier
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_state_transition.state_transition.cod_collected_by_courier_to_cod_remittance_recorded
  edge_type: HAS_STATE_TRANSITION
  source: business_process.cod_delivery_to_courier_remittance
  target: state_transition.cod_collected_by_courier_to_cod_remittance_recorded
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.cod_collected_by_courier_to_cod_remittance_recorded.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.cod_collected_by_courier_to_cod_remittance_recorded
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_state_transition.state_transition.cod_collected_by_courier_to_cod_remittance_recorded
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_state_transition.state_transition.cod_remittance_recorded_to_remittance_reference_available
  edge_type: HAS_STATE_TRANSITION
  source: business_process.cod_delivery_to_courier_remittance
  target: state_transition.cod_remittance_recorded_to_remittance_reference_available
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.cod_remittance_recorded_to_remittance_reference_available.belongs_to_process.business_process.cod_delivery_to_courier_remittance
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.cod_remittance_recorded_to_remittance_reference_available
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_state_transition.state_transition.cod_remittance_recorded_to_remittance_reference_available
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.aggregator_routed_shiprocket
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.cod_delivery_to_courier_remittance
  target: process_variant.aggregator_routed_shiprocket
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.aggregator_routed_shiprocket.extends_process.business_process.cod_delivery_to_courier_remittance
  edge_type: EXTENDS_PROCESS
  source: process_variant.aggregator_routed_shiprocket
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.aggregator_routed_shiprocket
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.direct_courier_delhivery
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.cod_delivery_to_courier_remittance
  target: process_variant.direct_courier_delhivery
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.direct_courier_delhivery.extends_process.business_process.cod_delivery_to_courier_remittance
  edge_type: EXTENDS_PROCESS
  source: process_variant.direct_courier_delhivery
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.direct_courier_delhivery
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.settlement_only_dtdc
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.cod_delivery_to_courier_remittance
  target: process_variant.settlement_only_dtdc
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.settlement_only_dtdc.extends_process.business_process.cod_delivery_to_courier_remittance
  edge_type: EXTENDS_PROCESS
  source: process_variant.settlement_only_dtdc
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.settlement_only_dtdc
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.platform_fulfilled_ekart
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.cod_delivery_to_courier_remittance
  target: process_variant.platform_fulfilled_ekart
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.platform_fulfilled_ekart.extends_process.business_process.cod_delivery_to_courier_remittance
  edge_type: EXTENDS_PROCESS
  source: process_variant.platform_fulfilled_ekart
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.platform_fulfilled_ekart
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.low_confidence_native_xpressbees
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.cod_delivery_to_courier_remittance
  target: process_variant.low_confidence_native_xpressbees
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.low_confidence_native_xpressbees.extends_process.business_process.cod_delivery_to_courier_remittance
  edge_type: EXTENDS_PROCESS
  source: process_variant.low_confidence_native_xpressbees
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.low_confidence_native_xpressbees
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.uses_metric.metric.cod_expected_amount
  edge_type: USES_METRIC
  source: business_process.cod_delivery_to_courier_remittance
  target: metric.cod_expected_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.uses_metric.metric.cod_collected_amount
  edge_type: USES_METRIC
  source: business_process.cod_delivery_to_courier_remittance
  target: metric.cod_collected_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.uses_metric.metric.cod_remitted_amount
  edge_type: USES_METRIC
  source: business_process.cod_delivery_to_courier_remittance
  target: metric.cod_remitted_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.uses_metric.metric.cod_gap_amount
  edge_type: USES_METRIC
  source: business_process.cod_delivery_to_courier_remittance
  target: metric.cod_gap_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.uses_metric.metric.cod_remittance_lag_days
  edge_type: USES_METRIC
  source: business_process.cod_delivery_to_courier_remittance
  target: metric.cod_remittance_lag_days
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.cod_delivery_to_courier_remittance
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: business_process.fields.reconciliation_profiles
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.supports_process.business_process.cod_delivery_to_courier_remittance
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.cod_order_expected_to_delivered_cod_shipment.triggered_by_step.workflow_step.cod_delivery_confirmed
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.cod_order_expected_to_delivered_cod_shipment
  target: workflow_step.cod_delivery_confirmed
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.delivered_cod_shipment_to_cod_collected_by_courier.triggered_by_step.workflow_step.cod_collected_by_courier
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.delivered_cod_shipment_to_cod_collected_by_courier
  target: workflow_step.cod_collected_by_courier
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.cod_collected_by_courier_to_cod_remittance_recorded.triggered_by_step.workflow_step.cod_remittance_record_created
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.cod_collected_by_courier_to_cod_remittance_recorded
  target: workflow_step.cod_remittance_record_created
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.cod_remittance_recorded_to_remittance_reference_available.triggered_by_step.workflow_step.settlement_date_or_utr_recorded
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.cod_remittance_recorded_to_remittance_reference_available
  target: workflow_step.settlement_date_or_utr_recorded
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_workflow_step.workflow_step.prepaid_pos_shipment_identified
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.prepaid_pos_logistics_settlement
  target: workflow_step.prepaid_pos_shipment_identified
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.prepaid_pos_shipment_identified.belongs_to_process.business_process.prepaid_pos_logistics_settlement
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.prepaid_pos_shipment_identified
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_workflow_step.workflow_step.prepaid_pos_shipment_identified
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_workflow_step.workflow_step.pos_settlement_created
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.prepaid_pos_logistics_settlement
  target: workflow_step.pos_settlement_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.pos_settlement_created.belongs_to_process.business_process.prepaid_pos_logistics_settlement
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.pos_settlement_created
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_workflow_step.workflow_step.pos_settlement_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_workflow_step.workflow_step.pos_batch_created
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.prepaid_pos_logistics_settlement
  target: workflow_step.pos_batch_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.pos_batch_created.belongs_to_process.business_process.prepaid_pos_logistics_settlement
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.pos_batch_created
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_workflow_step.workflow_step.pos_batch_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_workflow_step.workflow_step.pos_bank_reference_assigned
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.prepaid_pos_logistics_settlement
  target: workflow_step.pos_bank_reference_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.pos_bank_reference_assigned.belongs_to_process.business_process.prepaid_pos_logistics_settlement
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.pos_bank_reference_assigned
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_workflow_step.workflow_step.pos_bank_reference_assigned
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_state_transition.state_transition.prepaid_or_pos_shipment_to_pos_settlement_created
  edge_type: HAS_STATE_TRANSITION
  source: business_process.prepaid_pos_logistics_settlement
  target: state_transition.prepaid_or_pos_shipment_to_pos_settlement_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.prepaid_or_pos_shipment_to_pos_settlement_created.belongs_to_process.business_process.prepaid_pos_logistics_settlement
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.prepaid_or_pos_shipment_to_pos_settlement_created
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_state_transition.state_transition.prepaid_or_pos_shipment_to_pos_settlement_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_state_transition.state_transition.pos_settlement_created_to_pos_batch_created
  edge_type: HAS_STATE_TRANSITION
  source: business_process.prepaid_pos_logistics_settlement
  target: state_transition.pos_settlement_created_to_pos_batch_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.pos_settlement_created_to_pos_batch_created.belongs_to_process.business_process.prepaid_pos_logistics_settlement
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.pos_settlement_created_to_pos_batch_created
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_state_transition.state_transition.pos_settlement_created_to_pos_batch_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_state_transition.state_transition.pos_batch_created_to_pos_settlement_reference_recorded
  edge_type: HAS_STATE_TRANSITION
  source: business_process.prepaid_pos_logistics_settlement
  target: state_transition.pos_batch_created_to_pos_settlement_reference_recorded
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.pos_batch_created_to_pos_settlement_reference_recorded.belongs_to_process.business_process.prepaid_pos_logistics_settlement
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.pos_batch_created_to_pos_settlement_reference_recorded
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_state_transition.state_transition.pos_batch_created_to_pos_settlement_reference_recorded
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_process_variant.process_variant.platform_fulfilled_ekart
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.prepaid_pos_logistics_settlement
  target: process_variant.platform_fulfilled_ekart
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.platform_fulfilled_ekart.extends_process.business_process.prepaid_pos_logistics_settlement
  edge_type: EXTENDS_PROCESS
  source: process_variant.platform_fulfilled_ekart
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_process_variant.process_variant.platform_fulfilled_ekart
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.uses_metric.metric.pos_settled_amount
  edge_type: USES_METRIC
  source: business_process.prepaid_pos_logistics_settlement
  target: metric.pos_settled_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.uses_metric.metric.batch_settlement_amount
  edge_type: USES_METRIC
  source: business_process.prepaid_pos_logistics_settlement
  target: metric.batch_settlement_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.prepaid_or_pos_shipment_to_pos_settlement_created.triggered_by_step.workflow_step.pos_settlement_created
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.prepaid_or_pos_shipment_to_pos_settlement_created
  target: workflow_step.pos_settlement_created
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.pos_settlement_created_to_pos_batch_created.triggered_by_step.workflow_step.pos_batch_created
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.pos_settlement_created_to_pos_batch_created
  target: workflow_step.pos_batch_created
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.pos_batch_created_to_pos_settlement_reference_recorded.triggered_by_step.workflow_step.pos_bank_reference_assigned
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.pos_batch_created_to_pos_settlement_reference_recorded
  target: workflow_step.pos_bank_reference_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.remittance_batch_created
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.courier_batch_to_bank_reconciliation
  target: workflow_step.remittance_batch_created
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.remittance_batch_created.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.remittance_batch_created
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.remittance_batch_created
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.utr_or_reference_assigned
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.courier_batch_to_bank_reconciliation
  target: workflow_step.utr_or_reference_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.utr_or_reference_assigned.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.utr_or_reference_assigned
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.utr_or_reference_assigned
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.awb_amounts_aggregated
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.courier_batch_to_bank_reconciliation
  target: workflow_step.awb_amounts_aggregated
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.awb_amounts_aggregated.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.awb_amounts_aggregated
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.awb_amounts_aggregated
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.bank_credit_expected
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.courier_batch_to_bank_reconciliation
  target: workflow_step.bank_credit_expected
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.bank_credit_expected.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.bank_credit_expected
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.bank_credit_expected
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.bank_credit_matched
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.courier_batch_to_bank_reconciliation
  target: workflow_step.bank_credit_matched
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.workflow_steps
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.bank_credit_matched.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.bank_credit_matched
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_WORKFLOW_STEP
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_workflow_step.workflow_step.bank_credit_matched
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_state_transition.state_transition.courier_remittance_batch_created_to_utr_reference_available
  edge_type: HAS_STATE_TRANSITION
  source: business_process.courier_batch_to_bank_reconciliation
  target: state_transition.courier_remittance_batch_created_to_utr_reference_available
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.courier_remittance_batch_created_to_utr_reference_available.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.courier_remittance_batch_created_to_utr_reference_available
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_state_transition.state_transition.courier_remittance_batch_created_to_utr_reference_available
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_state_transition.state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch
  edge_type: HAS_STATE_TRANSITION
  source: business_process.courier_batch_to_bank_reconciliation
  target: state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_state_transition.state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_state_transition.state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected
  edge_type: HAS_STATE_TRANSITION
  source: business_process.courier_batch_to_bank_reconciliation
  target: state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_state_transition.state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_state_transition.state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned
  edge_type: HAS_STATE_TRANSITION
  source: business_process.courier_batch_to_bank_reconciliation
  target: state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.state_transitions
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned.belongs_to_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_STATE_TRANSITION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_state_transition.state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_process_variant.process_variant.logistics_to_bank_with_utr
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.courier_batch_to_bank_reconciliation
  target: process_variant.logistics_to_bank_with_utr
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.logistics_to_bank_with_utr.extends_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: EXTENDS_PROCESS
  source: process_variant.logistics_to_bank_with_utr
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_process_variant.process_variant.logistics_to_bank_with_utr
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_process_variant.process_variant.batch_without_utr_review_required
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.courier_batch_to_bank_reconciliation
  target: process_variant.batch_without_utr_review_required
  fields:
    edge_family: process_understanding
    evidence_basis: business_process.fields.process_variants
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.batch_without_utr_review_required.extends_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: EXTENDS_PROCESS
  source: process_variant.batch_without_utr_review_required
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of HAS_PROCESS_VARIANT
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_process_variant.process_variant.batch_without_utr_review_required
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.uses_metric.metric.batch_settlement_amount
  edge_type: USES_METRIC
  source: business_process.courier_batch_to_bank_reconciliation
  target: metric.batch_settlement_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.uses_metric.metric.bank_credit_matched_amount
  edge_type: USES_METRIC
  source: business_process.courier_batch_to_bank_reconciliation
  target: metric.bank_credit_matched_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.uses_metric.metric.unmatched_bank_credit_amount
  edge_type: USES_METRIC
  source: business_process.courier_batch_to_bank_reconciliation
  target: metric.unmatched_bank_credit_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: business_process.fields.common_metrics
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.courier_batch_to_bank_reconciliation
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: business_process.fields.reconciliation_profiles
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.supports_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.courier_remittance_batch_created_to_utr_reference_available.triggered_by_step.workflow_step.utr_or_reference_assigned
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.courier_remittance_batch_created_to_utr_reference_available
  target: workflow_step.utr_or_reference_assigned
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch.triggered_by_step.workflow_step.awb_amounts_aggregated
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.utr_reference_available_to_awb_amounts_aggregated_to_batch
  target: workflow_step.awb_amounts_aggregated
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected.triggered_by_step.workflow_step.bank_credit_expected
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.awb_amounts_aggregated_to_batch_to_bank_credit_expected
  target: workflow_step.bank_credit_expected
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned.triggered_by_step.workflow_step.bank_credit_matched
  edge_type: TRIGGERED_BY_STEP
  source: state_transition.bank_credit_expected_to_bank_credit_matched_or_exceptioned
  target: workflow_step.bank_credit_matched
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.triggering_step_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TRIGGERED_BY_STEP
    inverse_edge_type: TRIGGERS_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.process_variant.indirect_only_ecom_express.extends_process.business_process.cod_delivery_to_courier_remittance
  edge_type: EXTENDS_PROCESS
  source: process_variant.indirect_only_ecom_express
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: process_understanding
    evidence_basis: process_variant.fields.affected_business_processes
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: EXTENDS_PROCESS
    inverse_edge_type: HAS_PROCESS_VARIANT
    materialize_inverse: true
    edge_class: canonical
    source_type: process_variant
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_process_variant.process_variant.indirect_only_ecom_express
  edge_type: HAS_PROCESS_VARIANT
  source: business_process.cod_delivery_to_courier_remittance
  target: process_variant.indirect_only_ecom_express
  fields:
    edge_family: process_understanding
    evidence_basis: materialized inverse of EXTENDS_PROCESS
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PROCESS_VARIANT
    inverse_edge_type: EXTENDS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: process_variant
    materialized_from: edge.process_variant.indirect_only_ecom_express.extends_process.business_process.cod_delivery_to_courier_remittance
```

## 6. Review Items

```yaml
review_item:
  id: review.logistics_domain_overview_parser_ready_v4_unified_edges.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted
    from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```

## 7. Validation Summary

```yaml
validation_summary:
  document_id: logistics_domain_overview_parser_ready_v4_unified_edges
  candidate_cards: 157
  candidate_edges: 363
  card_types:
    metric: 51
    domain: 1
    table: 1
    column: 4
    relationship: 1
    formula_template: 7
    metric_dependency: 5
    business_process: 9
    workflow_step: 39
    state_transition: 30
    process_variant: 9
  edge_types:
    BELONGS_TO_DOMAIN: 60
    HAS_BUSINESS_PROCESS: 9
    HAS_COLUMN: 4
    BELONGS_TO_TABLE: 4
    HAS_RELATIONSHIP: 2
    SOURCE_TABLE: 1
    TARGET_TABLE: 1
    USES_SOURCE_COLUMN: 1
    USES_TARGET_COLUMN: 1
    PARENT_METRIC: 5
    DEPENDS_ON_METRIC: 9
    USES_DEPENDENT_METRIC: 9
    USES_FORMULA_TEMPLATE: 5
    HAS_WORKFLOW_STEP: 39
    BELONGS_TO_PROCESS: 69
    HAS_STATE_TRANSITION: 30
    HAS_PROCESS_VARIANT: 23
    EXTENDS_PROCESS: 23
    USES_METRIC: 26
    HAS_RECONCILIATION_PROFILE: 6
    SUPPORTS_PROCESS: 6
    TRIGGERED_BY_STEP: 30
  forbidden_card_types_present: []
  parser_boundary: generic logistics reusable knowledge only
```
