---
title: Amazon Marketplace Knowledge Base
doc_type: marketplace_raw_knowledge
domain: marketplace_finance
platforms: [amazon]
platform_types: [marketplace]
platform_contexts:
  - amazon.in
  - amazon.com
  - amazon.fr
  - amazon.es
related_domains:
  - marketplace_finance
  - settlement_reconciliation
  - return_analysis
  - fee_reconciliation
  - gst_compliance
  - cash_flow
  - logistics_enrichment
  - marketplace_to_bank_reconciliation
country: India primary, international secondary
currency: INR primary, USD/CAD/EUR secondary where international rows exist
primary_scope_keys:
  - group_id: 9
  - group_level_id: 22
  - group_level_id: 26
  - group_level_id: 123
primary_entities:
  - Amazon India seller account 1 / primary India account
  - Amazon India seller account 2 / secondary India account
  - Amazon International accounts for US, France, Spain where applicable
tables:
  - zs_observe.amazon_oms
  - zs_observe.amazon_settlement
  - zs_observe.amazon_disbursment
  - zs_observe.amazon_fee_preview
  - zs_observe.amazon_returns
  - zs_observe.amazon_sku_master
  - zs_observe.amazon_shipping_invoice
  - zs_observe.amazon_recon_report
optional_modules:
  - fee_preview_expected_vs_actual
  - line_level_disbursement_detail
  - safe_t_reimbursements
  - fee_recovery_on_returns
  - packaging_weight_optimization
  - international_returns_inactive_note
  - marketplace_to_bank_reconciliation_note
status: draft
owner: finance_data_team
created_for: ZenStatement Context Engineering KB
source_documents:
  - Amazon Recon Doc.docx
  - marketplace_gold_std_raw_md_frame.md
authoring_note: >
  Curated raw markdown knowledge document following the Marketplace Raw Markdown
  Gold Standard Frame. This is intentionally not card YAML, not canonical JSON,
  and not manually authored graph edges. It is human-readable source knowledge
  for semantic chunking, intermediate card extraction, validation, graph creation,
  retrieval indexing, and evidence metadata generation.
---

# Amazon Marketplace Knowledge Base

## 1. How to use this document

This is a curated raw markdown knowledge document for the Amazon marketplace domain in ZenStatement.

This document is intentionally **not card YAML**. It does not manually author canonical card JSON, graph edges, embeddings, lookup keys, or retrieval metadata. It is written as human-readable source knowledge so the ingestion pipeline can later produce semantic chunks, candidate cards, relationships, value profiles, metric implementations, process cards, reconciliation profiles, query patterns, rules, validation tests, output contracts, retrieval indexes, and evidence metadata.

This document follows the Marketplace Raw Markdown Gold Standard Frame so Amazon can be processed by the same generic marketplace ingestion pipeline as Flipkart, Myntra, Nykaa, and future marketplaces.

This document should support extraction of:

- Business hierarchy knowledge for Amazon marketplace accounts and `group_level_id` mappings.
- Data understanding for Amazon OMS, settlement, disbursement, fee preview, and returns tables.
- Metric understanding for revenue, settlement, seller realization, fee burden, fee recovery, returns, GST, TCS/TDS, SAFE-T, packaging, and weight optimization.
- Process understanding for order-to-settlement, settlement-cycle, return-to-refund, fee-preview-to-actual-fee, SAFE-T recovery, and packaging/weight dispute flows.
- Reconciliation understanding for OMS to settlement, settlement to disbursement, fee preview to actual fees, return to refund impact, SAFE-T reimbursement, and settlement-to-bank extension.
- Execution guidance for mandatory filters, date safety, aggregation grain, account scoping, joins, null handling, and analytical pitfalls.

---

## 2. Marketplace overview and business context

### 2.1 Marketplace role

Amazon is a marketplace intermediary. The buyer pays Amazon, not the seller directly. Amazon deducts commercial fees, fulfilment charges, taxes withheld/collected, promotions, and adjustments before transferring a net settlement amount to the seller.

The Amazon seller financial stack is:

```text
Buyer pays gross order amount
→ Amazon deducts referral / commission fee
→ Amazon deducts shipping / weight handling fee
→ Amazon deducts fixed closing fee
→ Amazon deducts technology / platform fee
→ Amazon deducts pick-and-pack fee for FBA
→ Amazon deducts TCS under GST
→ Amazon deducts TDS under Section 194-O
→ Amazon applies seller-funded promotions / rebates
→ Amazon adds reimbursements or adjustments where applicable
→ seller receives net settlement in a settlement cycle
```

Key principle:

```text
The seller never directly receives the buyer's gross payment.
Amazon nets all debits and credits, then transfers the net settlement amount.
```

### 2.2 Seller / brand context

The Amazon data is partitioned by `group_id` and `group_level_id`.

Known scope configuration:

| group_id | group_level_id | Marketplace / account meaning |
|---:|---:|---|
| 9 | 22 | Amazon India primary seller account; current default India account |
| 9 | 26 | Amazon India secondary seller account |
| 9 | 123 | Amazon International accounts, including US, France, and Spain |

For India operations, the historical default is:

```sql
group_level_id = 22
```

However, future queries should not assume only account 22 exists. Runtime account scope must be resolved through Business Hierarchy and Account Data Binding during extraction.

### 2.3 Commercial model

Amazon monetizes seller transactions through:

- referral / commission fee,
- weight-handling / shipping fee,
- closing fee,
- technology fee,
- FBA pick-and-pack fee,
- FBA inventory/storage/removal fees,
- advertising and service fees,
- tax deductions and collections such as TCS and TDS,
- miscellaneous adjustments, clawbacks, reimbursements, and SAFE-T recoveries.

Amazon settlement is usually cycle-based. Settlement periods are identified by `settlement_id`. Amazon groups transactions into roughly two-week settlement cycles and transfers net payout after the cycle closes.

### 2.4 Storefronts, sub-platforms, or fulfilment programs

Amazon context in this document includes:

| Context | Meaning |
|---|---|
| Amazon India / `amazon.in` | Primary active India marketplace context, INR |
| Amazon International / `amazon.com`, `amazon.fr`, `amazon.es` | International context under group 123 where available |
| B2C India | Retail consumer orders, usually `metadata = 'B2C'` |
| B2B India | Business buyer orders, usually `metadata = 'B2B'` or `destination_gst_id IS NOT NULL` |
| International orders | `metadata IS NULL` in OMS; separate currency and reconciliation treatment |
| FBA / AFN | Amazon fulfils using Amazon fulfilment centers; higher fulfilment fees |
| MFN / EasyShip | Seller fulfils or uses Amazon EasyShip; different logistics responsibility |

Fulfilment mapping:

| `fulfilment_channel` | `fulfilment_type` | Operational meaning |
|---|---|---|
| `AFN` | `FBA` | Amazon warehouses, picks, packs, and ships; seller pays FBA/pick-pack fees |
| `AFN` | `Other` | Amazon fulfils via a non-standard Amazon logistics method |
| `MFN` | `Easyship` | Seller ships using Amazon EasyShip; seller bears more logistics risk |
| `MFN` | Merchant Fulfilled | Seller-defined fulfilment; minimal Amazon fulfilment involvement |

Delivery zones influence shipping cost:

| Zone | Meaning | Cost profile |
|---|---|---|
| Local | Same city delivery | Lowest |
| Regional | Neighboring states / nearby region | Medium |
| National | Inter-state / national delivery | High |
| Remote | Difficult or remote delivery areas | Highest |

### 2.5 What this marketplace data can and cannot answer

This Amazon KB can answer:

- gross sales, net revenue, AOV, and return rate,
- seller realization and net settlement,
- fee burden, commission, shipping fee, closing fee, tech fee, pick-pack fee,
- fee recovery on returns,
- fee preview expected fee versus actual disbursement fee,
- GST / TCS / TDS interpretation,
- SAFE-T and reimbursement recovery,
- packaging and volumetric-weight optimization,
- order-to-settlement and settlement-to-disbursement reconciliation,
- India versus international segmentation where data is active.

This Amazon KB cannot fully answer without other KBs:

- actual bank-credit matching unless banking KB and marketplace-to-bank reconciliation KB are retrieved,
- external courier movement unless logistics data exists and is linked by order/AWB,
- international return analysis currently, because `amazon_returns` has no active rows,
- contractual fee truth unless seller-specific rate cards are available.

---

## 3. Scope and account context

### 3.1 Active platform context

The primary active Amazon platform context is Amazon India (`amazon.in`). International marketplaces such as Amazon US, France, and Spain are referenced under `group_level_id = 123`, but active data availability differs by table.

### 3.2 Seller / account identifiers

Known identifiers:

| Identifier | Meaning |
|---|---|
| `group_id = 9` | Amazon client / parent group identifier |
| `group_level_id = 22` | Amazon India primary seller account |
| `group_level_id = 26` | Amazon India secondary seller account |
| `group_level_id = 123` | Amazon International context: US, France, Spain |
| `marketplace` | Marketplace code such as `amazon.in`, `amazon.com`, `amazon.fr`, `amazon.es` |
| `account_type` | Electronic/COD in India; Standard/Invoiced in US context |

### 3.3 Default scope filters

Default India account filter:

```sql
group_level_id = 22
```

Mandatory active-row pattern where the table has these fields:

```sql
WHERE is_active = true
```

Optional validation filters where appropriate:

```sql
AND zen_status = true
AND is_duplicated = false
```

### 3.4 Table-specific scope differences

| Table | Scope notes |
|---|---|
| `amazon_oms` | India B2B/B2C and international orders present; active India order analysis usually uses `group_level_id = 22`; `metadata` distinguishes B2B/B2C/International |
| `amazon_settlement` | Contains India and international settlement records; `group_level_id` is integer; use `22`, `26`, or `123` based on account |
| `amazon_disbursment` | Amazon India only; table spelling is `disbursment`; `group_level_id` can be 22 or 26 |
| `amazon_fee_preview` | Amazon India only; apparel category; FBA/fulfilled-by-Amazon fee estimates |
| `amazon_returns` | International returns table for US/Canada; `group_level_id = 123`; currently all records inactive due to `FILE_DELETED` |

### 3.5 Reference-table exceptions

`amazon_sku_master`, `amazon_shipping_invoice`, and `amazon_recon_report` are referenced as related tables in source context. Their availability, filters, and grain should be validated before using them as authoritative sources.

### 3.6 Scope caveats

- Do not hardcode `group_level_id = 22` for every Amazon query.
- Do not compare India and international realization rates directly.
- `group_level_id` is an integer in Amazon settlement and should be filtered as `= 22`, not `= '22'`.
- Account filters belong to Account Data Binding extraction, not to Table Cards directly.
- Some tables are India-only, while others contain international context.

---

## 4. Table family overview

| Table | Business role | Grain | Primary use | Required filters | Important caveats |
|---|---|---|---|---|---|
| `zs_observe.amazon_oms` | Order management system master | Order line / item-level transaction row | Sales, returns, cancellations, GST, geography, fulfilment, product analysis | `is_active = true`; usually `transaction_type = 'forward'` for gross sales; group filter from scope | Active rate is very low due to duplicates; `cancel` is common; revenue must filter transaction type explicitly |
| `zs_observe.amazon_settlement` | Settlement ledger | Settlement transaction line | Cash flow, seller realization, settlement waterfall, fees, refunds, reimbursements | `is_active = true`; group filter; safe date fields | 64K+ active rows have `type = NULL`; do not drop blindly; `date_time` is varchar and unsafe for filtering |
| `zs_observe.amazon_disbursment` | Line-level disbursement detail | One row per order financial component | Actual fee breakdown, unit economics, fee recovery, SAFE-T, disbursement reconciliation | `is_active = true`; transaction-type filter | Table name is misspelled; aggregate before joining; ItemFees mix charges and refund credits |
| `zs_observe.amazon_fee_preview` | SKU-level expected fee estimate | One row per SKU fee preview | Expected vs actual fee reconciliation, packaging/weight optimization, cost planning | `is_active = true AND zen_status = true AND is_duplicated = false` | `zen_status` and `is_duplicated` are boolean; `referal_fee` percentage differs from `referral_fee` amount |
| `zs_observe.amazon_returns` | International customer returns | International return row | US/Canada return reason analysis, fraud, damage, SAFE-T attribution | `is_active = true` when re-ingested | Currently all records inactive; India returns live in `amazon_oms` as `transaction_type = 'reverse'` |
| `zs_observe.amazon_sku_master` | SKU/product reference | SKU-level product reference | Weight, dimension, category enrichment | Validate before use | Useful for cross-checking dimensions and product metadata |
| `zs_observe.amazon_shipping_invoice` | Shipping invoice evidence | Shipping invoice line | Actual shipping invoice validation | Validate before use | Mentioned as relationship source; schema details not curated in this document |
| `zs_observe.amazon_recon_report` | Aggregated reconciliation report | Aggregated report row | Recon waterfall summaries | Validate before use | Contains labels such as “Yet to be Settled”; not a substitute for raw table reconciliation |

---

## 5. End-to-end transaction lifecycle

### 5.1 Forward flow: order to settlement

Amazon forward sales flow:

```text
Customer places order on Amazon
→ order appears in amazon_oms as transaction_type = 'forward'
→ tax, fulfilment, product, geography, and payment attributes are captured
→ Amazon records order and related debits/credits in settlement/disbursement tables
→ Amazon deducts commission, shipping, closing, tech, fulfilment, TCS, TDS, promotions, and other charges
→ Amazon nets all settlement-period transactions by settlement_id
→ seller receives net settlement amount
```

Primary tables:

- Expected/order side: `amazon_oms`
- Settlement/cash-flow side: `amazon_settlement`
- Line-level component side: `amazon_disbursment`
- Expected-fee side: `amazon_fee_preview`

Important identifiers:

- `order_id`
- `item_id`
- `sku_id`
- `settlement_id`
- `marketplace`
- `group_level_id`

### 5.2 Reverse flow: return, cancellation, refund, clawback

Amazon reverse and cancellation flow:

```text
Customer return, cancellation, replacement, or refund event occurs
→ OMS records reverse/cancel/replacement/einvoicecancel transaction type
→ settlement records Refund, Fulfilment Fee Refund, Adjustment, SAFE-T, Reimbursement, Clawback, or other debit/credit type
→ disbursement rows show principal refund, fee reversals, refund commission, TCS/TDS behavior, and reimbursements
→ seller bears unrecovered fees and receives any eligible recovery or reimbursement
```

Important reverse economics:

- Principal is refunded to the customer.
- Shipping fee is not directly reversed on returns; recovery only through Fulfilment Fee Refund / weight dispute where applicable.
- Tech fee is not directly reversed on returns; recovery only through Fulfilment Fee Refund where applicable.
- Pick-and-pack fee is not recovered.
- Commission is partially recovered through refund commission.
- Closing fee is partially recovered.
- TCS is partially recovered as a timing item.
- TDS is not reversed on returns and should be modeled as cash-flow / tax-credit impact.

### 5.3 Adjustment flow: fees, SAFE-T, fulfilment fee refunds, reimbursements, service fees

Amazon adjustment-like financial movements include:

- `Fulfilment Fee Refund`: Amazon corrects overcharged fees, often related to weight/dimension disputes.
- `SAFE-T Reimbursement`: Amazon compensates seller when Amazon/buyer fault exists.
- `Reimbursements`: lost inventory, customer-service, or general reimbursements.
- `Adjustment`: inventory or settlement corrections.
- `Service Fee`: advertising, subscriptions, coupon fees, or marketplace service charges.
- `FBA Inventory Fee`: storage, removal, disposal, or inventory costs.
- `Clawbacks`: Amazon recovers previously paid amounts.
- `Other Transactions`: miscellaneous positive or negative events.

These rows affect cash flow and seller realization even when they are not direct product revenue.

### 5.4 Payout flow: settlement to seller bank

Amazon groups transactions by settlement period and settlement ID. All debits and credits in a period are netted and transferred to the seller bank account as a payout.

Known concept:

```text
order placed during settlement period
→ order appears in OMS
→ order appears in settlement/disbursement when Amazon settles it
→ settlement period closes
→ net amount is transferred to seller bank
```

If the user asks for Amazon settlement to bank reconciliation, retrieval should combine:

```text
Amazon marketplace settlement knowledge
+ banking statement knowledge
+ marketplace_to_bank reconciliation pattern
```

This Amazon source does not fully define bank statement tables or bank-credit matching keys.

### 5.5 Timing gaps and in-flight transactions

“Yet to be Settled” means revenue recognized in `amazon_oms` but not yet appearing in `amazon_settlement` for the same period.

Concept:

```text
Yet to be Settled = OMS Revenue in period - Settlement Revenue in same period
```

This is often a legitimate timing gap, not a discrepancy. The Amazon recon report labels this as “ZB. Yet to be Settled.”

---

## 6. Entity relationships and joins

### 6.1 Primary join map

| From table | To table | Join key | Reliability / notes |
|---|---|---|---|
| `amazon_oms` | `amazon_settlement` | `order_id` | Reconciles OMS sale/refund record to Amazon settlement lines |
| `amazon_settlement` | `amazon_disbursment` | `order_id`, `settlement_id` | Settlement is higher-level; disbursement gives line-level component breakdown |
| `amazon_oms` | `amazon_disbursment` | `order_id` | Adds component-level fees and revenue lines to order context |
| `amazon_fee_preview` | `amazon_disbursment` | `sku = sku_id` | Compares expected SKU-level fees to actual disbursement fees; aggregate disbursement by SKU first |
| `amazon_fee_preview` | `amazon_oms` | `sku = sku_id` | Adds expected fee and weight context to OMS SKU/order volume |
| `amazon_fee_preview` | `amazon_sku_master` | `sku = sku_id` | Cross-checks dimensions, weights, and category |
| `amazon_returns` | `amazon_oms` | `order_id` | International returns can relate to OMS returns when active |
| `amazon_returns` | `amazon_settlement` | `order_id` | Return settlements appear as `type = 'Refund'` |
| `amazon_shipping_invoice` | `amazon_oms` | `order_id` | Shipping invoice evidence where available |

### 6.2 Secondary validation keys

Useful secondary keys:

- `item_id` for order item context,
- `sku_id` / `sku` for SKU-level fee and product analysis,
- `settlement_id` for payout-period alignment,
- `marketplace` for `amazon.in`, `amazon.com`, `amazon.fr`, `amazon.es`,
- `group_level_id` for account scope,
- `currency_type` for currency separation.

### 6.3 Join reliability and match rates

The source provides conceptual join relationships but does not provide final match-rate values for all join pairs in this curated frame. Treat each relationship as card-extractable with confidence based on source statements:

- OMS ↔ Settlement by `order_id`: high conceptual relevance for reconciliation.
- Settlement ↔ Disbursement by `order_id` and `settlement_id`: high conceptual relevance; aggregate before comparison.
- Fee Preview ↔ Disbursement by SKU: high relevance for expected-vs-actual fee reconciliation; requires grain alignment.
- International Returns: currently low runtime usability because table has no active records.

### 6.4 Grain mismatch and double-counting risks

Important grain warnings:

- `amazon_oms` is order / item-level transaction data.
- `amazon_settlement` is settlement transaction line data.
- `amazon_disbursment` is many-rows-per-order component detail.
- `amazon_fee_preview` is SKU-level expected fee data.
- `amazon_returns` is return-row data for international returns.

Do not join `amazon_disbursment` directly to order-level or settlement-level tables and then aggregate order amounts without pre-aggregation. Always aggregate component rows to the correct grain first.

### 6.5 Identifier normalization rules

- `amazon_disbursment` table name is misspelled: use exactly `amazon_disbursment`.
- `amazon_fee_preview.referral_fee` is the fee amount in rupees.
- `amazon_fee_preview.referal_fee` is the percentage column and is misspelled.
- `amazon_fee_preview.sku` joins to `amazon_disbursment.sku_id` or `amazon_oms.sku_id`.
- `amazon_settlement.sku` and `sku_id` may both exist; `sku` can be raw source field.

### 6.6 Reference / mapping table joins

Potential reference joins:

- `amazon_sku_master` by `sku_id` for product weight, dimensions, and category.
- `amazon_shipping_invoice` by `order_id` for actual shipping invoice evidence.
- `amazon_recon_report` for aggregate reconciliation waterfall labels.

These should be validated before extraction into active canonical cards if detailed schema is not available.

---

## 7. Financial waterfall and seller realization

### 7.1 Forward settlement waterfall

Amazon India settlement formula concept:

```text
total ≈ product_sales
      + selling_fees
      + fba_fees
      + shipping_credits
      + promotional_rebates
      + gift_wrap_credits
      + other_transaction_fees
      + other
      - tcs_igst
      - tcs_cgst
      - tcs_sgst
      - tds
```

Sign conventions:

- `product_sales` is positive for orders and negative for refunds.
- `selling_fees`, `fba_fees`, `other_transaction_fees`, TCS, and TDS are generally negative deductions.
- `shipping_credits` and `gift_wrap_credits` are positive credits.
- `promotional_rebates` are usually negative discounts.
- `other` varies.
- `total` is the net credited or debited amount for the settlement line.

### 7.2 Reverse / refund settlement waterfall

For returns/refunds:

```text
refund / reverse event
→ product sales are reversed or refunded
→ some fees are partially reversed
→ non-recoverable fulfilment and platform costs remain
→ settlement period may debit the seller after original payout
```

True cost of return:

```text
Return Loss = principal refunded
            + non-recovered shipping fee
            + non-recovered tech fee
            + non-recovered pick-and-pack fee
            + unrecovered commission portion
            + unrecovered closing fee portion
            + TCS timing impact
            + TDS cash-flow impact
```

### 7.3 Non-order / adjustment waterfall

Non-order or adjustment-like Amazon movements include:

- service fees,
- FBA inventory fees,
- fulfilment fee refunds,
- SAFE-T reimbursements,
- general reimbursements,
- clawbacks,
- inventory adjustments,
- removal fees,
- advertising fees.

These should be included in full cash-flow analysis, but excluded from pure revenue reporting unless the metric explicitly includes all settlement types.

### 7.4 Seller realization definition

Seller realization rate measures how much of gross product sales reaches the seller after marketplace deductions, fees, refunds, and adjustments.

Default Amazon settlement implementation:

```text
Seller Realization Rate = SUM(total) / SUM(product_sales where type = 'Order')
```

Recommended source:

```text
amazon_settlement
```

Benchmark ranges from source:

| Context | Benchmark realization |
|---|---:|
| India group 22 / 26 | approximately 70%–78% |
| US group 123 | approximately 50%–55% |

Realization far outside these ranges should trigger investigation into high returns, unusual service fees/ad spend, inventory write-offs, reimbursements, or data scope mismatch.

### 7.5 Field-level payout interpretation

| Field | Table | Meaning |
|---|---|---|
| `amazon_settlement.total` | settlement | Net amount credited/debited for settlement line |
| `amazon_settlement.product_sales` | settlement | Product sale/refund amount used as realization denominator for orders |
| `amazon_oms.settled_amount` | OMS | Amount settled for this order where populated; not the primary settlement ledger |
| `amazon_disbursment.charged_amount` | disbursement | Component-level credit/debit amount |
| `amazon_disbursment.order_level_total` | disbursement | Pre-aggregated order total; use cautiously |
| `amazon_fee_preview.gross_commission` | fee preview | Expected total fee estimate per SKU |
| `amazon_fee_preview.shipping_amount` | fee preview | Expected weight handling / shipping fee |

### 7.6 Known benchmark ranges or observed snapshots

From source guidance:

- India seller realization: 70%–78%.
- US realization: 50%–55%.
- India general return-rate healthy range: below 15%; concerning above 25%.
- Apparel return-rate healthy range: below 20%; concerning above 35%.
- Electronics return-rate healthy range: below 10%; concerning above 20%.
- High-value item return-rate healthy range: below 12%; concerning above 20%.
- SAFE-T recovery benchmark: 15%–30% recovery on eligible returns.
- Apparel referral fee often around 17%–19%.
- Fee preview total fee burden for apparel often around 22%–26% of MRP.
- Referral fee is typically 60%–75% of expected gross commission.

---

## 8. Fees, deductions, taxes, promotions, and adjustments

### 8.1 Commission and marketplace fees

Commission / referral fee:

- Percentage of selling price.
- Varies by category.
- Apparel reference range: roughly 17%–19%.
- Charged on forward orders.
- Around 50% recovered on returns through refund commission.
- Most important variable cost and sensitive to price changes.

Actual commission source:

```text
amazon_disbursment where mp_fee_type = 'ItemFees' and charged_amount_type = 'commission'
```

Settlement summary source:

```text
amazon_settlement.selling_fees
```

Expected commission source:

```text
amazon_fee_preview.referral_fee
```

### 8.2 Fixed / closing / platform fees

Closing fee:

- Flat per transaction.
- Source example for apparel: around ₹51.
- Around 40%–45% reversed on returns.
- Disproportionately burdens low-price SKUs.

Technology fee:

- Platform / technology fee.
- Not directly reversed on returns.
- Only recoverable via Fulfilment Fee Refund in weight/fee correction scenarios.

Other transaction fees:

- Appear in settlement as `other_transaction_fees`.
- Appear in disbursement component rows under `ItemFees` and other classifications.

### 8.3 Shipping, freight, fulfilment, and reverse logistics fees

Amazon shipping / weight-handling fee:

- Based on final billing weight.
- Charged on forward orders.
- Not directly reversed on returns.
- Primary packaging optimization lever.

FBA / fulfilment fees:

- FBA fees include fulfilment and storage-related charges.
- Pick-and-pack fee is warehouse handling labour for FBA orders.
- Pick-and-pack fee is not recovered on returns.
- FBA Inventory Fee rows represent storage, removal, disposal, and other inventory costs.

### 8.4 Payment / collection / payment gateway fees

Amazon data includes `zen_vendor_payout_payment_gateway_fee` in settlement-derived computed payout fields, but the source document does not define a separate payment gateway table. Treat payment gateway fee as a marketplace fee component unless payment gateway KB is retrieved separately.

### 8.5 Promotional credits, discounts, offers, and rebates

Promotions in Amazon data include:

- `item_promo_discount`,
- `shipping_promo_discount`,
- `gift_wrap_promo_discount`,
- `promotional_rebates`,
- disbursement rows under `mp_fee_type = 'Promotion'`, such as shipping discount, promo rebates, product tax discount, and shipping tax discount.

Promotion amounts usually reduce seller realization if seller-funded.

### 8.6 Reimbursements, protection funds, SAFE-T, incentives, and penalties

SAFE-T reimbursement:

- Seller Assurance for E-Commerce Transactions.
- Used when Amazon, carrier, fulfilment center, or buyer behavior is at fault.
- Appears in settlement as `type = 'SAFE-T Reimbursement'`.
- Appears in disbursement as `mp_fee_type = 'Other Transactions'`, `charged_amount_type = 'reimbursement'`, or `transaction_type = 'SAFE-T Reimbursement'`.

SAFE-T triggers:

| Trigger | Meaning |
|---|---|
| `DAMAGED_BY_FC` | Amazon fulfilment center damaged the item |
| `DAMAGED_BY_CARRIER` | Carrier damaged item in transit |
| `SWITCHEROO` | Buyer returned different/empty item |
| `NOT_AS_DESCRIBED` where listing was accurate | Buyer misrepresented reason |

General reimbursements:

- Settlement type `Reimbursements`.
- Disbursement types such as `Other Transactions` or `FBA Inventory Reimbursement`.
- Can represent lost inventory, customer-service adjustments, or operational credits.

### 8.7 TCS and TDS

TCS:

- Tax Collected at Source under GST.
- Amazon deducts approximately 1% of gross sales.
- Split may be 0.5% CGST + 0.5% SGST for intra-state or 1% IGST for inter-state.
- Partially recovered on return transactions.
- Cash-flow timing difference and claimed in GST return.

TDS:

- Tax Deducted at Source under Section 194-O of the Income Tax Act.
- Amazon deducts 1% on gross sales.
- Not reversed on returns.
- Claimed as income-tax credit.
- Model as permanent deduction in margin/cash-flow calculations if the business view treats tax credit timing as cost.

### 8.8 GST on products and GST on marketplace fees

India GST model:

| Scenario | Tax type | Indicator |
|---|---|---|
| Source state differs from destination state | IGST | `tax_igst_rate > 0` |
| Source state equals destination state | CGST + SGST | `tax_cgst_rate > 0` and `tax_sgst_rate > 0` |
| Union Territory | UGST | `tax_ugst_rate > 0` |

Important rule:

```text
Use charged_amount_excluding_tax as the denominator for GST rate validation.
```

If `total_tax / charged_amount` is used, effective rate appears around 15.25% instead of 18% because `charged_amount` includes tax.

### 8.9 Fee recovery on returns

Fee recovery matrix:

| Fee | Reversed on refund transaction? | Via Fulfilment Fee Refund? | Permanent loss / impact |
|---|---|---|---|
| Commission | Around 50% | No | Around 50% unrecovered |
| Closing fee | Around 40%–45% | No | Around 55%–60% unrecovered |
| Shipping fee | No | Yes, only weight dispute | Usually lost |
| Tech fee | No | Yes, only fee correction | Usually lost |
| Pick-and-pack fee | No | No | Lost |
| TCS | Around 38%–40% | No | Timing difference |
| TDS | No | No | Tax credit / cash-flow impact |

### 8.10 Marketplace-specific naming traps

- `amazon_disbursment` is misspelled and must be used exactly.
- `amazon_fee_preview.referral_fee` is amount; `referal_fee` is percentage.
- `refund commission` in disbursement is positive and should not be treated as a fee charge.
- `date_time` in settlement is varchar and unsafe for filtering.
- `type = NULL` in settlement can still carry financial values.
- `zen_vendor_payout_*` fields are estimates, not always actual marketplace deductions.

---

## 9. Fulfilment, logistics, payment modes, and settlement cycle

### 9.1 Fulfilment models

| Fulfilment model | Codes | Business meaning | Cost impact |
|---|---|---|---|
| Fulfilled by Amazon | AFN / FBA | Amazon stores, picks, packs, ships | Higher FBA/pick-pack and national reach fees |
| Easy Ship | MFN / Easyship | Seller ships through Amazon EasyShip | Lower Amazon fees, seller logistics exposure |
| Merchant Fulfilled | MFN | Seller-defined logistics | Minimal Amazon fulfilment fees |

### 9.2 Logistics and courier signals

Amazon logistics cost is primarily represented through:

- `shipping fee` in disbursement,
- `fba_fees` in settlement,
- `shipping_amount` in fee preview,
- packaging dimensions and weight fields in fee preview,
- potentially `amazon_shipping_invoice` where available.

For physical courier events beyond Amazon tables, retrieve logistics KB only if query mentions courier, AWB, delivery, RTO, shipping invoice, or external logistics reconciliation.

### 9.3 COD vs prepaid / electronic behavior

`amazon_settlement.account_type` can distinguish Electronic vs COD for India and Standard vs Invoiced for US context. Interpret payment mode with marketplace context.

### 9.4 Settlement cycle and payout timing

Amazon settlement cycle mechanics:

- Settlement periods are identified by `settlement_id`.
- Transactions are grouped into roughly two-week settlement periods.
- All debits and credits in a period are netted.
- Seller receives one net transfer for the settlement period.
- Timing gaps between OMS and settlement are expected.

### 9.5 Bank / UTR / payout references, if available

The source Amazon marketplace document focuses on Amazon settlement and does not fully define bank statement fields or UTR matching logic. Settlement-to-bank reconciliation should use the banking KB and marketplace-to-bank reconciliation pattern when available.

### 9.6 Logistics handoff to the logistics KB

Retrieve logistics KB when Amazon analysis crosses from marketplace settlement into physical shipment/courier behavior, such as:

- delivery failures,
- RTO logistics,
- shipping invoice disputes,
- external courier freight,
- COD remittance through courier,
- AWB matching.

Do not retrieve logistics KB for pure Amazon commission, TCS/TDS, SAFE-T, settlement realization, or disbursement fee analysis unless shipping/courier context is explicitly needed.

---

## 10. Status and value semantics

### 10.1 Transaction types in `amazon_oms`

| `transaction_type` | Business meaning | `charged_amount` behavior | Include in metrics? |
|---|---|---|---|
| `forward` | Product sale shipped to customer | Positive | Use for gross revenue, AOV, GST, channel analysis |
| `reverse` | Customer return | Negative | Use for return value, refunds, net revenue |
| `cancel` | Order cancelled before shipment | Zero | Use for cancellation rate; exclude from revenue |
| `replacement` | Seller/customer-service replacement shipment | Zero | Track separately for CS/logistics cost; exclude from revenue |
| `einvoicecancel` | GST e-invoice cancelled after issue | Zero | Compliance edge case; exclude from revenue |
| NULL | Usually international or unclassified context | Varies | Handle explicitly |

Important: `cancel` can be the most common active transaction type by volume. Always filter explicitly for revenue.

### 10.2 Transaction types in `amazon_settlement.type`

| `type` | Business meaning | Sign / use |
|---|---|---|
| `Order` | Product sale | Positive revenue / settlement basis |
| `Refund` | Customer refund | Negative or reversal impact |
| `Fulfilment Fee Refund` | Amazon corrects overcharged fee | Positive recovery |
| `Adjustment` | Inventory reimbursements or corrections | Usually positive but varies |
| `Service Fee` | Advertising, subscriptions, coupon/service charges | Negative cost |
| `FBA Inventory Fee` | Storage, removal, disposal fees | Negative cost |
| `SAFE-T Reimbursement` | Amazon compensates seller for eligible return/fraud/damage | Positive recovery |
| `Reimbursements` | General reimbursements | Positive recovery |
| `Transfer` | Fund movement between periods | No direct revenue impact |
| `Clawbacks` | Amazon recovers earlier paid amounts | Negative |
| `Others` | Miscellaneous | Varies |
| NULL | Rows without transaction type | Do not drop blindly; may carry financial values |

For revenue reporting, use `type IN ('Order', 'Refund')`. For full cash-flow reporting, include all settlement types.

### 10.3 Transaction types in `amazon_disbursment`

| `transaction_type` | Meaning |
|---|---|
| `Order` | Forward sale; fees charged |
| `Refund` | Return/refund; some fees reversed |
| `Fulfillment Fee Refund` | Fee correction, often weight/dimension dispute |
| `SAFE-T Reimbursement` | Compensation for eligible buyer/Amazon/carrier fault |
| `Other` | Miscellaneous adjustment |
| `other-transaction` | Removal or operational transactions |

Always specify `transaction_type` when computing fees.

### 10.4 Disbursement `mp_fee_type` values

| `mp_fee_type` | Business category | Sign convention |
|---|---|---|
| `ItemPrice` | Buyer-paid revenue components | Positive |
| `ItemFees` | Amazon fees and commissions | Negative for charges; positive for refund commission |
| `Promotion` | Discounts / promo rebates | Negative |
| `ItemTCS` | TCS deduction under GST | Negative |
| `ItemTDS` | TDS deduction | Negative |
| `Item Fee Adjustment` | Fee refunds/corrections | Positive |
| `Other Transactions` | Reimbursements / SAFE-T / misc credits | Usually positive |
| `FBA Inventory Reimbursement` | Inventory loss/damage compensation | Positive |
| `other-transaction` | Removal fees / misc operational charges | Varies |

### 10.5 Disbursement `charged_amount_type` values

Key `charged_amount_type` values:

| Type | Business meaning |
|---|---|
| `principal` | Base item price before tax |
| `product tax` | GST on item price |
| `shipping` | Shipping charged to buyer |
| `shipping tax` | GST on shipping charge |
| `cod` | COD charge |
| `cod tax` | GST on COD charge |
| `commission` | Referral fee |
| `shipping fee` | Amazon logistics / weight handling fee |
| `closing fee` | Fixed per-order fee |
| `tech fee` | Platform technology fee |
| `pickup fee` | FBA pick-pack fee |
| `shipping chargeback` | Weight/dimension discrepancy adjustment |
| `refund commission` | Commission credit on refund; positive amount |
| `shipping discount` | Free shipping promotion |
| `promo rebates` | Promotional rebate |
| `tcs gst` | TCS deduction |
| `tds` | TDS deduction |
| `reimbursement` | SAFE-T or general reimbursement |
| `fba inventory` | FBA inventory loss/damage reimbursement |
| `removal complete` | Inventory removal fee |

### 10.6 Payment modes, fulfilment values, document values

- `amazon_oms.metadata = 'B2C'`: India consumer orders.
- `amazon_oms.metadata = 'B2B'`: India business buyer orders.
- `amazon_oms.metadata IS NULL`: international orders.
- `amazon_oms.fulfilment_channel = 'AFN'`: Amazon fulfilment.
- `amazon_oms.fulfilment_channel = 'MFN'`: merchant/seller fulfilment.
- `amazon_oms.fulfilment_type = 'FBA'`: Fulfilled by Amazon.
- `amazon_oms.fulfilment_type = 'Easyship'`: Seller ships via Amazon EasyShip.

### 10.7 Null and unknown handling

- Do not drop `amazon_settlement.type IS NULL` rows by default; they may carry financial data.
- Treat `metadata IS NULL` as international segment in OMS segmentation logic.
- Treat inactive international return records as unavailable rather than zero returns.
- Null or sparse values should be handled by use case, not globally filtered away.

---

## 11. Key metrics and business definitions

### 11.1 Gross sales / GMV

Gross sales are total sale value including tax and shipping for forward orders.

Default Amazon implementation:

```text
SUM(amazon_oms.charged_amount)
WHERE is_active = true
  AND transaction_type = 'forward'
```

For settlement-based gross product sales:

```text
SUM(amazon_settlement.product_sales)
WHERE is_active = true
  AND type = 'Order'
```

### 11.2 Net revenue after returns

Net revenue accounts for forward sales and reverse return rows.

Implementation from OMS:

```text
SUM(charged_amount)
WHERE transaction_type IN ('forward', 'reverse')
```

Reverse rows are negative, so this nets returns automatically.

### 11.3 Taxable revenue

Taxable revenue is revenue excluding GST.

Implementation:

```text
SUM(charged_amount_excluding_tax)
WHERE transaction_type = 'forward'
```

Use this for profitability analysis and GST-rate validation.

### 11.4 Principal revenue

Principal revenue is base item revenue from disbursement, excluding shipping and tax.

Implementation:

```text
SUM(charged_amount)
WHERE mp_fee_type = 'ItemPrice'
  AND charged_amount_type = 'principal'
```

### 11.5 Distinct orders, units, and line items

- Use `COUNT(DISTINCT order_id)` for orders.
- Use `COUNT(*)` for transaction rows / lines.
- Use `SUM(quantity)` for units where the quantity field is valid.

Forward-order counts from OMS:

```sql
SELECT COUNT(DISTINCT order_id) AS distinct_orders,
       COUNT(*) AS line_count,
       SUM(quantity) AS units
FROM zs_observe.amazon_oms
WHERE transaction_type = 'forward'
```

### 11.6 Average order value

AOV formula:

```text
SUM(charged_amount) / COUNT(DISTINCT order_id)
```

Use forward orders only.

### 11.7 Seller realization rate

Seller realization rate measures the percentage of gross product sales that reaches the seller after deductions and adjustments.

Default settlement formula:

```text
SUM(total) / SUM(product_sales where type = 'Order')
```

Denominator should use product sales on order rows only.

### 11.8 Net settlement amount

Net settlement amount is the total net amount credited or debited to the seller.

Default implementation:

```text
SUM(amazon_settlement.total)
```

For full cash-flow, include all settlement types. For revenue-only analysis, segment by `type` first.

### 11.9 Effective commission rate

Effective commission rate is actual commission as a percentage of principal revenue.

Implementation:

```text
ABS(SUM(commission)) / SUM(principal)
```

Actual component source:

```text
amazon_disbursment where mp_fee_type = 'ItemFees' and charged_amount_type = 'commission'
```

### 11.10 Effective fee / take rate

Effective fee rate is all marketplace fees as a percentage of principal or gross revenue.

Implementation concept:

```text
ABS(SUM(all ItemFees)) / SUM(principal)
```

Disbursement implementation:

```sql
SELECT ABS(SUM(CASE WHEN mp_fee_type = 'ItemFees'
                     THEN charged_amount END))
       / NULLIF(SUM(CASE WHEN charged_amount_type = 'principal'
                          THEN charged_amount END), 0) AS effective_fee_rate
FROM zs_observe.amazon_disbursment
WHERE transaction_type = 'Order'
```

Be careful to separate Order fees from Refund fee credits.

### 11.11 Shipping / freight cost rate

Logistics cost rate:

```text
ABS(SUM(shipping fee)) / SUM(principal)
```

Actual source:

```text
amazon_disbursment charged_amount_type = 'shipping fee'
```

Expected source:

```text
amazon_fee_preview.shipping_amount
```

### 11.12 Return rate

Return rate:

```text
COUNT(DISTINCT order_id where transaction_type = 'reverse')
/ COUNT(DISTINCT order_id where transaction_type = 'forward')
```

For India, use `amazon_oms`. For international detailed return reasons, `amazon_returns` must be re-ingested because current active rows are zero.

### 11.13 Cancellation rate

Cancellation rate:

```text
COUNT(cancel) / (COUNT(forward) + COUNT(cancel))
```

Use `amazon_oms.transaction_type = 'cancel'`.

OMS-side implementation:

```sql
SELECT 1.0 * COUNT(DISTINCT CASE WHEN transaction_type = 'cancel' THEN order_id END)
       / NULLIF(COUNT(DISTINCT CASE WHEN transaction_type IN ('forward', 'cancel') THEN order_id END), 0)
       AS cancellation_rate
FROM zs_observe.amazon_oms
```

### 11.14 Fee recovery rate on returns

Fee recovery rate:

```text
(reversed fees + fulfilment fee refunds) / charged fees
```

Use disbursement rows grouped by `charged_amount_type` and separated by `transaction_type`.

### 11.15 SAFE-T recovery rate

SAFE-T recovery rate:

```text
SUM(SAFE-T credits) / SUM(eligible return refund value)
```

Benchmark: approximately 15%–30% recovery on eligible returns.

### 11.16 TCS/TDS amount and rate

TCS:

```text
SUM(total_tcs_amount) from OMS
or SUM(tcs_igst + tcs_cgst + tcs_sgst) from settlement
```

TDS:

```text
SUM(total_tds) from OMS
or SUM(tds) from settlement
```

TCS/TDS are cash-flow deductions, but typically reclaimable through statutory returns.

### 11.17 GST rate validation

Correct GST effective rate:

```text
SUM(total_tax) / SUM(charged_amount_excluding_tax)
```

Do not use `charged_amount` as denominator for GST rate validation.

### 11.18 Settlement cycle / payout lag

Settlement cycle can be analyzed using:

- `amazon_oms.created_date`,
- `amazon_settlement.created_date`,
- `amazon_settlement.settlement_date`,
- `amazon_settlement.settlement_id`,
- `amazon_disbursment.settlement_date`.

Average payout lag from settlement:

```sql
SELECT AVG(DATE_DIFF('day', created_date, settlement_date)) AS avg_payout_lag_days
FROM zs_observe.amazon_settlement
WHERE settlement_date IS NOT NULL
  AND created_date IS NOT NULL
```

Timing gaps between OMS and settlement may be legitimate in-flight settlement.

### 11.19 Packaging / volumetric weight optimization

Volumetric weight:

```text
(longest_side × median_side × shortest_side) / 5000
```

Final billing weight:

```text
MAX(volumetric_weight, gross_weight)
```

Diagnostic:

```text
volumetric_weight > gross_weight × 1.5
```

These SKUs are high ROI for packaging review.

### 11.20 Reconciliation gap amount

Generic gap concept:

```text
Expected amount - actual amount
```

OMS revenue vs settlement product sales (per order):

```sql
SELECT o.order_id,
       SUM(o.charged_amount) AS oms_revenue,
       SUM(s.product_sales)  AS settlement_product_sales,
       SUM(o.charged_amount) - SUM(s.product_sales) AS gap_amount
FROM zs_observe.amazon_oms o
LEFT JOIN zs_observe.amazon_settlement s
       ON s.order_id = o.order_id
      AND s.type = 'Order'
WHERE o.transaction_type = 'forward'
GROUP BY o.order_id
```

Examples:

- OMS revenue minus settlement product sales.
- Settlement total minus disbursement aggregated charged amount.
- Fee preview expected fee minus actual disbursement fee.
- Expected seller realization minus observed realization.

---

## 12. Reconciliation playbook

### 12.1 OMS to settlement reconciliation

Question answered:

```text
Do Amazon OMS sales and returns appear correctly in Amazon settlement?
```

Expected side:

```text
amazon_oms forward / reverse order records
```

Actual side:

```text
amazon_settlement type = Order / Refund
```

Primary key:

```text
order_id
```

Grain:

```text
order or order-item depending on table cardinality; aggregate before comparing amounts
```

Core checks:

- Count distinct OMS forward orders vs settlement Order rows.
- Compare OMS `charged_amount` to settlement `product_sales`.
- Identify OMS orders in date range not yet in settlement.
- Classify timing gaps as “Yet to be Settled” where appropriate.

Mismatch categories:

- missing settlement,
- amount mismatch,
- timing gap / yet to be settled,
- duplicate/grain mismatch,
- wrong transaction-type inclusion.

Caveats:

- Use active filters.
- Use transaction-type filters.
- Do not confuse revenue reporting with cash-flow reporting.

### 12.2 Settlement to disbursement reconciliation

Question answered:

```text
Does settlement net amount reconcile to detailed disbursement components?
```

Expected side:

```text
amazon_settlement.total
```

Actual / detail side:

```text
SUM(amazon_disbursment.charged_amount)
```

Primary keys:

```text
order_id, settlement_id
```

Grain:

```text
aggregate disbursement to order + settlement_id before comparing
```

Mismatch categories:

- missing disbursement rows,
- settlement ID mismatch,
- order appears in different period,
- component rows duplicated,
- adjustment in separate period.

### 12.3 Fee preview / expected fee to actual fee reconciliation

Question answered:

```text
Is Amazon charging fees as expected based on SKU fee preview?
```

Expected side:

```text
amazon_fee_preview.gross_commission, referral_fee, fixed_fee, pick_and_pack_fee, shipping_amount
```

Actual side:

```text
amazon_disbursment ItemFees on Order transactions
```

Primary key:

```text
sku / sku_id
```

Grain:

```text
SKU-level expected fee versus actual fees aggregated from order-level disbursement
```

Variance logic:

```text
Expected = amazon_fee_preview.gross_commission
Actual = SUM(ItemFees) from amazon_disbursment for Order transactions
Variance = Expected + Actual
```

Actual fees are negative, so adding expected and actual gives variance.

Root causes:

- selling price differs from MRP,
- weight/dimension data mismatch,
- category reclassification,
- fee tier changes,
- Amazon used different dispatch weight,
- fixed/closing/pick-pack tiers changed.

### 12.4 Promotion / rebate reconciliation

Question answered:

```text
How much did promotions and rebates reduce seller realization?
```

Expected / evidence side:

```text
amazon_oms item_promo_discount, shipping_promo_discount, gift_wrap_promo_discount
amazon_settlement promotional_rebates
amazon_disbursment mp_fee_type = 'Promotion'
```

Caveats:

- Distinguish seller-funded promotion from Amazon-funded or platform adjustment if source supports it.
- Promotion rows may reduce payout but do not always represent marketplace fee.

### 12.5 Reverse / return / refund reconciliation

Question answered:

```text
Do returned Amazon orders have the expected refund, fee reversal, and recovery behavior?
```

Expected side:

```text
amazon_oms transaction_type = 'reverse'
```

Actual side:

```text
amazon_settlement type = 'Refund'
amazon_disbursment transaction_type = 'Refund'
```

Supporting side:

```text
amazon_returns when active for international return reasons
```

Mismatch categories:

- OMS reverse missing refund settlement,
- refund exists without OMS reverse,
- fees not recovered as expected,
- SAFE-T eligible return not reimbursed,
- refund in later settlement period.

### 12.6 SAFE-T / reimbursement reconciliation

Question answered:

```text
Are eligible Amazon-caused, carrier-caused, fraud, or buyer-fault returns recovered through SAFE-T or reimbursement?
```

Expected side:

```text
eligible return events / reasons
```

Actual side:

```text
amazon_settlement type = 'SAFE-T Reimbursement' or 'Reimbursements'
amazon_disbursment transaction_type = 'SAFE-T Reimbursement' or mp_fee_type = 'Other Transactions'
```

Primary keys:

```text
order_id, sku_id where available
```

Caveats:

- International return-reason table currently inactive.
- India returns in OMS lack detailed standardized reason codes.
- SAFE-T eligibility may need business rules not fully present in raw data.

### 12.7 Shipping / freight / logistics adjustment reconciliation

Question answered:

```text
Are Amazon shipping fees and weight-handling charges aligned to expected weight and dimensions?
```

Expected side:

```text
amazon_fee_preview.shipping_amount based on final_weight
```

Actual side:

```text
amazon_disbursment charged_amount_type = 'shipping fee'
amazon_disbursment charged_amount_type = 'shipping chargeback'
```

Supporting side:

```text
amazon_sku_master for dimensions and weight where available
amazon_shipping_invoice if available
```

Mismatch categories:

- actual shipping fee greater than expected,
- volumetric weight exceeds gross weight,
- shipping chargeback due to weight/dimension discrepancy,
- missing SKU weight/dimension data.

### 12.8 Entity / GSTIN / seller mapping reconciliation

Question answered:

```text
Are Amazon India orders correctly classified as B2B/B2C/international and GST type?
```

Evidence:

- `metadata`,
- `destination_gst_id`,
- `source_gst_id`,
- `source_state`,
- `destination_state`,
- GST rate/amount fields.

Caveats:

- `metadata` is the cleaner primary segment field.
- `destination_gst_id` presence is a B2B supporting signal.
- Effective GST rate must use excluding-tax denominator.

### 12.9 Settlement to bank reconciliation note

Question answered:

```text
Did Amazon settlement actually reach the seller bank account?
```

Amazon source side:

```text
amazon_settlement settlement_id, settlement_date, total
```

Actual bank side:

```text
bank statement / UTR / bank reference from banking KB
```

Caveat:

```text
This Amazon source does not fully define bank statement tables or UTR matching. Retrieve banking and marketplace_to_bank reconciliation KB to complete this analysis.
```

### 12.10 Reconciliation grain and fallback keys

Standard fallback keys:

- `order_id`,
- `item_id`,
- `sku_id` / `sku`,
- `settlement_id`,
- `settlement_date`,
- `marketplace`,
- `group_level_id`,
- `currency_type`.

Grain rules:

- order-level metrics: aggregate disbursement first,
- SKU-level expected fee: aggregate actual fee to SKU,
- settlement-cycle metrics: group by `settlement_id`,
- cash-flow metrics: include all settlement types,
- revenue metrics: isolate Order/Refund or forward/reverse rows.

---

## 13. Table-specific curated knowledge

### 13.1 `zs_observe.amazon_oms`

#### Role

`amazon_oms` is the master order record for Amazon transactions. It captures forward sales, returns, cancellations, replacements, e-invoice cancellations, pricing, tax, geography, fulfilment, product, and customer-order context. It is the source of truth for order-level revenue, GST compliance, B2B/B2C segmentation, fulfilment segmentation, and return/cancellation analytics.

#### Grain

One row represents an Amazon order transaction line / item-level order record.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.amazon_oms` |
| Engine | Athena v3 / Trino SQL |
| Total columns | 91+ |
| Source sheet | `amazon b2b sales` |
| Scope | Amazon India B2B, B2C, and international orders |
| Main join key | `order_id` |
| Product key | `sku_id`, `asin`, `item_id` |
| Recommended date | `created_date` |
| Scope keys | `group_id`, `group_level_id` |

#### Primary analytical roles

- gross sales,
- net revenue after returns,
- AOV,
- return rate,
- cancellation rate,
- GST analysis,
- B2B/B2C/international segmentation,
- fulfilment model analysis,
- delivery zone and geography analysis,
- SKU and ASIN performance.

#### Mandatory filters

```sql
WHERE is_active = true
```

Optional safety filters:

```sql
AND zen_status = true
AND is_duplicated = false
```

Revenue queries must add:

```sql
AND transaction_type = 'forward'
```

#### Important columns

Identity and keys:

- `order_id`: Amazon order ID; primary join key.
- `item_id`: item-level ID within an order.
- `sku_id`: seller SKU.
- `asin`: Amazon ASIN.
- `invoice_number`: GST invoice number.
- `group_id`: usually 9 for Amazon.
- `group_level_id`: seller account scope key.

Product and SKU:

- `description`,
- `brand`,
- `sku_id`,
- `asin`,
- `quantity`,
- `mrp`.

Financial amounts:

- `charged_amount`: gross revenue including tax.
- `charged_amount_excluding_tax`: revenue before GST.
- `total_tax`: total GST collected.
- `item_amount_excluding_tax`: base item amount before tax.
- `shipping_amount`: shipping recovered from customer.
- `item_promo_discount`: item discount.
- `shipping_promo_discount`: shipping discount.
- `principal_amount`: principal portion.
- `gross_commission`: pre-computed gross commission estimate.
- `settled_amount`: amount settled for order where populated.
- `total_tcs_amount`: TCS deduction.
- `total_tds`: TDS deduction.

Zen vendor payout estimates:

- `zen_vendor_payout_refferal_fee`,
- `zen_vendor_payout_shipping_fee`,
- `zen_vendor_payout_closing_fee`,
- `zen_vendor_payout_pick_and_pack_fee`,
- `zen_vendor_payout_technology_fee`,
- `zen_vendor_payout_easyship_charge`,
- `zen_vendor_payout_commission_fee`.

These are estimates, not actual fees. Use `amazon_disbursment` for exact actual disbursement fee analysis.

Tax and GST:

- `tax_igst_rate`, `tax_igst_amount`,
- `tax_cgst_rate`, `tax_cgst_amount`,
- `tax_sgst_rate`, `tax_sgst_amount`,
- `tax_ugst_rate`, `tax_ugst_amount`,
- `source_gst_id`,
- `destination_gst_id`,
- `source_state`,
- `destination_state`.

Lifecycle and status:

- `transaction_type`: forward, reverse, cancel, replacement, einvoicecancel, null.
- `metadata`: B2B, B2C, or null for international.
- `fulfilment_channel`: AFN or MFN.
- `fulfilment_type`: FBA, Easyship, Other.
- `zone`, `zone_new`: delivery zone.

Dates:

- `created_date`: primary date dimension.
- `order_date`: order placement timestamp.
- `invoice_date`: invoice timestamp.
- `order_shipped_date`: safe date field.
- `shipment_date`: shipment timestamp.
- `settlement_date`: settlement date where populated.

#### Value semantics

`transaction_type` must be handled explicitly. `forward` is sale revenue; `reverse` is return; `cancel` is cancellation; `replacement` is customer-service/logistics event; `einvoicecancel` is compliance event.

`metadata` is the primary market segment signal:

| metadata | Segment |
|---|---|
| `B2C` | India consumer order |
| `B2B` | India business buyer |
| NULL | International order |

#### Relationships

- Joins to `amazon_settlement` by `order_id`.
- Joins to `amazon_disbursment` by `order_id`.
- Joins to `amazon_fee_preview` by `sku_id = sku`.
- Joins to `amazon_returns` by `order_id` when international returns are active.
- Joins to `amazon_sku_master` by `sku_id`.
- Joins to `amazon_shipping_invoice` by `order_id` where available.

#### Caveats

- Always filter `is_active = true` because active rate is very low due to known duplication.
- Do not ignore `cancel`; it can be very common by volume.
- Do not mix transaction types in revenue metrics.
- `zen_vendor_payout_*` values are estimates, not actual disbursement fees.
- Use `charged_amount_excluding_tax` as GST denominator.
- Treat replacement and e-invoice cancellation as non-revenue events.

#### Common query use cases

- gross sales by month,
- B2B vs B2C split,
- return rate by SKU,
- state-wise revenue,
- GST type split,
- fulfilment model revenue,
- cancellation rate,
- discount depth.

---

### 13.2 `zs_observe.amazon_settlement`

#### Role

`amazon_settlement` is Amazon's financial ledger. It records every debit and credit in a settlement period. Where `amazon_oms` explains what was sold, `amazon_settlement` explains what Amazon actually paid or deducted. It is the ground truth for cash flow, seller realization, settlement waterfall, fee deduction analysis, reimbursements, and service-fee analysis.

#### Grain

One row represents one settlement transaction line.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.amazon_settlement` |
| Engine | Athena v3 / Trino SQL |
| Columns | 136+ |
| Scope | Amazon India active; US/EU present in schema with varying active status |
| Main period key | `settlement_id` |
| Main order key | `order_id` |
| Recommended dates | `created_date`, `settlement_date` |
| Unsafe date | `date_time`, `date_time_str` |

#### Primary analytical roles

- seller realization,
- net settlement,
- settlement waterfall,
- fee deduction analysis,
- tax deduction analysis,
- advertising/service fee analysis,
- reimbursements and SAFE-T recovery,
- settlement-cycle cash-flow analysis.

#### Mandatory filters

```sql
WHERE is_active = true
```

Optional:

```sql
AND zen_status = true
```

Scope filter example:

```sql
AND group_level_id = 22
```

#### Important columns

Identity and keys:

- `settlement_id`: settlement period ID.
- `order_id`: Amazon order ID.
- `sku`, `sku_id`: seller SKU fields.
- `marketplace`: amazon.in, amazon.com, amazon.fr, amazon.es.
- `account_type`: Electronic/COD or Standard/Invoiced depending on market.
- `group_level_id`: integer scope key.
- `type`: settlement transaction type (Order, Refund, Service Fee, etc.). See §10.2 for the full enumeration.

Financial amounts:

- `product_sales`: revenue from product sold; positive for orders and negative for refunds.
- `selling_fees`: referral/commission fees.
- `fba_fees`: FBA fulfilment/storage fees.
- `shipping_credits`: shipping charged to buyer.
- `promotional_rebates`: promotional discounts.
- `gift_wrap_credits`: gift wrap credits.
- `other_transaction_fees`: closing, tech, or other transaction fees.
- `other`: miscellaneous adjustments.
- `tcs_cgst`, `tcs_sgst`, `tcs_igst`: TCS deductions.
- `tds`: TDS deduction.
- `marketplace_withheld_tax`: tax withheld for US/EU.
- `gross_commission`: pre-computed commission amount.
- `mp_fees`: marketplace fee aggregate.
- `settled_amount`: pre-computed settled amount.
- `total`: net amount credited/debited for the row.

Zen payout fields:

- `zen_vendor_payout_commission_fee`,
- `zen_vendor_payout_shipping_fee`,
- `zen_vendor_payout_platform_fee`,
- `zen_vendor_payout_payment_gateway_fee`,
- `zen_vendor_payout_sales_fee`.

Dates:

- `created_date`: timestamp; safe for date grouping.
- `settlement_date`: timestamp; use for settlement-period analysis.
- `date_time`: human-readable varchar; avoid for filtering.
- `date_time_str`: alternate string representation; avoid for filtering.

#### Value semantics

`type` values include Order, Refund, Fulfilment Fee Refund, Adjustment, Service Fee, FBA Inventory Fee, SAFE-T Reimbursement, Reimbursements, Transfer, Clawbacks, Others, and NULL.

For revenue reporting:

```text
Use type IN ('Order', 'Refund')
```

For cash-flow reporting:

```text
Use all types, because service fees, FBA inventory fees, reimbursements, adjustments, and clawbacks affect payout.
```

#### Relationships

- Joins to `amazon_oms` by `order_id`.
- Joins to `amazon_disbursment` by `order_id` and `settlement_id`.
- Relates to `amazon_recon_report` as aggregate waterfall evidence.

#### Caveats

- 64K+ active rows have `type = NULL`; do not drop them blindly.
- `group_level_id` is integer; use `= 22`, not `'22'`.
- `date_time` is a varchar and unsafe for filtering.
- Do not treat all `type` values as revenue.
- Do not compare India and international realization without separate context.
- Service Fee and FBA Inventory Fee are real payout deductions.

#### Common query use cases

- seller realization by settlement ID,
- monthly net settlement,
- fee deduction breakdown,
- advertising spend from Service Fee rows,
- TCS/TDS by month,
- SAFE-T and reimbursement recovery,
- settlement cash position.

---

### 13.3 `zs_observe.amazon_disbursment`

#### Role

`amazon_disbursment` is the granular line-level disbursement table. It decomposes every order into component rows: principal, tax, shipping, COD, fees, promotions, TCS, TDS, reimbursements, fee adjustments, SAFE-T, FBA inventory reimbursements, and operational transactions.

This is the most detailed Amazon financial table for unit economics and actual fee analysis.

#### Grain

One row represents one financial component of an order or transaction. Each order can generate many rows.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.amazon_disbursment` |
| Spelling | Use exact misspelling: `disbursment` |
| Engine | Athena v3 / Trino SQL |
| Columns | 54 |
| Scope | Amazon India only |
| Source sheet | `amazon disbursment` |
| Main keys | `order_id`, `settlement_id`, `sku_id`, `item_id` |
| Active rate | Approximately 99.87% active |

#### Primary analytical roles

- actual fee breakdown,
- per-order unit economics,
- fee recovery on returns,
- settlement-to-component reconciliation,
- SAFE-T and reimbursement recovery,
- actual vs expected fee reconciliation with fee preview,
- return economics.

#### Mandatory filters

```sql
WHERE is_active = true
```

Always specify `transaction_type` for fee computations.

#### Important columns

Identity and keys:

- `order_id`: primary order join key.
- `item_id`: item ID.
- `sku_id`: mapped seller SKU.
- `sku`: raw SKU from source.
- `settlement_id`: settlement period ID.
- `settlement_date`: settlement timestamp.
- `group_id`: usually 9.
- `group_level_id`: 22 or 26.
- `currency_type`: INR.

Fee classification:

- `transaction_type`: Order, Refund, Fulfillment Fee Refund, SAFE-T Reimbursement, Other, other-transaction.
- `mp_fee_type`: level-1 category.
- `charged_amount_type`: specific component.
- `item_fee_type`: additional source fee dimension.

Financial:

- `charged_amount`: component amount; positive is credit, negative is deduction.
- `order_level_total`: pre-aggregated order total; use cautiously.

Promotion:

- `promotion_id`.

Dates:

- `posted_date`: source posting date as varchar.
- `settlement_date`: settlement timestamp.

#### Value semantics

The two-level classification is central:

```text
mp_fee_type = broad category
charged_amount_type = exact component
```

Revenue components under `ItemPrice` include principal, product tax, shipping, shipping tax, COD, and COD tax.

Fee components under `ItemFees` include commission, shipping fee, closing fee, tech fee, pickup fee, shipping chargeback, and refund commission.

`refund commission` is positive and represents a fee credit, not a charge.

#### Relationships

- Joins to `amazon_oms` by `order_id`.
- Joins to `amazon_settlement` by `order_id` and `settlement_id`.
- Joins to `amazon_fee_preview` by `sku_id = sku`.
- Joins to `amazon_sku_master` by `sku_id`.

#### Caveats

- Do not sum `charged_amount` without transaction context.
- Do not sum all `ItemFees` without separating Order and Refund.
- Do not expect shipping fee to reverse on returns.
- Do not use `order_level_total` as net revenue without validation.
- Include `other-transaction` for full cost analysis.
- Aggregate to order or SKU before joining to avoid double counting.

#### Common query use cases

- fee breakdown by component,
- effective commission by SKU,
- fee recovery on returns,
- SAFE-T and reimbursement recovery,
- order-level unit economics,
- actual fee reconciliation.

---

### 13.4 `zs_observe.amazon_fee_preview`

#### Role

`amazon_fee_preview` is the SKU-level expected fee table. It contains pre-calculated fee estimates based on dimensions, weight, selling price, fulfilment, and category. It is used for expected-versus-actual fee reconciliation, cost planning, and packaging/weight optimization.

#### Grain

One row represents one SKU's expected fee estimate.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.amazon_fee_preview` |
| Engine | Athena v3 / Trino SQL |
| Columns | 54 |
| Scope | Amazon India only |
| Category context | Apparel |
| Fulfilment context | Fulfilled by Amazon |
| Main key | `sku` |

#### Primary analytical roles

- expected fee schedule,
- fee burden analysis,
- expected-vs-actual fee reconciliation,
- packaging optimization,
- volumetric-weight diagnostics,
- SKU-level cost planning.

#### Mandatory filters

```sql
WHERE is_active = true
  AND zen_status = true
  AND is_duplicated = false
```

`zen_status` and `is_duplicated` are boolean fields in this table.

#### Important columns

Product identity:

- `sku`: seller SKU; primary join key.
- `asin`: Amazon ASIN.
- `fnsku`: Fulfilment Network SKU.
- `brand`: brand.
- `description`, `product_name`: product text.
- `product_group`: category, e.g. Apparel.
- `amazon_store`: `IN`.
- `fulfilled_by`: Amazon.
- `hsn`: HSN code.

Calculated fee columns:

- `charged_amount`: product selling price / MRP used for fee calculation.
- `referral_fee`: referral fee amount in rupees.
- `referal_fee`: referral fee percentage; misspelled.
- `fixed_fee`: fixed closing fee.
- `pick_and_pack_fee`: FBA pick-pack fee.
- `shipping_amount`: expected weight-handling/shipping fee.
- `gross_commission`: total expected fee.

Amazon estimated fee columns as varchar:

- `estimated_referral_fee_per_unit`,
- `estimated_pick_pack_fee_per_unit`,
- `estimated_weight_handling_fee_per_unit`,
- `estimated_fixed_closing_fee`,
- `estimated_delivery_services_fee_per_unit`,
- `estimated_fee_total`.

Use `TRY_CAST` for estimated fee columns when needed.

Weight and dimensions:

- `gross_weight`: actual product weight in kg.
- `volumetric_weight`: calculated from dimensions.
- `final_weight`: billing weight, max of volumetric and gross weight.
- `longest_side`, `median_side`, `shortest_side`: package dimensions as string.
- `item_package_weight`: raw source weight, usually grams as string.

#### Value semantics

Expected gross commission formula:

```text
gross_commission = referral_fee + fixed_fee + pick_and_pack_fee + shipping_amount
```

Volumetric weight formula:

```text
volumetric_weight = (longest_side × median_side × shortest_side) / 5000
```

Final billing weight:

```text
final_weight = MAX(volumetric_weight, gross_weight)
```

#### Relationships

- Joins to `amazon_disbursment` by `sku = sku_id`.
- Joins to `amazon_oms` by `sku = sku_id`.
- Joins to `amazon_sku_master` by `sku = sku_id`.

#### Caveats

- `referral_fee` and `referal_fee` are different columns.
- Estimated fee columns are varchar and need safe casting.
- Preview is SKU-level; disbursement is order/component-level.
- Fee preview is India-only and should not be used for US/FR/ES fee estimates.
- Gross commission is expected fee, not actual charged fee.

#### Common query use cases

- SKU fee summary,
- volumetric versus gross weight gap,
- expected versus actual fee reconciliation,
- fee by weight tier,
- packaging optimization candidate identification.

---

### 13.5 `zs_observe.amazon_returns`

#### Role

`amazon_returns` tracks customer-initiated international returns with standardized reason codes, fulfilment center data, and customer comments. It supports return root-cause analysis, fraud detection, delivery damage attribution, and SAFE-T eligibility analysis for US/Canada returns.

#### Grain

One row represents one international return/refund record.

#### Key facts

| Attribute | Value |
|---|---|
| Schema | `zs_observe` |
| Full reference | `zs_observe.amazon_returns` |
| Engine | Athena v3 / Trino SQL |
| Columns | 38 |
| Source sheet | `amazon returns us` |
| Scope | Amazon International, US and Canada returns |
| Currency | USD / CAD |
| group_level_id | 123 |
| Current state | All records inactive due to `FILE_DELETED` |

#### Primary analytical roles

- international return reason analysis,
- customer comment analysis,
- fraud signal detection,
- warehouse/FC damage attribution,
- SAFE-T eligibility support,
- international return value analysis.

#### Mandatory filters

```sql
WHERE is_active = true
```

This currently returns zero rows until data is re-ingested.

#### Important columns

Identity:

- `order_id`: Amazon order ID.
- `sku_id`: seller SKU.
- `quantity`: quantity returned.
- `group_level_id`: 123.

Return reason:

- `return_reason`: standardized reason code.
- `customer_comments`: free-text buyer comment.

Fulfilment:

- `fulfilment_channel`: Amazon fulfilment center code, not AFN/MFN.

Dates:

- `created_date`: safe date field.
- `return_date_str`: string date; avoid for filtering.

Financial:

- `charged_amount`: refund amount including tax.
- `charged_amount_excluding_tax`: refund excluding tax.
- `shipping_amount`: return shipping cost.
- `currency_type`: USD or CAD.

#### Value semantics

`transaction_type = 'reverse'` and `internal_transaction_type = 'refunds'` represent international returns/refunds.

Return reason categories include:

- quality: `QUALITY_UNACCEPTABLE`, `DEFECTIVE`, `MISSING_PARTS`,
- listing: `NOT_AS_DESCRIBED`, `NOT_COMPATIBLE`,
- sizing: `APPAREL_TOO_LARGE`, `APPAREL_TOO_SMALL`, `POOR_FIT`,
- buyer choice/error: `UNWANTED_ITEM`, `ORDERED_WRONG_ITEM`, `FOUND_BETTER_PRICE`,
- delivery: `NEVER_ARRIVED`, `MISSED_ESTIMATED_DELIVERY`, `UNDELIVERABLE_UNKNOWN`, `UNDELIVERABLE_REFUSED`,
- Amazon/carrier damage: `DAMAGED_BY_CARRIER`, `DAMAGED_BY_FC`,
- fraud: `SWITCHEROO`, `UNAUTHORIZED_PURCHASE`,
- unknown: `NO_REASON_GIVEN`.

Historical reason distribution from source:

| Category | Approximate share | Action |
|---|---:|---|
| Buyer preference | ~27% | Listing optimization |
| Quality | ~24% | Quality control |
| Delivery issues | ~20% | Carrier review |
| Listing accuracy | ~16% | Improve listing content |
| Amazon-caused | ~7% | SAFE-T claims |
| Fraud / other | ~4% | Investigation |
| Sizing | ~1% | Size guide improvements |

#### Relationships

- Joins to `amazon_oms` by `order_id`.
- Joins to `amazon_settlement` by `order_id` where returns appear as `type = 'Refund'`.
- Joins to `amazon_sku_master` by `sku_id`.

#### Caveats

- All current records have `is_active = false` with reason `FILE_DELETED`.
- International returns are unavailable until re-ingested.
- India returns are not tracked here; use `amazon_oms.transaction_type = 'reverse'`.
- `fulfilment_channel` is FC code, not AFN/MFN channel.
- `return_date_str` is string and unsafe for date filtering.

#### Common query use cases

- return volume by reason,
- controllable versus non-controllable returns,
- warehouse damage rate,
- fraud signal detection,
- SAFE-T eligible return identification.

---

## 14. Mandatory query rules

### 14.1 Scope rules

- Resolve tenant, group, platform context, and platform account through Business Hierarchy.
- Apply account filters through Account Data Binding.
- Use `group_level_id = 22` only when Amazon India primary account is intended.
- Use `group_level_id = 26` for Amazon India secondary account where selected.
- Use `group_level_id = 123` for international context.
- Do not mix India and international marketplaces unless the user explicitly asks for cross-market analysis.

### 14.2 Active-row rules

- Always apply `is_active = true` where the table has `is_active`.
- `amazon_oms` must always use `is_active = true` because inactive duplicates dominate.
- `amazon_settlement` must always use `is_active = true`.
- `amazon_disbursment` must always use `is_active = true`.
- `amazon_fee_preview` should use `is_active = true`, `zen_status = true`, and `is_duplicated = false`.
- `amazon_returns` currently returns no active rows; do not infer zero international returns from this.

### 14.3 Date rules

- Use `amazon_oms.created_date` for OMS time-series analysis.
- Use `amazon_settlement.created_date` or `settlement_date` for settlement analysis.
- Use `amazon_fee_preview` only for SKU-level expected fee; not time-series unless dated context exists.
- Do not use `amazon_settlement.date_time` for filtering because it is varchar.
- Do not use `amazon_returns.return_date_str` for filtering because it is string.

### 14.4 Transaction/status rules

- Gross revenue should use `amazon_oms.transaction_type = 'forward'`.
- Net revenue may use forward + reverse.
- Cancellation analysis should include `transaction_type = 'cancel'`.
- Replacement and e-invoice cancellation should be tracked separately and excluded from revenue.
- Settlement revenue analysis should isolate `type IN ('Order', 'Refund')`.
- Full cash-flow analysis should include all settlement types.
- Do not drop `amazon_settlement.type IS NULL` rows without metric-specific reason.

### 14.5 Join and grain rules

- Aggregate `amazon_disbursment` before joining to order-level or settlement-level data.
- Aggregate actual fee rows to SKU before comparing to `amazon_fee_preview`.
- Use `settlement_id` for settlement-period reconciliation.
- Avoid many-to-many joins between OMS, settlement, and disbursement without pre-aggregation.
- Compare amounts at matching grain: order, order-item, settlement period, SKU, or component.

### 14.6 Numeric casting rules

- Main Amazon financial columns in OMS and settlement are native decimal; no casting required.
- `amazon_disbursment.charged_amount` is decimal and can be aggregated directly.
- Some `amazon_fee_preview` estimated fee columns are varchar and require `TRY_CAST`.
- Dimension fields like package sides may be varchar and require safe casting if used in calculations.

### 14.7 Tax and TCS/TDS rules

- Use `charged_amount_excluding_tax` as GST denominator.
- TCS is a cash-flow timing deduction and should not always be treated as permanent marketplace cost.
- TDS is not reversed on returns and should be treated carefully as cash-flow/tax-credit impact.
- Use source/destination GST logic for inter-state versus intra-state classification.

### 14.8 Settlement and realization rules

- Seller realization denominator should use `product_sales` on `type = 'Order'` rows.
- Net settlement should use `SUM(total)`.
- For cash-flow reporting, include service fees, inventory fees, reimbursements, SAFE-T, adjustments, and clawbacks.
- For revenue reporting, do not include service fees or inventory fees as revenue.

### 14.9 Platform-specific forbidden assumptions

- Do not assume `amazon_returns` is active; it is currently file-deleted/inactive.
- Do not assume `zen_vendor_payout_*` fields are actuals.
- Do not treat `fee_preview.gross_commission` as actual charged fee.
- Do not use `referal_fee` as rupee amount; it is percentage.
- Do not treat `refund commission` as a negative fee charge.
- Do not assume shipping fee is reversed on returns.
- Do not compare India and US/EU fee/realization benchmarks directly.

---

## 15. Data-quality and semantic caveats

### 15.1 Cross-table caveats

- Amazon OMS, settlement, disbursement, fee preview, and returns all have different grains.
- `amazon_disbursment` can create many rows per order and must be aggregated.
- Settlement rows may include non-revenue cash-flow impacts.
- Fee preview is expected estimate, not actual transaction data.

### 15.2 Scope caveats

- `group_level_id` represents different Amazon account contexts.
- Not every table has the same active scope or marketplace coverage.
- International returns are under group 123 but inactive.

### 15.3 Status caveats

- `amazon_oms.cancel` can be very common.
- `amazon_settlement.type = NULL` can carry financial values.
- `amazon_returns` inactive rows should not be interpreted as no returns.

### 15.4 Financial caveats

- Gross sales, principal, net settlement, and actual disbursement are different concepts.
- TCS/TDS affect cash flow but are reclaimable through filings.
- Shipping fee, tech fee, and pick-pack fee are often unrecovered on returns.
- Refund commission is a credit.

### 15.5 Tax caveats

- Effective GST rate must use tax-exclusive base.
- TCS and TDS have different legal and recovery mechanisms.
- TDS is not reversed on returns.

### 15.6 Logistics caveats

- Amazon shipping fees are not the same as external courier invoices.
- Packaging weight optimization uses fee preview and SKU/package dimensions.
- For external delivery or AWB/courier investigation, retrieve logistics KB if linked data exists.

### 15.7 Type-casting caveats

- `amazon_fee_preview` estimated fields and dimension strings may require safe casting.
- `amazon_settlement.date_time` and `amazon_returns.return_date_str` should not be used for date filters.

### 15.8 Legacy / duplicate / migration-residue fields

- `amazon_oms` has a known duplication issue; inactive duplicates dominate.
- `amazon_fee_preview` has boolean `zen_status` and `is_duplicated`, unlike some legacy string fields in other marketplaces.
- The disbursement table is misspelled and should not be automatically corrected by the SQL generator.

---

## 16. Supported question patterns

### 16.1 Sales and revenue questions

- What were Amazon gross sales last month?
- What was net revenue after returns?
- Which SKUs generated the most revenue?
- What was B2B versus B2C revenue?
- Which states generated the most Amazon revenue?
- What is AOV by fulfilment type?

### 16.2 Settlement and realization questions

- What is Amazon seller realization rate this month?
- What was net settlement by settlement ID?
- Which settlement period had low realization?
- What is cash position after the latest settlement?
- Which settlement types affected payout most?

### 16.3 Fee and deduction questions

- What is effective commission rate by SKU?
- Which fees drove margin leakage?
- Are we being overcharged versus fee preview?
- Which orders had shipping chargebacks?
- How much did Amazon charge for advertising/service fees?
- Which fee types are unrecovered on returns?

### 16.4 Return / cancellation questions

- Which SKUs have the highest return rate?
- What is the true cost of returns?
- Which returns are seller-controllable versus Amazon-caused?
- Which returns are SAFE-T eligible?
- What is the cancellation rate?

### 16.5 GST / TCS / TDS questions

- What is GST split by inter-state versus intra-state orders?
- How much TCS was deducted this month?
- How much TDS was deducted?
- Why does effective GST rate look below 18%?
- Which B2B orders had buyer GSTIN?

### 16.6 Promotions / reimbursement questions

- How much promotional rebate reduced payout?
- How much SAFE-T reimbursement did we recover?
- How much was recovered through fulfilment fee refunds?
- Which reimbursements were received this month?

### 16.7 Logistics / shipping adjustment questions

- Which SKUs are overpaying due to volumetric weight?
- Which SKUs have volumetric weight greater than gross weight by more than 50%?
- Which orders had shipping chargebacks?
- How much shipping fee was charged versus expected?

### 16.8 Reconciliation questions

- Which OMS orders are missing settlement?
- Does settlement total match disbursement components?
- Does fee preview match actual Amazon fees?
- Which refund orders did not receive expected fee recovery?
- Which SAFE-T eligible returns did not receive reimbursement?

### 16.9 Diagnostic questions

- Why did Amazon realization drop this month?
- Why did fees increase for apparel SKUs?
- Why are returns hurting margin?
- Why is settlement lower than expected?
- Why are shipping fees higher than expected?

### 16.10 Bank / payout matching questions

- Did Amazon settlement reach the bank?
- Which Amazon settlement IDs are missing bank credit?
- Why does Amazon settlement not match bank credit?

These require retrieval of banking and marketplace-to-bank reconciliation KB in addition to this Amazon marketplace KB.

---

## 17. SQL pattern appendix

### 17.1 Gross sales

```sql
SELECT
  SUM(charged_amount) AS gross_sales
FROM zs_observe.amazon_oms
WHERE is_active = true
  AND group_level_id = 22
  AND transaction_type = 'forward';
```

### 17.2 Net revenue

```sql
SELECT
  SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END) AS gross_revenue,
  SUM(CASE WHEN transaction_type = 'reverse' THEN charged_amount ELSE 0 END) AS refunds,
  SUM(CASE WHEN transaction_type IN ('forward', 'reverse') THEN charged_amount ELSE 0 END) AS net_revenue
FROM zs_observe.amazon_oms
WHERE is_active = true
  AND group_level_id = 22;
```

### 17.3 Seller realization

```sql
SELECT
  settlement_id,
  SUM(CASE WHEN type = 'Order' THEN product_sales ELSE 0 END) AS gross_sales,
  SUM(total) AS net_settled,
  ROUND(
    100.0 * SUM(total) /
    NULLIF(SUM(CASE WHEN type = 'Order' THEN product_sales ELSE 0 END), 0),
    1
  ) AS realization_pct
FROM zs_observe.amazon_settlement
WHERE is_active = true
  AND group_level_id = 22
GROUP BY settlement_id
ORDER BY realization_pct ASC;
```

### 17.4 Fee breakdown

```sql
SELECT
  mp_fee_type,
  charged_amount_type,
  COUNT(*) AS line_count,
  SUM(charged_amount) AS total_amount,
  AVG(charged_amount) AS avg_per_line
FROM zs_observe.amazon_disbursment
WHERE is_active = true
  AND transaction_type = 'Order'
GROUP BY 1, 2
ORDER BY ABS(SUM(charged_amount)) DESC;
```

### 17.5 Return rate

```sql
SELECT
  sku_id,
  COUNT(DISTINCT CASE WHEN transaction_type = 'forward' THEN order_id END) AS forward_orders,
  COUNT(DISTINCT CASE WHEN transaction_type = 'reverse' THEN order_id END) AS returns,
  ROUND(
    100.0 * COUNT(DISTINCT CASE WHEN transaction_type = 'reverse' THEN order_id END) /
    NULLIF(COUNT(DISTINCT CASE WHEN transaction_type = 'forward' THEN order_id END), 0),
    1
  ) AS return_rate_pct
FROM zs_observe.amazon_oms
WHERE is_active = true
  AND group_level_id = 22
GROUP BY sku_id
ORDER BY return_rate_pct DESC;
```

### 17.6 OMS to settlement reconciliation

```sql
SELECT
  o.order_id,
  o.created_date,
  o.charged_amount AS oms_revenue,
  s.product_sales AS settled_sales,
  s.total AS net_settled,
  s.settlement_id
FROM zs_observe.amazon_oms o
LEFT JOIN zs_observe.amazon_settlement s
  ON o.order_id = s.order_id
  AND s.is_active = true
  AND s.type = 'Order'
WHERE o.is_active = true
  AND o.group_level_id = 22
  AND o.transaction_type = 'forward';
```

### 17.7 Settlement to disbursement reconciliation

```sql
WITH disb AS (
  SELECT
    order_id,
    settlement_id,
    SUM(charged_amount) AS disbursement_total
  FROM zs_observe.amazon_disbursment
  WHERE is_active = true
  GROUP BY order_id, settlement_id
)
SELECT
  s.order_id,
  s.settlement_id,
  s.total AS settlement_total,
  d.disbursement_total,
  s.total - d.disbursement_total AS difference
FROM zs_observe.amazon_settlement s
LEFT JOIN disb d
  ON s.order_id = d.order_id
  AND s.settlement_id = d.settlement_id
WHERE s.is_active = true
  AND s.group_level_id = 22;
```

### 17.8 Fee preview expected vs actual reconciliation

```sql
WITH actual_fees AS (
  SELECT
    sku_id,
    SUM(CASE WHEN mp_fee_type = 'ItemFees' AND transaction_type = 'Order'
             THEN charged_amount ELSE 0 END) AS actual_fee,
    COUNT(DISTINCT order_id) AS orders
  FROM zs_observe.amazon_disbursment
  WHERE is_active = true
  GROUP BY sku_id
)
SELECT
  fp.sku,
  fp.gross_commission AS expected_fee,
  a.actual_fee,
  a.orders,
  fp.gross_commission + a.actual_fee AS variance
FROM zs_observe.amazon_fee_preview fp
JOIN actual_fees a
  ON fp.sku = a.sku_id
WHERE fp.is_active = true
  AND fp.zen_status = true
  AND fp.is_duplicated = false
ORDER BY ABS(fp.gross_commission + a.actual_fee) DESC;
```

### 17.9 Packaging / volumetric weight diagnostic

```sql
SELECT
  sku,
  description,
  gross_weight,
  volumetric_weight,
  final_weight,
  ROUND(
    100.0 * (volumetric_weight - gross_weight) /
    NULLIF(gross_weight, 0),
    1
  ) AS volumetric_excess_pct,
  shipping_amount AS expected_shipping_fee
FROM zs_observe.amazon_fee_preview
WHERE is_active = true
  AND zen_status = true
  AND is_duplicated = false
  AND volumetric_weight > gross_weight
ORDER BY volumetric_excess_pct DESC;
```

### 17.10 GST/TCS/TDS validation

```sql
SELECT
  CASE
    WHEN tax_igst_rate > 0 THEN 'Inter-State (IGST)'
    WHEN tax_cgst_rate > 0 THEN 'Intra-State (CGST+SGST)'
    WHEN tax_ugst_rate > 0 THEN 'Union Territory'
    ELSE 'No Tax / Other'
  END AS gst_type,
  COUNT(DISTINCT order_id) AS orders,
  SUM(total_tax) AS total_tax_collected,
  SUM(charged_amount_excluding_tax) AS taxable_base,
  ROUND(100.0 * SUM(total_tax) / NULLIF(SUM(charged_amount_excluding_tax), 0), 2) AS effective_tax_rate
FROM zs_observe.amazon_oms
WHERE is_active = true
  AND group_level_id = 22
  AND transaction_type = 'forward'
GROUP BY 1;
```

### 17.11 Reimbursements and SAFE-T recovery

```sql
SELECT
  type,
  COUNT(*) AS rows,
  SUM(total) AS total_recovered
FROM zs_observe.amazon_settlement
WHERE is_active = true
  AND group_level_id = 22
  AND type IN ('SAFE-T Reimbursement', 'Reimbursements', 'Adjustment', 'Fulfilment Fee Refund')
GROUP BY 1
ORDER BY total_recovered DESC;
```

### 17.12 Advertising spend from Service Fee

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  SUM(total) AS advertising_spend
FROM zs_observe.amazon_settlement
WHERE is_active = true
  AND group_level_id = 22
  AND type = 'Service Fee'
  AND description LIKE '%Advertising%'
GROUP BY 1
ORDER BY 1;
```

### 17.13 International return reason analysis when re-ingested

```sql
SELECT
  return_reason,
  COUNT(*) AS return_count,
  SUM(charged_amount) AS total_refund
FROM zs_observe.amazon_returns
WHERE is_active = true
GROUP BY return_reason
ORDER BY return_count DESC;
```

---

## 18. Extraction guidance

### 18.1 Business Hierarchy extraction

Extract:

- Platform: Amazon.
- Platform contexts: Amazon India, Amazon US, Amazon France, Amazon Spain.
- Platform accounts: account scopes represented by `group_level_id` 22, 26, and 123.
- Account Data Bindings: table-specific filters using `group_id`, `group_level_id`, marketplace, and currency where applicable.
- Business Scope Sets only for reusable named scopes, such as Amazon India all accounts.

Do not embed account filters directly into Table or Metric cards.

### 18.2 Data Understanding extraction

Extract Table Cards for:

- `amazon_oms`,
- `amazon_settlement`,
- `amazon_disbursment`,
- `amazon_fee_preview`,
- `amazon_returns`,
- referenced tables such as `amazon_sku_master`, `amazon_shipping_invoice`, and `amazon_recon_report` if schemas are validated.

Extract Column Cards for the curated fields listed in table-specific sections.

Extract Relationship Cards for:

- OMS ↔ Settlement,
- Settlement ↔ Disbursement,
- OMS ↔ Disbursement,
- Fee Preview ↔ Disbursement,
- Fee Preview ↔ OMS,
- Returns ↔ OMS,
- Returns ↔ Settlement,
- Fee Preview ↔ SKU Master.

Extract Value Profile Cards for:

- `amazon_oms.transaction_type`,
- `amazon_oms.metadata`,
- `amazon_oms.fulfilment_channel`,
- `amazon_oms.fulfilment_type`,
- `amazon_settlement.type`,
- `amazon_disbursment.transaction_type`,
- `amazon_disbursment.mp_fee_type`,
- `amazon_disbursment.charged_amount_type`,
- `amazon_returns.return_reason`.

### 18.3 Metric Understanding extraction

Extract Metric Cards and Metric Implementations for:

- gross sales,
- net revenue,
- taxable revenue,
- principal revenue,
- AOV,
- seller realization rate,
- net settlement amount,
- effective commission rate,
- effective fee rate,
- logistics cost rate,
- return rate,
- cancellation rate,
- return value rate,
- fee recovery rate,
- SAFE-T recovery rate,
- GST effective rate,
- TCS/TDS amount and rate,
- settlement cycle / payout lag,
- volumetric weight excess,
- expected-vs-actual fee variance.

Metric Implementation should be platform/table-specific, but account scope should remain runtime-resolved through Account Data Binding.

### 18.4 Process Understanding extraction

Extract Business Process / Workflow context for:

- Amazon order-to-settlement flow,
- settlement cycle and payout flow,
- return-to-refund flow,
- fee preview to actual fee validation flow,
- SAFE-T reimbursement flow,
- fulfilment fee refund / weight dispute flow,
- packaging/volumetric weight optimization flow,
- international return reason analysis flow.

### 18.5 Reconciliation Understanding extraction

Extract Reconciliation Profiles for:

- Amazon OMS to Settlement reconciliation,
- Amazon Settlement to Disbursement reconciliation,
- Amazon Fee Preview to Actual Fee reconciliation,
- Amazon Return to Refund/Fee Recovery reconciliation,
- Amazon SAFE-T Recovery reconciliation,
- Amazon Shipping Fee / Weight Chargeback reconciliation,
- Amazon Settlement to Bank reconciliation note, with unresolved banking dependency.

Each profile should specify expected side, actual side, primary keys, grain, mismatch categories, timing gap behavior, and caveats.

### 18.6 Execution Guidance extraction

Extract Query Patterns, Rules, Validation Tests, and Output Contracts from:

- mandatory filters,
- transaction-type rules,
- date safety rules,
- grain alignment rules,
- numeric-casting rules,
- TCS/TDS/GST rules,
- realization formula rules,
- fee-preview comparison rules,
- SQL appendix examples.

### 18.7 Optional module extraction

Amazon uses these optional marketplace modules:

| Module | Evidence in this document |
|---|---|
| `fee_preview_expected_vs_actual` | `amazon_fee_preview` versus `amazon_disbursment` |
| `line_level_disbursement_detail` | `amazon_disbursment` component rows |
| `safe_t_reimbursements` | SAFE-T settlement and disbursement records |
| `fee_recovery_on_returns` | return economics and disbursement refund logic |
| `packaging_weight_optimization` | volumetric weight, final weight, shipping amount |
| `international_returns_inactive_note` | `amazon_returns` inactive state |
| `marketplace_to_bank_reconciliation_note` | settlement-to-bank extension dependency |

---

## 19. Final authoring checklist for Amazon

This document preserves the required gold-standard marketplace structure:

```text
Business context before table details.
All Amazon table families included.
Financial waterfall explained.
Fees, taxes, promotions, reimbursements, and returns preserved.
Fulfilment and logistics context preserved.
Status and value semantics curated.
Metrics business-defined before SQL.
Reconciliation playbook specifies expected side, actual side, grain, keys, and caveats.
Mandatory query rules explicit.
Data-quality caveats preserved.
SQL examples included only as supporting evidence.
No card YAML authored manually.
No canonical JSON authored manually.
No graph edges authored manually.
```

---

## 20. Final principle

```text
Amazon is the reference marketplace frame because it contains the broadest marketplace structure:
OMS, settlement, disbursement, fee preview, returns, fee taxonomy, GST/TCS/TDS, SAFE-T, packaging/weight optimization, and reconciliation logic.

The ingestion pipeline should process Amazon using the same generic marketplace frame used for Flipkart, Myntra, Nykaa, and future marketplaces.

Amazon-specific knowledge stays in content, not code.
```

