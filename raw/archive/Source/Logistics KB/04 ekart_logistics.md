---
title: Ekart Logistics Knowledge
version: 2.1-ingestion-ready
doc_type: logistics_vendor_knowledge
domain: logistics
platform: ekart
platform_type: marketplace_fulfilment
fulfilment_ownership_models:
  - platform_fulfilled
  - marketplace_fulfilment
  - settlement_only
schemas:
  - zs_observe
primary_tables:
  - zs_observe.ekart_settlement
  - zs_observe.ekart_invoice
related_tables:
  - zs_observe.shiprocket_oms
  - zs_observe.shiprocket_invoice
flow_types:
  - marketplace_fulfilment_settlement
  - cod_remittance
  - prepaid_or_pos_settlement
  - freight_billing_fallback
money_flow_paths:
  - marketplace_fulfilment_to_settlement
  - cod_delivery_to_courier_remittance
  - courier_remittance_to_bank
coverage_status: settlement_active_invoice_schema_only
status: draft
owner: finance_data_team
source_documents:
  - Logistics KB Doc.docx
related_docs:
  - logistics_domain_overview.md
  - shiprocket_logistics.md
  - logistics_reconciliation_patterns.md
---

# Ekart Logistics Knowledge

> Scope note: This document is a reusable KB grounding document. It preserves Ekart table semantics, shipment/settlement keys, transaction type meanings, amount meanings, and caveats. It does **not** define tenant/group ownership, Flipkart account ownership, customer-specific bank routing, or durable account filters. Row counts, group IDs, merchant/account semantics, brand names, and marketplace assumptions from source profiling are not durable KB truth and should be resolved through Account Data Binding, marketplace docs, or tenant/group context.

## 1. How to use this document

Use this document when questions involve Ekart settlement records, platform-fulfilled or marketplace-fulfilment logistics evidence, COD vs POS/prepaid settlement classification, shipment/batch settlement references, or Ekart invoice availability.

Retrieve this document for questions such as:

- Which Ekart settlement rows are COD vs POS/prepaid?
- Which Ekart shipments have settlement evidence?
- How should Ekart settlement batch fields be used for bank reconciliation?
- Why is Ekart freight not available through `ekart_invoice`?
- How can Ekart shipment IDs connect to operational sources such as Shiprocket OMS when a valid flow exists?

## 2. Logistics overview and business context

Ekart is modeled as a marketplace-fulfilment / platform-fulfilment logistics source. It can provide shipment-level settlement evidence for marketplace-managed fulfilment flows, especially where shipment/tracking IDs are available.

Ekart settlement data can include both:

```text
COD settlement/remittance rows
POS or prepaid/digital settlement rows
```

Ekart freight invoices are not available through `ekart_invoice` in the source snapshot. For some non-native or aggregator-routed contexts, Ekart freight may appear through a related aggregator invoice source such as Shiprocket invoice where the courier partner identifies Ekart. This fallback must not be assumed without compatible runtime scope and explicit courier evidence.

## 3. Applicability and scope model

This document describes reusable Ekart logistics and settlement semantics. It should not be treated as customer-specific or marketplace-account-specific configuration.

Terms such as FBF should be interpreted as marketplace-specific examples of the generic `platform_fulfilled` model. Do not make `FBF` the ingestion primitive.

Account identifiers such as merchant IDs, group IDs, bank names, or AWB prefixes must be treated as source fields or Account Data Binding candidates, not universal tenant or brand truth.

## 4. Fulfilment ownership and shipping model

Primary models:

```text
platform_fulfilled
marketplace_fulfilment
settlement_only
```

Interpretation:

- Ekart can represent platform/marketplace-managed logistics evidence.
- Ekart settlement can represent COD and POS/prepaid settlement flows.
- Ekart invoice/freight evidence is unavailable when `ekart_invoice` is schema-only/empty.
- Freight for Ekart-identified shipments may be embedded in marketplace economics or available through another evidence source; validate before use.

## 5. Operational shipment lifecycle

Ekart settlement primarily provides settlement and remittance evidence tied to shipment/tracking IDs.

Supported lifecycle signals:

```text
shipment / tracking ID
→ delivered date
→ settlement date
→ settlement batch / bank reference
```

For full order-to-shipment lifecycle, use marketplace/channel docs or operational shipment sources where a valid relationship is documented.

## 6. Money movement lifecycle

Ekart settlement supports two settlement types:

### COD settlement

```text
COD shipment delivered
→ cash collected
→ Ekart settlement row
→ settlement batch / bank reference
→ downstream bank matching
```

### POS / prepaid settlement

```text
prepaid or digital/POS shipment
→ settlement row
→ settlement batch / bank reference
→ downstream bank matching
```

Do not merge COD and POS/prepaid rows unless the business question explicitly asks for total settlement across payment modes.

## 7. Business objects and identifiers

| Object | Ekart field examples | Notes |
|---|---|---|
| Shipment / AWB | `shipment_id`, `tracking_id` | Primary shipment/settlement key candidate. |
| Marketplace shipment ID | `mp_id` | Marketplace-side shipment/reference field where populated. |
| Merchant/account code | `merchant_id` | Source account code; interpret via Account Data Binding, not this vendor doc. |
| Transaction type | `transaction_type`, `transaction_mode` | COD vs POS/prepaid settlement classification. |
| Settlement batch | `settlement_id`, `total_amount_of_batch` | Batch-level settlement references/amounts. |
| Settlement dates | `settlement_date`, `actual_date_of_remittance`, `due_date_of_remittance` | Used for lag and SLA analysis. |
| Delivery date | `delivered_date` | Operational date for delivery-to-remittance lag. |
| Bank bridge | `bank_reference_no`, `bank_name` | Bank matching hints; bank account scope required. |
| Financial amount | `charged_amount`, `cod_amount` | Table-specific settlement/payment amount; not automatically freight. |

## 8. Table family overview

| Table | Business role | Coverage status |
|---|---|---|
| `zs_observe.ekart_settlement` | Ekart settlement evidence for COD and POS/prepaid shipment-level or batch-level settlement analysis | active settlement evidence in source snapshot; account scope must be resolved separately |
| `zs_observe.ekart_invoice` | Intended Ekart freight invoice table | schema-only / empty in source snapshot; do not use for freight until populated |
| `zs_observe.shiprocket_oms` | Possible operational join source when Ekart shipment ID appears as Shiprocket AWB in a valid aggregator flow | optional/fallback; requires compatible scope |
| `zs_observe.shiprocket_invoice` | Possible freight fallback where Shiprocket identifies Ekart as courier partner | optional/fallback; requires explicit courier filter |

## 9. Entity relationships and join paths

Canonical Ekart settlement key:

```text
ekart_settlement.shipment_id / tracking_id
```

Possible relationships:

```text
ekart_settlement.shipment_id = shiprocket_oms.awb_code
```

or:

```text
ekart_settlement.tracking_id = shiprocket_oms.awb_code
```

when a valid business flow indicates that Shiprocket/aggregator operational evidence and Ekart settlement evidence refer to the same shipment.

Bank bridge relationship:

```text
ekart_settlement.bank_reference_no / settlement_id / amount + date window
→ bank_statement credit
```

Use batch-level matching carefully: `total_amount_of_batch` may represent a batch amount across multiple shipments rather than the shipment row amount.

## 10. Metrics and business definitions

| Metric | Definition | Preferred evidence |
|---|---|---|
| Ekart settlement row count | Count of Ekart settlement records by transaction type/status/date | `ekart_settlement` |
| Ekart COD settled amount | Sum of COD settlement amount for COD rows | `ekart_settlement` filtered to COD |
| Ekart POS settled amount | Sum of settlement amount for POS/prepaid rows | `ekart_settlement` filtered to POS/prepaid |
| Ekart total settlement amount | Sum of settlement amount across selected transaction types | `ekart_settlement` |
| Ekart batch settlement amount | Batch-level settlement amount | `total_amount_of_batch` |
| Ekart settlement lag | Actual remittance or settlement date minus delivered date | `actual_date_of_remittance` / `settlement_date`, `delivered_date` |
| Ekart bank reference coverage | Share of settlement rows/batches with bank reference populated | `bank_reference_no`, `settlement_id` |
| Ekart freight billed via fallback | Freight for Ekart shipments from fallback invoice source | `shiprocket_invoice` with Ekart courier filter, where valid |
| Ekart overdue remittance | Count of shipments/batches where actual remittance is after due date or missing after due date | `actual_date_of_remittance` / `due_date_of_remittance` |

## 11. Reconciliation playbook

Valid Ekart reconciliation use cases:

1. Ekart settlement transaction type classification: COD vs POS/prepaid.
2. Ekart shipment/tracking ID to operational shipment source, if a relationship is documented.
3. Ekart settlement batch to bank reference / bank credit.
4. COD settlement amount vs expected COD amount, where an expected COD source exists.
5. Settlement lag between delivery, due remittance, actual remittance, and settlement dates.
6. Freight visibility assessment: native invoice unavailable, fallback required or freight embedded in marketplace economics.

Invalid or low-confidence use cases until additional data exists:

- Direct Ekart freight analysis using `ekart_invoice`, when schema-only/empty.
- Inferring tenant, brand, or account ownership from `merchant_id` or AWB prefix alone.
- Treating POS/prepaid and COD settlement flows as the same without explicit aggregation intent.
- Treating `total_amount_of_batch` as shipment-level amount.

### 11.1 Reconciliation variants

| Variant name | Base profile | Variant reason | Mismatch category overrides |
|---|---|---|---|
| ekart_batch_level_cod_to_bank | `reconciliation_profile.courier_batch_to_bank_reconciliation` | Ekart settlement carries `total_amount_of_batch` at batch grain; bank-side reconciliation runs at the batch reference level, not per-AWB. | `mismatch_category.grain_mismatch`, `mismatch_category.unidentified_bank_credit` |
| ekart_native_cod_settlement | `reconciliation_profile.cod_reconciliation` | Native Ekart settlement is populated with COD vs POS classified by `transaction_type`; COD reconciliation runs from `zs_observe.ekart_settlement` filtered to COD rows. | `mismatch_category.cod_amount_mismatch`, `mismatch_category.missing_cod_remittance` |

## 12. Table-specific curated knowledge

### 12.1 Table: `zs_observe.ekart_settlement`

#### Business purpose

Contains Ekart settlement records for shipment-level and/or settlement-entry-level analysis. It supports COD and POS/prepaid settlement classification, settlement batch analysis, remittance lag analysis, and bank bridge preparation.

#### Grain

One row should be treated as one Ekart settlement entry tied to a shipment/tracking ID and transaction type. Validate grain before aggregation because settlement batches can include multiple shipments.

#### Table status and coverage

Active settlement evidence in the source snapshot. Row counts, group IDs, merchant ID meanings, bank distributions, and brand/account interpretations are profiling observations only and should not be used as reusable KB truth.

#### Applicability and account-binding notes

Fields such as `merchant_id`, `bank_name`, and any group/account identifiers are source/account fields. Their tenant/group meaning should be resolved through Account Data Binding and tenant/group context.

#### Critical filters

- Apply `is_active = true` where available.
- Use `transaction_type` or `transaction_mode` to separate COD from POS/prepaid rows.
- Use shipment-level amount fields for shipment-level metrics.
- Use `total_amount_of_batch` only at batch grain.
- Use bank-reference fields only when bank account scope is resolved.

#### Column-level information

| Column | Semantic role | Business meaning | Metric usage | Caveat |
|---|---|---|---|---|
| `shipment_id` | identifier, reconciliation key | Ekart shipment/AWB reference | join key, shipment settlement matching | May equal `tracking_id`; validate duplicates. |
| `tracking_id` | identifier, reconciliation key | Tracking/AWB reference | join key | Use as alternate to `shipment_id`. |
| `merchant_id` | identifier, account field | Source merchant/account code | account binding candidate | Do not hardcode tenant/brand semantics in vendor doc. |
| `transaction_type` | category/status | Settlement type such as COD or POS/prepaid | filtering, value profile | Required for correct settlement classification. |
| `transaction_mode` | category/status | Payment/settlement mode | filtering, cross-check | May duplicate or refine `transaction_type`. |
| `bank_name` | dimension, bank hint | Bank name recorded in settlement source | bank grouping/readiness | Not sufficient to identify bank account without Banking KB. |
| `charged_amount` | measure, financial_amount | Per-settlement/shipment amount in Ekart settlement context | COD/POS settlement metric after transaction filter | Do not interpret as freight. |
| `cod_amount` | measure, financial_amount | COD amount for COD rows where populated | COD settled/collected metric | Should be used only for COD rows or where populated meaning is confirmed. |
| `total_amount_of_batch` | measure, financial_amount | Batch-level settlement amount across multiple shipment rows | batch-to-bank matching | Do not sum at shipment grain without deduplication. |
| `settlement_id` | identifier | Settlement/batch identifier | batch grouping, bank matching | Useful with batch amount and bank reference. |
| `settlement_date` | date | Settlement date | reporting, bank matching | Use for settlement-period analysis. |
| `delivered_date` | date | Customer delivery date | remittance lag | Required for delivery-to-settlement lag. |
| `invoice_date` | date | Invoice/settlement invoice date | invoice timeline | Not necessarily freight invoice date. |
| `mp_id` | identifier | Marketplace shipment/reference ID | marketplace linkage | Interpret with marketplace docs. |
| `actual_date_of_remittance` | date | Actual remittance date | lag/SLA metric | Prefer over generic settlement date for remittance lag if populated. |
| `due_date_of_remittance` | date | Expected remittance due date | SLA/delay metric | Compare to actual remittance date. |
| `bank_reference_no` | identifier, bank_bridge | Bank reference for settlement/remittance | bank matching | Requires bank account scope and Banking KB. |

#### Value profile candidates

| Column | Candidate value | Business meaning | Use | Caveat |
|---|---|---|---|---|
| `transaction_type` | `COD` | Cash-on-delivery settlement row | COD settlement metrics | Use only as table-specific value. |
| `transaction_type` | `POS` | Digital/prepaid/POS settlement row | POS/prepaid settlement metrics | Do not combine with COD unless explicitly requested. |
| `transaction_mode` | `COD` | COD settlement/payment mode | Cross-check COD classification | Confirm consistency with `transaction_type`. |
| `transaction_mode` | `POS` | POS/prepaid settlement/payment mode | Cross-check POS classification | Confirm consistency with `transaction_type`. |
| `bank_name` | source-specific bank values | Bank name recorded by source | grouping/readiness | Bank account identity must come from Banking KB / Account Data Binding. |
| `merchant_id` | source-specific merchant codes | Source merchant/account identifier | account binding candidate | Do not encode tenant/brand meaning here. |

#### Relationship candidates

| Relationship | Join keys | Type | Use | Caveat |
|---|---|---|---|---|
| Ekart settlement → Shiprocket OMS | `shipment_id = shiprocket_oms.awb_code` or `tracking_id = shiprocket_oms.awb_code` | operational enrichment | Add shipment/status context where aggregator path exists | Only valid for compatible runtime scope; do not assume universal. |
| Ekart settlement → Shiprocket invoice | `shipment_id/tracking_id = shiprocket_invoice.other_id` + Ekart courier filter | freight fallback | Add freight billing evidence where Shiprocket identifies Ekart | Use only if courier partner identifies Ekart and scope is compatible. |
| Ekart settlement → bank statement | `bank_reference_no` / `settlement_id` / batch amount + date window | bank reconciliation | Match settlement batch to bank credit | Requires Banking KB and account scope. |

#### Reconciliation role

Primary role: settlement evidence for COD and POS/prepaid flows.

Supports:

- COD/POS settlement classification.
- Shipment settlement to operational shipment matching.
- Settlement batch to bank credit preparation.
- Remittance SLA and lag analysis.

#### Caveats

- `merchant_id` values are source account fields, not reusable tenant facts.
- AWB prefixes are identifier clues, not durable ownership proof.
- `total_amount_of_batch` is batch-level and can double count if summed per row.
- `charged_amount` is settlement/payment amount, not freight.
- Bank matching requires bank scope and may need batch-level aggregation.

#### Example questions

- Which Ekart settlements are COD versus POS?
- Which Ekart settlement rows have bank references?
- What is the settlement lag for Ekart shipments?
- Which Ekart settlement batches can be matched to bank credits?

### 12.2 Table: `zs_observe.ekart_invoice`

#### Business purpose

Intended to contain Ekart freight invoice records. In the source snapshot, this table should be treated as schema-only / empty.

#### Grain

Expected future grain is one freight invoice or invoice line, but actual grain cannot be trusted until data is populated.

#### Table status and coverage

Schema-only / empty in the source snapshot. Do not use this table for Ekart freight metrics until populated and validated.

#### Applicability and account-binding notes

If populated in the future, any account identifiers should be extracted as Account Data Binding candidates and resolved outside this vendor document.

#### Column-level information

Because the source only establishes the table as unavailable/schema-only, all columns should be treated as future schema candidates until populated. Candidate freight fields should be documented only after actual data profiling confirms semantic meaning.

#### Relationship candidates

Future likely relationship:

```text
ekart_invoice.<awb_or_tracking_field>
→ ekart_settlement.shipment_id / tracking_id
```

Do not activate this relationship until populated data confirms keys and grain.

#### Reconciliation role

Currently none for production. Future role: shipment-to-freight-invoice and freight charge reconciliation if populated.

#### Caveats

- Treat as schema-only until populated.
- Freight may be embedded in marketplace economics or visible through another source such as Shiprocket invoice. Do not assume native Ekart freight coverage.

## 13. Ingestion-compatible candidate sections

### 13.1 Relationship candidates

| Candidate ID suggestion | Source | Target | Join | Purpose | Confidence |
|---|---|---|---|---|---|
| `relationship.ekart_settlement.shiprocket_oms.awb` | `ekart_settlement` | `shiprocket_oms` | `shipment_id/tracking_id = awb_code` | Add operational shipment context | medium |
| `relationship.ekart_settlement.shiprocket_invoice.awb` | `ekart_settlement` | `shiprocket_invoice` | `shipment_id/tracking_id = other_id` + Ekart courier filter | Add freight fallback evidence | medium-low |
| `relationship.ekart_settlement.bank_statement.reference` | `ekart_settlement` | `bank_statement` | `bank_reference_no` / `settlement_id` / amount-date fallback | Match settlement batch to bank credit | medium, requires Banking KB |

### 13.2 Value profile candidates

| Candidate ID suggestion | Table | Column | Values to profile | Purpose |
|---|---|---|---|---|
| `value_profile.ekart_settlement.transaction_type` | `ekart_settlement` | `transaction_type` | COD, POS, future values | Settlement type classification |
| `value_profile.ekart_settlement.transaction_mode` | `ekart_settlement` | `transaction_mode` | COD, POS, future values | Payment mode cross-check |
| `value_profile.ekart_settlement.bank_name` | `ekart_settlement` | `bank_name` | source-specific bank values | Bank grouping/readiness; not bank account identity |
| `value_profile.ekart_settlement.merchant_id` | `ekart_settlement` | `merchant_id` | source merchant codes | Account binding candidate, not tenant meaning |

### 13.3 Metric candidates

| Candidate metric | Definition | Notes |
|---|---|---|
| `metric.ekart_cod_settled_amount` | COD settlement amount from Ekart COD rows | Filter by COD transaction type/mode |
| `metric.ekart_pos_settled_amount` | POS/prepaid settlement amount from Ekart POS rows | Filter by POS transaction type/mode |
| `metric.ekart_total_settled_amount` | Total selected Ekart settlement amount | Use selected transaction types explicitly |
| `metric.ekart_batch_settlement_amount` | Batch-level settlement amount | Use `total_amount_of_batch`; avoid row-level double counting |
| `metric.ekart_settlement_lag_days` | Days from delivery to actual/recorded remittance | Use delivery and remittance dates |
| `metric.ekart_bank_reference_coverage_rate` | Share of rows/batches with bank reference | Readiness for bank reconciliation |
| `metric.ekart_overdue_remittance_count` | Count of shipments/batches where actual remittance is after due date or missing after due date | Requires due and actual remittance dates |

### 13.4 Metric implementation candidates

| Metric | Implementation | Formula | Required tables | Caveats |
|---|---|---|---|---|
| Ekart settlement row count | `metric_impl.ekart_settlement.row_count` | `COUNT(*)` over active settlement rows, segmented by transaction type/status/date | `ekart_settlement` | Apply `is_active = true`; segment dimensions are not pre-defined. |
| Ekart COD settled amount | `metric_impl.ekart_settlement.cod_settled_amount` | `SUM(charged_amount)` where transaction type/mode = COD | `ekart_settlement` | Use COD filter; confirm amount column semantics. |
| Ekart POS settled amount | `metric_impl.ekart_settlement.pos_settled_amount` | `SUM(charged_amount)` where transaction type/mode = POS | `ekart_settlement` | POS/prepaid, not COD. |
| Ekart total settlement amount | `metric_impl.ekart_settlement.total_settled_amount` | `SUM(charged_amount)` across selected transaction types | `ekart_settlement` | Use transaction-type filter explicitly; do not sum across batch and row grains. |
| Ekart batch settlement amount | `metric_impl.ekart_settlement.batch_settlement_amount` | Use `total_amount_of_batch` at settlement/batch grain | `ekart_settlement` | Do not sum per shipment without deduplication. |
| Ekart settlement lag | `metric_impl.ekart_settlement.settlement_lag_days` | `DATE_DIFF('day', delivered_date, COALESCE(actual_date_of_remittance, settlement_date))` | `ekart_settlement` | Use only with valid dates. |
| Ekart bank reference coverage | `metric_impl.ekart_settlement.bank_reference_coverage_rate` | `COUNT(rows with bank_reference_no) / COUNT(settlement rows)` | `ekart_settlement` | Bank name alone is not bank reference. |
| Ekart overdue remittance | `metric_impl.ekart_settlement.overdue_remittance_count` | count where `actual_date_of_remittance > due_date_of_remittance` or actual missing after due date | `ekart_settlement` | Needs date normalization. |
| Ekart freight billed via fallback | `metric_impl.ekart_shiprocket_invoice.freight_billed_amount` | `SUM(shiprocket_invoice.charged_amount)` with Ekart courier label filter | `shiprocket_invoice` | Fallback only; native `ekart_invoice` is schema-only. Normalize courier label first. |

### 13.5 Formula template candidates

| Template | Formula shape | Use |
|---|---|---|
| `formula_template.sum_amount_with_filter` | `SUM(amount_column) WHERE category = value` | COD/POS settlement metrics |
| `formula_template.batch_deduped_sum` | `SUM(DISTINCT or grouped batch_amount by batch_id)` | Batch settlement metrics |
| `formula_template.date_lag_days` | `DATE_DIFF('day', start_date, end_date)` | Delivery-to-remittance lag |
| `formula_template.coverage_rate` | `COUNT(populated_key) / COUNT(total_rows)` | Bank reference coverage |
| `formula_template.overdue_count` | `COUNT(rows where actual_date > due_date or actual missing after due_date)` | Overdue remittance diagnostics |

### 13.6 Rule candidates

| Rule | Statement | Severity |
|---|---|---|
| `rule.ekart_split_cod_pos` | Ekart COD and POS/prepaid rows must be separated unless the query explicitly asks for combined settlement. | critical |
| `rule.ekart_charged_amount_not_freight` | In `ekart_settlement`, `charged_amount` is settlement/payment amount, not native freight. | critical |
| `rule.ekart_batch_amount_grain` | `total_amount_of_batch` must be used at batch grain, not summed per shipment row without deduplication. | critical |
| `rule.ekart_invoice_schema_only` | Do not use `ekart_invoice` for freight metrics while schema-only/empty. | critical |
| `rule.ekart_account_semantics_external` | Do not infer tenant/brand/account ownership from `merchant_id`, group IDs, bank names, or AWB prefixes in this vendor doc. | critical |
| `rule.ekart_bank_matching_requires_scope` | Bank matching requires bank account scope and Banking KB semantics. | high |
| `rule.ekart_shiprocket_join_requires_flow_context` | Joins to Shiprocket OMS/invoice require compatible runtime scope and shipment identity evidence. | high |

### 13.7 Validation test candidates

| Validation test | Check | Blocks execution? |
|---|---|---|
| `validation.ekart_cod_pos_filter_present` | Query computing COD or POS metric must filter or group by transaction type/mode. | yes |
| `validation.ekart_no_freight_from_settlement_charged_amount` | Query should not label `ekart_settlement.charged_amount` as freight. | yes |
| `validation.ekart_batch_amount_not_row_sum` | Query using `total_amount_of_batch` must aggregate/deduplicate by settlement/batch grain. | yes |
| `validation.ekart_no_invoice_metrics_when_schema_only` | Query should not use `ekart_invoice` for metrics unless coverage status is active. | yes |
| `validation.ekart_scope_filter_from_account_binding` | Tenant/account query should include filters from Account Data Binding, not hardcoded source profiling. | yes |
| `validation.ekart_bank_match_has_reference_or_fallback` | Bank matching query should use bank reference, settlement ID, or amount/date fallback with bank scope. | yes |

### 13.8 Query pattern candidates

| Query pattern | Purpose | Required context |
|---|---|---|
| `query_pattern.ekart_cod_pos_settlement_summary` | Summarize Ekart settlement by COD/POS, date, settlement ID, or shipment | `ekart_settlement`, Account Data Binding |
| `query_pattern.ekart_batch_to_bank_recon` | Match Ekart settlement batches to bank credits | `ekart_settlement`, bank statement, Banking KB, account scope |
| `query_pattern.ekart_settlement_lag` | Calculate delivery-to-remittance lag | `delivered_date`, `actual_date_of_remittance`, `settlement_date` |
| `query_pattern.ekart_overdue_remittance` | Identify rows/batches where due date is breached | `due_date_of_remittance`, `actual_date_of_remittance` |
| `query_pattern.ekart_shiprocket_operational_join` | Join Ekart settlement to Shiprocket OMS for operational context | valid relationship and compatible scope |
| `query_pattern.ekart_freight_visibility_check` | Determine whether freight is native, embedded, or fallback-only | `ekart_invoice` coverage + fallback docs |

## 14. Mandatory query rules

- Apply `is_active = true` where available.
- Do not hardcode row counts, group IDs, merchant/account interpretations, bank names, or AWB prefix meanings from source profiling.
- Separate COD and POS/prepaid settlement rows using `transaction_type` or `transaction_mode`.
- Treat `ekart_settlement.charged_amount` as settlement/payment amount, not freight.
- Treat `total_amount_of_batch` as batch-level amount.
- Treat `ekart_invoice` as schema-only until populated and validated.
- Use bank-reference fields only with bank account scope and Banking KB semantics.
- Use Shiprocket fallback relationships only when shipment identity and runtime scope support them.

## 15. Data-quality and semantic caveats

- Ekart settlement contains mixed transaction types; classification is mandatory.
- Batch-level fields can create double counting.
- Native Ekart freight evidence is unavailable if `ekart_invoice` is empty.
- Merchant IDs and AWB prefixes are account/source identifiers, not reusable tenant truths.
- Bank names do not identify bank accounts by themselves.
- Bank matching may require batch-level aggregation and amount/date fallback.

## 16. Supported question patterns

- Which Ekart settlements are COD versus POS/prepaid?
- What settlement amount did Ekart record by transaction type?
- Which Ekart settlement batches have bank references?
- Which Ekart remittances are overdue?
- Why should Ekart freight not be read from `ekart_invoice`?
- How can Ekart settlements be joined to operational shipment evidence?
- Which Ekart settlement batches do not match bank credits?

## 17. SQL pattern appendix

### Ekart COD/POS settlement summary

```sql
SELECT
  transaction_type,
  settlement_date,
  COUNT(*) AS settlement_rows,
  SUM(charged_amount) AS settled_amount
FROM zs_observe.ekart_settlement
WHERE is_active = true
GROUP BY transaction_type, settlement_date;
```

### Ekart batch-level settlement amount

```sql
SELECT
  settlement_id,
  bank_reference_no,
  MAX(total_amount_of_batch) AS batch_settlement_amount,
  COUNT(*) AS shipment_rows_in_batch
FROM zs_observe.ekart_settlement
WHERE is_active = true
GROUP BY settlement_id, bank_reference_no;
```

### Ekart settlement lag

```sql
SELECT
  shipment_id,
  transaction_type,
  delivered_date,
  COALESCE(actual_date_of_remittance, settlement_date) AS remittance_date,
  DATE_DIFF('day', delivered_date, COALESCE(actual_date_of_remittance, settlement_date)) AS remittance_lag_days
FROM zs_observe.ekart_settlement
WHERE is_active = true
  AND delivered_date IS NOT NULL
  AND COALESCE(actual_date_of_remittance, settlement_date) IS NOT NULL;
```

Use Account Data Binding filters in production queries. These examples intentionally omit tenant/account filters.

## 18. Extraction guidance

Expected card families:

```text
Data Understanding: Table, Column, Relationship, Value Profile
Metric Understanding: Metric, Metric Implementation, Formula Template
Reconciliation Understanding: Reconciliation Profile, Reconciliation Unit, Matching Logic, Mismatch Category
Execution Guidance: Query Pattern, Rule, Validation Test
Business Hierarchy: Account Data Binding candidates only where source/account fields are explicitly documented
```

Chunk by table block, COD/POS value-profile block, batch amount caveat, relationship candidates, and rule candidates. Keep “batch amount is not row-level” near all batch-to-bank extraction.
