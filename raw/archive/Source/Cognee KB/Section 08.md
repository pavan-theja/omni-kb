# **8. Common Card Schema**

**Status:** Draft - V4.0
**Phase:** 1 — KB Schema & Card Design   
**Scope:** Tenant-aware knowledge base for GraphRAG-driven SQL generation

## **Purpose of this section**

The Common Card Schema defines the baseline metadata every knowledge card should carry, regardless of card type.

This section answers:
* What fields should every card have?
* How do we uniquely identify cards?
* How do we track status, confidence, ownership, review, and source traceability?
* How do we support versioning, deprecation, and card replacement?
* How do we make cards easy to ingest into Cognee or another graph/RAG system?
* How do we keep authoring consistent across Business Hierarchy, Data Understanding, Metric Understanding, Process Understanding, Reconciliation Understanding, and Execution Guidance?
* How do we support the new Business Flow Binding primitive without making every card scope-heavy?

The common schema should stay lightweight. It should not force every card to carry every possible field. Domain-specific fields should remain inside their respective card sections.

---

## **8.1 Design Principle**

Every card should have:

```text
Stable identity
Clear type
Human-readable name
Business meaning
Source traceability
Lifecycle status
Confidence level
Review metadata
Optional aliases
Optional relationships
Optional applicability metadata
Optional evidence references
```

The common schema exists to make all cards predictable for:

```text
ingestion
linking
review
governance
retrieval
traceability
versioning
```

It should not become the place where business logic, SQL logic, matching logic, or account filtering lives.

---

## **8.2 Required Common Fields**

| Field              | Definition                                                                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `card_type`        | Type of card, e.g. `tenant`, `table`, `metric`, `business_process`, `business_flow_binding`, `query_pattern`                                     |
| `canonical_id`     | Stable unique ID for the card. This should not change when display names change.                                                                 |
| `name`             | Human-readable card name. Card-specific schemas may use more specific names like `metric_name`, `table_name`, `process_name`, or `binding_name`. |
| `description`      | Plain-English explanation of what the card represents.                                                                                           |
| `status`           | Lifecycle status: `draft`, `active`, `deprecated`, or `archived`.                                                                                |
| `confidence`       | Trust level: `curated`, `inferred`, `experimental`, `low_confidence`, or `unknown`.                                                              |
| `source_documents` | Source documents or references used to create the card.                                                                                          |
| `created_by`       | Person, system, or script that created the card.                                                                                                 |
| `updated_by`       | Person, system, or script that last updated the card.                                                                                            |
| `created_at`       | Creation timestamp, if available.                                                                                                                |
| `updated_at`       | Last update timestamp, if available.                                                                                                             |

---

## **8.3 Optional Common Fields**

| Field                 | Definition                                                                                                                   |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `aliases`             | Alternate names, synonyms, abbreviations, or business phrases for the card.                                                  |
| `tags`                | Search and organization tags.                                                                                                |
| `owner`               | Internal owner, team, or accountable function.                                                                               |
| `review_status`       | `unreviewed`, `reviewed`, `approved`, `needs_revision`, `rejected`.                                                          |
| `reviewed_by`         | Reviewer name, team, or system.                                                                                              |
| `reviewed_at`         | Review timestamp.                                                                                                            |
| `version`             | Version number or semantic version.                                                                                          |
| `replaces`            | Canonical ID of the older card this card replaces.                                                                           |
| `replaced_by`         | Canonical ID of the newer card that replaces this card.                                                                      |
| `valid_from`          | Date from which this card is valid.                                                                                          |
| `valid_to`            | Date until which this card is valid.                                                                                         |
| `notes`               | Additional authoring or interpretation notes.                                                                                |
| `links`               | Explicit related-card references, if not represented only through graph edges.                                               |
| `evidence_refs`       | References to semantic chunks that support this card.                                                                        |
| `applicability_scope` | Optional knowledge-validity metadata. Full rules are defined in Section 9.                                                   |
| `retrieval_text`      | Optional generated text fields for full-text/vector indexing. Should be produced by ingestion, not hand-authored by default. |
| `metadata_filters`    | Optional retrieval filters generated during ingestion. Should be generated from canonical card fields where possible.        |

---

## **8.4 Recommended Base Shape**

```json
{
  "card_type": "metric",
  "canonical_id": "metric.net_collected_amount",
  "name": "Net Collected Amount",
  "description": "Amount actually collected or realized after relevant deductions, refunds, fees, and adjustments depending on source-system context.",
  "aliases": [
    "net collection",
    "actual collection"
  ],
  "tags": [
    "cash_flow",
    "payment_reconciliation"
  ],
  "status": "active",
  "confidence": "curated",
  "source_documents": [
    "internal_metric_library"
  ],
  "evidence_refs": [
    {
      "source_doc": "internal_metric_library",
      "chunk_id": "internal_metric_library::net_collected_amount",
      "source_span": "lines 10-18"
    }
  ],
  "owner": "finance_data_team",
  "review_status": "approved",
  "created_by": "kb_authoring_script",
  "updated_by": "finance_data_team",
  "version": "1.0"
}
```

---

## **8.5 Canonical ID Convention**

Canonical IDs should be:

* Stable
* Human-readable
* Lowercase
* Dot-separated
* Type-prefixed
* Independent of display name changes

Recommended pattern:

```text
<card_type>.<domain_or_scope>.<specific_name>
```

Examples:

```text
tenant.acme_retail
group.acme_india
platform.amazon
platform.shiprocket
platform.razorpay
platform.hdfc_bank
platform_context.amazon.in
platform_context.shiprocket.in
platform_context.razorpay.in
platform_context.hdfc.india
platform_account.acme.amazon_in.primary
platform_account.acme.shiprocket.primary
platform_account.acme.razorpay.primary
platform_account.acme.hdfc.current
account_data_binding.acme.amazon_in.primary.amazon_settlement
account_data_binding.acme.shiprocket.primary.shiprocket_oms
business_scope_set.acme_india.amazon_all
business_scope_set.acme_india.razorpay_to_hdfc
business_flow_binding.acme_india.shopify_to_shiprocket
business_flow_binding.acme_india.razorpay_to_hdfc
table.zs_observe.amazon_settlement
column.zs_observe.amazon_settlement.total
metric.seller_realization_rate
metric_impl.amazon_settlement.seller_realization_rate
business_process.payment_gateway_to_bank_reconciliation
reconciliation_profile.payment_gateway_payout_to_bank_credit
query_pattern.payment_gateway_to_bank_recon.summary
validation_test.required_scope_filter_present
output_contract.reconciliation_summary
```

---

## **8.6 Status Values**

| Status       | Meaning                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------- |
| `draft`      | Card is being authored and should not be used for production execution.                       |
| `active`     | Card is approved for use.                                                                     |
| `deprecated` | Card should not be selected for new workflows but may be retained for backward compatibility. |
| `archived`   | Card is no longer relevant and should be ignored except for history.                          |

---

## **8.7 Confidence Values**

| Confidence       | Meaning                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| `curated`        | Human-reviewed and trusted.                                                                         |
| `inferred`       | Derived from schemas, data profiling, source docs, or model assistance but not fully reviewed.      |
| `experimental`   | Useful but not yet trusted for production.                                                          |
| `low_confidence` | Known data-quality, coverage, or extraction risk exists. Usable only with warnings or human review. |
| `unknown`        | Confidence not yet assessed.                                                                        |

Use `low_confidence` when the card is known to be risky, not merely unreviewed.

Examples:

```text
Native vendor table exists but key fields are mostly null.
A relationship is structurally possible but not validated.
A matching rule is inferred from field names but not confirmed.
```

---

## **8.8 Source Document Guidance**

`source_documents` should point to the material used to author or infer the card.

Examples:

```text
amazon_marketplace_gold_standard_curated_raw_ingestion.md
flipkart_marketplace_gold_standard_curated_raw_ingestion.md
myntra_marketplace_gold_standard_curated_raw_ingestion.md
nykaa_marketplace_gold_standard_curated_raw_ingestion.md
logistics_domain_overview.md
shiprocket_logistics.md
razorpay_schema_notes.md
bank_statement_mapping.xlsx
internal_metric_library
internal_process_library
warehouse_schema_snapshot_2026_05_16
```

The goal is not legal citation. The goal is traceability for review, debugging, regeneration, and explanation.

---

## **8.9 Evidence Reference Guidance**

Every card should retain evidence references where possible.

Recommended shape:

```json
{
  "evidence_refs": [
    {
      "source_doc": "shiprocket_logistics.md",
      "chunk_id": "shiprocket_logistics.md::cod_settlement_table",
      "source_span": "lines 80-120",
      "extraction_confidence": "curated"
    }
  ]
}
```

Principle:

```text
source_documents identify the source file.
evidence_refs identify the exact supporting chunk.
```

Default retrieval should return evidence metadata, not full evidence chunks. Full evidence chunks should be fetched only when needed for review, debugging, conflict resolution, or explanation support.

---

## **8.10 Relationship Storage Guidance**

There are two acceptable ways to represent relationships.

### Option 1 — Embedded references

```json
{
  "card_type": "metric",
  "canonical_id": "metric.seller_realization_rate",
  "implementations": [
    "metric_impl.amazon_settlement.seller_realization_rate"
  ]
}
```

### Option 2 — Graph edges

```text
Metric HAS_IMPLEMENTATION MetricImplementation
BusinessFlowBinding USES_PLATFORM_ACCOUNT PlatformAccount
BusinessFlowBinding USES_ACCOUNT_DATA_BINDING AccountDataBinding
BusinessFlowBinding SUPPORTS_PROCESS BusinessProcess
BusinessFlowBinding SUPPORTS_RECONCILIATION_PROFILE ReconciliationProfile
```

Recommended approach:

```text
Use graph edges as the primary relationship model.
Use embedded references only when they improve card readability or ingestion simplicity.
```

---

## **8.11 Common Graph Edge Types**

The exact graph edge catalog can evolve, but common edges should include:

```text
Tenant HAS_GROUP Group
Group HAS_PLATFORM_ACCOUNT PlatformAccount
Platform HAS_PLATFORM_CONTEXT PlatformContext
PlatformAccount HAS_ACCOUNT_DATA_BINDING AccountDataBinding
BusinessScopeSet INCLUDES_PLATFORM_ACCOUNT PlatformAccount
BusinessFlowBinding USES_PLATFORM_ACCOUNT PlatformAccount
BusinessFlowBinding USES_ACCOUNT_DATA_BINDING AccountDataBinding
BusinessFlowBinding SUPPORTS_PROCESS BusinessProcess
BusinessFlowBinding SUPPORTS_RECONCILIATION_PROFILE ReconciliationProfile
BusinessFlowBinding USES_TABLE Table
Table HAS_COLUMN Column
Table HAS_VALUE_PROFILE ValueProfile
Table RELATED_TO Table
Metric HAS_IMPLEMENTATION MetricImplementation
MetricImplementation USES_TABLE Table
MetricImplementation USES_COLUMN Column
BusinessProcess HAS_WORKFLOW_STEP WorkflowStep
BusinessProcess HAS_STATE_TRANSITION StateTransition
ReconciliationProfile HAS_SIDE ReconciliationSide
ReconciliationProfile HAS_UNIT ReconciliationUnit
ReconciliationProfile HAS_MATCHING_LOGIC MatchingLogic
ReconciliationProfile HAS_MISMATCH_CATEGORY MismatchCategory
QueryPattern REQUIRES_RULE Rule
Rule HAS_VALIDATION_TEST ValidationTest
QueryPattern HAS_OUTPUT_CONTRACT OutputContract
```

Business Flow Binding edges are important because they connect tenant/group-specific business reality to reusable process, reconciliation, data, and execution knowledge.

---

## **8.12 Applicability Metadata Guidance**

Some cards need `applicability_scope`; many do not.

Use applicability metadata when the card's validity depends on:

```text
platform type
platform
platform context
business process
reconciliation profile
business scope set
business flow binding
```

Do not use applicability metadata to store account filters.

Account filters belong to:

```text
Account Data Binding
```

Cross-platform tenant/group participation belongs to:

```text
Business Flow Binding
```

Example:

```json
{
  "applicability_scope": {
    "scope_level": "business_process",
    "business_process_ids": [
      "business_process.payment_gateway_to_bank_reconciliation"
    ],
    "notes": [
      "This rule applies to payment-gateway-to-bank reconciliation. Runtime account participation is resolved through Business Flow Binding."
    ]
  }
}
```

---

## **8.13 What Common Schema Should Not Do**

The common schema should not carry domain-specific logic such as:

* SQL formulas
* Account filters
* Join keys
* Metric-specific dimensions
* Reconciliation tolerances
* Output contract schemas
* Business process workflow steps
* Flow-specific participant roles
* Money-flow matching logic

Those belong in the relevant card sections.

Specifically:

```text
Account filters belong in Account Data Binding.
Cross-platform participant logic belongs in Business Flow Binding.
Metric formulas belong in Metric Implementation.
Workflow steps belong in Process Understanding.
Matching tolerances belong in Reconciliation Understanding.
Query safeguards belong in Execution Guidance.
```

---

## **8.14 Common Schema Review Checklist**

Before accepting a card, check:

```text
1. Does it have card_type?
2. Does it have canonical_id?
3. Is canonical_id stable and type-prefixed?
4. Does it have a readable name?
5. Does description explain what the card represents?
6. Is status valid?
7. Is confidence valid?
8. Are source_documents present?
9. Are evidence_refs present where possible?
10. Is domain-specific logic kept out of common fields?
11. Are account filters absent unless this is an Account Data Binding card?
12. Are cross-platform participant roles absent unless this is a Business Flow Binding card?
13. Are graph relationships represented through edges or clean embedded references?
14. Is the card reusable rather than one-off unless it intentionally represents tenant/group/account context?
```

---

## **8.15 Final Principle**

```text
Common schema gives every card identity, governance, traceability, reviewability, and retrieval hygiene.
Specialized schema gives each card its meaning.
```

The common schema should make cards easy to manage without turning every card into a scope model, execution plan, or graph traversal recipe.

---