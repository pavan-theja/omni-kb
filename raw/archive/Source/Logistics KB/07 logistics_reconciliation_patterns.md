---
title: Logistics Reconciliation Patterns
version: 2.2
doc_type: logistics_reconciliation_patterns
domain: logistics
business_processes:
  - logistics_order_reconciliation
  - logistics_shipment_reconciliation
  - logistics_freight_reconciliation
  - logistics_cod_reconciliation
  - logistics_batch_settlement_reconciliation
money_flow_paths:
  - order_to_shipment
  - shipment_to_freight_invoice
  - cod_delivery_to_courier_remittance
  - courier_remittance_to_bank
  - marketplace_fulfilment_to_settlement
status: draft
owner: finance_data_team
source_documents:
  - Logistics KB Doc.docx
related_docs:
  - logistics_domain_overview.md
  - shiprocket_logistics.md
  - delhivery_logistics.md
  - dtdc_logistics.md
  - xpressbees_logistics.md
  - ekart_logistics.md
  - shadowfax_ecom_logistics.md
---

# Logistics Reconciliation Patterns

> Scope note: This document is a reusable KB grounding document. It preserves logistics concepts, table semantics, join keys, amount meanings, and caveats. It does **not** define tenant/group ownership, customer-specific account scope, or durable marketplace routing. Tenant/group/account filters should be resolved through Business Hierarchy, Platform Account, Account Data Binding, Business Scope Set, and Runtime Scope.

> Curation note: Any row counts, profiling periods, group IDs, merchant IDs, bank names, marketplace names, or tenant references from source material must be treated as source-snapshot observations only. They should not become durable KB grounding unless represented through Tenant / Group Context or Account Data Binding documents.


## 1. How to use this document

Use this document for cross-vendor logistics reconciliation: order-to-shipment, shipment-to-invoice, freight charge validation, COD collection/remittance, and courier batch-to-bank bridge.

This document defines generic matching logic and mismatch categories. It should not decide tenant/group/account filters or hardcode row counts, periods, marketplace ownership, or bank account ownership.

## 2. Overview

Logistics reconciliation connects operational shipment evidence to money evidence.

The generic chain is:

```text
order / OMS
→ shipment / AWB
→ courier invoice / freight bill
→ COD settlement / courier remittance
→ settlement batch / UTR / bank reference
→ bank credit
```

Not every vendor supports every step. Missing evidence is a first-class reconciliation outcome.

## 3. Applicability and scope model

Before running reconciliation:

1. Resolve tenant/group/platform/account runtime scope.
2. Retrieve Account Data Bindings for all selected tables.
3. Retrieve vendor docs for each participating evidence source.
4. Select the correct reconciliation level.
5. Align grain before matching.

Do not infer account filters from table docs or vendor docs.

## 4. Business objects

| Object | Reconciliation role |
|---|---|
| Order | Source demand/commercial record |
| Shipment | Physical fulfilment record |
| AWB / waybill / tracking ID | Primary shipment reconciliation unit |
| Freight invoice | Actual freight billing evidence |
| COD expected | Amount expected to be collected on COD delivery |
| COD settlement/remittance | Courier/aggregator evidence of COD remitted |
| Settlement batch | Aggregated transfer unit |
| UTR / bank reference | Bridge from settlement/remittance to bank |
| Bank credit | Actual cash received in bank |

## 5. Expected side

Expected side varies by reconciliation level:

| Level | Expected side |
|---|---|
| Order to shipment | Order/OMS record |
| Shipment to invoice | Shipment/AWB record |
| Freight charge | Expected freight from rate card/shipment attributes |
| COD reconciliation | Delivered COD order/shipment |
| Courier batch to bank | Courier settlement batch/remittance |

## 6. Actual side

Actual side varies by level:

| Level | Actual side |
|---|---|
| Order to shipment | Shipment/AWB evidence |
| Shipment to invoice | Freight invoice/courier bill |
| Freight charge | Actual freight invoice components |
| COD reconciliation | Courier/aggregator settlement/remittance |
| Courier batch to bank | Bank statement credit |

## 7. Primary reconciliation unit

Use the most precise unit available:

```text
order ID
shipment/package ID
AWB / waybill / tracking ID
invoice number
settlement/remittance number
UTR / bank reference
amount + account + date window fallback
```

Preferred unit by level:

| Level | Primary unit |
|---|---|
| Order to shipment | order ID + shipment/package ID if available |
| Shipment to invoice | AWB / waybill / tracking ID |
| Freight charge | AWB + charge component grain |
| COD reconciliation | AWB for shipment-level COD; batch/UTR for bank-level matching |
| Courier batch to bank | UTR / bank reference / batch ID |

## 8. Secondary and fallback keys

Fallback keys are allowed but should lower confidence.

| Fallback | Use when | Caveat |
|---|---|---|
| amount + date window | reference missing | risk of false matches |
| courier partner + AWB | vendor reference inconsistent | requires courier name normalization |
| order ID parsed from composite key | integration-specific composite order ID exists | parsing must be validated |
| bank narration text search | UTR not cleanly stored | needs Banking KB narration rules |
| batch amount + settlement date | UTR missing | many-to-one/one-to-many risk |

## 9. Canonical join path

```text
order_id
→ shipment_id / package_id
→ AWB / waybill / tracking ID
→ invoice reference
→ settlement/remittance reference
→ UTR / bank reference
→ bank credit
```

Source-specific field examples:

| Generic key | Table/field examples |
|---|---|
| Shiprocket AWB | `shiprocket_oms.awb_code`, `shiprocket_invoice.other_id`, `shiprocket_settlement.awb_number` |
| Delhivery AWB | `delhivery_invoice.forward_awb_number`, `delhivery_settlement.waybill_num`, `waybill_number` |
| DTDC AWB | `dtdc_settlement.airwaybill_number` |
| Ekart AWB | `ekart_settlement.shipment_id`, `tracking_id` |
| XpressBees AWB | `xpressbees_settlement.shipping_id`, when populated |
| Bank bridge | `utr_no`, `bank_reference_no`, `bank_ref_number`, `remittance_number`, `settlement_id` |

## 10. Level 1 — Order to shipment reconciliation

### Purpose

Verify that orders from marketplace, D2C, or channel systems have corresponding shipment/AWB evidence.

### Expected side

Order/OMS table from marketplace, channel, Shopify, ERP, or custom source.

### Actual side

Shipment table such as Shiprocket OMS, marketplace fulfilment shipment table, direct courier operational table, or platform fulfilment evidence.

### Primary unit

Order ID plus shipment/package ID where available. AWB can be used once assigned.

### Matching logic

```text
order_id from source system
→ shipment order reference or composite order ID
→ AWB/tracking ID
```

### Mismatch categories

- order missing shipment,
- shipment without source order,
- duplicate shipment for one order,
- shipment generated late,
- cancelled order still shipped,
- order ID parsing failure.

### Caveats

Composite order IDs should be parsed only when source-specific pattern is confirmed.

## 11. Level 2 — Shipment to invoice reconciliation

### Purpose

Verify that shipped AWBs have freight invoice evidence.

### Expected side

Shipment/AWB movement evidence.

### Actual side

Freight invoice/courier bill.

### Primary unit

AWB / waybill / tracking ID.

### Matching logic

Examples:

```text
shiprocket_oms.awb_code → shiprocket_invoice.other_id
shiprocket_oms.awb_code → delhivery_invoice.forward_awb_number
```

### Mismatch categories

- shipment missing freight invoice,
- invoice without shipment,
- duplicate invoice for one AWB,
- freight amount mismatch,
- wrong courier partner,
- wrong zone/weight,
- invoice table empty/schema-only.

### Caveats

Do not treat settlement-only vendors as having freight invoice evidence. For DTDC and Ekart, source invoice tables are schema-only/empty in the attached doc.

## 12. Level 3 — Freight charge reconciliation

### Purpose

Validate actual freight charged against expected freight based on courier/rate-card/shipment characteristics.

### Expected side

Rate-card or computed expected freight based on weight, zone, service type, COD flag, RTO/DTO status, and taxes.

### Actual side

Freight invoice components.

### Component fields

Examples:

```text
charge_dl
charge_rto
charge_dto
charge_cod
charge_fsc
charge_fs
charge_fov
charge_air
charge_pickup
charge_peak
tax_cgst_amount
tax_sgst_amount
tax_igst_amount
total_tax
```

### Mismatch categories

- freight overcharge,
- RTO charge on non-RTO shipment,
- COD fee on prepaid shipment,
- zone mismatch,
- weight mismatch,
- tax mismatch,
- missing component,
- charged amount interpreted incorrectly.

### Caveats

Do not infer freight from `charged_amount` without table context. In Delhivery invoice it is product value; in Shiprocket invoice it is freight bill; in settlement tables it can be COD/remittance amount.

## 13. Level 4 — COD reconciliation

### Purpose

Validate expected COD against courier-collected and courier-remitted amounts.

### Expected side

Delivered COD shipment/order and expected COD amount.

### Actual side

Courier/aggregator COD settlement/remittance row.

### Primary unit

AWB for shipment-level matching.

### Matching examples

```text
shiprocket_oms.awb_code → shiprocket_settlement.awb_number
shiprocket_oms.awb_code → delhivery_settlement.waybill_num
shiprocket_oms.awb_code → dtdc_settlement.airwaybill_number
shiprocket_oms.awb_code → ekart_settlement.shipment_id / tracking_id
shiprocket_settlement.courier_partner = XpressBees-style label as fallback for sparse XpressBees native table
```

### Mismatch categories

- delivered COD not remitted,
- COD expected differs from COD remitted,
- remittance delayed,
- payable lower than COD due to deductions,
- missing AWB in settlement,
- native courier settlement low confidence,
- COD vs POS/prepaid transaction confusion.

### Caveats

COD lag is source- and account-specific. Do not hardcode a universal lag from one profiling snapshot.

## 14. Level 5 — Courier batch to bank reconciliation

### Purpose

Match courier/aggregator remittance batches to actual bank credits.

### Expected side

Courier settlement batch, remittance number, UTR, bank reference, or settlement amount.

### Actual side

Bank statement credit.

### Primary unit

UTR / bank reference / remittance number / settlement ID.

### Fallback unit

Amount + bank account + date window + narration search.

### Matching examples

```text
delhivery_settlement.utr_no → bank statement UTR/reference
dtdc_settlement.utr_no / bank_ref_number → bank statement reference
ekart_settlement.bank_reference_no / settlement_id → bank statement reference
shiprocket settlement/remittance fields → bank statement reference, when populated
```

### Mismatch categories

- courier settlement batch has no bank credit,
- bank credit has no courier settlement detail,
- batch amount differs from sum of AWB settlements,
- missing/malformed UTR,
- split bank credit,
- merged bank credit,
- delayed bank credit,
- bank account out of scope.

### Caveats

Bank statement semantics live in Banking KB. Logistics docs provide only the bridge fields. Always resolve the selected bank account via Account Data Binding.

## 15. Mismatch categories

| Category | Meaning |
|---|---|
| `missing_shipment` | Source order has no shipment/AWB evidence |
| `orphan_shipment` | Shipment exists without source order |
| `missing_invoice` | Shipment/AWB has no freight invoice |
| `orphan_invoice` | Freight invoice has no matching shipment |
| `freight_amount_mismatch` | Actual freight differs from expected freight |
| `missing_cod_remittance` | Delivered COD shipment has no settlement/remittance evidence |
| `cod_amount_mismatch` | COD expected differs from COD remitted |
| `delayed_remittance` | Settlement/remittance appears after expected window |
| `missing_bank_credit` | Remittance/batch has no bank credit evidence |
| `unidentified_bank_credit` | Bank credit cannot be matched to courier remittance |
| `low_confidence_native_data` | Native vendor data too sparse for confident reconciliation |
| `schema_only_source` | Table exists but has no usable data |
| `grain_mismatch` | AWB-level and batch-level data compared without aggregation |

## 16. Mandatory rules

- Always apply Account Data Binding filters for selected accounts and tables.
- Do not use vendor docs to infer tenant/group scope.
- Use AWB/waybill/tracking ID for shipment-level matching where available.
- Aggregate AWB-level settlement to batch/UTR before matching bank credits.
- Do not interpret `charged_amount` without table context.
- Treat empty invoice/report tables as schema-only.
- Treat sparse native sources as low confidence and use documented fallback where appropriate.
- Separate COD from POS/prepaid settlement rows.
- Use Banking KB for bank statement narration and bank-credit semantics.

## 17. Data-quality caveats

- Row counts and periods from the attached source are profiling snapshots.
- Group IDs and merchant IDs in source examples are not universal business semantics.
- Some tables may be partially populated depending on vendor, period, or account.
- Courier partner labels need normalization.
- AWB fields can be null in native settlement tables.
- Batch-level fields may repeat across shipment rows.

## 18. Example questions

- Which delivered COD shipments have no courier remittance?
- Which shipments have no freight invoice?
- Which courier batches have no bank credit?
- Which vendor data should be treated as low confidence?
- Which AWBs have freight overcharges?
- Which settlement rows are COD versus POS/prepaid?
- Which courier remittances have malformed or missing UTRs?

## 19. Extraction guidance

Expected cards:

```text
Reconciliation Profile
Reconciliation Side
Reconciliation Unit
Matching Logic
Mismatch Category
Rule
Validation Test
Output Contract
Query Pattern
```

Do not extract tenant/account-specific mappings from these reconciliation patterns. Those come from Account Data Binding and runtime scope.

---

## 20. Ingestion-compatible enrichment sections

This section is intentionally written as **raw markdown for KB grounding**, not as final card YAML. The ingestion pipeline can use it to extract candidate cards, edges, rules, validations, and query patterns.

The content below should be treated as reusable logistics reconciliation knowledge. It should not be used to infer tenant ownership, marketplace ownership, group/account scope, bank account ownership, or durable row-count coverage.

---

## 20.1 Column-level information candidates

These are reusable column families that commonly appear across logistics reconciliation sources. Actual physical column names must be resolved from the relevant vendor table document.

### Identifier columns

| Column concept | Business meaning | Semantic roles | Usage guidance | Caveats |
|---|---|---|---|---|
| `source_order_id` | Order identifier from marketplace, D2C, OMS, ERP, or channel system | identifier, join_key, reconciliation_key | Use for order-to-shipment matching | May be embedded in composite keys; parsing must be source-specific |
| `shipment_id` / `package_id` | Shipment or package identifier created during fulfilment | identifier, join_key | Use when one order can split into multiple shipments | Not always equivalent to AWB |
| `awb_number` / `waybill_number` / `tracking_id` | Carrier-level shipment reference | identifier, join_key, reconciliation_key | Primary unit for shipment-to-invoice and COD remittance matching | Normalize case, spacing, prefixes, and null handling |
| `invoice_number` / `bill_number` | Freight invoice or courier bill reference | identifier, reconciliation_key | Use for freight invoice traceability | May be batch-level, not AWB-level |
| `settlement_id` / `remittance_number` | Courier settlement/remittance reference | identifier, reconciliation_key | Use for COD settlement and batch-level reconciliation | May repeat across multiple AWBs |
| `utr_no` / `bank_reference_no` | Bank transfer bridge reference | identifier, reconciliation_key | Use for settlement-to-bank matching | Missing/malformed values should lower confidence |
| `courier_partner` / `courier_company` | Final courier or logistics partner label | dimension, filter, value_profile_candidate | Use to segment vendor/final courier evidence | Labels require normalization; aggregator label and final courier label may differ |

### Operational status columns

| Column concept | Business meaning | Semantic roles | Usage guidance | Caveats |
|---|---|---|---|---|
| `shipment_status` | Current shipment lifecycle status | status, dimension, filter | Use for shipped/delivered/RTO/return segmentation | Values differ by vendor and must be value-profiled |
| `delivery_status` | Delivery outcome | status, dimension, filter | Use for delivery success and COD eligibility | Do not infer COD remittance from delivery alone |
| `rto_status` | Return-to-origin lifecycle state | status, dimension, filter | Use for RTO metrics and reverse freight checks | RTO and customer return are different concepts |
| `return_status` | Customer return or reverse pickup state | status, dimension, filter | Use for reverse logistics reconciliation | May involve different courier than forward shipment |
| `payment_mode` / `service_type` | COD, prepaid, POS, or service mode | dimension, filter, value_profile_candidate | Required for COD vs prepaid/POS separation | Do not treat null as prepaid or COD by default |

### Financial amount columns

| Column concept | Business meaning | Semantic roles | Default aggregation | Usage guidance | Caveats |
|---|---|---|---|---|---|
| `cod_expected_amount` | COD amount expected from order/shipment | measure, financial_amount | SUM | Expected side for COD reconciliation | Should be limited to delivered COD shipments where relevant |
| `cod_collected_amount` | COD amount collected by courier | measure, financial_amount | SUM | Operational cash collection evidence | May not equal amount remitted |
| `cod_remitted_amount` | COD amount remitted by courier/aggregator | measure, financial_amount | SUM | Actual side for COD remittance reconciliation | May be AWB-level or batch-level depending on source |
| `freight_billed_amount` | Freight charged by courier/vendor | measure, financial_amount | SUM | Actual side for shipment-to-invoice and freight charge reconciliation | Do not infer from generic `charged_amount` without table context |
| `expected_freight_amount` | Computed/rate-card expected freight | measure, financial_amount | SUM | Expected side for freight charge validation | Requires rate-card or business-rule source |
| `payable_amount` | Net amount payable/remitted after deductions | measure, financial_amount | SUM | Use for settlement/remittance analysis | May include deductions; not always raw COD collected |
| `settlement_batch_amount` | Total batch/remittance amount | measure, financial_amount | SUM or latest per batch | Use for settlement-to-bank matching | Avoid double counting repeated batch values across AWB rows |
| `tax_amount` / `gst_amount` | Tax component on freight or settlement | measure, financial_amount | SUM | Use for GST/tax reconciliation | Clarify whether included in total freight or separate |

### Date columns

| Column concept | Business meaning | Semantic roles | Usage guidance | Caveats |
|---|---|---|---|---|
| `order_date` | Date order was created | date, filter | Use for order cohorting | Not shipment or settlement date |
| `shipment_created_date` | Date shipment/AWB was created | date, filter | Use for shipment creation SLA | May be absent for settlement-only vendors |
| `delivered_date` | Date shipment was delivered | date, filter, reconciliation_window | Use for COD eligibility and delivery-to-remittance lag | Delivery does not imply remittance |
| `invoice_date` | Date freight invoice was generated | date, filter | Use for freight invoice period | Not necessarily shipment date |
| `settlement_date` / `remittance_date` | Date courier settlement/remittance was created | date, filter, reconciliation_window | Use for COD remittance and settlement aging | May differ from bank credit date |
| `bank_credit_date` | Date amount was credited in bank | date, filter | Use only from Banking KB / bank statement table | Logistics docs should not define bank statement semantics |

### Scope/account columns

| Column concept | Business meaning | Semantic role | Usage guidance | Caveat |
|---|---|---|---|---|
| `group_level_id` | Source/account scoping key in some tables | filter, account_binding_candidate | Use only through Account Data Binding | Do not assign tenant/group meaning inside this reconciliation doc |
| `merchant_id` / `seller_id` / `account_id` | Platform/source account identifier | filter, account_binding_candidate | Use only through Account Data Binding | Not reusable across platforms or tables |
| `bank_account_id` | Bank account scoping key | filter, account_binding_candidate | Use from Banking KB / Account Data Binding | Bank name is not enough to identify bank account |

---

## 20.2 Relationship candidates

Relationship candidates describe reusable join paths. They are not tenant/account routing rules.

| Relationship candidate | Source side | Target side | Preferred key | Join type guidance | Grain risk |
|---|---|---|---|---|---|
| `relationship.order_to_shipment` | Order/OMS | Shipment/AWB evidence | order ID, shipment ID, package ID | left join from orders when finding missing shipments | One order can split into multiple shipments |
| `relationship.shipment_to_freight_invoice` | Shipment/AWB | Freight invoice/courier bill | AWB / waybill / tracking ID | left join from shipment when checking missing invoice | Invoice may have multiple charge rows per AWB |
| `relationship.shipment_to_cod_settlement` | Delivered COD shipment | Courier COD settlement/remittance | AWB / waybill / tracking ID | left join from delivered COD shipments | Settlement may be batch-level or delayed |
| `relationship.settlement_to_bank_bridge` | Courier settlement/remittance | Bank statement credit | UTR / bank reference / settlement ID | left/full join for reconciliation | Bank credit may be split, merged, delayed, or narration-only |
| `relationship.freight_component_to_invoice_total` | Freight component rows | Invoice total | invoice number, AWB | aggregate components before compare | Component-level rows can double count total |
| `relationship.aggregator_to_final_courier` | Aggregator shipment table | Final courier evidence | AWB + courier partner | use only when source documents confirm relationship | Aggregator and final courier may not have one-to-one native evidence |
| `relationship.native_vendor_to_aggregator_fallback` | Native low-confidence vendor table | Aggregator table | AWB + courier partner | use as fallback, not default truth | Fallback is valid only when runtime scope includes aggregator-routed evidence |

Relationship extraction should preserve the caveat that structural joinability does not equal tenant/group applicability.

---

## 20.3 Value profile candidates

These value profiles should be extracted where the physical columns exist in vendor docs.

### Payment mode / service type

| Raw value family | Business meaning | Category | Metric usage | Caveat |
|---|---|---|---|---|
| COD | Cash-on-delivery shipment or settlement | cod | Use for COD expected, COD remitted, COD gap, COD lag | Confirm value comes from payment/service column, not free text |
| Prepaid | Prepaid shipment/order | prepaid | Exclude from COD metrics; include in delivery/freight metrics | Prepaid may still have logistics settlement rows |
| POS | POS/digital settlement row in some fulfilment/logistics data | prepaid_or_pos_settlement | Analyze separately from COD | Do not merge with COD remittance |
| Unknown/null | Missing payment mode | unknown | Exclude from payment-mode-specific metrics unless explicitly handled | Do not infer COD/prepaid from null |

### Shipment lifecycle status

| Raw value family | Business meaning | Category | Metric usage | Caveat |
|---|---|---|---|---|
| Shipped / In Transit | Shipment is moving | in_transit | Shipment count, aging | Not delivery success |
| Delivered | Shipment delivered to customer | delivered | Delivery count, delivery success rate, COD eligibility | Delivered COD still needs settlement/remittance check |
| RTO / RTO Delivered | Returned to origin | rto | RTO count, RTO rate, reverse freight | Not same as customer return |
| Returned / Return Delivered | Customer return/reverse logistics | return | Return count, reverse logistics metrics | May involve separate reverse AWB |
| Cancelled | Shipment/order cancelled | cancelled | Exclude from shipped/delivered metrics unless requested | Confirm cancellation timing |

### Settlement/remittance status

| Raw value family | Business meaning | Category | Metric usage | Caveat |
|---|---|---|---|---|
| Settled / Remitted / Paid | Amount has been settled/remitted by courier | settled | COD remitted amount, remittance lag | Still needs bank matching for cash realization |
| Pending | Settlement not yet completed | pending | Pending COD/remittance aging | May be normal within lag window |
| Failed / Reversed | Settlement failed or reversed | failed | Exception reporting | Requires vendor-specific semantics |
| Unknown/null | Missing settlement state | unknown | Low-confidence classification | Do not assume missing = pending |

### Mismatch category values

The following should be available as reusable mismatch category cards:

```text
missing_shipment
orphan_shipment
missing_invoice
orphan_invoice
freight_amount_mismatch
missing_cod_remittance
cod_amount_mismatch
delayed_remittance
missing_bank_credit
unidentified_bank_credit
low_confidence_native_data
schema_only_source
grain_mismatch
```

---

## 20.4 Metric candidates

These are reusable metric concepts. They should not include tenant/account filters.

| Metric candidate | Business definition | Metric type | Unit | Default aggregation | Polarity |
|---|---|---|---|---|---|
| `shipment_count` | Count of shipments/AWBs in scope | count | count | COUNT_DISTINCT AWB/shipment key | context_dependent |
| `delivered_shipment_count` | Count of shipments delivered to customer | count | count | COUNT_DISTINCT delivered AWB/shipment key | higher_is_better |
| `missing_shipment_count` | Count of source orders without shipment evidence | count | count | COUNT unmatched orders | lower_is_better |
| `missing_invoice_count` | Count of shipments without freight invoice evidence | count | count | COUNT unmatched AWBs | lower_is_better |
| `freight_billed_amount` | Total freight charged by courier/vendor | amount | currency | SUM freight amount | lower_is_better, context-dependent |
| `expected_freight_amount` | Expected freight based on rate card/shipment attributes | amount | currency | SUM expected freight | neutral |
| `freight_overcharge_amount` | Difference between actual freight and expected freight when actual exceeds expected | amount | currency | SUM max(actual - expected, 0) | lower_is_better |
| `cod_expected_amount` | COD expected from delivered COD shipments/orders | amount | currency | SUM COD expected | neutral |
| `cod_remitted_amount` | COD remitted by courier/aggregator | amount | currency | SUM COD remitted | higher_is_better |
| `cod_gap_amount` | Difference between expected COD and remitted COD | amount | currency | SUM expected - remitted | lower_is_better |
| `cod_remittance_lag_days` | Days between delivery and COD settlement/remittance | duration | days | AVG or PERCENTILE | lower_is_better |
| `settlement_batch_amount` | Courier remittance batch amount | amount | currency | SUM distinct batch amount | neutral |
| `bank_credit_matched_amount` | Bank credit amount matched to courier settlement/remittance | amount | currency | SUM matched credits | higher_is_better |
| `missing_bank_credit_amount` | Courier remittance amount not matched to bank credit | amount | currency | SUM unmatched remittance amount | lower_is_better |
| `unidentified_bank_credit_amount` | Bank credits not matched to courier remittance | amount | currency | SUM unmatched bank credit amount | lower_is_better |
| `low_confidence_record_count` | Count of records from low-confidence native data sources | count | count | COUNT records | lower_is_better |

---

## 20.5 Metric implementation candidates

Metric implementations should be attached to reconciliation level, source table family, and applicable vendor/table docs. They should not be duplicated per tenant/account unless the formula changes.

| Metric implementation candidate | Applies to | Formula / logic | Required evidence | Caveats |
|---|---|---|---|---|
| `metric_impl.logistics.order_to_shipment.missing_shipment_count` | Order-to-shipment reconciliation | Count source orders with no matched shipment/AWB | order side + shipment side + order/shipment keys | One order may split into multiple shipments |
| `metric_impl.logistics.shipment_to_invoice.missing_invoice_count` | Shipment-to-invoice reconciliation | Count shipped AWBs with no matched freight invoice | shipment/AWB side + freight invoice side | Do not run against schema-only invoice tables |
| `metric_impl.logistics.freight.freight_billed_amount` | Freight invoice tables | Sum actual freight bill amount at invoice/AWB grain | freight invoice table + documented freight amount column | Confirm amount semantics at table level |
| `metric_impl.logistics.freight.freight_overcharge_amount` | Freight charge reconciliation | `SUM(GREATEST(actual_freight - expected_freight, 0))` | actual freight + expected freight/rate-card logic | Expected freight source must be available |
| `metric_impl.logistics.cod.cod_expected_amount` | COD reconciliation expected side | Sum expected COD on delivered COD shipments | delivered COD shipment/order data | Exclude prepaid/POS unless explicitly requested |
| `metric_impl.logistics.cod.cod_remitted_amount` | COD settlement/remittance side | Sum courier/aggregator COD remitted amount | COD settlement/remittance table | Amount may be AWB-level or batch-level |
| `metric_impl.logistics.cod.cod_gap_amount` | COD reconciliation | `SUM(cod_expected_amount) - SUM(cod_remitted_amount)` after grain alignment | expected COD + remitted COD | Pre-aggregate to comparable grain |
| `metric_impl.logistics.cod.cod_remittance_lag_days` | COD remittance lag | Date difference between delivery date and settlement/remittance date | delivered date + settlement/remittance date | Lag windows are vendor/account-specific; avoid universal thresholds |
| `metric_impl.logistics.bank.missing_bank_credit_amount` | Courier batch-to-bank reconciliation | Sum settlement/remittance amounts without matched bank credit | settlement/remittance + bank statement side | Bank matching rules come from Banking KB |
| `metric_impl.logistics.data_quality.low_confidence_record_count` | Low-confidence native source validation | Count records missing required identifiers/amounts/status | native vendor table | Use for confidence scoring, not direct financial truth |

---

## 20.6 Formula template candidates

| Formula template | Formula type | Required inputs | Plain-English meaning | Denominator/null handling |
|---|---|---|---|---|
| `formula_template.count_unmatched_expected_records` | mismatch_count | expected records, matched actual records | Counts expected records with no actual-side match | Expected side must be de-duplicated at reconciliation unit |
| `formula_template.count_orphan_actual_records` | mismatch_count | actual records, matched expected records | Counts actual records without expected-side evidence | Actual side must be de-duplicated at reconciliation unit |
| `formula_template.gap_amount` | amount_gap | expected amount, actual amount | Difference between expected and actual amount | Null actual treated as 0 only for unmatched expected records |
| `formula_template.overcharge_amount` | positive_variance | actual amount, expected amount | Amount by which actual charge exceeds expected charge | Use `GREATEST(actual - expected, 0)` |
| `formula_template.reconciliation_match_rate` | rate | matched count, expected count | Share of expected records matched to actual records | If denominator is 0, return null/not_applicable |
| `formula_template.amount_match_rate` | rate | matched amount, expected amount | Share of expected amount matched to actual amount | If denominator is 0, return null/not_applicable |
| `formula_template.lag_days` | date_diff | start date, end date | Days between two lifecycle events | Null date should create unknown lag, not zero lag |
| `formula_template.batch_to_bank_gap` | amount_gap | settlement batch amount, matched bank credit amount | Difference between courier remittance and bank credit | Requires batch/UTR-level aggregation |

---

## 20.7 Rule candidates

| Rule candidate | Rule type | Severity | Rule statement | Failure mode |
|---|---|---|---|---|
| `rule.logistics.apply_account_data_binding` | scope_filter | critical | Apply Account Data Binding filters for every selected account/table. | Query may mix accounts or tenants. |
| `rule.logistics.no_vendor_doc_scope_inference` | scope_safety | critical | Do not infer tenant/group/account scope from vendor or reconciliation docs. | Scope hallucination. |
| `rule.logistics.awb_normalization_required` | join_safety | high | Normalize AWB/waybill/tracking IDs before matching where formatting differs. | False missing/orphan classifications. |
| `rule.logistics.preaggregate_to_reconciliation_grain` | grain_safety | critical | Pre-aggregate records to the reconciliation unit before amount comparison. | Double counting or grain mismatch. |
| `rule.logistics.no_awb_to_bank_direct_match` | grain_safety | critical | Do not directly compare AWB-level COD rows to bank credits when bank credit is batch-level. | False COD/bank gaps. |
| `rule.logistics.amount_semantics_required` | metric_semantics | critical | Do not use amount columns until table-level meaning is known. | Product value, freight, COD, and payable amounts may be confused. |
| `rule.logistics.schema_only_sources_not_evidence` | data_quality | high | Empty/schema-only tables are not valid actual-side evidence. | False reconciliation confidence. |
| `rule.logistics.low_confidence_native_flag` | data_quality | medium | Sparse native vendor tables must be marked low confidence and not treated as authoritative by default. | Over-trust in incomplete sources. |
| `rule.logistics.cod_prepaid_separation` | semantic_filter | high | Separate COD from prepaid/POS settlement rows before COD metrics. | COD metrics polluted by non-COD rows. |
| `rule.logistics.bank_semantics_from_banking_kb` | domain_boundary | high | Bank statement credit/debit/narration semantics must come from Banking KB. | Incorrect bank-side interpretation. |
| `rule.logistics.reference_fallback_lowers_confidence` | matching_confidence | medium | Amount/date/narration fallback matching should lower match confidence. | False positive matches. |
| `rule.logistics.no_snapshot_row_counts_as_truth` | governance | medium | Row counts and periods from source profiling are not durable KB truth. | Stale or tenant-specific grounding. |

---

## 20.8 Validation test candidates

| Validation test candidate | Test type | Linked rule | Blocking? | Validation condition |
|---|---|---|---|---|
| `validation.logistics.scope_filters_present` | semantic_check | `rule.logistics.apply_account_data_binding` | yes | Every tenant-scoped table has resolved account/table filters. |
| `validation.logistics.no_unscoped_vendor_query` | semantic_check | `rule.logistics.no_vendor_doc_scope_inference` | yes | Query does not rely only on vendor doc to infer customer scope. |
| `validation.logistics.reconciliation_unit_present` | semantic_check | `rule.logistics.preaggregate_to_reconciliation_grain` | yes | A reconciliation unit is selected for every matching query. |
| `validation.logistics.no_awb_bank_direct_compare` | semantic_check | `rule.logistics.no_awb_to_bank_direct_match` | yes | AWB-level rows are aggregated before bank-side comparison. |
| `validation.logistics.amount_column_semantics_resolved` | semantic_check | `rule.logistics.amount_semantics_required` | yes | Every amount column used in a metric has table-level amount semantics. |
| `validation.logistics.schema_only_source_excluded` | semantic_check | `rule.logistics.schema_only_sources_not_evidence` | yes | Schema-only/empty tables are not used as actual-side evidence. |
| `validation.logistics.cod_filter_present_for_cod_metrics` | semantic_check | `rule.logistics.cod_prepaid_separation` | yes | COD metrics include explicit COD/payment-mode/service-type filtering where available. |
| `validation.logistics.bank_side_source_is_banking_kb` | semantic_check | `rule.logistics.bank_semantics_from_banking_kb` | yes | Bank-side columns and transaction semantics are sourced from Banking KB. |
| `validation.logistics.fallback_match_confidence_downgraded` | semantic_check | `rule.logistics.reference_fallback_lowers_confidence` | no | Amount/date/narration fallback matches are marked medium/low confidence. |
| `validation.logistics.no_row_count_claims_in_cards` | governance_check | `rule.logistics.no_snapshot_row_counts_as_truth` | no | Extracted cards do not store profiling row counts as durable truth. |

---

## 20.9 Query pattern candidates

### Query pattern: order to shipment exception summary

**Intent:** Find orders that should have shipment evidence but do not.

**Required cards:** Order source table, shipment table, order-to-shipment relationship, missing shipment mismatch category.

**Shape:**

```text
Resolve scope → select expected orders → normalize order/shipment keys → left join shipment evidence → classify missing/orphan/duplicate shipment records.
```

**Output fields:** source order ID, shipment ID if any, missing reason, confidence, evidence source.

---

### Query pattern: shipment to freight invoice exception summary

**Intent:** Find shipped AWBs without freight invoice evidence or invoice amount mismatches.

**Required cards:** Shipment table, freight invoice table, shipment-to-invoice relationship, freight amount metric implementation, missing invoice category.

**Shape:**

```text
Resolve scope → select shipped AWBs → pre-aggregate invoice rows by AWB/invoice grain → left join invoice evidence → classify missing invoice, duplicate invoice, amount mismatch.
```

**Output fields:** AWB, courier partner, invoice number, actual freight, expected freight if available, mismatch category.

---

### Query pattern: freight overcharge analysis

**Intent:** Compare actual freight billed to expected freight.

**Required cards:** Freight invoice amount semantics, expected freight source/rate-card logic, freight overcharge formula template, amount semantics rules.

**Shape:**

```text
Resolve scope → compute expected freight by AWB/component → aggregate actual freight by AWB/component → compare actual vs expected → classify overcharge drivers.
```

**Output fields:** AWB, zone, weight, service type, expected freight, actual freight, overcharge amount, driver.

---

### Query pattern: delivered COD not remitted

**Intent:** Find delivered COD shipments with no courier settlement/remittance evidence.

**Required cards:** Delivered COD shipment evidence, COD settlement/remittance table, shipment-to-COD settlement relationship, COD value profiles, COD gap metrics.

**Shape:**

```text
Resolve scope → select delivered COD shipments → normalize AWB → left join COD settlement/remittance → classify missing, delayed, partial, amount mismatch.
```

**Output fields:** AWB, delivery date, COD expected, COD remitted, settlement date, lag days, mismatch category.

---

### Query pattern: courier remittance to bank reconciliation

**Intent:** Match courier/aggregator remittance batches to bank credits.

**Required cards:** Courier settlement/remittance table, bank statement table from Banking KB, settlement-to-bank bridge relationship, matching logic, bank-side output contract.

**Shape:**

```text
Resolve logistics account scope → resolve bank account scope → aggregate courier remittance to batch/UTR/reference grain → match to bank credits using UTR/reference first, fallback amount/date/narration → classify missing bank credit, unidentified bank credit, split/merged/delayed credit.
```

**Output fields:** settlement ID, UTR/reference, settlement amount, bank credit amount, bank credit date, gap amount, match confidence, mismatch category.

---

### Query pattern: low-confidence vendor source validation

**Intent:** Assess whether a native vendor table is usable for reconciliation.

**Required cards:** Native vendor table, required identifier/amount/status columns, low-confidence native data rule, fallback relationship if available.

**Shape:**

```text
Resolve table → profile required identifiers and amount fields → classify completeness → compare with documented fallback source when available → return confidence recommendation.
```

**Output fields:** table, missing identifier rate, missing amount rate, usable record count, fallback recommendation, confidence.

---

## 20.10 Output contract candidates

### Output contract: logistics reconciliation summary

Required sections:

```text
scope_summary
reconciliation_level
expected_side_summary
actual_side_summary
matched_summary
unmatched_expected
unmatched_actual
amount_gap_summary
mismatch_categories
confidence_summary
evidence_metadata
unresolved_items
```

### Output contract: logistics exception list

Required fields per row:

```text
reconciliation_unit
source_side_reference
actual_side_reference
expected_amount
actual_amount
gap_amount
status_or_mismatch_category
date_context
match_confidence
evidence_tables
recommended_next_action
```

---

## 20.11 Extraction boundaries and anti-patterns

Extract from this document:

```text
Reconciliation Profile
Reconciliation Side
Reconciliation Unit
Matching Logic
Mismatch Category
Metric
Metric Implementation
Formula Template
Rule
Validation Test
Query Pattern
Output Contract
Relationship candidates
Value Profile candidates
```

Do not extract from this document:

```text
Tenant
Group
Platform Account
Account Data Binding values
Business Scope Set
Customer-specific routing
Marketplace ownership facts
Bank account ownership facts
Durable row counts or period coverage
```

Those belong to tenant/group context, account data binding docs, vendor docs, banking docs, or runtime scope resolution.

Final grounding rule:

```text
This document tells the KB what should match and how to reason about logistics reconciliation.
It does not tell the KB whose data to filter or which customer account owns a shipment, settlement, or bank credit.
```

