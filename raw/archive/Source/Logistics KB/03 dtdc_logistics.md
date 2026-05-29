---
title: DTDC Logistics Knowledge
version: 2.1-ingestion-ready
doc_type: logistics_vendor_knowledge
domain: logistics
platform: dtdc
platform_type: courier
fulfilment_ownership_models:
  - direct_courier
  - settlement_only
schemas:
  - zs_observe
primary_tables:
  - zs_observe.dtdc_settlement
  - zs_observe.dtdc_invoice
related_tables:
  - zs_observe.shiprocket_invoice
  - zs_observe.shiprocket_oms
flow_types:
  - cod_remittance
  - freight_billing_fallback
money_flow_paths:
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

# DTDC Logistics Knowledge

> Scope note: This document is a reusable KB grounding document. It preserves DTDC table semantics, join keys, amount meanings, value meanings, and reconciliation caveats. It does **not** define tenant/group ownership, marketplace ownership, account scope, or durable customer routing. Row counts, group IDs, tenant names, and marketplace/account interpretations from source profiling are not durable KB truth and should be handled through Account Data Binding or tenant/group context documents.

## 1. How to use this document

Use this document when questions involve DTDC COD remittance, DTDC AWB settlement evidence, DTDC UTR/bank-reference fields, or DTDC freight visibility through fallback sources.

Retrieve this document for questions such as:

- Which DTDC AWBs have COD remittance evidence?
- Which DTDC settlement rows have UTR or bank reference fields?
- Why is DTDC freight not available in `dtdc_invoice`?
- How can DTDC settlement be joined to Shiprocket invoice evidence?
- Which amount fields in DTDC settlement are COD/product/remittance amounts rather than freight?

## 2. Logistics overview and business context

DTDC is modeled as a direct courier / courier settlement source in the logistics KB. In the curated source, DTDC has usable COD settlement evidence in `zs_observe.dtdc_settlement` and a schema-only or empty freight invoice table in `zs_observe.dtdc_invoice`.

DTDC can also appear as an underlying courier inside Shiprocket freight evidence. In that case, Shiprocket is the aggregator evidence source and DTDC is the final courier partner. Use Shiprocket invoice data for DTDC freight only when the selected flow and account scope support that relationship.

## 3. Applicability and scope model

This document describes reusable DTDC logistics knowledge. It should not be treated as customer-specific account configuration.

Account filters such as group identifiers, merchant identifiers, seller identifiers, or tenant-specific account fields should be resolved through Account Data Binding. Source-profile row counts and group IDs must not be embedded as durable KB rules.

DTDC supports two reusable evidence patterns:

```text
DTDC settlement table = COD remittance evidence
DTDC invoice table = schema-only / unavailable freight evidence until populated
```

Freight billing fallback through Shiprocket should be used only when Shiprocket invoice rows explicitly identify DTDC as courier partner and the runtime scope includes the relevant Shiprocket data.

## 4. Fulfilment ownership and shipping model

Primary models:

```text
direct_courier
settlement_only
```

Secondary/fallback model:

```text
underlying_courier_through_aggregator
```

Interpretation:

- DTDC settlement evidence can support COD remittance analysis.
- DTDC direct invoice/freight evidence is not currently supported if `dtdc_invoice` is empty or schema-only.
- DTDC freight can be analyzed through Shiprocket only when Shiprocket invoice identifies DTDC as courier partner.

## 5. Operational shipment lifecycle

The DTDC settlement source mainly provides downstream remittance evidence, not the complete operational shipment lifecycle.

Supported lifecycle evidence:

```text
pickup date
→ delivery date
→ COD remittance / settlement date
→ UTR or bank reference, where populated
```

Operational shipment status can be inferred only from available settlement fields such as `order_status`, `pickup_date`, and `delivery_date`. If full shipment lifecycle evidence is needed, join to an operational shipment source such as Shiprocket OMS or marketplace/channel OMS where documented.

## 6. Money movement lifecycle

DTDC money movement in this KB is primarily COD remittance.

```text
COD shipment delivered
→ DTDC collects COD
→ DTDC settlement/remittance row created
→ settlement date / UTR / bank reference recorded
→ bank credit can be matched downstream by Banking KB
```

`dtdc_settlement.charged_amount` should be interpreted as COD/product/remittance amount in this table context, not as freight.

`dtdc_invoice` should not be used for freight amount calculations unless future data confirms it is populated and semantically valid.

## 7. Business objects and identifiers

| Object | DTDC field examples | Notes |
|---|---|---|
| Merchant/source order | `order_id`, `reference_no` | Source order format may vary; prefix patterns are identifier clues, not tenant truth. |
| AWB / waybill | `airwaybill_number` | Primary DTDC shipment/remittance key. |
| Shipment number | `shipment_no` | DTDC internal shipment reference. |
| Invoice reference | `invoice_number` | Settlement/invoice reference; freight table is schema-only in source. |
| COD collected/remitted | `charged_amount`, `cod_amount`, `cod_due` | Meaning is table-specific; do not infer freight. |
| Settlement date | `settlement_date` | DTDC remittance date. |
| Bank bridge | `utr_no`, `utr_date`, `bank_ref_number` | Use for downstream bank matching when populated. |
| Zone | `zone_name` | Delivery zone/route signal. |
| Pickup / delivery dates | `pickup_date`, `delivery_date` | Can support lag analysis. |

## 8. Table family overview

| Table | Business role | Coverage status |
|---|---|---|
| `zs_observe.dtdc_settlement` | DTDC COD settlement/remittance evidence at AWB or shipment-remittance grain | active settlement evidence in source snapshot; account scope must be resolved separately |
| `zs_observe.dtdc_invoice` | Intended DTDC freight invoice table | schema-only / empty in source snapshot; do not use for freight until populated |
| `zs_observe.shiprocket_invoice` | Possible fallback for DTDC freight when Shiprocket identifies DTDC as courier partner | fallback source; use only with explicit courier filter and valid scope |

## 9. Entity relationships and join paths

Canonical DTDC relationships:

```text
dtdc_settlement.airwaybill_number
→ dtdc_invoice.<awb_or_tracking_field>, if populated in future
```

Current practical fallback relationship:

```text
dtdc_settlement.airwaybill_number
→ shiprocket_invoice.other_id
where shiprocket_invoice.courier_partner indicates DTDC
```

Optional operational relationship:

```text
dtdc_settlement.airwaybill_number
→ shiprocket_oms.awb_code
```

Use AWB-level joins carefully. If the bank side is batch-level, aggregate DTDC settlement rows to remittance/bank-reference grain before comparing to bank credits.

## 10. Metrics and business definitions

| Metric | Definition | Preferred evidence |
|---|---|---|
| DTDC remitted shipment count | Count of DTDC settlement rows/AWBs with remittance evidence | `dtdc_settlement` |
| DTDC COD remitted amount | Sum of COD/remittance amount from settlement rows | `dtdc_settlement.charged_amount` or validated COD/remittance column |
| DTDC COD collected amount | Sum of COD collected where separately populated | `dtdc_settlement.cod_amount` |
| DTDC COD due amount | Sum of COD still due/unremitted where populated | `dtdc_settlement.cod_due` |
| DTDC remittance lag | Settlement date minus delivery date | `settlement_date`, `delivery_date` |
| DTDC UTR coverage rate | Share of settlement rows with UTR or bank reference populated | `utr_no`, `bank_ref_number` |
| DTDC freight billed via Shiprocket | Freight amount for DTDC shipments when fallback invoice source identifies DTDC | `shiprocket_invoice` with DTDC courier filter |
| DTDC settlement-to-freight matched AWB count | Count of DTDC settlement AWBs that match freight invoice evidence | `dtdc_settlement` + `shiprocket_invoice` |

## 11. Reconciliation playbook

Valid DTDC reconciliation use cases:

1. DTDC AWB to COD remittance evidence.
2. DTDC COD remittance to bank bridge using UTR / bank reference fields.
3. DTDC settlement AWB to Shiprocket invoice freight evidence where DTDC is the courier partner.
4. DTDC remittance lag analysis using delivery and settlement dates.
5. DTDC COD due or unremitted amount analysis where `cod_due` is populated.

Invalid or low-confidence use cases until additional data exists:

- Direct DTDC freight analysis using `dtdc_invoice`, when the table is schema-only/empty.
- Tenant-specific DTDC account filtering from this vendor doc alone.
- Inferring marketplace/channel origin only from an order ID prefix.

### 11.1 Reconciliation variants

| Variant name | Base profile | Variant reason | Mismatch category overrides |
|---|---|---|---|
| dtdc_settlement_only_cod | `reconciliation_profile.cod_reconciliation` | Native DTDC settlement is the only durable source; invoice table is schema-only, so COD remittance reconciliation runs from `zs_observe.dtdc_settlement` without paired native freight evidence. | `mismatch_category.cod_amount_mismatch`, `mismatch_category.missing_cod_remittance` |
| dtdc_freight_via_shiprocket | `reconciliation_profile.shipment_to_invoice_reconciliation` | DTDC native invoice is empty; freight charges for DTDC AWBs must be sourced from `zs_observe.shiprocket_invoice` rows where DTDC is the underlying courier label. | `mismatch_category.missing_invoice`, `mismatch_category.schema_only_source` |

## 12. Table-specific curated knowledge

### 12.1 Table: `zs_observe.dtdc_settlement`

#### Business purpose

Contains DTDC COD settlement/remittance records. Use this as DTDC's primary source for COD remittance, remittance dates, UTR/bank-reference fields, and AWB-level settlement evidence.

#### Grain

One row should be treated as one DTDC settlement/remittance record tied to an AWB or shipment reference. Validate uniqueness by `airwaybill_number`, `order_id`, `settlement_date`, and bank/reference fields before assuming strict one-AWB-one-row grain.

#### Table status and coverage

Active settlement evidence in the source snapshot. Row counts, account IDs, group IDs, and period-specific statistics are profiling observations only and should not be used as reusable KB truth.

#### Applicability and account-binding notes

This table may contain source/account fields such as group or account identifiers. These should be extracted only as Account Data Binding candidates and resolved separately for each tenant/group/platform account.

#### Critical filters

- Apply `is_active = true` if the table has `is_active`.
- Use `transaction_type` value semantics before selecting remitted rows.
- Use date filters on remittance/settlement date for remittance analysis and delivery date for operational lag analysis.

#### Column-level information

| Column | Semantic role | Business meaning | Metric usage | Caveat |
|---|---|---|---|---|
| `order_id` | identifier | Merchant/source order reference associated with DTDC settlement | grouping, tracing | Prefix patterns are clues only; do not infer tenant/channel ownership without supporting context. |
| `airwaybill_number` | identifier, reconciliation key | DTDC AWB / waybill number | join key, shipment remittance matching | Primary key candidate for DTDC-to-freight or DTDC-to-operational joins. |
| `shipment_no` | identifier | DTDC internal shipment number | tracing | Use as secondary identifier, not preferred cross-source key unless documented. |
| `order_status` | status | Shipment/order status visible in settlement source | filtering, delivery status checks | Value profile should be built from observed values before use. |
| `charged_amount` | measure, financial_amount | COD/product/remittance amount in DTDC settlement context | COD remitted metric after validation | Do not treat as freight in this table. |
| `cod_amount` | measure, financial_amount | COD amount collected/recorded for the shipment | COD collected metric | Confirm relation to `charged_amount`; both may not be interchangeable. |
| `cod_due` | measure, financial_amount | COD amount still due or not remitted where populated | COD due/unremitted metric | May be null/zero depending on settlement state. |
| `transaction_type` | status/category | Remittance transaction type | filter for remittance state | Example source value includes `Remitted`; do not assume exhaustive values. |
| `settlement_date` | date | Date of DTDC-to-seller remittance/settlement | date filter, lag metric | Recommended date for remittance-period reporting. |
| `created_date` | date | Original record/shipment creation date | operational timeline | Not a substitute for remittance date. |
| `delivery_date` | date | Delivery date to customer | remittance lag | Needed for settlement lag metrics. |
| `pickup_date` | date | Shipment pickup date | pickup-to-delivery lag | Useful operational signal if populated. |
| `invoice_number` | identifier | DTDC settlement/invoice reference | join/reference | Do not use as freight evidence while invoice table is empty. |
| `utr_no` | identifier, bank_bridge | UTR for remittance bank transfer | bank matching | Use with bank statement only after account scope is resolved. |
| `utr_date` | date | UTR/bank transaction date | bank matching, lag | Can differ from settlement date. |
| `bank_ref_number` | identifier, bank_bridge | Bank reference for remittance/batch | bank matching | Use as secondary bank bridge. |
| `reference_no` | identifier | Merchant or source reference number | tracing | Interpret source-specific semantics carefully. |
| `zone_name` | dimension | Delivery zone/route | grouping, freight diagnostics | Not enough for rate-card validation without weight/service fields. |

#### Value profile candidates

| Column | Candidate value | Business meaning | Use | Caveat |
|---|---|---|---|---|
| `transaction_type` | `Remitted` | COD/remittance has been remitted or settlement row represents remitted state | Include in COD remitted metrics | Confirm whether other transaction types can appear in future data. |
| `order_status` | source-specific status values | Shipment/order status in DTDC settlement feed | delivery or remittance diagnostics | Build value profile from actual data before hardcoding delivered/RTO mappings. |
| `zone_name` | source-specific zone values | Courier delivery zone | freight/route grouping | Do not infer charge correctness without rate card. |

#### Relationship candidates

| Relationship | Join keys | Type | Use | Caveat |
|---|---|---|---|---|
| DTDC settlement → Shiprocket invoice | `dtdc_settlement.airwaybill_number = shiprocket_invoice.other_id` with DTDC courier filter | reconciliation / fallback | Link DTDC COD settlement to Shiprocket freight evidence | Only valid when Shiprocket invoice identifies DTDC as courier partner and account scope is compatible. |
| DTDC settlement → Shiprocket OMS | `dtdc_settlement.airwaybill_number = shiprocket_oms.awb_code` | operational lookup | Add shipment lifecycle/courier routing context | Only if Shiprocket is the aggregator source for the same AWB. |
| DTDC settlement → bank statement | `utr_no` / `bank_ref_number` / amount + date window | reconciliation | Match courier remittance to bank credit | Banking KB and account scope required. Aggregate where bank credit is batch-level. |

#### Reconciliation role

Primary role: COD remittance evidence.

Supports:

- COD expected vs COD remitted, if expected COD source exists.
- DTDC remittance to bank bridge, if UTR or bank reference exists.
- Settlement-to-freight enrichment through Shiprocket invoice fallback where documented.

#### Caveats

- `charged_amount` is not freight in this table.
- Source order ID prefixes must not be used as tenant or marketplace truth.
- Bank matching requires bank account scope and Banking KB semantics.
- If `dtdc_invoice` is empty, do not claim direct DTDC freight coverage.

#### Example questions

- Which DTDC AWBs have remittance evidence?
- Which DTDC settlements have UTRs?
- What COD amount did DTDC remit for each AWB?
- Which DTDC remittances can be matched to bank references?

### 12.2 Table: `zs_observe.dtdc_invoice`

#### Business purpose

Intended to contain DTDC freight invoice records. In the source snapshot, this table should be treated as schema-only / empty.

#### Grain

Expected grain is one invoice or freight billing record, but actual grain cannot be trusted until data is populated.

#### Table status and coverage

Schema-only / empty in the source snapshot. Do not use for DTDC freight metrics until populated and validated.

#### Applicability and account-binding notes

If populated in the future, account filters should be extracted as Account Data Binding candidates and not hardcoded here.

#### Column-level information

| Column | Semantic role | Business meaning | Metric usage | Caveat |
|---|---|---|---|---|
| `order_id` | identifier | Order reference | tracing | Schema-only until populated. |
| `invoice_number` | identifier | DTDC invoice reference | freight invoice matching | Schema-only until populated. |
| `transaction_type` | category | Freight transaction type | value profiling | Schema-only until populated. |
| `fulfilment_channel` | dimension | Fulfilment/shipping channel | segmentation | Schema-only until populated. |
| `destination_city` | dimension | Destination city | route grouping | Schema-only until populated. |
| `source_city` | dimension | Origin/source city | route grouping | Schema-only until populated. |
| `mp_fees` | measure | Marketplace or platform fee field if present | do not use by default | Needs semantic validation. |
| `mp_fees_gst_amount` | measure | GST on marketplace/platform fees | do not use by default | Needs semantic validation. |
| `freight_charge` | measure | Forward freight charge candidate | freight billed metric if populated | Validate against invoice total. |
| `cod_charge` | measure | COD collection fee candidate | COD fee metric if populated | Not COD collected/remitted. |
| `charge_rto` | measure | RTO charge candidate | RTO freight metric if populated | Needs status/flow context. |
| `zone` | dimension | Courier zone | route/rate diagnostics | Requires rate-card context. |
| `charged_weight` | measure | Billable/charged weight | rate-card checks | Validate units. |

#### Value profile candidates

Build only after data is populated. Candidate fields include `transaction_type`, `fulfilment_channel`, `zone`, and route city fields.

#### Relationship candidates

Future likely relationship:

```text
dtdc_invoice.<awb_or_reference_field>
→ dtdc_settlement.airwaybill_number or invoice_number
```

Do not activate this relationship until populated data confirms keys.

#### Reconciliation role

Currently none for production. Future role: shipment-to-freight-invoice and freight charge reconciliation.

#### Caveats

- Treat as schema-only until populated.
- Do not use for freight metrics while empty.
- Use Shiprocket invoice fallback only when supported by runtime scope and courier partner filter.

## 13. Ingestion-compatible candidate sections

### 13.1 Relationship candidates

| Candidate ID suggestion | Source | Target | Join | Purpose | Confidence |
|---|---|---|---|---|---|
| `relationship.dtdc_settlement.shiprocket_invoice.awb` | `dtdc_settlement` | `shiprocket_invoice` | `airwaybill_number = other_id` + DTDC courier filter | Match DTDC COD settlement to Shiprocket freight invoice evidence | medium |
| `relationship.dtdc_settlement.shiprocket_oms.awb` | `dtdc_settlement` | `shiprocket_oms` | `airwaybill_number = awb_code` | Add operational shipment context | medium |
| `relationship.dtdc_settlement.bank_statement.utr` | `dtdc_settlement` | `bank_statement` | `utr_no` / `bank_ref_number` / amount-date fallback | Match courier remittance to bank credit | medium, requires Banking KB |

### 13.2 Value profile candidates

| Candidate ID suggestion | Table | Column | Values to profile | Purpose |
|---|---|---|---|---|
| `value_profile.dtdc_settlement.transaction_type` | `dtdc_settlement` | `transaction_type` | `Remitted`, future values | COD remittance state classification |
| `value_profile.dtdc_settlement.order_status` | `dtdc_settlement` | `order_status` | source-specific statuses | Delivery/remittance diagnostics |
| `value_profile.dtdc_invoice.transaction_type` | `dtdc_invoice` | `transaction_type` | future values | Freight type classification if populated |

### 13.3 Metric candidates

| Candidate metric | Definition | Notes |
|---|---|---|
| `metric.dtdc_cod_remitted_amount` | COD/remittance amount remitted through DTDC settlement records | Table-specific implementation of generic COD remitted metric |
| `metric.dtdc_cod_collected_amount` | COD amount collected/recorded by DTDC | Use `cod_amount` only after confirming semantic relation to remittance |
| `metric.dtdc_cod_due_amount` | COD amount still due/unremitted | Use `cod_due` where populated |
| `metric.dtdc_remittance_lag_days` | Days between delivery date and settlement date | Requires valid dates |
| `metric.dtdc_utr_coverage_rate` | Share of settlement rows with UTR/bank reference populated | Useful for bank reconciliation readiness |
| `metric.dtdc_freight_billed_amount_via_shiprocket` | Freight billed for DTDC courier shipments through Shiprocket invoice | Requires Shiprocket fallback relationship and courier filter |

### 13.4 Metric implementation candidates

| Metric | Implementation | Formula | Required tables | Caveats |
|---|---|---|---|---|
| DTDC remitted shipment count | `metric_impl.dtdc_settlement.remitted_shipment_count` | `COUNT(DISTINCT airwaybill_number)` over remittance rows | `dtdc_settlement` | Apply `is_active = true` and remittance `transaction_type` filter before counting. |
| DTDC COD remitted amount | `metric_impl.dtdc_settlement.cod_remitted_amount` | `SUM(charged_amount)` over remittance rows | `dtdc_settlement` | `charged_amount` is COD/remittance amount in this table, not freight. |
| DTDC COD collected amount | `metric_impl.dtdc_settlement.cod_collected_amount` | `SUM(cod_amount)` | `dtdc_settlement` | Confirm not duplicate of remitted amount. |
| DTDC COD due amount | `metric_impl.dtdc_settlement.cod_due_amount` | `SUM(cod_due)` | `dtdc_settlement` | Null/zero handling required. |
| DTDC remittance lag | `metric_impl.dtdc_settlement.remittance_lag_days` | `DATE_DIFF('day', delivery_date, settlement_date)` | `dtdc_settlement` | Use only when both dates are valid. |
| DTDC UTR coverage rate | `metric_impl.dtdc_settlement.utr_coverage_rate` | `COUNT(rows with utr_no or bank_ref_number) / COUNT(settlement rows)` | `dtdc_settlement` | Useful quality/readiness metric. |
| DTDC freight billed via Shiprocket | `metric_impl.dtdc_shiprocket_invoice.freight_billed_amount` | `SUM(shiprocket_invoice.charged_amount)` with DTDC courier filter | `shiprocket_invoice` | Fallback implementation, not native DTDC invoice. |
| DTDC settlement-to-freight matched AWB count | `metric_impl.dtdc_settlement.shiprocket_matched_awb_count` | `COUNT(DISTINCT dtdc_settlement.airwaybill_number)` where AWB matches `shiprocket_invoice.other_id` with DTDC courier filter | `dtdc_settlement` + `shiprocket_invoice` | Validate normalized AWB before joining. |

### 13.5 Formula template candidates

| Template | Formula shape | Use |
|---|---|---|
| `formula_template.sum_amount` | `SUM(amount_column)` | COD remitted, COD collected, COD due, freight billed |
| `formula_template.coverage_rate` | `COUNT(populated_key) / COUNT(total_rows)` | UTR coverage, bank reference coverage |
| `formula_template.date_lag_days` | `DATE_DIFF('day', start_date, end_date)` | Delivery-to-settlement lag |
| `formula_template.gap_amount` | `expected_amount - actual_amount` | COD expected vs remitted gap when expected source exists |

### 13.6 Rule candidates

| Rule | Statement | Severity |
|---|---|---|
| `rule.dtdc_charged_amount_not_freight` | In `dtdc_settlement`, `charged_amount` must not be used as freight billed. | critical |
| `rule.dtdc_invoice_schema_only` | Do not use `dtdc_invoice` for freight metrics while table is schema-only/empty. | critical |
| `rule.dtdc_shiprocket_freight_requires_courier_filter` | DTDC freight via Shiprocket invoice requires explicit DTDC courier partner filter. | high |
| `rule.dtdc_account_scope_external` | Do not infer tenant/group/account scope from this vendor doc; use Account Data Binding. | critical |
| `rule.dtdc_bank_matching_requires_scope` | UTR/bank-reference matching requires bank account scope and Banking KB semantics. | high |
| `rule.dtdc_order_prefix_not_tenant_truth` | Order ID prefix patterns are identifier clues, not tenant or marketplace ownership proof. | medium |

### 13.7 Validation test candidates

| Validation test | Check | Blocks execution? |
|---|---|---|
| `validation.dtdc_no_freight_from_settlement_charged_amount` | Query should not label `dtdc_settlement.charged_amount` as freight. | yes |
| `validation.dtdc_no_dtdc_invoice_metrics_when_schema_only` | Query should not use `dtdc_invoice` for metrics unless coverage status is active. | yes |
| `validation.dtdc_scope_filter_from_account_binding` | Query using tenant/account data should include Account Data Binding-derived filters. | yes |
| `validation.dtdc_bank_match_has_bank_scope` | Bank matching query should include bank account scope and date/amount/reference logic. | yes |
| `validation.dtdc_shiprocket_fallback_has_dtdc_filter` | Shiprocket invoice fallback must filter courier partner to DTDC-like values. | yes |

### 13.8 Query pattern candidates

| Query pattern | Purpose | Required context |
|---|---|---|
| `query_pattern.dtdc_cod_remittance_summary` | Summarize DTDC COD remittance by date, AWB, status, or settlement reference | `dtdc_settlement`, Account Data Binding |
| `query_pattern.dtdc_utr_readiness` | Check UTR/bank-reference coverage in settlement rows | `dtdc_settlement` |
| `query_pattern.dtdc_cod_to_bank_recon` | Match DTDC remittance references to bank credits | `dtdc_settlement`, bank statement, Banking KB, account scope |
| `query_pattern.dtdc_freight_via_shiprocket` | Analyze DTDC freight from Shiprocket invoice fallback | `shiprocket_invoice`, DTDC courier filter, compatible scope |
| `query_pattern.dtdc_remittance_lag` | Calculate delivery-to-settlement lag | `dtdc_settlement.delivery_date`, `settlement_date` |

## 14. Mandatory query rules

- Apply `is_active = true` where available.
- Do not hardcode row counts, group IDs, tenant names, or marketplace account meaning from source profiling.
- Treat `dtdc_settlement.charged_amount` as COD/product/remittance amount, not freight.
- Treat `dtdc_invoice` as schema-only until populated and validated.
- Use `airwaybill_number` as the primary DTDC AWB key.
- Use `utr_no`, `utr_date`, and `bank_ref_number` as bank bridge fields only with bank account scope.
- Use Shiprocket invoice for DTDC freight only with explicit DTDC courier partner filtering and compatible account scope.
- Do not infer marketplace/channel origin solely from order ID prefixes.

## 15. Data-quality and semantic caveats

- Native DTDC freight evidence is unavailable if `dtdc_invoice` is empty.
- `charged_amount`, `cod_amount`, and `cod_due` require separate semantic handling.
- UTR/bank-reference fields may be missing or batch-level.
- Bank matching may require aggregation to reference/batch/date amount grain.
- Source-profile statistics are not stable business truth.

## 16. Supported question patterns

- Which DTDC COD remittances have UTRs?
- Which DTDC AWBs have COD remittance evidence?
- What is the delivery-to-remittance lag for DTDC?
- Why should DTDC freight not be read from `dtdc_invoice`?
- How can DTDC freight be analyzed through Shiprocket invoice fallback?
- Which DTDC COD settlements are not matched to bank credits?

## 17. SQL pattern appendix

### DTDC COD remittance summary

```sql
SELECT
  settlement_date,
  COUNT(*) AS settlement_rows,
  SUM(charged_amount) AS cod_remitted_amount
FROM zs_observe.dtdc_settlement
WHERE is_active = true
  AND transaction_type = 'Remitted'
GROUP BY settlement_date;
```

### DTDC freight fallback through Shiprocket invoice

```sql
SELECT
  ds.airwaybill_number,
  ds.charged_amount AS dtdc_cod_or_remittance_amount,
  si.charged_amount AS freight_billed_amount
FROM zs_observe.dtdc_settlement ds
LEFT JOIN zs_observe.shiprocket_invoice si
  ON ds.airwaybill_number = si.other_id
 AND LOWER(si.courier_partner) LIKE '%dtdc%'
WHERE ds.is_active = true
  AND si.is_active = true;
```

Use Account Data Binding filters in production queries. These examples intentionally omit tenant/account filters.

## 18. Extraction guidance

Expected card families:

```text
Data Understanding: Table, Column, Relationship, Value Profile
Metric Understanding: Metric, Metric Implementation, Formula Template
Reconciliation Understanding: Reconciliation Profile, Reconciliation Unit, Matching Logic, Mismatch Category
Execution Guidance: Query Pattern, Rule, Validation Test
Business Hierarchy: Account Data Binding candidates only where scope fields are explicitly documented
```

Chunk by table block, relationship block, amount semantics block, and rule block. Keep the caveat “DTDC invoice is schema-only” close to all freight-related extraction.
