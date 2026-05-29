---
title: Shadowfax and Ecom Express Logistics Knowledge
version: 3.0
doc_type: logistics_vendor_knowledge
domain: logistics
platforms:
  - shadowfax
  - ecom_express
platform_type: indirect_courier
fulfilment_ownership_models:
  - reverse_only
  - indirect_only
  - aggregator_routed
schemas:
  - zs_observe
primary_tables: []
related_tables:
  - zs_observe.shiprocket_oms
  - zs_observe.shiprocket_invoice
  - zs_observe.shiprocket_settlement
flow_types:
  - reverse_logistics
  - shipment_tracking
  - indirect_courier_evidence
money_flow_paths:
  - order_to_shipment
  - shipment_to_freight_invoice
  - cod_delivery_to_courier_remittance
coverage_status: indirect_only
status: draft
owner: finance_data_team
source_documents:
  - Logistics KB Doc.docx
related_docs:
  - logistics_domain_overview.md
  - shiprocket_logistics.md
  - logistics_reconciliation_patterns.md
---

# Shadowfax and Ecom Express Logistics Knowledge

> Scope note: This is a reusable KB grounding document. It preserves indirect courier behavior, negative knowledge, evidence paths, relationship candidates, column-level extraction candidates, value profiles, metrics, rules, and query patterns. It does **not** define tenant/group ownership, customer-specific account scope, durable marketplace routing, or direct native courier facts. Tenant/group/account filters should be resolved through Business Hierarchy, Platform Account, Account Data Binding, Business Scope Set, and Runtime Scope.

---

## 1. How to use this document

Use this document when Shadowfax or Ecom Express appears as a courier partner or courier label, but no dedicated native Shadowfax/Ecom table exists in the current KB source.

This document is most useful for:

- identifying indirect courier evidence through Shiprocket tables,
- preventing unsafe creation of native Shadowfax/Ecom facts,
- segmenting Shiprocket operational, freight, or COD records by courier partner,
- understanding what can and cannot be inferred for indirect couriers,
- creating ingestion-ready columns, relationships, value profiles, metrics, rules, validation tests, and query patterns.

Do **not** use this document to infer direct Shadowfax/Ecom account ownership, direct freight invoices, direct COD remittance, or direct bank receipt.

---

## 2. Logistics overview and business context

The source describes Shadowfax and Ecom Express as couriers visible through Shiprocket-related evidence rather than dedicated native tables.

Current interpretation:

| Vendor | Current KB role | Evidence source |
|---|---|---|
| Shadowfax | `reverse_only` / `indirect_only` | Shiprocket OMS-style courier/status/reverse/QC evidence. |
| Ecom Express | `indirect_only` / `aggregator_routed` | Shiprocket invoice/settlement/OMS-style courier labels. |

Because no dedicated native tables are documented, these vendors should be treated as `indirect_only` unless new source tables are added and curated.

---

## 3. Applicability and scope model

Use Shiprocket or another documented aggregator/source table as the evidence source when Shadowfax/Ecom appears as a courier partner.

Rules:

- Do not create fake native Shadowfax/Ecom tables.
- Do not infer direct Shadowfax/Ecom settlement or freight evidence without native tables or explicit source fields.
- Do not infer bank bridge or cash receipt from courier label alone.
- Do not treat indirect courier label as platform account identity.
- Resolve account filters through the source table's Account Data Binding, usually the aggregator/source account.

---

## 4. Fulfilment ownership and shipping model

| Vendor | Generic model | Meaning |
|---|---|---|
| Shadowfax | `reverse_only` / `indirect_only` | Appears as reverse, QC, return, or courier label evidence in source/aggregator data. |
| Ecom Express | `indirect_only` / `aggregator_routed` | Appears as underlying courier label in aggregator shipment, invoice, or settlement evidence. |

These vendors should be modeled as **indirect evidence participants**, not standalone native platforms, until dedicated native source tables are documented.

---

## 5. Operational shipment lifecycle

Operational evidence should come from Shiprocket OMS or another documented aggregator/source table where the courier partner label identifies Shadowfax or Ecom Express.

Generic indirect operational flow:

```text
order/shipment in aggregator OMS
→ AWB/tracking reference
→ courier partner label = Shadowfax or Ecom Express
→ shipment status / delivery / return / reverse/QC fields from aggregator
```

For Shadowfax, reverse/QC interpretation must be validated using status, transaction type, return/RTO fields, or source-specific labels.

For Ecom Express, operational segmentation depends on courier label normalization.

---

## 6. Money movement lifecycle

No dedicated native money movement table is documented for Shadowfax or Ecom Express in the current source.

Possible indirect evidence:

```text
Shiprocket invoice rows where courier partner identifies Shadowfax/Ecom
Shiprocket settlement rows where courier partner identifies Shadowfax/Ecom
```

Money movement should be interpreted through the **source table's semantics**:

```text
Shiprocket invoice → freight evidence
Shiprocket settlement → COD/remittance evidence
```

If no invoice/settlement row exists, do not infer freight, COD remittance, payout, UTR, or bank receipt for Shadowfax/Ecom.

---

## 7. Business objects and identifiers

| Object | Indirect field source | Notes |
|---|---|---|
| Shipment / AWB | `shiprocket_oms.awb_code` | Operational shipment key when Shiprocket is evidence source. |
| Courier partner | `shiprocket_oms.courier_company`, `fulfilment_channel`, `master_courier`, or equivalent courier label fields | Normalize labels before classification. |
| Freight evidence | `shiprocket_invoice.other_id`, `shiprocket_invoice.courier_partner`, `shiprocket_invoice.charged_amount` | Use Shiprocket invoice semantics. |
| COD/remittance evidence | `shiprocket_settlement.awb_number`, `shiprocket_settlement.courier_partner`, `shiprocket_settlement.charged_amount` | Use Shiprocket settlement semantics. |
| Reverse/QC evidence | Shiprocket transaction/status/NDR/return fields | Shadowfax reverse/QC classification needs value profiling. |
| Bank bridge | Not directly documented for native Shadowfax/Ecom | Requires banking/reconciliation context and source evidence. |

---

## 8. Table family overview

| Table | Role | Coverage status |
|---|---|---|
| `zs_observe.shiprocket_oms` | Indirect operational shipment, courier label, status, reverse/RTO/QC evidence. | Source table; use Shiprocket account binding. |
| `zs_observe.shiprocket_invoice` | Possible indirect freight evidence when courier label identifies Shadowfax/Ecom. | Source table; use Shiprocket invoice semantics. |
| `zs_observe.shiprocket_settlement` | Possible indirect COD/remittance evidence when courier label identifies Shadowfax/Ecom. | Source table; use Shiprocket settlement semantics. |

No dedicated native Shadowfax or Ecom Express table is documented in the current source.

---

## 9. Entity relationships and join paths

Generic Shiprocket indirect chain:

```text
shiprocket_oms.awb_code
→ shiprocket_invoice.other_id
→ shiprocket_settlement.awb_number
```

Segment using normalized courier labels:

```text
Shadowfax-style labels
Ecom Express / Ecom-style labels
```

Interpret amount fields through source table semantics:

```text
shiprocket_invoice.charged_amount = freight amount candidate
shiprocket_settlement.charged_amount = COD/remittance amount candidate
```

Do not join to native Shadowfax/Ecom tables unless such tables are added and curated later.

---

## 10. Metrics and business definitions

| Metric | Definition | Evidence source |
|---|---|---|
| Shadowfax indirect shipment count | Count of source/aggregator shipments where courier label identifies Shadowfax. | `shiprocket_oms` |
| Shadowfax reverse/QC shipment count | Count of Shadowfax-labelled shipments where status/transaction fields indicate reverse, return, QC, or RTO. | `shiprocket_oms` |
| Ecom indirect shipment count | Count of source/aggregator shipments where courier label identifies Ecom Express. | `shiprocket_oms` |
| Indirect courier freight billed amount | Freight amount from source/aggregator invoice rows for Shadowfax/Ecom labels. | `shiprocket_invoice` |
| Indirect courier COD remitted amount | COD/remittance amount from source/aggregator settlement rows for Shadowfax/Ecom labels. | `shiprocket_settlement` |
| Indirect courier missing freight evidence count | Courier-labelled AWBs in OMS without invoice evidence. | OMS → invoice join |
| Indirect courier missing COD evidence count | Courier-labelled COD/delivered AWBs without settlement evidence. | OMS → settlement join |
| Native coverage status | Whether a dedicated native table exists. | KB metadata / negative knowledge |

---

## 11. Reconciliation playbook

Valid use cases:

1. Segment Shiprocket shipments by Shadowfax or Ecom courier labels.
2. Analyze reverse/QC or return-oriented Shadowfax evidence where status fields support it.
3. Analyze indirect freight billed when Shiprocket invoice rows carry Shadowfax/Ecom courier labels.
4. Analyze indirect COD/remittance when Shiprocket settlement rows carry Shadowfax/Ecom courier labels.
5. Track missing invoice or settlement evidence for indirect courier-labelled AWBs.
6. Preserve negative knowledge that native direct reconciliation is unavailable until native tables are added.

Invalid use cases:

- Direct Shadowfax COD-to-bank reconciliation without native settlement or bank bridge evidence.
- Direct Ecom Express freight invoice reconciliation without native invoice or aggregator invoice evidence.
- Assuming indirect courier label implies direct platform account relationship.
- Treating reverse/QC classification as durable without status/value-profile validation.
- Creating direct vendor facts from Shiprocket evidence without stating the evidence source.

### 11.1 Reconciliation variants

| Variant name | Base profile | Variant reason | Mismatch category overrides |
|---|---|---|---|
| shadowfax_indirect_freight | `reconciliation_profile.shipment_to_invoice_reconciliation` | No native Shadowfax invoice exists; freight reconciliation is indirect-only via `zs_observe.shiprocket_invoice` rows carrying a Shadowfax courier label. | `mismatch_category.missing_invoice`, `mismatch_category.schema_only_source` |
| shadowfax_indirect_cod | `reconciliation_profile.cod_reconciliation` | No native Shadowfax settlement exists; COD reconciliation is indirect-only via `zs_observe.shiprocket_settlement` rows carrying a Shadowfax courier label. | `mismatch_category.missing_cod_remittance`, `mismatch_category.schema_only_source` |
| ecom_express_indirect_freight | `reconciliation_profile.shipment_to_invoice_reconciliation` | No native Ecom Express invoice exists; freight reconciliation is indirect-only via Shiprocket invoice rows labelled Ecom Express. | `mismatch_category.missing_invoice`, `mismatch_category.schema_only_source` |

---

## 12. Table-specific curated knowledge

No dedicated native tables are documented in the source. Use related source/aggregator table sections for field semantics.

### 12.1 Indirect evidence: `zs_observe.shiprocket_oms`

#### Business purpose

Operational shipment evidence source when courier labels identify Shadowfax or Ecom Express.

#### Grain

Use the grain documented in the Shiprocket OMS KB section. Usually shipment/AWB-level operational evidence, but validate before aggregation.

#### Key columns

| Column | Business meaning | Extraction note |
|---|---|---|
| `awb_code` | Shipment/AWB key. | Primary operational key for indirect courier segmentation. |
| `courier_company` | Courier label candidate. | Normalize to identify Shadowfax/Ecom. |
| `fulfilment_channel` | Fulfilment/channel/courier context candidate. | May help identify source path. |
| `master_courier` | Courier normalization/supporting field, if present. | Use as supporting courier-label evidence. |
| `transaction_type` | Transaction/movement type candidate. | Needed for reverse/QC/RTO interpretation. |
| `status` | Shipment or operational status candidate. | Value profiling required. |
| `is_active` | Active row flag if present. | Apply only where available. |

#### Reconciliation role

Expected-side operational evidence for indirect courier shipment, reverse/QC, freight, or COD checks.

---

### 12.2 Indirect evidence: `zs_observe.shiprocket_invoice`

#### Business purpose

Possible freight evidence source when courier labels identify Shadowfax or Ecom Express.

#### Grain

Use the grain documented in Shiprocket invoice KB. Usually invoice/billing line or AWB-linked freight record.

#### Key columns

| Column | Business meaning | Extraction note |
|---|---|---|
| `other_id` | AWB/reference candidate. | Join to `shiprocket_oms.awb_code` when valid. |
| `courier_partner` | Courier label candidate. | Normalize labels to identify Shadowfax/Ecom. |
| `charged_amount` | Freight amount candidate in invoice context. | Use Shiprocket invoice semantics. |
| `is_active` | Active row flag if present. | Apply only where available. |

#### Reconciliation role

Actual-side freight evidence for indirect courier-labelled shipments.

---

### 12.3 Indirect evidence: `zs_observe.shiprocket_settlement`

#### Business purpose

Possible COD/remittance evidence source when courier labels identify Shadowfax or Ecom Express.

#### Grain

Use the grain documented in Shiprocket settlement KB. Usually AWB-level or settlement-linked COD/remittance evidence.

#### Key columns

| Column | Business meaning | Extraction note |
|---|---|---|
| `awb_number` | AWB/reference candidate. | Join to `shiprocket_oms.awb_code` when valid. |
| `courier_partner` | Courier label candidate. | Normalize labels to identify Shadowfax/Ecom. |
| `charged_amount` | COD/remittance amount candidate in settlement context. | Use Shiprocket settlement semantics. |
| `delivered_date` | Delivery date candidate. | Use for delivery-to-remittance checks where valid. |
| `settlement_date` | Settlement/remittance date candidate. | Use for remittance lag where valid. |
| `is_active` | Active row flag if present. | Apply only where available. |

#### Reconciliation role

Actual-side COD/remittance evidence for indirect courier-labelled shipments.

---

## 13. Mandatory query rules

### 13.1 Native-table safety rules

- Do not create native Shadowfax/Ecom facts without native tables.
- Do not query non-existent native Shadowfax/Ecom tables.
- Do not infer direct vendor invoice, settlement, payout, or bank bridge evidence from courier label alone.

### 13.2 Indirect evidence rules

- Always state the source table when reporting Shadowfax/Ecom metrics from Shiprocket data.
- Normalize courier partner names before filtering.
- Use Shiprocket table semantics for invoice and settlement amount fields.
- Resolve account filters through the aggregator/source Account Data Binding.

### 13.3 Reverse/QC interpretation rules

- Treat Shadowfax reverse/QC interpretation as source-specific.
- Validate reverse/QC classification against status, transaction type, return/RTO, or NDR value profiles.
- Do not classify a shipment as reverse/QC only because the courier is Shadowfax.

### 13.4 Bank and money movement rules

- Do not perform direct Shadowfax/Ecom-to-bank reconciliation unless native remittance/bank bridge evidence is added.
- For indirect settlement-to-bank work, use the aggregator/source account and banking KB, not a direct Shadowfax/Ecom account assumption.

---

## 14. Data-quality and semantic caveats

- Indirect-only visibility means the true vendor contract/account may not be visible.
- Courier partner names may vary across source tables and rows.
- Ecom Express may appear as Ecom, Ecom Express, EcomExpress, Ecom-Express, or similar labels.
- Shadowfax reverse/QC interpretation requires source status and transaction-type support.
- If native tables are added later, create separate vendor docs or update this document with native table sections.
- Negative knowledge is important: no native dedicated tables are documented in the current source.

---

## 15. Supported question patterns

- Does Shadowfax have a native table?
- Does Ecom Express have a native settlement table?
- Where does Shadowfax appear in logistics data?
- Can I analyze Ecom Express COD remittance directly?
- Which Shiprocket shipments were handled by Shadowfax or Ecom?
- Which Shadowfax-labelled shipments look like return, reverse, QC, or RTO flows?
- Which Ecom-labelled shipments have freight invoice evidence?
- Which indirect courier rows have freight or COD evidence?
- Why should a query not join Shadowfax directly to bank credits?

---

## 16. SQL pattern appendix

SQL examples are evidence patterns only. Production queries must inject account filters through Account Data Binding.

```sql
-- Indirect courier segmentation through Shiprocket OMS
SELECT
  awb_code,
  courier_company,
  transaction_type,
  status
FROM zs_observe.shiprocket_oms
WHERE is_active = true
  AND (
    LOWER(courier_company) LIKE '%shadowfax%'
    OR LOWER(courier_company) LIKE '%ecom%'
  );
```

```sql
-- Indirect courier freight evidence through Shiprocket invoice
SELECT
  other_id AS awb,
  courier_partner,
  charged_amount AS freight_amount
FROM zs_observe.shiprocket_invoice
WHERE is_active = true
  AND (
    LOWER(courier_partner) LIKE '%shadowfax%'
    OR LOWER(courier_partner) LIKE '%ecom%'
  );
```

```sql
-- Indirect courier COD/remittance evidence through Shiprocket settlement
SELECT
  awb_number AS awb,
  courier_partner,
  charged_amount AS cod_or_remittance_amount,
  delivered_date,
  settlement_date
FROM zs_observe.shiprocket_settlement
WHERE is_active = true
  AND (
    LOWER(courier_partner) LIKE '%shadowfax%'
    OR LOWER(courier_partner) LIKE '%ecom%'
  );
```

---

## 17. Extraction guidance

Extract Shadowfax and Ecom Express as indirect/low-coverage logistics entities.

Preserve negative knowledge:

```text
No dedicated native Shadowfax table is documented in the source.
No dedicated native Ecom Express table is documented in the source.
Shiprocket can provide indirect evidence only when courier labels identify these vendors.
```

Do not extract direct native table cards for Shadowfax/Ecom unless future source content provides those tables.

---

## 18. Ingestion-compatible extraction sections

### 18.1 Column-level information candidates

#### Indirect evidence table: `zs_observe.shiprocket_oms`

| Column | Business meaning | Semantic roles | Default aggregation | Filtering/grouping guidance | Reconciliation usage | Caveats |
|---|---|---|---|---|---|---|
| `awb_code` | Shipment/AWB key in Shiprocket OMS. | identifier, join_key, reconciliation_key | none | Exact AWB lookup; join key. | Expected-side shipment key. | Use Shiprocket doc for full semantics. |
| `courier_company` | Courier label candidate. | dimension, filter, value_profile_candidate | none | Filter after label normalization. | Identifies indirect Shadowfax/Ecom evidence. | Not platform account identity. |
| `fulfilment_channel` | Fulfilment/channel context candidate. | dimension, filter | none | Supporting filter only. | Helps interpret logistics path. | Values require profiling. |
| `master_courier` | Normalized/superior courier label candidate. | dimension, filter, value_profile_candidate | none | Use alongside courier company. | Supports courier normalization. | Field availability may vary. |
| `transaction_type` | Transaction/movement type candidate. | dimension, filter, value_profile_candidate | none | Needed for reverse/QC/RTO classification. | Supports mismatch classification. | Values are source-specific. |
| `status` | Shipment operational status candidate. | status, filter, value_profile_candidate | none | Use after value profiling. | Delivery/RTO/reverse classification. | Do not infer reverse/QC alone. |
| `is_active` | Active row flag if present. | filter, rule_guardrail | none | Use `is_active = true` where present. | Prevents inactive row leakage. | Apply only where column exists. |

#### Indirect evidence table: `zs_observe.shiprocket_invoice`

| Column | Business meaning | Semantic roles | Default aggregation | Filtering/grouping guidance | Reconciliation usage | Caveats |
|---|---|---|---|---|---|---|
| `other_id` | AWB/reference candidate in invoice. | identifier, join_key, reconciliation_key | none | Join to OMS AWB when valid. | Actual-side freight evidence key. | Use Shiprocket invoice semantics. |
| `courier_partner` | Courier label candidate in invoice. | dimension, filter, value_profile_candidate | none | Filter after normalization. | Identifies indirect courier freight rows. | Not direct vendor account. |
| `charged_amount` | Freight amount candidate in invoice context. | measure, financial_amount | `SUM` | Aggregate after grain check. | Freight billed amount. | Do not interpret as COD. |
| `is_active` | Active row flag if present. | filter, rule_guardrail | none | Use `is_active = true` where present. | Prevents inactive row leakage. | Apply only where column exists. |

#### Indirect evidence table: `zs_observe.shiprocket_settlement`

| Column | Business meaning | Semantic roles | Default aggregation | Filtering/grouping guidance | Reconciliation usage | Caveats |
|---|---|---|---|---|---|---|
| `awb_number` | AWB/reference candidate in settlement. | identifier, join_key, reconciliation_key | none | Join to OMS AWB when valid. | Actual-side COD/remittance key. | Use Shiprocket settlement semantics. |
| `courier_partner` | Courier label candidate in settlement. | dimension, filter, value_profile_candidate | none | Filter after normalization. | Identifies indirect courier COD rows. | Not direct vendor account. |
| `charged_amount` | COD/remittance amount candidate in settlement context. | measure, financial_amount | `SUM` | Aggregate after grain check. | COD/remitted amount. | Do not interpret as freight. |
| `delivered_date` | Delivery date candidate. | date | none | Use for delivery-to-remittance lag. | Lag analysis. | Validate date availability/format. |
| `settlement_date` | Settlement/remittance date candidate. | date | none | Use for settlement window. | Lag and reconciliation window. | Validate date availability/format. |
| `is_active` | Active row flag if present. | filter, rule_guardrail | none | Use `is_active = true` where present. | Prevents inactive row leakage. | Apply only where column exists. |

---

### 18.2 Relationship candidates

| Relationship candidate | Source | Target | Join / match keys | Type | Cardinality expectation | Confidence | Caveats |
|---|---|---|---|---|---|---|---|
| Shiprocket OMS to invoice for indirect courier | `shiprocket_oms` | `shiprocket_invoice` | `awb_code` ↔ `other_id` | reconciliation_relation | one-to-many possible | medium-high | Filter/segment by normalized courier labels. |
| Shiprocket OMS to settlement for indirect courier | `shiprocket_oms` | `shiprocket_settlement` | `awb_code` ↔ `awb_number` | reconciliation_relation | one-to-zero-or-many | medium-high | Settlement may not exist for every shipment. |
| Shiprocket invoice to settlement by AWB | `shiprocket_invoice` | `shiprocket_settlement` | `other_id` ↔ `awb_number` | diagnostic_relation | many-to-many possible | medium | Pre-aggregate to AWB before comparing freight/COD. |
| Shadowfax/Ecom courier label to vendor entity | Shiprocket courier label fields | Platform entity `shadowfax` / `ecom_express` | normalized courier label | semantic_mapping | many labels to one vendor | medium | Mapping is label-based, not account-based. |
| Reverse/QC classification for Shadowfax | Shiprocket status/transaction fields | reverse logistics process | status/transaction/return indicators | process_classification | N/A | low-medium | Requires value profiling; do not infer from courier alone. |

---

### 18.3 Value profile candidates

| Table | Column | Candidate values / groups | Business meaning | Null handling | Extraction note |
|---|---|---|---|---|---|
| `shiprocket_oms` | `courier_company` | Shadowfax-like labels; Ecom-like labels; other courier labels | Underlying courier identification. | Null means courier cannot be segmented. | Normalize spelling/case/punctuation. |
| `shiprocket_oms` | `master_courier` | normalized courier groups | Supporting courier identification. | Null means no master mapping available. | Use with `courier_company`. |
| `shiprocket_oms` | `transaction_type` | forward, reverse, return, QC, RTO, unknown | Movement type / transaction class. | Null means movement type unresolved. | Profile actual values. |
| `shiprocket_oms` | `status` | delivered, RTO, returned, in_transit, failed, unknown | Shipment lifecycle status. | Null means status unresolved. | Do not hardcode without profiling. |
| `shiprocket_invoice` | `courier_partner` | Shadowfax-like labels; Ecom-like labels | Freight courier label. | Null means courier cannot be segmented. | Normalize labels. |
| `shiprocket_settlement` | `courier_partner` | Shadowfax-like labels; Ecom-like labels | COD/remittance courier label. | Null means courier cannot be segmented. | Normalize labels. |

---

### 18.4 Metric candidates

| Metric candidate | Business definition | Metric type | Default aggregation | Evidence source | Caveats |
|---|---|---|---|---|---|
| `metric.shadowfax_indirect_shipment_count` | Count of Shiprocket/source shipments where courier label identifies Shadowfax. | count | COUNT_DISTINCT | `shiprocket_oms` | Indirect source only. |
| `metric.shadowfax_reverse_qc_shipment_count` | Count of Shadowfax-labelled shipments classified as reverse/QC/RTO/return by status or transaction values. | count | COUNT_DISTINCT | `shiprocket_oms` | Requires value profile. |
| `metric.ecom_indirect_shipment_count` | Count of Shiprocket/source shipments where courier label identifies Ecom Express. | count | COUNT_DISTINCT | `shiprocket_oms` | Indirect source only. |
| `metric.indirect_courier_freight_billed_amount` | Freight billed for indirect courier-labelled shipments in source invoice table. | amount | SUM | `shiprocket_invoice` | Use source invoice semantics. |
| `metric.indirect_courier_cod_remitted_amount` | COD/remittance amount for indirect courier-labelled shipments in source settlement table. | amount | SUM | `shiprocket_settlement` | Use source settlement semantics. |
| `metric.indirect_courier_missing_invoice_awb_count` | Count of indirect courier-labelled AWBs without invoice evidence. | count | COUNT_DISTINCT | OMS + invoice | Requires AWB join. |
| `metric.indirect_courier_missing_settlement_awb_count` | Count of indirect courier-labelled COD/delivered AWBs without settlement evidence. | count | COUNT_DISTINCT | OMS + settlement | Requires COD/delivery classification. |
| `metric.native_coverage_status` | Whether native table exists for vendor. | status | latest / none | KB metadata | Negative knowledge metric. |

---

### 18.5 Metric implementation candidates

| Metric implementation candidate | Metric | Applicability | Formula / calculation description | Required columns | Required rules |
|---|---|---|---|---|---|
| `metric_impl.shiprocket_oms.shadowfax_indirect_shipment_count` | Shadowfax indirect shipment count | Shiprocket OMS indirect evidence | Count distinct `awb_code` where normalized courier label identifies Shadowfax. | `awb_code`, `courier_company` or `master_courier` | Courier label normalization; account binding. |
| `metric_impl.shiprocket_oms.shadowfax_reverse_qc_count` | Shadowfax reverse/QC shipment count | Shiprocket OMS indirect reverse evidence | Count distinct Shadowfax-labelled AWBs where status/transaction values indicate reverse/QC/RTO/return. | `awb_code`, courier label, `status`, `transaction_type` | Value profile; no courier-only reverse inference. |
| `metric_impl.shiprocket_oms.ecom_indirect_shipment_count` | Ecom indirect shipment count | Shiprocket OMS indirect evidence | Count distinct `awb_code` where normalized courier label identifies Ecom Express. | `awb_code`, courier label fields | Courier label normalization; account binding. |
| `metric_impl.shiprocket_invoice.indirect_courier_freight_amount` | Indirect courier freight billed amount | Shiprocket invoice | Sum `charged_amount` for normalized Shadowfax/Ecom courier labels. | `other_id`, `courier_partner`, `charged_amount` | Source invoice amount semantics. |
| `metric_impl.shiprocket_settlement.indirect_courier_cod_amount` | Indirect courier COD remitted amount | Shiprocket settlement | Sum `charged_amount` for normalized Shadowfax/Ecom courier labels. | `awb_number`, `courier_partner`, `charged_amount` | Source settlement amount semantics. |
| `metric_impl.shiprocket_oms.indirect_missing_freight_evidence_count` | Indirect courier missing freight evidence count | Shiprocket OMS left-joined to invoice | Count distinct Shadowfax/Ecom-labelled `awb_code` in OMS with no matching `shiprocket_invoice.other_id`. | OMS `awb_code`, courier label, `shiprocket_invoice.other_id` | Courier label normalization; left-join missing-evidence rule. |
| `metric_impl.shiprocket_oms.indirect_missing_cod_evidence_count` | Indirect courier missing COD evidence count | Shiprocket OMS left-joined to settlement | Count distinct Shadowfax/Ecom-labelled COD/delivered `awb_code` in OMS with no matching `shiprocket_settlement.awb_number`. | OMS `awb_code`, payment/status, courier label, `shiprocket_settlement.awb_number` | Apply delivered + COD filter; left-join missing-evidence rule. |
| `metric_impl.kb_metadata.native_coverage_status` | Native coverage status | KB metadata / platform doc | Return unavailable/indirect-only until native tables are documented. | N/A | Native-table safety rule. |

---

### 18.6 Formula template candidates

| Formula template | Plain-English formula | SQL-style pattern | Applies to |
|---|---|---|---|
| `formula_template.normalized_label_count` | Count distinct records where normalized label maps to vendor. | `COUNT(DISTINCT key) WHERE normalized_label IN (...)` | Indirect shipment counts. |
| `formula_template.filtered_amount_sum` | Sum amount after label, date, account, and semantic filters. | `SUM(amount_column)` with required filters | Indirect freight/COD metrics. |
| `formula_template.unmatched_key_count` | Count expected-side keys missing actual-side evidence. | `COUNT_DISTINCT(expected.key) WHERE actual.key IS NULL` | Missing invoice/settlement checks. |
| `formula_template.coverage_status_flag` | Return native coverage status from curated KB metadata. | static/status output | Native availability checks. |
| `formula_template.reverse_classification_count` | Count records where courier label and reverse/QC status rules both hold. | `COUNT(DISTINCT key) WHERE label_match AND reverse_status_match` | Shadowfax reverse/QC metrics. |

---

### 18.7 Rule candidates

| Rule candidate | Rule statement | Severity | Applies to | Failure mode |
|---|---|---|---|---|
| `rule.indirect_courier_no_native_fact_without_table` | Do not create native Shadowfax/Ecom facts unless native tables are documented. | critical | All Shadowfax/Ecom queries | Fabricated evidence. |
| `rule.indirect_courier_source_table_required` | Always state/use the aggregator/source table for indirect courier metrics. | high | Indirect metrics and outputs | Misrepresents indirect evidence as direct evidence. |
| `rule.indirect_courier_normalize_labels` | Normalize courier labels before filtering Shadowfax/Ecom rows. | medium | Query patterns | Missed rows or false exclusions. |
| `rule.indirect_courier_no_direct_bank_claim` | Do not claim direct bank receipt for Shadowfax/Ecom without bank bridge/native evidence. | critical | COD-to-bank outputs | False cash-realization claim. |
| `rule.shadowfax_reverse_requires_status_evidence` | Do not classify Shadowfax as reverse/QC using courier label alone. | high | Shadowfax reverse metrics | Incorrect process classification. |
| `rule.indirect_courier_account_filters_from_source_binding` | Apply account filters using the source/aggregator Account Data Binding. | critical | Executable queries | Cross-account leakage. |
| `rule.indirect_courier_amount_semantics_from_source` | Interpret freight/COD amounts using source table semantics, not direct vendor assumptions. | high | Amount metrics | Wrong metric meaning. |

---

### 18.8 Validation test candidates

| Validation test candidate | Test condition | Blocking? | Linked rule |
|---|---|---|---|
| `validation.indirect_no_native_table_reference` | Query does not reference undocumented native Shadowfax/Ecom tables. | yes | `rule.indirect_courier_no_native_fact_without_table` |
| `validation.indirect_source_table_present` | Query/output references Shiprocket or another documented source table. | yes | `rule.indirect_courier_source_table_required` |
| `validation.indirect_courier_label_filter_present` | Query contains normalized courier-label filter for Shadowfax/Ecom. | yes | `rule.indirect_courier_normalize_labels` |
| `validation.shadowfax_reverse_status_condition_present` | Reverse/QC Shadowfax query includes status/transaction/reverse condition beyond courier label. | yes | `rule.shadowfax_reverse_requires_status_evidence` |
| `validation.indirect_account_binding_present` | Query includes Account Data Binding filters for source/aggregator account tables. | yes | `rule.indirect_courier_account_filters_from_source_binding` |
| `validation.indirect_no_direct_bank_claim` | Output does not claim direct bank receipt without bank-side evidence. | yes | `rule.indirect_courier_no_direct_bank_claim` |
| `validation.indirect_amount_table_semantics` | Query uses invoice amount for freight and settlement amount for COD/remittance. | yes | `rule.indirect_courier_amount_semantics_from_source` |

---

### 18.9 Query pattern candidates

| Query pattern candidate | Intent supported | Required tables | Required joins / filters | Output expectation |
|---|---|---|---|---|
| `query_pattern.indirect_courier_oms_segmentation` | Find shipments handled by Shadowfax/Ecom through Shiprocket/source evidence. | `shiprocket_oms` | normalized courier label filter; account binding; date filter. | AWB list, courier label, status, count. |
| `query_pattern.shadowfax_reverse_qc_segmentation` | Identify Shadowfax-labelled reverse/QC/RTO/return shipments. | `shiprocket_oms` | Shadowfax label + reverse/QC/RTO status conditions. | Reverse/QC shipment count and evidence rows. |
| `query_pattern.ecom_indirect_shipment_summary` | Summarize Ecom Express indirect shipments. | `shiprocket_oms` | Ecom label filter; account binding. | Shipment count by status/date. |
| `query_pattern.indirect_courier_freight_summary` | Compute freight for Shadowfax/Ecom labels through Shiprocket invoice. | `shiprocket_invoice` | courier label filter; account binding; date filter. | Freight amount and AWB count. |
| `query_pattern.indirect_courier_cod_summary` | Compute COD/remittance for Shadowfax/Ecom labels through Shiprocket settlement. | `shiprocket_settlement` | courier label filter; account binding; date filter. | COD/remittance amount and AWB count. |
| `query_pattern.indirect_missing_invoice_by_awb` | Find indirect courier-labelled shipments without invoice evidence. | `shiprocket_oms`, `shiprocket_invoice` | AWB left join; courier filter. | Missing invoice AWBs. |
| `query_pattern.indirect_missing_settlement_by_awb` | Find indirect courier-labelled shipments without settlement evidence. | `shiprocket_oms`, `shiprocket_settlement` | AWB left join; courier filter; COD/delivery filters when available. | Missing settlement AWBs. |
| `query_pattern.indirect_native_coverage_lookup` | Answer whether native Shadowfax/Ecom tables exist. | KB metadata / this doc | deterministic lookup. | Coverage status and safe next steps. |

