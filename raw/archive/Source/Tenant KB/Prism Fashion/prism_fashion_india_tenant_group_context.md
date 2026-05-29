---
title: Prism Fashion India Business Hierarchy and Account Context
version: 1.0-test
doc_type: tenant_group_context
domain: business_hierarchy
tenant: Prism Fashion
tenant_code: PRISM
groups:
  - Prism India Marketplaces
platforms:
  - flipkart
  - myntra
  - nykaa
  - ekart
  - dtdc
  - xpressbees
  - shiprocket
  - icici_bank
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
  - 03 dtdc_logistics.md
  - 04 ekart_logistics.md
  - 05 xpressbees_logistics.md
  - 06 shadowfax_ecom_logistics.md
  - flipkart_gold_std_md_frame.md
  - myntra_gold_std_md_frame.md
  - nykaa_gold_std_md_frame.md
related_docs:
  - 04_prism_fashion_india_business_flow_applicability.md
---

# Prism Fashion India Business Hierarchy and Account Context

> Test-data note: This is an artificial tenant/group document for KB retrieval testing. All account names, identifiers, and table filters are fictional. The purpose is to test platform-fulfilled flows, settlement-only courier flows, low-confidence courier evidence, indirect reverse courier evidence, and Account Data Binding resolution.

## 1. How to use this document

Use this document when a query mentions Prism Fashion, Prism India Marketplaces, Prism Flipkart, Prism Myntra, Prism Nykaa, Prism Ekart, Prism DTDC, Prism XpressBees, Prism Shiprocket Returns, or Prism ICICI.

This document resolves:

- tenant and group identity,
- connected marketplace and logistics platform accounts,
- table-specific account filters,
- reusable business scopes.

It does not define generic marketplace or logistics behavior.

## 2. Tenant overview

Prism Fashion is a fictional fashion and beauty seller using ZenStatement for marketplace settlement, logistics reconciliation, return operations, COD remittance, and bank realization testing.

- Tenant code: `PRISM`
- Primary country: India
- Primary currency: INR
- Status: active for test retrieval

Expected extraction:

- `tenant.prism_fashion`

## 3. Group landscape

Prism India Marketplaces is the India marketplace operations group.

- Group code: `PRISM_IN_MKT`
- Country/region: India
- Currency: INR
- Status: active for test retrieval

Expected extraction:

- `group.prism_india_marketplaces`
- `tenant.prism_fashion HAS_GROUP group.prism_india_marketplaces`

## 4. Platform inventory

Marketplace platforms:

- Flipkart India
- Myntra India
- Nykaa Fashion

Logistics platforms:

- Ekart
- DTDC
- XpressBees
- Shiprocket, used only as an aggregator/fallback or reverse-routing evidence source in selected test flows

Banking platforms:

- ICICI Bank

Expected extraction:

- platform references for Flipkart, Myntra, Nykaa, Ekart, DTDC, XpressBees, Shiprocket, and ICICI Bank.

## 5. Platform account catalog

| Platform | Platform context | Account name | Account type | Source account identifier | Group | Status |
|---|---|---|---|---|---|---|
| Flipkart | Flipkart India | Prism Flipkart India Seller | seller_account | `fk_prism_in_seller` | Prism India Marketplaces | active |
| Myntra | Myntra India | Prism Myntra Seller | seller_account | `myntra_prism_in_seller` | Prism India Marketplaces | active |
| Nykaa | Nykaa Fashion India | Prism Nykaa Fashion Seller | seller_account | `nykaa_prism_fashion_in` | Prism India Marketplaces | active |
| Ekart | Ekart India | Prism Ekart Marketplace Fulfilment | marketplace_fulfilment_account | `ekart_prism_fbf_01` | Prism India Marketplaces | active |
| DTDC | DTDC India | Prism DTDC Direct COD | logistics_account | `dtdc_prism_cod_01` | Prism India Marketplaces | active |
| XpressBees | XpressBees India | Prism XpressBees Native COD | logistics_account | `xb_prism_native_01` | Prism India Marketplaces | low_confidence |
| Shiprocket | Shiprocket India | Prism Shiprocket Reverse Routing | logistics_account | `sr_prism_reverse_01` | Prism India Marketplaces | active |
| ICICI Bank | ICICI India | Prism ICICI Operating Account | bank_account | `icici_prism_operating_01` | Prism India Marketplaces | active |

Expected extracted platform accounts:

- `platform_account.prism.flipkart_in.seller`
- `platform_account.prism.myntra_in.seller`
- `platform_account.prism.nykaa_fashion.seller`
- `platform_account.prism.ekart.marketplace_fulfilment`
- `platform_account.prism.dtdc.direct_cod`
- `platform_account.prism.xpressbees.native_cod`
- `platform_account.prism.shiprocket.reverse_routing`
- `platform_account.prism.icici.operating`

## 6. Account data binding observations

Account filters below are test-only Account Data Binding observations. They are table-specific and should not be generalized across vendors or domains.

### Flipkart account bindings

In `zs_observe.flipkart_settlement`:

- Prism Flipkart India Seller maps to `seller_id = 'fk_prism_in_seller'`.

In `zs_observe.flipkart_orders`:

- Prism Flipkart India Seller maps to `seller_id = 'fk_prism_in_seller'`.

Suggested extraction:

- `account_data_binding.prism.flipkart_in.seller.flipkart_settlement`
- `account_data_binding.prism.flipkart_in.seller.flipkart_orders`

### Myntra account bindings

In `zs_observe.myntra_orders`:

- Prism Myntra Seller maps to `seller_party_id = 'myntra_prism_in_seller'`.

In `zs_observe.myntra_settlement`:

- Prism Myntra Seller maps to `seller_party_id = 'myntra_prism_in_seller'`.

Suggested extraction:

- `account_data_binding.prism.myntra_in.seller.myntra_orders`
- `account_data_binding.prism.myntra_in.seller.myntra_settlement`

### Nykaa account bindings

In `zs_observe.nykaa_mapper_gst`:

- Prism Nykaa Fashion Seller maps to `brand_account_id = 'nykaa_prism_fashion_in'`.

Suggested extraction:

- `account_data_binding.prism.nykaa_fashion.seller.nykaa_mapper_gst`

### Ekart account bindings

In `zs_observe.ekart_settlement`:

- Prism Ekart Marketplace Fulfilment maps to `seller_code = 'ekart_prism_fbf_01'`.

In `zs_observe.ekart_invoice`:

- Prism Ekart Marketplace Fulfilment maps to `seller_code = 'ekart_prism_fbf_01'`.

Suggested extraction:

- `account_data_binding.prism.ekart.marketplace_fulfilment.ekart_settlement`
- `account_data_binding.prism.ekart.marketplace_fulfilment.ekart_invoice`

### DTDC account bindings

In `zs_observe.dtdc_settlement`:

- Prism DTDC Direct COD maps to `customer_code = 'DTDC_PRISM_COD'`.

In `zs_observe.dtdc_invoice`:

- Prism DTDC Direct COD maps to `customer_code = 'DTDC_PRISM_COD'`, but invoice coverage should be treated as partial or empty if the source table is unavailable.

Suggested extraction:

- `account_data_binding.prism.dtdc.direct_cod.dtdc_settlement`
- `account_data_binding.prism.dtdc.direct_cod.dtdc_invoice`

### XpressBees account bindings

In `zs_observe.xpressbees_settlement`:

- Prism XpressBees Native COD maps to `company = 'PRISM_XB_NATIVE'` when populated.
- This binding is low-confidence because core fields may be sparse or null depending on ingestion quality.

Suggested extraction:

- `account_data_binding.prism.xpressbees.native_cod.xpressbees_settlement`

### Shiprocket reverse-routing account bindings

In `zs_observe.shiprocket_oms`:

- Prism Shiprocket Reverse Routing maps to `shiprocket_account_id = 'sr_prism_reverse_01'`.

Suggested extraction:

- `account_data_binding.prism.shiprocket.reverse_routing.shiprocket_oms`

### ICICI account bindings

In `zs_observe.bank_statement`:

- Prism ICICI Operating Account maps to `bank_account_id = 'icici_prism_operating_01'`.

Suggested extraction:

- `account_data_binding.prism.icici.operating.bank_statement`

## 7. Business scope sets

### Prism India Marketplace Fulfilment Scope

Includes:

- Prism Flipkart India Seller
- Prism Ekart Marketplace Fulfilment

Use this scope for Flipkart platform-fulfilled / FBF-like fulfilment evidence tests.

Suggested extraction:

- `business_scope_set.prism_india_marketplaces.flipkart_ekart_fulfilment_scope`

### Prism India Direct Courier COD Scope

Includes:

- Prism DTDC Direct COD
- Prism XpressBees Native COD
- Prism ICICI Operating Account

Use this scope for direct courier COD-to-bank tests.

Suggested extraction:

- `business_scope_set.prism_india_marketplaces.direct_courier_cod_scope`

### Prism India Reverse Logistics Scope

Includes:

- Prism Myntra Seller
- Prism Shiprocket Reverse Routing

Use this scope for reverse logistics, Shadowfax/Ecom indirect evidence, and return pickup tests.

Suggested extraction:

- `business_scope_set.prism_india_marketplaces.reverse_logistics_scope`

## 8. Account and scope caveats

- `seller_id = 'fk_prism_in_seller'` is a fictional Flipkart account binding and should not be reused for Myntra, Nykaa, or logistics tables.
- `seller_code = 'ekart_prism_fbf_01'` is a fictional Ekart binding and does not prove Flipkart ownership unless a Business Flow Binding connects Flipkart and Ekart.
- XpressBees native COD binding is intentionally low-confidence to test retrieval behavior around sparse native data.
- Shadowfax and Ecom Express should not get direct physical table bindings in this example; they are treated as indirect labels through Shiprocket evidence.
- ICICI account binding identifies the bank statement account, not proof that all courier or marketplace remittances land in ICICI.

## 9. Example questions this document should answer

- Which platform accounts does Prism India Marketplaces use?
- Which account binding applies to `zs_observe.ekart_settlement`?
- Which account binding applies to `zs_observe.dtdc_settlement`?
- Which vendor account is low-confidence for Prism?
- Which scope contains Prism DTDC, XpressBees, and ICICI?

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

Do not extract Business Flow Binding from this document. Flow participation is documented separately in `04_prism_fashion_india_business_flow_applicability.md`.
