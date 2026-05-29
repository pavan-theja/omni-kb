---
title: Prism Fashion India Business Flow Applicability
version: 1.0-test
doc_type: business_flow_applicability
domain: business_hierarchy
tenant: Prism Fashion
tenant_code: PRISM
group: Prism India Marketplaces
group_code: PRISM_IN_MKT
flow_domains:
  - marketplace_to_logistics
  - order_to_shipment
  - shipment_to_freight_invoice
  - logistics_cod_to_bank
  - reverse_logistics
expected_extracted_cards:
  - business_flow_binding
  - business_scope_set
  - graph_edge
  - review_item
status: draft
owner: kb_test_team
source_documents:
  - tenantgrp_bizflow_gold_std_raw_md.md
  - 03 dtdc_logistics.md
  - 04 ekart_logistics.md
  - 05 xpressbees_logistics.md
  - 06 shadowfax_ecom_logistics.md
  - 07 logistics_reconciliation_patterns.md
  - flipkart_gold_std_md_frame.md
  - myntra_gold_std_md_frame.md
  - nykaa_gold_std_md_frame.md
related_docs:
  - 03_prism_fashion_india_tenant_group_context.md
  - 00 logistics_domain_overview.md
  - 03 dtdc_logistics.md
  - 04 ekart_logistics.md
  - 05 xpressbees_logistics.md
  - 06 shadowfax_ecom_logistics.md
  - 07 logistics_reconciliation_patterns.md
---

# Prism Fashion India Business Flow Applicability

> Test-data note: This is an artificial Business Flow Applicability document for KB retrieval testing. It is designed to test platform-fulfilled marketplace logistics, settlement-only courier behavior, low-confidence native courier evidence, and indirect reverse logistics evidence.

## 1. How to use this document

Use this document when a Prism Fashion query crosses marketplace, logistics, courier settlement, reverse logistics, or bank evidence.

This document should help retrieval decide when to use:

- Flipkart + Ekart fulfilment evidence,
- Myntra + Shiprocket reverse-routing evidence for Shadowfax/Ecom labels,
- DTDC settlement-only COD to ICICI bank evidence,
- XpressBees low-confidence native COD evidence.

This document does not define generic Flipkart, Myntra, Nykaa, Ekart, DTDC, XpressBees, Shadowfax, Ecom, or ICICI behavior. It only describes Prism-specific account participation in reusable flows.

## 2. Tenant and group context

- Tenant: Prism Fashion
- Group: Prism India Marketplaces
- Primary business model: fashion and beauty marketplace selling
- Primary logistics patterns: platform-fulfilled marketplace logistics, direct courier COD, reverse logistics labels through aggregator evidence
- Primary bank destination for test COD flows: Prism ICICI Operating Account

## 3. Participating platform accounts

| Account | Platform | Role family | Source account identifier |
|---|---|---|---|
| Prism Flipkart India Seller | Flipkart | marketplace source | `fk_prism_in_seller` |
| Prism Myntra Seller | Myntra | marketplace source / reverse order source | `myntra_prism_in_seller` |
| Prism Nykaa Fashion Seller | Nykaa | marketplace source / logistics handoff source | `nykaa_prism_fashion_in` |
| Prism Ekart Marketplace Fulfilment | Ekart | marketplace fulfilment / logistics evidence source | `ekart_prism_fbf_01` |
| Prism DTDC Direct COD | DTDC | direct courier remittance source | `dtdc_prism_cod_01` |
| Prism XpressBees Native COD | XpressBees | low-confidence native courier remittance source | `xb_prism_native_01` |
| Prism Shiprocket Reverse Routing | Shiprocket | reverse logistics operational evidence source | `sr_prism_reverse_01` |
| Prism ICICI Operating Account | ICICI Bank | bank destination | `icici_prism_operating_01` |

## 4. Flow summary matrix

| Flow name | Money-flow path | Source account | Target / evidence account | Optional bank account | Status | Confidence |
|---|---|---|---|---|---|---|
| Flipkart FBF-like flow to Ekart | `marketplace_to_logistics`, `order_to_shipment`, `marketplace_fulfilment_to_settlement` | Prism Flipkart India Seller | Prism Ekart Marketplace Fulfilment | N/A | active | curated |
| Myntra reverse flow through Shiprocket labels | `marketplace_to_logistics`, `reverse_logistics` | Prism Myntra Seller | Prism Shiprocket Reverse Routing | N/A | draft | inferred |
| DTDC COD to ICICI | `logistics_cod_to_bank`, `courier_remittance_to_bank` | Prism DTDC Direct COD | Prism ICICI Operating Account | Prism ICICI Operating Account | active | curated |
| XpressBees native COD to ICICI | `logistics_cod_to_bank`, `courier_remittance_to_bank` | Prism XpressBees Native COD | Prism ICICI Operating Account | Prism ICICI Operating Account | draft | low_confidence |
| Nykaa mapper courier evidence | `marketplace_to_logistics`, `order_to_shipment` | Prism Nykaa Fashion Seller | unresolved logistics evidence | N/A | draft | inferred |

## 5. Marketplace / channel to logistics flows

### Flow: Prism Flipkart India Seller → Prism Ekart Marketplace Fulfilment

#### Business meaning

For Prism Flipkart platform-fulfilled or FBF-like orders, Ekart acts as marketplace fulfilment/logistics evidence. Flipkart is the marketplace order and settlement source. Ekart provides fulfilment, settlement, invoice, COD/POS, or logistics evidence where table coverage supports it.

#### Flow status

active

#### Money-flow path

- marketplace_to_logistics
- order_to_shipment
- marketplace_fulfilment_to_settlement
- shipment_to_freight_invoice, only where Ekart invoice evidence exists

#### Participating accounts and roles

- Prism Flipkart India Seller: `marketplace_source`, `order_source`
- Prism Ekart Marketplace Fulfilment: `logistics_source`, `operational_evidence`, `settlement_source`

#### Activation conditions

Use this flow when Flipkart order or settlement evidence indicates platform-fulfilled / FBF-like fulfilment, or when Ekart shipment/settlement evidence is the relevant logistics evidence source.

Do not use this flow for seller self-ship orders unless the data explicitly links the shipment to Ekart evidence.

#### Evidence path

Flipkart order / settlement → fulfilment signal → Ekart settlement or invoice → COD/POS/logistics settlement evidence.

#### Account Data Binding references

- `account_data_binding.prism.flipkart_in.seller.flipkart_orders`
- `account_data_binding.prism.flipkart_in.seller.flipkart_settlement`
- `account_data_binding.prism.ekart.marketplace_fulfilment.ekart_settlement`
- `account_data_binding.prism.ekart.marketplace_fulfilment.ekart_invoice`

#### Reconciliation variants applied

- `reconciliation_variant.ekart.ekart_native_cod_settlement`
- `reconciliation_variant.ekart.ekart_batch_level_cod_to_bank`

#### Related process and reconciliation models

- Order to shipment reconciliation
- Marketplace fulfilment to settlement reconciliation
- Shipment to freight invoice reconciliation, if invoice evidence exists

#### Confidence and unresolved assumptions

Curated for test retrieval. Exact Flipkart-to-Ekart join key should be resolved from marketplace and Ekart evidence cards.

#### Example questions

- Which Prism Flipkart FBF orders have no Ekart settlement evidence?
- Which Ekart settlement rows relate to Prism Flipkart platform-fulfilled orders?
- Which Flipkart platform-fulfilled shipments have missing logistics evidence?

### Flow: Prism Myntra Seller → Prism Shiprocket Reverse Routing

#### Business meaning

For selected Prism Myntra returns, reverse logistics evidence may appear through Shiprocket reverse-routing labels. Shadowfax or Ecom Express may appear as indirect courier labels inside Shiprocket data, but they do not have direct native table evidence in this test setup.

#### Flow status

draft

#### Money-flow path

- marketplace_to_logistics
- reverse_logistics
- order_to_shipment

#### Participating accounts and roles

- Prism Myntra Seller: `marketplace_source`, `order_source`
- Prism Shiprocket Reverse Routing: `logistics_source`, `operational_evidence`
- Shadowfax/Ecom Express labels: `indirect_courier_label`, not direct platform accounts with native tables

#### Activation conditions

Use this flow only for Myntra return or reverse pickup questions where Shiprocket reverse-routing evidence is present. Do not infer direct Shadowfax or Ecom settlement evidence unless native tables are later added.

#### Evidence path

Myntra return / reverse order → Shiprocket reverse routing entry → courier label such as Shadowfax or Ecom Express → reverse pickup / QC / return status evidence.

#### Account Data Binding references

- `account_data_binding.prism.myntra_in.seller.myntra_orders`
- `account_data_binding.prism.shiprocket.reverse_routing.shiprocket_oms`

#### Reconciliation variants applied

- `reconciliation_variant.shadowfax.shadowfax_indirect_freight`
- `reconciliation_variant.shadowfax.shadowfax_indirect_cod`
- `reconciliation_variant.shadowfax.ecom_express_indirect_freight`
- `reconciliation_variant.shiprocket.shiprocket_aggregator_freight_bridge`

#### Cross-domain relationships used

- `relationship.myntra_oms_to_shiprocket_oms_awb`
- `relationship.myntra_oms_to_shiprocket_oms_order`
- `relationship.myntra_seller_report_forward_to_shiprocket_invoice`

#### Related process and reconciliation models

- Reverse logistics process
- Order to shipment reconciliation
- Indirect courier evidence validation

#### Confidence and unresolved assumptions

Inferred. This flow is intentionally draft to test indirect-only courier retrieval and review-item generation.

#### Example questions

- Which Prism Myntra returns were routed to Shadowfax labels through Shiprocket?
- Does Prism have direct Shadowfax settlement evidence?
- Which reverse pickups have no native courier settlement table?

### Flow: Prism Nykaa Fashion Seller → unresolved logistics evidence

#### Business meaning

Nykaa Fashion may expose logistics enrichment through mapper or GST/logistics fields such as AWB, transporter name, warehouse status, or courier fields. In this artificial setup, the logistics destination account is intentionally unresolved to test partial-scope retrieval.

#### Flow status

draft

#### Money-flow path

- marketplace_to_logistics
- order_to_shipment

#### Participating accounts and roles

- Prism Nykaa Fashion Seller: `marketplace_source`, `order_source`
- Logistics evidence account: unresolved

#### Activation conditions

Use this flow only when the query asks about Nykaa shipment/courier evidence and mapper fields such as AWB or transporter name are present.

#### Evidence path

Nykaa order / mapper GST logistics fields → AWB / transporter / warehouse status → unresolved courier evidence.

#### Account Data Binding references

- `account_data_binding.prism.nykaa_fashion.seller.nykaa_mapper_gst`

#### Cross-domain relationships used

- `relationship.nykaa_mapper_gst_to_shiprocket_oms_awb`
- `relationship.nykaa_oms_to_shiprocket_oms_order`
- `relationship.nykaa_mapper_gst_to_shiprocket_invoice`

#### Related process and reconciliation models

- Order to shipment reconciliation
- Marketplace logistics handoff validation

#### Confidence and unresolved assumptions

Low confidence. Logistics destination account is unresolved by design.

#### Example questions

- Which Prism Nykaa orders have AWB but unresolved courier account?
- Which Nykaa courier names should be mapped to logistics vendors?

## 6. Logistics COD to bank flows

### Flow: Prism DTDC Direct COD → Prism ICICI Operating Account

#### Business meaning

DTDC COD remittance for Prism India Marketplaces should be matched against ICICI bank credits when DTDC settlement evidence contains remittance reference, amount, date, or bank bridge fields.

#### Flow status

active

#### Money-flow path

- logistics_cod_to_bank
- courier_remittance_to_bank

#### Participating accounts and roles

- Prism DTDC Direct COD: `remittance_source`, `courier_source`
- Prism ICICI Operating Account: `bank_destination`

#### Activation conditions

Use this flow for DTDC COD settlement evidence. Treat DTDC invoice evidence as partial or unavailable unless table coverage supports freight analysis.

#### Evidence path

DTDC settlement → remittance reference / amount / settlement date → ICICI bank statement credit.

#### Account Data Binding references

- `account_data_binding.prism.dtdc.direct_cod.dtdc_settlement`
- `account_data_binding.prism.icici.operating.bank_statement`

#### Reconciliation variants applied

- `reconciliation_variant.dtdc.dtdc_settlement_only_cod`
- `reconciliation_variant.dtdc.dtdc_freight_via_shiprocket`

#### Related process and reconciliation models

- Logistics COD to bank reconciliation
- Courier batch to bank reconciliation

#### Confidence and unresolved assumptions

Curated for test retrieval. Freight invoice visibility should remain separate from COD settlement visibility.

#### Example questions

- Which DTDC COD settlements did not reach ICICI?
- Which ICICI credits look like DTDC remittances?
- Is DTDC usable for freight invoice analysis or only COD settlement analysis?

### Flow: Prism XpressBees Native COD → Prism ICICI Operating Account

#### Business meaning

XpressBees native COD settlement for Prism India Marketplaces may be matched to ICICI bank credits, but native XpressBees data should be treated as low-confidence unless field completeness is validated.

#### Flow status

draft

#### Money-flow path

- logistics_cod_to_bank
- courier_remittance_to_bank

#### Participating accounts and roles

- Prism XpressBees Native COD: `remittance_source`, `courier_source`
- Prism ICICI Operating Account: `bank_destination`

#### Activation conditions

Use this flow only when XpressBees settlement rows have populated remittance amount, shipment status, service type, and transaction date fields. If native XpressBees fields are sparse, retrieval should prefer documented fallback evidence where available.

#### Evidence path

XpressBees settlement → remittance amount / transaction date / order or shipping reference → ICICI bank statement credit.

#### Account Data Binding references

- `account_data_binding.prism.xpressbees.native_cod.xpressbees_settlement`
- `account_data_binding.prism.icici.operating.bank_statement`

#### Reconciliation variants applied

- `reconciliation_variant.xpressbees.xpressbees_native_low_confidence_cod`
- `reconciliation_variant.xpressbees.xpressbees_freight_via_shiprocket`

#### Related process and reconciliation models

- Low-confidence vendor source validation
- Logistics COD to bank reconciliation

#### Confidence and unresolved assumptions

Low-confidence by design. Use this to test retrieval behavior when a native vendor table exists but field quality is incomplete.

#### Example questions

- Can Prism use native XpressBees settlement for COD reconciliation?
- Which XpressBees COD rows are complete enough for bank matching?
- Should retrieval fall back from XpressBees native settlement to aggregator evidence?

## 7. Marketplace settlement to bank flows

No active documented flow yet.

## 8. Payment gateway to bank flows

No active documented flow yet.

## 9. Refund, dispute, and chargeback flows

No active documented flow yet.

## 10. ERP / accounting to bank flows

No active documented flow yet.

## 11. Flow caveats and unresolved assumptions

- Do not treat Ekart as a generic courier for every Prism marketplace order. Ekart is connected to Flipkart platform-fulfilled evidence only when the selected flow applies.
- Do not create direct Shadowfax or Ecom physical table cards from this flow. They are indirect labels through Shiprocket evidence in this example.
- Do not use XpressBees native settlement as high-confidence evidence unless completeness tests pass.
- Do not infer Nykaa logistics destination without additional mapper/courier evidence.
- ICICI is the bank destination only for the selected DTDC and XpressBees flows.

## 12. Example questions this document should answer

- Which Business Flow Binding connects Prism Flipkart to Ekart?
- Which Prism flow should be used for DTDC COD to ICICI reconciliation?
- Is XpressBees native data high-confidence for Prism?
- Does Prism have direct Shadowfax settlement evidence?
- Which Prism Nykaa logistics flow is unresolved?

## 13. Extraction guidance

Expected extracted cards:

- Business Flow Binding
- Business Scope Set if the flow group is reusable
- Account Data Binding references
- Rule or caveat candidates
- Review items for unresolved assumptions

Expected graph edges:

- Group HAS_BUSINESS_FLOW_BINDING BusinessFlowBinding
- BusinessFlowBinding USES_PLATFORM_ACCOUNT PlatformAccount
- BusinessFlowBinding USES_SOURCE_ACCOUNT PlatformAccount
- BusinessFlowBinding USES_OPERATIONAL_EVIDENCE_ACCOUNT PlatformAccount
- BusinessFlowBinding USES_SETTLEMENT_SOURCE_ACCOUNT PlatformAccount
- BusinessFlowBinding USES_BANK_DESTINATION_ACCOUNT PlatformAccount
- BusinessFlowBinding USES_ACCOUNT_DATA_BINDING AccountDataBinding
- BusinessFlowBinding SUPPORTS_PROCESS BusinessProcess
- BusinessFlowBinding SUPPORTS_RECONCILIATION_PROFILE ReconciliationProfile
- BusinessFlowBinding USES_TABLE Table, where evidence tables are known

Do not extract generic vendor behavior from this document. Vendor behavior belongs to Ekart, DTDC, XpressBees, Shadowfax/Ecom, Flipkart, Myntra, Nykaa, and banking docs.
