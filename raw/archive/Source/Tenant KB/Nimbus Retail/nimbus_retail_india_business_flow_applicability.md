---
title: Nimbus Retail India Business Flow Applicability
version: 1.0-test
doc_type: business_flow_applicability
domain: business_hierarchy
tenant: Nimbus Retail
tenant_code: NIMBUS
group: Nimbus India D2C
group_code: NIMBUS_IN_D2C
flow_domains:
  - marketplace_to_logistics
  - order_to_shipment
  - shipment_to_freight_invoice
  - logistics_cod_to_bank
  - payment_gateway_to_bank
  - marketplace_to_bank
expected_extracted_cards:
  - business_flow_binding
  - business_scope_set
  - graph_edge
  - review_item
status: draft
owner: kb_test_team
source_documents:
  - tenantgrp_bizflow_gold_std_raw_md.md
  - 01 shiprocket_logistics.md
  - 02 delhivery_logistics.md
  - 07 logistics_reconciliation_patterns.md
related_docs:
  - 01_nimbus_retail_india_tenant_group_context.md
  - 00 logistics_domain_overview.md
  - 01 shiprocket_logistics.md
  - 02 delhivery_logistics.md
  - amazon_gold_std_md_frame.md
---

# Nimbus Retail India Business Flow Applicability

> Test-data note: This is an artificial Business Flow Applicability document for KB retrieval testing. It is meant to test Business Flow Binding retrieval, graph traversal, and completeness checks. All accounts and identifiers are fictional.

## 1. How to use this document

Use this document when a Nimbus Retail query crosses platform families, such as:

- Shopify order to Shiprocket shipment,
- Shiprocket COD remittance to HDFC bank credit,
- Razorpay payout to HDFC bank credit,
- Amazon MFN order to Delhivery direct courier evidence.

This document does not define generic Shiprocket, Delhivery, Razorpay, HDFC, Shopify, or Amazon semantics. It only describes which Nimbus accounts participate together in reusable flows.

## 2. Tenant and group context

- Tenant: Nimbus Retail
- Group: Nimbus India D2C
- Primary business model: D2C Shopify and Amazon India marketplace sales
- Primary logistics modes: Shiprocket aggregator-routed logistics and Delhivery direct courier
- Primary bank destination for test flows: Nimbus HDFC Current Account

## 3. Participating platform accounts

| Account | Platform | Role family | Source account identifier |
|---|---|---|---|
| Nimbus Shopify India Store | Shopify | order / channel source | `shopify_nimbus_in_store` |
| Nimbus Amazon India Primary Seller | Amazon | marketplace source / settlement source | `amz_nimbus_in_primary` |
| Nimbus Shiprocket Primary | Shiprocket | logistics source / courier aggregator / COD remittance source | `sr_nimbus_in_01` |
| Nimbus Delhivery Direct | Delhivery | direct courier source | `dlh_nimbus_direct_01` |
| Nimbus Razorpay Primary | Razorpay | payment gateway payout source | `rzp_test_nimbus_in` |
| Nimbus HDFC Current Account | HDFC Bank | bank destination | `hdfc_nimbus_current_01` |

## 4. Flow summary matrix

| Flow name | Money-flow path | Source account | Target / evidence account | Optional bank account | Status | Confidence |
|---|---|---|---|---|---|---|
| Shopify to Shiprocket | `marketplace_to_logistics`, `order_to_shipment` | Nimbus Shopify India Store | Nimbus Shiprocket Primary | N/A | active | curated |
| Shiprocket COD to HDFC | `logistics_cod_to_bank`, `courier_remittance_to_bank` | Nimbus Shiprocket Primary | Nimbus HDFC Current Account | Nimbus HDFC Current Account | active | curated |
| Razorpay to HDFC | `payment_gateway_to_bank` | Nimbus Razorpay Primary | Nimbus HDFC Current Account | Nimbus HDFC Current Account | active | curated |
| Amazon MFN to Delhivery | `marketplace_to_logistics`, `order_to_shipment`, `shipment_to_freight_invoice` | Nimbus Amazon India Primary Seller | Nimbus Delhivery Direct | N/A | draft | inferred |
| Amazon settlement to HDFC | `marketplace_to_bank` | Nimbus Amazon India Primary Seller | Nimbus HDFC Current Account | Nimbus HDFC Current Account | draft | low_confidence |

## 5. Marketplace / channel to logistics flows

### Flow: Nimbus Shopify India Store → Nimbus Shiprocket Primary

#### Business meaning

For Shopify D2C orders, Nimbus India D2C uses Shiprocket as the courier aggregator. Shopify is the order source. Shiprocket provides shipment, AWB, courier partner, freight invoice, and COD settlement evidence.

#### Flow status

active

#### Money-flow path

- marketplace_to_logistics
- order_to_shipment
- shipment_to_freight_invoice
- cod_delivery_to_courier_remittance

#### Participating accounts and roles

- Nimbus Shopify India Store: `order_source`
- Nimbus Shiprocket Primary: `logistics_source`, `operational_evidence`, `remittance_source` when COD settlement is involved

#### Activation conditions

Use this flow when:

- order source is Nimbus Shopify India Store,
- shipment evidence is expected in Shiprocket,
- AWB or Shiprocket order reference is available,
- for COD checks, Shiprocket settlement evidence is required.

#### Evidence path

Shopify order → Shiprocket shipment → AWB → courier partner → Shiprocket invoice → Shiprocket settlement.

#### Account Data Binding references

- `account_data_binding.nimbus.shopify_in.store.shopify_orders`
- `account_data_binding.nimbus.shiprocket.primary.shiprocket_oms`
- `account_data_binding.nimbus.shiprocket.primary.shiprocket_invoice`
- `account_data_binding.nimbus.shiprocket.primary.shiprocket_settlement`

#### Reconciliation variants applied

- `reconciliation_variant.shiprocket.shiprocket_aggregator_freight_bridge`
- `reconciliation_variant.shiprocket.shiprocket_aggregator_cod_bridge`

#### Related process and reconciliation models

- Order to shipment reconciliation
- Shipment to freight invoice reconciliation
- COD delivery to courier remittance reconciliation

#### Confidence and unresolved assumptions

Curated for test retrieval. Confirm exact Shopify-to-Shiprocket order identifier mapping before production-style execution.

#### Example questions

- Which Nimbus Shopify orders have no Shiprocket shipment?
- Which Shopify COD orders were delivered but not remitted by Shiprocket?
- Which Shiprocket invoices relate to Nimbus Shopify shipments?

### Flow: Nimbus Amazon India Primary Seller → Nimbus Delhivery Direct

#### Business meaning

For Amazon merchant-fulfilled orders, Nimbus India D2C may use Delhivery as a direct courier. Amazon is the marketplace order source. Delhivery provides direct courier freight and COD/remittance evidence when the courier reference points to Delhivery.

#### Flow status

draft

#### Money-flow path

- marketplace_to_logistics
- order_to_shipment
- shipment_to_freight_invoice

#### Participating accounts and roles

- Nimbus Amazon India Primary Seller: `marketplace_source`, `order_source`
- Nimbus Delhivery Direct: `courier_source`, `logistics_source`

#### Activation conditions

Use this flow only when Amazon order/shipment evidence indicates merchant-fulfilled shipping and courier evidence indicates Delhivery. Do not use this flow for Amazon FBA/platform-fulfilled orders.

#### Evidence path

Amazon order / shipment reference → tracking ID / AWB → Delhivery invoice or settlement evidence.

#### Account Data Binding references

- `account_data_binding.nimbus.amazon_in.primary.amazon_settlement`
- `account_data_binding.nimbus.delhivery.direct.delhivery_invoice`
- `account_data_binding.nimbus.delhivery.direct.delhivery_settlement`

#### Reconciliation variants applied

- `reconciliation_variant.delhivery.delhivery_native_freight`
- `reconciliation_variant.delhivery.delhivery_native_cod`

#### Related process and reconciliation models

- Order to shipment reconciliation
- Shipment to freight invoice reconciliation
- COD delivery to courier remittance reconciliation, only when COD evidence exists

#### Confidence and unresolved assumptions

Inferred. Requires confirmation from Amazon fulfilment signal and Delhivery AWB/courier evidence.

#### Example questions

- Which Nimbus Amazon MFN orders shipped through Delhivery?
- Which Delhivery freight invoices relate to Nimbus Amazon merchant-fulfilled orders?

## 6. Logistics COD to bank flows

### Flow: Nimbus Shiprocket Primary → Nimbus HDFC Current Account

#### Business meaning

Shiprocket COD remittances for Nimbus India D2C should be matched against HDFC current account credits when UTR or bank reference is available.

#### Flow status

active

#### Money-flow path

- logistics_cod_to_bank
- courier_remittance_to_bank

#### Participating accounts and roles

- Nimbus Shiprocket Primary: `remittance_source`
- Nimbus HDFC Current Account: `bank_destination`

#### Activation conditions

Use this flow for COD shipments where Shiprocket settlement/remittance evidence exists. Do not use this flow for prepaid shipments unless the settlement table clearly contains prepaid/POS settlement rows.

#### Evidence path

Shiprocket settlement/remittance → settlement batch / UTR / bank reference → HDFC bank statement credit.

#### Account Data Binding references

- `account_data_binding.nimbus.shiprocket.primary.shiprocket_settlement`
- `account_data_binding.nimbus.hdfc.current.bank_statement`

#### Related process and reconciliation models

- Logistics COD to bank reconciliation
- Courier batch to bank reconciliation

#### Confidence and unresolved assumptions

Curated for test retrieval. Confirm whether all COD remittances use HDFC or whether some split to another bank.

#### Example questions

- Which Shiprocket COD remittances did not reach Nimbus HDFC?
- Which HDFC credits are unidentified courier remittances?
- Which COD batches have partial bank credits?

## 7. Marketplace settlement to bank flows

### Flow: Nimbus Amazon India Primary Seller → Nimbus HDFC Current Account

#### Business meaning

Amazon India marketplace settlements for Nimbus India D2C may be reconciled against HDFC bank credits when the user asks about actual cash realization in the bank.

#### Flow status

draft

#### Money-flow path

- marketplace_to_bank

#### Participating accounts and roles

- Nimbus Amazon India Primary Seller: `settlement_source`
- Nimbus HDFC Current Account: `bank_destination`

#### Activation conditions

Use this flow only when the query asks whether Amazon settlement money reached the bank. Do not use it for ordinary Amazon seller realization analysis inside settlement data.

#### Evidence path

Amazon settlement / payout reference → expected bank credit → HDFC bank statement credit.

#### Account Data Binding references

- `account_data_binding.nimbus.amazon_in.primary.amazon_settlement`
- `account_data_binding.nimbus.hdfc.current.bank_statement`

#### Related process and reconciliation models

- Marketplace settlement to bank reconciliation

#### Confidence and unresolved assumptions

Low-confidence test flow. Bank destination is fictional and must be confirmed before production-style activation.

#### Example questions

- Did Nimbus Amazon settlement reach HDFC?
- Which Amazon payouts are missing in bank?

## 8. Payment gateway to bank flows

### Flow: Nimbus Razorpay Primary → Nimbus HDFC Current Account

#### Business meaning

Razorpay payouts for Nimbus India D2C should be reconciled against HDFC current account credits.

#### Flow status

active

#### Money-flow path

- payment_gateway_to_bank

#### Participating accounts and roles

- Nimbus Razorpay Primary: `payout_source`
- Nimbus HDFC Current Account: `bank_destination`

#### Activation conditions

Use this flow for processed or paid Razorpay payouts. Use only bank credit rows on the HDFC side.

#### Evidence path

Razorpay payout → UTR / payout reference → HDFC bank statement credit.

#### Account Data Binding references

- `account_data_binding.nimbus.razorpay.primary.razorpay_payouts`
- `account_data_binding.nimbus.hdfc.current.bank_statement`

#### Related process and reconciliation models

- Payment gateway to bank reconciliation
- Payout to bank credit matching

#### Confidence and unresolved assumptions

Curated test flow.

#### Example questions

- Why does Nimbus Razorpay payout not match HDFC credit?
- Which Razorpay payouts are delayed?

## 9. Refund, dispute, and chargeback flows

No active documented flow yet.

## 10. ERP / accounting to bank flows

No active documented flow yet.

## 11. Flow caveats and unresolved assumptions

- Do not assume every Nimbus logistics remittance goes to HDFC unless the selected Business Flow Binding says so.
- Do not use Amazon settlement-to-bank flow for ordinary Amazon seller realization analysis.
- Do not use Amazon MFN to Delhivery flow for Amazon FBA/platform-fulfilled orders.
- Do not infer Delhivery participation from table existence alone; use the activation conditions and account scope.

## 12. Example questions this document should answer

- Which Business Flow Binding connects Nimbus Shopify to Shiprocket?
- Which Business Flow Binding should be used for Nimbus Shiprocket COD to HDFC reconciliation?
- Should Nimbus Amazon settlement be matched to HDFC bank credits?
- Which flow applies when a Nimbus Amazon MFN order is shipped through Delhivery?

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

Do not extract generic vendor behavior from this document. Vendor behavior belongs to Shiprocket, Delhivery, Amazon, and payment/banking docs.
