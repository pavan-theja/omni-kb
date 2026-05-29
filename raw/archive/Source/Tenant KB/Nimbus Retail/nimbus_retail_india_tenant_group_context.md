---
title: Nimbus Retail India Business Hierarchy and Account Context
version: 1.0-test
doc_type: tenant_group_context
domain: business_hierarchy
tenant: Nimbus Retail
tenant_code: NIMBUS
groups:
  - Nimbus India D2C
platforms:
  - amazon
  - shopify
  - shiprocket
  - delhivery
  - razorpay
  - hdfc_bank
expected_extracted_cards:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
status: draft
owner: kb_test_team
source_documents:
  - tenantgrp_bizflow_gold_std_raw_md.md
  - 00 logistics_domain_overview.md
  - 01 shiprocket_logistics.md
  - 02 delhivery_logistics.md
  - amazon_gold_std_md_frame.md
related_docs:
  - 02_nimbus_retail_india_business_flow_applicability.md
---

# Nimbus Retail India Business Hierarchy and Account Context

> Test-data note: This is an artificial tenant/group document for KB retrieval testing. All account names, identifiers, and table filters are fictional. These values should be used only to test scope resolution, Account Data Binding retrieval, and Business Flow Binding retrieval.

## 1. How to use this document

Use this document when a query mentions Nimbus Retail, Nimbus India D2C, Nimbus Shopify, Nimbus Amazon India, Nimbus Shiprocket, Nimbus Delhivery, Nimbus Razorpay, or Nimbus HDFC.

This document resolves:

- tenant and group identity,
- connected platform accounts,
- table-specific account filters,
- reusable business scopes.

It does not define generic Amazon, Shopify, Shiprocket, Delhivery, Razorpay, or HDFC semantics. Those should come from marketplace, logistics, payment, and banking KB documents.

## 2. Tenant overview

Nimbus Retail is a fictional omnichannel seller using ZenStatement for D2C, marketplace, logistics, payment gateway, and bank reconciliation testing.

- Tenant code: `NIMBUS`
- Primary country: India
- Primary currency: INR
- Status: active for test retrieval

Expected extraction:

- `tenant.nimbus_retail`

## 3. Group landscape

Nimbus India D2C is the India operating group for D2C Shopify sales and Amazon India marketplace sales.

- Group code: `NIMBUS_IN_D2C`
- Country/region: India
- Currency: INR
- Status: active for test retrieval

Expected extraction:

- `group.nimbus_india_d2c`
- `tenant.nimbus_retail HAS_GROUP group.nimbus_india_d2c`

## 4. Platform inventory

Nimbus India D2C uses the following platform families:

Marketplace / channel platforms:

- Amazon India
- Shopify India

Logistics platforms:

- Shiprocket
- Delhivery

Payment gateway platforms:

- Razorpay

Banking platforms:

- HDFC Bank

Expected extraction:

- platform references for Amazon, Shopify, Shiprocket, Delhivery, Razorpay, and HDFC Bank.
- platform context references for India-specific operating contexts where supported.

## 5. Platform account catalog

| Platform | Platform context | Account name | Account type | Source account identifier | Group | Status |
|---|---|---|---|---|---|---|
| Amazon | Amazon India | Nimbus Amazon India Primary Seller | seller_account | `amz_nimbus_in_primary` | Nimbus India D2C | active |
| Shopify | Shopify India | Nimbus Shopify India Store | store_account | `shopify_nimbus_in_store` | Nimbus India D2C | active |
| Shiprocket | Shiprocket India | Nimbus Shiprocket Primary | logistics_account | `sr_nimbus_in_01` | Nimbus India D2C | active |
| Delhivery | Delhivery India | Nimbus Delhivery Direct | logistics_account | `dlh_nimbus_direct_01` | Nimbus India D2C | active |
| Razorpay | Razorpay India | Nimbus Razorpay Primary | merchant_account | `rzp_test_nimbus_in` | Nimbus India D2C | active |
| HDFC Bank | HDFC India | Nimbus HDFC Current Account | bank_account | `hdfc_nimbus_current_01` | Nimbus India D2C | active |

Expected extracted platform accounts:

- `platform_account.nimbus.amazon_in.primary`
- `platform_account.nimbus.shopify_in.store`
- `platform_account.nimbus.shiprocket.primary`
- `platform_account.nimbus.delhivery.direct`
- `platform_account.nimbus.razorpay.primary`
- `platform_account.nimbus.hdfc.current`

## 6. Account data binding observations

Account filters below are test-only Account Data Binding observations. They are table-specific and should not be generalized across vendors or domains.

### Amazon account bindings

In `zs_observe.amazon_settlement`:

- Nimbus Amazon India Primary Seller maps to `group_level_id = 4101`.
- `group_level_id` must be treated as an integer.

Suggested extraction:

- `account_data_binding.nimbus.amazon_in.primary.amazon_settlement`

### Shopify account bindings

In `zs_observe.shopify_orders`:

- Nimbus Shopify India Store maps to `store_id = 'shopify_nimbus_in_store'`.

Suggested extraction:

- `account_data_binding.nimbus.shopify_in.store.shopify_orders`

### Shiprocket account bindings

In `zs_observe.shiprocket_oms`:

- Nimbus Shiprocket Primary maps to `shiprocket_account_id = 'sr_nimbus_in_01'`.

In `zs_observe.shiprocket_invoice`:

- Nimbus Shiprocket Primary maps to `shiprocket_account_id = 'sr_nimbus_in_01'`.

In `zs_observe.shiprocket_settlement`:

- Nimbus Shiprocket Primary maps to `shiprocket_account_id = 'sr_nimbus_in_01'`.

Suggested extraction:

- `account_data_binding.nimbus.shiprocket.primary.shiprocket_oms`
- `account_data_binding.nimbus.shiprocket.primary.shiprocket_invoice`
- `account_data_binding.nimbus.shiprocket.primary.shiprocket_settlement`

### Delhivery account bindings

In `zs_observe.delhivery_invoice`:

- Nimbus Delhivery Direct maps to `client_code = 'NIMBUS_DLH_IN'`.

In `zs_observe.delhivery_settlement`:

- Nimbus Delhivery Direct maps to `client_code = 'NIMBUS_DLH_IN'`.

Suggested extraction:

- `account_data_binding.nimbus.delhivery.direct.delhivery_invoice`
- `account_data_binding.nimbus.delhivery.direct.delhivery_settlement`

### Razorpay account bindings

In `zs_observe.razorpay_payouts`:

- Nimbus Razorpay Primary maps to `merchant_id = 'rzp_test_nimbus_in'`.

Suggested extraction:

- `account_data_binding.nimbus.razorpay.primary.razorpay_payouts`

### HDFC account bindings

In `zs_observe.bank_statement`:

- Nimbus HDFC Current Account maps to `bank_account_id = 'hdfc_nimbus_current_01'`.

Suggested extraction:

- `account_data_binding.nimbus.hdfc.current.bank_statement`

## 7. Business scope sets

### Nimbus India D2C Logistics Scope

Includes:

- Nimbus Shopify India Store
- Nimbus Shiprocket Primary
- Nimbus Delhivery Direct

Use this scope for D2C shipment, freight, courier, and COD operational analysis.

Suggested extraction:

- `business_scope_set.nimbus_india_d2c.logistics_scope`

### Nimbus India Cash Realization Scope

Includes:

- Nimbus Razorpay Primary
- Nimbus Shiprocket Primary
- Nimbus HDFC Current Account

Use this scope for payout, COD remittance, and bank realization checks.

Suggested extraction:

- `business_scope_set.nimbus_india_d2c.cash_realization_scope`

### Nimbus India Amazon Reporting Scope

Includes:

- Nimbus Amazon India Primary Seller

Use this scope for Amazon seller realization and settlement reporting.

Suggested extraction:

- `business_scope_set.nimbus_india_d2c.amazon_reporting_scope`

## 8. Account and scope caveats

- `group_level_id = 4101` is only a fictional Amazon settlement binding. It is not a universal Nimbus India group filter.
- `shiprocket_account_id = 'sr_nimbus_in_01'` applies only to Shiprocket tables where that field exists.
- `client_code = 'NIMBUS_DLH_IN'` applies only to Delhivery tables where that field exists.
- HDFC account binding identifies a bank statement account, not a proof that all marketplace, payment, or logistics remittances should land in HDFC.
- Cross-platform routing must come from the Business Flow Applicability document, not this account catalog alone.

## 9. Example questions this document should answer

- Which accounts does Nimbus India D2C use?
- What account filter should be applied to `zs_observe.shiprocket_settlement` for Nimbus Shiprocket?
- Which bank account belongs to Nimbus India D2C?
- Which platform accounts belong to the Nimbus India D2C Logistics Scope?
- What does `group_level_id = 4101` mean in Amazon settlement data?

## 10. Extraction guidance

Expected extracted cards:

- Tenant
- Group
- Platform Account
- Account Data Binding
- Business Scope Set

Expected graph edges:

- Tenant HAS_GROUP Group
- Group HAS_PLATFORM_ACCOUNT PlatformAccount
- PlatformAccount USES_PLATFORM Platform
- PlatformAccount HAS_PLATFORM_CONTEXT PlatformContext
- PlatformAccount HAS_DATA_BINDING AccountDataBinding
- AccountDataBinding APPLIES_TO_TABLE Table
- BusinessScopeSet INCLUDES_PLATFORM_ACCOUNT PlatformAccount

Do not extract Business Flow Binding from this document. Flow participation is documented separately in `02_nimbus_retail_india_business_flow_applicability.md`.
