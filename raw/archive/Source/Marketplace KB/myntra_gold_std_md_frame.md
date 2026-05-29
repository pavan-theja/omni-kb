---
title: Myntra Marketplace Knowledge Base
doc_type: marketplace_raw_knowledge
domain: marketplace_finance
platforms: [myntra]
platform_types: [marketplace]
platform_contexts: [myntra.india]
related_domains:
  - marketplace_finance
  - settlement_reconciliation
  - return_analysis
  - fee_reconciliation
  - gst_compliance
  - cash_flow
  - logistics_enrichment
  - payment_reconciliation
  - bank_reconciliation
country: India
currency: INR
primary_scope_keys:
  - group_level_id: <client_id>
primary_entities:
  - Myntra seller / brand group
  - Myntra marketplace seller account
  - GSTIN-linked seller entity
  - Myntra India marketplace context
tables:
  - zs_observe.myntra_oms
  - zs_observe.myntra_settlement
  - zs_observe.myntra_reverse
  - zs_observe.myntra_non_order_settlement
optional_modules:
  - reverse_returns_report
  - non_order_settlement
  - payout_bank_reference
  - settlement_velocity_tracking
  - prepaid_postpaid_settlement_split
  - logistics_awb_enrichment
  - marketplace_to_bank_reconciliation_note
status: draft
owner: finance_data_team
source_documents:
  - Myntra Recon Doc.docx
created_for: ZenStatement Context Engineering KB
intended_ingestion_flow: raw_markdown_to_semantic_chunks_to_intermediate_card_yaml
---

# Myntra Marketplace Knowledge Base

## 1. How to use this document

This is a curated raw markdown knowledge document for Myntra marketplace finance, settlement, returns, and reconciliation.

This document is intentionally not card YAML, not canonical JSON, and not a graph-edge file. It is written as human-readable source knowledge so the ZenStatement ingestion pipeline can later produce semantic chunks, candidate cards, relationships, value profiles, metrics, query patterns, rules, validation tests, output contracts, retrieval indexes, and evidence metadata.

This document should support extraction across these card families:

- Business Hierarchy: platform, platform context, platform account, account data binding, reusable business scope sets if applicable.
- Data Understanding: table, column, relationship, and value profile cards.
- Metric Understanding: metric, metric implementation, formula template, and dependency cards.
- Process Understanding: marketplace order, settlement, return, refund, payout, and non-order adjustment process cards.
- Reconciliation Understanding: OMS-to-settlement, reverse-to-settlement, non-order settlement, payout-to-bank, and UTR-level matching cards.
- Execution Guidance: query patterns, mandatory filters, casting rules, date rules, reconciliation safeguards, and output contracts.

The goal is to keep Myntra aligned to the same marketplace ingestion frame used for Amazon, Flipkart, Nykaa, and future marketplaces, while preserving Myntra-specific concepts such as prepaid/postpaid settlement splits, UTR fields, day-wise settlement tracking, reverse transactions, and non-order settlements.

---

## 2. Marketplace overview and business context

### 2.1 Marketplace role

Myntra is a leading Indian fashion e-commerce marketplace. Sellers list products on Myntra, while Myntra handles the customer-facing marketplace layer: catalog experience, customer payments, delivery coordination, returns, and settlement reporting.

Myntra operates on a marketplace model where the seller retains ownership of inventory and goods, and Myntra earns through commissions, marketplace fees, fulfilment or logistics-related charges, payment gateway fees, marketing charges, royalty charges, and other deductions before settlement.

The primary commercial flow is:

```text
Customer pays Myntra
→ Myntra records the order
→ item is packed / dispatched / delivered
→ Myntra deducts commission, marketplace fees, freight, payment gateway fees, reverse charges, marketing charges, TCS, and TDS
→ Myntra settles the net amount to the seller
```

### 2.2 Seller / brand context

The seller or brand is identified through a combination of `group_level_id`, seller identifiers, seller GST information, client metadata, and source GST information.

Important seller and entity fields include:

- `group_level_id`: client or brand group scope key.
- `group_id`: parent group identifier.
- `seller_id`: seller identifier in OMS.
- `seller_name`: seller registered name in OMS.
- `seller_gstn`: seller GSTIN in OMS.
- `source_gst_id` / `source_gst_name`: source GSTIN and entity fields in settlement and reverse tables.
- `client_name`: client name in settlement and reverse tables.
- `metadata`: client or brand metadata tag in settlement/non-order settlement.

### 2.3 Commercial model

Myntra commercial economics are driven by forward sales, reverse returns/refunds, prepaid and postpaid collections, marketplace commission, MP fees, freight and reverse charges, payment gateway fees, marketing charges, royalty charges, GTA fees, TCS, TDS, and non-order adjustments.

The forward sale flow creates a positive seller receivable after deductions. The reverse flow creates refund or clawback impact. Non-order settlements capture financial movements that are not tied to specific orders, such as penalties, incentives, reimbursements, corrections, marketing reimbursements, or platform charges.

### 2.4 Storefronts, fulfilment, and operational programs

The source document positions Myntra as a fashion marketplace. It does not define a separate sub-platform like Flipkart Shopsy or Nykaa Fashion vs Beauty, but it does include operational signals such as:

- `courier_code`
- `tracking_no`
- `shipping_case`
- `is_try_and_buy`
- `packed_id`
- `packing_date`
- `forward_awb_number`
- `return_awb_number`
- `shipment_zone_classification`

These signals can support logistics enrichment and return flow analysis, but marketplace-level finance should remain distinct from deeper courier/COD/freight reconciliation unless a logistics KB is retrieved.

### 2.5 What this marketplace data can and cannot answer

This Myntra marketplace KB can answer:

- What was sold on Myntra?
- What was settled to the seller?
- What was returned or cancelled?
- What is the split between prepaid and postpaid/COD components?
- What commissions and fees were deducted?
- What freight, reverse, marketing, royalty, and payment gateway charges were applied?
- What TCS and TDS were deducted?
- What remains pending settlement?
- Which UTRs and settlement dates are associated with prepaid and postpaid components?
- Which amounts are non-order adjustments?
- How do OMS, settlement, reverse, and non-order settlement connect?

This document cannot fully answer:

- Actual bank-credit matching unless bank statement data is available.
- Deep courier-level freight/COD reconciliation unless logistics vendor data is available.
- Product profitability after COGS unless cost data is available.
- Exact seller account ownership unless Business Hierarchy and Account Data Binding cards define the tenant/group/account mappings.

---

## 3. Scope and account context

### 3.1 Active platform context

The active platform context is Myntra India.

Recommended normalized platform context:

| Concept | Value |
|---|---|
| Platform | Myntra |
| Platform type | Marketplace |
| Platform context | Myntra India |
| Country | India |
| Currency | INR |
| Domain | marketplace_finance |

### 3.2 Seller / account identifiers

Myntra scope is primarily resolved through `group_level_id`, with supporting identifiers such as seller ID, GSTIN, source GST fields, and client metadata.

Important identifiers:

| Identifier | Where it appears | Business meaning |
|---|---|---|
| `group_level_id` | All main tables | Client/brand group scope key. Use for runtime account filtering. |
| `seller_id` | `myntra_oms` | Myntra seller ID. |
| `seller_name` | `myntra_oms` | Registered seller name. |
| `seller_gstn` | `myntra_oms` | Seller GSTIN. |
| `source_gst_id` | `myntra_settlement`, `myntra_reverse` | Source GSTIN for tax/entity mapping. |
| `source_gst_name` | `myntra_settlement`, `myntra_reverse`, `myntra_non_order_settlement` | Source GST entity name. |
| `client_name` | `myntra_settlement`, `myntra_reverse` | Client or brand name. |
| `metadata` | `myntra_settlement`, `myntra_non_order_settlement` | Client/brand metadata tag. |
| `tenant_id` | `myntra_reverse`, `myntra_non_order_settlement` | Tenant identifier in system metadata. |

### 3.3 Default scope filters

The source document uses `<client_id>` as the placeholder for Myntra `group_level_id`. Account-specific filters should be produced through Account Data Binding during extraction, not hardcoded into table or metric cards.

Common scope pattern:

```sql
WHERE group_level_id = <client_id>
```

Table-specific filter pattern:

| Table | Scope filter | Active filter |
|---|---|---|
| `zs_observe.myntra_oms` | `group_level_id = '<client_id>'` or typed equivalent | No `is_active` column in source notes |
| `zs_observe.myntra_settlement` | `group_level_id = <client_id>` | `is_active = true` |
| `zs_observe.myntra_reverse` | `group_level_id = <client_id>` | `is_active = true` |
| `zs_observe.myntra_non_order_settlement` | `group_level_id = <client_id>` | `is_active = true` |

### 3.4 Table-specific scope differences

`myntra_oms` stores many fields, including `group_level_id`, as string. Its amount and date fields are also string-heavy. Settlement, reverse, and non-order settlement tables use typed financial fields and mandatory active filters.

Do not assume that the exact same data type for `group_level_id` applies across all tables. The ingestion pipeline should preserve table-specific type caveats and the execution layer should cast or compare appropriately.

### 3.5 Reference-table exceptions

The source relationship map mentions additional Myntra-related tables that may exist or may be available in some environments:

- `myntra_oms_settlement`
- `myntra_seller_report_forward`
- `myntra_seller_report_reverse`
- `myntra_expenses`
- `myntra_receivables`

These are not described with full table dictionaries in the provided source. Treat them as adjacent or potential supporting tables until validated in the warehouse.

### 3.6 Scope caveats

- `group_level_id` is the mandatory business scope key across Myntra analysis.
- `myntra_oms` does not have `is_active` per source notes; do not blindly apply active filters to it.
- `myntra_settlement`, `myntra_reverse`, and `myntra_non_order_settlement` require `is_active = true`.
- OMS uses string-heavy fields, so group and amount filters may need explicit casting depending on warehouse schema.
- Account filters belong to Account Data Binding cards, not directly inside Metric Implementation or Table cards.

---

## 4. Table family overview

| Table | Business role | Grain | Primary use | Required filters | Important caveats |
|---|---|---|---|---|---|
| `zs_observe.myntra_oms` | Order master / forward order source | One row per line item/SKU within an order at packing/dispatch | Gross sales, product, tax, customer, seller, logistics, payment split | `group_level_id`; no `is_active` per source notes | Almost all columns are strings; no `transaction_type`; amount/date casting required |
| `zs_observe.myntra_settlement` | Core settlement ledger | One row per settled line item with financial breakup | Net settlement, commissions, fees, prepaid/postpaid split, UTRs, payout dates, settlement velocity | `is_active = true`, `group_level_id` | Contains forward/reverse rows, NULL internal classifications, day_1 to day_31 columns, many settlement components |
| `zs_observe.myntra_reverse` | Return and refund table | One row per returned or cancelled item | Return/refund impact, reverse tax/TCS/TDS, return AWB, cancellation status | `is_active = true`, `group_level_id` | `transaction_type` always reverse; `order_status` can be `cancelled` or NULL |
| `zs_observe.myntra_non_order_settlement` | Non-order settlement ledger | One row per non-order financial entry | Penalties, incentives, reimbursements, corrections, platform charges | `is_active = true`, `group_level_id` | May be empty for some clients; does not join to OMS/reverse by order ID |

Adjacent table families mentioned but not fully described:

| Table | Business role | Status in source |
|---|---|---|
| `myntra_oms_settlement` | OMS-to-settlement reconciliation report | Mentioned for Level 1 reconciliation; schema not fully described |
| `myntra_seller_report_forward` | Dispatch/forward seller report | Mentioned in relationship map; schema not fully described |
| `myntra_seller_report_reverse` | Return seller report | Mentioned in relationship map; schema not fully described |
| `myntra_expenses` | Penalties/expenses | Mentioned in relationship map; schema not fully described |
| `myntra_receivables` | Aging and pending receivables | Mentioned in relationship map and SQL example; schema not fully described |

---

## 5. End-to-end transaction lifecycle

### 5.1 Forward flow: order to settlement

A forward transaction represents a successful sale where the product moves from seller or warehouse to the customer.

Expected business flow:

```text
Customer places order on Myntra
→ order appears in myntra_oms using order_created_date
→ seller/warehouse packs or dispatches item using packing_date
→ invoice is generated using invoice_number
→ product is delivered to customer
→ settlement appears in myntra_settlement where transaction_type = 'forward'
→ Myntra deducts commission, marketplace fees, payment gateway fee, freight, marketing, TCS, TDS, and other applicable charges
→ seller receives net settled amount
```

Primary tables:

- `myntra_oms`: order-side sales and product evidence.
- `myntra_settlement`: settlement-side financial truth.

Key identifiers:

- `myntra_oms.order_code`
- `myntra_settlement.order_id`
- `invoice_number`
- `item_id`
- `sku_code` / `sku_id`

### 5.2 Reverse flow: return, cancellation, refund, and seller clawback

A reverse transaction represents a return, refund, or cancellation where value flows back from seller account to customer or marketplace.

Expected business flow:

```text
Customer initiates return or order/item is cancelled
→ reverse record appears in myntra_reverse
→ return logistics information is captured through return_awb_number and forward_awb_number
→ customer refund is processed through refund_amount
→ reverse settlement adjustment appears in myntra_settlement where transaction_type = 'reverse'
→ seller account is debited or adjusted
```

Primary tables:

- `myntra_reverse`: detailed return/refund source.
- `myntra_settlement`: financial settlement impact of reverse transactions.
- `myntra_oms`: original order context.

Important semantics:

- `myntra_reverse.transaction_type` is always `reverse`.
- `myntra_reverse.order_status = 'cancelled'` means cancelled item/order.
- `myntra_reverse.order_status IS NULL` indicates a return without explicit cancellation flag, usually customer-initiated return.
- `refund_amount` is the key financial metric for return impact.

### 5.3 Adjustment flow: non-order settlements and non-base commercial movements

Myntra also records financial movements that are not tied to a specific order. These are captured in `myntra_non_order_settlement`.

Typical non-order movements include:

- penalties for SLA violations or late dispatch,
- incentives or performance bonuses,
- promotional credits,
- corrections,
- marketing reimbursements,
- platform-level charges,
- other financial adjustments not attributable to one order.

Expected business flow:

```text
Commercial or operational event occurs
→ Myntra creates non-order settlement entry
→ amount is settled or deducted at settlement cycle level
→ entry may not join to OMS or reverse tables
→ seller-level settlement and realization analysis must include these rows when calculating total cash impact
```

### 5.4 Payout flow: settlement to seller bank

Myntra settlement contains payout-enrichment fields such as settlement dates and UTRs. Unlike a pure marketplace-only table, Myntra settlement can support marketplace-to-bank reconciliation notes when bank statement data is available.

Important payout references include:

- `utr_prepaid_commision`
- `utr_prepaid_mp_fees`
- `utr_prepaid_payment`
- `utr_postpaid_commision`
- `utr_postpaid_mp_fees`
- `utr_postpaid_payment`
- `settlement_prepaid_commision_date`
- `settlement_prepaid_mp_fees_date`
- `settlement_prepaid_payment_date`
- `settlement_postpaid_commision_date`
- `settlement_postpaid_mp_fees_date`
- `settlement_postpaid_payment_date`
- `settlement_date` in non-order settlement

Payout-side reconciliation should not compare order-level rows directly to bank statement rows. It should first aggregate or identify the relevant UTR/payment component grain.

### 5.5 Timing gaps and in-flight transactions

Timing gaps can occur when:

- order exists in OMS but has not yet settled,
- return exists but refund or reverse settlement has not yet completed,
- settlement component is pending,
- prepaid and postpaid settlement streams settle at different times,
- non-order adjustments settle in a later cycle,
- bank credit is delayed relative to settlement/UTR date.

Fields supporting timing and pending analysis:

- `myntra_oms.order_created_date`
- `myntra_oms.packing_date`
- `myntra_settlement.packing_date`
- settlement prepaid/postpaid date fields,
- `myntra_settlement.amount_pending_settlement`,
- `myntra_settlement.day_1` to `day_31`,
- `myntra_reverse.created_date`,
- `myntra_reverse.return_date`,
- `myntra_reverse.settlement_date`,
- `myntra_non_order_settlement.settlement_date`.

---

## 6. Entity relationships and joins

### 6.1 Primary join map

| From table | To table | Join key | Reliability / notes |
|---|---|---|---|
| `myntra_oms` | `myntra_settlement` | `myntra_oms.order_code = myntra_settlement.order_id`; validate with `invoice_number` where available | Primary OMS-to-settlement join. Settlement can contain both forward and reverse rows. |
| `myntra_oms` | `myntra_reverse` | `myntra_oms.order_code = myntra_reverse.order_id` | Adds original order context to return/refund rows. |
| `myntra_settlement` | `myntra_reverse` | `order_id + item_id` | Links reverse settlement to return/refund record. Use `transaction_type = 'reverse'` in settlement. |
| `myntra_settlement` | `myntra_non_order_settlement` | No order-level join | Combine at settlement cycle, date, client, or reporting level only. |
| `myntra_oms` | `myntra_seller_report_forward` | `order_id` / source-equivalent | Mentioned in source relationship map; validate schema before use. |
| `myntra_oms` | `myntra_seller_report_reverse` | `order_id` / source-equivalent | Mentioned in source relationship map; validate schema before use. |
| `myntra_oms` | `myntra_expenses` | `order_id` | Mentioned in source relationship map; validate schema before use. |
| `myntra_oms` | `myntra_receivables` | `order_id` | Mentioned in source relationship map; used for pending receivables/aging if available. |

### 6.2 Secondary validation keys

Use these supporting fields to validate joins:

- `invoice_number`
- `item_id`
- `sku_code` / `sku_id`
- `packed_id`
- `tracking_no`
- `forward_awb_number`
- `return_awb_number`
- `settlement_id`
- UTR fields
- `source_gst_id`
- `metadata`

### 6.3 Join reliability and match rates

The source document defines `myntra_oms_settlement` as a Level 1 reconciliation table/report with `recon_status` values such as `Matched` and `Amount yet to deducted`. If that table exists and is validated, it can be used as a high-level reconciliation aid.

Without that table, joins should be performed directly using OMS and settlement identifiers, with careful grain control and validation.

### 6.4 Grain mismatch and double-counting risks

Major grain risks:

- `myntra_oms` is a forward order line/SKU-line source.
- `myntra_settlement` contains both forward and reverse transaction rows.
- `myntra_reverse` contains return/refund rows and may not be one-to-one with settlement if partial returns or multiple items exist.
- `myntra_non_order_settlement` is not order-level and should not be joined to OMS by order.
- Prepaid/postpaid components in settlement are split across many component columns and dates; do not sum all columns without understanding whether they overlap or represent separate components.
- Day-wise `day_1` to `day_31` fields are settlement velocity/aging fields, not base transaction amount fields.

### 6.5 Identifier normalization rules

Myntra does not have the Flipkart-style `OD` prefix issue in the source document, but it does use different field names across tables:

| Concept | OMS field | Settlement field | Reverse field |
|---|---|---|---|
| Order ID | `order_code` | `order_id` | `order_id` |
| SKU | `sku_code` | `sku_id` | `sku_id` |
| Invoice | `invoice_number` | `invoice_number` | `invoice_number` |
| Shipment / tracking | `tracking_no`, `packed_id` | `packing_date`, shipment zone fields | `forward_awb_number`, `return_awb_number` |

### 6.6 Reference / mapping table joins

No dedicated GST mapper/entity mapping table is described in the source for Myntra. Entity and tax enrichment should use embedded fields such as seller GST, source GST, destination state, seller state, product tax category, and supply type.

If external GST or entity mapping tables are added later, they should be handled as reference-table modules without changing the marketplace ingestion frame.

---

## 7. Financial waterfall and seller realization

### 7.1 Forward settlement waterfall

Myntra forward settlement starts from the customer charged amount and deducts marketplace economics before seller settlement.

Formula concept from the source:

```text
settled_amount
= charged_amount
- gross_commission
- mp_fees
- freight_charge
- marketing_charges
- reverse_charges
- TCS
- TDS
+ commission_discount
```

More detailed component interpretation:

```text
Net seller settlement
= customer charged amount / seller product amount
- gross commission
- marketplace fees
- fixed fee
- pick and pack fee
- payment gateway fee
- freight charge
- freight GST
- GTA fees
- marketing charges
- royalty charges
- additional forward charges
- TCS
- TDS
+ commission discount
+ eligible adjustments
```

Primary table: `myntra_settlement`.

Primary output field: `settled_amount`.

### 7.2 Reverse / refund settlement waterfall

Reverse transactions represent return, refund, or cancellation impact. The seller account is debited or adjusted when the customer refund or reverse settlement occurs.

Reverse waterfall concept:

```text
Reverse impact
= refund amount / reverse charged amount
+ tax reversal
+ TCS/TDS reversal where applicable
+ reverse logistics or reverse prepaid/postpaid charges
+ any reverse settlement adjustment
```

Primary tables:

- `myntra_reverse` for refund details.
- `myntra_settlement` where `transaction_type = 'reverse'` for financial settlement impact.

Key reverse fields:

- `refund_amount`
- `charged_amount`
- `charged_amount_excluding_tax`
- `total_tax`
- `total_tcs_amount`
- `total_tds`
- `reverse_prepaid_charges`
- `reverse_postpaid_charges`
- `return_awb_number`
- `forward_awb_number`

### 7.3 Non-order / adjustment waterfall

Non-order settlement entries should be included when calculating total seller cash impact but should not be attributed to individual orders unless a validated reference exists.

Non-order amount interpretation:

```text
Total non-order impact = SUM(settled_amount) from myntra_non_order_settlement
```

Positive amounts may represent incentives, reimbursements, or credits. Negative amounts may represent penalties, deductions, or platform-level charges.

### 7.4 Seller realization definition

Seller realization rate measures the percentage of gross sale value that reaches the seller after Myntra deductions, returns, and adjustments.

Default concept:

```text
Seller realization rate = net settled amount / gross sale amount
```

Recommended Myntra implementation concept:

```text
SUM(myntra_settlement.settled_amount)
/
SUM(myntra_settlement.charged_amount where transaction_type = 'forward')
```

Alternative denominator, depending on analysis:

- `myntra_oms.total_amount` for OMS-sourced gross sales.
- `myntra_settlement.charged_amount` for settlement-sourced gross sale value.
- `sales_amount` / `sales_settled_amount` if using `myntra_oms_settlement` reconciliation report.

Caveat: decide whether to include reverse and non-order rows in the numerator depending on whether the metric is order-level realization or total cash realization.

### 7.5 Field-level payout interpretation

| Field | Table | Meaning |
|---|---|---|
| `settled_amount` | `myntra_settlement` | Net seller settlement after deductions. Primary payout metric. |
| `amount_pending_settlement` | `myntra_settlement` | Amount still pending settlement. |
| `series_settled_value` | `myntra_settlement` | Settled value from series/cycle. |
| `total_actual_settlement` | `myntra_settlement` | Actual total settlement received. |
| `difference_in_settled` | `myntra_settlement` | Difference between expected/series and actual settlement. |
| `settled_amount` | `myntra_non_order_settlement` | Net settlement impact for non-order financial movement. |
| `refund_amount` | `myntra_reverse` | Actual refund amount to customer. |

### 7.6 Known benchmark ranges or observed snapshots

The source document does not provide Myntra-specific benchmark ranges for realization, return rate, or settlement cycle. Use marketplace-level benchmarks only if separately curated, and do not import Amazon/Flipkart benchmark ranges into Myntra without validation.

---

## 8. Fees, deductions, taxes, promotions, and adjustments

### 8.1 Commission and marketplace fees

Myntra deducts commission and marketplace fees before settlement.

Key fields in `myntra_settlement`:

| Field | Meaning |
|---|---|
| `gross_commission` | Total marketplace commission. |
| `commission_percentage` | Commission rate applied. |
| `commission_discount` | Commission discount or waiver. |
| `commission_excluding_tcs_tds` | Commission net of TCS/TDS. |
| `prepaid_commission` / `postpaid_commission` | Commission split by payment mode. |
| `mp_fees` | Total marketplace fees. |
| `prepaid_mp_fees` / `postpaid_mp_fees` | Marketplace fees split by payment mode. |

### 8.2 Fixed / closing / platform fees

`fixed_fee` is the fixed platform charge per transaction. It should be treated as a marketplace/platform deduction and included in effective fee-rate calculations where present.

### 8.3 Shipping, freight, fulfilment, and reverse logistics fees

Myntra settlement includes several logistics-related fees:

| Field | Meaning |
|---|---|
| `freight_charge` | Forward logistics or freight charge. |
| `freight_charge_gst` | GST on freight charge. |
| `gta_fees` | Goods Transport Agency fees. |
| `pick_and_pack_fee` | Fulfilment handling fee. |
| `reverse_prepaid_charges` | Reverse logistics charges linked to prepaid stream. |
| `reverse_postpaid_charges` | Reverse logistics charges linked to postpaid/COD stream. |
| `shipment_zone_classification` | Shipping zone classification. |

Reverse logistics can also be investigated using `myntra_reverse.forward_awb_number` and `myntra_reverse.return_awb_number`.

### 8.4 Payment / collection / payment gateway fees

Myntra settlement includes `payment_gateway_fee`, and also separates payment values into prepaid and postpaid streams.

Important fields:

- `payment_gateway_fee`
- `prepaid_payment`
- `postpaid_payment`
- `payment_method` in OMS
- `prepaid_amount` and `postpaid_amount` in OMS
- prepaid/postpaid settlement dates
- prepaid/postpaid UTRs

Do not treat payment captured as equivalent to bank-realized cash. UTR/bank reconciliation requires bank statement data.

### 8.5 Promotional credits, discounts, and rebates

Myntra data includes customer and seller-side discount concepts:

- `discount_amount` in OMS,
- `coupon_discount` in OMS,
- `postpaid_coupon_discount` in settlement,
- `commission_discount` in settlement,
- possible incentives or promotional credits in non-order settlement.

These should be separated from marketplace fees and from seller realization numerator/denominator depending on the metric.

### 8.6 Reimbursements, incentives, penalties, and non-order adjustments

`myntra_non_order_settlement` captures non-order financial movements, including:

- penalties,
- incentives,
- performance bonuses,
- marketing reimbursements,
- corrections,
- platform charges,
- other non-order deductions or credits.

These can affect total seller cash flow even when they do not tie to an order.

### 8.7 TCS and TDS

Myntra deducts TCS and TDS as part of marketplace settlement.

TCS fields:

- `total_tcs_amount`
- `tcs_igst_rate` / `tcs_igst_amount`
- `tcs_cgst_rate` / `tcs_cgst_amount`
- `tcs_sgst_rate` / `tcs_sgst_amount`
- `tcs_amount_prepaid`
- `tcs_amount_postpaid`

TDS fields:

- `total_tds`
- `tds_amount`
- `tds_amount_prepaid`
- `tds_amount_postpaid`

TCS is collected under GST rules, and TDS is deducted on seller payments. Both affect cash flow and should be handled explicitly in realization and tax analysis.

### 8.8 GST on products and GST on marketplace fees

GST is represented through CGST, SGST, and IGST fields.

OMS tax fields are string-heavy and must be cast before aggregation:

- `cgst_rate`, `cgst_amount`
- `sgst_rate`, `sgst_amount`
- `igst_rate`, `igst_amount`
- `cess_rate`, `cess_amount`
- `tax_rate`

Settlement and reverse tables use typed financial fields for tax components.

Supply classification:

- `supply_type` in OMS helps determine intra-state vs inter-state supply.
- seller/source and customer/destination states support GST classification.

### 8.9 Fee recovery on returns

The source document does not give explicit fee recovery percentages for Myntra. Fee recovery should be inferred through reverse settlement, reverse charges, refund amounts, and TCS/TDS reversal fields.

Do not assume Amazon-style partial fee recovery rates for Myntra. Create a Myntra-specific fee recovery metric only when reverse and settlement fields are reconciled.

### 8.10 Marketplace-specific naming traps

- `gross_commission` is not the same as total marketplace fees.
- `mp_fees` is broader than commission.
- `commission_discount` is a credit/waiver and should not be treated as a deduction.
- `freight_charge` and `freight_charge_gst` should be separated.
- prepaid and postpaid fields are separate streams and should not be collapsed blindly.
- UTR fields are component-specific, not one universal settlement UTR.
- `day_1` to `day_31` are settlement velocity fields, not base order fields.
- `myntra_oms.total_amount` is string and must be cast.

---

## 9. Fulfilment, logistics, payment modes, and settlement cycle

### 9.1 Fulfilment models

The source document describes the forward lifecycle as seller/warehouse to customer. It does not define a specific FBF/NFBF equivalent model, but it includes warehouse, packing, courier, and shipment fields.

Operational fields:

- `packing_date`
- `packed_id`
- `tracking_no`
- `courier_code`
- `shipping_case`
- `shipment_zone_classification`
- `is_try_and_buy`

### 9.2 Logistics and courier signals

Myntra logistics signals appear in both OMS and reverse tables.

OMS:

- `courier_code`
- `tracking_no`
- `packed_id`
- `shipping_case`

Reverse:

- `forward_awb_number`
- `return_awb_number`
- `return_date`

Use these fields for marketplace-level logistics enrichment. Retrieve logistics KB only if the user asks for courier-level COD, AWB, freight, RTO, or bank remittance analysis and corresponding logistics vendor data exists.

### 9.3 COD vs prepaid / postpaid behavior

Myntra splits payment and settlement components into prepaid and postpaid streams.

Payment modes:

| Mode | Meaning |
|---|---|
| Prepaid | Customer paid online before delivery using UPI, card, wallet, or similar. |
| Postpaid / COD | Customer pays at delivery; Myntra collects and later remits/settles to seller. |

Important fields:

- `payment_method`
- `prepaid_amount`
- `postpaid_amount`
- `prepaid_payment`
- `postpaid_payment`
- prepaid/postpaid commission fields
- prepaid/postpaid MP fee fields
- prepaid/postpaid TCS/TDS fields
- prepaid/postpaid UTR fields
- prepaid/postpaid settlement date fields

### 9.4 Settlement cycle and payout timing

Myntra settlement timing can be analyzed through component-specific settlement dates and settlement velocity fields.

Important date fields:

- `settlement_prepaid_commision_date`
- `settlement_prepaid_mp_fees_date`
- `settlement_prepaid_payment_date`
- `settlement_postpaid_commision_date`
- `settlement_postpaid_mp_fees_date`
- `settlement_postpaid_payment_date`
- `packing_date`
- `settlement_date` in reverse and non-order tables

Day-wise settlement tracking:

- `day_1` through `day_31` track daily settlement amounts across a month.
- These fields support settlement velocity/aging analysis.

### 9.5 Bank / UTR / payout references

Myntra settlement provides UTR references by component and payment stream:

| UTR field | Meaning |
|---|---|
| `utr_prepaid_commision` | UTR for prepaid commission settlement component. |
| `utr_prepaid_mp_fees` | UTR for prepaid marketplace fee component. |
| `utr_prepaid_payment` | UTR for prepaid payment component. |
| `utr_postpaid_commision` | UTR for postpaid commission component. |
| `utr_postpaid_mp_fees` | UTR for postpaid marketplace fee component. |
| `utr_postpaid_payment` | UTR for postpaid payment component. |

These fields can support marketplace-to-bank or settlement-to-bank reconciliation when bank statement data is available.

### 9.6 Logistics handoff to logistics KB

Do not always expand into the logistics KB for Myntra questions.

Expand into logistics only when the user asks about:

- courier,
- AWB,
- forward or return shipment,
- COD remittance,
- freight,
- RTO,
- delivery failures,
- return pickup,
- courier-level settlement.

For pure seller realization, commission, TCS/TDS, or marketplace settlement questions, stay within the Myntra marketplace KB unless the metric explicitly depends on logistics data.

---

## 10. Status and value semantics

### 10.1 Transaction types

| Field | Raw value | Business meaning | Include in metrics? | Notes |
|---|---|---|---|---|
| `myntra_settlement.transaction_type` | `forward` | Sale/dispatch transaction | Yes for gross sales and forward settlement | Combine with `internal_txn_type = 'sales'` where needed |
| `myntra_settlement.transaction_type` | `reverse` | Return/refund transaction | Yes for return/refund impact and net revenue | Join to `myntra_reverse` using order/item fields |
| `myntra_reverse.transaction_type` | `reverse` | Return/refund row | Yes for return impact | Always reverse per source |

### 10.2 Internal transaction types

| Field | Raw value | Meaning | Notes |
|---|---|---|---|
| `internal_txn_type` | `sales` | Confirmed sale transaction | Typically paired with settlement `forward` |
| `internal_txn_type` | `reverse` | Confirmed return/refund | Typically paired with settlement `reverse` |
| `internal_txn_type` | `NULL` | Unclassified | May be edge case or data issue; do not drop blindly |

### 10.3 Final statuses / order statuses

| Table | Field | Value | Business meaning |
|---|---|---|---|
| `myntra_reverse` | `order_status` | `cancelled` | Order or item was cancelled before or after delivery |
| `myntra_reverse` | `order_status` | `NULL` | Return without explicit cancellation status, likely customer-initiated return |

### 10.4 Payment modes

| Mode | Meaning |
|---|---|
| Prepaid | Customer paid online before delivery. |
| Postpaid / COD | Cash on delivery; settlement/remittance can follow a separate timing path. |

### 10.5 Fulfilment and logistics values

The source does not enumerate fulfilment models as explicit categories. Use logistics fields such as `courier_code`, `shipping_case`, `shipment_zone_classification`, `tracking_no`, and AWB fields for operational segmentation.

### 10.6 Document types / credit-debit notes

Myntra source focuses on invoices and reverse invoice/reference fields rather than a dedicated credit/debit note taxonomy. Use `invoice_number`, `settlement_id`, reverse fields, and non-order settlement references for settlement documentation.

### 10.7 Fee names and fee descriptions

Myntra fee semantics are column-driven rather than line-item description-driven. Important fee families include gross commission, MP fees, fixed fee, payment gateway fee, pick and pack fee, freight charge, GTA fees, marketing charges, royalty charges, reverse prepaid/postpaid charges, and forward additional charges.

### 10.8 Null and unknown handling

- `internal_txn_type = NULL` can be financially meaningful and should not be dropped without inspection.
- `order_status = NULL` in reverse does not mean invalid; it may mean customer return rather than cancellation.
- Non-order settlement may be empty for some clients; absence does not imply no adjustments unless source coverage is confirmed.
- Missing UTR fields may mean unsettled, pending, or unlinked payout components depending on date and status context.

---

## 11. Key metrics and business definitions

### 11.1 Gross sales / GMV

Gross sales represent total sale value before deductions.

Default sources:

- `myntra_oms.total_amount` after casting to numeric.
- `myntra_settlement.charged_amount` for settlement-sourced forward rows.

Formula concept:

```text
SUM(total_amount) from OMS
or
SUM(charged_amount where transaction_type = 'forward') from settlement
```

Caveats:

- `myntra_oms.total_amount` is string and must be cast.
- Settlement includes forward and reverse rows; filter to forward for gross sales.

### 11.2 Net revenue after returns

Net revenue accounts for returns/refunds.

Formula concept:

```text
Forward charged amount - reverse/refund amount
```

Possible implementation:

```text
SUM(charged_amount where transaction_type = 'forward')
+
SUM(charged_amount or refund impact where transaction_type = 'reverse')
```

Settlement-side implementation:

```sql
SELECT SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount
                WHEN transaction_type = 'reverse' THEN -charged_amount
                ELSE 0 END) AS net_revenue
FROM zs_observe.myntra_settlement
WHERE is_active = true
```

Caveat: understand sign convention before adding reverse rows.

### 11.3 Distinct orders and line items

Order count uses distinct `order_code` in OMS or distinct `order_id` in settlement.

Line-item count uses `item_id`, `sku_code`, or `sku_id` depending on table.

OMS-side counts:

```sql
SELECT COUNT(DISTINCT order_code) AS distinct_orders,
       COUNT(DISTINCT order_code || sku_code) AS distinct_order_items
FROM zs_observe.myntra_oms
```

Settlement-side counts (forward only):

```sql
SELECT COUNT(DISTINCT order_id) AS distinct_orders,
       COUNT(DISTINCT order_id || item_id) AS distinct_order_items
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
```

### 11.4 Units sold

Units sold should use quantity fields where available. OMS is the preferred source for order-line detail. Settlement and reverse tables also contain item-level context but may not always be the best sales-unit source.

OMS-side units (line-count proxy — `myntra_oms` is one row per line-item/SKU within an order, no explicit quantity field is documented):

```sql
SELECT COUNT(*) AS units_sold_line_proxy
FROM zs_observe.myntra_oms
```

Reverse-side returned-unit count (for return-impact analysis only):

```sql
SELECT SUM(quantity) AS returned_units
FROM zs_observe.myntra_reverse
WHERE is_active = true
```

Treat as low-confidence until a forward-side quantity field is confirmed against the live schema. Account scope is applied through Account Data Binding.

### 11.5 Average order value

AOV measures average gross order value.

Formula concept:

```text
Gross sales / distinct forward orders
```

Use forward transactions only.

Settlement-side AOV:

```sql
SELECT SUM(charged_amount) * 1.0
       / NULLIF(COUNT(DISTINCT order_id), 0) AS aov
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
```

### 11.6 Seller realization rate

Seller realization rate measures what percentage of gross sale value reaches the seller after marketplace deductions, refunds, and adjustments.

Formula concept:

```text
SUM(settled_amount) / SUM(gross sale amount)
```

Recommended source: `myntra_settlement`.

Caveats:

- Decide whether numerator includes reverse and non-order rows.
- Denominator should usually use forward sale amount.
- Account scope must come from Account Data Binding.

### 11.7 Net settlement amount

Net settlement amount is the sum of `settled_amount` from settlement rows, plus non-order settlement impact if the business question asks for total seller cash impact.

Formula concept:

```text
SUM(myntra_settlement.settled_amount)
+
SUM(myntra_non_order_settlement.settled_amount, if included)
```

### 11.8 Effective commission rate

Effective commission rate measures commission burden relative to charged amount or seller product amount.

Formula concept:

```text
SUM(gross_commission) / SUM(charged_amount)
```

Use forward rows unless analyzing reverse recovery.

### 11.9 Effective fee / take rate

Effective fee rate measures total marketplace deductions as a percentage of gross sale.

Possible fee components:

- `gross_commission`
- `mp_fees`
- `fixed_fee`
- `pick_and_pack_fee`
- `payment_gateway_fee`
- `freight_charge`
- `freight_charge_gst`
- `gta_fees`
- `marketing_charges_prepaid/postpaid`
- `royaltycharges_prepaid/postpaid`
- `forward_additional_charges_prepaid/postpaid`
- reverse charges if calculating net fee burden after returns

Settlement-side fee aggregate:

```sql
SELECT ABS(SUM(COALESCE(gross_commission, 0)
                + COALESCE(mp_fees, 0)
                + COALESCE(fixed_fee, 0)
                + COALESCE(pick_and_pack_fee, 0)
                + COALESCE(payment_gateway_fee, 0)
                + COALESCE(freight_charge, 0)
                + COALESCE(freight_charge_gst, 0)
                + COALESCE(gta_fees, 0)))
       / NULLIF(SUM(charged_amount), 0) AS effective_fee_rate
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
```

### 11.10 Shipping / freight cost rate

Formula concept:

```text
SUM(freight_charge + freight_charge_gst + gta_fees + reverse charges where applicable)
/
SUM(charged_amount)
```

Use logistics fields if segmenting by courier, AWB, or zone.

### 11.11 Return rate

Return rate measures reverse transactions relative to forward transactions.

Formula concept:

```text
COUNT(DISTINCT reverse order_id) / COUNT(DISTINCT forward order_id)
```

Settlement implementation can use `transaction_type = 'reverse'` and `transaction_type = 'forward'`. Reverse table can be used for return details.

### 11.12 RTO rate

The source does not explicitly define RTO status values. RTO should not be inferred unless a status, return AWB pattern, shipping case, or logistics table confirms it.

Placeholder using reverse-side AWB / shipping-case fields — must be validated against a logistics KB before production use:

```sql
SELECT 1.0 * COUNT(DISTINCT CASE
                              WHEN shipping_case ILIKE '%rto%'
                                OR LOWER(order_status) = 'rto'
                              THEN order_id || item_id END)
       / NULLIF(COUNT(DISTINCT order_id || item_id), 0) AS rto_rate
FROM zs_observe.myntra_reverse
WHERE is_active = true
```

Treat as low-confidence — RTO classification needs cross-validation with the logistics KB. Account scope is applied through Account Data Binding.

### 11.13 Cancellation rate

Cancellation can be identified in `myntra_reverse.order_status = 'cancelled'`.

Formula concept:

```text
COUNT(DISTINCT order_id where order_status = 'cancelled')
/
COUNT(DISTINCT original orders)
```

### 11.14 Cashback / offer rate

No dedicated cashback table is described for Myntra. Promotion/discount analysis should use OMS discount/coupon fields and settlement discount/commission discount fields.

Potential fields:

- `discount_amount`
- `coupon_discount`
- `postpaid_coupon_discount`
- `commission_discount`

OMS-side discount/offer aggregate (forward orders):

```sql
SELECT SUM(COALESCE(discount_amount, 0)
            + COALESCE(coupon_discount, 0)) AS total_offer_outflow
FROM zs_observe.myntra_oms
```

Settlement-side discount aggregate:

```sql
SELECT SUM(COALESCE(postpaid_coupon_discount, 0)
            + COALESCE(commission_discount, 0)) AS settlement_offer_impact
FROM zs_observe.myntra_settlement
WHERE is_active = true
```

Treat as low-confidence proxy for cashback/offer outflow — Myntra has no Flipkart-style cashback credit/debit note ledger. Account scope is applied through Account Data Binding.

### 11.15 Fee recovery rate on returns

Myntra fee recovery should be derived from reverse settlements and reverse charge fields, not assumed.

Formula concept:

```text
fees reversed or credited on reverse transactions
/
fees originally charged on forward transactions
```

Settlement-side fee recovery:

```sql
SELECT ABS(SUM(CASE WHEN transaction_type = 'reverse'
                     THEN COALESCE(gross_commission, 0) + COALESCE(mp_fees, 0)
                     ELSE 0 END))
       / NULLIF(ABS(SUM(CASE WHEN transaction_type = 'forward'
                              THEN COALESCE(gross_commission, 0) + COALESCE(mp_fees, 0)
                              ELSE 0 END)), 0) AS fee_recovery_rate
FROM zs_observe.myntra_settlement
WHERE is_active = true
```

Requires careful matching by `order_id + item_id`.

### 11.16 TCS/TDS amount and rate

TCS/TDS should be reported separately from permanent fees because tax deductions may be recoverable or creditable depending on tax filing.

Formula concepts:

```text
TCS rate = SUM(total_tcs_amount) / taxable base
TDS rate = SUM(total_tds) / seller payment or taxable base
```

### 11.17 GST rate validation

GST validation compares CGST+SGST or IGST against taxable amount and supply type.

Settlement-side effective GST rate:

```sql
SELECT SUM(total_tax)
       / NULLIF(SUM(charged_amount_excluding_tax), 0) AS effective_gst_rate
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
```

Component-level CGST/SGST/IGST consistency check:

```sql
SELECT order_id, item_id,
       tax_cgst_amount + tax_sgst_amount AS cgst_sgst_total,
       tax_igst_amount,
       total_tax,
       (COALESCE(tax_cgst_amount, 0) + COALESCE(tax_sgst_amount, 0)
        + COALESCE(tax_igst_amount, 0)) - COALESCE(total_tax, 0) AS gst_component_gap
FROM zs_observe.myntra_settlement
WHERE is_active = true
```

Account scope is applied through Account Data Binding.

Use OMS and settlement tax fields, with casting for OMS.

### 11.18 Settlement cycle / payout lag

Settlement lag can be measured using order/packing dates against settlement date fields.

Potential formula:

```text
DATE_DIFF('day', packing_date, settlement_component_date)
```

Use component-specific prepaid/postpaid dates depending on the settlement stream.

### 11.19 Reconciliation gap amount

Gap amount depends on the reconciliation profile.

Examples:

```text
OMS sales amount - settlement sales amount
Expected settlement - actual settlement
Series settled value - total actual settlement
Gateway/UTR amount - bank credit amount
```

---

## 12. Reconciliation playbook

### 12.1 OMS to settlement reconciliation

Question answered:

Do Myntra OMS orders have matching settlement rows?

Expected side:

- `myntra_oms` order and sales data.

Actual side:

- `myntra_settlement` transaction rows.

Primary keys:

- `myntra_oms.order_code = myntra_settlement.order_id`
- `invoice_number` where needed
- `item_id` where available

Grain:

- order line / item line.

Mismatch categories:

- OMS order missing settlement,
- settlement without OMS order,
- amount mismatch,
- invoice mismatch,
- timing gap,
- transaction type mismatch,
- group scope mismatch.

Caveats:

- OMS amounts are strings and require casting.
- OMS has no `is_active` column per source notes.
- Settlement contains both forward and reverse rows.
- The source mentions `myntra_oms_settlement` with `recon_status = Matched / Amount yet to deducted`; validate table before relying on it.

### 12.2 Settlement to fee detail reconciliation

Myntra does not have a separate commission invoice table in the provided source. Fee detail is embedded as columns inside `myntra_settlement`.

Question answered:

Do the detailed fee component columns explain the net settled amount?

Expected side:

- Fee component fields in `myntra_settlement`.

Actual side:

- `settled_amount`, `series_settled_value`, or `total_actual_settlement` depending on use case.

Primary keys:

- `order_id + item_id`, or settlement component grain.

Caveats:

- Prepaid/postpaid component splits may not align one-to-one with total fields.
- Day-wise fields are settlement tracking fields, not fee fields.

### 12.3 Fee preview / expected fee to actual fee reconciliation

No fee preview table is described for Myntra in the source. Do not create a fee-preview reconciliation profile unless a fee schedule or expected-fee table is later added.

### 12.4 Cashback / offer / promotion reconciliation

No dedicated cashback/credit-debit note table is described for Myntra. Promotion and discount reconciliation should use:

- `discount_amount`
- `coupon_discount`
- `postpaid_coupon_discount`
- `commission_discount`
- non-order promotional credits if present

### 12.5 Reverse / return / refund reconciliation

Question answered:

Do returns/refunds in `myntra_reverse` align with reverse settlement impact in `myntra_settlement`?

Expected side:

- `myntra_reverse.refund_amount`, return tax reversal, return AWB details.

Actual side:

- `myntra_settlement` rows where `transaction_type = 'reverse'`.

Primary keys:

- `order_id + item_id`.

Fallback keys:

- `invoice_number`, `parent_id`, `sku_id`, AWB fields.

Grain:

- returned/cancelled item.

Mismatch categories:

- return without reverse settlement,
- reverse settlement without reverse row,
- refund amount mismatch,
- tax reversal mismatch,
- cancelled vs returned status mismatch,
- timing gap between return and settlement.

### 12.6 Non-order / adjustment reconciliation

Question answered:

Are all non-order financial movements included in total seller cash impact?

Expected side:

- Non-order settlement entries.

Actual side:

- Total settlement/cash-flow reporting.

Primary keys:

- `settlement_id`, `invoice_number`, `settlement_date`, `group_level_id`, metadata.

Grain:

- non-order settlement entry.

Mismatch categories:

- missing adjustment,
- duplicated adjustment,
- positive/negative sign misclassification,
- incorrect exclusion from realization/cash-flow analysis.

Caveats:

- Non-order settlements do not join to OMS or reverse tables.
- Table may be empty for some clients.

### 12.7 Shipping / freight / logistics adjustment reconciliation

Question answered:

Do freight, reverse logistics, and shipment-related fields explain logistics impact on settlement?

Expected side:

- OMS logistics fields and shipment information.
- Reverse AWB details.

Actual side:

- Settlement fields such as `freight_charge`, `freight_charge_gst`, `gta_fees`, `reverse_prepaid_charges`, `reverse_postpaid_charges`, `shipment_zone_classification`.

Primary keys:

- `order_id + item_id`.

Fallback keys:

- `tracking_no`, `forward_awb_number`, `return_awb_number`, `packed_id`.

Caveats:

- Courier-level invoice reconciliation requires logistics vendor data.
- RTO should not be inferred without a reliable status/value profile.

### 12.8 Entity / GSTIN / seller mapping reconciliation

Question answered:

Do seller/source GST and destination tax fields align with GST treatment?

Expected side:

- OMS seller GST/state/supply information.

Actual side:

- Settlement and reverse source/destination GST and tax component fields.

Primary keys:

- `order_code/order_id`, `invoice_number`, `source_gst_id`, `seller_gstn`, `destination_state`.

Mismatch categories:

- source GST mismatch,
- seller GST mismatch,
- wrong intra/inter-state classification,
- missing HSN/product tax category,
- tax amount mismatch.

### 12.9 Settlement to bank reconciliation note

Myntra provides component-specific UTRs and settlement dates. This enables a marketplace-to-bank reconciliation path if bank statement data is available.

Question answered:

Did Myntra settlement amounts actually reach the bank?

Expected side:

- Myntra settlement UTR/payment components.

Actual side:

- Bank statement credit transactions.

Primary keys:

- UTR fields.

Fallback keys:

- amount + date window + bank account + narration.

Caveats:

- There are multiple UTR fields, not one universal UTR.
- Prepaid and postpaid components may settle separately.
- Do not compare order-level rows directly to bank statement credits.

### 12.10 Reconciliation grain and fallback keys

| Reconciliation | Primary grain | Primary keys | Fallback keys |
|---|---|---|---|
| OMS to settlement | order/item | `order_code = order_id`, `item_id`, `invoice_number` | SKU, amount, date window |
| Reverse to settlement | returned item | `order_id + item_id` | invoice, parent_id, AWB, SKU |
| Non-order settlement | settlement entry | `settlement_id`, `invoice_number`, `settlement_date` | metadata, amount, source GST |
| Settlement to bank | UTR/component | UTR fields | amount + date + narration + bank account |
| GST validation | invoice/order line | invoice, GSTIN, HSN, state/supply type | source/destination state, tax rates |

---

## 13. Table-specific curated knowledge

### 13.1 `zs_observe.myntra_oms`

#### Role

`myntra_oms` captures forward order-level transactional data from Myntra. It is the primary sales-side source before settlement and contains order, product, payment split, GST, seller, customer, logistics, and system metadata.

#### Grain

One row represents a single line item/SKU within an order at the point of packing or dispatch.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.myntra_oms` |
| Engine | Athena v3 / Trino SQL |
| Table family | OMS / order master |
| Currency | INR, usually via `currency` field |
| Scope key | `group_level_id` stored as string in source notes |
| Active filter | No `is_active` column per source notes |

#### Primary analytical roles

- gross sales,
- order count,
- SKU/product analysis,
- GST and supply type validation,
- seller/GSTIN analysis,
- customer geography,
- logistics enrichment,
- payment split analysis,
- OMS-to-settlement reconciliation.

#### Mandatory filters

Use `group_level_id` for client/brand scope.

Do not apply `is_active = true` unless warehouse validation confirms the column exists.

#### Important columns

Identity and keys:

- `order_code`
- `sale_order_code`
- `seller_order_id`
- `invoice_number`
- `sku_code`
- `packed_id`
- `tracking_no`

Product and SKU:

- `brand`
- `article_type`
- `gender`
- `hsn`
- `product_tax_category`

Financial amounts:

- `mrp`
- `total_amount`
- `taxable_amount`
- `discount_amount`
- `coupon_discount`
- `shipping_amount`
- `additional_amount`
- `gift_amount`

Payment split:

- `payment_method`
- `prepaid_amount`
- `postpaid_amount`
- `prepaid_amount_other`
- `postpaid_amount_other`

Tax and GST:

- `cgst_rate`, `cgst_amount`
- `sgst_rate`, `sgst_amount`
- `igst_rate`, `igst_amount`
- `cess_rate`, `cess_amount`
- `tax_rate`
- `tcs_cgst_rate`, `tcs_cgst_amount`
- `tcs_sgst_rate`, `tcs_sgst_amount`
- `tcs_igst_rate`, `tcs_igst_amount`
- `tds_amount`

Seller and GST:

- `seller_id`
- `seller_name`
- `seller_gstn`
- `seller_state_code`
- `myntra_gstn`
- `e_commerce_portal_name`

Customer and geography:

- `customer_name`
- `customer_address`
- `customer_pincode`
- `customer_state`

Logistics and dates:

- `order_created_date`
- `packing_date`
- `courier_code`
- `shipping_case`
- `supply_type`
- `is_try_and_buy`

System and metadata:

- `currency`
- `gta_fees`
- `group_level_id`
- `group_id`
- `unique_id`
- `txn_uuid`
- `file_uuid`
- `zen_sheet_name`
- `created_at`

#### Value semantics

- `payment_method` indicates prepaid or COD/postpaid behavior.
- `supply_type` supports intra-state/inter-state GST classification.
- `is_try_and_buy` can support operational segmentation.

#### Relationships

- Join to `myntra_settlement` using `order_code = order_id`, validating with `invoice_number` where possible.
- Join to `myntra_reverse` using `order_code = order_id`.
- Use `tracking_no`, `courier_code`, and `packed_id` for logistics enrichment, not direct financial reconciliation unless vendor data exists.

#### Caveats

- Almost all amount columns are strings; cast before calculations.
- Date columns are strings; parse before filtering or grouping.
- No `is_active` or `transaction_type` column per source notes.
- Use `group_level_id` for scope.

#### Common query use cases

- gross sales from OMS,
- order count,
- brand/category sales,
- prepaid vs COD split,
- GST validation,
- source/destination tax classification,
- logistics/courier analysis,
- OMS-to-settlement missing order checks.

### 13.2 `zs_observe.myntra_settlement`

#### Role

`myntra_settlement` is the core financial settlement ledger. It records how Myntra settles payments with sellers for forward sales and reverse returns/refunds, including commissions, fees, taxes, payment mode splits, UTR references, and actual settlement fields.

#### Grain

One row represents a single settled line item with financial breakup.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.myntra_settlement` |
| Engine | Athena v3 / Trino SQL |
| Table family | Settlement ledger |
| Mandatory active filter | `is_active = true` |
| Scope key | `group_level_id` |
| Currency | `currency` / `currency_type` |

#### Primary analytical roles

- net settlement,
- seller realization,
- commission and fee analysis,
- prepaid/postpaid settlement split,
- UTR-level payout analysis,
- reverse settlement analysis,
- settlement velocity,
- OMS-to-settlement reconciliation,
- marketplace-to-bank reconciliation note.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = <client_id>
```

#### Important columns

Transaction identity:

- `transaction_type`
- `internal_txn_type`
- `order_id`
- `parent_id`
- `item_id`
- `invoice_number`
- `other_id`
- `metadata`

Product information:

- `brand`
- `sku_id`
- `hsn`
- `hsn_generated`
- `article_type`
- `gender`
- `product_tax_category`

Pricing and charged amounts:

- `mrp`
- `charged_amount`
- `charged_amount_excluding_tax`
- `customer_paid_amt`
- `seller_product_amount`

Tax and GST:

- `tax_igst_rate`, `tax_igst_amount`
- `tax_cgst_rate`, `tax_cgst_amount`
- `tax_sgst_rate`, `tax_sgst_amount`
- `total_tax`

TCS and TDS:

- `total_tcs_amount`
- `tcs_amount_prepaid`
- `tcs_amount_postpaid`
- `total_tds`
- `tds_amount_prepaid`
- `tds_amount_postpaid`

Commission and fees:

- `gross_commission`
- `commission_excluding_tcs_tds`
- `commission_percentage`
- `commission_discount`
- `mp_fees`
- `pick_and_pack_fee`
- `payment_gateway_fee`
- `fixed_fee`
- `freight_charge`
- `freight_charge_gst`
- `gta_fees`
- `forward_additional_charges_prepaid`
- `forward_additional_charges_postpaid`
- `reverse_prepaid_charges`
- `reverse_postpaid_charges`
- `marketing_charges_prepaid`
- `marketing_charges_postpaid`
- `royaltypercent_prepaid`
- `royaltypercent_postpaid`
- `royaltycharges_prepaid`
- `royaltycharges_postpaid`

Payment split and settlement:

- `prepaid_commission`
- `postpaid_commission`
- `prepaid_payment`
- `postpaid_payment`
- `prepaid_mp_fees`
- `postpaid_mp_fees`
- `postpaid_coupon_discount`
- `settled_amount`
- `amount_pending_settlement`

Settlement dates and UTRs:

- `settlement_prepaid_commision_date`
- `settlement_prepaid_mp_fees_date`
- `settlement_prepaid_payment_date`
- `settlement_postpaid_commision_date`
- `settlement_postpaid_mp_fees_date`
- `settlement_postpaid_payment_date`
- `utr_prepaid_commision`
- `utr_prepaid_mp_fees`
- `utr_prepaid_payment`
- `utr_postpaid_commision`
- `utr_postpaid_mp_fees`
- `utr_postpaid_payment`
- `packing_date`

Settlement reconciliation and velocity:

- `day_1` to `day_31`
- `series_settled_value`
- `total_actual_settlement`
- `difference_in_settled`

Location:

- `source_gst_id`
- `source_gst_name`
- `source_state`
- `source_country`
- `source_zipcode`
- `destination_zipcode`
- `destination_country`
- `shipment_zone_classification`

System and metadata:

- `is_active`
- `is_duplicated`
- `zen_status`
- `zen_status_false_reason`
- `is_active_false_reason`
- `group_level_id`
- `group_id`
- `client_name`
- `unique_id`
- `unique_value`
- `txn_uuid`
- `file_uuid`
- `zen_sheet_name`
- `created_at`
- `updated_at`

#### Value semantics

| Field | Value | Meaning |
|---|---|---|
| `transaction_type` | `forward` | Sale / seller receives payment |
| `transaction_type` | `reverse` | Return/refund / seller account debited |
| `internal_txn_type` | `sales` | Confirmed sale transaction |
| `internal_txn_type` | `reverse` | Confirmed return/refund |
| `internal_txn_type` | `NULL` | Unclassified row requiring investigation |

#### Relationships

- Join to `myntra_oms` using `order_id = order_code`.
- Join to `myntra_reverse` using `order_id + item_id`.
- Use UTR fields to connect to bank statement data when available.
- Do not join directly to `myntra_non_order_settlement` at order grain.

#### Caveats

- Always filter `is_active = true`.
- `settled_amount` is the primary net payable metric.
- Prepaid and postpaid components are separate streams.
- UTRs are component-specific.
- `day_1` to `day_31` are settlement tracking fields, not base transaction amounts.
- `internal_txn_type = NULL` should be handled explicitly.

#### Common query use cases

- net settlement,
- seller realization,
- fee breakdown,
- prepaid vs postpaid analysis,
- settlement lag,
- UTR payout tracking,
- reverse settlement analysis,
- amount pending settlement,
- day-wise settlement velocity.

### 13.3 `zs_observe.myntra_reverse`

#### Role

`myntra_reverse` captures return and refund transactions. It provides the return-side operational and financial context, including refund amounts, tax reversals, TCS/TDS reversals, return dates, and AWB references.

#### Grain

One row represents a single returned or cancelled item.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.myntra_reverse` |
| Engine | Athena v3 / Trino SQL |
| Table family | Reverse / returns report |
| Mandatory active filter | `is_active = true` |
| Scope key | `group_level_id` |

#### Primary analytical roles

- return/refund analysis,
- cancellation analysis,
- reverse GST/TCS/TDS impact,
- return logistics/AWB analysis,
- reverse-to-settlement reconciliation,
- refund timing analysis.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = <client_id>
```

#### Important columns

Transaction identity:

- `transaction_type`
- `internal_txn_type`
- `order_id`
- `order_status`
- `item_id`
- `parent_id`
- `invoice_number`
- `quantity`

Product information:

- `brand`
- `description`
- `sku_id`
- `hsn`
- `hsn_generated`

Financial:

- `mrp`
- `charged_amount`
- `charged_amount_excluding_tax`
- `refund_amount`
- `total_tax`
- `total_tcs_amount`
- `total_tds`
- `gta_fees`

Tax reversal:

- `tax_cgst_rate`, `tax_cgst_amount`
- `tax_sgst_rate`, `tax_sgst_amount`
- `tax_igst_rate`, `tax_igst_amount`
- `tcs_cgst_amount`, `tcs_sgst_amount`, `tcs_igst_amount`

Location:

- `source_gst_id`
- `source_gst_name`
- `source_state`
- `source_city`
- `source_country`
- `source_zipcode`
- `destination_state`
- `destination_state_code`
- `destination_country`
- `destination_zipcode`
- `destination_state_temp`
- `destination_state_code_temp`

Dates and logistics:

- `created_date`
- `settlement_date`
- `return_date`
- `return_awb_number`
- `forward_awb_number`

System and metadata:

- `is_active`
- `is_duplicated`
- `zen_status`
- `currency`
- `currency_type`
- `group_level_id`
- `group_id`
- `client_name`
- `other_id`
- `tenant_id`
- `unique_id`
- `unique_value`
- `txn_uuid`
- `file_uuid`
- `zen_sheet_name`
- `created_at`
- `updated_at`

#### Value semantics

| Field | Value | Meaning |
|---|---|---|
| `transaction_type` | `reverse` | Return/refund row |
| `order_status` | `cancelled` | Cancelled order/item |
| `order_status` | `NULL` | Return without explicit cancelled flag |

#### Relationships

- Join to `myntra_settlement` where `transaction_type = 'reverse'` using `order_id + item_id`.
- Join to `myntra_oms` using `order_id = order_code`.
- Use `forward_awb_number` and `return_awb_number` for logistics enrichment.

#### Caveats

- Always filter `is_active = true`.
- `refund_amount` is the key return financial metric.
- `order_status = NULL` is not necessarily invalid.
- Return AWB data supports logistics questions but does not replace courier settlement data.

#### Common query use cases

- return/refund value,
- cancellation analysis,
- return AWB analysis,
- refund settlement timing,
- reverse tax impact,
- reverse-to-settlement mismatch detection.

### 13.4 `zs_observe.myntra_non_order_settlement`

#### Role

`myntra_non_order_settlement` captures settlement transactions not linked to specific orders. These include penalties, incentives, marketing reimbursements, corrections, platform charges, and other non-order-level financial movements.

#### Grain

One row represents one non-order settlement entry.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.myntra_non_order_settlement` |
| Engine | Athena v3 / Trino SQL |
| Table family | Non-order settlement / adjustment ledger |
| Mandatory active filter | `is_active = true` |
| Scope key | `group_level_id` |

#### Primary analytical roles

- non-order settlement analysis,
- penalties and incentive tracking,
- reimbursement and correction analysis,
- complete cash-flow impact,
- settlement cycle reconciliation beyond order-level rows.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = <client_id>
```

#### Important columns

Identity and reference:

- `transaction_type`
- `internal_txn_type`
- `invoice_number`
- `settlement_id`
- `metadata`

Financial and dates:

- `settlement_date`
- `settled_amount`

Entity and scope:

- `source_gst_name`
- `currency_type`
- `group_level_id`
- `group_id`
- `tenant_id`

System and metadata:

- `is_active`
- `is_duplicated`
- `zen_status`
- `zen_status_false_reason`
- `is_active_false_reason`
- `unique_id`
- `unique_value`
- `txn_uuid`
- `file_uuid`
- `zen_sheet_name`
- `created_at`
- `updated_at`

#### Value semantics

- `settled_amount` can be positive or negative.
- Positive values may indicate credits, incentives, reimbursements, or corrections.
- Negative values may indicate penalties, platform charges, deductions, or corrections.

#### Relationships

- Does not join to `myntra_oms` or `myntra_reverse` by order ID.
- Can be combined with marketplace settlement at reporting period, settlement cycle, client, or cash-flow grain.

#### Caveats

- May be empty for some clients.
- Do not exclude from total cash-flow reporting unless explicitly doing order-only analysis.
- Do not force order-level joins.

#### Common query use cases

- non-order adjustment amount,
- penalties/incentives by settlement date,
- cash-flow reconciliation beyond orders,
- total realized settlement including adjustments.

---

## 14. Mandatory query rules

### 14.1 Scope rules

- Always apply `group_level_id` to scope Myntra queries to the correct client/brand.
- Use Account Data Binding to determine the correct `group_level_id` and data type.
- Do not hardcode `<client_id>` inside metric definitions.
- Do not assume `group_level_id` has the same data type across all tables.

### 14.2 Active-row rules

- Apply `is_active = true` to `myntra_settlement`, `myntra_reverse`, and `myntra_non_order_settlement`.
- Do not apply `is_active = true` to `myntra_oms` unless schema validation confirms it exists.

### 14.3 Date rules

- `myntra_oms.order_created_date` and `packing_date` are strings; parse before filtering.
- Settlement date fields in `myntra_settlement` are typed timestamps per source.
- Reverse date fields such as `created_date`, `settlement_date`, and `return_date` are date fields per source.
- Use the date that matches the business question: order date, packing date, return date, settlement date, or UTR/payment settlement date.

### 14.4 Transaction/status rules

- Use `transaction_type = 'forward'` for forward sales.
- Use `transaction_type = 'reverse'` for reverse/refund impact.
- Handle `internal_txn_type IS NULL` explicitly; do not drop blindly.
- In reverse table, `order_status = 'cancelled'` indicates cancellation; `NULL` can indicate return without cancel flag.

### 14.5 Join and grain rules

- Join OMS to settlement using `myntra_oms.order_code = myntra_settlement.order_id`.
- Join settlement to reverse using `order_id + item_id` where available.
- Do not join non-order settlement to OMS by order ID.
- Pre-aggregate where needed before comparing settlement to bank credits or non-order adjustments.
- Avoid double counting when joining line-item settlement rows to order-level OMS rows.

### 14.6 Numeric casting rules

- Cast OMS amount fields before arithmetic: `total_amount`, `taxable_amount`, `discount_amount`, `shipping_amount`, TCS/TDS fields, and GST fields.
- Use `TRY_CAST` where strings may contain blanks or malformed values.
- Settlement and reverse financial columns are typed numeric/double per source and can generally be aggregated directly.

### 14.7 Tax and TCS/TDS rules

- Treat TCS and TDS separately from marketplace fees.
- Validate GST using taxable amount and supply type/source-destination state context.
- Do not mix product GST and GST on freight/fees without clear metric definition.
- Preserve prepaid/postpaid TCS/TDS splits when analyzing payment-mode economics.

### 14.8 Settlement and realization rules

- Use `settled_amount` as the primary seller settlement field.
- Include `amount_pending_settlement` when the question asks about pending/unsettled amounts.
- Include non-order settlement rows when the question asks for total seller cash impact.
- Use `total_actual_settlement`, `series_settled_value`, and `difference_in_settled` for settlement reconciliation/variance analysis.
- Do not compare order-level rows directly to bank statement credits; use UTR/component or payout grain.

### 14.9 Platform-specific forbidden assumptions

- Do not assume Myntra has a dedicated fee-preview table.
- Do not assume Myntra has a separate cashback table.
- Do not assume all rows have non-null `internal_txn_type`.
- Do not treat day-wise columns as base sales or settlement components.
- Do not infer RTO without explicit status or logistics evidence.
- Do not treat payment captured as bank-realized cash.

---

## 15. Data-quality and semantic caveats

### 15.1 Cross-table caveats

- OMS, settlement, reverse, and non-order settlement have different grains.
- OMS is source-of-truth for order-side details; settlement is source-of-truth for financial settlement.
- Reverse table is source-of-truth for return/refund details; settlement captures the financial impact.
- Non-order settlement is not order-level.

### 15.2 Scope caveats

- `group_level_id` is mandatory.
- `myntra_oms.group_level_id` is string in source notes, while settlement/reverse/non-order use int-like scope keys.
- Use Account Data Binding for table-specific scope filters.

### 15.3 Status caveats

- `internal_txn_type = NULL` is a meaningful unclassified state.
- `order_status = NULL` in reverse should not be dropped as invalid.
- `transaction_type` values should be explicitly filtered for metric intent.

### 15.4 Financial caveats

- `settled_amount` is net payable after deductions.
- Prepaid and postpaid settlement streams may settle separately.
- `amount_pending_settlement` should be included in pending/aging analysis.
- Non-order settlement can materially change total cash realization.

### 15.5 Tax caveats

- OMS tax fields are strings.
- TCS/TDS have prepaid/postpaid splits in settlement.
- Product GST, freight GST, and TCS/TDS should not be collapsed into one tax measure without definition.

### 15.6 Logistics caveats

- OMS and reverse contain courier/tracking/AWB fields, but courier invoice or COD remittance reconciliation requires logistics vendor tables.
- `return_awb_number` and `forward_awb_number` are useful for reverse logistics enrichment.

### 15.7 Type-casting caveats

- OMS amount and date fields require casting/parsing.
- Use `TRY_CAST` and `DATE_PARSE` patterns in Athena/Trino.
- Avoid arithmetic on raw string amount fields.

### 15.8 Legacy / duplicate / migration-residue fields

- The source does not enumerate many legacy fields, but system metadata fields such as `unique_id`, `unique_value`, `txn_uuid`, `file_uuid`, `zen_sheet_name`, `zen_status`, and duplication flags should be preserved as system/control metadata.
- Do not treat metadata fields as business metrics.

---

## 16. Supported question patterns

### 16.1 Sales and revenue questions

- What were Myntra gross sales last month?
- What was Myntra GMV by brand or article type?
- What was prepaid vs COD order value?
- What was sales by GST supply type or state?

### 16.2 Settlement and realization questions

- What was Myntra net settlement for a client?
- What was seller realization rate?
- How much amount is pending settlement?
- Which settlement components are prepaid vs postpaid?
- What is the difference between series settled value and actual settlement?

### 16.3 Fee and deduction questions

- What was gross commission charged by Myntra?
- What was the effective commission rate?
- How much MP fee was deducted?
- What were freight, payment gateway, pick-pack, marketing, royalty, and GTA charges?

### 16.4 Return / cancellation questions

- What was Myntra return rate?
- How many orders were cancelled?
- What refund amount was processed?
- Which reverse rows do not have matching reverse settlement?
- Which returns have forward and return AWB numbers?

### 16.5 GST / TCS / TDS questions

- What TCS was deducted by Myntra?
- What TDS was deducted by Myntra?
- What was GST by supply type?
- Are tax amounts aligned with taxable amount?
- Which source GST entities generated the most sales or refunds?

### 16.6 Cashback / promotion / offer questions

- What discounts or coupon discounts were applied?
- What commission discounts were given?
- What promotional or incentive credits appeared in non-order settlements?

### 16.7 Logistics / shipping adjustment questions

- What was freight charge by shipment zone?
- What were reverse prepaid and postpaid charges?
- Which returns have return AWB numbers?
- Which courier codes or shipping cases have high return rates?

### 16.8 Reconciliation questions

- Which OMS orders are missing settlement?
- Which reverse records are missing reverse settlement?
- What is the settlement gap by order/item?
- Do non-order settlements explain cash-flow differences?
- Which UTRs should be matched to bank credits?

### 16.9 Diagnostic questions

- Why did Myntra realization drop this month?
- Did returns, freight, commission, MP fees, marketing, royalty, or pending settlement drive the change?
- Did prepaid/postpaid mix affect settlement timing?
- Did non-order penalties reduce seller cash flow?

### 16.10 Bank / payout matching questions

- Which Myntra UTRs were paid last month?
- Did prepaid payment UTRs appear in bank statement?
- Are postpaid/COD settlement components delayed?
- Which settlement components have missing UTRs?

---

## 17. SQL pattern appendix

SQL examples are supporting evidence for later Query Pattern, Rule, and Validation Test extraction. They should not replace the business definitions above.

### 17.1 Gross sales from OMS

```sql
SELECT
  SUM(TRY_CAST(total_amount AS DOUBLE)) AS gross_sales
FROM zs_observe.myntra_oms
WHERE group_level_id = '<client_id>';
```

### 17.2 Forward orders count from settlement

```sql
SELECT
  COUNT(DISTINCT order_id) AS forward_orders
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
  AND group_level_id = <client_id>;
```

### 17.3 Net settlement

```sql
SELECT
  SUM(settled_amount) AS net_settlement
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND group_level_id = <client_id>;
```

### 17.4 Seller realization

```sql
SELECT
  SUM(settled_amount) AS net_settled,
  SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END) AS gross_sales,
  SUM(settled_amount) / NULLIF(SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END), 0) AS realization_rate
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND group_level_id = <client_id>;
```

### 17.5 Return rate

```sql
SELECT
  COUNT(DISTINCT CASE WHEN transaction_type = 'reverse' THEN order_id END) * 100.0 /
  NULLIF(COUNT(DISTINCT CASE WHEN transaction_type = 'forward' THEN order_id END), 0) AS return_rate_pct
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND group_level_id = <client_id>;
```

### 17.6 Cancellation count from reverse table

```sql
SELECT
  COUNT(DISTINCT order_id) AS cancelled_orders,
  SUM(refund_amount) AS cancelled_refund_amount
FROM zs_observe.myntra_reverse
WHERE is_active = true
  AND group_level_id = <client_id>
  AND order_status = 'cancelled';
```

### 17.7 OMS to settlement reconciliation

```sql
SELECT
  o.order_code,
  o.invoice_number,
  TRY_CAST(o.total_amount AS DOUBLE) AS oms_total_amount,
  SUM(s.charged_amount) AS settlement_charged_amount,
  TRY_CAST(o.total_amount AS DOUBLE) - SUM(s.charged_amount) AS amount_gap
FROM zs_observe.myntra_oms o
LEFT JOIN zs_observe.myntra_settlement s
  ON o.order_code = s.order_id
 AND o.invoice_number = s.invoice_number
 AND s.is_active = true
WHERE o.group_level_id = '<client_id>'
  AND s.group_level_id = <client_id>
GROUP BY o.order_code, o.invoice_number, TRY_CAST(o.total_amount AS DOUBLE)
HAVING ABS(TRY_CAST(o.total_amount AS DOUBLE) - COALESCE(SUM(s.charged_amount), 0)) > 0.01;
```

### 17.8 Reverse to settlement reconciliation

```sql
SELECT
  r.order_id,
  r.item_id,
  r.refund_amount,
  SUM(s.settled_amount) AS reverse_settlement_amount,
  r.refund_amount - COALESCE(SUM(s.settled_amount), 0) AS refund_settlement_gap
FROM zs_observe.myntra_reverse r
LEFT JOIN zs_observe.myntra_settlement s
  ON r.order_id = s.order_id
 AND r.item_id = s.item_id
 AND s.transaction_type = 'reverse'
 AND s.is_active = true
WHERE r.is_active = true
  AND r.group_level_id = <client_id>
GROUP BY r.order_id, r.item_id, r.refund_amount
HAVING ABS(r.refund_amount - COALESCE(SUM(s.settled_amount), 0)) > 0.01;
```

### 17.9 Fee breakdown from settlement

```sql
SELECT
  SUM(gross_commission) AS gross_commission,
  SUM(mp_fees) AS marketplace_fees,
  SUM(fixed_fee) AS fixed_fee,
  SUM(payment_gateway_fee) AS payment_gateway_fee,
  SUM(freight_charge) AS freight_charge,
  SUM(freight_charge_gst) AS freight_charge_gst,
  SUM(gta_fees) AS gta_fees,
  SUM(marketing_charges_prepaid + marketing_charges_postpaid) AS marketing_charges,
  SUM(royaltycharges_prepaid + royaltycharges_postpaid) AS royalty_charges
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND group_level_id = <client_id>;
```

### 17.10 GST/TCS/TDS validation

```sql
SELECT
  SUM(total_tax) AS total_gst,
  SUM(total_tcs_amount) AS total_tcs,
  SUM(total_tds) AS total_tds,
  SUM(charged_amount_excluding_tax) AS taxable_base
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND group_level_id = <client_id>;
```

### 17.11 Settlement cycle / payout lag

```sql
SELECT
  AVG(DATE_DIFF('day', packing_date, settlement_prepaid_payment_date)) AS avg_prepaid_payment_lag,
  AVG(DATE_DIFF('day', packing_date, settlement_postpaid_payment_date)) AS avg_postpaid_payment_lag
FROM zs_observe.myntra_settlement
WHERE is_active = true
  AND group_level_id = <client_id>;
```

### 17.12 Pending receivables by aging, if receivables table exists

```sql
SELECT
  dpd,
  SUM(pending_amount) AS pending_amount
FROM zs_observe.myntra_receivables
WHERE group_level_id = <client_id>
GROUP BY dpd
ORDER BY dpd;
```

---

## 18. Extraction guidance

Expected card families:

```text
Business Hierarchy:
Tenant, Group, Platform, Platform Context, Platform Account, Account Data Binding, Business Scope Set if reusable.

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

Important extraction instructions:

- Use this document as raw markdown source knowledge, not final card YAML.
- Use the stable heading contract for semantic chunking.
- Use Section 3 for Business Hierarchy and Account Data Binding candidates.
- Use Section 4 and Section 13 for Table, Column, Relationship, and Value Profile candidates.
- Use Section 5 for Process cards.
- Use Section 7 and Section 11 for Metric and Formula Template candidates.
- Use Section 12 for Reconciliation Profile, Reconciliation Side, Reconciliation Unit, Matching Logic, and Mismatch Category candidates.
- Use Section 14, Section 15, and Section 17 for Query Pattern, Rule, Validation Test, Output Contract, and review-item candidates.
- Preserve UTR fields as deterministic lookup keys for future marketplace-to-bank reconciliation.
- Preserve prepaid/postpaid split as value/profile and metric applicability context.
- Preserve `myntra_oms` type-casting caveats as hard execution guidance.
- Preserve the fact that `myntra_non_order_settlement` is not order-level and must not be force-joined to OMS.

Final principle:

```text
Myntra follows the same marketplace frame as Amazon, Flipkart, Nykaa, and future marketplaces.
Myntra-specific knowledge lives inside standard sections, not in a custom ingestion script.
```
