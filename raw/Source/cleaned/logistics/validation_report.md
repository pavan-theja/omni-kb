# Validation Report — Logistics v6 Role Split Unified Edges

## Summary

```yaml
validation_summary:
  package: logistics_parser_ready_vendor_docs_v6_role_split
  raw_candidate_cards: 896
  unique_card_ids: 796
  candidate_edges: 2315
  duplicate_card_ids: 47
  duplicate_edge_ids: 57
  missing_edge_references: 0
  forbidden_card_types_present: []
  unknown_edge_types_present: []
  yaml_parse_errors: 0
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
| `metric` | 149 |
| `metric_dependency` | 5 |
| `metric_implementation` | 103 |
| `mismatch_category` | 49 |
| `output_contract` | 5 |
| `platform` | 8 |
| `platform_context` | 8 |
| `process_variant` | 10 |
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
| `process_variant` | 10 |
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
| `BELONGS_TO_DOMAIN` | 158 |
| `BELONGS_TO_PLATFORM` | 8 |
| `BELONGS_TO_PROCESS` | 69 |
| `BELONGS_TO_RECONCILIATION_PROFILE` | 14 |
| `BELONGS_TO_TABLE` | 215 |
| `DEPENDS_ON_METRIC` | 9 |
| `EXTENDS_PROCESS` | 26 |
| `HAS_BUSINESS_PROCESS` | 9 |
| `HAS_COLUMN` | 215 |
| `HAS_IMPLEMENTATION` | 103 |
| `HAS_MISMATCH_CATEGORY` | 28 |
| `HAS_PLATFORM_CONTEXT` | 8 |
| `HAS_PROCESS_VARIANT` | 26 |
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

## Shiprocket role split file counts

| file | candidate cards | candidate edges |
|---|---:|---:|
| `shiprocket_logistics_partner_parser_ready_v6_role_split.md` | 96 | 272 |
| `shiprocket_services_aggregator_parser_ready_v6_role_split.md` | 90 | 251 |

## Edge reference validation

No missing edge references.

## Unknown edge type validation

No unknown edge types.

## Deliberate duplicate card_ids

Repeated Metric and Platform cards across role/vendor files are deliberate for single-file readability. Ingestion should upsert/dedupe by `card_id`.

| card_id | occurrences |
|---|---:|
| `metric.actual_weight` | 2 |
| `metric.average_delivery_attempts` | 2 |
| `metric.average_freight_per_awb` | 3 |
| `metric.batch_settlement_amount` | 3 |
| `metric.billable_weight` | 3 |
| `metric.cancelled_shipment_count` | 2 |
| `metric.cod_collected_amount` | 6 |
| `metric.cod_due_amount` | 2 |
| `metric.cod_expected_amount` | 3 |
| `metric.cod_fee_amount` | 5 |
| `metric.cod_gap_amount` | 2 |
| `metric.cod_remittance_lag_days` | 5 |
| `metric.cod_remitted_amount` | 9 |
| `metric.damaged_lost_shipment_count` | 2 |
| `metric.declared_product_value` | 5 |
| `metric.delivered_shipment_count` | 4 |
| `metric.delivery_success_rate` | 2 |
| `metric.delivery_tat_days` | 3 |
| `metric.dto_freight_amount` | 2 |
| `metric.forward_freight_amount` | 5 |
| `metric.forward_shipment_count` | 2 |
| `metric.fov_insurance_amount` | 2 |
| `metric.freight_billed_amount` | 8 |
| `metric.freight_excluding_tax_amount` | 2 |
| `metric.fuel_surcharge_amount` | 3 |
| `metric.gst_on_freight_amount` | 3 |
| `metric.in_transit_shipment_count` | 2 |
| `metric.ndr_attempt_count` | 2 |
| `metric.order_total_amount` | 2 |
| `metric.payable_amount` | 2 |
| `metric.peak_surcharge_amount` | 2 |
| `metric.pickup_charge_amount` | 2 |
| `metric.populated_native_record_count` | 2 |
| `metric.pos_settled_amount` | 2 |
| `metric.qr_cod_remitted_amount` | 2 |
| `metric.return_shipment_count` | 3 |
| `metric.rto_count` | 3 |
| `metric.rto_freight_amount` | 5 |
| `metric.rto_rate` | 2 |
| `metric.rto_tat_days` | 2 |
| `metric.settlement_batch_count` | 4 |
| `metric.shipment_count` | 5 |
| `metric.shipment_pickup_lag_days` | 2 |
| `metric.sparse_native_record_count` | 2 |
| `metric.unique_awb_count` | 7 |
| `platform.shiprocket` | 2 |
| `platform_context.shiprocket.in` | 2 |

## Shiprocket role split assertions

```yaml
shiprocket_role_split_assertions:
  single_canonical_platform_id_present: true
  forbidden_shiprocket_role_platform_ids_present: false
  logistics_partner_doc_owns_table:
    - table.zs_observe.shiprocket_oms
  services_aggregator_doc_owns_tables:
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.shiprocket_settlement
    - table.zs_observe.shiprocket_settlement_report
  process_variants_added:
    - process_variant.shiprocket_logistics_partner.operational_handoff
    - process_variant.shiprocket_services_aggregator.financial_intermediary
```
