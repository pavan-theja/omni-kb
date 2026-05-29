---
title: Delhivery Logistics Knowledge
version: 2.2-ingestion-ready
doc_type: logistics_vendor_knowledge
domain: logistics
platform: delhivery
platform_type: courier
fulfilment_ownership_models:
  - direct_courier
  - aggregator_routed
schemas:
  - zs_observe
primary_tables:
  - zs_observe.delhivery_invoice
  - zs_observe.delhivery_settlement
related_tables:
  - zs_observe.shiprocket_oms
  - zs_observe.shiprocket_invoice
  - zs_observe.shiprocket_settlement
flow_types:
  - freight_billing
  - cod_remittance
  - shipment_reconciliation
money_flow_paths:
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
  - shiprocket_logistics.md
  - logistics_reconciliation_patterns.md
---

# Delhivery Logistics Knowledge

> Scope note: This document is a reusable KB grounding document. It preserves logistics concepts, table semantics, join keys, amount meanings, and caveats. It does **not** define tenant/group ownership, customer-specific account scope, or durable marketplace routing. Tenant/group/account filters should be resolved through Business Hierarchy, Platform Account, Account Data Binding, Business Scope Set, and Runtime Scope.


## 1. How to use this document

Use this document when questions involve direct Delhivery freight invoices, Delhivery COD settlement/remittance, Delhivery AWB joins, or reconciliation between Delhivery and Shiprocket-routed evidence.

## 2. Logistics overview and business context

Delhivery can appear as a direct courier source and also as an underlying courier partner through Shiprocket. The source document includes two Delhivery table families:

```text
delhivery_invoice     = direct freight billing evidence
delhivery_settlement  = COD remittance evidence
```

Delhivery evidence should be interpreted table-by-table because similar fields may mean different things in invoice versus settlement context.

## 3. Applicability and scope model

Delhivery can support `direct_courier` flows and may also appear inside `aggregator_routed` flows. Do not infer that every Delhivery AWB belongs to the same tenant, marketplace, or account. Use Account Data Binding to filter Delhivery tables.

## 4. Fulfilment ownership and shipping model

Supported models:

```text
direct_courier
aggregator_routed, when Delhivery is the final courier assigned by an aggregator such as Shiprocket
```

## 5. Operational shipment lifecycle

Delhivery invoice records can represent delivered, RTO, and DTO lifecycle events. Settlement records focus on remittance after COD collection.

Generic flow:

```text
order / shipment
→ Delhivery AWB
→ delivered / RTO / DTO
→ freight invoice components
→ COD remittance, if COD
→ UTR / bank reference, where available
```

## 6. Money movement lifecycle

### Freight invoice

`delhivery_invoice` contains freight billing components. Important: `charged_amount` is described as declared product/order value, not freight.

Actual freight should be reconstructed from component fields such as `charge_dl`, `charge_rto`, `charge_dto`, `charge_cod`, `charge_fsc`, `charge_fs`, `charge_fov`, `charge_air`, `charge_pickup`, `charge_peak`, and taxes.

### COD remittance

`delhivery_settlement` contains COD remittance records. It includes `cod_amount`, `payable`, `remittance_number`, `utr_no`, and `settlement_date`.

`payable` may differ from `cod_amount` if deductions or net settlement logic apply.

## 7. Business objects and identifiers

| Object | Delhivery field examples |
|---|---|
| Order | `order_id` |
| Forward AWB | `forward_awb_number`, `waybill_num`, `waybill_number` |
| Reverse AWB | `return_awb_number` |
| Invoice | `invoice_number` |
| Remittance batch | `remittance_number` |
| UTR / bank bridge | `utr_no` |
| COD amount | `cod_amount` |
| Net payable | `payable` |

## 8. Table family overview

| Table | Business role | Coverage status |
|---|---|---|
| `zs_observe.delhivery_invoice` | Direct Delhivery freight invoice and lifecycle billing evidence | active in source snapshot |
| `zs_observe.delhivery_settlement` | Delhivery COD remittance / payable / UTR evidence | active with some nullable fields in source snapshot |

## 9. Entity relationships and join paths

```text
delhivery_invoice.forward_awb_number
→ shiprocket_oms.awb_code, when shipment passed through Shiprocket

delhivery_settlement.waybill_num / waybill_number
→ delhivery_invoice.forward_awb_number
→ shiprocket_oms.awb_code, where relevant

delhivery_settlement.utr_no
→ bank statement UTR/reference, via Banking KB
```

Use `waybill_num` and `waybill_number` carefully because both exist.

## 10. Metrics and business definitions

| Metric | Definition |
|---|---|
| Delhivery freight billed | Sum of reconstructed freight components from invoice table |
| Delhivery freight excluding tax | Reconstructed freight without GST |
| Delhivery tax amount | GST on Delhivery freight |
| Delivered shipment count | Count of delivered Delhivery invoice rows after status normalization |
| RTO count | Count of RTO rows |
| DTO count | Count of DTO/pickup-related rows |
| COD collected | Sum of COD amount from settlement table |
| Net payable | Sum of payable amount from settlement table |
| COD remittance gap | COD expected/collected minus payable/remitted after grain alignment |
| Delhivery remittance lag | Settlement date minus delivery/created date, depending on available evidence |
| Delhivery settlement-to-bank matched amount | Sum settlement amount with matching bank credit evidence (after Banking KB resolution) |

## 11. Reconciliation playbook

Valid Delhivery reconciliation use cases:

1. Delhivery invoice vs shipment/AWB evidence.
2. Delhivery settlement vs Delhivery invoice by AWB.
3. Delhivery settlement vs Shiprocket settlement when Delhivery appears as underlying courier.
4. Delhivery remittance vs bank credit via UTR/bank reference.
5. Freight component validation using invoice components.

### 11.1 Reconciliation variants

| Variant name | Base profile | Variant reason | Mismatch category overrides |
|---|---|---|---|
| delhivery_native_freight | `reconciliation_profile.shipment_to_invoice_reconciliation` | Native Delhivery invoice is populated; AWB-level freight reconciliation runs directly off `zs_observe.delhivery_invoice` without falling back to Shiprocket evidence. | `mismatch_category.freight_amount_mismatch`, `mismatch_category.missing_invoice` |
| delhivery_native_cod | `reconciliation_profile.cod_reconciliation` | Native Delhivery settlement table is populated and trustworthy; COD remittance can be reconciled at AWB grain without Shiprocket fallback. | `mismatch_category.cod_amount_mismatch`, `mismatch_category.missing_cod_remittance` |

## 12. Table-specific curated knowledge

### 12.1 Table: `zs_observe.delhivery_invoice`

#### Business purpose

Per-AWB freight invoice raised by Delhivery. It captures freight charges and shipment lifecycle events such as delivered, RTO, and DTO.

#### Grain

Usually one invoice/lifecycle charge row per AWB/event. Validate whether an AWB can have multiple rows for forward/RTO/DTO components.

#### Applicability and account-binding notes

The source includes account/group-like fields elsewhere, but this document should not assign customer semantics. Use Account Data Binding for selected Delhivery accounts.

#### Critical filters

- Use `is_active = true` where present.
- Use `transaction_type` to separate delivered, RTO, and DTO.
- Use `order_status` to separate Pre-paid, COD, and Pickup cases.

#### Key identifiers

| Field | Meaning |
|---|---|
| `order_id` | Merchant/order reference |
| `forward_awb_number` | Forward journey AWB |
| `return_awb_number` | Reverse journey AWB, if RTO/return |
| `invoice_number` | Delhivery invoice number |

#### Product value fields

| Field | Meaning |
|---|---|
| `charged_amount` | Declared product value, not freight |
| `cod_amount` | COD amount to be collected for COD orders |
| `order_value` | Order value |
| `product_value` | Product price/value |

#### Freight component fields

| Field | Meaning |
|---|---|
| `charge_dl` | Delivery/forward freight charge |
| `charge_rto` | RTO freight charge |
| `charge_dto` | DTO charge |
| `charge_cod` | COD collection fee |
| `charge_fsc` | Fuel surcharge |
| `charge_fs` | Freight surcharge |
| `charge_fov` | Freight on value / insurance |
| `charge_air` | Air freight charge |
| `charge_pickup` | Pickup charge |
| `charge_peak` | Peak season surcharge |
| `charge_reattempt` | Reattempt fee |
| `charge_wod` | Weekend/holiday delivery charge |

#### Tax fields

- `tax_cgst_amount`
- `tax_sgst_amount`
- `tax_igst_amount`

#### Weight and zone

- `charged_weight` is described in the source as grams, not kg. Validate data type and unit before use.
- `zone` contains zone labels such as A/B/C/D/E.

#### Computed payout fields

- `zen_vendor_payout_forward_charge`
- `zen_vendor_payout_rto_charge`
- `zen_vendor_payout_cod_charge`
- `zen_vendor_payout_dto_charge`

These can support expected freight logic if maintained and validated.

#### Status and value semantics

| transaction_type | order_status | Interpretation |
|---|---|---|
| `delivered` | Pre-paid | Prepaid order delivered; forward freight applies |
| `delivered` | COD | COD order delivered; forward freight + COD fee may apply |
| `rto` | Pre-paid | Prepaid order returned to origin; RTO charge applies |
| `rto` | COD | COD order returned; forward/RTO charges may apply |
| `dto` | Pickup | Dispatch-to-origin or pickup-related charge; validate operational meaning |

#### Relationships and joins

- `forward_awb_number` → `shiprocket_oms.awb_code`, where Delhivery shipment is represented through Shiprocket.
- `forward_awb_number` → `delhivery_settlement.waybill_num` / `waybill_number` for COD remittance checks.

#### Reconciliation role

Direct freight billing evidence. Expected side may be shipment/AWB; actual side is Delhivery freight components.

#### Caveats

- `charged_amount` is not freight.
- Reconstruct freight from components and taxes.
- Validate AWB grain before aggregating.

### 12.2 Table: `zs_observe.delhivery_settlement`

#### Business purpose

COD remittance records from Delhivery. Captures Delhivery collecting COD and remitting payable amounts to the seller/account.

#### Grain

Usually one COD remittance row per AWB or remittance record. Validate duplicates by AWB and remittance number.

#### Critical filters

- Use `is_active = true` where present.
- `txn_type = CR` indicates credit/remittance to seller in source semantics.
- Some rows may have null transaction type; treat with caution.

#### Key identifiers

| Field | Meaning |
|---|---|
| `order_id` | Merchant/order reference |
| `waybill_num` | Delhivery AWB |
| `waybill_number` | Alternate AWB field |
| `remittance_number` | Batch remittance reference |
| `utr_no` | Bank UTR / bridge to bank statement |

#### Financial fields

| Field | Meaning |
|---|---|
| `charged_amount` | Total COD/settlement amount in source context |
| `cod_amount` | COD amount collected per shipment |
| `payable` | Net payable after deductions or settlement adjustments |

#### Date and route fields

- `settlement_date`
- `created_date`
- `source_city`, `destination_city`
- `pincode`, `destination_pin`

#### Payment mode fields

- `payment_mode = QR` can indicate customer paid via QR/digital mode at delivery instead of cash.
- Null payment mode may represent cash or missing data; do not infer without profiling.

#### Relationships and joins

- `waybill_num` / `waybill_number` → `delhivery_invoice.forward_awb_number`.
- `waybill_num` → `shiprocket_settlement.awb_number` where Delhivery is visible through Shiprocket.
- `utr_no` → bank statement reference via Banking KB.

#### Reconciliation role

COD settlement/remittance evidence. Useful for COD collected vs payable, courier settlement vs Shiprocket settlement, and courier remittance-to-bank checks.

#### Caveats

- Some rows may have missing transaction type.
- `payable` can differ from `cod_amount` due to deduction/net settlement logic.
- Multiple remittance modes may appear.
- Account/group fields in source snapshots should be treated only as Account Data Binding candidates.

## 13. Mandatory query rules

- Do not use `charged_amount` in Delhivery invoice as freight.
- Reconstruct freight from charge components.
- Use AWB fields carefully: `forward_awb_number`, `waybill_num`, and `waybill_number` may all appear.
- Use `txn_type = CR` for Delhivery remittance when appropriate.
- Do not compare AWB-level settlement directly to batch-level bank credits without aggregation.
- Resolve account filters via Account Data Binding.

## 14. Data-quality and semantic caveats

- Settlement rows can have missing transaction type.
- QR payments and cash COD may coexist.
- `charged_weight` unit must be validated.
- Row counts and account IDs from source are profiling observations, not KB truth.

## 15. Supported question patterns

- Which Delhivery invoices relate to delivered/RTO/DTO shipments?
- What is the actual freight billed by Delhivery?
- Which Delhivery COD remittances have UTRs?
- Why does Delhivery `charged_amount` differ from freight?
- Which Delhivery AWBs are visible through Shiprocket?

## 16. SQL pattern appendix

```sql
-- Delhivery invoice to Shiprocket OMS AWB bridge
SELECT
  d.order_id,
  d.forward_awb_number,
  d.transaction_type,
  d.charge_dl,
  d.charge_rto,
  d.charge_cod,
  s.status,
  s.courier_company
FROM zs_observe.delhivery_invoice d
LEFT JOIN zs_observe.shiprocket_oms s
  ON d.forward_awb_number = s.awb_code
WHERE d.is_active = true
  AND s.is_active = true;
```

```sql
-- Delhivery settlement to Shiprocket settlement comparison by AWB
SELECT
  ds.waybill_num,
  ds.cod_amount AS delhivery_cod,
  ds.payable AS delhivery_payable,
  ss.charged_amount AS shiprocket_cod
FROM zs_observe.delhivery_settlement ds
LEFT JOIN zs_observe.shiprocket_settlement ss
  ON ds.waybill_num = ss.awb_number
WHERE ds.is_active = true
  AND ss.is_active = true;
```

## 17. Extraction guidance

Extract separate table, column, relationship, value profile, metric, and reconciliation cards. Preserve the critical amount semantic that Delhivery invoice `charged_amount` is product value, not freight.
---

## 18. Ingestion-ready card extraction detail

> This section is an extraction aid for the ingestion pipeline. It is still raw markdown, not canonical card YAML. Extracted cards should retain evidence references back to the relevant sections above.

### 18.1 Table card candidates

| Candidate table card | Table type | Grain | Coverage / confidence | Notes |
|---|---|---|---|---|
| `table.zs_observe.delhivery_invoice` | freight invoice ledger / shipment lifecycle evidence | Usually one invoice/lifecycle charge row per AWB or event | active, but source-period-specific | Freight must be reconstructed from components; `charged_amount` is product/order value, not freight. |
| `table.zs_observe.delhivery_settlement` | COD settlement ledger | Usually one COD remittance row per AWB or remittance record | active with nullable fields | Use `txn_type = CR` where appropriate; payable may differ from COD amount. |

### 18.2 Column card candidates — `zs_observe.delhivery_invoice`

| Column | Semantic roles | Business meaning | Metric / reconciliation usage | Caveat |
|---|---|---|---|---|
| `order_id` | identifier | Merchant/order reference | order-to-AWB traceability | Not sufficient for settlement matching alone. |
| `forward_awb_number` | identifier, join_key, reconciliation_key | Forward journey AWB | join to Shiprocket OMS and Delhivery settlement | Preferred invoice-side AWB key. |
| `return_awb_number` | identifier, join_key | Reverse/RTO journey AWB | reverse logistics and RTO analysis | Use only for reverse/RTO flows. |
| `invoice_number` | identifier | Delhivery invoice number | invoice traceability | Not shipment grain by itself. |
| `charged_amount` | measure, financial_amount | Declared product/order value | product/order value context only | Not freight. Critical semantic trap. |
| `cod_amount` | measure, financial_amount | COD amount to be collected for COD orders | COD expected/collected support | Not necessarily net payable. |
| `order_value` | measure, financial_amount | Order value | product/order value analysis | Validate relation to product value. |
| `product_value` | measure, financial_amount | Product price/value | product value analysis | Not freight. |
| `charge_dl` | measure, financial_amount | Delivery / forward freight charge | freight reconstruction | Component may be null. |
| `charge_rto` | measure, financial_amount | RTO freight charge | RTO freight metric | Use for RTO flows. |
| `charge_dto` | measure, financial_amount | DTO / pickup-related charge | DTO freight metric | Validate DTO meaning before use. |
| `charge_cod` | measure, financial_amount | COD collection fee | COD fee component | Not COD collected/remitted. |
| `charge_fsc` | measure, financial_amount | Fuel surcharge | freight component | Component may be null. |
| `charge_fs` | measure, financial_amount | Freight surcharge | freight component | Component may be null. |
| `charge_fov` | measure, financial_amount | Freight-on-value / insurance charge | freight component | Component may be null. |
| `charge_air` | measure, financial_amount | Air freight charge | freight component | Component may be null. |
| `charge_pickup` | measure, financial_amount | Pickup charge | freight component | Component may be null. |
| `charge_peak` | measure, financial_amount | Peak season surcharge | freight component | Component may be null. |
| `charge_reattempt` | measure, financial_amount | Reattempt fee | failed delivery/NDR cost | Component may be null. |
| `charge_wod` | measure, financial_amount | Weekend/holiday delivery charge | freight component | Component may be null. |
| `tax_cgst_amount` | measure, financial_amount | CGST amount on freight/charges | tax component | Include only when tax-inclusive metric is needed. |
| `tax_sgst_amount` | measure, financial_amount | SGST amount on freight/charges | tax component | Include only when tax-inclusive metric is needed. |
| `tax_igst_amount` | measure, financial_amount | IGST amount on freight/charges | tax component | Include only when tax-inclusive metric is needed. |
| `charged_weight` | measure | Charged/billable weight; source describes grams | weight validation and freight audit | Unit must be validated before rate-card comparison. |
| `zone` | dimension, value_profile | Delivery zone label such as A/B/C/D/E | zone-wise freight analysis | Requires rate-card context for overcharge logic. |
| `zen_vendor_payout_forward_charge` | measure, financial_amount | System-computed expected forward charge | expected freight validation | Use only if maintained and validated. |
| `zen_vendor_payout_rto_charge` | measure, financial_amount | System-computed expected RTO charge | expected RTO freight validation | Use only if maintained and validated. |
| `zen_vendor_payout_cod_charge` | measure, financial_amount | System-computed expected COD fee | expected COD fee validation | Not COD collected/remitted. |
| `zen_vendor_payout_dto_charge` | measure, financial_amount | System-computed expected DTO charge | expected DTO validation | Validate DTO semantics. |
| `transaction_type` | dimension, status, value_profile | Lifecycle/billing type such as delivered, rto, dto | delivered/RTO/DTO classification | Use with `order_status`. |
| `order_status` | dimension, status, value_profile | Payment/order status such as Pre-paid, COD, Pickup | payment-mode and lifecycle classification | Values require normalization. |
| `is_active` | filter | Active/current row indicator | mandatory filter where present | Apply only if column exists. |

### 18.3 Column card candidates — `zs_observe.delhivery_settlement`

| Column | Semantic roles | Business meaning | Metric / reconciliation usage | Caveat |
|---|---|---|---|---|
| `order_id` | identifier | Merchant/order reference | traceability | Use AWB/remittance for settlement matching. |
| `waybill_num` | identifier, join_key, reconciliation_key | Delhivery AWB | primary join to invoice and Shiprocket settlement | Validate against `waybill_number`. |
| `waybill_number` | identifier, join_key, reconciliation_key | Alternate Delhivery AWB field | fallback/alternate join key | Use coalescing only after profiling. |
| `remittance_number` | identifier, batch_key | Batch remittance reference | batch-to-bank matching | Bank match may be batch-level. |
| `utr_no` | identifier, bank_bridge | Bank UTR / payment reference | bridge to bank statement | Bank semantics live in Banking KB. |
| `charged_amount` | measure, financial_amount | Total COD/settlement amount in settlement context | COD collected/settlement analysis | Not invoice freight. |
| `cod_amount` | measure, financial_amount | COD amount collected per shipment | COD collected metric | May differ from payable. |
| `payable` | measure, financial_amount | Net payable after deductions or settlement adjustments | COD remitted/net payable metric | Compare to `cod_amount` carefully. |
| `settlement_date` | date | Settlement/remittance date | remittance reporting and lag | Required for lag analysis. |
| `created_date` | date | Record creation date | fallback reporting date | Do not use as settlement date if `settlement_date` exists. |
| `source_city` | dimension | Origin/source city | route-level analysis | Optional dimension. |
| `destination_city` | dimension | Destination city | route-level analysis | Optional dimension. |
| `pincode` | dimension | Destination/source pincode depending on source context | geography analysis | Confirm meaning before grouping. |
| `destination_pin` | dimension | Destination pincode | geography analysis | Prefer over generic `pincode` if confirmed. |
| `payment_mode` | dimension, value_profile | Payment mode such as QR/cash/null | COD/digital-at-delivery classification | Null should not be blindly treated as cash. |
| `txn_type` | dimension, status, value_profile | Transaction type; `CR` indicates credit/remittance in source semantics | remittance filtering | Null transaction type requires caution. |
| `is_active` | filter | Active/current row indicator | mandatory filter where present | Apply only if column exists. |

### 18.4 Relationship card candidates

| Candidate relationship | Source table / column | Target table / column | Type | Cardinality expectation | Safe for | Caveats |
|---|---|---|---|---|---|---|
| `relationship.delhivery_invoice.delhivery_settlement.forward_awb` | `delhivery_invoice.forward_awb_number` | `delhivery_settlement.waybill_num` / `waybill_number` | invoice_to_cod_settlement | one-to-zero-or-many | COD and freight reconciliation | COD settlement may be absent for prepaid shipments. |
| `relationship.shiprocket_oms.delhivery_invoice.awb` | `shiprocket_oms.awb_code` | `delhivery_invoice.forward_awb_number` | aggregator_to_direct_courier_invoice | candidate | courier cross-check | Use when Delhivery is final courier under Shiprocket. |
| `relationship.shiprocket_settlement.delhivery_settlement.awb` | `shiprocket_settlement.awb_number` | `delhivery_settlement.waybill_num` | aggregator_to_direct_courier_settlement | candidate | COD settlement cross-check | Requires courier partner alignment and grain validation. |
| `relationship.delhivery_settlement.bank_statement.utr` | `delhivery_settlement.utr_no` | bank statement reference/UTR | courier_remittance_to_bank | candidate | bank reconciliation | Requires Banking KB and selected bank account scope. |
| `relationship.delhivery_invoice.shiprocket_invoice.awb` | `delhivery_invoice.forward_awb_number` | `shiprocket_invoice.other_id` | direct_courier_to_aggregator_invoice | diagnostic | freight cross-check | Amount semantics may differ; do not subtract directly without normalization. |

### 18.5 Value profile candidates

| Candidate value profile | Column | Values / patterns to preserve | Business meaning | Extraction note |
|---|---|---|---|---|
| `value_profile.delhivery_invoice.transaction_type` | `delhivery_invoice.transaction_type` | `delivered`, `rto`, `dto` | lifecycle / billing event classification | Normalize case and pair with `order_status`. |
| `value_profile.delhivery_invoice.order_status` | `delhivery_invoice.order_status` | `Pre-paid`, `COD`, `Pickup` | payment/lifecycle context | Use for COD fee and pickup/DTO classification. |
| `value_profile.delhivery_invoice.zone` | `delhivery_invoice.zone` | A/B/C/D/E-like labels | freight zone | Rate-card semantics external to this doc. |
| `value_profile.delhivery_settlement.txn_type` | `delhivery_settlement.txn_type` | `CR`, null/other | credit/remittance indicator | Use `CR` where appropriate; null requires warning. |
| `value_profile.delhivery_settlement.payment_mode` | `delhivery_settlement.payment_mode` | `QR`, null/other | customer paid via QR/digital mode or missing/cash-like values | Do not infer null = cash without profiling. |

---

## 19. Metric and metric implementation extraction detail

### 19.1 Metric implementation candidates

| Metric | Candidate implementation | Base table(s) | Formula / logic | Grain | Required columns | Caveats |
|---|---|---|---|---|---|---|
| Delhivery freight billed | Reconstructed Delhivery freight | `delhivery_invoice` | Sum freight components: delivery/RTO/DTO/COD fee/fuel/FOV/air/pickup/peak/reattempt/WOD plus taxes if tax-inclusive metric is requested | AWB / invoice row | freight component columns, tax columns | Do not use `charged_amount` as freight. |
| Delhivery freight excluding tax | Reconstructed freight without GST | `delhivery_invoice` | Sum charge components excluding tax fields | AWB / invoice row | `charge_dl`, `charge_rto`, `charge_dto`, `charge_cod`, etc. | Requires component null handling. |
| Delhivery tax amount | GST on Delhivery freight | `delhivery_invoice` | `SUM(COALESCE(tax_cgst_amount,0)+COALESCE(tax_sgst_amount,0)+COALESCE(tax_igst_amount,0))` | invoice row | tax fields | Use only when tax fields are populated. |
| Delivered shipment count | Count delivered rows/AWBs | `delhivery_invoice` | Count distinct `forward_awb_number` where normalized `transaction_type = delivered` | AWB | `forward_awb_number`, `transaction_type` | Validate whether multiple delivered rows per AWB exist. |
| RTO count | Count RTO rows/AWBs | `delhivery_invoice` | Count distinct AWB where normalized `transaction_type = rto` | AWB | `forward_awb_number`, `return_awb_number`, `transaction_type` | Use return AWB for reverse route analysis. |
| DTO count | Count DTO/pickup rows | `delhivery_invoice` | Count distinct AWB/order where `transaction_type = dto` or order status indicates pickup | AWB/order | `transaction_type`, `order_status` | DTO meaning must be validated. |
| COD collected | Sum COD amount from settlement | `delhivery_settlement` | `SUM(cod_amount)` after active and `txn_type = CR` filtering where appropriate | AWB/remittance | `cod_amount`, `txn_type`, `waybill_num` | May differ from payable. |
| Net payable | Sum payable from settlement | `delhivery_settlement` | `SUM(payable)` after remittance filtering | AWB/remittance | `payable`, `txn_type` | Represents net payable/remitted context. |
| COD remittance gap | COD amount minus payable | `delhivery_settlement` | `SUM(cod_amount) - SUM(payable)` after grain alignment | AWB/remittance | `cod_amount`, `payable` | Interpret as deductions/net settlement difference, not always leakage. |
| Delhivery remittance lag | Settlement date minus delivery/created date | `delhivery_invoice` + `delhivery_settlement` | Date difference between delivery evidence and `settlement_date` | AWB | `forward_awb_number`, `waybill_num`, `settlement_date`, delivery date if available | Use delivery date if available; otherwise treat created date as fallback with warning. |
| Delhivery settlement to bank matched amount | Sum remittance amount matched to bank | `delhivery_settlement` + Banking KB | Match `utr_no` / remittance reference to bank credit and sum matched amount | remittance/UTR | `utr_no`, `payable`, bank reference | Requires Banking KB and bank account scope. |

### 19.2 Formula template candidates

| Formula template | Applies to | Plain-English formula | Notes |
|---|---|---|---|
| `formula_template.sum_component_amounts` | Delhivery freight billed | Sum a list of component charge fields, optionally plus taxes | Must handle null components as zero. |
| `formula_template.count_distinct_identifier` | delivered/RTO/DTO counts | Count distinct AWB/order identifiers after value filtering | Requires duplicate handling. |
| `formula_template.sum_financial_amount` | COD collected, net payable, tax amount | Sum the relevant amount after semantic validation | Amount semantics are table-specific. |
| `formula_template.gap_amount` | COD remittance gap | Expected/collected amount minus payable/remitted amount after grain alignment | Must not imply leakage by default. |
| `formula_template.lag_days` | remittance lag | Settlement date minus delivery/created date | Date choice must be explicit. |

---

## 20. Rule and validation extraction detail

### 20.1 Rule candidates

| Rule | Rule type | Severity | Statement | Applies to |
|---|---|---:|---|---|
| Delhivery invoice `charged_amount` is not freight | metric_semantics | critical | Do not use `charged_amount` from `delhivery_invoice` as freight billed. | Delhivery invoice metrics |
| Reconstruct Delhivery freight from components | metric_semantics | high | Freight billed should be reconstructed from charge component fields and taxes as needed. | freight metrics |
| Use Account Data Binding for Delhivery filters | scope_filter | critical | Do not infer tenant/account filters from vendor docs or profiling observations. | all Delhivery tables |
| Normalize AWB fields | join_safety | high | `forward_awb_number`, `waybill_num`, and `waybill_number` should be normalized before joining. | invoice-settlement relationships |
| Use `txn_type = CR` carefully | semantic_filter | medium | Use `txn_type = CR` for remittance credit filtering where appropriate, but treat null transaction type with caution. | settlement queries |
| Do not infer null payment mode as cash | value_semantics | medium | Null payment mode may mean missing data, not necessarily cash COD. | settlement payment mode |
| Validate charged weight unit | data_quality | medium | Source describes `charged_weight` as grams; confirm unit before rate-card analysis. | weight/rate-card metrics |
| Align grain before bank matching | aggregation_safety | critical | Aggregate settlement rows to remittance/UTR grain before comparing to bank credits. | bank reconciliation |
| Use Shiprocket relationships only when Delhivery is final courier | applicability | high | Join Delhivery to Shiprocket only when evidence indicates Delhivery is the underlying courier. | cross-platform courier checks |

### 20.2 Validation test candidates

| Validation test | Test type | Blocking? | Validates |
|---|---|---:|---|
| `validation.delhivery_freight_not_charged_amount` | semantic_check | yes | Freight metric does not use `delhivery_invoice.charged_amount` as freight. |
| `validation.delhivery_freight_components_present` | column_check | yes | Freight implementation uses available charge component fields. |
| `validation.delhivery_scope_filter_from_binding` | semantic_check | yes | Account filters are injected from Account Data Binding. |
| `validation.delhivery_awb_join_normalized` | join_check | yes | Joins use normalized AWB fields across invoice/settlement/Shiprocket. |
| `validation.delhivery_txn_type_null_handled` | semantic_check | no | Null `txn_type` rows are either excluded with reason or classified as unknown. |
| `validation.delhivery_payment_mode_null_not_cash` | semantic_check | no | Null payment mode is not treated as cash without profiling. |
| `validation.delhivery_bank_match_grain` | grain_check | yes | Settlement is aggregated to remittance/UTR grain before bank matching. |
| `validation.delhivery_weight_unit_warning` | data_quality_check | no | Rate-card analysis warns that weight unit must be validated. |

### 20.3 Query pattern candidates

| Query pattern | Purpose | Required cards |
|---|---|---|
| Delhivery freight reconstruction | Reconstruct freight from invoice charge components | Delhivery invoice table, freight component columns, freight rules |
| Delhivery invoice to settlement bridge | Compare invoice AWBs to settlement AWBs | invoice table, settlement table, AWB relationship |
| Delhivery COD payable analysis | Compare COD amount and payable | settlement table, COD collected and payable metrics |
| Delhivery remittance to bank bridge | Match UTR/remittance to bank credits | settlement table, `utr_no`, Banking KB, bank scope |
| Delhivery through Shiprocket cross-check | Compare Delhivery native evidence to Shiprocket evidence | Shiprocket and Delhivery relationships, courier normalization rule |
| Delhivery RTO/DTO cost analysis | Analyze RTO and DTO charges | invoice table, transaction_type value profile, charge_rto and charge_dto columns |
