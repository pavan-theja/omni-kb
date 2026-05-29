---
title: Synthetic Tenant Flow Retrieval Test Queries
version: 1.0-test
doc_type: retrieval_test_plan
domain: kb_retrieval_testing
status: draft
owner: kb_test_team
related_docs:
  - 01_nimbus_retail_india_tenant_group_context.md
  - 02_nimbus_retail_india_business_flow_applicability.md
  - 03_prism_fashion_india_tenant_group_context.md
  - 04_prism_fashion_india_business_flow_applicability.md
---

# Synthetic Tenant Flow Retrieval Test Queries

## Purpose

Use these questions to test whether KB retrieval can correctly separate:

- tenant/group context,
- platform accounts,
- account data bindings,
- business scope sets,
- business flow bindings,
- logistics/vendor grounding docs,
- reconciliation pattern docs.

## Test Set 1 — Nimbus Retail India

### Query 1

```text
Which Nimbus Shopify COD orders were delivered but not remitted by Shiprocket last month?
```

Expected retrieval path:

```text
Tenant / Group Context:
- tenant.nimbus_retail
- group.nimbus_india_d2c
- platform_account.nimbus.shopify_in.store
- platform_account.nimbus.shiprocket.primary
- account_data_binding.nimbus.shopify_in.store.shopify_orders
- account_data_binding.nimbus.shiprocket.primary.shiprocket_oms
- account_data_binding.nimbus.shiprocket.primary.shiprocket_settlement

Business Flow Binding:
- Nimbus Shopify India Store → Nimbus Shiprocket Primary

Logistics docs:
- 00 logistics_domain_overview.md
- 01 shiprocket_logistics.md
- 07 logistics_reconciliation_patterns.md

Reconciliation profile candidates:
- order_to_shipment_reconciliation
- cod_delivery_to_courier_remittance
```

### Query 2

```text
Why does Nimbus Razorpay payout not match HDFC bank credit?
```

Expected retrieval path:

```text
Tenant / Group Context:
- platform_account.nimbus.razorpay.primary
- platform_account.nimbus.hdfc.current
- account_data_binding.nimbus.razorpay.primary.razorpay_payouts
- account_data_binding.nimbus.hdfc.current.bank_statement

Business Flow Binding:
- Nimbus Razorpay Primary → Nimbus HDFC Current Account

Related docs:
- payment gateway docs, if available
- banking docs, if available
- payment_gateway_to_bank reconciliation profile, if available
```

### Query 3

```text
Which Nimbus Amazon MFN orders shipped through Delhivery have no freight invoice?
```

Expected retrieval path:

```text
Tenant / Group Context:
- platform_account.nimbus.amazon_in.primary
- platform_account.nimbus.delhivery.direct
- account_data_binding.nimbus.amazon_in.primary.amazon_settlement
- account_data_binding.nimbus.delhivery.direct.delhivery_invoice

Business Flow Binding:
- Nimbus Amazon India Primary Seller → Nimbus Delhivery Direct

Marketplace docs:
- amazon_gold_std_md_frame.md or Amazon marketplace KB docs

Logistics docs:
- 02 delhivery_logistics.md
- 07 logistics_reconciliation_patterns.md

Completeness check:
- Confirm Amazon MFN/merchant-fulfilled activation condition before using this flow.
```

## Test Set 2 — Prism Fashion India

### Query 4

```text
Which Prism Flipkart FBF orders are missing Ekart settlement evidence?
```

Expected retrieval path:

```text
Tenant / Group Context:
- platform_account.prism.flipkart_in.seller
- platform_account.prism.ekart.marketplace_fulfilment
- account_data_binding.prism.flipkart_in.seller.flipkart_orders
- account_data_binding.prism.ekart.marketplace_fulfilment.ekart_settlement

Business Flow Binding:
- Prism Flipkart India Seller → Prism Ekart Marketplace Fulfilment

Marketplace docs:
- flipkart_gold_std_md_frame.md

Logistics docs:
- 04 ekart_logistics.md
- 07 logistics_reconciliation_patterns.md
```

### Query 5

```text
Can Prism use native XpressBees settlement for COD-to-bank reconciliation?
```

Expected retrieval path:

```text
Tenant / Group Context:
- platform_account.prism.xpressbees.native_cod
- platform_account.prism.icici.operating
- account_data_binding.prism.xpressbees.native_cod.xpressbees_settlement
- account_data_binding.prism.icici.operating.bank_statement

Business Flow Binding:
- Prism XpressBees Native COD → Prism ICICI Operating Account

Logistics docs:
- 05 xpressbees_logistics.md
- 07 logistics_reconciliation_patterns.md

Expected warning:
- Native XpressBees evidence is low-confidence unless completeness validation passes.
```

### Query 6

```text
Do Prism Myntra returns have direct Shadowfax settlement evidence?
```

Expected retrieval path:

```text
Tenant / Group Context:
- platform_account.prism.myntra_in.seller
- platform_account.prism.shiprocket.reverse_routing

Business Flow Binding:
- Prism Myntra Seller → Prism Shiprocket Reverse Routing

Logistics docs:
- 06 shadowfax_ecom_logistics.md
- 01 shiprocket_logistics.md

Expected answer behavior:
- Shadowfax/Ecom should be treated as indirect courier labels unless native tables are added.
- Do not create or retrieve direct Shadowfax settlement table cards from this example.
```

### Query 7

```text
Which Prism Nykaa courier flow should be used for mapper GST AWB records?
```

Expected retrieval path:

```text
Tenant / Group Context:
- platform_account.prism.nykaa_fashion.seller
- account_data_binding.prism.nykaa_fashion.seller.nykaa_mapper_gst

Business Flow Binding:
- Prism Nykaa Fashion Seller → unresolved logistics evidence

Marketplace docs:
- nykaa_gold_std_md_frame.md

Expected unresolved item:
- missing logistics destination account / unresolved courier account.
```
