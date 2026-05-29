# Logistics Parser-Ready Vendor Docs v6 — Shiprocket Role Split + Unified Edges

This package is the v6 logistics refactor. It preserves the manifest-aligned deterministic ingestion style from v5 and splits Shiprocket into two role-specific documents while keeping one canonical platform card: `platform.shiprocket`.

## What changed from v5

Shiprocket is no longer represented as one overloaded vendor file. It is split into:

| file | role | owns |
|---|---|---|
| `shiprocket_logistics_partner_parser_ready_v6_role_split.md` | Shiprocket as logistics partner / operational handoff | `shiprocket_oms`, AWB assignment, courier routing, shipment status, delivery/RTO/return, COD expected evidence |
| `shiprocket_services_aggregator_parser_ready_v6_role_split.md` | Shiprocket as services aggregator / financial intermediary | `shiprocket_invoice`, `shiprocket_settlement`, `shiprocket_settlement_report`, freight billing, COD remittance, underlying courier financial attribution |

Both files may repeat `platform.shiprocket` and some metric cards for readability. A deterministic parser should upsert by `card_id`. Do **not** create `platform.shiprocket_logistics_partner` or `platform.shiprocket_services_aggregator`.

## Deterministic ingestion order

1. Parse `document_metadata` and reject forbidden card types in generic logistics docs.
2. Parse every `candidate_card`; upsert/dedupe by `card_id`. Repeated Metric and Platform cards are deliberate readability duplicates.
3. Parse every `candidate_edge`; normalize accepted legacy aliases into canonical uppercase edge types.
4. Materialize inverse edges only where `materialize_inverse: true`; otherwise rely on reverse graph indexes.
5. Validate every edge source/target against the package card registry.
6. Reject any Business Flow Binding or Account Data Binding emitted from these generic logistics files.

## Conceptual boundaries

- **Shiprocket Logistics Partner** = operational shipment lifecycle and `shiprocket_oms`.
- **Shiprocket Services Aggregator** = consolidated freight invoice, COD remittance, and financial aggregation tables.
- **Metric** = colloquial reusable business meaning.
- **Metric Implementation** = role/table-specific formula with required columns, filters, metric pattern, allowed grains, and caveats.
- **Business Process / Workflow Step / State Transition** stay reusable and tenant-neutral.
- **Process Variant** captures operating-model difference, not tenant/group difference.
- **Business Flow Binding** is intentionally absent; tenant/group/account routing belongs in separate applicability docs.

## Files

| file | purpose |
|---|---|
| `logistics_domain_overview_parser_ready_v6_role_split.md` | Shared logistics metric/process catalog, including the two Shiprocket role-specific process variants. |
| `logistics_reconciliation_patterns_parser_ready_v6_role_split.md` | Cross-vendor reconciliation profiles, sides, units, matching logic, query patterns, rules, tests, and output contracts. |
| `shiprocket_logistics_partner_parser_ready_v6_role_split.md` | Shiprocket operational logistics handoff and `shiprocket_oms` evidence. |
| `shiprocket_services_aggregator_parser_ready_v6_role_split.md` | Shiprocket freight invoice, COD settlement, settlement-report schema-only handling, and aggregator financial evidence. |
| `delhivery_logistics_parser_ready_v6_role_split.md` | Delhivery direct invoice and settlement evidence. |
| `dtdc_logistics_parser_ready_v6_role_split.md` | DTDC settlement-only/native invoice-empty evidence and fallback behavior. |
| `ekart_logistics_parser_ready_v6_role_split.md` | Ekart FBF/COD/POS settlement and invoice-empty handling. |
| `xpressbees_logistics_parser_ready_v6_role_split.md` | XpressBees sparse native settlement and Shiprocket fallback behavior. |
| `shadowfax_logistics_parser_ready_v6_role_split.md` | Shadowfax reverse-only/indirect evidence through Shiprocket. |
| `ecom_express_logistics_parser_ready_v6_role_split.md` | Ecom Express indirect-only evidence through Shiprocket. |
| `canonical_edge_taxonomy_registry.md` | Compact canonical edge taxonomy and legacy alias policy used by this package. |
| `validation_report.md` | Package-level validation counts, reference checks, and ingestion boundary checks. |

## Package counts

### Candidate cards by raw occurrence

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

### Candidate cards by unique card_id

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

### Candidate edges

Total candidate edges: **2315**. Duplicate edge IDs are accepted only when repeated role/readability blocks are semantically identical and should be upserted by `edge_id`.

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

## Shiprocket role split counts

### `shiprocket_logistics_partner_parser_ready_v6_role_split.md`

Candidate cards: **96**. Candidate edges: **272**.

| card_type | count |
|---|---:|
| `column` | 41 |
| `metric` | 21 |
| `metric_implementation` | 21 |
| `platform` | 1 |
| `platform_context` | 1 |
| `relationship` | 6 |
| `table` | 1 |
| `value_profile` | 4 |

### `shiprocket_services_aggregator_parser_ready_v6_role_split.md`

Candidate cards: **90**. Candidate edges: **251**.

| card_type | count |
|---|---:|
| `column` | 40 |
| `metric` | 15 |
| `metric_implementation` | 16 |
| `platform` | 1 |
| `platform_context` | 1 |
| `relationship` | 8 |
| `table` | 3 |
| `value_profile` | 6 |

## Non-negotiable logistics rules encoded here

- Do not infer amount semantics from column name alone, especially `charged_amount`.
- Do not calculate freight from `shiprocket_oms.charged_amount`; primary Shiprocket freight evidence is `shiprocket_invoice.charged_amount`.
- Do not calculate COD remitted from `shiprocket_invoice`; primary Shiprocket COD remittance evidence is `shiprocket_settlement.charged_amount`.
- Do not use empty tables as active evidence; mark them schema-only or unsupported.
- Prefer Shiprocket fallback where XpressBees native settlement is sparse and the query is not native-ingestion validation.
- Treat Shadowfax and Ecom Express as indirect/limited coverage, not native table vendors.
- Resolve tenant/group/account filters only through Account Data Binding and Business Flow Binding, not generic vendor docs.
