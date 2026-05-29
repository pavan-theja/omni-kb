---
title: Logistics & Shipping Domain Overview
version: 2.1
doc_type: logistics_domain_overview
domain: logistics
platform_types:
  - marketplace
  - d2c_channel
  - courier_aggregator
  - courier
  - marketplace_fulfilment
  - seller_fulfilment
  - reverse_logistics
  - banking_bridge
fulfilment_ownership_models:
  - platform_fulfilled
  - marketplace_assisted
  - seller_fulfilled
  - aggregator_routed
  - direct_courier
  - reverse_only
  - indirect_only
  - settlement_only
  - low_confidence_native
business_processes:
  - order_to_shipment_flow
  - shipment_tracking
  - delivery_and_rto_flow
  - reverse_logistics
  - freight_billing
  - cod_collection_and_remittance
  - prepaid_or_pos_logistics_settlement
  - logistics_batch_to_bank_reconciliation
money_flow_paths:
  - order_to_shipment
  - shipment_to_freight_invoice
  - cod_delivery_to_courier_remittance
  - courier_remittance_to_bank
  - marketplace_fulfilment_to_settlement
  - reverse_logistics_to_adjustment
status: draft
owner: finance_data_team
source_documents:
  - Logistics KB Doc.docx
related_docs:
  - shiprocket_logistics.md
  - delhivery_logistics.md
  - dtdc_logistics.md
  - xpressbees_logistics.md
  - ekart_logistics.md
  - shadowfax_ecom_logistics.md
  - logistics_reconciliation_patterns.md
---

# Logistics & Shipping Domain Overview

> Scope note: This document is a reusable KB grounding document. It preserves logistics concepts, table semantics, join keys, amount meanings, and caveats. It does **not** define tenant/group ownership, customer-specific account scope, or durable marketplace routing. Tenant/group/account filters should be resolved through Business Hierarchy, Platform Account, Account Data Binding, Business Scope Set, and Runtime Scope.


## 1. How to use this document

Use this document as the shared logistics grounding layer for questions involving shipments, couriers, AWBs, fulfilment ownership, freight, COD, remittance, returns, RTO, and logistics-to-bank bridges.

This overview should be retrieved when a user asks questions like:

- Which shipping model applies to this order?
- Which table contains freight billing evidence?
- Which table contains COD remittance evidence?
- How do marketplace orders connect to courier settlements?
- What is the difference between freight charged, COD collected, COD remitted, and bank credited?

This document should not be used to decide which tenant, group, marketplace account, logistics account, or bank account is in scope. Those choices belong to runtime scope and Account Data Binding.

## 2. Logistics overview and business context

Logistics in ZenStatement is the bridge between commercial order records and physical/money movement evidence.

A reusable logistics chain looks like:

```text
marketplace / channel order
→ warehouse or fulfilment system
→ shipment/package
→ AWB / waybill / tracking ID
→ courier partner / aggregator
→ delivery, return, or RTO event
→ freight invoice or courier bill
→ COD collection/remittance, if COD
→ UTR / bank reference, if remittance reaches bank
```

Marketplace and channel systems explain what was sold and commercially settled. Logistics systems explain what happened to the shipment, who moved it, what freight was billed, whether COD was collected, and whether courier remittance evidence exists.

## 3. Applicability and scope model

This logistics KB is marketplace-aware and vendor-aware, but not customer-specific.

It can describe:

```text
vendor behavior
fulfilment model
shipment lifecycle
freight billing
COD remittance
bank bridge fields
table semantics
reconciliation logic
```

It should not hardcode:

```text
tenant identity
group filters
client-specific group_level_id values
seller account filters
merchant IDs
bank account IDs
marketplace-account ownership
```

Account-specific filters must be resolved through Account Data Binding. A logistics table may contain fields such as group/account identifiers, but this overview should treat them only as candidate account-binding fields.

## 4. Fulfilment ownership and shipping model

Use generic fulfilment ownership models instead of marketplace-specific labels as primitives.

| Generic model | Meaning | Examples / signals |
|---|---|---|
| `platform_fulfilled` | Marketplace/platform owns storage, fulfilment, dispatch, or fulfilment economics | Flipkart FBF, Amazon FBA/AFN, marketplace-managed fulfilment, Ekart-style fulfilment evidence |
| `marketplace_assisted` | Seller owns goods but marketplace provides pickup/shipping rails | Amazon EasyShip, Flipkart seller_easy_ship, platform-assisted pickup |
| `seller_fulfilled` | Seller dispatches using own courier, direct courier, or aggregator | Amazon MFN, Flipkart Self Ship, seller warehouse + direct courier |
| `aggregator_routed` | Channel/seller routes shipment through a courier aggregator | Shiprocket routes to Delhivery, DTDC, XpressBees, Ekart, Shadowfax, Ecom Express |
| `direct_courier` | Seller or platform works directly with a courier vendor | Delhivery direct, DTDC direct, XpressBees direct |
| `reverse_only` | Vendor appears mainly for reverse pickup/QC/returns/RTO | Shadowfax reverse QC style evidence |
| `indirect_only` | Vendor appears only through another source; no dedicated native table exists | Ecom Express via Shiprocket, Shadowfax via Shiprocket where no native table exists |
| `settlement_only` | Settlement/remittance evidence exists but operational invoice or shipment evidence is missing | DTDC-style settlement when invoice table is empty |
| `low_confidence_native` | Native table exists but core fields are sparse or unreliable | XpressBees-style sparse native settlement, until re-profiled |

Do not treat `FBF` as the primitive. Treat it as one marketplace-specific implementation of `platform_fulfilled`.

## 5. Operational shipment lifecycle

The generic operational flow is:

```text
order created
→ shipment created
→ AWB assigned
→ courier assigned
→ pickup scheduled
→ picked up
→ in transit
→ delivered / RTO delivered / return delivered / damaged / lost / cancelled
```

Important logistics events:

- shipment creation date,
- AWB assignment date,
- pickup scheduled date,
- pickup completed date,
- expected delivery date,
- delivery date,
- RTO initiated date,
- RTO delivered date,
- return delivered date,
- NDR/failed delivery attempt dates.

## 6. Money movement lifecycle

Logistics money movement has multiple layers. These should not be collapsed.

```text
Product/order value
≠ freight billed
≠ COD expected
≠ COD collected
≠ COD remitted
≠ bank credited
```

### Freight billing chain

```text
shipment / AWB
→ courier invoice or aggregator invoice
→ freight components
→ GST/tax
→ total freight billed
```

Freight components may include forward freight, RTO freight, DTO charge, COD collection fee, fuel surcharge, FOV/insurance, pickup charge, peak surcharge, reattempt charge, and taxes.

### COD remittance chain

```text
COD order delivered
→ courier collects COD
→ courier/aggregator creates remittance evidence
→ remittance batch / UTR / bank reference
→ bank credit expected
```

### Prepaid/POS settlement chain

For prepaid/digital/POS flows, payment is usually collected outside the courier COD chain. Some marketplace fulfilment systems may still expose POS/prepaid settlement rows. These should be handled separately from COD.

## 7. Business objects and identifiers

| Object | Meaning |
|---|---|
| Channel order | Order from marketplace, D2C, Shopify, ERP, or custom source |
| Marketplace order | Order from Amazon, Flipkart, Myntra, Nykaa, Ajio, HealthKart, etc. |
| Shipment | Physical dispatch instance for an order/order line/package |
| Package | Parcel that may contain one or more items |
| AWB / waybill / tracking ID | Carrier-level shipment identifier |
| Courier partner | Final carrier handling physical movement |
| Courier aggregator | Platform routing shipments to multiple courier partners |
| Fulfilment owner | Party responsible for storage, dispatch, and fulfilment workflow |
| Freight invoice | Billing record for shipment movement |
| COD expected | Amount expected to be collected from customer for COD order |
| COD collected | Amount collected by courier at delivery |
| COD remitted | Amount remitted by courier/aggregator |
| Payable amount | Net amount due after deductions/adjustments |
| Settlement batch | Batch of remittances paid in one transfer |
| UTR / bank reference | Bank bridge identifier for actual cash movement |
| RTO event | Failed delivery returned to origin |
| Return event | Customer-initiated reverse flow |
| Reverse pickup | Pickup of returned item from customer |
| NDR | Non-delivery report or failed delivery attempt |

## 8. Covered platform/vendor archetypes

| Archetype | KB role | Example vendor documents |
|---|---|---|
| Courier aggregator | Provides consolidated shipment, courier assignment, freight invoice, COD settlement evidence | Shiprocket |
| Direct courier | Provides direct shipment/freight/COD evidence where native tables exist | Delhivery, DTDC, XpressBees |
| Marketplace fulfilment | Provides platform-fulfilled shipment and settlement evidence | Ekart / marketplace fulfilment arms |
| Settlement-only courier | Provides COD/remittance evidence but no usable freight invoice | DTDC-style settlement-only cases |
| Low-confidence native source | Native data exists but sparse; fallback source may be better | XpressBees native settlement until profiled |
| Indirect-only courier | Vendor appears through aggregator or marketplace table only | Shadowfax/Ecom where no dedicated table exists |

## 9. Canonical join path

Use this generic join chain where evidence exists:

```text
order_id
→ shipment_id / package_id
→ AWB / waybill / tracking ID
→ courier invoice reference
→ courier settlement/remittance reference
→ settlement batch / UTR / bank reference
→ bank credit
```

Common field mappings from the source KB include:

| Generic object | Example field patterns |
|---|---|
| Order ID | `order_id`, marketplace order ID, Shopify order ID, composite channel order ID |
| Shipment ID | shipment ID, package ID, fulfilment ID, pickup ID |
| AWB / tracking | `awb_code`, `awb_number`, `other_id`, `forward_awb_number`, `waybill_num`, `airwaybill_number`, `shipment_id`, `tracking_id`, `shipping_id` |
| Invoice reference | `invoice_number`, courier invoice ID, bill number |
| Settlement reference | `settlement_id`, `remittance_number`, payout/remittance ID |
| Bank bridge | `utr_no`, `bank_reference_no`, `bank_ref_number`, NEFT/IMPS reference |

Do not require every vendor to support every step. Missing invoice, settlement, AWB, or bank bridge evidence should be explicit.

## 10. When to retrieve vendor docs

| User intent | Retrieve |
|---|---|
| shipment created, AWB assigned, courier partner, RTO/return, NDR | `shiprocket_logistics.md` and possibly vendor-specific docs |
| consolidated freight billing across many couriers | `shiprocket_logistics.md` |
| direct Delhivery freight or COD remittance | `delhivery_logistics.md` |
| DTDC COD remittance or DTDC invoice absence | `dtdc_logistics.md` |
| XpressBees COD, sparse native data, fallback via Shiprocket | `xpressbees_logistics.md` |
| Ekart / platform-fulfilled settlement, COD/POS settlement, AWB prefix patterns | `ekart_logistics.md` |
| Shadowfax/Ecom appearing as indirect or reverse-only courier evidence | `shadowfax_ecom_logistics.md` |
| cross-vendor matching or logistics-to-bank questions | `logistics_reconciliation_patterns.md` |

## 11. Global caveats

- Row counts and periods in source documents are profiling snapshots. Do not treat them as durable KB truth.
- Group IDs, tenant names, merchant IDs, and bank names in source examples are account-binding observations, not universal semantics.
- `charged_amount` has different meanings across tables. Interpret it only in table context.
- AWB fields have different names across vendors and may be sparse.
- Bank matching belongs to Banking KB, but logistics docs should expose UTR/bank reference fields.
- Batch-level bank credits should not be matched directly to AWB-level rows without aggregation.
- Empty invoice/report tables should be treated as schema-only until populated.
- Low-confidence native vendor data should prefer documented fallback sources.

## 12. Example questions

- Which fulfilment model applies to this shipment?
- Which table contains Shiprocket COD remittance evidence?
- How do I join Shiprocket shipment to freight invoice?
- Why does Delhivery `charged_amount` not equal freight?
- Which courier tables expose UTR or bank reference fields?
- Which XpressBees data should be treated as low confidence?
- Which logistics evidence should I use for COD delivered but not remitted?
- Which docs should I retrieve for courier batch-to-bank reconciliation?

## 13. Extraction guidance

Expected extracted card families:

```text
Domain
Business Process
Reconciliation Profile
Reconciliation Unit
Matching Logic
Mismatch Category
Rule
Validation Test
Metric
Formula Template
```

The domain overview should create generic logistics concepts and retrieval anchors. Vendor-specific table, column, and value cards should come from vendor docs.
