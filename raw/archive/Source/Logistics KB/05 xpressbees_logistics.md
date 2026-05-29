---
title: XpressBees Logistics Knowledge
version: 3.0
doc_type: logistics_vendor_knowledge
domain: logistics
platform: xpressbees
platform_type: courier
fulfilment_ownership_models:
  - direct_courier
  - low_confidence_native
  - aggregator_routed
schemas:
  - zs_observe
primary_tables:
  - zs_observe.xpressbees_settlement
related_tables:
  - zs_observe.shiprocket_settlement
  - zs_observe.shiprocket_invoice
  - zs_observe.shiprocket_oms
flow_types:
  - cod_remittance
  - indirect_courier_evidence
money_flow_paths:
  - cod_delivery_to_courier_remittance
  - courier_remittance_to_bank
coverage_status: low_confidence_native_with_fallback_preferred
status: draft
owner: finance_data_team
source_documents:
  - Logistics KB Doc.docx
related_docs:
  - logistics_domain_overview.md
  - shiprocket_logistics.md
  - logistics_reconciliation_patterns.md
---

# XpressBees Logistics Knowledge

> Scope note: This is a reusable KB grounding document. It preserves vendor behavior, table semantics, column meanings, join candidates, amount semantics, low-confidence caveats, and extraction guidance. It does **not** define tenant/group ownership, customer-specific account scope, durable marketplace routing, or production filters. Tenant/group/account filters should be resolved through Business Hierarchy, Platform Account, Account Data Binding, Business Scope Set, and Runtime Scope.

---

## 1. How to use this document

Use this document when a question involves XpressBees as a direct courier, as an underlying courier inside an aggregator such as Shiprocket, or as a low-confidence native logistics settlement source.

This document is most useful for:

- checking whether native XpressBees settlement evidence is reliable,
- identifying when Shiprocket fallback evidence should be preferred,
- understanding XpressBees COD/remittance fields,
- creating table, column, relationship, value profile, metric, rule, and query-pattern candidates for ingestion,
- preventing unsafe inference from sparse native data.

Do **not** use this document to decide which tenant, group, marketplace, or seller account uses XpressBees. That belongs to tenant/group context and, where cross-platform routing matters, Business Flow Applicability.

---

## 2. Logistics overview and business context

XpressBees can appear in two ways:

```text
1. Native courier evidence
   XpressBees-specific table exists, but source content marks it as low-confidence because important fields can be sparse.

2. Aggregator-routed evidence
   XpressBees appears as the underlying courier inside a courier aggregator table, especially Shiprocket settlement, invoice, or OMS tables.
```

For KB grounding, treat the native `xpressbees_settlement` table as a **low-confidence native source** until field completeness is validated for the selected runtime scope.

Shiprocket consolidated evidence may be preferred when:

```text
the shipment was routed through Shiprocket,
courier partner identifies XpressBees,
AWB-level fields are populated,
and settlement/invoice evidence exists in Shiprocket tables.
```

---

## 3. Applicability and scope model

XpressBees can map to these generic logistics models:

```text
direct_courier
  Use only when native XpressBees data is reliable for the selected scope.

aggregator_routed
  Use when XpressBees appears as the final courier inside Shiprocket or another aggregator.

low_confidence_native
  Use when native XpressBees table exists but core fields are sparse or incomplete.
```

Scope rules:

- Do not interpret `group_level_id`, seller account, marketplace, or tenant identity from this vendor doc.
- Treat any account/scope fields as Account Data Binding candidates only.
- Do not assume Shiprocket fallback applies unless runtime scope or evidence path supports Shiprocket-routed logistics.
- Do not treat the existence of a native table as proof of complete COD or freight visibility.

---

## 4. Fulfilment ownership and shipping model

Primary models from the source context:

| Model | Meaning for XpressBees |
|---|---|
| `direct_courier` | XpressBees may provide native courier settlement/remittance evidence if the native table is complete enough. |
| `aggregator_routed` | XpressBees may appear as the underlying courier inside Shiprocket evidence. |
| `low_confidence_native` | Native XpressBees table exists, but key fields may be sparse; use with profiling and confidence warnings. |

XpressBees should not be treated as a marketplace fulfilment platform by default. It is a courier/final-mile logistics vendor unless another source explicitly defines a different role.

---

## 5. Operational shipment lifecycle

Native XpressBees operational visibility is limited in the current source. Fields such as `shipping_id`, `service_type`, `shipment_status`, `hub_name`, and `company` may exist but should be profiled before use.

Generic native flow:

```text
order_id / poid
→ shipping_id / AWB candidate
→ shipment_status / service_type
→ delivery_date
→ settlement/remittance row
```

Aggregator fallback flow:

```text
Shiprocket OMS shipment
→ Shiprocket AWB
→ courier partner label = XpressBees
→ Shiprocket invoice and/or Shiprocket settlement evidence
```

---

## 6. Money movement lifecycle

Native XpressBees settlement can theoretically support:

```text
COD shipment
→ XpressBees settlement/remittance row
→ net payment
→ transaction date
→ possible bank bridge, if available outside this table
```

However, because native fields may be sparse, fallback through Shiprocket may be more reliable:

```text
Shiprocket settlement where courier partner identifies XpressBees
→ COD remittance by AWB
→ settlement date / delivered date
→ bank bridge only if available through downstream banking/reconciliation docs
```

Do not infer bank credit from XpressBees settlement alone. Bank matching requires bank-statement semantics and account binding from banking context.

---

## 7. Business objects and identifiers

| Object | XpressBees field examples | Notes |
|---|---|---|
| XpressBees order/reference | `order_id` | Native source order/reference candidate. |
| Shipment / AWB candidate | `shipping_id` | Use as AWB bridge only when populated and validated. |
| Purchase order candidate | `poid` | Supporting identifier; do not use as primary join without validation. |
| Service type | `service_type` | May identify COD/prepaid/service semantics when populated. |
| Shipment status | `shipment_status` | Operational state candidate; values require profiling. |
| Transaction type | `transaction_type` | Settlement/remittance classification candidate. |
| Remittance / transaction date | `transaction_date` | Date candidate for settlement/remittance analysis. |
| Delivery date | `delivery_date` | Date candidate for delivered-to-remitted lag. |
| Net payment | `net_payment` | COD/remitted amount candidate when populated. |
| Operational context | `hub_name`, `company` | Context fields; often sparse in source context. |

---

## 8. Table family overview

| Table | Business role | Coverage status |
|---|---|---|
| `zs_observe.xpressbees_settlement` | Native XpressBees COD settlement/remittance candidate. | `low_confidence_native`; must be profiled before analytical use. |
| `zs_observe.shiprocket_settlement` | Fallback COD evidence when courier partner identifies XpressBees and runtime context supports Shiprocket routing. | `fallback_preferred` where Shiprocket evidence is applicable. |
| `zs_observe.shiprocket_invoice` | Fallback freight evidence when courier partner identifies XpressBees and AWB can be linked. | Use Shiprocket amount semantics. |
| `zs_observe.shiprocket_oms` | Fallback operational shipment/AWB/courier evidence for Shiprocket-routed XpressBees shipments. | Use Shiprocket status/value semantics. |

---

## 9. Entity relationships and join paths

### 9.1 Native XpressBees path

Use only when populated and validated:

```text
xpressbees_settlement.shipping_id
→ AWB / shipment bridge
→ source order/shipment context
```

Supporting identifiers:

```text
xpressbees_settlement.order_id
xpressbees_settlement.poid
```

### 9.2 Shiprocket fallback path

Use when XpressBees appears as underlying courier in Shiprocket evidence:

```text
shiprocket_oms.awb_code
→ shiprocket_invoice.other_id
→ shiprocket_settlement.awb_number
```

Filter/segment by normalized courier partner label:

```text
courier partner contains XpressBees / Xpress Bees / xpress
```

### 9.3 Native vs fallback comparison path

Use only for diagnostics and coverage validation:

```text
xpressbees_settlement.shipping_id
↔ shiprocket_oms.awb_code
↔ shiprocket_settlement.awb_number
```

Do not assume equality unless identifiers are normalized and non-null.

---

## 10. Metrics and business definitions

| Metric | Definition | Preferred evidence |
|---|---|---|
| XpressBees native populated record count | Count of native settlement rows with key fields populated. | `xpressbees_settlement` |
| XpressBees native data completeness | Share of rows with non-null AWB/status/net-payment fields. | `xpressbees_settlement` |
| XpressBees native COD remitted amount | COD/remittance amount for XpressBees shipments from native settlement. | Native `net_payment` only when reliable. |
| XpressBees fallback COD amount | COD amount from Shiprocket settlement for XpressBees courier label. | `shiprocket_settlement` |
| XpressBees fallback freight billed amount | Freight billed for XpressBees-labelled Shiprocket shipments. | `shiprocket_invoice` |
| XpressBees unmatched AWB count | XpressBees-labelled AWBs without expected settlement/invoice evidence. | Shiprocket OMS vs invoice/settlement joins |
| Native-vs-fallback coverage gap | Difference between native XpressBees settlement coverage and Shiprocket fallback coverage. | Native + Shiprocket fallback |

---

## 11. Reconciliation playbook

Valid XpressBees reconciliation use cases:

1. Native XpressBees settlement quality profiling.
2. XpressBees COD remittance analysis through Shiprocket fallback.
3. XpressBees AWB to Shiprocket invoice/settlement bridge.
4. Native-vs-fallback comparison when both sources are populated.
5. Courier COD-to-bank reconciliation only when a valid bank bridge and bank account scope are supplied by related banking/reconciliation docs.

Invalid or unsafe use cases:

- Treating native XpressBees data as complete without profiling.
- Computing final COD totals from null-heavy native rows.
- Inferring direct bank settlement from `net_payment` alone.
- Treating Shiprocket-routed evidence as universally applicable to all XpressBees shipments.
- Treating courier label normalization as account identity.

### 11.1 Reconciliation variants

| Variant name | Base profile | Variant reason | Mismatch category overrides |
|---|---|---|---|
| xpressbees_native_low_confidence_cod | `reconciliation_profile.cod_reconciliation` | Native XpressBees settlement is null-heavy/low-confidence; COD reconciliation requires field-completeness profiling and a Shiprocket fallback when native rows are too sparse. | `mismatch_category.low_confidence_native_data`, `mismatch_category.missing_cod_remittance` |
| xpressbees_freight_via_shiprocket | `reconciliation_profile.shipment_to_invoice_reconciliation` | XpressBees has no native invoice; freight charges must be bridged via `zs_observe.shiprocket_invoice` rows where XpressBees is the courier partner. | `mismatch_category.missing_invoice`, `mismatch_category.schema_only_source` |

---

## 12. Table-specific curated knowledge

### 12.1 Table: `zs_observe.xpressbees_settlement`

#### Business purpose

Native XpressBees settlement/remittance candidate table. It may support COD/remittance analysis if key identifiers, status fields, and payment fields are populated.

#### Grain

Intended grain is one settlement/remittance record per shipment/AWB or shipment reference. Because source content flags sparsity, grain must be validated before use.

#### Table status and coverage

Coverage status: `low_confidence_native`.

Do not use source row counts as durable KB truth. Field completeness must be profiled at runtime or during ingestion validation.

#### Applicability and account-binding notes

Any account/scope columns should be treated as Account Data Binding candidates only. This table does not by itself define tenant, group, marketplace, seller account, or bank account identity.

#### Critical filters

- Use `is_active = true` where the field exists.
- Prefer rows with populated `shipping_id`, `service_type`, `shipment_status`, `transaction_type`, and `net_payment` for native analysis.
- Do not use null-heavy rows for AWB-level reconciliation without fallback evidence.
- Do not classify COD/non-COD without confirmed `service_type` or `transaction_type` semantics.

#### Key identifiers

| Field | Business meaning | Semantic roles | Caveat |
|---|---|---|---|
| `order_id` | Native XpressBees order/reference ID. | identifier, join_candidate | Not enough for marketplace/customer linkage without source mapping. |
| `shipping_id` | AWB/shipping ID candidate. | identifier, reconciliation_key, join_key | Often sparse in source context; profile before use. |
| `poid` | Purchase order/reference candidate. | identifier | Supporting key only; validate before joining. |

#### Operational fields

| Field | Business meaning | Semantic roles | Caveat |
|---|---|---|---|
| `service_type` | Service/payment mode candidate, such as COD when populated. | dimension, filter, value_profile_candidate | Values must be profiled. |
| `shipment_status` | Shipment lifecycle state candidate. | status, filter, value_profile_candidate | Do not infer delivered/RTO without value profile. |
| `hub_name` | Hub/location context. | dimension | Often sparse; diagnostic use only unless profiled. |
| `company` | Operational/company context. | dimension | Not tenant identity unless confirmed elsewhere. |

#### Financial fields

| Field | Business meaning | Semantic roles | Default aggregation | Caveat |
|---|---|---|---|---|
| `transaction_type` | Settlement transaction category candidate. | dimension, filter, value_profile_candidate | none | Table-specific value meaning required. |
| `net_payment` | Net COD/remittance amount candidate when populated. | measure, financial_amount | `SUM` | Do not use when null-heavy without completeness check. |
| `transaction_date` | Transaction/remittance date candidate. | date | none | Recommended for settlement/remittance timing if populated. |
| `delivery_date` | Delivery date candidate. | date | none | Useful for remittance lag if populated. |

#### Relationships and joins

- `shipping_id` may join to AWB/shipment evidence if populated.
- `shipping_id` may be compared against `shiprocket_oms.awb_code` or `shiprocket_settlement.awb_number` only when XpressBees appears via Shiprocket and identifiers are normalized.
- `order_id` and `poid` should not be used as primary reconciliation keys unless validated against source order systems.

#### Reconciliation role

Low-confidence native COD/remittance evidence. Use for:

```text
native field profiling
native-vs-fallback comparison
supporting evidence
```

Use as primary evidence only after completeness validation.

#### Caveats

- Core fields can be sparse.
- Native table may undercount actual XpressBees-routed shipments.
- Shiprocket fallback can be more reliable for Shiprocket-routed XpressBees shipments.
- Do not compare native AWB-level rows to bank credits without aggregation and bank bridge.

#### Example questions

- Is native XpressBees settlement reliable enough to use?
- Which XpressBees rows have populated AWB and net payment?
- How much XpressBees COD is visible through native data versus Shiprocket fallback?
- Which XpressBees-labelled Shiprocket AWBs are missing native settlement evidence?

---

## 13. Mandatory query rules

### 13.1 Native table confidence rules

- Treat `xpressbees_settlement` as low-confidence by default.
- Run field completeness checks before using native totals.
- Do not use `net_payment` totals unless key identifiers and amount fields are sufficiently populated.
- Do not assume `shipping_id` is a reliable AWB key when null or malformed.

### 13.2 Fallback rules

- Prefer Shiprocket fallback only when runtime context supports Shiprocket-routed evidence.
- Normalize courier labels before identifying XpressBees in Shiprocket tables.
- Use Shiprocket table semantics for Shiprocket fallback amounts; do not import native XpressBees amount semantics into Shiprocket fields.

### 13.3 Scope and account-binding rules

- Resolve account filters through Account Data Binding.
- Do not treat `company`, `hub_name`, or courier label as tenant/account identity.
- Do not generalize any group/account field across tables.

### 13.4 Reconciliation rules

- Aggregate to the correct grain before comparing settlement to bank credit.
- Do not perform COD-to-bank reconciliation unless a bank bridge and bank account scope are available.
- Classify missing native evidence separately from missing courier remittance.

---

## 14. Data-quality and semantic caveats

- Native key fields may be null or sparse.
- `net_payment` is useful only when populated and tied to a valid shipment/remittance record.
- Fallback through Shiprocket depends on courier partner normalization.
- Row counts and percentages from source profiling are not durable KB truth.
- Use the durable KB rule: **profile completeness before using native XpressBees data for metrics or reconciliation**.

---

## 15. Supported question patterns

- Is native XpressBees settlement reliable enough for reconciliation?
- Which XpressBees COD records are available through Shiprocket?
- Which XpressBees shipments have missing AWB or net payment in native data?
- Should I use XpressBees native table or Shiprocket fallback?
- What is the completeness of XpressBees settlement fields?
- Which Shiprocket AWBs handled by XpressBees have no settlement evidence?
- Can XpressBees COD be reconciled to bank credits for this runtime scope?

---

## 16. SQL pattern appendix

SQL examples are evidence patterns only. Production queries must inject account filters through Account Data Binding.

```sql
-- XpressBees via Shiprocket fallback
SELECT
  ss.awb_number,
  ss.courier_partner,
  ss.charged_amount AS cod_amount,
  ss.delivered_date,
  ss.settlement_date
FROM zs_observe.shiprocket_settlement ss
WHERE ss.is_active = true
  AND LOWER(ss.courier_partner) LIKE '%xpress%';
```

```sql
-- Native XpressBees field completeness check
SELECT
  COUNT(*) AS rows_checked,
  SUM(CASE WHEN shipping_id IS NOT NULL THEN 1 ELSE 0 END) AS rows_with_shipping_id,
  SUM(CASE WHEN net_payment IS NOT NULL THEN 1 ELSE 0 END) AS rows_with_net_payment,
  SUM(CASE WHEN shipment_status IS NOT NULL THEN 1 ELSE 0 END) AS rows_with_status
FROM zs_observe.xpressbees_settlement
WHERE is_active = true;
```

---

## 17. Extraction guidance

Extract XpressBees as:

```text
Platform: XpressBees
Platform type: courier
Coverage: low_confidence_native_with_fallback_preferred
Primary native table: zs_observe.xpressbees_settlement
Fallback evidence: Shiprocket OMS / invoice / settlement when courier partner identifies XpressBees
```

Preserve the negative and confidence knowledge:

```text
Native table exists, but should not be used as complete evidence until profiled.
Shiprocket fallback can be preferred only when runtime context supports Shiprocket-routed evidence.
```

---

## 18. Ingestion-compatible extraction sections

### 18.1 Column-level information candidates

#### Table: `zs_observe.xpressbees_settlement`

| Column | Business meaning | Semantic roles | Default aggregation | Filtering/grouping guidance | Reconciliation usage | Caveats |
|---|---|---|---|---|---|---|
| `order_id` | Native XpressBees order/reference ID. | identifier, join_candidate | none | Filter only for exact lookup. | Supporting key only. | Does not prove marketplace/customer identity. |
| `shipping_id` | AWB/shipping ID candidate. | identifier, join_key, reconciliation_key | none | Filter for AWB-level lookup when populated. | Primary native shipment bridge if populated. | Sparse; profile before use. |
| `poid` | Purchase order/reference candidate. | identifier | none | Exact lookup only. | Supporting key. | Validate before joins. |
| `service_type` | Service/payment mode candidate. | dimension, filter, value_profile_candidate | none | Group/filter after value profiling. | Helps classify COD/non-COD. | Values and nulls require profiling. |
| `shipment_status` | Shipment lifecycle state candidate. | status, dimension, filter, value_profile_candidate | none | Use after value profiling. | Helps classify delivered/RTO/pending if populated. | Do not infer delivered without profile. |
| `transaction_type` | Settlement transaction category candidate. | dimension, filter, value_profile_candidate | none | Use after value profiling. | Helps identify COD/remittance rows. | Meaning is table-specific. |
| `net_payment` | Net remittance/COD payment candidate. | measure, financial_amount | `SUM` | Do not group by. | Compare to expected COD/remittance after completeness check. | Null-heavy rows should be excluded or flagged. |
| `transaction_date` | Transaction/remittance date candidate. | date | none | Recommended settlement date when populated. | Lag and reconciliation window. | Validate date format and timezone. |
| `delivery_date` | Delivery date candidate. | date | none | Use for delivery-to-remittance lag when populated. | Lag analysis. | May be null or inconsistent. |
| `hub_name` | Hub/location context. | dimension | none | Diagnostic grouping only. | Usually not a match key. | Sparse; not account identity. |
| `company` | Company/source context. | dimension | none | Diagnostic grouping only. | Usually not a match key. | Not tenant identity without external mapping. |
| `is_active` | Active/current row flag if present. | filter, rule_guardrail | none | Use `is_active = true` where present. | Prevents inactive-row leakage. | Only apply where column exists. |

#### Related fallback columns from Shiprocket tables

| Table | Column | Business meaning | Reuse guidance |
|---|---|---|---|
| `shiprocket_oms` | `awb_code` | Shipment/AWB key in Shiprocket OMS. | Use as fallback operational bridge for Shiprocket-routed XpressBees shipments. |
| `shiprocket_oms` | courier label columns such as `courier_company` / equivalent | Underlying courier label. | Normalize labels to identify XpressBees. |
| `shiprocket_invoice` | `other_id` | AWB/reference used in invoice evidence. | Join to Shiprocket OMS AWB where valid. |
| `shiprocket_invoice` | `courier_partner` | Courier label in invoice evidence. | Filter/segment XpressBees after normalization. |
| `shiprocket_invoice` | `charged_amount` | Shiprocket invoice freight amount. | Use Shiprocket amount semantics, not XpressBees native semantics. |
| `shiprocket_settlement` | `awb_number` | AWB/reference used in settlement evidence. | Join to Shiprocket OMS AWB where valid. |
| `shiprocket_settlement` | `courier_partner` | Courier label in settlement evidence. | Filter/segment XpressBees after normalization. |
| `shiprocket_settlement` | `charged_amount` | Shiprocket settlement COD/remittance amount. | Use Shiprocket settlement semantics. |

---

### 18.2 Relationship candidates

| Relationship candidate | Source | Target | Join / match keys | Type | Cardinality expectation | Confidence | Caveats |
|---|---|---|---|---|---|---|---|
| Native XpressBees settlement to shipment context | `xpressbees_settlement` | Source order/shipment table | `shipping_id` ↔ AWB/shipment key | reconciliation_relation | unknown | low | Use only when `shipping_id` is populated and normalized. |
| Native XpressBees to Shiprocket OMS fallback comparison | `xpressbees_settlement` | `shiprocket_oms` | `shipping_id` ↔ `awb_code` | diagnostic_relation | unknown | low-medium | Only valid for Shiprocket-routed shipments. |
| Shiprocket OMS to Shiprocket invoice for XpressBees-labelled shipments | `shiprocket_oms` | `shiprocket_invoice` | `awb_code` ↔ `other_id` | join / reconciliation_relation | one-to-many possible | medium-high | Use Shiprocket doc for exact semantics. |
| Shiprocket OMS to Shiprocket settlement for XpressBees-labelled shipments | `shiprocket_oms` | `shiprocket_settlement` | `awb_code` ↔ `awb_number` | reconciliation_relation | one-to-zero-or-many | medium-high | Segment by normalized courier partner. |
| Shiprocket invoice to Shiprocket settlement by AWB | `shiprocket_invoice` | `shiprocket_settlement` | `other_id` ↔ `awb_number` | diagnostic_relation | many-to-many possible | medium | Pre-aggregate to AWB before comparison. |

---

### 18.3 Value profile candidates

| Table | Column | Candidate values / groups | Business meaning | Null handling | Extraction note |
|---|---|---|---|---|---|
| `xpressbees_settlement` | `service_type` | COD, prepaid/other, unknown | Service/payment mode classification. | Null means service mode unresolved. | Profile values before using as filter. |
| `xpressbees_settlement` | `shipment_status` | Delivered, RTO, in_transit, pending, unknown | Shipment lifecycle state. | Null means status unresolved. | Do not hardcode value list until profiled. |
| `xpressbees_settlement` | `transaction_type` | COD, adjustment/other, unknown | Settlement row category. | Null means transaction class unresolved. | Table-specific semantics only. |
| `shiprocket_settlement` | `courier_partner` | XpressBees-like labels | Underlying courier identification through aggregator. | Null means courier cannot be segmented. | Normalize `xpress`, `xpressbees`, `xpress bees`. |
| `shiprocket_invoice` | `courier_partner` | XpressBees-like labels | Freight courier identification through aggregator. | Null means courier cannot be segmented. | Use fallback only when label exists. |

---

### 18.4 Metric candidates

| Metric candidate | Business definition | Metric type | Default aggregation | Evidence source | Caveats |
|---|---|---|---|---|---|
| `metric.xpressbees_native_data_completeness` | Share of native XpressBees rows with required key fields populated. | percentage | ratio | `xpressbees_settlement` | Used before trusting native metrics. |
| `metric.xpressbees_native_cod_remitted_amount` | Sum of native `net_payment` for reliable COD/remittance rows. | amount | SUM | `xpressbees_settlement` | Low-confidence unless completeness passes. |
| `metric.xpressbees_fallback_cod_remitted_amount` | Sum of COD/remittance amount from Shiprocket settlement for XpressBees-labelled courier rows. | amount | SUM | `shiprocket_settlement` | Valid only for Shiprocket-routed evidence. |
| `metric.xpressbees_fallback_freight_billed_amount` | Sum of Shiprocket invoice freight for XpressBees-labelled courier rows. | amount | SUM | `shiprocket_invoice` | Use Shiprocket invoice amount semantics. |
| `metric.xpressbees_unmatched_awb_count` | Count of XpressBees-labelled AWBs missing expected invoice or settlement evidence. | count | COUNT_DISTINCT | Shiprocket OMS + invoice/settlement | Requires AWB normalization and correct grain. |
| `metric.xpressbees_delivery_to_remittance_lag` | Difference between delivery date and settlement/remittance date. | duration | AVG / distribution | native or fallback | Use only where both dates are populated. |

---

### 18.5 Metric implementation candidates

| Metric implementation candidate | Metric | Applicability | Formula / calculation description | Required columns | Required rules |
|---|---|---|---|---|---|
| `metric_impl.xpressbees_settlement.native_populated_record_count` | XpressBees native populated record count | Native XpressBees table | Count active rows where `shipping_id`, `net_payment`, and `shipment_status` are all populated. | `shipping_id`, `net_payment`, `shipment_status`, `is_active` | Active-row rule; null profiling rule. |
| `metric_impl.xpressbees_settlement.native_data_completeness` | XpressBees native data completeness | Native XpressBees table | Count rows with populated key fields divided by total active rows checked. | `shipping_id`, `net_payment`, `shipment_status`, `is_active` | Active-row rule; null profiling rule. |
| `metric_impl.xpressbees_settlement.native_cod_remitted_amount` | XpressBees native COD remitted amount | Native table after completeness validation | Sum `net_payment` for rows classified as COD/remittance and sufficiently populated. | `net_payment`, `transaction_type`, `service_type`, `is_active` | Native confidence rule; COD classification rule. |
| `metric_impl.shiprocket_settlement.xpressbees_fallback_cod_amount` | XpressBees fallback COD amount | Shiprocket fallback where courier partner identifies XpressBees | Sum Shiprocket settlement COD/remittance amount for XpressBees-labelled courier rows. | `awb_number`, `courier_partner`, `charged_amount`, `is_active` | Courier label normalization; Shiprocket amount semantics. |
| `metric_impl.shiprocket_invoice.xpressbees_fallback_freight_amount` | XpressBees fallback freight billed amount | Shiprocket fallback invoice evidence | Sum Shiprocket invoice freight amount for XpressBees-labelled courier rows. | `other_id`, `courier_partner`, `charged_amount`, `is_active` | Courier label normalization; invoice amount semantics. |
| `metric_impl.shiprocket_oms.xpressbees_unmatched_awb_count` | XpressBees unmatched AWB count | Shiprocket-routed evidence | Count distinct XpressBees-labelled AWBs in OMS without matching invoice/settlement evidence. | `awb_code`, courier label columns | AWB grain rule; left-join missing-evidence rule. |
| `metric_impl.xpressbees_settlement.native_vs_fallback_coverage_gap` | Native-vs-fallback coverage gap | Native + Shiprocket fallback evidence | Native XpressBees AWB count minus Shiprocket fallback AWB count for the same scope/period (or amount-side analogue). | `shipping_id`, Shiprocket `awb_number`, `courier_partner` | Native confidence rule; courier label normalization. |

---

### 18.6 Formula template candidates

| Formula template | Plain-English formula | SQL-style pattern | Applies to |
|---|---|---|---|
| `formula_template.field_completeness_rate` | Rows with populated required field divided by rows checked. | `SUM(CASE WHEN field IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*)` | Native data completeness metrics. |
| `formula_template.filtered_amount_sum` | Sum an amount after status, account, and semantic filters. | `SUM(amount_column)` with required filters | COD/remitted/freight amount metrics. |
| `formula_template.unmatched_key_count` | Count keys on expected side without corresponding actual-side records. | `COUNT_DISTINCT(expected.key) WHERE actual.key IS NULL` | Missing invoice/settlement checks. |
| `formula_template.date_lag_days` | Difference between later process date and earlier process date. | `DATE_DIFF('day', start_date, end_date)` | Delivery-to-remittance lag. |
| `formula_template.native_vs_fallback_gap` | Difference between native metric and fallback metric for same courier label/scope. | `native_amount - fallback_amount` | Coverage gap diagnostics. |

---

### 18.7 Rule candidates

| Rule candidate | Rule statement | Severity | Applies to | Failure mode |
|---|---|---|---|---|
| `rule.xpressbees_native_low_confidence_default` | Treat native XpressBees table as low-confidence until field completeness passes. | high | `xpressbees_settlement` metrics/recon | Overstates or understates COD/remittance. |
| `rule.xpressbees_require_awb_for_native_recon` | Do not perform AWB-level native reconciliation when `shipping_id` is null or malformed. | critical | Native reconciliation | Invalid joins and false missing matches. |
| `rule.xpressbees_use_shiprocket_fallback_only_when_applicable` | Use Shiprocket fallback only when runtime scope/evidence supports Shiprocket-routed shipments. | high | Fallback metrics/recon | Mixes unrelated courier/account evidence. |
| `rule.xpressbees_normalize_courier_label` | Normalize XpressBees courier labels before filtering Shiprocket fallback rows. | medium | Fallback query patterns | Misses rows due to spelling/case variations. |
| `rule.xpressbees_account_filters_from_binding` | Apply tenant/account filters only through Account Data Binding. | critical | All executable patterns | Cross-account leakage. |
| `rule.xpressbees_no_bank_inference_without_bridge` | Do not infer bank receipt from XpressBees remittance evidence without bank bridge and banking context. | critical | COD-to-bank reconciliation | False cash-realization claim. |

---

### 18.8 Validation test candidates

| Validation test candidate | Test condition | Blocking? | Linked rule |
|---|---|---|---|
| `validation.xpressbees_native_completeness_present` | Native metric/recon query includes a completeness check or uses only populated required fields. | yes | `rule.xpressbees_native_low_confidence_default` |
| `validation.xpressbees_native_awb_not_null_for_recon` | Native AWB-level reconciliation filters or handles null `shipping_id`. | yes | `rule.xpressbees_require_awb_for_native_recon` |
| `validation.xpressbees_fallback_courier_filter_present` | Shiprocket fallback query contains normalized XpressBees courier-label filtering. | yes | `rule.xpressbees_normalize_courier_label` |
| `validation.xpressbees_account_binding_present` | Query uses Account Data Binding filters for selected runtime accounts/tables. | yes | `rule.xpressbees_account_filters_from_binding` |
| `validation.xpressbees_no_direct_bank_claim` | Output does not claim bank receipt unless bank-side evidence exists. | yes | `rule.xpressbees_no_bank_inference_without_bridge` |
| `validation.xpressbees_amount_semantics_checked` | Query uses native `net_payment` or Shiprocket `charged_amount` according to table-specific semantics. | yes | amount semantics rules |

---

### 18.9 Query pattern candidates

| Query pattern candidate | Intent supported | Required tables | Required joins / filters | Output expectation |
|---|---|---|---|---|
| `query_pattern.xpressbees_native_quality_profile` | Assess whether native XpressBees table is usable. | `xpressbees_settlement` | `is_active = true`; non-null checks for key fields. | Completeness rates, confidence, recommended usage. |
| `query_pattern.xpressbees_shiprocket_fallback_cod_summary` | Compute XpressBees COD from Shiprocket fallback. | `shiprocket_settlement` | normalized courier label filter; account binding; date filter. | COD amount, AWB count, settlement date breakdown. |
| `query_pattern.xpressbees_shiprocket_fallback_freight_summary` | Compute XpressBees freight from Shiprocket fallback. | `shiprocket_invoice` | normalized courier label filter; account binding; date filter. | Freight amount, AWB count, invoice date breakdown. |
| `query_pattern.xpressbees_native_vs_fallback_coverage` | Compare native XpressBees evidence with Shiprocket fallback. | `xpressbees_settlement`, Shiprocket tables | AWB normalization; left/full join by AWB. | Native-only, fallback-only, matched, confidence flags. |
| `query_pattern.xpressbees_missing_settlement_by_awb` | Find XpressBees-labelled AWBs missing settlement evidence. | `shiprocket_oms`, `shiprocket_settlement` | OMS AWB left join settlement AWB; courier filter. | Missing AWBs with operational status. |
| `query_pattern.xpressbees_delivery_to_remittance_lag` | Measure lag from delivery to settlement/remittance. | native or fallback tables | populated delivery and settlement dates. | Lag days by AWB/date bucket. |

