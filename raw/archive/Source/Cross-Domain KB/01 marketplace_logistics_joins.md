---
title: Marketplace ⇄ Logistics Cross-Domain Joins
version: 1.0-ingestion-ready
doc_type: cross_domain_joins
domain: cross_domain_reconciliation
platform: cross_domain
schemas:
  - zs_observe
  - zs_recon_processor
primary_tables:
  - zs_observe.amazon_oms
  - zs_observe.amazon_settlement
  - zs_recon_processor.flipkart_oms
  - zs_observe.flipkart_settlement
  - zs_observe.myntra_oms
  - zs_observe.myntra_seller_report_forward
  - zs_observe.nykaa_oms
  - zs_observe.nykaa_mapper_gst
  - zs_observe.nykaa_settlement
related_tables:
  - zs_observe.shiprocket_oms
  - zs_observe.shiprocket_invoice
  - zs_observe.shiprocket_settlement
flow_types:
  - cross_domain_join
  - order_to_shipment
  - shipment_to_invoice
  - cod_remittance
---

# Marketplace ⇄ Logistics Cross-Domain Joins

## 1. Overview

This document identifies the canonical join keys between marketplace order/settlement tables and logistics aggregator (Shiprocket) tables. The marketplace side carries order, settlement, and financial truth at order or SKU grain. The logistics side adds AWB / shipment / courier truth, plus freight and COD evidence.

The pivot column is either:

1. The **channel order ID** — captured on the logistics side as `shiprocket_oms.channel_order_id` and joined back to each marketplace's order ID column.
2. The **AWB / waybill** — when a marketplace doc carries an AWB column (Myntra `forward_awb_number`, Nykaa `awb_number` in the GST mapper), it joins directly to `shiprocket_oms.awb_code`.

Once the join lands in `shiprocket_oms`, the rest of the canonical join path (`shiprocket_oms.awb_code` → `shiprocket_invoice.other_id` → `shiprocket_settlement.awb_number` → bank reference) is covered by the Shiprocket vendor doc.

## 2. Relationship card candidates

| Candidate relationship | Source table / column | Target table / column | Type | Cardinality expectation | Safe for | Caveats |
|---|---|---|---|---|---|---|
| `relationship.amazon_oms_to_shiprocket_oms` | `zs_observe.amazon_oms.order_id` | `zs_observe.shiprocket_oms.channel_order_id` | reconciliation_relation | many_to_one | order-to-shipment reconciliation for Amazon channel orders fulfilled via Shiprocket | Only valid for tenants whose Amazon channel routes through Shiprocket; otherwise zero matches. |
| `relationship.flipkart_oms_to_shiprocket_oms` | `zs_recon_processor.flipkart_oms.order_id` | `zs_observe.shiprocket_oms.channel_order_id` | reconciliation_relation | many_to_one | order-to-shipment reconciliation for Flipkart-via-Shiprocket fulfilment | Flipkart's native fulfilment is typically Ekart; only the Shiprocket-routed Flipkart subset matches. |
| `relationship.myntra_oms_to_shiprocket_oms_awb` | `zs_observe.myntra_oms.forward_awb_number` | `zs_observe.shiprocket_oms.awb_code` | reconciliation_relation | one_to_one | AWB-grain join from Myntra orders to Shiprocket shipment evidence | `forward_awb_number` sparsity must be profiled; null AWBs cannot join. |
| `relationship.myntra_oms_to_shiprocket_oms_order` | `zs_observe.myntra_oms.order_id` | `zs_observe.shiprocket_oms.channel_order_id` | reconciliation_relation | many_to_one | Fallback channel-order-level bridge when `forward_awb_number` is null | Use only when AWB join fails; cardinality is many-to-one and may overcount. |
| `relationship.nykaa_mapper_gst_to_shiprocket_oms_awb` | `zs_observe.nykaa_mapper_gst.awb_number` | `zs_observe.shiprocket_oms.awb_code` | reconciliation_relation | one_to_one | AWB-grain join from Nykaa warehouse mapper to Shiprocket shipment evidence | `nykaa_mapper_gst.awb_number` is sparse; profile coverage before relying on this join. |
| `relationship.nykaa_oms_to_shiprocket_oms_order` | `zs_observe.nykaa_oms.order_id` | `zs_observe.shiprocket_oms.channel_order_id` | reconciliation_relation | many_to_one | Fallback channel-order-level bridge from Nykaa OMS to Shiprocket when AWB enrichment is absent | `nykaa_oms.order_id` does not directly join to `nykaa_mapper_gst.orderno`; treat as Nykaa-side fallback only. |
| `relationship.amazon_settlement_to_shiprocket_settlement` | `zs_observe.amazon_settlement.order_id` | `zs_observe.shiprocket_settlement.channel_order_id` | reconciliation_relation | many_to_many | Compare Amazon-side payout against Shiprocket COD settlement for the same channel order, where Shiprocket carries the COD leg | Independent legs — do not net amounts across; partition by side. |
| `relationship.flipkart_settlement_to_shiprocket_settlement` | `zs_observe.flipkart_settlement.order_id` | `zs_observe.shiprocket_settlement.channel_order_id` | reconciliation_relation | many_to_many | Compare Flipkart-side payout to Shiprocket COD settlement when Flipkart routes COD via Shiprocket | Typically Flipkart COD remits through Ekart; only the Shiprocket-routed subset matches. |
| `relationship.myntra_seller_report_forward_to_shiprocket_invoice` | `zs_observe.myntra_seller_report_forward.forward_awb_number` | `zs_observe.shiprocket_invoice.other_id` | reconciliation_relation | one_to_one | Join Myntra forward seller report to Shiprocket freight invoice for AWB-level freight cross-check | Only valid when Myntra fulfilment used Shiprocket; otherwise zero matches expected. |
| `relationship.nykaa_mapper_gst_to_shiprocket_invoice` | `zs_observe.nykaa_mapper_gst.awb_number` | `zs_observe.shiprocket_invoice.other_id` | reconciliation_relation | one_to_one | Join Nykaa AWB mapper to Shiprocket freight invoice at AWB grain | Both sides sparse; profile before use. |

## 3. Query pattern candidates

| Query pattern | Purpose | Required cards |
|---|---|---|
| `marketplace_order_to_courier_remittance` | Trace a marketplace order through Shiprocket shipment to courier remittance, returning order, AWB, invoice ref, settlement amount, and remittance date. | `table.zs_observe.shiprocket_oms`, `table.zs_observe.shiprocket_settlement`, `relationship.myntra_oms_to_shiprocket_oms_awb`, `relationship.amazon_oms_to_shiprocket_oms` |
| `marketplace_settlement_vs_courier_cod` | Compare marketplace-side payout for COD orders against Shiprocket COD settlement on the same channel order, partitioned by side. | `table.zs_observe.shiprocket_settlement`, `relationship.amazon_settlement_to_shiprocket_settlement`, `relationship.flipkart_settlement_to_shiprocket_settlement` |
| `marketplace_freight_cross_check` | Cross-check marketplace-reported freight deduction against Shiprocket invoice freight at AWB grain. | `table.zs_observe.shiprocket_invoice`, `relationship.myntra_seller_report_forward_to_shiprocket_invoice`, `relationship.nykaa_mapper_gst_to_shiprocket_invoice` |
