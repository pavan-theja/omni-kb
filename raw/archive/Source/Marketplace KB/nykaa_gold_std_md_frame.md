---
title: Nykaa Fashion Marketplace Knowledge Base
doc_type: marketplace_raw_knowledge
domain: marketplace_finance
platforms: [nykaa_fashion]
platform_types: [marketplace]
platform_aliases: [Nykaa]
platform_contexts: [nykaa_fashion_india]
related_domains:
  - marketplace_finance
  - settlement_reconciliation
  - return_analysis
  - fee_reconciliation
  - gst_compliance
  - cash_flow
  - logistics_enrichment
  - bank_reconciliation
country: India
currency: INR
primary_scope_keys:
  - group_level_id: 22
primary_entities:
  - Mensa Brand Technologies Pvt. Ltd.
  - Mensa house-of-brands including Dennis Lingo and Hubberholme
tables:
  - zs_observe.nykaa_oms
  - zs_observe.nykaa_settlement
  - zs_observe.nykaa_addition_charge
  - zs_observe.nykaa_mapper_gst
  - zs_observe.nykaa_mapping
optional_modules:
  - shipping_adjustment_trueup
  - warehouse_gst_mapper
  - entity_gstin_mapping
  - marketplace_to_bank_reconciliation_note
  - logistics_enrichment
  - storefront_distinction
  - tax_anomaly_caveats
status: draft
owner: finance_data_team
source_documents:
  - Nykaa Recon Doc.docx
  - nykaa_marketplace_cognee_raw_ingestion.md
---

# Nykaa Fashion Marketplace Knowledge Base

## 1. How to use this document

This document is the curated raw markdown knowledge source for the Nykaa Fashion marketplace domain in the ZenStatement Context Engineering KB.

It follows the marketplace gold-standard raw markdown frame so Nykaa can be ingested using the same generic marketplace ingestion pipeline as Amazon, Flipkart, Myntra, and future marketplace docs.

This document is intentionally not card YAML, not canonical JSON, and not a manually authored graph-edge file. It is human-readable source knowledge designed for semantic chunking and later extraction into candidate cards, relationships, value profiles, query patterns, rules, validation tests, output contracts, retrieval indexes, and evidence metadata.

The document supports extraction across the following KB families:

- Business Hierarchy: platform, platform context, platform account, account data binding, reusable scope context.
- Data Understanding: table roles, columns, relationships, value profiles, grain, date safety, caveats.
- Metric Understanding: gross sales, net revenue, realization, commission rate, take rate, return rate, RTO rate, TCS, shipping adjustment metrics.
- Process Understanding: order-to-settlement, reverse/RTO/cancellation, shipping true-up, GST/entity canonicalization, marketplace-to-bank handoff.
- Reconciliation Understanding: OMS-to-settlement, reverse-to-settlement, settlement-vs-actual-settlement, shipping adjustment, mapper GST join, GSTIN mapping, bank handoff.
- Execution Guidance: mandatory filters, join transformations, status normalization, date usage, tax anomaly handling, grain alignment, table-specific exceptions.

The most important modeling principle for Nykaa is:

```text
nykaa_oms = order truth.
nykaa_settlement = payout and financial waterfall truth.
nykaa_addition_charge = shipping true-up / freight adjustment truth.
nykaa_mapper_gst = warehouse, AWB, courier, RTO, return, and GST invoice enrichment truth.
nykaa_mapping = seller entity and GSTIN canonicalization truth.
```

No one Nykaa table should be treated as the full source of truth for all business questions.

---

## 2. Marketplace overview and business context

### 2.1 Marketplace role

Nykaa operates multiple storefronts, but the data covered by this KB is **Nykaa Fashion**, not Nykaa Beauty / Nykaa.com transactional commerce.

Nykaa Fashion is the apparel, footwear, accessories, and fashion marketplace storefront. It operates as a managed marketplace where the seller owns the merchandise economics, while Nykaa intermediates customer ordering, storefront discovery, payment collection, fulfillment coordination, return handling, marketplace fee deduction, tax withholding, and seller settlement.

The transactional tables show Nykaa Fashion marketplace flow, not a pure Nykaa-owned inventory flow and not a beauty-commerce flow.

Evidence supporting Nykaa Fashion-only interpretation:

- `metadata` values are fashion-oriented: `nf`, `nf_mid`, `popup`, `popup_mid`.
- Dominant HSN codes are apparel/textile chapters: `61`, `62`, `63`, `54`, `52`, and `50`.
- `nykaa_mapper_gst.vendortype = 'Marketplace'` for all mapper GST rows.
- `nykaa_mapper_gst.locationtype = 'WareHouse'` for all mapper GST rows.
- The seller entity is Mensa Brand Technologies Pvt. Ltd. and related Mensa house-of-brands.
- `nykaa_mapping` includes both Nykaa Fashion and Nykaa.com labels, but transactional tables indicate Nykaa Fashion activity.

### 2.2 Seller / brand context

The seller represented in the active transactional data is primarily **Mensa Brand Technologies Pvt. Ltd.**

The data also includes Mensa house-of-brands and brand/entity aliases including Dennis Lingo, Hubberholme, and related source GST names.

Known entity/account signals:

- `group_level_id = 22` across transactional Nykaa tables.
- invoice prefixes include mostly `MBTPT`, with some `MBTPL` in settlement.
- `source_gst_name` values map to Mensa entity aliases.
- `nykaa_mapping` contains entity-to-GSTIN mappings for Mensa and related entities.
- GSTINs appear across Haryana, West Bengal, Maharashtra, and Karnataka registration states.

### 2.3 Commercial model

Nykaa Fashion’s commercial model in these tables can be read as:

```text
Customer pays Nykaa Fashion
→ Nykaa records the marketplace order
→ seller ships / fulfills the order through the Nykaa-aligned operational flow
→ Nykaa deducts commission, marketplace fees, TCS, shipping or adjustment components, and return/RTO impacts
→ Nykaa settles net amount to the seller
```

The seller does not receive the full customer payment directly. The seller’s realized amount is the net amount after marketplace deductions, tax withholdings, returns/RTOs, and adjustment layers.

The settlement ledger carries both sale and reverse/cancellation effects. The shipping adjustment table carries selective shipping/freight true-ups that are not the base order or base settlement ledger.

### 2.4 Storefronts, sub-platforms, or fulfillment programs

Nykaa storefront distinction is critical.

| Storefront / label | Business focus | Status in this KB |
|---|---|---|
| Nykaa Fashion | Apparel, footwear, accessories, fashion marketplace | Active transactional context |
| Nykaa.com / Beauty | Beauty, skincare, personal care | Appears in reference mapping labels only; not the active transactional context |
| `nf` | Standard Nykaa Fashion order metadata | Active |
| `nf_mid` | Nykaa Fashion mid-margin / margin-tier flow; exact economics require validation | Active |
| `popup` | Pop-up campaign or event order metadata | Active |
| `popup_mid` | Pop-up campaign with mid-margin tier; exact economics require validation | Active |
| `NykaaMan` | Small `fulfilment_channel` value in OMS | Interpreted as men’s vertical / managed fulfillment tag, not international marketplace |

Do not infer beauty-commerce volume merely because `nykaa_mapping` contains Nykaa.com labels. Transactional order and settlement context points to Nykaa Fashion.

### 2.5 What this marketplace data can and cannot answer

This KB can answer:

- Nykaa Fashion gross sales, net revenue, AOV, orders, units, and status funnels.
- Seller realization, net settlement, commission/take rate, MP fee impact, and TCS impact.
- Reverse, return, RTO, cancellation, and settlement clawback behavior.
- Shipping-charge true-ups and freight adjustment impact.
- OMS-to-settlement match coverage.
- Settlement-to-shipping-adjustment linkage.
- Courier delivery/RTO patterns using mapper GST.
- Entity/GSTIN canonicalization using Nykaa mapping.
- GST split and GST rate validation, with caveats.
- Marketplace-to-bank handoff, if banking KB and bank statements are available.

This KB cannot fully answer without additional data:

- Direct bank-credit matching unless bank statement and payout reference data are available.
- Contractual commission accuracy unless seller agreement / rate card is available.
- Full Nykaa Beauty / Nykaa.com commercial behavior.
- Full courier settlement or logistics vendor billing unless logistics KB/tables are retrieved.
- True TDS interpretation because TDS is not clearly represented as a separate reliable field in the available Nykaa tables.

---

## 3. Scope and account context

### 3.1 Active platform context

The active platform context is:

```text
Platform: Nykaa Fashion
Platform type: marketplace
Country: India
Currency: INR
Primary seller/account scope: group_level_id = 22
```

The raw markdown should explain this account/filter relationship. Final Account Data Binding cards should be generated by the ingestion pipeline later.

### 3.2 Seller / account identifiers

Primary seller/account indicators:

| Identifier | Meaning | Notes |
|---|---|---|
| `group_level_id = 22` | Primary Nykaa Fashion seller/account scope in transactional tables | Integer filter in transactional tables |
| `source_gst_name` | Seller/source GST entity name | Multiple Mensa spelling variants exist |
| `source_gst_id` | Seller/source GSTIN | Use with mapping table for canonicalization |
| invoice prefix `MBTPT` | Dominant Mensa invoice prefix | Seen in OMS, settlement, addition charge |
| invoice prefix `MBTPL` | Secondary Mensa invoice prefix | Present in settlement, around 3% in the source summary |
| `metadata` | Storefront / order-segment signal | `nf`, `nf_mid`, `popup`, `popup_mid` |

### 3.3 Default scope filters

For Nykaa transactional tables, default query scope is:

```sql
WHERE is_active = true
  AND group_level_id = 22
```

Apply this to:

- `zs_observe.nykaa_oms`
- `zs_observe.nykaa_settlement`
- `zs_observe.nykaa_addition_charge`
- `zs_observe.nykaa_mapper_gst`

### 3.4 Table-specific scope differences

| Table | Scope behavior |
|---|---|
| `nykaa_oms` | Has `is_active` and `group_level_id`; use both filters. |
| `nykaa_settlement` | Has `is_active` and `group_level_id`; use both filters. |
| `nykaa_addition_charge` | Has `is_active` and `group_level_id`; use both filters. |
| `nykaa_mapper_gst` | Has `is_active` and `group_level_id`; use both filters. |
| `nykaa_mapping` | Reference table; no `is_active` and no `group_level_id`; do not apply transactional filters. |

### 3.5 Reference-table exceptions

`nykaa_mapping` is a 27-row reference/dimension table for entity and GSTIN canonicalization.

Do not run:

```sql
WHERE is_active = true
```

or:

```sql
WHERE group_level_id = 22
```

on `nykaa_mapping`, because those columns do not exist.

Use `nykaa_mapping` to canonicalize seller/entity labels using fields such as:

- `entity`
- `mbtpt_remarks`
- `gstin_of_the_seller`

### 3.6 Scope caveats

- `group_level_id = 22` appears to be the current active Nykaa Fashion scope, but the model should remain extensible for future Nykaa accounts.
- Account filters belong to Account Data Binding extraction, not to Table Cards or Metric Cards.
- `nykaa_mapping` contains Nykaa Fashion and Nykaa.com labels. This is an entity mapping artifact, not proof of Nykaa.com transactional volume.
- Source GST names have inconsistent spelling, whitespace, underscore, and suffix variants. Exact string matching may under-match entities unless normalized.
- GSTIN state code can be derived from the first two digits of GSTIN and may be useful for entity/state validation.

---

## 4. Table family overview

| Table | Business role | Grain | Primary use | Required filters | Important caveats |
|---|---|---|---|---|---|
| `zs_observe.nykaa_oms` | Order Management System master | One row per order line / SKU line | Sales, returns, status funnel, payment mode, GST, brand/SKU, order lifecycle | `is_active = true`, `group_level_id = 22` | `transaction_type` includes stage values; `final_status` has case duplicates; `total_tax_perc` heavily NULL; many legacy/residue fields |
| `zs_observe.nykaa_settlement` | Marketplace settlement ledger | One row per settlement transaction line; one order can have forward and reverse rows | Payout, commission, MP fees, TCS, settlement amount, actual settlement, financial waterfall | `is_active = true`, `group_level_id = 22` | `settled_amount` and `actual_settlement` can differ; sparse `final_payout`; many GST/commission fields nullable; `awbno` sparse |
| `zs_observe.nykaa_addition_charge` | Shipping charge adjustment / true-up table | One row per shipping adjustment line; one order can have multiple adjustment rows | Shipping/freight true-ups, revised freight, shipping diff, GST on diff, credit-note coverage | `is_active = true`, `group_level_id = 22` | Selective adjustment table, not base settlement; `final_status` mostly NULL; several typo/variant shipping fields |
| `zs_observe.nykaa_mapper_gst` | Warehouse/OMS GST mapping and courier enrichment feed | One row per warehouse order | AWB, courier, warehouse status, return/RTO tags, order risk tags, GST invoice mapping, pre-OMS historical orders | `is_active = true`, `group_level_id = 22` | `orderno` does not directly join OMS; use truncated `magentoorderno`; includes Dec-2024 rows outside OMS window; not settlement data |
| `zs_observe.nykaa_mapping` | Entity/GSTIN reference table | One row per entity alias / GSTIN mapping | Canonical seller entity mapping, GSTIN/state mapping, source GST name standardization | No active/group filters | Contains Nykaa Fashion and Nykaa.com labels; duplicate GSTINs can be valid entity aliases |

Common table family mapping for Nykaa:

```text
OMS / order master: nykaa_oms
Settlement ledger: nykaa_settlement
Shipping adjustment / freight true-up: nykaa_addition_charge
Warehouse / GST / courier mapper: nykaa_mapper_gst
Entity / GSTIN mapping: nykaa_mapping
```

Nykaa does not have a separate Amazon-style line-level disbursement table, Flipkart-style commission invoice table, Flipkart-style cashback credit/debit note table, or Myntra-style non-order settlement table in the current source set.

---

## 5. End-to-end transaction lifecycle

### 5.1 Forward flow: order to settlement

Forward flow represents a customer sale that should eventually contribute to seller settlement.

Expected business sequence:

```text
Customer order placed on Nykaa Fashion
→ order appears in nykaa_oms
→ order moves through stage/status values such as shipped, intransit, delivered
→ warehouse/courier enrichment may appear in nykaa_mapper_gst
→ Nykaa settlement row appears in nykaa_settlement
→ Nykaa deducts gross commission, MP fees, TCS, shipping/other adjustments where applicable
→ settled_amount / actual_settlement represents the seller payout impact
```

Primary forward-flow tables:

- `nykaa_oms` for order truth.
- `nykaa_mapper_gst` for courier/AWB/warehouse truth.
- `nykaa_settlement` for payout truth.

Important forward-flow fields:

| Field | Table | Meaning |
|---|---|---|
| `order_id` | `nykaa_oms`, `nykaa_settlement`, `nykaa_addition_charge` | Marketplace order ID |
| `invoice_number` | `nykaa_oms`, `nykaa_settlement`, `nykaa_addition_charge` | Secondary validation key |
| `transaction_type` | `nykaa_oms`, `nykaa_settlement` | Forward/reverse/stage classification |
| `final_status` | `nykaa_oms`, `nykaa_settlement` | Lifecycle status |
| `charged_amount` | OMS/settlement | Gross amount / charged value |
| `payment_mode` | OMS/settlement | COD vs prepaid |
| `gross_commission` | settlement | Marketplace commission deduction |
| `mp_fees` | settlement | Marketplace platform fee deduction |
| `total_tcs_amount` | OMS/settlement | TCS deducted |
| `settled_amount` | settlement | Net settlement output |
| `actual_settlement` | settlement | Actual/final settlement amount, may differ from `settled_amount` |
| `magentoorderno` | mapper GST | Marketplace-style order reference with extra suffix |
| `transname` | mapper GST | Courier partner |
| `awbno` | mapper GST | Forward AWB/tracking |

For clean forward delivered rows, the main financial interpretation is:

```text
Customer charged amount
- commission
- marketplace fees
- TCS
- any applicable adjustment layer
= seller settlement impact
```

### 5.2 Reverse flow: return, cancellation, RTO, refund, clawback

Reverse flow covers returns, RTOs, cancellations, and seller payout clawbacks.

Expected business sequence:

```text
Customer return, RTO, cancellation, or failed delivery occurs
→ status appears in nykaa_oms and/or nykaa_mapper_gst
→ reverse or cancelled row appears in nykaa_settlement
→ customer-side refund / marketplace-side clawback is reflected
→ commission may reverse, remain zero, or behave differently by status
→ marketplace fee may be retained
→ settled_amount can be negative or adjustment-like
```

Reverse/RTO signals can appear in multiple places:

- `nykaa_oms.transaction_type = 'reverse'`
- `nykaa_oms.final_status IN ('Return', 'Customer Returns', 'RTO', 'reverse')`, with case normalization.
- `nykaa_settlement.transaction_type = 'reverse'`
- `nykaa_settlement.transaction_type = 'cancelled'`
- `nykaa_mapper_gst.status IN ('Returned', 'RTO Delivered', 'Cancelled')`
- `nykaa_mapper_gst.return_type IN ('Raise Return', 'RTO')`
- `nykaa_mapper_gst.return_status`, `return_create_reason`, and `return_code`

Important reverse-flow interpretations:

- Returns and RTOs must not be merged blindly.
- Settlement reverse rows can have positive `charged_amount` but negative `settled_amount`.
- Commission can be negative on returns because a previously charged commission may be reversed back to the seller.
- MP fees may still be retained on return/RTO scenarios.
- Cancelled rows typically have zero commission but may still have small settlement adjustments.
- `actual_settlement` can differ materially from `settled_amount` on reverse rows.

### 5.3 Adjustment flow: shipping true-ups, freight corrections, credit notes, and prior adjustments

Nykaa’s major adjustment module is `nykaa_addition_charge`.

This table captures shipping/freight true-ups or disputes that sit on top of base settlement.

Business sequence:

```text
Order has previously recorded shipping charge
→ Nykaa or finance computes revised freight / expected freight
→ difference is captured as shipping charge adjustment
→ GST on shipping difference is recorded
→ adjustment may be reflected in settlement, credit-note, or finance follow-up
```

Primary shipping true-up fields:

- `previous_shipping_charges`
- `revised_freight`
- `freight_final`
- `revised_freight_allocated`
- `diff_shipping_charge`
- `diff_shipping_charge_tax`
- `dif_revised_shipping_charge`
- `diff_revised_shipping_charge_tax`
- `shiping_charges_diff`
- `diff_freight`
- `tax_amount_on_charges`
- `tax_on_previous_shipping_charges`
- `rversal_cn`
- `gst_cn`
- `total_cn`
- `already_adjusted`

Observed typical pattern:

```text
diff_shipping_charge ≈ ₹10
diff_shipping_charge_tax ≈ ₹1.80
```

This suggests an adjustment of approximately ₹10 plus 18% GST per shipment line, but exact contractual interpretation should be validated with finance.

### 5.4 Payout flow: settlement to seller bank

The current Nykaa source does not provide a dedicated bank statement table or reliable UTR/payout reference mapping.

`nykaa_settlement` provides payout-impact fields such as:

- `settled_amount`
- `actual_settlement`
- `final_payout`
- `previous_final_out_value`
- `differential_amount`
- `already_paid` variants

But a complete settlement-to-bank reconciliation requires banking KB/table retrieval.

If the question asks whether Nykaa settlement matched bank credit, retrieval should combine:

```text
Nykaa settlement knowledge
+ Banking statement knowledge
+ marketplace_to_bank reconciliation pattern
```

and mark Nykaa payout reference / UTR as unresolved if no such field is available.

### 5.5 Timing gaps and in-flight transactions

Known timing and coverage issues:

- `nykaa_oms` active range is 2025-01-01 to 2025-12-31 using `created_date`.
- `nykaa_mapper_gst` range is 2024-11-30 to 2025-03-31 using `orderdate` and contains Dec-2024 pre-OMS historical records.
- `nykaa_addition_charge` range is 2025-02-01 to 2025-12-30 using `created_date`.
- Settlement order coverage is high but not perfect: about 98.3% of settlement orders match OMS.
- Mapper GST to OMS match is much lower, around 54%, partly due to date window mismatch and order ID transformation.
- Addition-charge orders match OMS completely in the source summary, but only about 91% match settlement.

Do not treat every unmatched row as a true business discrepancy without considering timing, grain, date-window, and ID-format caveats.

---

## 6. Entity relationships and joins

### 6.1 Primary join map

| From table | To table | Join key | Reliability / notes |
|---|---|---|---|
| `nykaa_oms` | `nykaa_settlement` | `order_id` | Strong primary join. Source summary: 45,185 of 45,966 settlement orders match OMS, about 98.3%. |
| `nykaa_oms` | `nykaa_settlement` | `order_id + invoice_number` | Strong validation join. Invoice match is about 99.6% for distinct settlement invoices in source summary. |
| `nykaa_oms` | `nykaa_addition_charge` | `order_id` | Strong. Source summary: 4,329 of 4,329 addition-charge orders match OMS. |
| `nykaa_settlement` | `nykaa_addition_charge` | `order_id` | Medium/high. Source summary: 3,947 of 4,329 addition-charge orders match settlement, about 91%. |
| `nykaa_oms` | `nykaa_mapper_gst` | truncated `magentoorderno` to `order_id` | Approximate. Around 54% match due to suffixes and date-window mismatch. |
| Transactional tables | `nykaa_mapping` | normalized `source_gst_name` to `mbtpt_remarks` | Approximate. Requires trim/lowercase and sometimes fuzzy matching. |

### 6.2 Secondary validation keys

Use `invoice_number` as a strong secondary validation key across:

- `nykaa_oms`
- `nykaa_settlement`
- `nykaa_addition_charge`

Observed invoice match in source summary:

```text
46,428 of 46,595 distinct settlement invoices match OMS, about 99.6%.
```

Use invoice number to validate order-level joins, but do not make it the only join key unless the analysis specifically requires invoice-level matching.

### 6.3 Join reliability and match rates

| Relationship | Approximate reliability | Interpretation |
|---|---:|---|
| OMS ↔ Settlement by `order_id` | High, around 98.3% match | Strong for settlement reconciliation |
| OMS ↔ Settlement by `invoice_number` | Very high, around 99.6% invoice match | Strong secondary validation |
| OMS ↔ Addition Charge by `order_id` | Very high, 100% in source summary | Addition-charge orders are all represented in OMS |
| Addition Charge ↔ Settlement by `order_id` | Medium/high, around 91% | Some shipping adjustments may be before/after settlement or not present in settlement |
| Mapper GST ↔ OMS by truncated `magentoorderno` | Medium/low, around 54% | Use for enrichment, not as mandatory order completeness control |
| Mapping ↔ Source GST name | Medium | Use normalization and review unmatched aliases |

### 6.4 Grain mismatch and double-counting risks

- OMS is order-line / SKU-line grain.
- Settlement is settlement transaction line grain; an order can have forward and reverse rows.
- Addition charge is selective adjustment-line grain; one order can have multiple shipping adjustment rows.
- Mapper GST is warehouse order grain; it may not align one-to-one with OMS order lines.
- Mapping is reference grain; do not join it in a way that multiplies transaction rows without checking uniqueness.

Before comparing amounts, aggregate both sides to the same grain:

```text
order_id
order_id + invoice_number
order_id + transaction_type
order_id + item_id if item_id is reliable
shipping adjustment order grain
courier / AWB grain for logistics analysis
```

### 6.5 Identifier normalization rules

Mapper GST join rule:

```sql
array_join(slice(split(magentoorderno, '-'), 1, 3), '-')
```

Example:

```text
magentoorderno = NYK-24095271-1493711-2-1
base order ID = NYK-24095271-1493711
```

Then join:

```text
base order ID → nykaa_oms.order_id
```

Entity/GST name normalization rule:

```sql
LOWER(TRIM(source_gst_name)) = LOWER(TRIM(mbtpt_remarks))
```

This may still under-match because of spelling, underscore, whitespace, suffix, or source-label variation.

### 6.6 Reference / mapping table joins

Use `nykaa_mapping` to canonicalize:

- seller entity name,
- source GST name,
- GSTIN,
- GSTIN state code.

Known Mensa Nykaa Fashion GSTIN examples:

| State / entity context | GSTIN |
|---|---|
| Haryana / Parent | `06AAOCM5326J1Z6` |
| West Bengal / Hooghly | `19AAOCM5326J1ZZ` |
| Maharashtra / Thane | `27AAOCM5326J1Z2` |
| Karnataka / Bangalore | `29AAOCM5326J1ZY` |

GSTIN state code comes from the first two digits:

- `06` = Haryana
- `19` = West Bengal
- `27` = Maharashtra
- `29` = Karnataka

---

## 7. Financial waterfall and seller realization

### 7.1 Forward settlement waterfall

For clean forward delivered rows in `nykaa_settlement`, the confirmed simplified settlement logic is:

```text
settled_amount = charged_amount - gross_commission - mp_fees - total_tcs_amount
```

A more complete conceptual waterfall is:

```text
Net seller settlement
= charged_amount
- gross_commission
- gross_commission_gst_amount, when populated
- mp_fees
- mp_fees_gst_amount, when populated
- total_tcs_amount
- shipping_amount / shipping true-up components, when applicable
+/- adjustments, prior-cycle differentials, actual settlement corrections
```

Important caveat:

```text
Not all fields are populated for every row. Some differences arise because of GST-on-commission, adjustment layers, final_payout, actual_settlement, nullable components, rounding, or prior-cycle differential fields.
```

### 7.2 Reverse / refund settlement waterfall

Reverse and cancellation flows should be interpreted separately from forward flows.

Reverse behavior:

```text
Original charged amount may remain positive
→ commission can be zero, negative, or reversed
→ marketplace fees may be retained
→ TCS can reverse or change sign
→ settled_amount often becomes negative
→ actual_settlement may differ from settled_amount
```

Cancelled behavior:

- 726 settlement rows in source summary.
- `gross_commission = 0` because no commission was earned.
- Total adjustment is small, around ₹ -10,692 in the source summary.

Do not treat reverse `charged_amount` as new revenue.

### 7.3 Non-order / adjustment waterfall

Nykaa does not have a separate Myntra-style non-order settlement table in the current source set.

The main non-base adjustment table is `nykaa_addition_charge`, which captures shipping/freight true-ups.

Shipping adjustment conceptual waterfall:

```text
previous_shipping_charges
→ revised_freight / freight_final
→ diff_shipping_charge
→ diff_shipping_charge_tax
→ total shipping adjustment impact
```

Use this adjustment table to explain shipping differences, not base revenue or base settlement.

### 7.4 Seller realization definition

Seller realization measures how much of customer charged amount reaches the seller after Nykaa deductions, tax withholding, returns, and adjustment effects.

Default Nykaa settlement realization:

```text
SUM(settled_amount) / SUM(charged_amount)
```

Recommended clean forward realization:

```text
SUM(settled_amount) / SUM(charged_amount)
WHERE transaction_type = 'forward'
```

Alternative actual realization:

```text
SUM(actual_settlement) / SUM(charged_amount)
```

Use `actual_settlement` when the question asks about final payout after settlement corrections; use `settled_amount` when the question asks about settlement ledger output.

### 7.5 Field-level payout interpretation

| Field | Business interpretation | Reliability / caveat |
|---|---|---|
| `charged_amount` | Customer charged / order value basis | Use with transaction type filter |
| `gross_commission` | Marketplace commission / major deduction | Observed high rate; confirm contract before external reporting |
| `mp_fees` | Marketplace platform fee | May be retained in return/RTO |
| `total_tcs_amount` | TCS deducted | Reclaimable/tax credit; cash-flow deduction, not necessarily permanent cost |
| `settled_amount` | Net settlement impact for the line | Primary settlement output |
| `actual_settlement` | Final/actual settlement amount after corrections | Can differ materially on reverse rows |
| `final_payout` | Alternate payout field | Often NULL; use cautiously |
| `commission_excluding_tcs_tds` | Commission net of withholdings | Often NULL; validate before use |
| `differential_amount` | Prior-cycle or correction delta | Varchar/drift-prone; interpret carefully |
| `already_paid` variants | Prior-cycle amount trackers | Varchar/inconsistent naming |

### 7.6 Known benchmark ranges or observed snapshots

Observed active forward rows with commission in the source summary:

| Metric | Observed value |
|---|---:|
| Gross sales / charged amount | about ₹4.14 Cr |
| Gross commission | about ₹1.63 Cr |
| Commission rate | about 39.4% of charged amount |
| MP fees | about ₹0.40 Cr / ₹40.2 L |
| TCS | about ₹0.019 Cr / ₹1.94 L |
| Effective TCS rate | about 0.47% |
| Settled amount | about ₹2.32 Cr |
| Net settlement percentage | about 56.2% of charged amount |
| Average MP fee per line | about ₹141 |

Public-domain seller-guide ranges often cite Nykaa category commission around 15%–30% or sometimes a flat 25% default, but the observed source summary shows a materially higher effective commission.

Possible interpretations:

- fashion/category mix has higher negotiated commission,
- seller-specific agreement differs from public guides,
- `gross_commission` may include embedded commercial sub-components,
- Nykaa-funded/brand-funded economics or fulfillment-related economics may be embedded,
- commission excluding discounts or taxes may be lower than the raw gross commission rate.

Do not quote 39.4% as contractual commission without seller agreement validation.

---

## 8. Fees, deductions, taxes, promotions, and adjustments

### 8.1 Commission and marketplace fees

Primary settlement commission fields:

- `gross_commission`
- `gross_commission_gst_amount`
- `commission_excluding_tcs_tds`
- `total_commission_amt`
- `comm_amt_calc`
- `commission_amt_per_unit`
- `final_commission_amt_per_unit`
- `commission_diff`
- `commission_tax_diff`
- `diff_commission_charge`
- `diff_commission_charge_tax`

Primary marketplace fee fields:

- `mp_fees`
- `mp_fees_gst_amount`

Recommended field for effective commission rate:

```text
gross_commission
```

Recommended field for marketplace fee impact:

```text
mp_fees
```

Use forward rows for clean commission/take-rate calculations unless the question explicitly concerns reversals.

### 8.2 Fixed / closing / platform fees

Nykaa does not expose a separate Flipkart-style fixed fee / closing fee breakdown in the current source set.

Marketplace/platform fee economics appear primarily in:

- `mp_fees`
- `mp_fees_gst_amount`
- related diff/adjustment columns where present

If the user asks about fixed fee specifically, retrieval should mark fixed-fee detail as unavailable unless a future Nykaa fee-detail table or contract/rate card is added.

### 8.3 Shipping, freight, fulfillment, and reverse logistics fees

Shipping/freight appears across settlement and addition-charge tables, but the clearest shipping true-up table is `nykaa_addition_charge`.

Relevant shipping/adjustment fields:

- `shipping_amount`
- `shipping_amount_excluding_tax`
- `shipping_charges_calc`
- `shiping_charges___gst`
- `previous_shipping_charges`
- `revised_freight`
- `freight_final`
- `revised_freight_allocated`
- `diff_shipping_charge`
- `diff_shipping_charge_tax`
- `dif_revised_shipping_charge`
- `diff_revised_shipping_charge_tax`
- `shiping_charges_diff`
- `diff_freight`
- `tax_amount_on_charges`
- `tax_on_previous_shipping_charges`

Business interpretation:

```text
positive diff_shipping_charge = possible additional amount / undercharged shipping correction
negative diff_shipping_charge = possible reversal, clawback, or overcharge correction
```

The exact sign convention should be validated with finance before external reporting.

### 8.4 Payment / collection / payment gateway fees

The source Nykaa tables include `payment_mode` but do not expose a clear, reliable separate payment gateway fee table.

Payment modes include:

- COD
- Prepaid

Use `payment_mode` for segmentation, return/RTO behavior, and COD-vs-prepaid analysis. Do not infer standalone payment gateway fee unless a future field or source table explicitly provides it.

### 8.5 Promotional credits, cashback, offers, and rebates

Nykaa source data includes discount and funding fields rather than a dedicated cashback credit/debit-note table.

Relevant OMS/settlement fields include:

- `discount`
- `discountamount`
- `nykaa_funded_amount`
- `nykaa_funded`
- `brand_funded_amount`
- `brand_funded`
- `distbutor_amount`

Use these for discount/funding analysis. Do not model Nykaa as having a Flipkart-style cashback credit/debit-note table unless future data provides it.

### 8.6 Reimbursements, protection funds, incentives, and penalties

No dedicated reimbursement/protection-fund/non-order settlement table is present in the current Nykaa source set.

Potential adjustment-like behavior exists through:

- `actual_settlement`
- `final_payout`
- `differential_amount`
- `previous_final_out_value`
- `already_paid` variants
- `nykaa_addition_charge` shipping/freight differences

If the user asks about non-order adjustments, retrieval should mark the dedicated non-order adjustment source as unavailable for Nykaa unless future source tables are added.

### 8.7 TCS and TDS

TCS:

- Tax Collected at Source under Section 52 of the CGST Act.
- Present as `total_tcs_amount` and `tcs` in OMS/settlement contexts.
- Observed around 0.47% of charged amount in the source summary, consistent with statutory 0.5% after rounding and transaction effects.
- Treat as a cash-flow deduction / reclaimable tax credit, not necessarily permanent marketplace cost.

TDS:

- Tax Deducted at Source under Section 194-O.
- Expected at around 0.1% of gross sale since Oct 2020.
- Not clearly maintained as a separate reliable field in the current Nykaa tables.
- May be netted into `commission_excluding_tcs_tds` or absent.
- Confirm with finance before quoting Nykaa TDS.

### 8.8 GST on products and GST on marketplace fees

Product GST fields appear in OMS, settlement, and mapper GST.

Relevant product GST fields:

- `total_tax`
- `total_tax_perc`
- `tax_percent`
- `tax_cgst_rate`
- `tax_sgst_rate`
- `tax_igst_rate`
- `tax_ugst_rate`
- `tax_cgst_amount`
- `tax_sgst_amount`
- `tax_igst_amount`
- `tax_ugst_amount`
- `cgst`
- `sgst`
- `igst`
- `ugst`

GST split logic:

```text
If source_state = destination_state:
  CGST + SGST should apply.

If source_state <> destination_state:
  IGST should apply.
```

Examples:

- West Bengal to Karnataka → inter-state → IGST.
- Karnataka to Karnataka → intra-state → CGST + SGST.

Known GST caveats:

- OMS `total_tax_perc` is NULL on about 65.5% of rows.
- Dominant valid GST rates include 5%, 12%, 18%, and 0%.
- `0.12` likely indicates unit error and should probably mean `12.0`.
- Settlement includes anomalous `total_tax_perc` values such as `57.571`, `80.905`, `83.286`, `95.238`, `97.883`, `98.857`, `103.286`, and `116.619`, likely caused by near-zero/negative bases or calculation artifacts.

For GST-rate validation, filter to known valid slabs:

```sql
WHERE total_tax_perc IN (0, 5, 12, 18)
```

### 8.9 Fee recovery on returns

Nykaa return economics must be interpreted through settlement and status context.

Return/RTO caveats:

- Commission may reverse, remain zero, or behave differently depending on settlement row type.
- MP fees may be retained even when sale value reverses.
- `settled_amount` can be negative even when `charged_amount` remains positive.
- `actual_settlement` may differ from `settled_amount` materially on reverse rows.
- RTO and customer return should be analyzed separately when possible.

A complete fee-recovery metric requires:

```text
forward fees charged
vs reverse fees reversed or retained
by order_id / invoice_number / transaction_type
```

### 8.10 Marketplace-specific naming traps

| Field / pattern | Trap | Guidance |
|---|---|---|
| `nykaa_settlement.awbno` | Very sparse; not reliable for forward shipment analysis | Use `nykaa_mapper_gst.awbno` for forward shipment tracking |
| `return_awb_number` | Mostly reverse context | Use for reverse shipment tracking |
| `final_status` | Case and semantic duplicates | Normalize with `LOWER()` |
| `transaction_type` in OMS | Contains stage-like values such as shipped/intransit/not shipped | Do not assume only forward/reverse |
| `nykaa_mapping` Nykaa.com labels | Reference mapping includes Nykaa.com labels | Do not infer transactional Nykaa.com volume |
| `total_tax_perc` | NULL-heavy and anomalous | Use validated tax splits or filter valid slabs |
| `gross_commission` | Observed high effective rate | Do not equate blindly to contractual commission |
| `_temp_old`, `_1`, `unnamed__*` fields | Spreadsheet/migration residue | Ignore unless debugging ingestion lineage |
| `shiping_*` typo fields | Misspelled but business-relevant shipping columns | Preserve exact physical column names in SQL |

---

## 9. Fulfillment, logistics, payment modes, and settlement cycle

### 9.1 Fulfillment models

Nykaa source data does not expose a clean Amazon-style FBA/MFN or Flipkart-style FBF/NFBF fulfillment model.

Operational fulfillment and shipment context appears through:

- `nykaa_oms.fulfilment_channel`, mostly NULL with a small `NykaaMan` count.
- `nykaa_mapper_gst.locationtype = 'WareHouse'`.
- `nykaa_mapper_gst.vendortype = 'Marketplace'`.
- `nykaa_mapper_gst.status`, `return_status`, `return_type`, and courier fields.

Interpretation:

```text
Nykaa Fashion data should be understood as marketplace + warehouse/courier-enriched flow, not a pure seller-self-ship model and not a clean FBF/NFBF split.
```

### 9.2 Logistics and courier signals

The best Nykaa logistics source is `nykaa_mapper_gst`, not `nykaa_settlement`.

Courier field:

```text
nykaa_mapper_gst.transname
```

Observed courier partners:

- DelhiverySurface
- Shadowfax
- BLUEDART
- BLUEDART1
- Nykaa Fashion surface
- EcomExpress

Important caveats:

- `BLUEDART` and `BLUEDART1` may represent different service tiers or source labels.
- `nykaa_settlement.awbno` is sparsely populated and should not be the primary forward AWB source.
- `nykaa_settlement.return_awb_number` is primarily reverse context.
- `nykaa_mapper_gst.awbno` is preferred for forward courier / AWB analysis.

### 9.3 COD vs prepaid behavior

Payment mode is important for RTO and return behavior.

Approximate distribution in source summary:

| Source | Prepaid share | COD share |
|---|---:|---:|
| OMS | about 57% | about 43% |
| Settlement | about 58% | about 42% |
| Mapper GST | similar COD/prepaid split | similar COD/prepaid split |

Use `payment_mode` in OMS/settlement and `mode` in mapper GST for prepaid vs COD analysis.

COD is especially relevant for RTO-risk and logistics diagnosis.

### 9.4 Settlement cycle and payout timing

The current Nykaa source does not provide a clearly documented payout calendar or UTR-level bank settlement reference.

Date fields useful for timing analysis include:

- `nykaa_oms.created_date`
- `nykaa_oms.order_shipped_date`
- `nykaa_oms.delivered_date`
- `nykaa_settlement.created_date`
- `nykaa_settlement.order_shipped_date`
- `nykaa_settlement.delivered_date`
- `nykaa_addition_charge.created_date`
- `nykaa_mapper_gst.orderdate`
- `nykaa_mapper_gst.shippeddate`
- `nykaa_mapper_gst.delivereddate`
- `nykaa_mapper_gst.invoicedate`
- `nykaa_mapper_gst.cancelleddate`

Settlement-to-bank timing cannot be fully validated without banking data.

### 9.5 Bank / UTR / payout references

The current Nykaa tables do not expose a strong, reliable UTR or bank reference field equivalent to Myntra’s UTR fields.

Potential payout-adjacent fields include:

- `settled_amount`
- `actual_settlement`
- `final_payout`
- `previous_final_out_value`
- `differential_amount`
- `already_paid` variants

These are payout-amount fields, not bank-reference fields.

For Nykaa-to-bank reconciliation, retrieve banking KB and use fallback matching by:

```text
settlement amount / actual settlement amount
bank account
date window
narration/reference if available in bank data
```

If no Nykaa payout reference exists, mark reference matching as unresolved.

### 9.6 Logistics handoff to the logistics KB

Nykaa marketplace KB should trigger logistics KB retrieval when the user asks about:

- courier performance,
- AWB tracking,
- Delhivery / Shadowfax / BlueDart / EcomExpress performance,
- RTO by courier,
- delivery failure,
- forward AWB,
- return AWB,
- shipping/freight true-up,
- logistics settlement beyond Nykaa’s marketplace adjustment layer.

Nykaa marketplace KB can provide order/courier enrichment, but courier billing / COD remittance / vendor settlement logic belongs to the logistics KB if those vendor tables exist.

---

## 10. Status and value semantics

### 10.1 Transaction types

`nykaa_oms.transaction_type` is not just `forward` / `reverse`. It includes stage-like operational values.

| Table | Field | Raw value | Business meaning | Include in metrics? | Notes |
|---|---|---|---|---|---|
| OMS | `transaction_type` | `forward` | completed or sale-like forward order line | Yes for clean gross sales | Safest default for gross sales |
| OMS | `transaction_type` | `reverse` | return/reverse lifecycle line | Yes for return/reverse analysis | Do not count as gross sale |
| OMS | `transaction_type` | `shipped` | shipped sale-like state | Maybe | Include only when analyzing shipped/in-flight sale cohort |
| OMS | `transaction_type` | `not shipped` | non-shipped stage | No for gross sales | Operational status |
| OMS | `transaction_type` | `intransit` | sale-like but in transit | Maybe | Include only when requested |
| Settlement | `transaction_type` | `forward` | sale / settlement credit side | Yes for realization denominator/numerator | Use forward filter for clean rates |
| Settlement | `transaction_type` | `reverse` | return/refund/RTO settlement impact | Yes for reverse impact | Interpret signs carefully |
| Settlement | `transaction_type` | `cancelled` | cancellation settlement impact | Yes for cancellation adjustment | Do not treat as sale |

Default gross sales definition should use:

```text
nykaa_oms.transaction_type = 'forward'
```

Alternative sale cohort can include:

```text
forward + shipped + intransit
```

but only when the business question explicitly asks for in-flight or shipped-not-delivered sales.

### 10.2 Internal transaction types

No strongly standardized internal transaction type profile is documented for Nykaa equivalent to Myntra’s `internal_txn_type`.

Use the documented `transaction_type`, `final_status`, and mapper GST status fields instead.

### 10.3 Final statuses / order statuses

`final_status` contains case and semantic duplicates.

Important values include:

- `Delivered`
- `Return`
- `Shipped`
- `forward`
- `reverse`
- `RTO`
- `shipped`
- `Not Shipped`
- `not shipped`
- `Lost`
- `Customer Returns`
- `Intransit`
- `Cancelled`

Always normalize for grouping:

```sql
LOWER(final_status)
```

Suggested status groupings:

| Normalized status | Business grouping |
|---|---|
| `delivered`, `forward` | Delivered / sale-like |
| `shipped`, `intransit` | In-flight sale-like |
| `return`, `customer returns`, `reverse` | Customer return / reverse |
| `rto` | Return-to-origin |
| `cancelled`, `not shipped` | Cancellation / non-shipped |
| `lost` | Lost shipment / exception |

### 10.4 Payment modes

Payment modes include:

- Prepaid
- COD

Use COD vs prepaid for:

- RTO rate comparison,
- return rate comparison,
- delivery success analysis,
- settlement segmentation,
- logistics handoff analysis.

### 10.5 Fulfillment values

`nykaa_oms.fulfilment_channel` is mostly NULL. A small value `NykaaMan` appears but should not be interpreted as international marketplace.

Use mapper GST fields for operational fulfillment/courier analysis:

- `transname`
- `status`
- `return_status`
- `return_type`
- `mode`
- `order_tag`
- `locationtype`
- `vendortype`

### 10.6 Document types / credit-debit notes

Nykaa does not expose a Flipkart-style cashback credit/debit note table in the current source set.

Credit-note-like fields in addition charge include:

- `rversal_cn`
- `gst_cn`
- `total_cn`
- `already_adjusted`

These are relevant for shipping/reversal adjustment coverage, not generic cashback.

### 10.7 Fee names / fee descriptions

Nykaa does not expose a separate commission invoice table with fee-name rows.

Fee components are represented as columns in settlement and addition-charge tables:

- `gross_commission`
- `mp_fees`
- `gross_commission_gst_amount`
- `mp_fees_gst_amount`
- `diff_shipping_charge`
- `diff_shipping_charge_tax`
- `cod_charges`
- `return_charges_calc`
- `return_charges__gst`

### 10.8 Null and unknown handling

- Do not drop NULL `total_tax_perc` rows blindly; many OMS rows have NULL tax percentage.
- Do not treat NULL `mp_fees_gst_amount` or `gross_commission_gst_amount` as zero without validating whether the component is absent or merely not populated.
- Do not treat NULL `final_payout` as zero payout; field is sparse.
- Do not treat missing mapper GST match as missing order; mapper GST has different date coverage and order ID formatting.
- Do not treat Nykaa.com labels in mapping as transactional Nykaa.com volume.

---

## 11. Key metrics and business definitions

### 11.1 Gross sales / GMV

Gross sales measure customer charged value for forward sale lines.

Default source:

```text
nykaa_oms
```

Default formula concept:

```text
SUM(charged_amount)
WHERE is_active = true
  AND group_level_id = 22
  AND transaction_type = 'forward'
```

Alternative cohort:

```text
forward + shipped + intransit
```

Use the alternative only when the question asks about shipped/in-flight sale cohort.

### 11.2 Net revenue after returns

Net revenue after returns measures gross sales less reverse/return value.

Default OMS concept:

```text
SUM(charged_amount where transaction_type = 'forward')
- SUM(charged_amount where transaction_type = 'reverse')
```

Caveat:

```text
Reverse charged_amount may reflect original order value, not direct payout clawback. Use settlement for payout impact.
```

### 11.3 Distinct orders and line items

- Use `COUNT(DISTINCT order_id)` for order count.
- Use `COUNT(*)` for line count.
- Use `SUM(quantity)` for units where quantity is reliable.

OMS is line-item grain, so line count and order count differ.

OMS-side counts:

```sql
SELECT COUNT(DISTINCT order_id) AS distinct_orders,
       COUNT(*) AS line_count,
       SUM(quantity) AS units_sold
FROM zs_observe.nykaa_oms
WHERE transaction_type = 'forward'
```

### 11.4 Units sold

Use OMS `quantity` on forward rows.

Default concept:

```text
SUM(quantity)
WHERE transaction_type = 'forward'
```

Validate that quantity is populated and meaningful for the selected status cohort.

### 11.5 Average order value

AOV measures customer charged amount per distinct order.

Default formula:

```text
SUM(charged_amount) / COUNT(DISTINCT order_id)
```

Use forward OMS rows by default.

### 11.6 Seller realization rate

Seller realization measures seller settlement as a percentage of gross customer charged amount.

Default settlement formula:

```text
SUM(settled_amount) / SUM(charged_amount)
```

Clean forward realization:

```text
SUM(settled_amount) / SUM(charged_amount)
WHERE transaction_type = 'forward'
```

Actual settlement variant:

```text
SUM(actual_settlement) / SUM(charged_amount)
```

Use actual settlement variant when the user asks about final actual payout rather than ledger-calculated settlement.

### 11.7 Net settlement amount

Net settlement amount is the payout-impact measure from `nykaa_settlement`.

Default formula:

```text
SUM(settled_amount)
```

If the question asks final payout after adjustments, use:

```text
SUM(actual_settlement)
```

### 11.8 Effective commission rate

Effective commission rate measures commission burden relative to charged amount.

Default source:

```text
nykaa_settlement
```

Formula:

```text
SUM(gross_commission) / SUM(charged_amount)
```

Use forward rows only for clean commission-rate analysis.

### 11.9 Effective fee / take rate

Take rate includes commission plus marketplace fees.

Formula:

```text
SUM(gross_commission + mp_fees) / SUM(charged_amount)
```

If fee GST fields are populated and the question asks for tax-inclusive take rate, include:

```text
gross_commission_gst_amount + mp_fees_gst_amount
```

but confirm null semantics first.

### 11.10 Shipping / freight cost rate

Nykaa shipping/freight cost rate is not fully represented as a clean base shipping fee table.

For shipping adjustment rate, use `nykaa_addition_charge`:

```text
SUM(diff_shipping_charge + diff_shipping_charge_tax) / SUM(relevant charged_amount or settlement amount)
```

Use only when the business question asks about shipping true-ups / adjustments.

### 11.11 Return rate

OMS-style return rate:

```text
COUNT(DISTINCT order_id with return/reverse final_status)
/ COUNT(DISTINCT order_id with forward sale status)
```

Mapper GST logistics-style return rate:

```text
COUNT(status = 'Returned') / COUNT(all mapper GST orders)
```

Do not mix OMS and mapper GST definitions without explaining grain differences.

### 11.12 RTO rate

OMS-style RTO rate:

```text
COUNT(DISTINCT order_id where LOWER(final_status) = 'rto')
/ COUNT(DISTINCT order_id in relevant sale/shipment cohort)
```

Mapper GST-style RTO rate:

```text
COUNT(status = 'RTO Delivered') / COUNT(all mapper GST orders)
```

Mapper GST is better for courier-level RTO analysis.

### 11.13 Cancellation rate

Cancellation/non-shipped rate can use:

- `nykaa_oms.final_status IN ('Not Shipped', 'not shipped', 'Cancelled')`
- `nykaa_mapper_gst.status = 'Cancelled'`
- `nykaa_settlement.transaction_type = 'cancelled'` for settlement-impact view.

OMS-side cancellation rate:

```sql
SELECT 1.0 * COUNT(DISTINCT CASE
                              WHEN LOWER(final_status) IN ('not shipped', 'cancelled')
                              THEN order_id END)
       / NULLIF(COUNT(DISTINCT order_id), 0) AS cancellation_rate
FROM zs_observe.nykaa_oms
```

Define the source and status cohort explicitly.

### 11.14 Cashback / offer rate

Nykaa has no dedicated cashback table in the current source.

Use discount/funding fields when the question asks about offers or discount funding:

- `discount`
- `discountamount`
- `nykaa_funded_amount`
- `brand_funded_amount`

Discount/offer aggregate from OMS:

```sql
SELECT SUM(COALESCE(discount, 0)
            + COALESCE(discountamount, 0)
            + COALESCE(nykaa_funded_amount, 0)
            + COALESCE(brand_funded_amount, 0)) AS total_offer_outflow
FROM zs_observe.nykaa_oms
WHERE transaction_type = 'forward'
```

Do not infer Flipkart-style cashback credit/debit note behavior.

### 11.15 Fee recovery rate on returns

Fee recovery on returns requires comparing forward fee/commission charged against reverse fee/commission reversal.

Conceptual formula:

```text
reversed commission / forward commission charged
```

or:

```text
(return-side fee reversal + adjustment credits) / forward-side fees charged
```

Settlement-side implementation:

```sql
SELECT ABS(SUM(CASE WHEN transaction_type = 'reverse'
                     THEN COALESCE(gross_commission, 0) END))
       / NULLIF(ABS(SUM(CASE WHEN transaction_type = 'forward'
                              THEN COALESCE(gross_commission, 0) END)), 0)
       AS fee_recovery_rate
FROM zs_observe.nykaa_settlement
```

Caveats:

- commission may be negative on reverse rows,
- MP fees may be retained,
- no separate line-level fee-detail table exists,
- aggregate to order level before comparing.

### 11.16 TCS/TDS amount and rate

TCS amount:

```text
SUM(total_tcs_amount)
```

TCS rate:

```text
SUM(total_tcs_amount) / SUM(charged_amount)
```

TDS:

```text
Not clearly available as a reliable standalone field in current Nykaa source.
```

If the user asks for TDS, state the field limitation and require finance/source validation.

### 11.17 GST rate validation

Use source/destination state and GST component fields.

Default GST validation:

```text
If source_state = destination_state → CGST + SGST
If source_state <> destination_state → IGST
```

Filter anomalous tax percentages:

```sql
WHERE total_tax_perc IN (0, 5, 12, 18)
```

### 11.18 Settlement cycle / payout lag

Use date differences only when fields are available and aligned:

```text
settlement created_date - OMS created_date
settlement created_date - OMS order_shipped_date
settlement created_date - OMS delivered_date
```

True bank payout lag requires banking data.

### 11.19 Reconciliation gap amount

Common gap formulas:

OMS vs settlement charged gap:

```text
SUM(oms.charged_amount) - SUM(settlement.charged_amount)
```

Settlement vs actual settlement gap:

```text
SUM(settled_amount - actual_settlement)
```

Shipping adjustment gap:

```text
SUM(diff_shipping_charge + diff_shipping_charge_tax)
```

Bank reconciliation gap, when bank data exists:

```text
SUM(expected Nykaa settlement/payout) - SUM(matched bank credit)
```

---

## 12. Reconciliation playbook

### 12.1 OMS to settlement reconciliation

Question answered:

```text
Which Nykaa OMS orders are missing settlement, and do settled orders match the order value?
```

Expected side:

```text
nykaa_oms forward delivered/shipped order lines
```

Actual side:

```text
nykaa_settlement settlement lines
```

Primary keys:

```text
order_id
```

Secondary keys:

```text
invoice_number
```

Grain:

```text
order_id or order_id + invoice_number, depending on analysis.
```

Mismatch categories:

- OMS order missing settlement.
- Settlement order missing OMS.
- Amount mismatch.
- Invoice mismatch.
- Timing gap.
- Status mismatch.
- Grain mismatch due to multiple rows per order.

Caveats:

- OMS `transaction_type` includes stage values.
- Normalize `final_status`.
- Settlement coverage is high but not perfect.
- Aggregate before amount comparison.

### 12.2 Settlement to fee detail reconciliation

Nykaa does not have a separate fee-detail invoice table in the current source set.

Question answered:

```text
Can Nykaa settlement deductions be decomposed into commission, MP fees, tax, and adjustments?
```

Expected side:

```text
nykaa_settlement component columns
```

Actual side:

```text
nykaa_settlement settled_amount / actual_settlement
```

Primary formula:

```text
charged_amount - gross_commission - mp_fees - total_tcs_amount ≈ settled_amount
```

Mismatch categories:

- GST component missing or nullable.
- Actual settlement differs from settled amount.
- Final payout field sparse.
- Adjustment/differential fields explain residual.
- Reverse/cancelled rows have different signs.

Caveats:

- This is not a separate table-to-table reconciliation.
- Use settlement row/component reconciliation.
- Do not expect Amazon-style disbursement detail.

### 12.3 Fee preview / expected fee to actual fee reconciliation

Nykaa does not have a fee-preview / expected-fee schedule table in the current source set.

If the user asks whether Nykaa overcharged commission or fees:

- Use observed settlement rates as actuals.
- Require seller contract/rate card or fee-preview source for expected values.
- Mark expected fee schedule as unresolved if no such document/table is available.

### 12.4 Cashback / offer / promotion reconciliation

Nykaa does not have a Flipkart-style cashback credit/debit note table.

Use discount/funding fields for offer analysis:

- `discount`
- `discountamount`
- `nykaa_funded_amount`
- `brand_funded_amount`

Question answered:

```text
How much discount or funding is reflected in orders or settlement?
```

Caveats:

- Do not treat discounts as cashback credit notes.
- Do not infer offer settlement reconciliation without explicit source fields.

### 12.5 Reverse / return / refund reconciliation

Question answered:

```text
Which returns, RTOs, or cancellations have matching reverse/cancelled settlement impact?
```

Expected side:

```text
nykaa_oms reverse / Return / RTO / Customer Returns rows
or nykaa_mapper_gst Returned / RTO Delivered / Cancelled rows
```

Actual side:

```text
nykaa_settlement reverse / cancelled rows
```

Primary keys:

```text
order_id
invoice_number, where available
return_awb_number, for reverse logistics context
```

Grain:

```text
order-level or order/invoice-level, not raw row-level unless line cardinality is validated.
```

Mismatch categories:

- Return in OMS but no reverse settlement.
- RTO in mapper GST but no settlement clawback.
- Reverse settlement with no OMS reverse record.
- Amount mismatch.
- Status mismatch.
- Timing gap.

Caveats:

- Mapper GST has different date coverage.
- RTO and customer returns should be separated.
- Settlement reverse rows can have positive charged amount and negative settled amount.

### 12.6 Non-order / adjustment reconciliation

No separate non-order settlement table exists in the current Nykaa source.

Adjustment analysis is primarily through:

```text
nykaa_addition_charge
nykaa_settlement differential / actual settlement fields
```

Question answered:

```text
Which orders have adjustment impacts outside base order settlement?
```

Caveats:

- Addition-charge is selective and shipping-focused.
- Do not use it as a complete non-order settlement ledger.

### 12.7 Shipping / freight / logistics adjustment reconciliation

Question answered:

```text
Which orders have shipping charge corrections or freight true-ups, and do those adjustments appear in settlement?
```

Expected side:

```text
nykaa_addition_charge shipping adjustment amount
```

Actual side:

```text
nykaa_settlement settled_amount / actual_settlement / shipping diff mirror fields
```

Primary keys:

```text
order_id
invoice_number
tracking_no / AWB for logistics context
```

Key fields:

```text
diff_shipping_charge
diff_shipping_charge_tax
revised_freight
previous_shipping_charges
already_adjusted
rversal_cn
gst_cn
total_cn
```

Mismatch categories:

- Addition charge present but settlement missing.
- Shipping diff has no credit note.
- Revised freight differs from expected.
- Adjustment not marked already adjusted.
- Multiple adjustment rows per order.

Caveats:

- `final_status` in addition-charge is mostly NULL.
- Join to OMS for lifecycle and to mapper GST for courier context.
- Settlement match is about 91% in source summary.

### 12.8 Entity / GSTIN / seller mapping reconciliation

Question answered:

```text
Which seller entity and GSTIN should a raw source GST name map to?
```

Expected side:

```text
transactional source_gst_name / source_gst_id
```

Actual / canonical side:

```text
nykaa_mapping.mbtpt_remarks
nykaa_mapping.gstin_of_the_seller
nykaa_mapping.entity
```

Primary matching logic:

```sql
LOWER(TRIM(source_gst_name)) = LOWER(TRIM(mbtpt_remarks))
```

Fallback:

- fuzzy string match,
- GSTIN direct match,
- first-two-digit GSTIN state code validation,
- manual review for unresolved aliases.

Caveats:

- `nykaa_mapping` has no active/group filters.
- Multiple aliases can map to the same GSTIN.
- Nykaa.com labels in mapping do not imply transactional Nykaa.com volume.

### 12.9 Settlement to bank reconciliation note

Question answered:

```text
Does Nykaa settlement match actual bank credit?
```

Expected side:

```text
nykaa_settlement settled_amount or actual_settlement
```

Actual side:

```text
bank statement credit, from banking KB
```

Primary keys:

```text
No reliable Nykaa UTR / bank reference in current source.
```

Fallback keys:

```text
amount + bank account + date window + bank narration/reference if available
```

Caveats:

- Requires banking KB.
- No clear Nykaa UTR/payout reference is present.
- Use payout reference matching only if future Nykaa source adds reliable reference fields.
- Return unresolved reference items explicitly.

### 12.10 Reconciliation grain and fallback keys

Recommended reconciliation grains:

| Reconciliation | Recommended grain |
|---|---|
| OMS ↔ Settlement | `order_id`, optionally `order_id + invoice_number` |
| OMS ↔ Addition Charge | `order_id`, optionally `order_id + invoice_number` |
| Settlement ↔ Addition Charge | `order_id`; aggregate if multiple rows |
| Mapper GST ↔ OMS | transformed base order ID from `magentoorderno` |
| Entity mapping | normalized source GST name / GSTIN |
| Settlement ↔ Bank | settlement amount/date + bank account + date window; UTR unresolved |

Do not compare raw rows directly across tables with different grains.

---

## 13. Table-specific curated knowledge

### 13.1 `zs_observe.nykaa_oms`

#### Role

`nykaa_oms` is the order-line-item master for Nykaa Fashion marketplace orders. It captures order identity, SKU, brand, HSN, customer charge, tax, payment mode, lifecycle status, source/destination state, and seller entity context.

It is the primary source for sales-side order analytics, status funnels, gross sales, AOV, return/RTO indicators, and GST analysis.

#### Grain

```text
One row per order line / SKU line.
```

Distinct orders are lower than row count because one order can have multiple SKUs or line items.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.nykaa_oms` |
| Active rows | 89,085 |
| Distinct orders | 62,470 |
| Column count | 175 |
| Date range | 2025-01-01 to 2025-12-31 using `created_date` |
| Currency | INR |
| Scope key | `group_level_id = 22` |
| Seller | Mensa Brand Technologies Pvt. Ltd. |
| Invoice prefix | Mostly `MBTPT` |

#### Primary analytical roles

- gross sales,
- net revenue after returns,
- order count and line count,
- units sold,
- AOV,
- return and RTO status analysis,
- payment mode mix,
- brand/SKU/category revenue,
- GST split analysis,
- discount/funding analysis,
- source/destination state analysis,
- OMS-to-settlement reconciliation.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = 22
```

Use `transaction_type = 'forward'` for clean gross sales unless the business question explicitly asks to include shipped/intransit stages.

#### Important columns

Identity and keys:

- `order_id`
- `invoice_number`
- `parent_id`
- `item_id`
- `unique_id`
- `txn_uuid`
- `unique_value`
- `file_uuid`

Product and SKU:

- `brand`
- `category`
- `sku_id`
- `product_sku`
- `skucode`
- `skuname`
- `product_name`
- `description`
- `hsn`
- `hsn_code`
- `hsn_generated`
- `quantity`
- `mrp`
- `mrp_per_unit`
- `base_mrp`
- `total_mrp`

Financial amounts:

- `charged_amount`
- `charged_amount_excluding_tax`
- `discount`
- `discountamount`
- `nykaa_funded_amount`
- `nykaa_funded`
- `brand_funded_amount`
- `brand_funded`
- `distbutor_amount`
- `sp_per_unit`
- `dp_per_unit`
- `taxable_amount`

Tax and GST:

- `total_tax`
- `total_tax_perc`
- `tax_percent`
- `tax_cgst_rate`
- `tax_sgst_rate`
- `tax_igst_rate`
- `tax_ugst_rate`
- `tax_cgst_amount`
- `tax_sgst_amount`
- `tax_igst_amount`
- `tax_ugst_amount`
- `cgst`
- `sgst`
- `igst`
- `ugst`
- `total_tcs_amount`
- `tcs`

Lifecycle and status:

- `transaction_type`
- `final_status`
- `payment_mode`
- `ordertype`
- `order_type`
- `ret_yes_no`
- `yes_or_no`
- `rule_name`

Fulfillment and logistics context:

- `fulfilment_channel`
- `ordersource`
- `order_source`
- `metadata`
- `return_awb`
- `vendor_name`
- `vendorname`
- `parent_vendor_name`
- `parent_vendor_code`
- `child_vendor_gst`

Location and GST entity:

- `source_state`
- `source_state_code`
- `source_gst_id`
- `source_gst_name`
- `destination_state`
- `destination_state_code`
- `destination_city`

Dates:

- `created_date`
- `order_shipped_date`
- `delivered_date`
- `invoice_date`
- `invoice_date_2`

System and metadata:

- `is_active`
- `zen_status`
- `is_duplicated`
- `group_level_id`
- `group_id`
- `tenant_id`
- `created_at`
- `updated_at`
- `deleted_at`

#### Value semantics

- `transaction_type` contains forward, reverse, shipped, not shipped, intransit.
- `final_status` has case and semantic duplicates.
- `metadata` values identify Nykaa Fashion segments such as `nf`, `nf_mid`, `popup`, `popup_mid`.
- `payment_mode` supports COD vs prepaid segmentation.

#### Relationships

- Join to `nykaa_settlement` on `order_id`; validate with `invoice_number`.
- Join to `nykaa_addition_charge` on `order_id`.
- Join to `nykaa_mapper_gst` using truncated `magentoorderno` from mapper GST.
- Join to `nykaa_mapping` by normalized `source_gst_name` to `mbtpt_remarks`.

#### Caveats

- `final_status` has case duplicates and semantic duplicates.
- `transaction_type` includes stage values; do not assume only forward/reverse.
- `total_tax_perc` is NULL on about 65.5% of rows.
- `source_gst_name` has multiple Mensa spelling variants.
- `_temp_old`, `_1`, `_temp`, `unnamed__*`, and duplicate date/string fields are migration or spreadsheet residue.
- `invoice_date` is mostly NULL.
- Prefer `created_date` for order-date reporting.
- Prefer curated primary fields over duplicate variants unless debugging source ingestion.

#### Common query use cases

- Monthly gross sales.
- Order-status funnel.
- Return and RTO rate.
- AOV.
- Brand/SKU/category sales.
- Payment mode mix.
- GST split by source and destination state.
- OMS orders missing settlement.

### 13.2 `zs_observe.nykaa_settlement`

#### Role

`nykaa_settlement` is the marketplace settlement ledger. It shows customer charged amount, Nykaa commission, marketplace fees, TCS, settlement amount, actual settlement, and reverse/cancelled settlement impacts.

It is the primary source for seller realization, payout waterfall, commission/take rate, settlement-vs-actual-settlement reconciliation, and return/RTO financial impact.

#### Grain

```text
One row per settlement transaction line.
An order can have multiple rows, including forward and reverse rows.
```

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.nykaa_settlement` |
| Row count | 52,342 |
| Distinct settlement orders | 45,966 |
| Invoice prefixes | `MBTPT` about 95%; `MBTPL` about 3% |
| Currency | INR |
| Scope key | `group_level_id = 22` |
| OMS coverage | about 98.3% of settlement orders match OMS |

#### Primary analytical roles

- net settlement,
- seller realization,
- commission and take rate,
- marketplace fee impact,
- TCS reporting,
- return/RTO settlement impact,
- settlement vs actual settlement reconciliation,
- OMS-to-settlement matching,
- payout-to-bank handoff where banking data exists.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = 22
```

Use `transaction_type = 'forward'` for clean forward realization and commission analysis.

#### Important columns

Identity and keys:

- `order_id`
- `invoice_number`
- `parent_id`
- `item_id`
- `unique_id`
- `txn_uuid`
- `unique_value`
- `file_uuid`

Financial base:

- `charged_amount`
- `charged_amount_excluding_tax`
- `shipping_amount`
- `shipping_amount_excluding_tax`
- `discount`
- `discountamount`
- `nykaa_funded_amount`
- `brand_funded_amount`

Tax and GST:

- `total_tax`
- `total_tax_perc`
- `tax_amount`
- `tax_amount_on_charges`
- `tax_amount_on_commission`
- `total_tcs_amount`
- `tcs`
- `gstin__uin`

Fees and deductions:

- `gross_commission`
- `gross_commission_gst_amount`
- `commission_excluding_tcs_tds`
- `mp_fees`
- `mp_fees_gst_amount`
- `cod_charges`
- `cod_charges__gst`
- `cod_charges_calc`
- `minumum_margin`
- `min_margin_amt`
- `diff_commission_charge`
- `diff_commission_charge_tax`
- `diff_shipping_charge`
- `diff_shipping_charge_tax`
- `return_charges_calc`
- `return_charges__gst`

Settlement output:

- `settled_amount`
- `actual_settlement`
- `final_payout`
- `previous_final_out_value`
- `differential_amount`
- `already_paid` variants

Lifecycle and status:

- `transaction_type`
- `final_status`
- `payment_mode`
- `ordertype`
- `ret_yes_no`

Dates:

- `created_date`
- `order_shipped_date`
- `delivered_date`
- `invoice_date`

Logistics and location:

- `awbno`
- `return_awb_number`
- `return_awb`
- `source_gst_id`
- `source_gst_name`
- `destination_state`
- `destination_city`
- `metadata`
- `supplier_id`

#### Value semantics

- `transaction_type = 'forward'` represents forward sale settlement.
- `transaction_type = 'reverse'` represents return/refund/RTO settlement impact.
- `transaction_type = 'cancelled'` represents cancellation settlement impact.
- `final_status` includes Delivered, Return, RTO, forward, reverse, Cancelled, Lost, Customer Returns.

#### Relationships

- Join to OMS by `order_id`, validate with `invoice_number`.
- Join to addition charge by `order_id` and optionally `invoice_number`.
- Join to mapper GST indirectly through OMS or transformed mapper GST order ID.
- Join to mapping using normalized source GST entity name if entity canonicalization is needed.
- Join to bank statement only through external banking KB and fallback amount/date logic, since UTR is not reliable/available.

#### Caveats

- `awbno` is populated on only about 42 rows; do not use settlement as primary forward AWB source.
- `return_awb_number` is populated mainly on reverse rows.
- `final_payout` is often NULL.
- `gross_commission_gst_amount`, `mp_fees_gst_amount`, and `commission_excluding_tcs_tds` are often NULL.
- Some numeric fields are stored as varchar because of schema drift and must be cast carefully.
- Many legacy/truncated/duplicate fields exist; prefer typed primary fields.
- Tax percent anomalies should be filtered for tax-rate analysis.
- `gross_commission` observed rate is high and should not be quoted as contractual commission without validation.

#### Common query use cases

- Seller realization.
- Commission/take rate.
- Net settlement by month.
- Forward vs reverse settlement impact.
- Settled amount vs actual settlement difference.
- TCS summary.
- OMS-to-settlement reconciliation.

### 13.3 `zs_observe.nykaa_addition_charge`

#### Role

`nykaa_addition_charge` is the shipping charge adjustment table. It captures freight/shipping deltas, revised freight, tax on the diff, and credit-note/adjustment indicators.

It is used for shipping true-up analysis, not as a base revenue or settlement table.

#### Grain

```text
One row per shipping adjustment line.
An order can have multiple adjustment rows.
```

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.nykaa_addition_charge` |
| Active rows | 4,563 |
| Distinct orders | 4,329 |
| Column count | 127 |
| Date range | 2025-02-01 to 2025-12-30 using `created_date` |
| Currency | INR |
| Scope key | `group_level_id = 22` |
| Invoice prefix | 100% `MBTPT` |
| OMS match | 100% of addition-charge orders match OMS |
| Settlement match | about 91% match settlement |

#### Primary analytical roles

- shipping-charge dispute analysis,
- revised freight vs previous charge,
- shipping adjustment impact on settlement,
- orders with adjustments but missing settlement,
- reversal credit-note coverage,
- shipping-diff distribution,
- logistics-enriched settlement diagnostics.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = 22
```

#### Important columns

Identity and keys:

- `order_id`
- `invoice_number`
- `parent_id`
- `invoiceno`
- `nykaa_orderno`
- `eretail_orderno`
- `tracking_no`
- `return_awb_number`
- `return_awb`
- `awb_number`
- `other_id`
- `unique_id`
- `txn_uuid`

Financial base:

- `charged_amount`
- `taxable_amount`
- `amount_with_gst`
- `sp_per_unit`
- `dp_per_unit`
- `nykaa_funded_amount`
- `brand_funded_amount`

Shipping adjustment core:

- `shipping_amount`
- `shiping_charges___gst`
- `shipping_charges_calc`
- `shiping_charges_tax_diff`
- `previous_shipping_charges`
- `revised_freight`
- `freight_final`
- `revised_freight_allocated`
- `diff_shipping_charge`
- `diff_shipping_charge_tax`
- `dif_revised_shipping_charge`
- `diff_revised_shipping_charge_tax`
- `shiping_charges_diff`
- `diff_freight`
- `tax_amount_on_charges`
- `tax_on_previous_shipping_charges`

Reversal / credit note:

- `rversal_cn`
- `gst_cn`
- `total_cn`
- `already_adjusted`

Lifecycle and status:

- `transaction_type`
- `final_status`
- `payment_mode`
- `order_type`
- `order_tag`

#### Value semantics

- Positive/negative sign convention for shipping diff requires finance validation.
- `already_adjusted` indicates whether an adjustment may already have been applied, but it is mostly NULL.
- `rversal_cn`, `gst_cn`, and `total_cn` support credit-note/reversal coverage checks.

#### Relationships

- Join to OMS by `order_id`.
- Join to settlement by `order_id`; aggregate if multiple rows exist.
- Join to mapper GST by order context through OMS if courier/AWB enrichment is needed.

#### Caveats

- `final_status` is mostly NULL; use OMS or settlement for lifecycle.
- Primary adjustment fields are `diff_shipping_charge` and `diff_shipping_charge_tax`.
- `already_adjusted` is mostly NULL.
- `brand_funded_amount` and some financial fields may be varchar and require casting.
- This table is small and selective; it should not be used as the base settlement table.
- Joins can multiply rows if settlement has multiple rows per order.
- Several shipping fields contain misspellings such as `shiping` and `dif`; preserve exact names in SQL.

#### Common query use cases

- Which orders have shipping charge true-ups?
- What is the total shipping adjustment amount?
- Which shipping adjustments have no matching settlement?
- Which orders have credit-note coverage for shipping reversal?
- What is the revised freight vs previous shipping charge?

### 13.4 `zs_observe.nykaa_mapper_gst`

#### Role

`nykaa_mapper_gst` is a warehouse / OMS GST mapping feed. It enriches Nykaa orders with warehouse order IDs, marketplace order IDs, invoice details, AWB, courier partner, shipment status, return/RTO status, return reasons, risk tags, and GST invoice mapping.

It is best used for logistics, courier, AWB, warehouse status, and return/RTO enrichment.

#### Grain

```text
One row per warehouse order.
```

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.nykaa_mapper_gst` |
| Active rows | 24,114 |
| Distinct `orderno` | 24,114 |
| Column count | 80 |
| Date range | 2024-11-30 to 2025-03-31 using `orderdate` |
| Scope key | `group_level_id = 22` |
| `vendortype` | 100% Marketplace |
| `locationtype` | 100% WareHouse |
| `is_replacement` | 100% No |
| `ordersource` | 100% NULL |

#### Primary analytical roles

- courier performance,
- delivery/RTO rate by courier,
- order-tag risk analysis,
- return reason distribution,
- AWB enrichment,
- pre-OMS historical order identification,
- warehouse-to-marketplace order mapping,
- GST invoice enrichment.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = 22
```

#### Important columns

Identity and keys:

- `orderno`
- `magentoorderno`
- `original_orderno`
- `invoiceno`
- `extlineno`
- `unique_id`
- `txn_uuid`
- `awbno`

Product and SKU:

- `brand`
- `category`
- `skucode`
- `skuname`
- `hsncode`
- `weight`
- `orderqty`
- `shippedqty`
- `unitprice`
- `sellingprice`
- `lineitemtotal`
- `mrp`

Financial and tax:

- `taxamount`
- `taxpercent`
- `cgstamount`
- `sgstamount`
- `igstamount`
- `cgsttaxpercent`
- `sgsttaxpercent`
- `igsttaxpercent`
- `shippingcharge`
- `discountamount`
- `discount_code`

Lifecycle and status:

- `status`
- `return_status`
- `return_type`
- `return_create_reason`
- `return_code`
- `reasonforcancellation`
- `cancelremark`
- `mode`
- `order_tag`
- `is_replacement`
- `onhold`
- `commenthistory`

Dates:

- `orderdate`
- `shippeddate`
- `delivereddate`
- `invoicedate`
- `cancelleddate`
- `upddate`
- `unhold_date`

Logistics and entity:

- `transname`
- `vendorname`
- `vendortype`
- `sellerid`
- `locationtype`
- `city`
- `state`
- `pincode`
- `country`
- `source_gst_name`

#### Value semantics

Status values include:

- `Delivered`
- `Returned`
- `RTO Delivered`
- `Cancelled`
- `Shipped`
- `Lost In Transit`
- `Confirmed`
- `Ready for Ship`

Return types include:

- `Raise Return`
- `RTO`

Order tags are comma-separated multi-label risk/ops fields.

Known order tags include:

- `replacement_order`
- `Blacklisted Customer`
- `City level RTO reduction`
- `RTO history check - COD`
- `RTO history check - Prepaid`
- `Duplicate order`
- `Verification-Adress Check`
- `Verification-Duplicate Qty`
- `Verification-Test Order`
- `mob_with_gt10000_spend`
- `Shoot orders Automated`

#### Relationships

- `orderno` is warehouse-style and does not directly join OMS.
- `magentoorderno` must be truncated to first three dash-separated components to join OMS.
- Use mapper GST for courier/AWB enrichment after linking to OMS.

#### Caveats

- `orderno` is warehouse style and does not directly join to OMS.
- `magentoorderno` contains extra suffixes.
- Date columns mix timestamp and varchar types.
- This table has no commission/fee/waterfall fields.
- It includes Dec-2024 records not present in OMS.
- It is most useful for courier, AWB, fraud/RTO, return reason, and historical mapping use cases.
- Do not use it as settlement truth.

#### Common query use cases

- Delivery success by courier.
- RTO rate by courier.
- RTO rate by COD vs prepaid.
- Return reason distribution.
- Risk-tag analysis.
- Pre-OMS historical orders.
- Mapper GST to OMS join coverage.

### 13.5 `zs_observe.nykaa_mapping`

#### Role

`nykaa_mapping` is a static entity-to-GSTIN reference table. It canonicalizes raw seller entity labels and maps Mensa/Nykaa Fashion entity names to GSTINs.

#### Grain

```text
One row per entity alias / GSTIN mapping.
```

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.nykaa_mapping` |
| Rows | 27 |
| `is_active` | Not present |
| `group_level_id` | Not present |
| Currency | Not applicable |

#### Primary analytical roles

- entity canonicalization,
- GSTIN mapping,
- state-code extraction from GSTIN,
- source GST name standardization,
- seller entity validation.

#### Mandatory filters

No `is_active` filter. No `group_level_id` filter.

#### Important columns

- `entity`
- `mbtpt_remarks`
- `gstin_of_the_seller`

#### Value semantics

Known entity labels include:

- Mensa Nykaa Fashion
- Mensa Nykaa.com
- Prita Nykaa.com
- Tanvi Nykaa.com
- Prita Nykaa Fashion
- SRK Nykaa.com
- SRK Nykaa Fashion

Important interpretation:

```text
The table contains both Nykaa Fashion and Nykaa.com entity labels.
This does not mean transactional data contains Nykaa.com beauty volume.
```

#### Relationships

- Join transactional `source_gst_name` to `nykaa_mapping.mbtpt_remarks` after normalization.
- Use `gstin_of_the_seller` for GSTIN/state canonicalization.

#### Caveats

- Do not apply `is_active = true`.
- Do not apply `group_level_id = 22`.
- Duplicate GSTINs within an entity can be valid because multiple aliases map to the same GST registration.
- Fuzzy matching may be needed.
- Use this as reference data, not transaction data.

#### Common query use cases

- Which GSTIN should this source GST name map to?
- Which entity owns this source GST name?
- Which state does this GSTIN belong to?
- How many orders map to each canonical GSTIN?

---

## 14. Mandatory query rules

### 14.1 Scope rules

- Use only `zs_observe` for Nykaa unless a future curated source explicitly says otherwise.
- Apply `group_level_id = 22` to Nykaa transactional tables.
- Do not apply `group_level_id = 22` to `nykaa_mapping` because it has no such column.
- Treat account scope as an Account Data Binding extraction outcome, not as a table-level universal property.

### 14.2 Active-row rules

Apply:

```sql
is_active = true
```

to:

- `nykaa_oms`
- `nykaa_settlement`
- `nykaa_addition_charge`
- `nykaa_mapper_gst`

Do not apply `is_active = true` to:

- `nykaa_mapping`

### 14.3 Date rules

- Use `created_date` for OMS and settlement analytics by default.
- Use `created_date` for addition-charge reporting unless shipping-specific source date is requested.
- Use `orderdate` for mapper GST order-date analysis.
- Use `order_shipped_date`, `delivered_date`, `shippeddate`, or `delivereddate` only when the user asks about shipping, delivery, or fulfillment timing.
- Avoid display or inconsistent date strings unless parsed safely.

### 14.4 Transaction/status rules

- Always define `transaction_type` when measuring gross sales, returns, settlement, or reversal impact.
- Use `transaction_type = 'forward'` for clean gross sales.
- Do not aggregate `charged_amount` across all `transaction_type` values without explaining the interpretation.
- Normalize `final_status` with `LOWER()` for bucketing.
- Separate return, RTO, cancelled, not-shipped, and in-transit cohorts where possible.

### 14.5 Join and grain rules

- Aggregate to the correct grain before comparing amounts across tables.
- Do not directly compare raw settlement rows to raw OMS rows if multiple rows exist per order.
- Join OMS to settlement by `order_id`, validate with `invoice_number`.
- Join addition charge to OMS by `order_id`.
- Join addition charge to settlement by `order_id`, but expect incomplete settlement match.
- Join mapper GST to OMS by transforming `magentoorderno`, not by `orderno`.
- Do not use mapper GST as settlement truth.
- Do not use addition charge as base settlement truth.

### 14.6 Numeric casting rules

- Some Nykaa fields are typed inconsistently due to schema drift.
- Cast varchar-typed numeric fields before arithmetic.
- Avoid `_temp_old`, `_1`, `unnamed__*`, and migration-residue fields unless debugging ingestion history.

### 14.7 Tax and TCS/TDS rules

- Use GST component fields and source/destination state logic for GST validation.
- Filter to known valid tax slabs for tax-rate analysis: 0%, 5%, 12%, 18%.
- Treat anomalous tax rates as calculation artifacts unless validated.
- TCS is represented and observed around 0.47% in the source summary.
- TDS is not clearly available as a standalone reliable field; do not force TDS analysis without source validation.
- Treat TCS/TDS as tax-credit/cash-flow items, not always permanent marketplace cost.

### 14.8 Settlement and realization rules

- Use `settled_amount` for settlement ledger output.
- Use `actual_settlement` when the question asks for final actual settlement.
- Do not treat `final_payout` as reliable by default because it is often NULL.
- Use forward rows for clean seller realization and commission rate.
- Separate reverse/cancelled rows for clawback analysis.
- Explain whether realization includes or excludes tax withholdings and adjustments.

### 14.9 Platform-specific forbidden assumptions

- Do not treat Nykaa Fashion as Nykaa Beauty / Nykaa.com.
- Do not infer all Nykaa.com mapping labels are active transactional storefronts.
- Do not assume Nykaa has a Flipkart-style cashback table.
- Do not assume Nykaa has an Amazon-style fee-preview table.
- Do not assume Nykaa has a Myntra-style non-order settlement table.
- Do not assume Nykaa settlement contains reliable forward AWB data.
- Do not assume `gross_commission` equals contractual commission without agreement validation.
- Do not assume mapper GST unmatched orders are business discrepancies without date-window and ID-format review.

---

## 15. Data-quality and semantic caveats

### 15.1 Cross-table caveats

- Nykaa tables contain many duplicate, legacy, temporary, and migration-residue columns.
- Field names vary across tables: `created_date` vs `orderdate`, `sku_id` vs `skucode`, `total_tax` vs `taxamount`, `source_gst_name` variants.
- Some fields have correct business meaning only in one table but misleading names in another.
- `nykaa_mapping` is reference data, not transactional data.
- `nykaa_mapper_gst` is warehouse/courier enrichment data, not settlement data.
- `nykaa_addition_charge` is adjustment data, not base settlement data.

### 15.2 Scope caveats

- Transactional tables use `group_level_id = 22`.
- Reference table `nykaa_mapping` has no `group_level_id`.
- Future Nykaa accounts may require additional Account Data Bindings.

### 15.3 Status caveats

- OMS `transaction_type` includes stage values.
- OMS `final_status` contains case duplicates.
- Mapper GST uses different status names from OMS.
- Settlement status is cleaner but still requires context for reverse/cancelled rows.
- Null and unknown values should not be dropped without business logic.

### 15.4 Financial caveats

- `charged_amount` in OMS is gross selling price including tax.
- `settled_amount` is seller settlement output.
- `actual_settlement` can differ from `settled_amount`.
- `final_payout` is sparse.
- `gross_commission` may include broader deductions, not only pure contractual commission.
- MP fees may be retained on return/RTO.
- Shipping adjustment table is selective and small.

### 15.5 Tax caveats

- `total_tax_perc` is heavily NULL in OMS.
- Settlement has anomalous tax percentages.
- Use GST split fields and source/destination state for GST validation.
- TDS is not clearly represented as a separate reliable field.
- GSTIN mapping should be canonicalized through `nykaa_mapping` when possible.

### 15.6 Logistics caveats

- Courier partner is available in `nykaa_mapper_gst.transname`.
- OMS lacks reliable courier partner fields.
- Settlement `awbno` is sparse.
- Settlement `return_awb_number` is mainly reverse context.
- Mapper GST includes historical orders before OMS date window.

### 15.7 Type-casting caveats

- Some fields are varchar despite financial names.
- Use `TRY_CAST` or safe casts for financial/string columns when needed.
- Avoid arithmetic on raw varchar fields.
- Preserve exact misspelled column names in SQL, especially `shiping_*` and `dif_*` variants.

### 15.8 Legacy / duplicate / migration-residue fields

Ignore by default unless the task is ingestion debugging:

- `_temp_old`
- `_temp_old_temp_old`
- `_temp`
- `_1`
- `unnamed__*`
- duplicate date variants
- old source spreadsheet residue columns

---

## 16. Supported question patterns

### 16.1 Sales and revenue questions

- What were Nykaa Fashion gross sales last month?
- What was Nykaa Fashion net revenue after returns?
- What were units sold by brand or SKU?
- What was AOV for Nykaa Fashion?
- How much revenue came from `nf`, `nf_mid`, `popup`, and `popup_mid`?

### 16.2 Settlement and realization questions

- What was Nykaa seller realization rate?
- What was net settlement by month?
- How does `settled_amount` compare with `actual_settlement`?
- Which transaction types drove negative settlement impact?
- Why is Nykaa settlement lower than expected?

### 16.3 Fee and deduction questions

- What is the effective commission rate?
- What is the total marketplace fee impact?
- What is the combined take rate of commission plus MP fees?
- Why does observed commission look higher than expected?
- Which rows have high MP fees or unusual commission?

### 16.4 Return / RTO / cancellation questions

- What is the return rate?
- What is the RTO rate?
- Which orders have reverse rows in OMS but no reverse settlement?
- Which RTO orders caused negative settlement?
- How do COD and prepaid differ in RTO rate?

### 16.5 GST / TCS / TDS questions

- What is total TCS deducted?
- What is the observed TCS rate?
- Which GST rates appear in Nykaa Fashion data?
- Which orders have anomalous GST percentages?
- Which seller GSTIN should a source GST name map to?
- Is a transaction inter-state or intra-state?
- Can we calculate TDS from Nykaa data?

### 16.6 Cashback / promotion / offer questions

- How much discount was funded by Nykaa?
- How much discount was funded by brand?
- Is there a cashback table for Nykaa?
- What is the discount/funding rate by brand or campaign metadata?

### 16.7 Logistics / shipping adjustment questions

- Which orders have shipping charge true-ups?
- What is the total shipping adjustment amount?
- Which courier has highest RTO rate?
- Which orders have AWB in mapper GST?
- Which shipping adjustments are missing settlement?
- Which shipping adjustments have reversal credit notes?

### 16.8 Reconciliation questions

- Which OMS orders are missing settlement?
- Which settlement orders do not match OMS?
- Where does OMS charged amount differ from settlement charged amount?
- Which reverse/RTO orders are missing settlement reversal?
- Which addition-charge rows are missing settlement?
- How does mapper GST map to OMS?
- How should source GST names be canonicalized?

### 16.9 Diagnostic questions

- Why did Nykaa realization drop this month?
- Was realization decline caused by commission, MP fees, returns/RTOs, shipping adjustments, or TCS?
- Did COD orders drive higher RTO?
- Did a courier drive higher delivery failure?
- Did GST anomalies affect reporting?

### 16.10 Bank / payout matching questions

- Does Nykaa settlement match bank credit?
- Which Nykaa settlements are missing bank credit?
- What should be used as Nykaa payout reference?
- Can Nykaa settlement be reconciled to bank without UTR?

Answer these only by retrieving banking KB as well, because current Nykaa tables do not contain a reliable UTR/payout reference.

---

## 17. SQL pattern appendix

These SQL snippets are evidence examples for later Query Pattern, Rule, or Validation Test extraction. They are not final canonical query cards.

### 17.1 Gross sales

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  COUNT(DISTINCT order_id) AS orders,
  SUM(quantity) AS units,
  ROUND(SUM(charged_amount), 2) AS gross_sales
FROM zs_observe.nykaa_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND group_level_id = 22
GROUP BY 1
ORDER BY 1;
```

### 17.2 Net revenue

```sql
WITH base AS (
  SELECT
    DATE_TRUNC('month', created_date) AS month,
    SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END) AS gross,
    SUM(CASE WHEN transaction_type = 'reverse' THEN charged_amount ELSE 0 END) AS returned
  FROM zs_observe.nykaa_oms
  WHERE is_active = true
    AND group_level_id = 22
  GROUP BY 1
)
SELECT
  month,
  gross,
  returned,
  gross - returned AS net_revenue,
  ROUND(100.0 * (gross - returned) / NULLIF(gross, 0), 2) AS net_revenue_pct
FROM base
ORDER BY month;
```

### 17.3 Seller realization

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  SUM(charged_amount) AS charged,
  SUM(settled_amount) AS settled,
  SUM(actual_settlement) AS actual_settlement,
  ROUND(100.0 * SUM(settled_amount) / NULLIF(SUM(charged_amount), 0), 2) AS settlement_realization_pct,
  ROUND(100.0 * SUM(actual_settlement) / NULLIF(SUM(charged_amount), 0), 2) AS actual_realization_pct
FROM zs_observe.nykaa_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
  AND group_level_id = 22
GROUP BY 1
ORDER BY 1;
```

### 17.4 Fee breakdown

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  SUM(charged_amount) AS charged,
  SUM(gross_commission) AS commission,
  SUM(mp_fees) AS mp_fees,
  SUM(total_tcs_amount) AS tcs,
  SUM(settled_amount) AS settled,
  ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(charged_amount), 0), 2) AS commission_pct,
  ROUND(100.0 * (SUM(gross_commission) + SUM(mp_fees)) / NULLIF(SUM(charged_amount), 0), 2) AS take_rate_pct
FROM zs_observe.nykaa_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
  AND group_level_id = 22
GROUP BY 1
ORDER BY 1;
```

### 17.5 Return / RTO rate

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  COUNT_IF(transaction_type = 'forward') AS forward_lines,
  COUNT_IF(LOWER(final_status) IN ('return','customer returns','reverse')) AS return_lines,
  COUNT_IF(LOWER(final_status) = 'rto') AS rto_lines,
  ROUND(100.0 * COUNT_IF(LOWER(final_status) IN ('return','customer returns','reverse'))
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_rate_pct,
  ROUND(100.0 * COUNT_IF(LOWER(final_status) = 'rto')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct
FROM zs_observe.nykaa_oms
WHERE is_active = true
  AND group_level_id = 22
GROUP BY 1
ORDER BY 1;
```

### 17.6 OMS to settlement reconciliation

```sql
WITH oms_fwd AS (
  SELECT DISTINCT order_id, invoice_number, charged_amount
  FROM zs_observe.nykaa_oms
  WHERE is_active = true
    AND transaction_type = 'forward'
    AND LOWER(final_status) IN ('delivered','shipped')
    AND group_level_id = 22
),
sett AS (
  SELECT DISTINCT order_id
  FROM zs_observe.nykaa_settlement
  WHERE is_active = true
    AND group_level_id = 22
)
SELECT o.order_id, o.invoice_number, o.charged_amount
FROM oms_fwd o
LEFT JOIN sett s ON o.order_id = s.order_id
WHERE s.order_id IS NULL;
```

### 17.7 Settlement component reconciliation

```sql
SELECT
  order_id,
  transaction_type,
  ROUND(SUM(charged_amount), 2) AS charged,
  ROUND(SUM(gross_commission), 2) AS commission,
  ROUND(SUM(mp_fees), 2) AS mp_fees,
  ROUND(SUM(total_tcs_amount), 2) AS tcs,
  ROUND(SUM(settled_amount), 2) AS settled,
  ROUND(SUM(charged_amount - gross_commission - mp_fees - total_tcs_amount), 2) AS expected_settled_simple,
  ROUND(SUM(settled_amount) - SUM(charged_amount - gross_commission - mp_fees - total_tcs_amount), 2) AS residual
FROM zs_observe.nykaa_settlement
WHERE is_active = true
  AND group_level_id = 22
GROUP BY order_id, transaction_type
ORDER BY ABS(residual) DESC
LIMIT 100;
```

### 17.8 Discount / funding analysis

```sql
SELECT
  metadata,
  COUNT(DISTINCT order_id) AS orders,
  SUM(charged_amount) AS charged,
  SUM(discountamount) AS discount_amount,
  SUM(nykaa_funded_amount) AS nykaa_funded,
  SUM(brand_funded_amount) AS brand_funded
FROM zs_observe.nykaa_oms
WHERE is_active = true
  AND group_level_id = 22
  AND transaction_type = 'forward'
GROUP BY metadata
ORDER BY charged DESC;
```

### 17.9 Shipping adjustment reconciliation

```sql
SELECT
  order_id,
  invoice_number,
  previous_shipping_charges,
  revised_freight,
  diff_shipping_charge,
  diff_shipping_charge_tax,
  dif_revised_shipping_charge
FROM zs_observe.nykaa_addition_charge
WHERE is_active = true
  AND group_level_id = 22
  AND ABS(COALESCE(diff_shipping_charge, 0)) > 0
ORDER BY ABS(diff_shipping_charge) DESC;
```

### 17.10 GST/TCS/TDS validation

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  ROUND(SUM(total_tcs_amount), 2) AS total_tcs,
  ROUND(SUM(charged_amount), 2) AS charged,
  ROUND(100.0 * SUM(total_tcs_amount) / NULLIF(SUM(charged_amount), 0), 4) AS tcs_rate_observed
FROM zs_observe.nykaa_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
  AND group_level_id = 22
GROUP BY 1
ORDER BY 1;
```

GST slab validation:

```sql
SELECT
  total_tax_perc,
  COUNT(*) AS rows,
  SUM(charged_amount) AS charged
FROM zs_observe.nykaa_oms
WHERE is_active = true
  AND group_level_id = 22
  AND total_tax_perc IN (0, 5, 12, 18)
GROUP BY total_tax_perc
ORDER BY rows DESC;
```

### 17.11 Settlement cycle / payout lag

```sql
SELECT
  DATE_DIFF('day', o.created_date, s.created_date) AS days_to_settlement,
  COUNT(DISTINCT o.order_id) AS orders,
  SUM(s.settled_amount) AS settled
FROM zs_observe.nykaa_oms o
JOIN zs_observe.nykaa_settlement s
  ON o.order_id = s.order_id
WHERE o.is_active = true
  AND s.is_active = true
  AND o.group_level_id = 22
  AND s.group_level_id = 22
  AND o.transaction_type = 'forward'
  AND s.transaction_type = 'forward'
GROUP BY 1
ORDER BY 1;
```

### 17.12 Settled amount vs actual settlement difference

```sql
SELECT
  transaction_type,
  COUNT(*) AS rows,
  ROUND(SUM(settled_amount - actual_settlement), 2) AS total_diff,
  ROUND(AVG(settled_amount - actual_settlement), 4) AS avg_diff
FROM zs_observe.nykaa_settlement
WHERE is_active = true
  AND group_level_id = 22
  AND settled_amount IS NOT NULL
  AND actual_settlement IS NOT NULL
GROUP BY transaction_type;
```

### 17.13 Reverse OMS rows missing reverse/cancelled settlement

```sql
WITH oms_rev AS (
  SELECT DISTINCT order_id
  FROM zs_observe.nykaa_oms
  WHERE is_active = true
    AND transaction_type = 'reverse'
    AND LOWER(final_status) IN ('return','customer returns','rto','reverse')
    AND group_level_id = 22
),
sett_rev AS (
  SELECT DISTINCT order_id
  FROM zs_observe.nykaa_settlement
  WHERE is_active = true
    AND transaction_type IN ('reverse','cancelled')
    AND group_level_id = 22
)
SELECT o.order_id AS unmatched_return
FROM oms_rev o
LEFT JOIN sett_rev s ON o.order_id = s.order_id
WHERE s.order_id IS NULL;
```

### 17.14 OMS vs settlement amount discrepancy

```sql
SELECT
  o.order_id,
  SUM(o.charged_amount) AS oms_charged,
  SUM(s.charged_amount) AS settlement_charged,
  SUM(o.charged_amount) - SUM(s.charged_amount) AS diff
FROM zs_observe.nykaa_oms o
JOIN zs_observe.nykaa_settlement s
  ON o.order_id = s.order_id
  AND o.invoice_number = s.invoice_number
WHERE o.is_active = true
  AND s.is_active = true
  AND o.transaction_type = 'forward'
  AND s.transaction_type = 'forward'
  AND o.group_level_id = 22
  AND s.group_level_id = 22
GROUP BY o.order_id
HAVING ABS(SUM(o.charged_amount) - SUM(s.charged_amount)) > 1
ORDER BY ABS(diff) DESC
LIMIT 100;
```

### 17.15 Shipping adjustment impact on settlement

```sql
SELECT
  s.order_id,
  s.transaction_type,
  ROUND(s.settled_amount, 2) AS settled,
  ROUND(a.diff_shipping_charge, 2) AS shipping_diff,
  ROUND(a.diff_shipping_charge_tax, 2) AS shipping_diff_tax,
  ROUND(s.settled_amount + COALESCE(a.diff_shipping_charge, 0) + COALESCE(a.diff_shipping_charge_tax, 0), 2) AS adjusted_settled
FROM zs_observe.nykaa_settlement s
INNER JOIN zs_observe.nykaa_addition_charge a
  ON s.order_id = a.order_id
  AND s.is_active = true
  AND a.is_active = true
  AND s.group_level_id = 22
  AND a.group_level_id = 22
LIMIT 50;
```

### 17.16 Addition charge present in OMS but missing settlement

```sql
SELECT
  a.order_id,
  a.created_date,
  a.charged_amount,
  a.diff_shipping_charge
FROM zs_observe.nykaa_addition_charge a
INNER JOIN zs_observe.nykaa_oms o
  ON a.order_id = o.order_id
  AND o.is_active = true
  AND o.group_level_id = 22
LEFT JOIN zs_observe.nykaa_settlement s
  ON a.order_id = s.order_id
  AND s.is_active = true
  AND s.group_level_id = 22
WHERE a.is_active = true
  AND a.group_level_id = 22
  AND s.order_id IS NULL
ORDER BY a.created_date DESC;
```

### 17.17 Reversal credit-note coverage

```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT_IF(rversal_cn IS NOT NULL AND rversal_cn <> '') AS rows_with_cn,
  COUNT_IF(already_adjusted IS NOT NULL AND already_adjusted <> '') AS rows_already_adjusted
FROM zs_observe.nykaa_addition_charge
WHERE is_active = true
  AND group_level_id = 22;
```

### 17.18 Delivery success by courier

```sql
SELECT
  transname AS courier,
  COUNT(*) AS total_shipments,
  COUNT_IF(status = 'Delivered') AS delivered,
  COUNT_IF(status = 'RTO Delivered') AS rto,
  COUNT_IF(status = 'Returned') AS returned,
  COUNT_IF(status = 'Cancelled') AS cancelled,
  ROUND(100.0 * COUNT_IF(status = 'Delivered') / COUNT(*), 2) AS delivery_pct,
  ROUND(100.0 * COUNT_IF(status = 'RTO Delivered') / COUNT(*), 2) AS rto_pct
FROM zs_observe.nykaa_mapper_gst
WHERE is_active = true
  AND group_level_id = 22
  AND transname IS NOT NULL
GROUP BY transname
ORDER BY total_shipments DESC;
```

### 17.19 RTO rate by payment mode from mapper GST

```sql
SELECT
  mode AS payment_mode,
  COUNT(*) AS orders,
  COUNT_IF(status = 'RTO Delivered') AS rto_count,
  ROUND(100.0 * COUNT_IF(status = 'RTO Delivered') / COUNT(*), 2) AS rto_rate_pct
FROM zs_observe.nykaa_mapper_gst
WHERE is_active = true
  AND group_level_id = 22
GROUP BY mode;
```

### 17.20 Order-tag fraud/risk analysis

```sql
SELECT
  CASE
    WHEN order_tag LIKE '%Blacklisted%' THEN 'blacklisted_customer'
    WHEN order_tag LIKE '%RTO history%' THEN 'rto_history_check'
    WHEN order_tag LIKE '%Duplicate%' THEN 'duplicate_flag'
    WHEN order_tag LIKE '%Verification%' THEN 'verification_needed'
    WHEN order_tag IS NULL THEN 'no_flag'
    ELSE 'other_tag'
  END AS risk_category,
  COUNT(*) AS orders,
  COUNT_IF(status = 'RTO Delivered') AS rto,
  COUNT_IF(status = 'Delivered') AS delivered,
  ROUND(100.0 * COUNT_IF(status = 'RTO Delivered') / COUNT(*), 2) AS rto_rate
FROM zs_observe.nykaa_mapper_gst
WHERE is_active = true
  AND group_level_id = 22
GROUP BY 1
ORDER BY orders DESC;
```

### 17.21 Return reasons distribution

```sql
SELECT
  return_create_reason,
  COUNT(*) AS returns
FROM zs_observe.nykaa_mapper_gst
WHERE is_active = true
  AND group_level_id = 22
  AND return_create_reason IS NOT NULL
GROUP BY return_create_reason
ORDER BY returns DESC;
```

### 17.22 Join mapper GST to OMS via base magento order ID

```sql
WITH mg_joined AS (
  SELECT
    mg.*,
    array_join(slice(split(mg.magentoorderno, '-'), 1, 3), '-') AS base_order_id
  FROM zs_observe.nykaa_mapper_gst mg
  WHERE mg.is_active = true
    AND mg.group_level_id = 22
    AND mg.magentoorderno IS NOT NULL
)
SELECT
  m.base_order_id,
  m.orderno AS warehouse_orderno,
  m.status AS warehouse_status,
  m.transname AS courier,
  o.final_status AS oms_status,
  o.charged_amount
FROM mg_joined m
INNER JOIN zs_observe.nykaa_oms o
  ON m.base_order_id = o.order_id
  AND o.is_active = true
  AND o.group_level_id = 22
LIMIT 100;
```

### 17.23 Pre-OMS historical orders in mapper GST

```sql
SELECT
  DATE_TRUNC('month', orderdate) AS month,
  COUNT(*) AS orders
FROM zs_observe.nykaa_mapper_gst
WHERE is_active = true
  AND group_level_id = 22
  AND CAST(orderdate AS date) < DATE '2025-01-01'
GROUP BY 1
ORDER BY 1;
```

### 17.24 Canonicalize source GST name via mapping

```sql
SELECT
  o.order_id,
  o.source_gst_name AS raw_source_name,
  m.entity AS canonical_entity,
  m.gstin_of_the_seller AS canonical_gstin
FROM zs_observe.nykaa_oms o
LEFT JOIN zs_observe.nykaa_mapping m
  ON LOWER(TRIM(o.source_gst_name)) = LOWER(TRIM(m.mbtpt_remarks))
WHERE o.is_active = true
  AND o.group_level_id = 22
LIMIT 50;
```

### 17.25 GSTIN-level breakdown using mapping

```sql
SELECT
  m.gstin_of_the_seller,
  m.entity,
  SUBSTR(m.gstin_of_the_seller, 1, 2) AS home_state_code,
  COUNT(DISTINCT o.order_id) AS orders
FROM zs_observe.nykaa_mapping m
LEFT JOIN zs_observe.nykaa_oms o
  ON LOWER(TRIM(o.source_gst_name)) = LOWER(TRIM(m.mbtpt_remarks))
  AND o.is_active = true
  AND o.group_level_id = 22
GROUP BY m.gstin_of_the_seller, m.entity
ORDER BY orders DESC NULLS LAST;
```

---

## 18. Extraction guidance

Expected card families:

```text
Business Hierarchy:
Platform, Platform Context, Platform Account, Account Data Binding, Business Scope Set if reusable.

Data Understanding:
Table, Column, Relationship, Value Profile.

Metric Understanding:
Metric, Metric Implementation, Formula Template, Metric Dependency.

Process Understanding:
Domain, Business Process, Workflow Step, State Transition, Process Variant.

Reconciliation Understanding:
Reconciliation Profile, Reconciliation Side, Reconciliation Unit, Matching Logic, Mismatch Category, Reconciliation Variant.

Execution Guidance:
Query Pattern, Rule, Validation Test, Output Contract, Execution Constraint Set.
```

Nykaa-specific extraction priorities:

### Business Hierarchy extraction

Extract:

- Platform: Nykaa Fashion.
- Platform Context: Nykaa Fashion India.
- Platform Account: seller account represented by `group_level_id = 22`.
- Account Data Binding: `group_level_id = 22` for transactional tables.
- Reference-table exception: no account binding on `nykaa_mapping`.

### Data Understanding extraction

Extract Table Cards for:

- `table.zs_observe.nykaa_oms`
- `table.zs_observe.nykaa_settlement`
- `table.zs_observe.nykaa_addition_charge`
- `table.zs_observe.nykaa_mapper_gst`
- `table.zs_observe.nykaa_mapping`

Extract Relationship Cards for:

- OMS ↔ Settlement by `order_id` and invoice validation.
- OMS ↔ Addition Charge by `order_id`.
- Settlement ↔ Addition Charge by `order_id`.
- Mapper GST ↔ OMS by truncated `magentoorderno`.
- Mapping ↔ transaction source GST name via normalized string match.

Extract Value Profile Cards for:

- OMS `transaction_type`.
- OMS `final_status`.
- Settlement `transaction_type`.
- Settlement `final_status`.
- Payment mode.
- Metadata values: `nf`, `nf_mid`, `popup`, `popup_mid`.
- Mapper GST `status`.
- Mapper GST `return_type`.
- Mapper GST `transname`.
- Mapper GST `order_tag`.
- GST rate values and anomaly handling.

### Metric Understanding extraction

Extract metrics for:

- gross sales / GMV,
- net revenue after returns,
- distinct orders and line items,
- units sold,
- AOV,
- seller realization rate,
- net settlement amount,
- effective commission rate,
- effective take rate,
- shipping adjustment amount,
- return rate,
- RTO rate,
- cancellation rate,
- discount/funding amount,
- TCS amount and observed rate,
- GST rate validation,
- settlement/actual settlement gap,
- reconciliation gap amount.

### Process Understanding extraction

Extract processes for:

- Nykaa forward order-to-settlement flow.
- Nykaa reverse / return / RTO / cancellation flow.
- Shipping charge true-up process.
- Warehouse/courier enrichment process.
- GST/entity canonicalization process.
- Nykaa settlement-to-bank handoff process, conditional on banking KB.

### Reconciliation Understanding extraction

Extract reconciliation profiles for:

- OMS to settlement matching.
- Settlement component waterfall validation.
- Reverse/RTO/cancelled to settlement impact matching.
- Shipping charge true-up reconciliation.
- Mapper GST to OMS mapping.
- Entity/GSTIN canonicalization.
- Nykaa settlement to bank reconciliation note.

### Execution Guidance extraction

Extract rules for:

- required `is_active = true` filters on transactional tables,
- required `group_level_id = 22` on transactional tables,
- no active/group filters on `nykaa_mapping`,
- case normalization for status,
- date field recommendations,
- no migration-residue fields by default,
- no raw cross-transaction aggregation without transaction type filter,
- grain alignment before joins,
- mapper GST join transformation,
- tax anomaly filtering,
- `settled_amount` vs `actual_settlement` distinction,
- no Nykaa.com transactional inference from mapping labels.

### Final extraction principle

```text
Use the same marketplace ingestion script for Nykaa as for Amazon, Flipkart, Myntra, and future marketplaces.
Nykaa-specific knowledge belongs in content modules, not custom ingestion code.
```
