# Logistics Parser-Ready Vendor Docs v4 — Unified Edges

This package is the v4 logistics refactor. It follows the Flipkart V8 deterministic ingestion style: every semantic object is authored as a `candidate_card`, every graph relationship is authored as a `candidate_edge`, and every edge includes `edge_type`, `inverse_edge_type`, `materialize_inverse`, family/class metadata, source/target IDs, and confidence.

## How to read this package

Start with the domain overview to understand shared metrics, business processes, workflow steps, state transitions, process variants, formula templates, and metric dependencies. Then read the reconciliation patterns file for matching semantics. Finally read the vendor file that owns the source table or vendor-specific implementation you need.

Vendor files are intentionally reusable and **not tenant/group-specific**. They explain logistics behavior, table semantics, relationships, metric implementations, fallbacks, and caveats. Tenant/group/account participation belongs in separate Business Flow Applicability markdown that creates Business Flow Binding and Account Data Binding cards.

## Deterministic ingestion order

1. Parse `document_metadata` and reject forbidden card types in generic logistics docs.
2. Parse every `candidate_card`; upsert/dedupe by `card_id`. Repeated Metric cards across vendor docs are deliberate readability duplicates.
3. Parse every `candidate_edge`; normalize any accepted legacy aliases into canonical uppercase edge types.
4. Materialize inverse edges only where `materialize_inverse: true`; otherwise rely on reverse graph indexes.
5. Validate every edge source/target against the package card registry or a deliberately external reference.
6. Reject any Business Flow Binding or Account Data Binding emitted from these generic files.

## Conceptual boundaries

- **Metric** = colloquial reusable business meaning, for example COD Remitted Amount or Freight Billed Amount.
- **Metric Implementation** = vendor/table-specific formula, required columns, filters, metric pattern, allowed grains, date basis, and caveats.
- **Business Process** = reusable lifecycle, for example COD Delivery to Courier Remittance.
- **Workflow Step** = evidence-bearing checkpoint inside a process.
- **State Transition** = from-state to to-state expectation with lag and failure classification.
- **Process Variant** = operating-model variation, not tenant/group variation. Examples: Shiprocket aggregator-routed, Ekart platform-fulfilled, Shadowfax reverse-only, Ecom indirect-only.
- **Business Flow Binding** is intentionally absent here. It belongs in tenant/group business-flow applicability docs.

## Files

| file | purpose |
|---|---|
| `logistics_domain_overview_parser_ready_v4_unified_edges.md` | Shared logistics metric/process catalog and operational process layer. |
| `logistics_reconciliation_patterns_parser_ready_v4_unified_edges.md` | Cross-vendor reconciliation profiles, sides, units, matching logic, query patterns, rules, tests, and output contracts. |
| `shiprocket_logistics_parser_ready_v4_unified_edges.md` | Shiprocket aggregator tables, relationships, value profiles, metric implementations, and guardrails. |
| `delhivery_logistics_parser_ready_v4_unified_edges.md` | Delhivery direct invoice and settlement evidence. |
| `dtdc_logistics_parser_ready_v4_unified_edges.md` | DTDC settlement-only/native invoice-empty evidence and fallback behavior. |
| `ekart_logistics_parser_ready_v4_unified_edges.md` | Ekart FBF/COD/POS settlement and invoice-empty handling. |
| `xpressbees_logistics_parser_ready_v4_unified_edges.md` | XpressBees sparse native settlement and Shiprocket fallback behavior. |
| `shadowfax_logistics_parser_ready_v4_unified_edges.md` | Shadowfax reverse-only/indirect evidence through Shiprocket. |
| `ecom_express_logistics_parser_ready_v4_unified_edges.md` | Ecom Express indirect-only evidence through Shiprocket. |
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

### Candidate edges

Total candidate edges: **2304**. Materialized inverse edges physically authored: **485**.

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

## Non-negotiable logistics rules encoded here

- Do not infer amount semantics from column name alone, especially `charged_amount`.
- Do not join AWB-level settlements directly to bank credits without aggregation to batch/UTR/reference grain.
- Do not use empty tables as evidence; mark them schema-only or unsupported.
- Prefer Shiprocket fallback where XpressBees native settlement is sparse and the query is not native-ingestion validation.
- Treat Shadowfax and Ecom Express as indirect/limited coverage, not native table vendors.
- Resolve tenant/group/account filters only through Account Data Binding and Business Flow Binding, not generic vendor docs.
