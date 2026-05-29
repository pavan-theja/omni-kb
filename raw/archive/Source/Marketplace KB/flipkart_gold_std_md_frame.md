---
title: Flipkart Marketplace Knowledge Base
doc_type: marketplace_raw_knowledge
domain: marketplace_finance
platforms: [flipkart]
platform_types: [marketplace]
platform_contexts: [flipkart.india]
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
  - group_level_id: table_specific
primary_entities:
  - Flipkart India marketplace seller accounts represented in ZenStatement warehouse tables
  - Seller / business account linked to GSTIN and registered bank account in Flipkart Seller Hub
tables:
  - zs_recon_processor.flipkart_oms
  - zs_observe.flipkart_commission
  - zs_observe.flipkart_cashback
  - zs_observe.flipkart_settlement
optional_modules:
  - commission_detail_invoice
  - cashback_credit_debit_notes
  - seller_tier_fee_model
  - sub_platform_flag
  - payout_bank_reference
  - marketplace_to_bank_reconciliation_note
  - logistics_enrichment
  - settlement_velocity_tracking
status: draft
owner: finance_data_team
source_documents:
  - Flipkart Recon Doc.docx
  - marketplace_gold_std_raw_md_frame.md
authoring_note: >
  Curated human-readable raw markdown for ZenStatement ingestion. This document
  follows the marketplace gold-standard frame. It intentionally avoids card-level
  YAML, canonical JSON, and manually-authored graph edges. The ingestion pipeline
  should chunk this document semantically and extract candidate cards, relationships,
  value profiles, metrics, rules, validation tests, output contracts, retrieval
  indexes, and evidence metadata.
---

# Flipkart Marketplace Knowledge Base

## 1. How to use this document

This is a curated raw markdown knowledge document for the Flipkart India marketplace domain. It is intended for ingestion into the ZenStatement context-engineering KB.

This document is intentionally **not card YAML**, **not canonical JSON**, and does **not manually author graph edges**. It is written as human-readable source knowledge so the ingestion pipeline can later produce semantic chunks, candidate cards, relationships, value profiles, query patterns, rules, validation tests, output contracts, retrieval indexes, and evidence metadata.

This document supports extraction of:

- business hierarchy knowledge for Flipkart marketplace accounts and table-specific `group_level_id` mappings,
- data understanding for `flipkart_oms`, `flipkart_settlement`, `flipkart_commission`, and `flipkart_cashback`,
- metric understanding for GMV, net revenue, seller realization, marketplace fees, commission, cashback, TCS/TDS, return rate, cancellation rate, collection fee, and settlement lag,
- process understanding for order-to-settlement, FBF/NFBF fulfilment, commission invoicing, cashback credit/debit note lifecycle, refund/reversal lifecycle, and settlement payout flow,
- reconciliation understanding for OMS-to-settlement, settlement-to-commission, cashback-to-settlement offer adjustment, fee/tax validation, refund/reversal validation, and settlement-to-bank matching where bank references exist,
- execution guidance for active-row filters, table-specific scope filters, order ID normalization, grain alignment, numeric casting, safe date selection, and platform-specific caveats.

Use this document as the Flipkart-specific content source under the shared marketplace gold-standard frame. Do not create a Flipkart-specific ingestion script. Platform-specific complexity should stay in this content, while the ingestion pipeline remains generic.

---

## 2. Marketplace overview and business context

### 2.1 Marketplace role

Flipkart is a major Indian e-commerce marketplace. It operates a marketplace model where third-party sellers list products and Flipkart provides customer-facing commerce infrastructure, including catalogue, payments, logistics enablement, returns, customer service, seller reporting, and settlement.

Flipkart is owned by Walmart and operates at India scale across categories such as fashion, electronics, home, appliances, beauty, books, and general merchandise.

For sellers, Flipkart is not merely a sales channel. It is also a financial intermediary:

```text
Customer pays Flipkart
→ Flipkart records the order
→ Flipkart applies fulfilment, payment, and marketplace charges
→ Flipkart deducts commission, fixed fees, shipping fees, collection fees, GST on fees, TCS, TDS, refunds, cashback reversals, and adjustments
→ Flipkart settles the net amount to the seller's registered bank account
```

### 2.2 Seller / brand context

The source document does not name a single legal seller entity in the same way some marketplace documents do. The Flipkart data should therefore be treated as seller/account-scoped through the table-specific ZenStatement scope keys and GST/account identifiers.

Important seller/account-related concepts:

- `group_level_id` is required but differs across tables.
- GSTIN and business name fields exist in commission/cashback tables.
- Seller tier influences fixed fee and payout cycle.
- The registered business bank account linked to GSTIN receives payouts through NEFT/RTGS-like references in the settlement table.

### 2.3 Commercial model

Flipkart monetizes the seller transaction through multiple deductions:

```text
Total Flipkart deduction
= commission fee
+ fixed / closing fee
+ shipping fee
+ collection fee
+ GST on all fees
+ TCS
+ TDS
+ refund / reverse / cancellation adjustments where applicable
- offer / cashback / protection / addon / adjustment credits where applicable
```

The simplified seller settlement model is:

```text
Seller bank settlement
= selling price
- Flipkart deductions
- TCS
- TDS
+ credits / offers / adjustments / protection fund where applicable
```

All marketplace fees attract 18% GST. GST on fees is generally claimable as input tax credit. TCS and TDS are cash-flow deductions but are usually reclaimable through tax/GST filing workflows, so they should not always be treated as permanent marketplace cost.

### 2.4 Storefronts, sub-platforms, and fulfilment programs

Flipkart has three important marketplace-context dimensions for this KB:

1. **FBF — Fulfilment by Flipkart**
   - Flipkart handles storage, packing, shipping, delivery, returns, quality checks, and customer queries.
   - Seller sends bulk inventory to Flipkart fulfilment centres.
   - Typically lower fixed fees, F-Assured eligibility, faster delivery, better visibility, and higher conversion.
   - Seller loses some packaging/control flexibility and may incur storage-related economics.
   - In data: `FBF` in OMS and `flipkart_fulfilment` in settlement.

2. **NFBF — Non-Fulfilment by Flipkart**
   - Seller manages fulfilment and dispatch; Flipkart/Ekart may still provide pickup and last-mile logistics.
   - Includes Easy Ship and Self Ship patterns.
   - More seller control but higher fixed fees, lower F-Assured advantage, and greater SLA responsibility.
   - In data: `NON_FBF` in OMS and `seller_easy_ship` in settlement.

3. **Shopsy — Flipkart value platform**
   - Budget/value-focused Flipkart sub-platform aimed heavily at Tier-2 and Tier-3 city customers.
   - Typical item prices are around ₹150–₹250 in the source business description.
   - Popular categories include fashion, home décor, general merchandise, and accessories.
   - Zero commission applies to all Shopsy products, but other fees such as fixed fee, shipping fee, and collection fee still apply.
   - In data: `is_shopsy_order_ = 'true'` as a string field, not a boolean.

### 2.5 What this marketplace data can and cannot answer

This Flipkart KB can answer:

- gross sales / GMV,
- net revenue after returns,
- seller realization rate,
- settlement amount and settlement lag,
- marketplace fee burden,
- commission / fixed fee / shipping fee / reverse shipping fee / collection fee analysis,
- FBF vs NFBF settlement and fee comparison,
- prepaid vs postpaid / COD settlement comparison,
- cashback / promotional credit and reversal analysis,
- Shopsy vs non-Shopsy analysis,
- TCS/TDS and GST-on-fee deductions,
- OMS-to-settlement reconciliation,
- settlement-to-commission reconciliation,
- cashback-to-settlement offer reconciliation,
- settlement-to-bank reconciliation when bank reference data is combined with banking KB.

This Flipkart KB cannot fully answer by itself:

- actual bank receipt status unless bank statement KB is retrieved,
- courier-level COD remittance or AWB-level logistics performance unless logistics/Ekart/Shiprocket KB is retrieved,
- exact contractual fee rate by seller tier unless a seller-specific rate card is available,
- exact profitability after COGS unless product cost data is joined,
- refund root cause if a separate detailed return-reason source is absent.

---

## 3. Scope and account context

### 3.1 Active platform context

The active platform context for this document is:

```text
Platform: Flipkart
Platform type: marketplace
Platform context: Flipkart India
Country: India
Currency: INR
```

The data spans multiple processing layers in the ZenStatement warehouse:

```text
Flipkart Seller Hub Reports
→ zs_ingest raw ingestion
→ zs_recon_processor cleaned/typed processor layer
→ zs_observe standardized observation layer
→ zs_refined final enriched settlement layer
```

In the source document:

- `flipkart_oms` is described as living in `zs_recon_processor` for cleaned/typed order data.
- `flipkart_commission` and `flipkart_cashback` live in `zs_observe`.
- `flipkart_settlement` appears in `zs_refined` in reconciliation examples, while its table dictionary also references `zs_observe`. The ingestion pipeline should preserve this schema ambiguity as a review item and prefer the actual warehouse catalog during card validation.

### 3.2 Seller / account identifiers

Key account/scope identifiers include:

- `group_level_id`, but values differ by table.
- GST fields such as `seller_gstin`, `business_gst_number`, and warehouse state fields.
- settlement/bank transfer identifiers such as `settlement_id`.
- seller tier is business-relevant but may not be directly encoded as a stable warehouse key in every table.

### 3.3 Default scope filters

Flipkart requires table-specific account scoping. Do **not** assume a single `group_level_id` applies across all Flipkart tables.

| Table | Known `group_level_id` behavior | Query implication |
|---|---|---|
| `flipkart_oms` | Uses `22`, `26`, `65787`, `65853` in source caveats | Must resolve through Account Data Binding / selected account context |
| `flipkart_settlement` | Known value `66388` in table dictionary | Do not filter using OMS/commission/cashback group ID by default |
| `flipkart_commission` | Known value `22` | Use integer `22`, not string `'22'` |
| `flipkart_cashback` | Known value `22` | Use integer `22`, not string `'22'` |

### 3.4 Table-specific scope differences

The most important Flipkart scope caveat is:

```text
group_level_id differs across OMS, settlement, commission, and cashback.
```

This means a query like:

```sql
WHERE group_level_id = 22
```

may be correct for commission/cashback but wrong for settlement. Conversely:

```sql
WHERE group_level_id = 66388
```

may be correct for settlement but wrong for commission/cashback.

The ingestion pipeline should extract this as a strong Account Data Binding / Rule / Validation Test candidate.

### 3.5 Reference-table exceptions

The source Flipkart document does not describe a standalone Flipkart reference table equivalent to Nykaa's `nykaa_mapping`. There are, however, legacy and JSON/alternate columns within tables. These should not be treated as reference tables unless validated against the warehouse catalog.

### 3.6 Scope caveats

- Apply scope through Account Data Binding, not by embedding hardcoded filters in Table or Metric cards.
- Treat `group_level_id` as integer in commission, cashback, and settlement where documented.
- Do not join or reconcile on matching `group_level_id` across tables because the source explicitly warns the values differ.
- If a user asks for "Flipkart India" but not the seller/group, retrieval should return partial scope or unresolved group/account metadata rather than assuming a default.

---

## 4. Table family overview

| Table | Business role | Grain | Primary use | Required filters | Important caveats |
|---|---|---|---|---|---|
| `zs_recon_processor.flipkart_oms` | Order master / order verification source | Order item / SKU line, based on source business description | GMV, order count, quantities, tax validation, fulfilment type, Shopsy flag, order verification | `is_active = true` where available; table-specific `group_level_id` | Source document has a mislabeled table section where the `flipkart_oms` heading repeats cashback content. Treat OMS details as high-level and validate against warehouse schema. Active rate is very low (~1%). |
| `zs_observe.flipkart_commission` | Marketplace fee invoice detail | One fee line item per order item; multiple rows per order item | Fee breakdown, commission/fixed/shipping/reverse shipping/collection fee analysis, settlement `mp_fee` validation | `is_active = true`; `group_level_id = 22` | `order_id` has no `OD` prefix; financial string fields exist but decimal `charged_amount` and `total_tax` are authoritative. |
| `zs_observe.flipkart_cashback` | Cashback / credit-debit note ledger | One cashback or promotional credit/debit event per order item | Cashback given, cashback reversal, credit/debit note analysis, offer reconciliation, Shopsy cashback comparison | `is_active = true`; `group_level_id = 22` | `is_shopsy_order_` is string `'true'`/`'false'`; document type fields can be null but still financially meaningful. |
| `zs_observe.flipkart_settlement` / `zs_refined.flipkart_settlement` | Financial settlement / payout ledger | One settled order item | Seller realization, settlement amount, settlement cycle, payout/bank reference, FBF/NFBF comparison, settlement-to-fee reconciliation | `is_active = true`; `group_level_id = 66388` where applicable | `mp_fee` is reliable aggregate; granular fee columns often NULL; schema location should be validated between `zs_observe` and `zs_refined`. |

Common table-family interpretation:

```text
flipkart_oms = what was ordered / sold / fulfilled
flipkart_commission = what Flipkart charged as marketplace fee invoice detail
flipkart_cashback = what Flipkart credited or clawed back as promotional cashback / offer credit-debit notes
flipkart_settlement = what Flipkart actually settled to the seller
```

---

## 5. End-to-end transaction lifecycle

### 5.1 Forward flow: order to settlement

Forward flow represents a successful sale that should eventually settle to the seller.

```text
Customer places order on Flipkart
→ order appears in Flipkart OMS
→ item is packed/fulfilled through FBF or NFBF
→ Flipkart records fee invoice rows in flipkart_commission
→ Flipkart may record cashback / offer credit notes in flipkart_cashback
→ Flipkart creates settlement row in flipkart_settlement
→ Flipkart deducts commission, fixed fee, shipping fee, collection fee, GST on fees, TCS, and TDS
→ seller receives net settlement into registered bank account
```

Business interpretation:

- OMS is the sales-side anchor.
- Commission table is the invoice-level fee detail behind marketplace fee deductions.
- Cashback table records promotional credits and reversals.
- Settlement table is the payout-side financial truth for what the seller receives.

### 5.2 Reverse flow: return, cancellation, refund, clawback

Reverse flow covers returns, cancellations, refunds, and related deductions/reversals.

```text
Customer returns or cancels order
→ OMS / settlement status or transaction type reflects reverse/cancel behavior
→ Flipkart reverses or adjusts sale-settled amount
→ cashback may be clawed back through debit note
→ reverse shipping fee may be charged
→ settlement reflects refund_settled_amount and net payout impact
```

Important interpretations:

- Commission may be reimbursed to the seller in the event of refund according to the business playbook.
- Reverse shipping fee can be charged separately in commission detail or settlement granular columns.
- Cashback given on sale can be reversed through debit notes on returns/cancellations.
- Cancellation should not be treated as normal forward GMV unless a specific metric defines it that way.

### 5.3 Adjustment flow: fees, cashback reversals, fee waivers, protection fund, and rebates

Flipkart has multiple adjustment-like flows:

```text
cashback credit note
cashback debit note
fee waiver / fee rebate
commission rebate
shipping fee rebate
collection fee rebate
fixed fee rebate
offer adjustment settled amount
protection fund settled amount
addon settled amount
my share settled amount
```

These are not base gross sale fields. They should be modeled as credits/debits that affect seller realization or promotion economics.

### 5.4 Payout flow: settlement to seller bank

Flipkart credits seller bank accounts through settlement payout cycles.

Known payout facts from the source:

- payout cycle begins from **dispatch date**, not delivery or order date,
- cycle length varies from about 7 days for Gold/Platinum sellers to about 15 days for Bronze sellers,
- seller bank payouts happen on Monday, Wednesday, and Friday,
- payout method is NEFT to the seller's registered business bank account linked to GSTIN,
- `settlement_id` in settlement can represent a bank NEFT/RTGS transfer reference such as `AXISCN1234497424`,
- `settlement_date` is the bank payout date.

If a user asks whether Flipkart settlement reached the bank, retrieval should combine this marketplace KB with the banking KB and the `marketplace_to_bank` reconciliation pattern.

### 5.5 Timing gaps and in-flight transactions

Timing gaps can arise because:

- settlement begins from dispatch date, not order date,
- seller tier changes payout lag,
- payout days are limited to Monday/Wednesday/Friday,
- refunds and returns may be deducted from subsequent settlements,
- cashback reversals may appear as separate debit note events,
- commission/cashback/settlement tables can use different date columns and different processing layers.

Do not classify an OMS order as permanently missing settlement until the relevant seller tier and settlement cycle window have been applied.

---

## 6. Entity relationships and joins

### 6.1 Primary join map

| From table | To table | Join key | Reliability / notes |
|---|---|---|---|
| `flipkart_oms` | `flipkart_settlement` | `order_id + item_id` | Both use OD-prefixed order IDs in source relationship notes. Use for OMS-to-settlement matching. |
| `flipkart_settlement` | `flipkart_commission` | `REPLACE(settlement.order_id, 'OD', '') = commission.order_id` and `item_id` | Commission table has no `OD` prefix. Aggregate commission fee rows before comparing to settlement `mp_fee`. |
| `flipkart_oms` | `flipkart_commission` | `REPLACE(oms.order_id, 'OD', '') = commission.order_id` and `item_id` | One OMS order item can map to multiple fee rows. |
| `flipkart_cashback` | `flipkart_settlement` | `order_id + item_id` | Cashback can map to settlement `offer_settled_amount` or `offer_adjustment_settled_amount`. |
| `flipkart_cashback` | `flipkart_commission` | `REPLACE(cashback.order_id, 'OD', '') = commission.order_id` and `item_id` | Indirect relation through the same order item. |

### 6.2 Secondary validation keys

Secondary keys and validation fields include:

- `invoice_number`,
- `item_id`,
- `order_item_id`,
- `credit_debit_note_no` / `credit_note_id__debit_note_id`,
- `settlement_id`,
- `settlement_date`,
- `vendor_payout`,
- `irn` for e-invoicing context,
- `seller_gstin` / `business_gst_number` / source GST fields for seller/tax validation.

### 6.3 Join reliability and match rates

The source document does not provide full match-rate percentages across all Flipkart joins. The curated interpretation should therefore capture join reliability qualitatively:

- OMS-to-settlement should be the main order-item reconciliation path.
- Settlement-to-commission is reliable only after stripping the `OD` prefix and pre-aggregating commission rows by order/item.
- Cashback-to-settlement is valid where offer/cashback settlement fields exist, but not every order has cashback.
- Commission and cashback do not necessarily have one row per order item; both can be one-to-many or optional.

### 6.4 Grain mismatch and double-counting risks

Important grain risks:

- `flipkart_commission` is many rows per order item because each fee type is a separate row.
- `flipkart_cashback` is one event per cashback/credit-debit note and not every order has cashback.
- `flipkart_settlement` is one settled order item.
- OMS likely has order-item grain but the detailed OMS schema section in the source is inconsistent and should be validated.

Do not join fee rows directly to settlement and then sum settlement amounts without pre-aggregating the fee side. This will multiply settlement amounts.

### 6.5 Identifier normalization rules

Critical identifier normalization:

```sql
REPLACE(order_id, 'OD', '')
```

Use this when joining OD-prefixed OMS/settlement/cashback order IDs to `flipkart_commission.order_id`, which lacks the `OD` prefix.

Additional non-standard commission order ID formats mentioned in the source:

- `RU*` with 12 characters,
- `LS*` with 25 characters,
- `KQ*` with 12 characters.

These should be treated as edge-case / non-standard transactions and may require review before reconciliation.

### 6.6 Reference / mapping table joins

The source document does not define a separate Flipkart mapping/reference table. Instead, mapping concerns exist inside table columns:

- FBF/NFBF naming differs between OMS and settlement.
- Shopsy flag appears as `is_shopsy_order_` in OMS and cashback.
- GST and seller identity appear through GSTIN/business fields.
- commission fee descriptions define fee-type taxonomy.

---

## 7. Financial waterfall and seller realization

### 7.1 Forward settlement waterfall

The forward Flipkart waterfall is:

```text
Customer selling price / sale settled amount
+ offer / cashback / addon / tax / protection / seller-share credits where applicable
- commission fee
- fixed fee
- shipping fee
- collection fee
- GST on marketplace fees
- TCS
- TDS
= settled amount to seller
```

A simplified business formula from the source is:

```text
Total Flipkart Deduction
= Commission Fee
+ Fixed Fee
+ Shipping Fee
+ Collection Fee
+ GST on all fees

Seller Bank Settlement
= Selling Price
- Total Deduction
- TCS
- TDS
```

The settlement-table formula is more detailed:

```text
settled_amount
= sale_settled_amount
+ refund_settled_amount
+ offer_settled_amount
+ my_share_settled_amount
+ addon_settled_amount
+ taxes_settled_amount
+ offer_adjustment_settled_amount
+ protection_fund_settled_amount
- |mp_fee|
- |gst_on_mp_fees|
- |total_tcs_amount|
- |total_tds_amount|
```

### 7.2 Reverse / refund settlement waterfall

Reverse/refund economics may include:

```text
refund_settled_amount
+ cashback debit note reversal
+ reverse shipping fee
+ marketplace fee reversals or non-reversals
+ TCS/TDS/tax adjustments
= net reverse settlement impact
```

Important points:

- Commission is reimbursed in the event of refund according to the source playbook.
- Return/refund deductions are auto-deducted from the next settlement.
- Cashback given on sale can be reversed with a debit note on return/cancellation.
- Reverse shipping fee may be charged to seller and should be analyzed separately.

### 7.3 Non-order / adjustment waterfall

Flipkart adjustment-like settlement components include:

- `offer_settled_amount`,
- `my_share_settled_amount`,
- `addon_settled_amount`,
- `taxes_settled_amount`,
- `offer_adjustment_settled_amount`,
- `protection_fund_settled_amount`,
- fee waivers and rebates from the commission table,
- cashback credit/debit notes.

These should be included in cash-flow realization when the question asks what the seller actually received, but isolated when the question asks pure product economics.

### 7.4 Seller realization definition

Seller realization measures what percentage of sale value the seller actually receives after deductions and adjustments.

Default concept:

```text
seller realization rate = SUM(settled_amount) / SUM(sale_settled_amount)
```

Default table:

```text
flipkart_settlement
```

Caveats:

- Denominator should use sale/forward settlement value, not all rows blindly.
- TCS/TDS treatment depends on cash-flow vs profitability interpretation.
- FBF + Postpaid can have settled amount greater than sale amount because offer/addon/adjustment credits can supplement sale value.
- Realization should be compared within a consistent fulfilment type, payment mode, seller tier, and account scope.

### 7.5 Field-level payout interpretation

| Field | Meaning | Caveat |
|---|---|---|
| `settled_amount` | Net amount paid to seller; final cash-flow output | Primary seller realization field |
| `sale_settled_amount` | Sale value being settled | Use as denominator for realization where appropriate |
| `refund_settled_amount` | Refund deduction / return impact | Usually zero for forward orders, negative for returns |
| `offer_settled_amount` | Offer/promotion credit | Can make settlement exceed sale amount |
| `offer_adjustment_settled_amount` | Corrections to offer amount | Reconcile with cashback where applicable |
| `protection_fund_settled_amount` | Buyer protection or similar amount | Sign can vary |
| `mp_fee` | Aggregate marketplace fee | More reliable than sparse granular fee columns |
| `gst_on_mp_fees` | GST on marketplace fees | Negative deduction, claimable as ITC |
| `total_tcs_amount` | Tax collected at source | Cash-flow deduction, reclaimable in GST filing |
| `total_tds_amount` | Tax deducted at source | Cash-flow deduction, reclaimable in income tax filing |
| `settlement_id` | Bank NEFT/RTGS transfer reference | Useful for marketplace-to-bank reconciliation |
| `settlement_date` | Bank payout date | Use for settlement cycle analysis |

### 7.6 Known benchmark ranges or observed snapshots

General benchmark:

- Flipkart realization benchmark in source: approximately 70–80% for India.

Settlement distribution observed in source for active rows:

| NEFT type | Fulfilment type | Count | Total settled | Total sale | Total MP fee | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| Postpaid | seller_easy_ship | 111,699 | ₹16.7M | ₹19.6M | -₹1.85M | Settled lower than sale due to normal deductions |
| Postpaid | flipkart_fulfilment | 106,674 | ₹61.7M | ₹58.8M | -₹4.19M | Settled exceeds sale due to offer/addon/adjustment credits |
| Prepaid | seller_easy_ship | 33,852 | ₹6.96M | ₹10.4M | -₹1.04M | Settled lower than sale |
| Prepaid | flipkart_fulfilment | 31,639 | ₹4.19M | ₹5.02M | -₹0.40M | Settled lower than sale |

The `flipkart_fulfilment + Postpaid` pattern should be preserved as a diagnostic insight, not treated as a data error by default.

---

## 8. Fees, deductions, taxes, promotions, and adjustments

### 8.1 Commission and marketplace fees

Flipkart commission is category-based and ranges approximately from 3% to 25% of selling price.

Category ranges in source:

| Category | Commission range |
|---|---:|
| Mobiles & Tablets | 3%–5% |
| Electronics & Appliances | 5%–12% |
| Home & Kitchen | 8%–15% |
| Fashion & Apparel | 10%–25% |
| Beauty & Personal Care | 5%–15% |
| Books & Media | 2%–10% |

Key commission rules:

- Commission is the same for FBF and NFBF; fulfilment choice does not directly change commission.
- Products under ₹1,000 have 0% commission under the November 2025 revision across most categories.
- Shopsy has zero commission on all products regardless of price.
- Commission is calculated on selling price excluding customer discounts but including shipping charges.
- In the event of refund, commission fee is reimbursed to the seller.

Marketplace fee details appear in `flipkart_commission` as fee invoice rows and in `flipkart_settlement.mp_fee` as an aggregate.

### 8.2 Fixed / closing / platform fees

Fixed fee / closing fee is a flat per-order fee, usually around ₹14–₹55+ depending on:

- seller tier,
- fulfilment type,
- price slab.

Approximate source fee table:

| Price range | FBF fee | NFBF fee |
|---|---:|---:|
| Under ₹300 | ~₹14 | ~₹16 |
| ₹300–₹500 | ~₹20–₹30 | ~₹25–₹35 |
| ₹500–₹1,000 | ~₹35–₹45 | ~₹40–₹50 |
| Above ₹1,000 | ~₹50+ | ~₹55+ |

Exact values depend on seller tier and rate card. Platinum and Gold tiers can be ₹10–₹30 lower than Bronze.

### 8.3 Shipping, freight, fulfilment, and reverse logistics fees

Shipping fee is weight × zone based. Flipkart uses the higher of actual weight and volumetric weight:

```text
volumetric weight = L × W × H / 5000
billing weight = max(actual weight, volumetric weight)
```

Zone behavior from source:

| Zone | Description | Sub-500g behavior |
|---|---|---|
| Local | Same city | Free for most categories |
| Zonal | Same geographic region | Free for most categories |
| National | Cross-region | Charged by weight slab |

Reverse shipping fee can appear as a separate fee in commission detail and settlement granular columns. It should be separated from forward shipping fee when analyzing returns/RTO economics.

### 8.4 Payment / collection / payment gateway fees

Flipkart collection fee is a payment processing fee:

| Payment method | Collection fee |
|---|---:|
| Prepaid | 2% of order value |
| Postpaid / COD | 2.5% of order value |

In settlement, payment mode is represented by `neft_type` values such as `Prepaid` and `Postpaid`.

### 8.5 Promotional credits, cashback, offers, and rebates

Flipkart cashback and promotional credits are captured in `flipkart_cashback`.

Lifecycle:

```text
Customer places order with platform offer
→ Flipkart issues Credit Note to seller for cashback amount
→ if returned, cashback is reversed via Debit Note
→ if cancelled, cashback is reversed via Debit Note / Cancellation
```

Important cashback values:

| Transaction/document pattern | Meaning | Amount behavior |
|---|---|---:|
| `forward` + `Credit Note` + `Sale` | Cashback given on delivered/sale order | Positive |
| `reverse` + `Debit Note` + `Return` | Cashback reversed on return | Negative |
| `forward cancel` + `Debit Note` + `Cancellation` | Cashback reversed on cancellation | Negative |
| `forward` with null doc type | Cashback with missing document classification | Positive |
| `reverse` with null doc type | Cashback reversal with missing document classification | Negative |

Observed active source totals:

- forward credit note sale: 156,896 records, about +₹10.4M,
- reverse debit note return: 56,645 records, about -₹3.4M,
- forward null document classification: 44,601 records, about +₹1.6M,
- reverse null document classification: 24,433 records, about -₹0.86M,
- forward cancel debit note cancellation: 6,668 records, about -₹0.42M,
- net cashback outflow: about ₹7.3M.

Commission rebate fields also exist in the commission table but are typically NULL.

### 8.6 Reimbursements, protection funds, incentives, and penalties

Flipkart settlement contains `protection_fund_settled_amount`, `addon_settled_amount`, `my_share_settled_amount`, and offer/tax adjustment fields. These should be treated as settlement credits/debits that can materially affect realized payout.

The source document does not describe a separate non-order settlement table for Flipkart. Therefore, non-order adjustment extraction should focus on settlement-level adjustment columns and cashback/commission rebate fields.

### 8.7 TCS and TDS

TCS:

- Flipkart collects 1% TCS on net taxable supplies.
- It can be split as 0.5% CGST + 0.5% SGST for intra-state, or 1% IGST for inter-state.
- Deducted before settlement.
- Seller claims TCS credit during GST return filing.

TDS:

- Flipkart deducts 1% TDS on seller payments.
- Seller claims TDS credit during income tax filing.

TCS/TDS are cash-flow deductions but generally reclaimable. Do not treat them as permanent marketplace cost unless the metric explicitly asks for cash impact.

### 8.8 GST on products and GST on marketplace fees

GST concepts:

- Product GST applies on product selling price.
- Intra-state supply uses CGST + SGST.
- Inter-state supply uses IGST.
- Common GST rates include 5%, 12%, 18%, and 28%, depending on HSN.
- HSN codes are required for products.
- GST on marketplace fees is 18% and usually claimable as input tax credit.
- E-invoicing IRN appears as `irn` where relevant.

### 8.9 Fee recovery on returns

- Commission is reimbursed to seller on refund according to the source playbook.
- Cashback credits can be clawed back through debit notes.
- Return/refund deductions are auto-deducted from future settlements.
- Reverse shipping fee may still be charged.
- TCS/TDS should be treated according to tax-credit/cash-flow logic, not automatically as permanent loss.

### 8.10 Marketplace-specific naming traps

- `is_shopsy_order_` is a string, not a boolean.
- `flipkart_commission.order_id` has no `OD` prefix.
- `flipkart_settlement.mp_fee` is the reliable aggregate marketplace fee; granular fee columns can be NULL.
- `fee_name` may mirror `description`; use `description` as primary fee identifier because it is always populated in commission table source notes.
- `charged_amount` means different things by table: order value in OMS, fee amount in commission, cashback/offer amount in cashback, and settlement component in settlement.

---

## 9. Fulfilment, logistics, payment modes, and settlement cycle

### 9.1 Fulfilment models

| Business model | OMS value | Settlement value | Meaning |
|---|---|---|---|
| FBF | `FBF` | `flipkart_fulfilment` | Flipkart stores, packs, ships, handles delivery/returns/customer queries |
| NFBF | `NON_FBF` | `seller_easy_ship` | Seller manages fulfilment; Flipkart/Ekart may provide logistics pickup/delivery |

FBF benefits include lower fixed fees, F-Assured eligibility, faster delivery, better listing visibility, and higher conversion. NFBF benefits include seller control and no Flipkart FC storage dependency, but higher fixed fees and SLA responsibility.

### 9.2 Logistics and courier signals

Flipkart logistics is closely related to Ekart and FBF/NFBF flows.

Marketplace-level data contains:

- fulfilment type,
- delivery zone,
- gross weight,
- volumetric weight,
- reverse shipping fee,
- settlement date and payout date.

For detailed AWB/courier/COD remittance analysis, retrieval should branch into the logistics KB, especially Ekart/logistics docs, when the user asks about:

```text
courier
shipment
AWB
COD remittance
freight
RTO
reverse shipping
Ekart
bank remittance from logistics
```

### 9.3 COD vs prepaid / postpaid behavior

Payment behavior appears through:

- collection fee rules: prepaid 2%, postpaid/COD 2.5%,
- settlement `neft_type`: `Prepaid` or `Postpaid`,
- postpaid can represent COD-like settlement behavior,
- FBF + Postpaid shows a distinctive observed pattern where settled amount can exceed sale amount due to credits/adjustments.

### 9.4 Settlement cycle and payout timing

Seller tier controls payout speed:

| Seller tier | Payout cycle | Fixed fee level | Qualification logic |
|---|---:|---|---|
| Platinum | 7 days from dispatch | Lowest | Top-tier performance |
| Gold | 7 days from dispatch | Low | High volume, low defect rate, consistent service |
| Silver | ~10 days | Medium | Moderate performance |
| Bronze | 15 days | Highest | Default/new/underperforming seller |

Performance metrics influencing seller tier:

- order volume,
- on-time dispatch rate, usually 24 hours to Ready to Ship,
- cancellation rate,
- customer ratings,
- order defect rate below 1%,
- return rate.

Financial impact: moving from Bronze to Gold can save approximately ₹10–₹30 per order in fixed fees; at 500 orders/month, that is roughly ₹5,000–₹15,000/month.

### 9.5 Bank / UTR / payout references, if available

`flipkart_settlement.settlement_id` is described as a bank NEFT/RTGS transfer reference. `settlement_date` is the date money was transferred to the seller's bank.

For marketplace-to-bank reconciliation:

```text
Expected side: flipkart_settlement aggregated by settlement_id / settlement_date / account
Actual side: bank statement credits using bank reference / narration / amount / date window
```

This document does not include the bank statement schema, so bank matching requires the banking KB.

### 9.6 Logistics handoff to the logistics KB

Trigger retrieval of logistics KB when the user asks about:

- Ekart,
- FBF shipping behavior,
- NFBF / seller easy ship,
- COD remittance,
- RTO,
- reverse shipping fee,
- shipment/AWB-level performance,
- freight billing outside marketplace settlement.

Do not automatically expand into logistics for pure marketplace commission/cashback/settlement questions.

---

## 10. Status and value semantics

### 10.1 Transaction types

| Table | Field | Raw value | Business meaning | Metric usage |
|---|---|---|---|---|
| `flipkart_cashback` | `transaction_type` | `forward` | Cashback credit on sale | Include in cashback given |
| `flipkart_cashback` | `transaction_type` | `reverse` | Cashback reversal on return | Include in cashback clawback |
| `flipkart_cashback` | `transaction_type` | `forward cancel` | Cashback reversal on cancellation | Include in cashback clawback |
| `flipkart_commission` | `transaction_type` | `Order Item` | Fee invoice line for order item | Include in fee analysis |
| `flipkart_settlement` | implicit components | sale/refund/offer/adjustment fields | Settlement components rather than one transaction type | Use component fields carefully |

### 10.2 Internal transaction types

For cashback:

- `internal_transaction_type = 'forward'` for both normal forward and forward cancellation debit note patterns.
- `internal_transaction_type = 'reverse'` for return-related reversals.

### 10.3 Final statuses / order statuses

The source document does not provide a complete OMS status taxonomy. Status semantics should be validated against the actual `flipkart_oms` schema. For ingestion, capture this as an unresolved / review item rather than inventing statuses.

### 10.4 Payment modes

| Field | Value | Meaning |
|---|---|---|
| `neft_type` | `Prepaid` | Online payment settlement behavior |
| `neft_type` | `Postpaid` | COD/postpaid-like settlement behavior |
| business rule | prepaid | Collection fee around 2% |
| business rule | postpaid / COD | Collection fee around 2.5% |

### 10.5 Fulfilment values

| Field/table | Value | Business meaning |
|---|---|---|
| OMS | `FBF` | Fulfilment by Flipkart |
| OMS | `NON_FBF` | Non-Fulfilment by Flipkart |
| Settlement | `flipkart_fulfilment` | Fulfilment by Flipkart |
| Settlement | `seller_easy_ship` | Seller/Easy Ship fulfilment |

### 10.6 Document types / credit-debit notes

| Field combination | Meaning |
|---|---|
| `Credit Note` + `Sale` | Cashback/offer credit given on sale |
| `Debit Note` + `Return` | Cashback/offer credit reversed on return |
| `Debit Note` + `Cancellation` | Cashback/offer credit reversed on cancellation |
| null document type/subtype | Missing classification but financial values still matter |

### 10.7 Fee names / fee descriptions

`flipkart_commission.description` identifies fee type.

Known values:

- Fixed Fee,
- Commission,
- Shipping Fee,
- Reverse Shipping Fee,
- Collection Fee.

Source active row counts:

| Fee description | Active count | Business meaning |
|---|---:|---|
| Fixed Fee | 327,190 | Flat per-order fee |
| Commission | 307,632 | Category-based percentage fee |
| Shipping Fee | 125,215 | Forward delivery charge |
| Reverse Shipping Fee | 122,250 | Return shipping charge |
| Collection Fee | 3,644 | Payment processing charge |

### 10.8 Null and unknown handling

- Null cashback document type/subtype rows still carry financial values and should not be dropped blindly.
- Sparse granular settlement fee columns should not be interpreted as zero fee if `mp_fee` is populated.
- Commission rebate fields are usually NULL; NULL means no recorded rebate, not necessarily inapplicability of rebate programs.
- Unknown/non-standard commission order ID prefixes such as `RU`, `LS`, `KQ` require review before standard OD-based joins.

---

## 11. Key metrics and business definitions

### 11.1 Gross sales / GMV

Gross Merchandise Value is the total sale value before deductions.

Default formula concept:

```text
SUM(charged_amount) from forward OMS rows
```

Alternative settlement-side formula:

```text
SUM(sale_settled_amount)
```

Caveats:

- OMS is preferred for sales-side GMV.
- Settlement is preferred for payout-side sale value.
- Account scope must come from Account Data Binding.

### 11.2 Net revenue after returns

Net revenue is GMV less returns/refunds.

Concept:

```text
forward sale value + reverse/refund value
```

Use settlement refund fields when analyzing payout impact. Use OMS where raw order status and original order value are required.

### 11.3 Distinct orders and line items

Use:

- `COUNT(DISTINCT order_id)` for order count,
- `COUNT(DISTINCT order_id || item_id)` or equivalent for order-item count where needed,
- row count only when analyzing line-level fee/cashback/settlement events.

Forward-order count from OMS:

```sql
SELECT COUNT(DISTINCT order_id) AS forward_orders,
       COUNT(DISTINCT order_id || item_id) AS forward_order_items
FROM zs_recon_processor.flipkart_oms
WHERE is_active = true
  AND transaction_type = 'forward'
```

### 11.4 Units sold

Use quantity fields in OMS or settlement where available. The source document does not provide a detailed OMS quantity dictionary, so validate actual quantity field before production metric extraction.

Settlement-side units (forward only):

```sql
SELECT SUM(quantity) AS units_sold
FROM zs_observe.flipkart_settlement
WHERE is_active = true
  AND transaction_type = 'forward'
```

Treat as low-confidence until the OMS quantity field is confirmed against the live schema. Account scope is applied through Account Data Binding.

### 11.5 Average order value

AOV concept:

```text
GMV / distinct forward order count
```

Use forward sale orders only. Do not include cancellations or cashback/commission rows.

OMS-side AOV:

```sql
SELECT SUM(charged_amount) * 1.0
       / NULLIF(COUNT(DISTINCT order_id), 0) AS aov
FROM zs_recon_processor.flipkart_oms
WHERE is_active = true
  AND transaction_type = 'forward'
```

### 11.6 Seller realization rate

Seller realization rate measures what percentage of sale value reaches the seller after Flipkart deductions, taxes, refunds, and adjustments.

Default formula:

```text
SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0)
```

Default table:

```text
flipkart_settlement
```

Benchmark from source:

```text
70%–80% for India
```

### 11.7 Net settlement amount

Net settlement amount is:

```text
SUM(settled_amount)
```

Use `flipkart_settlement` and the correct settlement `group_level_id`.

### 11.8 Effective commission rate

Concept:

```text
ABS(SUM(commission fee)) / SUM(sale value)
```

Use `flipkart_commission` where `description = 'Commission'`, or validated settlement commission field if populated. The commission detail table is preferred for detailed fee analysis.

### 11.9 Effective fee / take rate

Concept:

```text
ABS(SUM(total marketplace fees + GST on fees)) / SUM(GMV or sale_settled_amount)
```

Use:

- `flipkart_settlement.mp_fee` for aggregate marketplace fees,
- `flipkart_commission` for fee-level breakdown.

### 11.10 Shipping / freight cost rate

Concept:

```text
ABS(SUM(shipping fee + reverse shipping fee)) / SUM(sale value)
```

Separate forward shipping fee and reverse shipping fee where possible.

Numerator from commission detail:

```sql
SELECT ABS(SUM(CASE
                 WHEN description IN ('Shipping Fee', 'Reverse Shipping Fee')
                 THEN charged_amount END)) AS shipping_burden
FROM zs_observe.flipkart_commission
WHERE is_active = true
```

(Account scope — e.g. commission/cashback `group_level_id = 22` — is applied through Account Data Binding, not in the metric formula.)

Denominator typically pairs with `SUM(sale_settled_amount)` from `zs_observe.flipkart_settlement`.

### 11.11 Return rate

Concept:

```text
reverse orders / forward orders
```

The source gives category benchmark ranges:

- fashion: 20%–30%,
- electronics: 5%–10%.

Validate table-specific transaction/status fields before production execution.

OMS-side return rate:

```sql
SELECT 1.0 * COUNT(DISTINCT CASE
                              WHEN transaction_type = 'reverse'
                              THEN order_id || item_id END)
       / NULLIF(COUNT(DISTINCT CASE
                                 WHEN transaction_type = 'forward'
                                 THEN order_id || item_id END), 0) AS return_rate
FROM zs_recon_processor.flipkart_oms
WHERE is_active = true
```

### 11.12 RTO rate

The source document does not provide a complete RTO field taxonomy. RTO analysis should use logistics/fulfilment KB if AWB/courier/RTO data is required.

Placeholder using settlement `return_type` / `fulfilment_type` — must be cross-validated against a logistics KB before production use:

```sql
SELECT 1.0 * COUNT(DISTINCT CASE
                              WHEN LOWER(return_type) LIKE '%rto%'
                              THEN order_id || item_id END)
       / NULLIF(COUNT(DISTINCT order_id || item_id), 0) AS rto_rate
FROM zs_observe.flipkart_settlement
WHERE is_active = true
```

Treat as low-confidence — RTO classification needs cross-validation with the logistics KB. Account scope is applied through Account Data Binding.

### 11.13 Cancellation rate

Concept:

```text
forward cancel / total forward-order population
```

For cashback, `transaction_type = 'forward cancel'` means cashback reversal on cancellation, not necessarily the full order cancellation count.

### 11.14 Cashback / offer rate

Net cashback from cashback ledger (forward credit minus reversals):

```sql
SELECT SUM(CASE
             WHEN transaction_type = 'forward' THEN charged_amount
             WHEN transaction_type IN ('reverse', 'forward cancel') THEN -charged_amount
             ELSE 0 END) AS net_cashback
FROM zs_observe.flipkart_cashback
WHERE is_active = true
```

(Account scope is applied through Account Data Binding, not in the metric formula.)

Concept:

```text
net cashback / GMV
```

Where:

```text
net cashback = cashback credits - cashback reversals / cancellations
```

Use `flipkart_cashback.charged_amount` with transaction/document semantics.

### 11.15 Fee recovery rate on returns

Concept:

```text
fees reimbursed or reversed on returns / fees originally charged
```

For Flipkart, commission is said to be reimbursed on refund. Reverse shipping may still be charged. Detailed fee recovery should compare settlement/refund and commission fee rows at order-item grain.

### 11.16 TCS/TDS amount and rate

Use settlement fields:

```text
SUM(total_tcs_amount)
SUM(total_tds_amount)
```

Interpret as cash-flow deductions and tax-credit items, not pure marketplace costs.

### 11.17 GST rate validation

Validate:

- product GST using HSN/product tax columns where available,
- GST on marketplace fees using `gst_on_mp_fees` in settlement or `total_tax` in commission,
- fee GST should generally be 18% of fee amount.

Settlement-side GST-on-fees effective rate (should land near 18%):

```sql
SELECT SUM(gst_on_mp_fees)
       / NULLIF(ABS(SUM(mp_fee)), 0) AS gst_on_mp_fees_rate
FROM zs_observe.flipkart_settlement
WHERE is_active = true
```

Commission-side fee GST effective rate:

```sql
SELECT ABS(SUM(total_tax))
       / NULLIF(ABS(SUM(charged_amount)), 0) AS commission_fee_gst_rate
FROM zs_observe.flipkart_commission
WHERE is_active = true
```

Account scope is applied through Account Data Binding.

### 11.18 Settlement cycle / payout lag

Concept:

```text
DATE_DIFF('day', created_date, settlement_date)
```

Caveat:

- business payout cycle starts from dispatch date, but the settlement table example uses `created_date` vs `settlement_date` for available fields.
- seller tier affects expected lag.

### 11.19 Reconciliation gap amount

Generic concept:

```text
expected amount - actual amount
```

Settlement mp_fee vs commission fee aggregate (per order-item):

```sql
SELECT s.order_id, s.item_id,
       s.mp_fee AS settlement_mp_fee,
       SUM(c.charged_amount) AS commission_fee_sum,
       s.mp_fee - SUM(c.charged_amount) AS gap_amount
FROM zs_observe.flipkart_settlement s
LEFT JOIN zs_observe.flipkart_commission c
       ON c.order_id = REPLACE(s.order_id, 'OD', '')
      AND c.item_id = s.item_id
WHERE s.is_active = true
GROUP BY s.order_id, s.item_id, s.mp_fee
```

(Account scope — settlement vs commission `group_level_id` — is applied through Account Data Binding, not in the metric formula.)

Examples:

- settlement `mp_fee` vs summed commission `charged_amount`,
- cashback charged amount vs settlement offer fields,
- OMS sale value vs settlement sale-settled amount,
- settlement amount vs bank credit amount when banking data is available.

---

## 12. Reconciliation playbook

### 12.1 OMS to settlement reconciliation

Question answered:

```text
Which Flipkart orders/order-items exist in OMS but are missing or mismatched in settlement?
```

Expected side:

```text
flipkart_oms order-item sales records
```

Actual side:

```text
flipkart_settlement settled order-item records
```

Primary keys:

```text
order_id + item_id
```

Fallback keys:

```text
invoice_number, SKU, settlement date / created date window
```

Grain:

```text
order-item
```

Mismatch categories:

- missing settlement,
- amount mismatch,
- timing gap,
- duplicate order-item,
- fulfilment type mismatch,
- scope mismatch.

Caveats:

- Validate the actual OMS schema because the uploaded source has an inconsistent OMS table section.
- Do not assume the same `group_level_id` across OMS and settlement.
- Apply settlement-cycle timing logic before calling something missing.

### 12.2 Settlement to fee detail reconciliation

Question answered:

```text
Does settlement mp_fee match the detailed Flipkart commission invoice rows?
```

Expected side:

```text
SUM(flipkart_commission.charged_amount) grouped by order_id + item_id
```

Actual side:

```text
flipkart_settlement.mp_fee
```

Primary keys:

```text
REPLACE(settlement.order_id, 'OD', '') = commission.order_id
AND settlement.item_id = commission.item_id
```

Grain:

```text
order-item after pre-aggregating commission rows
```

Mismatch categories:

- missing commission rows,
- missing settlement rows,
- fee amount mismatch,
- GST-on-fee mismatch,
- OD prefix normalization failure,
- duplicate fee rows,
- non-standard order ID format.

Caveats:

- `flipkart_commission` contains multiple fee rows per order item.
- `commission.charged_amount` is negative.
- `settlement.mp_fee` is also negative.
- Do not compare absolute values unless the metric explicitly wants magnitude.

### 12.3 Fee preview / expected fee to actual fee reconciliation

The Flipkart source does not include a separate fee-preview table like Amazon. Expected fee validation should therefore be based on:

- Flipkart public/contractual fee rules,
- seller tier,
- fulfilment type,
- price slab,
- category,
- weight/zone,
- collection mode,
- actual `flipkart_commission` invoice rows.

Question answered:

```text
Are Flipkart fee invoice rows consistent with rate-card expectations?
```

Expected side:

```text
rate-card-derived fee estimate, if seller tier/category/price/weight data is available
```

Actual side:

```text
flipkart_commission fee rows
```

Caveat:

```text
Do not invent expected fee values without a seller-specific rate card or validated public rule inputs.
```

### 12.4 Cashback / offer / promotion reconciliation

Question answered:

```text
Do cashback credits/debits align with settlement offer fields?
```

Expected side:

```text
SUM(flipkart_cashback.charged_amount) by order_id + item_id
```

Actual side:

```text
flipkart_settlement.offer_settled_amount + flipkart_settlement.offer_adjustment_settled_amount
```

Primary keys:

```text
order_id + item_id
```

Grain:

```text
order-item
```

Mismatch categories:

- cashback exists but settlement offer amount missing,
- settlement offer amount exists but cashback row missing,
- amount mismatch,
- document type missing,
- credit/debit note sign mismatch,
- cancellation reversal missing.

Caveats:

- Not every order has cashback.
- Cashback document type/subtype can be null but still financially meaningful.
- `is_shopsy_order_` is a string and may be relevant to cashback behavior.

### 12.5 Reverse / return / refund reconciliation

Question answered:

```text
Are reverse/refund/cancellation events correctly reflected in settlement and cashback reversal?
```

Expected side:

```text
return/refund/cancel population from OMS or settlement components
```

Actual side:

```text
refund_settled_amount, cashback debit notes, reverse shipping fee, commission recovery behavior
```

Primary keys:

```text
order_id + item_id
```

Caveats:

- Source does not provide a dedicated Flipkart reverse table.
- Reverse behavior must be inferred from settlement refund components, cashback debit notes, and fee rows.
- Reverse shipping fee should be separated from forward shipping fee.

### 12.6 Non-order / adjustment reconciliation

The source does not provide a standalone Flipkart non-order settlement table. Adjustment reconciliation should use settlement fields and fee/cashback adjustment rows.

Relevant fields:

- `addon_settled_amount`,
- `my_share_settled_amount`,
- `taxes_settled_amount`,
- `offer_adjustment_settled_amount`,
- `protection_fund_settled_amount`,
- fee rebate columns in commission,
- cashback debit/credit notes.

### 12.7 Shipping / freight / logistics adjustment reconciliation

Question answered:

```text
Do shipping, reverse shipping, and fulfilment-related charges align with fulfilment type and zone/weight behavior?
```

Expected side:

```text
rate-card-derived shipping fee using fulfilment type, zone, weight, and seller tier where available
```

Actual side:

```text
flipkart_commission Shipping Fee / Reverse Shipping Fee and settlement shipping fields
```

Caveats:

- Flipkart FBF/NFBF affects fixed fee and logistics economics.
- Commission is the same for FBF/NFBF, but fixed fee and operational cost profile differ.
- Detailed courier/AWB reconciliation requires logistics KB.

### 12.8 Entity / GSTIN / seller mapping reconciliation

Question answered:

```text
Do seller GSTIN, business GST number, and invoice/IRN fields align with seller account and tax reporting?
```

Expected side:

```text
Seller account / GSTIN context from business hierarchy or seller master, if available
```

Actual side:

```text
seller_gstin, business_gst_number, source_gst_id, invoice_number, IRN fields
```

Caveat:

- The source does not include a dedicated Flipkart GSTIN mapping reference table.
- Entity/GSTIN canonicalization may need an external seller master.

### 12.9 Settlement to bank reconciliation note

Question answered:

```text
Did Flipkart settlement actually reach the seller's bank account?
```

Expected side:

```text
flipkart_settlement aggregated by settlement_id / settlement_date / seller account
```

Actual side:

```text
bank statement credit from banking KB
```

Primary keys:

```text
settlement_id / NEFT / RTGS reference
amount
settlement date / bank credit date window
bank account
```

Caveats:

- Bank statement data is not present in this marketplace document.
- Use banking KB and `marketplace_to_bank` reconciliation profile.
- Do not treat `settled_amount` as bank-received cash without bank confirmation.

### 12.10 Reconciliation grain and fallback keys

Default grains:

| Reconciliation | Grain |
|---|---|
| OMS to settlement | order-item |
| settlement to commission | order-item after fee pre-aggregation |
| cashback to settlement offer | order-item |
| fee rate-card validation | order-item or fee-line depending on rate-card granularity |
| settlement to bank | settlement ID / payout reference / bank credit |

Fallback keys:

- `invoice_number`,
- `item_id`,
- `order_item_id`,
- `settlement_id`,
- `settlement_date`,
- `credit_debit_note_no`,
- `seller_gstin`,
- amount + date window.

---

## 13. Table-specific curated knowledge

### 13.1 `zs_recon_processor.flipkart_oms`

#### Role

`flipkart_oms` is the order-management source used for order verification. It should represent what customers ordered, the order/item identity, quantities, tax/order values, transaction type, fulfilment classification, Shopsy flag, and order-level state.

The source document's table section labelled `flipkart_oms` appears to contain cashback table content. Treat this as a source-document inconsistency. Do not extract the duplicated cashback section as OMS truth without warehouse validation.

#### Grain

Expected grain:

```text
One row per order item / SKU line.
```

#### Key facts

| Attribute | Value |
|---|---|
| Likely schema | `zs_recon_processor` according to pipeline architecture |
| Possible use in examples | `zs_recon_processor.flipkart_oms` |
| Engine | Athena v3 / Trino SQL |
| Scope key | `group_level_id`, but values can include 22, 26, 65787, 65853 |
| Active-row caveat | Low active rate around ~1% according to source gotcha |
| Order ID format | OD-prefixed |
| Shopsy flag | `is_shopsy_order_ = 'true'` as string |

#### Primary analytical roles

- gross sales / GMV,
- order count,
- item count,
- tax validation,
- order verification,
- fulfilment type analysis,
- Shopsy vs non-Shopsy segmentation,
- OMS-to-settlement reconciliation.

#### Mandatory filters

Use active-row filter if the table has `is_active`:

```sql
WHERE is_active = true
```

Apply the correct table-specific `group_level_id` through Account Data Binding. Do not assume settlement `group_level_id = 66388` applies to OMS.

#### Important columns

Identity and keys:

- `order_id`,
- `item_id`,
- `order_item_id`,
- `invoice_number`,
- `irn` where available.

Financial amounts:

- `charged_amount` for order/sale value,
- product/tax amount fields if present.

Lifecycle and status:

- `transaction_type`,
- order status / fulfilment status fields where present.

Fulfilment and logistics:

- `fulfilment_type` values such as `FBF` and `NON_FBF`,
- zone / shipment fields where available.

Sub-platform:

- `is_shopsy_order_` as string.

System and metadata:

- `is_active`,
- `group_level_id`,
- `group_id`,
- `tenant_id`,
- source file tracking fields.

#### Value semantics

Known from broader source:

- `FBF` means Fulfilment by Flipkart.
- `NON_FBF` means seller/Easy Ship fulfilment.
- `is_shopsy_order_ = 'true'` means Shopsy order.

#### Relationships

- Joins to `flipkart_settlement` on `order_id + item_id`.
- Joins to `flipkart_commission` after stripping `OD` prefix from `order_id`.
- Joins to `flipkart_cashback` on `order_id + item_id`.

#### Caveats

- The detailed OMS table section in the source is inconsistent and should be validated.
- `group_level_id` differs from settlement/commission/cashback.
- Active row rate is low; forgetting `is_active = true` can inflate results massively.
- Shopsy flag is string, not boolean.

#### Common query use cases

- Show Flipkart GMV.
- Count Flipkart forward orders.
- Compare FBF vs NFBF order value.
- Identify Shopsy orders.
- Find orders missing settlement.

---

### 13.2 `zs_observe.flipkart_settlement` / `zs_refined.flipkart_settlement`

#### Role

`flipkart_settlement` is the financial settlement / payout ledger showing what Flipkart actually pays to the seller after deductions and adjustments. It is the cash-flow ground truth within the marketplace domain.

#### Grain

```text
One settled order item.
```

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` in table dictionary; `zs_refined` in examples |
| Engine | Athena v3 / Trino SQL |
| Scope key | `group_level_id = 66388` where documented |
| Currency | INR |
| Order ID format | OD-prefixed |
| Date fields | `created_date`, `settlement_date` |
| Payout reference | `settlement_id` as NEFT/RTGS-like transfer reference |

#### Primary analytical roles

- seller realization,
- net settlement,
- settlement cycle analysis,
- FBF/NFBF comparison,
- prepaid/postpaid settlement comparison,
- marketplace fee impact,
- TCS/TDS cash-flow analysis,
- settlement-to-commission reconciliation,
- cashback/offer reconciliation,
- settlement-to-bank reconciliation.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = 66388
```

Validate schema and group binding during ingestion against actual warehouse catalog.

#### Important columns

Settlement output:

- `settled_amount`,
- `sale_settled_amount`,
- `refund_settled_amount`,
- `offer_settled_amount`,
- `my_share_settled_amount`,
- `addon_settled_amount`,
- `taxes_settled_amount`,
- `offer_adjustment_settled_amount`,
- `protection_fund_settled_amount`.

Fees and deductions:

- `mp_fee`,
- `gst_on_mp_fees`,
- `total_tcs_amount`,
- `total_tds_amount`,
- `total_tax`,
- `commission_fee`,
- `shipping_fee`,
- `fixed_fee`,
- `pick_and_pack_fee`,
- `reverse_shipping_fee`,
- `collection_fee`,
- `franchise_fee`.

ZenStatement computed fees:

- `zen_vendor_payout_fixed_fee`,
- `zen_vendor_payout_reverse_shipping_fee`,
- `zen_vendor_payout_commission_fee`,
- `zen_vendor_payout_collection_fee`,
- `zen_vendor_payout_franchise_fee`,
- `zen_vendor_payout_reverse_fee`.

Payment and payout:

- `settlement_id`,
- `settlement_date`,
- `neft_type`,
- `vendor_payout`.

Order/product:

- `order_id`,
- `item_id`,
- `invoice_number`,
- `sku_id`,
- `quantity`,
- `product_sub_category`.

Fulfilment/logistics:

- `fulfilment_type`,
- `zone`,
- `tier`,
- `return_type`,
- `gross_weight`,
- `vol_weight`.

System:

- `is_active`,
- `is_duplicated`,
- `zen_status`,
- `group_level_id`,
- `group_id`,
- `currency_type`,
- file and transaction UUIDs.

#### Value semantics

- `neft_type = Prepaid` means online-payment settlement behavior.
- `neft_type = Postpaid` means COD/postpaid-like settlement behavior.
- `fulfilment_type = flipkart_fulfilment` maps to OMS `FBF`.
- `fulfilment_type = seller_easy_ship` maps to OMS `NON_FBF`.

#### Relationships

- Joins to OMS on `order_id + item_id`.
- Joins to commission on stripped order ID + item ID.
- Joins to cashback on `order_id + item_id`.
- Joins to bank statement through `settlement_id`, amount, date, and bank account context when banking KB is available.

#### Caveats

- `mp_fee` is the reliable aggregate; granular fee columns are often NULL.
- Settlement table schema location is inconsistent between source examples (`zs_observe`, `zs_refined`); validate before canonical card creation.
- JSON/legacy `*_json` columns may represent secondary data; use primary fields unless reconciling that source.
- Do not compare settlement group ID to commission/cashback group ID.

#### Common query use cases

- What was Flipkart seller realization last month?
- What was net settlement by fulfilment type?
- How many days does Flipkart take to settle?
- Which settlement IDs should match bank credits?
- Why is FBF Postpaid settled amount higher than sale value?

---

### 13.3 `zs_observe.flipkart_commission`

#### Role

`flipkart_commission` is the marketplace fee invoice detail table. It provides the line-item breakdown behind settlement `mp_fee`.

Each order item can have multiple fee rows: fixed fee, commission, shipping fee, reverse shipping fee, collection fee, and related taxes.

#### Grain

```text
One fee line item for one order item.
```

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Engine | Athena v3 / Trino SQL |
| Scope key | `group_level_id = 22` |
| Currency | INR |
| Order ID format | No `OD` prefix |
| Active transaction type | `Order Item` |
| Metadata | `commission invoice` |
| Primary fee identifier | `description` |

#### Primary analytical roles

- detailed fee breakdown,
- commission analysis,
- fixed fee analysis,
- forward and reverse shipping fee analysis,
- collection fee analysis,
- GST on marketplace fee analysis,
- settlement `mp_fee` reconciliation,
- seller tier/rate-card validation where rate card exists.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = 22
```

#### Important columns

Identity and keys:

- `order_id` without `OD` prefix,
- `item_id`,
- `order_item_id`,
- `order_item_id__listing_id__campaign_id_transaction_id`,
- `recall_id`.

Fee classification:

- `metadata`,
- `transaction_type`,
- `service_type`,
- `fee_name`,
- `description`.

Financial amounts:

- `charged_amount` as primary fee amount, always negative in source,
- `total_tax` as GST on fee, always negative,
- string legacy fields such as `fee_amount`, `fee_waiver_amount`, `total_fee_amount`, `total_tax_amount`, and alternate `*_rs__` columns.

Rebates:

- `commission_rebate`,
- `shipping_fee_rebate`,
- `collection_fee_rebate`,
- `fixed_fee_rebate`,
- `total_mp_fee_rebate`.

Tax:

- `tax_cgst_rate`, `tax_cgst_amount`,
- `tax_sgst_rate`, `tax_sgst_amount`,
- `tax_igst_rate`, `tax_igst_amount`,
- legacy string tax columns.

Geography:

- `source_state`,
- `source_country`,
- `warehouse_state_code`.

Dates:

- `created_date` as primary fee invoice date,
- `date` as string alternative.

System:

- `is_active`,
- `is_duplicated`,
- `zen_status`,
- `group_level_id`,
- `group_id`,
- `tenant_id`,
- `currency_type`,
- file/transaction UUIDs.

#### Value semantics

Known `description` / `fee_name` values:

- `Fixed Fee`,
- `Commission`,
- `Shipping Fee`,
- `Reverse Shipping Fee`,
- `Collection Fee`.

Each value is a marketplace fee category and should be extracted into a Value Profile.

#### Relationships

- Joins to settlement by stripping `OD` from settlement order ID.
- Joins to OMS by stripping `OD` from OMS order ID.
- Joins to cashback by stripping `OD` from cashback order ID.

#### Caveats

- Do not use `order_id` directly against OD-prefixed tables.
- Pre-aggregate by order/item before joining to settlement.
- String financial columns are legacy/supplementary; use decimal `charged_amount` and `total_tax` as authoritative.
- Rebate columns are usually NULL.
- Non-standard order ID prefixes require review.

#### Common query use cases

- What fee types did Flipkart charge?
- How much commission did we pay?
- How much GST was charged on Flipkart fees?
- Which order-items have fee mismatch vs settlement `mp_fee`?
- What is reverse shipping fee burden?

---

### 13.4 `zs_observe.flipkart_cashback`

#### Role

`flipkart_cashback` records cashback, promotional subsidies, offer credits, and their reversals as credit/debit note events.

It explains offer economics and helps reconcile cashback credits/debits against settlement offer fields.

#### Grain

```text
One cashback / credit-debit note event for one order item.
```

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Engine | Athena v3 / Trino SQL |
| Scope key | `group_level_id = 22` |
| Currency | INR |
| Order ID format | OD-prefixed |
| Primary date | `created_date` |
| Shopsy flag | `is_shopsy_order_` string |
| Net cashback outflow | about ₹7.3M in source snapshot |

#### Primary analytical roles

- cashback amount,
- cashback reversals,
- promotional subsidy analysis,
- Shopsy cashback comparison,
- credit/debit note analysis,
- cashback-to-settlement offer reconciliation,
- state-wise cashback distribution,
- campaign/offer economics.

#### Mandatory filters

```sql
WHERE is_active = true
  AND group_level_id = 22
```

#### Important columns

Identity and keys:

- `order_id`,
- `item_id`,
- `order_item_id`,
- `credit_debit_note_no`,
- `credit_note_id__debit_note_id`,
- `invoice_number`,
- `irn`.

Classification:

- `transaction_type`,
- `internal_transaction_type`,
- `document_type`,
- `document_sub_type`,
- `is_shopsy_order_`.

Financial:

- `charged_amount`,
- `charged_amount_excluding_tax`,
- `taxable_value`,
- `tds_amount`,
- `manual_charge_amount_excluding_tax`.

Tax:

- `tax_cgst_rate`, `tcs_cgst_rate`, `tcs_cgst_amount`,
- `tax_sgst_rate`, `tcs_sgst_rate`, `tcs_sgst_amount`,
- `tax_igst_rate`, `tcs_igst_rate`, `tcs_igst_amount`,
- legacy tax columns.

Geography/seller:

- `destination_state`,
- `customer_s_delivery_state`,
- `source_gst_id`,
- `seller_gstin`,
- `business_gst_number`,
- `business_name`.

Dates:

- `created_date`,
- `invoice_date` string.

System:

- `is_active`,
- `is_duplicated`,
- `zen_status`,
- `group_level_id`,
- `group_id`,
- `tenant_id`,
- `currency_type`,
- source metadata fields.

#### Value semantics

| `transaction_type` | `document_type` | `document_sub_type` | Meaning | Sign |
|---|---|---|---|---|
| `forward` | Credit Note | Sale | Cashback given on sale | Positive |
| `reverse` | Debit Note | Return | Cashback reversed on return | Negative |
| `forward cancel` | Debit Note | Cancellation | Cashback reversed on cancellation | Negative |
| `forward` | null | null | Cashback with missing document classification | Positive |
| `reverse` | null | null | Cashback reversal with missing document classification | Negative |

#### Relationships

- Joins to OMS on `order_id + item_id`.
- Joins to settlement on `order_id + item_id`.
- Joins to commission with `REPLACE(cashback.order_id, 'OD', '') = commission.order_id` and item ID.

#### Caveats

- Not every order has cashback.
- Null document type/subtype rows must not be dropped blindly.
- `is_shopsy_order_` is a string, not boolean.
- `taxable_value` and some legacy tax columns are strings; cast before arithmetic.

#### Common query use cases

- What is net cashback outflow?
- How much cashback was reversed on returns?
- Which cashback rows do not align with settlement offer amounts?
- How does Shopsy cashback differ from non-Shopsy cashback?
- Which states receive the highest cashback amount?

---

## 14. Mandatory query rules

### 14.1 Scope rules

- Always resolve table-specific account scope through Account Data Binding.
- Do not assume one `group_level_id` works across all Flipkart tables.
- Use `group_level_id = 22` for `flipkart_commission` and `flipkart_cashback` where documented.
- Use `group_level_id = 66388` for `flipkart_settlement` where documented.
- Validate `flipkart_oms` group scope because multiple values are mentioned: `22`, `26`, `65787`, `65853`.

### 14.2 Active-row rules

- Apply `is_active = true` where the table has `is_active`.
- The OMS active row rate is low; missing active filter can massively inflate row counts.
- Do not apply `is_active` to a table unless it exists.

### 14.3 Date rules

- Use `created_date` for commission and cashback event-date analysis.
- Use `settlement_date` for payout/settlement date analysis.
- Use `created_date` vs `settlement_date` for settlement lag only when dispatch date is unavailable.
- Treat string date fields such as invoice date alternatives as unsafe until parsed.

### 14.4 Transaction/status rules

- Define transaction type explicitly for cashback metrics.
- Do not use cashback `forward cancel` as a generic order cancellation count without validating OMS.
- Do not drop cashback rows with null document type/subtype by default.
- Use `description` as primary fee type in commission.

### 14.5 Join and grain rules

- Strip `OD` prefix when joining OD-prefixed tables to `flipkart_commission`.
- Pre-aggregate commission rows by order/item before joining to settlement.
- Do not join commission line rows to settlement and then sum settlement amounts.
- Use order-item grain for settlement-to-commission and cashback-to-settlement reconciliation.

### 14.6 Numeric casting rules

- Use decimal `charged_amount` and `total_tax` in commission where available.
- Cast string legacy fields before arithmetic.
- Do not mix string and decimal financial fields without explicit casting.

### 14.7 Tax and TCS/TDS rules

- Treat GST on marketplace fees as claimable input tax credit unless the metric asks for cash deduction.
- Treat TCS/TDS as reclaimable cash-flow deductions, not default permanent cost.
- Validate 18% GST on marketplace fee using fee amount and `total_tax` / `gst_on_mp_fees`.

### 14.8 Settlement and realization rules

- Use `flipkart_settlement.settled_amount` as the primary net settlement field.
- Use `sale_settled_amount` as the realization denominator where appropriate.
- Prefer `mp_fee` over sparse granular settlement fee columns for aggregate fee burden.
- Separate FBF/NFBF and prepaid/postpaid when diagnosing realization.

### 14.9 Platform-specific forbidden assumptions

- Do not assume Shopsy orders have commission.
- Do not assume FBF and NFBF have different commission rates; source says commission is the same.
- Do not assume commission details have `OD`-prefixed order IDs.
- Do not assume granular settlement fee columns are complete.
- Do not assume settlement reaching Flipkart ledger means bank credit has arrived.

---

## 15. Data-quality and semantic caveats

### 15.1 Cross-table caveats

- Schema location differs in examples for settlement (`zs_observe` vs `zs_refined`). Validate during canonical ingestion.
- `group_level_id` differs across tables.
- OD prefix mismatch is a major join risk.
- Commission and cashback are not one-row-per-order base tables.

### 15.2 Scope caveats

- Settlement uses `group_level_id = 66388`; commission/cashback use `22`; OMS has multiple possible values.
- Account filters should be extracted as Account Data Bindings.
- Do not hardcode a single Flipkart scope in metric cards.

### 15.3 Status caveats

- Source does not provide a complete OMS status/value taxonomy.
- Cashback document classifications can be null.
- `forward cancel` in cashback is a cashback reversal, not necessarily the source of all cancellation metrics.

### 15.4 Financial caveats

- `charged_amount` means different things across tables.
- Settlement `mp_fee` should be used as aggregate fee when granular fields are NULL.
- FBF + Postpaid settled amount exceeding sale amount can be valid due to credits/adjustments.
- Cashback credits are not base revenue; they are promotional/offer economics.

### 15.5 Tax caveats

- GST on marketplace fees is generally claimable.
- TCS/TDS are reclaimable through filing cycles and should not be treated as permanent marketplace cost by default.
- Legacy tax fields may be strings and should be cast before use.

### 15.6 Logistics caveats

- Marketplace tables contain fulfilment and zone signals but not full courier/AWB remittance logic.
- Ekart/logistics-specific analysis should use the logistics KB.
- Reverse shipping fee is a marketplace fee component; COD remittance is a logistics/banking flow and should not be inferred solely from marketplace settlement.

### 15.7 Type-casting caveats

- Commission and cashback contain many legacy string fields.
- Use decimal fields where documented as authoritative.
- Cast string fields with safe casting before arithmetic.

### 15.8 Legacy / duplicate / migration-residue fields

- Settlement contains many `*_json` columns that may represent alternate/secondary data.
- Commission and cashback contain old string-based financial/tax columns and temporary/migration variants.
- Use primary curated fields unless the user specifically asks to reconcile legacy source formats.

---

## 16. Supported question patterns

### 16.1 Sales and revenue questions

- What was Flipkart GMV last month?
- What was net revenue after returns?
- How many Flipkart orders were fulfilled via FBF vs NFBF?
- What was the Shopsy order contribution?

### 16.2 Settlement and realization questions

- What was Flipkart seller realization rate?
- Why is settlement lower than sale value?
- Which fulfilment/payment combination has the best realization?
- Why is FBF Postpaid settlement higher than sale amount?

### 16.3 Fee and deduction questions

- How much commission did Flipkart charge?
- What is total fixed fee, shipping fee, reverse shipping fee, and collection fee?
- Does settlement `mp_fee` match commission invoice detail?
- What is GST on Flipkart marketplace fees?

### 16.4 Return / RTO / cancellation questions

- How much cashback was reversed on returns?
- How much reverse shipping fee was charged?
- Which cancellations triggered cashback debit notes?
- What is the refund impact on settlement?

### 16.5 GST / TCS / TDS questions

- How much TCS did Flipkart deduct?
- How much TDS did Flipkart deduct?
- How much GST was charged on marketplace fees?
- Are TCS/TDS being treated as cost or recoverable tax credit?

### 16.6 Cashback / promotion / offer questions

- What is net cashback outflow?
- Which orders have cashback credit notes?
- Which cashback credits were reversed?
- Does cashback match settlement offer fields?
- How does Shopsy cashback compare to non-Shopsy?

### 16.7 Logistics / shipping adjustment questions

- How much did Flipkart charge as shipping fee?
- How much did Flipkart charge as reverse shipping fee?
- How do fees differ between FBF and NFBF?
- Which shipping questions require logistics KB?

### 16.8 Reconciliation questions

- Which OMS orders are missing settlement?
- Does settlement `mp_fee` match commission detail?
- Do cashback amounts match offer settlement amounts?
- Which settlements are missing bank credit?

### 16.9 Diagnostic questions

- Why did Flipkart realization drop this month?
- Was the drop due to commission, shipping, collection fee, cashback, refunds, or settlement timing?
- Did FBF/NFBF mix change realization?
- Did Shopsy mix affect commission and fee rate?

### 16.10 Bank / payout matching questions

- Which Flipkart settlement IDs should match bank credits?
- Did settlement `AXISCN...` reach the bank?
- What settlement amount should be matched to bank statement?
- Which bank credits are unidentified Flipkart payouts?

---

## 17. SQL pattern appendix

SQL examples are supporting evidence for later Query Pattern, Rule, and Validation Test extraction. They are not the primary knowledge layer.

### 17.1 Seller realization

```sql
SELECT
  SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0) AS realization_rate
FROM zs_observe.flipkart_settlement
WHERE is_active = true
  AND group_level_id = 66388;
```

### 17.2 Settlement by fulfilment and payment mode

```sql
SELECT
  fulfilment_type,
  neft_type,
  COUNT(*) AS order_items,
  SUM(settled_amount) AS total_settled,
  SUM(sale_settled_amount) AS total_sale,
  SUM(mp_fee) AS total_marketplace_fee,
  SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0) AS realization_rate
FROM zs_observe.flipkart_settlement
WHERE is_active = true
  AND group_level_id = 66388
GROUP BY fulfilment_type, neft_type;
```

### 17.3 Settlement cycle / payout lag

```sql
SELECT
  AVG(DATE_DIFF('day', created_date, settlement_date)) AS avg_settlement_days,
  MIN(DATE_DIFF('day', created_date, settlement_date)) AS min_days,
  MAX(DATE_DIFF('day', created_date, settlement_date)) AS max_days
FROM zs_observe.flipkart_settlement
WHERE is_active = true
  AND settlement_date IS NOT NULL;
```

### 17.4 Fee breakdown by fee type

```sql
SELECT
  description,
  COUNT(*) AS fee_rows,
  SUM(charged_amount) AS total_fee,
  SUM(total_tax) AS gst_on_fee,
  SUM(charged_amount + total_tax) AS total_fee_deduction
FROM zs_observe.flipkart_commission
WHERE is_active = true
  AND group_level_id = 22
GROUP BY description
ORDER BY total_fee;
```

### 17.5 Settlement `mp_fee` vs commission detail

```sql
WITH commission_by_item AS (
  SELECT
    order_id,
    item_id,
    SUM(charged_amount) AS commission_total
  FROM zs_observe.flipkart_commission
  WHERE is_active = true
    AND group_level_id = 22
  GROUP BY order_id, item_id
)
SELECT
  s.order_id,
  s.item_id,
  s.mp_fee AS settlement_mp_fee,
  c.commission_total,
  s.mp_fee - COALESCE(c.commission_total, 0) AS discrepancy
FROM zs_observe.flipkart_settlement s
LEFT JOIN commission_by_item c
  ON REPLACE(s.order_id, 'OD', '') = c.order_id
 AND s.item_id = c.item_id
WHERE s.is_active = true
  AND s.group_level_id = 66388
  AND ABS(s.mp_fee - COALESCE(c.commission_total, 0)) > 0.01;
```

### 17.6 Net cashback outflow

```sql
SELECT
  SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END) AS cashback_given,
  SUM(CASE WHEN transaction_type IN ('reverse', 'forward cancel') THEN charged_amount ELSE 0 END) AS cashback_reversed,
  SUM(charged_amount) AS net_cashback
FROM zs_observe.flipkart_cashback
WHERE is_active = true
  AND group_level_id = 22;
```

### 17.7 Cashback by document type

```sql
SELECT
  transaction_type,
  document_type,
  document_sub_type,
  COUNT(*) AS records,
  SUM(charged_amount) AS total_amount,
  AVG(charged_amount) AS avg_amount
FROM zs_observe.flipkart_cashback
WHERE is_active = true
  AND group_level_id = 22
GROUP BY 1, 2, 3
ORDER BY records DESC;
```

### 17.8 Cashback vs settlement offer reconciliation

```sql
WITH cashback_by_item AS (
  SELECT
    order_id,
    item_id,
    SUM(charged_amount) AS total_cashback
  FROM zs_observe.flipkart_cashback
  WHERE is_active = true
    AND group_level_id = 22
  GROUP BY order_id, item_id
)
SELECT
  cb.order_id,
  cb.item_id,
  cb.total_cashback,
  s.offer_settled_amount,
  s.offer_adjustment_settled_amount,
  cb.total_cashback
    - COALESCE(s.offer_settled_amount, 0)
    - COALESCE(s.offer_adjustment_settled_amount, 0) AS discrepancy
FROM cashback_by_item cb
JOIN zs_observe.flipkart_settlement s
  ON cb.order_id = s.order_id
 AND cb.item_id = s.item_id
WHERE s.is_active = true
  AND s.group_level_id = 66388
  AND ABS(
    cb.total_cashback
    - COALESCE(s.offer_settled_amount, 0)
    - COALESCE(s.offer_adjustment_settled_amount, 0)
  ) > 0.01;
```

### 17.9 Shopsy vs non-Shopsy cashback

```sql
SELECT
  is_shopsy_order_,
  COUNT(*) AS events,
  SUM(charged_amount) AS total_cashback,
  AVG(charged_amount) AS avg_cashback
FROM zs_observe.flipkart_cashback
WHERE is_active = true
  AND group_level_id = 22
  AND transaction_type = 'forward'
GROUP BY is_shopsy_order_;
```

### 17.10 GST/TCS/TDS validation

```sql
SELECT
  SUM(mp_fee) AS total_mp_fee,
  SUM(gst_on_mp_fees) AS gst_on_mp_fees,
  SUM(total_tcs_amount) AS total_tcs,
  SUM(total_tds_amount) AS total_tds
FROM zs_observe.flipkart_settlement
WHERE is_active = true
  AND group_level_id = 66388;
```

### 17.11 Monthly settled vs sale amount

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  SUM(sale_settled_amount) AS gross_sale,
  SUM(settled_amount) AS net_settled,
  SUM(mp_fee) AS total_fees,
  SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0) AS realization_pct
FROM zs_observe.flipkart_settlement
WHERE is_active = true
  AND group_level_id = 66388
GROUP BY 1
ORDER BY 1;
```

---

## 18. Extraction guidance

Expected extracted card families:

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

Important extraction notes:

- Extract Flipkart as `platform.flipkart` with platform type `marketplace`.
- Extract Flipkart India as platform context.
- Extract table-specific Account Data Bindings because `group_level_id` differs across OMS, settlement, commission, and cashback.
- Extract `flipkart_commission` as a fee detail / invoice table, not a settlement table.
- Extract `flipkart_cashback` as cashback / credit-debit note table, not base revenue.
- Extract `flipkart_settlement` as the settlement ledger and payout reference source.
- Mark `flipkart_oms` detailed schema as needing validation because the source section appears mislabeled and repeats cashback content.
- Extract OD-prefix normalization as a Relationship caveat, Query Rule, and Validation Test.
- Extract Shopsy as a sub-platform / value-profile flag using `is_shopsy_order_` string semantics.
- Extract FBF/NFBF mappings between OMS and settlement as value profiles and relationship guidance.
- Extract `settlement_id` as a possible payout/bank reference for marketplace-to-bank reconciliation.
- Extract TCS/TDS treatment as cash-flow deduction but reclaimable tax-credit caveat.
- Extract settlement-to-bank reconciliation as a cross-domain retrieval note requiring Banking KB.

Final principle:

```text
Flipkart-specific knowledge stays in this curated marketplace content.
The ingestion pipeline should remain generic across marketplaces.
```
