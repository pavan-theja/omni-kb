# Validation Report — Logistics v4 Unified Edges

## Summary

```yaml
validation_summary:
  package: logistics_parser_ready_vendor_docs_v4_unified_edges
  raw_candidate_cards: 890
  unique_card_ids: 795
  candidate_edges: 2304
  missing_edge_references: 0
  forbidden_card_types_present: []
  unknown_edge_types_present: []
  cards_missing_required_common_fields: 0
  result: pass
```

## Raw candidate card counts

| card_type | raw candidates |
|---|---:|
| `business_process` | 9 |
| `column` | 215 |
| `domain` | 1 |
| `execution_constraint_set` | 10 |
| `formula_template` | 7 |
| `matching_logic` | 15 |
| `metric` | 146 |
| `metric_dependency` | 5 |
| `metric_implementation` | 103 |
| `mismatch_category` | 49 |
| `output_contract` | 5 |
| `platform` | 7 |
| `platform_context` | 7 |
| `process_variant` | 9 |
| `query_pattern` | 31 |
| `reconciliation_profile` | 7 |
| `reconciliation_side` | 14 |
| `reconciliation_unit` | 26 |
| `reconciliation_variant` | 7 |
| `relationship` | 22 |
| `rule` | 44 |
| `state_transition` | 30 |
| `table` | 13 |
| `validation_test` | 44 |
| `value_profile` | 25 |
| `workflow_step` | 39 |

## Unique card_id counts

| card_type | unique card_ids |
|---|---:|
| `business_process` | 9 |
| `column` | 215 |
| `domain` | 1 |
| `execution_constraint_set` | 10 |
| `formula_template` | 7 |
| `matching_logic` | 15 |
| `metric` | 51 |
| `metric_dependency` | 5 |
| `metric_implementation` | 103 |
| `mismatch_category` | 49 |
| `output_contract` | 5 |
| `platform` | 7 |
| `platform_context` | 7 |
| `process_variant` | 9 |
| `query_pattern` | 31 |
| `reconciliation_profile` | 7 |
| `reconciliation_side` | 14 |
| `reconciliation_unit` | 26 |
| `reconciliation_variant` | 7 |
| `relationship` | 22 |
| `rule` | 44 |
| `state_transition` | 30 |
| `table` | 13 |
| `validation_test` | 44 |
| `value_profile` | 25 |
| `workflow_step` | 39 |

## Candidate edge counts

| edge_type | count |
|---|---:|
| `APPLIES_TO_PLATFORM` | 11 |
| `APPLIES_TO_QUERY_PATTERN` | 29 |
| `BELONGS_TO_DOMAIN` | 155 |
| `BELONGS_TO_PLATFORM` | 7 |
| `BELONGS_TO_PROCESS` | 69 |
| `BELONGS_TO_RECONCILIATION_PROFILE` | 14 |
| `BELONGS_TO_TABLE` | 215 |
| `DEPENDS_ON_METRIC` | 9 |
| `EXTENDS_PROCESS` | 23 |
| `HAS_BUSINESS_PROCESS` | 9 |
| `HAS_COLUMN` | 215 |
| `HAS_IMPLEMENTATION` | 103 |
| `HAS_MISMATCH_CATEGORY` | 28 |
| `HAS_PLATFORM_CONTEXT` | 7 |
| `HAS_PROCESS_VARIANT` | 23 |
| `HAS_RECONCILIATION_PROFILE` | 13 |
| `HAS_RECONCILIATION_SIDE` | 14 |
| `HAS_RELATIONSHIP` | 44 |
| `HAS_STATE_TRANSITION` | 30 |
| `HAS_VALIDATION_TEST` | 62 |
| `HAS_VALUE_PROFILE` | 50 |
| `HAS_WORKFLOW_STEP` | 39 |
| `IMPLEMENTS_METRIC` | 103 |
| `INCLUDES_RULE` | 120 |
| `INCLUDES_VALIDATION_TEST` | 120 |
| `PARENT_METRIC` | 5 |
| `PRODUCES_METRIC` | 53 |
| `PROFILES_COLUMN` | 25 |
| `PROFILES_TABLE` | 25 |
| `REQUIRES_RULE` | 61 |
| `SOURCED_FROM_PLATFORM` | 11 |
| `SOURCE_TABLE` | 22 |
| `SUPPORTS_PROCESS` | 13 |
| `SUPPORTS_RECONCILIATION_PROFILE` | 7 |
| `TARGET_TABLE` | 22 |
| `TRIGGERED_BY_STEP` | 30 |
| `USES_COLUMN` | 137 |
| `USES_DEPENDENT_METRIC` | 9 |
| `USES_FORMULA_TEMPLATE` | 77 |
| `USES_MATCHING_LOGIC` | 7 |
| `USES_METRIC` | 26 |
| `USES_OUTPUT_CONTRACT` | 31 |
| `USES_RECONCILIATION_PROFILE` | 29 |
| `USES_SOURCE_COLUMN` | 22 |
| `USES_TABLE` | 158 |
| `USES_TARGET_COLUMN` | 22 |

## Deliberate duplicated card_ids

Repeated Metric cards across vendor files are deliberate for single-file readability. Ingestion should upsert/dedupe by `card_id`.

| card_id | occurrences | files |
|---|---:|---|
| `metric.actual_weight` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.average_delivery_attempts` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.average_freight_per_awb` | 3 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.batch_settlement_amount` | 3 | ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.billable_weight` | 3 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.cancelled_shipment_count` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.cod_collected_amount` | 6 | delhivery_logistics_parser_ready_v3_expansive.md, dtdc_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md, xpressbees_logistics_parser_ready_v3_expansive.md |
| `metric.cod_due_amount` | 2 | dtdc_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.cod_expected_amount` | 3 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.cod_fee_amount` | 5 | delhivery_logistics_parser_ready_v3_expansive.md, dtdc_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.cod_gap_amount` | 2 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.cod_remittance_lag_days` | 4 | dtdc_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.cod_remitted_amount` | 8 | delhivery_logistics_parser_ready_v3_expansive.md, dtdc_logistics_parser_ready_v3_expansive.md, ecom_express_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shadowfax_logistics_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md, xpressbees_logistics_parser_ready_v3_expansive.md |
| `metric.damaged_lost_shipment_count` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.declared_product_value` | 5 | delhivery_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shadowfax_logistics_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.delivered_shipment_count` | 4 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md, xpressbees_logistics_parser_ready_v3_expansive.md |
| `metric.delivery_success_rate` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.delivery_tat_days` | 3 | dtdc_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.dto_freight_amount` | 2 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.forward_freight_amount` | 5 | delhivery_logistics_parser_ready_v3_expansive.md, dtdc_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.forward_shipment_count` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.fov_insurance_amount` | 2 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.freight_billed_amount` | 8 | delhivery_logistics_parser_ready_v3_expansive.md, dtdc_logistics_parser_ready_v3_expansive.md, ecom_express_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shadowfax_logistics_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md, xpressbees_logistics_parser_ready_v3_expansive.md |
| `metric.freight_excluding_tax_amount` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.fuel_surcharge_amount` | 3 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.gst_on_freight_amount` | 3 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.in_transit_shipment_count` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.ndr_attempt_count` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.order_total_amount` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.payable_amount` | 2 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.peak_surcharge_amount` | 2 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.pickup_charge_amount` | 2 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.populated_native_record_count` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, xpressbees_logistics_parser_ready_v3_expansive.md |
| `metric.pos_settled_amount` | 2 | ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.qr_cod_remitted_amount` | 2 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.return_shipment_count` | 3 | logistics_domain_overview_parser_ready_v3_expansive.md, shadowfax_logistics_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.rto_count` | 3 | delhivery_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.rto_freight_amount` | 5 | delhivery_logistics_parser_ready_v3_expansive.md, dtdc_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.rto_rate` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.rto_tat_days` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.settlement_batch_count` | 4 | delhivery_logistics_parser_ready_v3_expansive.md, dtdc_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md |
| `metric.shipment_count` | 5 | delhivery_logistics_parser_ready_v3_expansive.md, ecom_express_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shadowfax_logistics_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.shipment_pickup_lag_days` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md |
| `metric.sparse_native_record_count` | 2 | logistics_domain_overview_parser_ready_v3_expansive.md, xpressbees_logistics_parser_ready_v3_expansive.md |
| `metric.unique_awb_count` | 6 | delhivery_logistics_parser_ready_v3_expansive.md, dtdc_logistics_parser_ready_v3_expansive.md, ekart_logistics_parser_ready_v3_expansive.md, logistics_domain_overview_parser_ready_v3_expansive.md, shiprocket_logistics_parser_ready_v3_expansive.md, xpressbees_logistics_parser_ready_v3_expansive.md |

## Missing edge references

None.

## Cards missing required common fields

None.

## Boundary checks

- Forbidden generic-logistics card types are absent.
- Candidate edges use the canonical uppercase edge taxonomy.
- Edge inverse metadata is present on every edge.
- Business Flow Binding remains reserved for tenant/group business-flow applicability docs.
