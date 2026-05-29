---
title: Shiprocket Logistics Knowledge
version: 2.2-ingestion-ready
doc_type: logistics_vendor_knowledge
domain: logistics
platform: shiprocket
platform_type: courier_aggregator
fulfilment_ownership_models:
  - aggregator_routed
schemas:
  - zs_observe
primary_tables:
  - zs_observe.shiprocket_oms
  - zs_observe.shiprocket_invoice
  - zs_observe.shiprocket_settlement
related_tables:
  - zs_observe.shiprocket_settlement_report
  - zs_observe.delhivery_invoice
  - zs_observe.delhivery_settlement
  - zs_observe.dtdc_settlement
  - zs_observe.ekart_settlement
  - zs_observe.xpressbees_settlement
flow_types:
  - shipment_tracking
  - freight_billing
  - cod_remittance
  - reverse_logistics
money_flow_paths:
  - order_to_shipment
  - shipment_to_freight_invoice
  - cod_delivery_to_courier_remittance
  - courier_remittance_to_bank
coverage_status: active_with_table_specific_caveats
status: draft
owner: finance_data_team
source_documents:
  - Logistics KB Doc.docx
related_docs:
  - logistics_domain_overview.md
  - delhivery_logistics.md
  - dtdc_logistics.md
  - xpressbees_logistics.md
  - ekart_logistics.md
  - shadowfax_ecom_logistics.md
  - logistics_reconciliation_patterns.md
---

# Shiprocket Logistics Knowledge

> Scope note: This document is a reusable KB grounding document. It preserves logistics concepts, table semantics, join keys, amount meanings, and caveats. It does **not** define tenant/group ownership, customer-specific account scope, or durable marketplace routing. Tenant/group/account filters should be resolved through Business Hierarchy, Platform Account, Account Data Binding, Business Scope Set, and Runtime Scope.


## 1. How to use this document

Use this document when questions involve Shiprocket shipment tracking, AWB assignment, courier allocation, freight invoices, COD settlements, reverse logistics routed through Shiprocket, or fallback evidence for underlying couriers.

Retrieve this doc for questions such as:

- Which shipments have an AWB but no freight invoice?
- Which COD shipments were delivered but not remitted?
- Which courier partner handled a shipment routed through Shiprocket?
- Which Shiprocket amount field means product value, freight, or COD?
- How do Shiprocket records connect to Delhivery, DTDC, XpressBees, Ekart, or Ecom evidence?

## 2. Logistics overview and business context

Shiprocket acts as a courier aggregator. It can sit between a channel/warehouse and multiple final courier partners. The source document describes Shiprocket routing shipments to partners such as Delhivery, DTDC, XpressBees, Ekart, Shadowfax, and Ecom Express.

Shiprocket evidence has three major layers:

```text
shiprocket_oms          = shipment/order/AWB/courier/status evidence
shiprocket_invoice      = freight billing evidence per AWB
shiprocket_settlement   = COD remittance evidence per AWB
```

`shiprocket_settlement_report` exists as a schema/report candidate but should be treated as schema-only until data is confirmed.

## 3. Applicability and scope model

Shiprocket is a reusable `courier_aggregator` / `aggregator_routed` platform. It should not be treated as the default logistics path for every marketplace or tenant.

Account filters such as group/account identifiers must be resolved using Account Data Binding for each Shiprocket table.

This doc can support D2C/channel, seller-fulfilled, marketplace-assisted, and aggregator-routed logistics analysis when runtime scope selects a Shiprocket platform account and relevant tables.

## 4. Fulfilment ownership and shipping model

Primary model:

```text
aggregator_routed
```

Shiprocket may assign the final courier partner. Therefore, distinguish:

```text
Shiprocket = aggregator evidence
courier_partner / courier_company = final courier evidence
```

Do not assume Shiprocket and the final courier are the same entity.

## 5. Operational shipment lifecycle

The source Shiprocket OMS table covers a broad operational lifecycle:

```text
shipment created
→ AWB assigned
→ courier assigned
→ pickup scheduled
→ picked up
→ in transit
→ delivered / RTO delivered / return delivered / cancelled / damaged/lost
```

It also contains NDR fields for failed delivery attempts.

## 6. Money movement lifecycle

Shiprocket supports two major money evidence layers:

### Freight billing

```text
AWB / shipment
→ shiprocket_invoice
→ freight components
→ total freight billed
```

`shiprocket_invoice.charged_amount` is the freight bill amount in the invoice table.

### COD remittance

```text
COD shipment delivered
→ courier collects COD
→ shiprocket_settlement row
→ settlement date
→ possible bank bridge through remittance/UTR fields where available
```

`shiprocket_settlement.charged_amount` means COD collected/remitted amount, not freight.

## 7. Business objects and identifiers

| Object | Shiprocket field examples |
|---|---|
| Shiprocket order | `order_id` in OMS / invoice / settlement |
| Channel order | source order embedded in composite order ID, where applicable |
| AWB / tracking | `awb_code`, `other_id`, `awb_number` |
| Courier partner | `courier_company`, `fulfilment_channel`, `courier_partner`, `master_courier` |
| Freight invoice | `shiprocket_invoice` row, `other_id` as AWB bridge |
| COD settlement | `shiprocket_settlement` row, `awb_number` as AWB bridge |
| Bank bridge | `utr_no`, `crf_id`, settlement/remittance references where present |
| NDR evidence | `ndr_*`, `latest_ndr_*`, `attempt_count`, `rto_reason` |

## 8. Table family overview

| Table | Business role | Coverage status |
|---|---|---|
| `zs_observe.shiprocket_oms` | Shipment, AWB, courier assignment, status, NDR, some financial/status fields | active / rich operational table in source snapshot |
| `zs_observe.shiprocket_invoice` | Per-AWB freight invoice raised by Shiprocket | active freight evidence in source snapshot |
| `zs_observe.shiprocket_settlement` | COD remittance evidence by AWB | active COD settlement evidence in source snapshot |
| `zs_observe.shiprocket_settlement_report` | More granular/remittance report schema candidate | schema-only / empty in source snapshot |

Row counts and dates from the source are profiling observations only and should not be encoded as durable KB truth.

## 9. Entity relationships and join paths

Canonical Shiprocket joins:

```text
shiprocket_oms.awb_code
→ shiprocket_invoice.other_id
→ shiprocket_settlement.awb_number
```

Possible cross-source joins:

```text
shiprocket_oms.awb_code → delhivery_invoice.forward_awb_number
shiprocket_oms.awb_code → delhivery_settlement.waybill_num / waybill_number
shiprocket_oms.awb_code → dtdc_settlement.airwaybill_number
shiprocket_oms.awb_code → ekart_settlement.shipment_id / tracking_id
shiprocket_oms.awb_code → xpressbees_settlement.shipping_id, when populated
```

If `order_id` is composite, parse with caution. The source notes a pattern like `{channel_order_id}-s{shiprocket_shipment_id}` for some records. Treat this as a source-specific pattern and validate before use.

## 10. Metrics and business definitions

| Metric | Definition |
|---|---|
| Shiprocket shipment count | Count of Shiprocket OMS shipments/AWBs |
| Delivered shipment count | Count of shipments with delivered status after value normalization |
| RTO shipment count | Count of shipments returned to origin |
| Return shipment count | Count of customer-initiated reverse/return shipments |
| Freight billed | Sum of Shiprocket invoice freight amount at AWB grain |
| Freight billed excluding tax | Sum of Shiprocket invoice pre-tax freight amount at AWB grain |
| Freight tax amount | Sum of invoice GST/tax amount |
| COD expected | COD amount expected from OMS/customer order fields |
| COD remitted | Sum of Shiprocket settlement COD amount at AWB grain |
| COD gap | COD expected minus COD remitted after grain alignment |
| COD remittance lag | Settlement date minus delivery date |
| Uninvoiced AWB count | OMS AWBs missing invoice evidence |
| Unremitted COD AWB count | Delivered COD AWBs missing COD settlement evidence |

## 11. Reconciliation playbook

Valid Shiprocket reconciliation use cases:

1. Order/channel order to Shiprocket shipment.
2. Shiprocket shipment to Shiprocket invoice.
3. Shiprocket shipment to Shiprocket COD settlement.
4. Shiprocket invoice to underlying courier invoice where native invoice exists.
5. Shiprocket COD settlement to underlying courier settlement where native settlement exists.
6. Shiprocket COD remittance to bank bridge, when UTR/remittance reference exists and Banking KB is available.

### 11.1 Reconciliation variants

Shiprocket is the canonical aggregator source for `shipment_to_invoice_reconciliation` and `cod_reconciliation`; the base profiles assume Shiprocket-shaped evidence. The variants below capture supporting bridges Shiprocket plays for under-populated underlying-courier sources.

| Variant name | Base profile | Variant reason | Mismatch category overrides |
|---|---|---|---|
| shiprocket_aggregator_freight_bridge | `reconciliation_profile.shipment_to_invoice_reconciliation` | Shiprocket invoice is the freight evidence source when an underlying courier (DTDC, XpressBees, Shadowfax, Ecom Express) lacks a native invoice; reconciliation runs at AWB grain joined on `shiprocket_invoice.awb`. | `mismatch_category.missing_invoice`, `mismatch_category.orphan_invoice` |
| shiprocket_aggregator_cod_bridge | `reconciliation_profile.cod_reconciliation` | Shiprocket settlement is the COD evidence source when an underlying courier lacks native settlement coverage; reconciliation joins on `shiprocket_settlement.awb` with the underlying courier label preserved as the partitioning dimension. | `mismatch_category.missing_cod_remittance`, `mismatch_category.orphan_shipment` |

## 12. Table-specific curated knowledge

### 12.1 Table: `zs_observe.shiprocket_oms`

#### Business purpose

Courier aggregator OMS table containing shipment, AWB, courier assignment, delivery/RTO/return status, NDR fields, and selected financial/remittance fields.

#### Grain

One row should generally represent one Shiprocket shipment/order-shipment record. Validate uniqueness by `order_id` and/or `awb_code` depending on use case.

#### Table status and coverage

The source describes this as the richest logistics table. Treat it as active but source-period-specific. Re-profile before production use.

#### Applicability and account-binding notes

This table may contain group/account fields. Do not interpret those fields globally. Use Account Data Binding to decide which Shiprocket account/filter applies.

#### Critical filters

- Use `is_active = true` where present.
- Normalize `transaction_type` and `status` before classifying delivered, return, RTO, cancelled, in-transit, or damaged/lost.
- Use `payment_method = cod` or equivalent only after validating values.

#### Key identifiers

| Field | Meaning |
|---|---|
| `order_id` | Shiprocket order ID; may be composite in some integrations |
| `awb_code` | Primary AWB/tracking key |
| `channel` | Channel/source integration label |
| `courier_company` / `fulfilment_channel` | Assigned courier partner |
| `master_courier` | Aggregated courier name |
| `customer_invoice_id` | Invoice reference candidate |
| `utr_no` / `crf_id` | Remittance/bank bridge candidates |

#### Operational fields

- `transaction_type`: forward, return, cancelled, pending/in transit, damaged/lost style values.
- `status`: delivery/RTO/return/cancelled status.
- `created_date`, `awb_assigned_date`, `pickup_scheduled_date`, `order_picked_up_date`, `edd`, `order_delivered_date`, `rto_initiated_date`, `rto_delivered_date`.
- NDR fields such as `ndr_1_attempt_date`, `ndr_1_remark`, `latest_ndr_date`, `latest_ndr_reason`, `attempt_count`, `rto_reason`.

#### Financial fields

| Field | Meaning |
|---|---|
| `charged_amount` | Declared product/order value, not freight |
| `order_total` | Channel/order total |
| `cod_payble_amount` | COD amount expected from customer |
| `payment_method` | prepaid/cod style payment mode |
| `remitted_amount` | COD amount remitted, where populated |
| `cod_remittance_date` | COD remittance date, where populated |
| `freight_total_amount` | Freight charged, where populated |
| `shipping_charges` | Shipping fee breakdown, where populated |

#### Status and value semantics

Source value examples:

| transaction_type | status pattern | Meaning |
|---|---|---|
| `forward` | DELIVERED | Successful forward delivery |
| `forward` | RTO DELIVERED | Forward shipment returned to origin |
| `return` | RETURN DELIVERED | Customer-initiated return completed |
| `return` | RTO DELIVERED | Reverse/RTO style completion; validate semantics |
| `cancelled` | CANCELLED | Cancelled before or during fulfilment |
| `in transit` | IN TRANSIT | Shipment currently in transit |
| `damaged/lost` | DAMAGED/LOST | Shipment lost or damaged |

#### Relationships and joins

- Join to `shiprocket_invoice` using `awb_code = other_id`.
- Join to `shiprocket_settlement` using `awb_code = awb_number`.
- Join to direct courier settlement/invoice tables using their AWB/waybill fields where populated.

#### Reconciliation role

Primary shipment evidence for Shiprocket-routed orders. Useful as expected or bridge side for shipment-to-invoice and shipment-to-COD remittance reconciliation.

#### Caveats

- Many fields may be sparse because Shiprocket exports optional fields across courier integrations.
- `charged_amount` in OMS is not freight.
- `cod_payble_amount` may differ from declared order value due to discounts or adjustments.
- NDR fields only populate for delivery-failure cases.
- Composite order ID parsing is integration-specific; do not generalize without validation.

### 12.2 Table: `zs_observe.shiprocket_invoice`

#### Business purpose

Per-AWB freight invoice raised by Shiprocket to the seller/account. It consolidates freight billing even when an underlying courier performed delivery.

#### Grain

Usually one freight invoice row per AWB/shipment charge line. Validate whether multiple charge lines per AWB exist.

#### Critical filters

- Use `is_active = true` where present.
- Use `courier_partner` only after normalizing names.
- Use `payment_mode` to distinguish COD/prepaid freight components where needed.

#### Key identifiers

| Field | Meaning |
|---|---|
| `order_id` | Shiprocket order ID |
| `other_id` | AWB number; primary join to `shiprocket_oms.awb_code` |
| `courier_partner` | Underlying courier partner |
| `mp_sin` | Shiprocket internal order reference |

#### Financial fields

| Field | Meaning |
|---|---|
| `charged_amount` | Total freight bill for the AWB in invoice context |
| `charged_amount_excluding_tax` | Freight before GST/tax |
| `total_tax` | GST/tax on freight |
| `charge_fsc` | Fuel surcharge |
| `charge_rto` | RTO charge |
| `charge_cod` | COD handling fee |
| `charge_cod_adjust` | COD adjustment |
| `charge_dl` | Delivery/forward charge |
| `settled_amount` | Net freight settled after deductions, where available |
| `referal_fee` | Shiprocket platform/referral fee |

#### Weight and zone fields

- `final_weight`: actual weight.
- `charged_weight`: billable weight.
- `zone`: delivery zone. Source example identifies farther zones as higher freight bands; validate zone semantics by rate-card context.

#### Freight calculation

Use a component-based interpretation:

```text
freight billed = delivery charge + RTO/DTO/COD-related charges + fuel/FOV/other surcharges + taxes/adjustments
```

Do not assume every component is populated for every AWB.

#### Relationships and joins

- `shiprocket_invoice.other_id` → `shiprocket_oms.awb_code`.
- `shiprocket_invoice.other_id` → direct courier AWB fields for courier-level cross-checks when relevant.

#### Reconciliation role

Used to validate freight billed against shipments dispatched and, where possible, against underlying direct courier invoice/settlement records.

#### Caveats

- `charged_amount` in invoice context means freight bill; in other Shiprocket tables it may mean something else.
- Underlying courier names may appear as service labels such as air/weight bands. Normalize before grouping.

### 12.3 Table: `zs_observe.shiprocket_settlement`

#### Business purpose

COD remittance report from Shiprocket. For COD orders, courier collects cash and remittance evidence appears at AWB level.

#### Grain

Generally one COD settlement/remittance record per AWB. Validate duplicates before matching.

#### Key identifiers

| Field | Meaning |
|---|---|
| `order_id` | Shiprocket order ID |
| `awb_number` | AWB; join to `shiprocket_oms.awb_code` and `shiprocket_invoice.other_id` |
| `courier_partner` | Courier that collected COD |

#### Financial and date fields

| Field | Meaning |
|---|---|
| `charged_amount` | COD amount collected/remitted in settlement context |
| `delivered_date` | Delivery date |
| `settlement_date` | COD settlement/remittance date |

#### Relationships and joins

- `shiprocket_settlement.awb_number` → `shiprocket_oms.awb_code`.
- `shiprocket_settlement.awb_number` → `shiprocket_invoice.other_id`.
- `shiprocket_settlement.awb_number` → native courier settlement AWB fields where populated.

#### Reconciliation role

Primary Shiprocket COD remittance evidence. Useful for COD expected vs remitted and courier-level COD fallback where native courier data is sparse.

#### Caveats

- COD lag from delivery to settlement can be substantial and source-specific. Do not encode a universal lag without profiling.
- `charged_amount` means COD here, not freight.
- Bank reconciliation requires batch/UTR/bank evidence and Banking KB context.

### 12.4 Table: `zs_observe.shiprocket_settlement_report`

#### Business purpose

Schema candidate for a more detailed Shiprocket settlement report.

#### Coverage status

The source snapshot describes this table as having no usable data. Treat as `schema_only` until profiling confirms populated records.

#### Fields to preserve if populated later

- `order_id`
- `courier_partner`
- `awb_remittance_status`
- `courier_received_amount`
- `settlement_id`
- `source_gst_name` / `source_gst_id`
- `offer_adjustment_settled_amount`
- `parent_id`

#### Caveats

Do not use for production metrics or reconciliation until data exists and meanings are validated.

## 13. Mandatory query rules

- Do not infer account filters from this vendor doc.
- Apply Account Data Binding for selected Shiprocket platform account and table.
- Use AWB as the primary bridge across OMS, invoice, and settlement where populated.
- Do not compare COD and freight fields without table-context semantics.
- Normalize courier partner names before grouping.
- Treat `shiprocket_settlement_report` as schema-only until populated.
- Prefer Shiprocket consolidated settlement as fallback for underlying courier COD when native courier data is sparse or missing.

## 14. Data-quality and semantic caveats

- Source row counts and periods are profiling snapshots; omit them from durable KB truth.
- Some Shiprocket OMS fields are sparse.
- `charged_amount` has different meanings in OMS, invoice, and settlement.
- Shadowfax/Ecom may appear through Shiprocket even without dedicated native tables.
- Courier partner labels may include service-level names, not just vendor names.

## 15. Supported question patterns

- Which Shiprocket shipments are delivered but not COD-settled?
- Which Shiprocket AWBs have no freight invoice?
- Which courier partner handled this AWB?
- What is the COD remittance lag for Shiprocket shipments?
- Which XpressBees/DTDC/Delhivery shipments are visible through Shiprocket?
- Which Shiprocket amount field should be used for freight vs COD?

## 16. SQL pattern appendix

These examples are illustrative query shapes. Production SQL must inject account filters through Account Data Binding.

```sql
-- Shipment to freight invoice bridge
SELECT
  s.awb_code,
  s.order_id,
  s.courier_company,
  i.charged_amount AS freight_billed
FROM zs_observe.shiprocket_oms s
LEFT JOIN zs_observe.shiprocket_invoice i
  ON s.awb_code = i.other_id
WHERE s.is_active = true
  AND i.is_active = true;
```

```sql
-- Shipment to COD settlement bridge
SELECT
  s.awb_code,
  s.payment_method,
  s.cod_payble_amount,
  ss.charged_amount AS cod_remitted,
  ss.settlement_date
FROM zs_observe.shiprocket_oms s
LEFT JOIN zs_observe.shiprocket_settlement ss
  ON s.awb_code = ss.awb_number
WHERE s.is_active = true
  AND ss.is_active = true;
```

## 17. Extraction guidance

Expected cards:

```text
Platform
Table
Column
Relationship
Value Profile
Metric
Metric Implementation
Reconciliation Profile
Matching Logic
Mismatch Category
Rule
Validation Test
```

Important extraction constraints:

- Extract account-binding fields as candidates only, not fixed account semantics.
- Extract three separate amount meanings for OMS, invoice, and settlement.
- Extract `shiprocket_settlement_report` as schema-only / low-confidence until populated.
---

## 18. Ingestion-ready card extraction detail

> This section is an extraction aid for the ingestion pipeline. It is still raw markdown, not canonical card YAML. Extracted cards should retain evidence references back to the relevant sections above.

### 18.1 Table card candidates

| Candidate table card | Table type | Grain | Coverage / confidence | Notes |
|---|---|---|---|---|
| `table.zs_observe.shiprocket_oms` | operational fact / shipment evidence | Usually one Shiprocket shipment/order-shipment record per AWB/order combination | active, but source-period-specific | Richest Shiprocket operational table. Re-profile before production use. |
| `table.zs_observe.shiprocket_invoice` | freight invoice ledger | Usually one freight invoice/charge row per AWB; validate multiple charge rows per AWB | active freight evidence | `charged_amount` means freight bill in this table only. |
| `table.zs_observe.shiprocket_settlement` | COD settlement ledger | Usually one COD settlement/remittance row per AWB; validate duplicates | active COD remittance evidence | `charged_amount` means COD collected/remitted in this table only. |
| `table.zs_observe.shiprocket_settlement_report` | settlement report / schema candidate | Unknown until populated | schema_only / low confidence | Do not use for metrics until populated and validated. |

### 18.2 Column card candidates — `zs_observe.shiprocket_oms`

| Column | Semantic roles | Business meaning | Metric / reconciliation usage | Caveat |
|---|---|---|---|---|
| `order_id` | identifier, join_key | Shiprocket order identifier; may be integration-specific or composite | order-to-shipment matching, shipment lookup | Composite parsing should be integration-specific, not generic. |
| `awb_code` | identifier, join_key, reconciliation_key | Primary AWB / tracking key | joins to invoice and settlement; shipment-level reconciliation | Validate uniqueness before AWB-grain metrics. |
| `channel` | dimension, filter | Source/channel integration label | channel-level breakdown | Do not infer tenant/group ownership from this field. |
| `courier_company` | dimension, filter | Assigned final courier partner | courier-level grouping, vendor fallback routing | Normalize names before grouping. |
| `fulfilment_channel` | dimension, filter | Fulfilment/courier service label | fulfilment model or courier classification | May be service-level, not only vendor-level. |
| `master_courier` | dimension, filter | Aggregated courier name | courier normalization support | Use as supporting evidence, not sole join key. |
| `customer_invoice_id` | identifier | Customer/order invoice reference candidate | invoice traceability | Meaning may depend on source integration. |
| `utr_no` | identifier, bank_bridge | Possible bank/remittance reference | bank bridge only when populated and validated | Bank matching belongs to Banking KB. |
| `crf_id` | identifier, bank_bridge | Possible remittance/control reference | remittance traceability | Validate source semantics before matching. |
| `transaction_type` | dimension, status, value_profile | Shipment transaction category such as forward, return, cancelled, in transit, damaged/lost | lifecycle classification, delivered/RTO/return metrics | Normalize with `status`; do not use alone. |
| `status` | status, value_profile | Operational shipment status | delivered, RTO, return, cancelled, in-transit classification | Values should be normalized case-insensitively. |
| `created_date` | date | Shipment/order creation date | default shipment reporting date when no better lifecycle date is needed | Confirm timezone/date type. |
| `awb_assigned_date` | date | AWB assignment date | AWB generation lag | May be null before AWB assignment. |
| `pickup_scheduled_date` | date | Scheduled pickup date | pickup SLA analysis | Optional field. |
| `order_picked_up_date` | date | Actual pickup date | pickup lag and handoff analysis | Optional field. |
| `edd` | date | Expected delivery date | delivery SLA analysis | Treat as expected date, not actual delivery. |
| `order_delivered_date` | date | Actual delivery date | delivery count, COD remittance lag denominator | Required for delivery-to-remittance lag when available. |
| `rto_initiated_date` | date | RTO initiation date | RTO lifecycle analysis | Use only for RTO flows. |
| `rto_delivered_date` | date | RTO delivered-to-origin date | RTO completion analysis | Use only for RTO flows. |
| `ndr_1_attempt_date` | date | First NDR attempt date | failed delivery / NDR analysis | Populates only for NDR cases. |
| `ndr_1_remark` | dimension, text | First NDR remark | NDR reason analysis | Free-text normalization may be needed. |
| `latest_ndr_date` | date | Latest NDR event date | NDR aging analysis | Optional. |
| `latest_ndr_reason` | dimension, text | Latest NDR reason | delivery failure classification | Free-text normalization may be needed. |
| `attempt_count` | measure | Delivery attempt count | delivery failure analysis | Numeric quality validation required. |
| `rto_reason` | dimension, text | RTO reason | RTO root-cause analysis | Free-text normalization may be needed. |
| `charged_amount` | measure, financial_amount | Declared product/order value in OMS context | product/order value context only | Not freight and not COD remittance. |
| `order_total` | measure, financial_amount | Channel/order total | order value analysis | May differ from COD payable due to discounts/adjustments. |
| `cod_payble_amount` | measure, financial_amount | COD amount expected from customer | COD expected metric | Typo-like field name should be preserved as source column. |
| `payment_method` | dimension, filter, value_profile | Payment mode such as COD/prepaid | COD filtering, prepaid/COD split | Validate exact values before filtering. |
| `remitted_amount` | measure, financial_amount | COD amount remitted where populated in OMS | supporting COD remittance evidence | Prefer settlement table for primary remittance evidence. |
| `cod_remittance_date` | date | COD remittance date where populated | COD lag support | Prefer settlement table date when available. |
| `freight_total_amount` | measure, financial_amount | Freight charged where populated in OMS | supporting freight evidence | Prefer invoice table for primary freight billing. |
| `shipping_charges` | measure, financial_amount | Shipping fee breakdown where populated | supporting shipping charge analysis | Validate relation to invoice freight. |
| `is_active` | filter | Active/current row indicator | mandatory filter where present | Apply only if column exists in the table. |

### 18.3 Column card candidates — `zs_observe.shiprocket_invoice`

| Column | Semantic roles | Business meaning | Metric / reconciliation usage | Caveat |
|---|---|---|---|---|
| `order_id` | identifier | Shiprocket order ID | order-level traceability | Not the primary invoice-OMS join if AWB is available. |
| `other_id` | identifier, join_key, reconciliation_key | AWB number in invoice context | primary join to `shiprocket_oms.awb_code` and `shiprocket_settlement.awb_number` | Validate formatting and nulls. |
| `courier_partner` | dimension, filter, value_profile | Underlying courier partner/service | courier-level freight breakdown | Normalize names before grouping. |
| `mp_sin` | identifier | Shiprocket internal reference | traceability | Use as supporting ID only. |
| `charged_amount` | measure, financial_amount | Total freight bill for AWB in invoice context | freight billed metric | Not product value and not COD remittance in this table. |
| `charged_amount_excluding_tax` | measure, financial_amount | Freight before GST/tax | pre-tax freight metric | Validate whether all taxes are excluded. |
| `total_tax` | measure, financial_amount | GST/tax on freight | tax component analysis | May include CGST/SGST/IGST depending on source. |
| `charge_fsc` | measure, financial_amount | Fuel surcharge | freight component analysis | Component may be null. |
| `charge_rto` | measure, financial_amount | RTO charge | RTO freight metric | Use only for RTO/reverse flows. |
| `charge_cod` | measure, financial_amount | COD handling fee | COD fee component | Not COD remitted amount. |
| `charge_cod_adjust` | measure, financial_amount | COD adjustment | freight/COD fee adjustment | Interpret as adjustment, not customer COD. |
| `charge_dl` | measure, financial_amount | Delivery / forward charge | forward freight component | Component may be null. |
| `settled_amount` | measure, financial_amount | Net freight settled after deductions, where available | freight settlement support | Confirm semantics before using as invoice total. |
| `referal_fee` | measure, financial_amount | Shiprocket platform/referral fee | fee analysis | Preserve source spelling. |
| `final_weight` | measure | Actual/final weight | weight-based freight validation | Unit must be confirmed. |
| `charged_weight` | measure | Billable weight | freight validation | Unit must be confirmed. |
| `zone` | dimension, value_profile | Delivery zone / freight band | zone-wise freight analysis | Zone semantics require rate-card context. |
| `payment_mode` | dimension, filter, value_profile | COD/prepaid mode if present | payment-mode breakdown | Validate exact values. |
| `is_active` | filter | Active/current row indicator | mandatory filter where present | Apply only if column exists. |

### 18.4 Column card candidates — `zs_observe.shiprocket_settlement`

| Column | Semantic roles | Business meaning | Metric / reconciliation usage | Caveat |
|---|---|---|---|---|
| `order_id` | identifier | Shiprocket order ID | traceability to OMS/order | AWB remains preferred settlement join key. |
| `awb_number` | identifier, join_key, reconciliation_key | AWB number in settlement context | primary join to OMS and invoice | Validate duplicates. |
| `courier_partner` | dimension, filter, value_profile | Courier that collected COD | courier-level COD remittance breakdown | Normalize names. |
| `charged_amount` | measure, financial_amount | COD amount collected/remitted in settlement context | COD remitted metric | Not freight and not product value. |
| `delivered_date` | date | Delivery date | COD lag denominator | Validate against OMS delivery date when both exist. |
| `settlement_date` | date | COD settlement/remittance date | COD remittance lag, settlement reporting | May lag delivery substantially. |
| `is_active` | filter | Active/current row indicator | mandatory filter where present | Apply only if column exists. |

### 18.5 Column card candidates — `zs_observe.shiprocket_settlement_report`

| Column | Semantic roles | Business meaning | Metric / reconciliation usage | Caveat |
|---|---|---|---|---|
| `order_id` | identifier | Order reference candidate | future traceability | Schema-only until data exists. |
| `courier_partner` | dimension | Courier partner candidate | future courier grouping | Schema-only until data exists. |
| `awb_remittance_status` | status, value_profile | AWB remittance status candidate | future remittance status classification | Schema-only until data exists. |
| `courier_received_amount` | measure, financial_amount | Amount received by courier candidate | future COD/remittance analysis | Schema-only until data exists. |
| `settlement_id` | identifier | Settlement reference candidate | future settlement batch matching | Schema-only until data exists. |
| `source_gst_name` | dimension | GST entity name candidate | future tax/entity analysis | Schema-only until data exists. |
| `source_gst_id` | identifier | GST entity ID candidate | future tax/entity analysis | Schema-only until data exists. |
| `offer_adjustment_settled_amount` | measure, financial_amount | Offer adjustment settlement candidate | future settlement adjustment analysis | Schema-only until data exists. |
| `parent_id` | identifier | Parent reference candidate | future hierarchy/rollup | Schema-only until data exists. |

### 18.6 Relationship card candidates

| Candidate relationship | Source table / column | Target table / column | Type | Cardinality expectation | Safe for | Caveats |
|---|---|---|---|---|---|---|
| `relationship.shiprocket_oms.shiprocket_invoice.awb` | `shiprocket_oms.awb_code` | `shiprocket_invoice.other_id` | shipment_to_invoice | one-to-zero-or-many | freight reconciliation | Validate multiple invoice rows per AWB. |
| `relationship.shiprocket_oms.shiprocket_settlement.awb` | `shiprocket_oms.awb_code` | `shiprocket_settlement.awb_number` | shipment_to_cod_settlement | one-to-zero-or-one or one-to-many | COD reconciliation | COD-only shipments expected; prepaid may not settle. |
| `relationship.shiprocket_invoice.shiprocket_settlement.awb` | `shiprocket_invoice.other_id` | `shiprocket_settlement.awb_number` | invoice_to_cod_settlement_bridge | many-to-zero-or-many | diagnostic only | Freight and COD are different money concepts; do not compare amounts directly. |
| `relationship.shiprocket_oms.delhivery_invoice.awb` | `shiprocket_oms.awb_code` | `delhivery_invoice.forward_awb_number` | aggregator_to_direct_courier_invoice | candidate | courier cross-check | Use only when Delhivery is final courier and native data is populated. |
| `relationship.shiprocket_settlement.delhivery_settlement.awb` | `shiprocket_settlement.awb_number` | `delhivery_settlement.waybill_num` / `waybill_number` | aggregator_to_direct_courier_settlement | candidate | COD cross-check | Requires courier partner alignment and grain validation. |
| `relationship.shiprocket_settlement.dtdc_settlement.awb` | `shiprocket_settlement.awb_number` | DTDC AWB field | aggregator_to_direct_courier_settlement | candidate | COD fallback/cross-check | Only if DTDC settlement table exposes comparable AWB field. |
| `relationship.shiprocket_settlement.xpressbees_settlement.awb` | `shiprocket_settlement.awb_number` | XpressBees AWB field | aggregator_to_direct_courier_settlement | candidate | low-confidence cross-check | Native XpressBees may be sparse; mark low confidence. |

### 18.7 Value profile candidates

| Candidate value profile | Column | Values / patterns to preserve | Business meaning | Extraction note |
|---|---|---|---|---|
| `value_profile.shiprocket_oms.transaction_type` | `shiprocket_oms.transaction_type` | `forward`, `return`, `cancelled`, `in transit`, `damaged/lost` | lifecycle category | Normalize case and map with `status`. |
| `value_profile.shiprocket_oms.status` | `shiprocket_oms.status` | `DELIVERED`, `RTO DELIVERED`, `RETURN DELIVERED`, `CANCELLED`, `IN TRANSIT`, `DAMAGED/LOST` | operational shipment state | Should support delivered/RTO/return/cancelled/in-transit classifications. |
| `value_profile.shiprocket_oms.payment_method` | `shiprocket_oms.payment_method` | COD/prepaid-like values | payment mode | Use for COD expected filtering only after validating exact values. |
| `value_profile.shiprocket_invoice.courier_partner` | `shiprocket_invoice.courier_partner` | Delhivery, DTDC, XpressBees, Ekart, Shadowfax, Ecom Express, service labels | underlying courier/service | Normalize to canonical courier names separately. |
| `value_profile.shiprocket_settlement.courier_partner` | `shiprocket_settlement.courier_partner` | courier names in COD settlement | courier collecting/remitting COD | Use for courier-level COD grouping after normalization. |
| `value_profile.shiprocket_settlement_report.awb_remittance_status` | `shiprocket_settlement_report.awb_remittance_status` | unknown until populated | future remittance status | Extract as schema-only / pending. |

---

## 19. Metric and metric implementation extraction detail

### 19.1 Metric implementation candidates

| Metric | Candidate implementation | Base table(s) | Formula / logic | Grain | Required columns | Caveats |
|---|---|---|---|---|---|---|
| Shiprocket shipment count | Count distinct Shiprocket AWBs | `shiprocket_oms` | `COUNT(DISTINCT awb_code)` after active filtering | AWB / shipment | `awb_code`, `is_active` | Validate AWB uniqueness and nulls. |
| Delivered shipment count | Count delivered forward shipments | `shiprocket_oms` | Count AWBs where normalized status indicates delivered and lifecycle is forward | AWB / shipment | `awb_code`, `status`, `transaction_type` | Normalize status and transaction type together. |
| RTO shipment count | Count returned-to-origin shipments | `shiprocket_oms` | Count AWBs where status/transaction type indicates RTO | AWB / shipment | `awb_code`, `status`, `transaction_type`, `rto_delivered_date` | RTO logic must be value-profile driven. |
| Return shipment count | Count customer-initiated return shipments | `shiprocket_oms` | Count AWBs where `transaction_type` indicates return and status indicates return completion | AWB / shipment | `awb_code`, `transaction_type`, `status` | Do not mix RTO and customer return without explicit mapping. |
| Freight billed | Sum freight invoice amount | `shiprocket_invoice` | `SUM(charged_amount)` after active filtering and AWB-grain alignment | AWB / invoice | `other_id`, `charged_amount`, `is_active` | `charged_amount` means freight only in invoice table. |
| Freight billed excluding tax | Sum pre-tax freight | `shiprocket_invoice` | `SUM(charged_amount_excluding_tax)` | AWB / invoice | `charged_amount_excluding_tax` | Validate tax inclusion/exclusion. |
| Freight tax amount | Sum invoice tax | `shiprocket_invoice` | `SUM(total_tax)` | AWB / invoice | `total_tax` | Tax field may represent total GST. |
| COD expected | Sum expected COD from OMS | `shiprocket_oms` | `SUM(cod_payble_amount)` for COD shipments after active filtering | AWB / shipment | `cod_payble_amount`, `payment_method`, `status` | Use only for COD shipments; exact COD filter is value-profile driven. |
| COD remitted | Sum Shiprocket COD settlement amount | `shiprocket_settlement` | `SUM(charged_amount)` after active filtering | AWB / settlement | `charged_amount`, `awb_number`, `settlement_date` | `charged_amount` means COD here, not freight. |
| COD gap | Expected COD minus remitted COD | `shiprocket_oms` + `shiprocket_settlement` | Aggregate by AWB, compare `cod_payble_amount` vs settlement `charged_amount` | AWB, day, courier | OMS COD expected, settlement charged amount | Align grain before subtracting. |
| COD remittance lag | Settlement date minus delivery date | `shiprocket_oms` + `shiprocket_settlement` | `DATE_DIFF('day', order_delivered_date, settlement_date)` | AWB | `order_delivered_date`, `settlement_date` | Use only delivered COD shipments with valid dates. |
| Uninvoiced AWB count | Count OMS AWBs without invoice | `shiprocket_oms` + `shiprocket_invoice` | Left join OMS to invoice on AWB and count invoice-null AWBs | AWB | `awb_code`, `other_id` | Apply active filters carefully; null invoice may be timing-related. |
| Unremitted COD AWB count | Count delivered COD AWBs without settlement | `shiprocket_oms` + `shiprocket_settlement` | Left join delivered COD OMS AWBs to settlement; count settlement-null AWBs | AWB | `awb_code`, `payment_method`, `status`, `awb_number` | Apply remittance lag window before classifying missing. |

### 19.2 Formula template candidates

| Formula template | Applies to | Plain-English formula | Notes |
|---|---|---|---|
| `formula_template.count_distinct_identifier` | shipment count, delivered count, RTO count, return count | Count unique AWB or shipment identifiers after status filtering | Requires null and duplicate handling. |
| `formula_template.sum_financial_amount` | freight billed, COD expected, COD remitted | Sum the relevant amount field after table-context semantic validation | Amount field meaning must be table-specific. |
| `formula_template.gap_amount` | COD gap | Expected amount minus actual/remitted amount after grain alignment | Requires pre-aggregation before subtraction. |
| `formula_template.lag_days` | COD remittance lag | Later event date minus earlier event date | Requires valid date columns. |
| `formula_template.unmatched_count` | uninvoiced AWB, unremitted COD AWB | Left join expected side to actual side and count missing actual records | Requires timing-window rules. |

---

## 20. Rule and validation extraction detail

### 20.1 Rule candidates

| Rule | Rule type | Severity | Statement | Applies to |
|---|---|---:|---|---|
| Shiprocket account filters must come from Account Data Binding | scope_filter | critical | Do not infer account or tenant scope from this vendor doc. | all Shiprocket tables |
| Use AWB as primary Shiprocket bridge | join_safety | high | Use `awb_code`, `other_id`, and `awb_number` as the primary bridge across OMS, invoice, and settlement where populated. | OMS, invoice, settlement relationships |
| Preserve table-specific amount semantics | metric_semantics | critical | `charged_amount` means different things in OMS, invoice, and settlement. | amount columns |
| Treat `shiprocket_settlement_report` as schema-only | data_quality | high | Do not use this table for metrics/reconciliation until populated. | settlement report |
| Normalize courier partner names | value_normalization | medium | Normalize courier names before grouping or comparing to direct courier tables. | courier fields |
| Align grain before comparing COD expected and remitted | aggregation_safety | critical | Compare COD expected and COD remitted at AWB or settlement grain after aggregation. | COD metrics/reconciliation |
| Apply active-row filters only where present | filter_safety | high | Use `is_active = true` where the column exists; do not invent the filter for tables without it. | all tables |
| Do not classify remittance as missing before lag window | reconciliation_window | high | COD settlement can lag delivery; missing classification requires an allowed delay window. | COD reconciliation |

### 20.2 Validation test candidates

| Validation test | Test type | Blocking? | Validates |
|---|---|---:|---|
| `validation.shiprocket_scope_filter_from_binding` | semantic_check | yes | Account filters are injected from Account Data Binding, not hardcoded. |
| `validation.shiprocket_awb_join_keys_present` | join_check | yes | OMS/invoice/settlement joins use `awb_code`, `other_id`, `awb_number` correctly. |
| `validation.shiprocket_charged_amount_context` | semantic_check | yes | `charged_amount` is interpreted according to the table context. |
| `validation.shiprocket_settlement_report_not_used_for_metrics` | semantic_check | yes | Schema-only table is not used in production metric implementation. |
| `validation.shiprocket_cod_gap_grain_alignment` | grain_check | yes | COD expected and COD remitted are pre-aggregated to comparable grain. |
| `validation.shiprocket_courier_name_normalized` | value_normalization_check | no | Courier partner grouping uses normalized values or emits a warning. |
| `validation.shiprocket_active_filter_safe` | ast_check / semantic_check | no | `is_active = true` is applied only to tables where present. |

### 20.3 Query pattern candidates

| Query pattern | Purpose | Required cards |
|---|---|---|
| Shiprocket shipment-to-invoice bridge | Identify shipments with/without freight invoice | OMS table, invoice table, AWB relationship, active-row rule |
| Shiprocket delivered COD to settlement bridge | Identify delivered COD shipments and remittance status | OMS table, settlement table, payment method value profile, COD rules |
| Shiprocket courier-level freight summary | Summarize freight by underlying courier | invoice table, courier partner value profile, freight billed metric |
| Shiprocket COD lag analysis | Measure lag from delivery to settlement | OMS table, settlement table, COD lag metric implementation |
| Shiprocket underlying courier fallback | Use Shiprocket as fallback when native courier tables are sparse | relationship candidates to direct courier tables, low-confidence caveats |
