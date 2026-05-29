# **12. Raw Markdown Authoring & Ingestion Pipeline**

**Status:** Draft - V4.0
**Phase:** 1 — KB Schema & Card Design   
**Scope:** Tenant-aware knowledge base for GraphRAG-driven SQL generation

## **Purpose of this section**

This section defines how human-written markdown becomes retrieval-ready KB artifacts.

The core principle is:

```text
Humans write readable knowledge documents.
The pipeline extracts structured cards, graph edges, indexes, and evidence metadata.
```

Raw markdown should not force humans to author:

```text
card YAML
canonical JSON
graph edges
retrieval metadata
full card schemas
```

Raw markdown should be a human-editable source of truth. The ingestion pipeline should turn it into structured KB artifacts.

---

## **12.1 Core Design Principle**

The ingestion design must preserve five separate layers:

```text
1. Raw Markdown
   Human-readable, business-editable source knowledge.

2. Semantic Chunks
   Heading-aware evidence blocks extracted from raw markdown.

3. Intermediate Card YAML
   Candidate cards, graph edges, review items, and confidence metadata.

4. Canonical KB Artifacts
   Validated cards and graph edges.

5. Retrieval-Ready Artifacts
   Deterministic lookup keys, full-text fields, vector text, metadata filters, and evidence references.
```

The important separation is:

```text
Raw markdown = human editing layer
Semantic chunks = evidence layer
Intermediate YAML = extraction layer
Canonical cards = KB artifact layer
Retrieval indexes = runtime discovery layer
```

Do not collapse all of these into one format.

---

## **12.2 What Raw Markdown Should Be**

Raw markdown should look like normal internal documentation.

It should contain:

```text
Business explanation
Important entities
Platform behavior
Tenant/group/account observations where relevant
Tables, columns, metrics, processes, matching logic, or rules
Flow applicability described in plain English
Caveats and exceptions
Examples and common questions
```

It should not require humans to write:

```text
card_type
canonical_id
full card fields
canonical JSON
graph edges
embedding text
retrieval metadata
all relationships upfront
```

A lightweight frontmatter is enough.

Example:

```yaml
---
title: Razorpay Payment Gateway Knowledge
doc_type: payment_gateway_knowledge
domain: payment_reconciliation
platforms: [razorpay]
platform_types: [payment_gateway]
money_flow_paths:
  - order_to_payment
  - payment_gateway_to_bank
status: draft
owner: finance_data_team
last_updated: 2026-05-18
related_docs:
  - payment_gateway_to_bank_reconciliation.md
---
```

---

## **12.3 What Raw Markdown Should Not Be**

Raw markdown should not become:

```text
A card YAML file
A graph-edge file
A SQL-only playbook
A warehouse schema dump
A copy-paste of source documentation
A tenant-specific JSON config file
A marketplace-specific ingestion script disguised as prose
```

Especially important:

```text
Raw markdown can describe business flow applicability.
It should not force humans to author Business Flow Binding cards directly.
```

Correct:

```markdown
For Acme India Shopify D2C orders, shipments are normally routed through Shiprocket.
Shiprocket provides AWB, courier partner, freight invoice, and COD settlement evidence.
HDFC is the bank account used for COD remittance matching when bank reconciliation is required.
```

Incorrect:

```yaml
card_type: business_flow_binding
canonical_id: business_flow_binding.acme_india.shopify_to_shiprocket
...
```

The second form belongs to the intermediate extraction output, not the raw markdown authoring layer.

---

## **12.4 Recommended Raw Markdown Document Families**

Raw markdown should be split into coherent, independently ingestible documents.

### Marketplace docs

```text
marketplace_domain_overview.md
amazon_marketplace.md
flipkart_marketplace.md
myntra_marketplace.md
nykaa_marketplace.md
future_marketplace.md
marketplace_reconciliation_patterns.md
```

### Logistics docs

```text
logistics_domain_overview.md
shiprocket_logistics.md
delhivery_logistics.md
dtdc_logistics.md
ekart_logistics.md
xpressbees_logistics.md
shadowfax_ecom_logistics.md
logistics_reconciliation_patterns.md
```

### Payment gateway docs

```text
payment_domain_overview.md
razorpay_payments.md
cashfree_payments.md
payu_payments.md
stripe_payments.md
payment_gateway_reconciliation_patterns.md
```

### Banking docs

```text
banking_domain_overview.md
hdfc_bank_statement.md
icici_bank_statement.md
axis_bank_statement.md
bank_reconciliation_patterns.md
```

### Accounting / ERP docs

```text
accounting_domain_overview.md
tally_accounting.md
netsuite_accounting.md
quickbooks_accounting.md
erp_to_bank_reconciliation.md
```

### Cross-domain reconciliation docs

```text
marketplace_to_bank_reconciliation.md
payment_gateway_to_bank_reconciliation.md
marketplace_to_payment_gateway_reconciliation.md
logistics_cod_to_bank_reconciliation.md
refund_to_bank_reconciliation.md
unidentified_bank_credit_classification.md
```

### Tenant/group context docs

```text
<tenant>_business_hierarchy.md
<tenant>_<group>_platform_accounts.md
<tenant>_<group>_account_data_bindings.md
<tenant>_<group>_business_scope_sets.md
<tenant>_<group>_business_flow_applicability.md
```

The final family is important because platform/vendor docs should stay generic, while tenant/group flow applicability is customer-specific.

---

## **12.5 Role of Tenant/Group Business Flow Applicability Docs**

Business Flow Binding should usually be extracted from tenant/group context docs, not from generic marketplace, logistics, payment, or banking docs.

A tenant/group business flow applicability doc should explain:

```text
Which platform accounts participate together
What business flow they support
Which account plays which role
Which conditions activate the flow
Which evidence tables are usually involved
Which joins or evidence paths are expected
Which bank/payment/logistics/accounting endpoints are used
What is known, partial, inferred, or unresolved
```

Example raw markdown:

```markdown
# Acme India Business Flow Applicability

Acme India uses Shopify for D2C orders and Shiprocket for courier aggregation.

For Shopify D2C orders, Shiprocket is the logistics evidence source.
Shopify is the order source.
Shiprocket provides AWB, courier partner, shipment status, freight invoice, and COD settlement evidence.

For COD orders, Shiprocket COD settlement should be reconciled against HDFC bank credits when UTR or bank reference is available.

For Razorpay payments, Razorpay payouts should be reconciled against HDFC current account credits.
Razorpay is the payout source and HDFC is the bank destination.

For Amazon marketplace settlement, Amazon settlement payouts should be reconciled against HDFC credits only when the question crosses into bank realization.
Amazon is the settlement source and HDFC is the bank destination.
```

Expected extracted cards:

```text
Business Flow Binding
Business Scope Set, if reusable
Account Data Binding references
Graph edges from Business Flow Binding to Platform Accounts, Tables, Business Processes, and Reconciliation Profiles
Review items for unresolved or inferred flow assumptions
```

---

## **12.6 Recommended Raw Markdown Structure**

A general-purpose raw markdown document should follow this shape:

```markdown
# Title

## 1. How to use this document
Explain when this doc should be retrieved and what it covers.

## 2. Overview
Plain-English explanation.

## 3. Scope and applicability
Where this knowledge applies. Do not hardcode runtime filters unless this is a tenant/group context doc.

## 4. Business role
What role this domain/platform/table/process plays.

## 5. Key concepts
Important business, data, process, reconciliation, or execution concepts.

## 6. Tables or evidence sources covered
Tables and their business meaning, if applicable.

## 7. Relationships and join concepts
Human-readable join paths, identifiers, fallback keys, and grain risks.

## 8. Metrics and definitions
Important metrics and business definitions, if applicable.

## 9. Process or flow understanding
Expected process flow or money-flow path, if applicable.

## 10. Reconciliation use cases
What should match, when applicable.

## 11. Mandatory rules and caveats
Known rules, unsafe assumptions, data-quality risks.

## 12. Example questions
Typical questions this document should help answer.

## 13. Extraction guidance
What card families the pipeline should expect to extract.
```

Domain-specific gold-standard frames can extend this structure.

Examples:

```text
Marketplace gold-standard frame
Logistics gold-standard frame
Payment gateway gold-standard frame
Banking gold-standard frame
Accounting/ERP gold-standard frame
```

---

## **12.7 Semantic Chunking**

Chunking should be semantic, not token-first.

```text
Chunk for meaning first.
Extract cards second.
Optimize retrieval later.
```

A chunk is an evidence unit, not a card.

```text
One chunk can create many cards.
One card can be assembled from many chunks.
```

---

## **12.8 Recommended Chunk Boundaries**

| Raw doc type                 | Chunk by                                                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Business Hierarchy           | Tenant, group, platform accounts, account bindings, business scope sets, business flow applicability          |
| Business Flow Applicability  | One flow at a time: participants, roles, conditions, evidence path, unresolved assumptions                    |
| Data Understanding           | Table overview, table grain, columns, relationships, value meanings, caveats                                  |
| Metric Understanding         | Metric definition, aliases, formula, implementation notes, dependencies, caveats                              |
| Process Understanding        | Process overview, workflow steps, states, lags, failure modes                                                 |
| Reconciliation Understanding | Sides, units, keys, fallback logic, tolerances, mismatch categories                                           |
| Execution Guidance           | Query pattern, safeguards, rules, validation checks, output expectations                                      |
| Marketplace Knowledge        | Marketplace lifecycle, settlement waterfall, table family, fees, refunds, taxes, fulfilment/logistics signals |
| Logistics Knowledge          | Fulfilment ownership, shipment lifecycle, freight, COD/remittance, bank bridge, vendor caveats                |
| Payment Gateway Knowledge    | Payment lifecycle, captures, refunds, disputes, fees, payouts, settlement-to-bank bridge                      |
| Banking Knowledge            | Credits, debits, UTRs, narration parsing, account identity, bank statement grain, cash-realization caveats    |
| Cross-Domain Reconciliation  | Expected side, actual side, money-flow path, participating platform types, match keys, caveats                |

---

## **12.9 Recommended Chunk Metadata**

```yaml
chunk_id: acme_india_business_flow_applicability.md::razorpay_to_hdfc
source_file: acme_india_business_flow_applicability.md
heading_path:
  - Acme India Business Flow Applicability
  - Razorpay to HDFC Payout Reconciliation
chunk_type: business_flow_applicability
parent_context:
  tenant: acme_retail
  group: acme_india
  money_flow_path: payment_gateway_to_bank
  participating_platforms:
    - razorpay
    - hdfc_bank
expected_card_types:
  - business_flow_binding
  - business_scope_set
  - account_data_binding_reference
  - graph_edge
source_span: lines 24-52
text: |
  Razorpay payouts should be reconciled against HDFC current account credits.
  Razorpay is the payout source and HDFC is the bank destination.
  Use Razorpay payout reference or UTR where available, otherwise amount and date-window fallback is required.
```

Avoid:

```text
Fixed-size chunks with no heading awareness.
Splitting a formula away from its definition.
Splitting matching keys away from tolerances.
Splitting Business Flow Binding participants away from their conditions.
Splitting account-binding observations away from the table they apply to.
Treating every bullet as a separate chunk.
Treating one chunk as one final card.
```

---

## **12.10 Intermediate Card YAML**

The extractor converts semantic chunks into candidate cards, edges, review items, and confidence metadata.

The YAML is the intermediary structured output. It is not the primary human-authored source.

### Example — Business Flow Binding extraction

```yaml
document:
  title: Acme India Business Flow Applicability
  source_file: acme_india_business_flow_applicability.md
  doc_type: business_flow_applicability
  extraction_confidence: inferred

cards:
  - card_type: business_flow_binding
    canonical_id: business_flow_binding.acme_india.razorpay_to_hdfc
    tenant_id: tenant.acme_retail
    group_id: group.acme_india
    binding_name: Acme India Razorpay to HDFC Bank Flow
    binding_type: money_flow
    money_flow_paths:
      - payment_gateway_to_bank
    participating_accounts:
      - platform_account_id: platform_account.acme.razorpay.primary
        role: payout_source
        required: true
      - platform_account_id: platform_account.acme.hdfc.current
        role: bank_destination
        required: true
    business_process_ids:
      - business_process.payment_gateway_to_bank_reconciliation
    reconciliation_profile_ids:
      - reconciliation_profile.payment_gateway_payout_to_bank_credit
    evidence_table_ids:
      - table.zs_observe.razorpay_payouts
      - table.zs_observe.bank_statement
    account_data_binding_ids:
      - account_data_binding.acme.razorpay.primary.razorpay_payouts
      - account_data_binding.acme.hdfc.current.bank_statement
    conditions:
      - concept: payout_status
        operator: IN
        value: [processed, paid]
      - concept: bank_transaction_direction
        operator: =
        value: credit
    confidence: inferred
    status: draft
    source_documents:
      - acme_india_business_flow_applicability.md
    evidence_refs:
      - chunk_id: acme_india_business_flow_applicability.md::razorpay_to_hdfc

edges:
  - source: group.acme_india
    edge: HAS_BUSINESS_FLOW_BINDING
    target: business_flow_binding.acme_india.razorpay_to_hdfc
  - source: business_flow_binding.acme_india.razorpay_to_hdfc
    edge: USES_SETTLEMENT_SOURCE_ACCOUNT
    target: platform_account.acme.razorpay.primary
  - source: business_flow_binding.acme_india.razorpay_to_hdfc
    edge: USES_BANK_DESTINATION_ACCOUNT
    target: platform_account.acme.hdfc.current
  - source: business_flow_binding.acme_india.razorpay_to_hdfc
    edge: SUPPORTS_PROCESS
    target: business_process.payment_gateway_to_bank_reconciliation
  - source: business_flow_binding.acme_india.razorpay_to_hdfc
    edge: SUPPORTS_RECONCILIATION_PROFILE
    target: reconciliation_profile.payment_gateway_payout_to_bank_credit

review_items:
  - item: business_flow_binding.acme_india.razorpay_to_hdfc
    issue: Confirm exact HDFC account and Razorpay merchant account identifiers before activation.
    severity: medium
```

---

## **12.11 Intermediate YAML Extraction Rules**

Intermediate YAML should be produced by the ingestion pipeline and then reviewed.

It should include:

```text
candidate cards
candidate edges
confidence
source documents
evidence references
review items
missing references
validation warnings
```

It should not be treated as canonical until validation and review pass.

Important extraction rules:

```text
Do not create metric implementations per account unless the formula changes.
Do not create Business Scope Sets for ad-hoc account combinations.
Do not create Business Flow Bindings for one-off user questions.
Do not create logistics-specific, payment-specific, or banking-specific binding card types.
Use Business Flow Binding as the generic primitive.
Do not place reconciliation matching tolerances inside Business Flow Binding.
Do not place SQL query plans inside Business Flow Binding.
Do not place account filters inside Table, Metric, Process, or Reconciliation cards.
```

---

## **12.12 Validation and Review**

Before canonical ingestion, validate:

```text
Every card has card_type.
Every card has canonical_id.
Every card has status.
Every card has source_documents.
Every card has evidence references where possible.
Required fields for the card type are present.
Canonical IDs are unique.
Referenced IDs exist or are marked pending.
Enum values are valid.
Account filters are not incorrectly embedded in table or metric cards.
Metric implementations are not duplicated per account unless formula changes.
Business Scope Sets are not created for ad-hoc account combinations.
Business Flow Bindings are not created for one-off user questions.
Business Flow Bindings have participant accounts and roles.
Business Flow Bindings reference valid platform accounts.
Business Flow Bindings do not contain detailed matching logic that belongs to Reconciliation Understanding.
Business Flow Bindings do not contain SQL plans that belong to Execution Guidance.
Graph edges reference valid card IDs.
Money-flow path values are valid.
Evidence references point to actual chunks.
```

Review flow:

```text
Raw markdown authored
→ semantic chunks created
→ YAML extracted as draft
→ validation runs
→ human reviews review_items
→ approved cards become canonical JSON
→ graph nodes and edges are generated
→ retrieval indexes are generated
→ Cognee / graph KB ingestion
```

---

## **12.13 Retrieval-Ready Outputs**

Ingestion should not stop at canonical cards.

It must also produce the artifacts required by retrieval.

| Output                    | Purpose                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------- |
| Canonical cards           | Primary KB nodes                                                                   |
| Graph edges               | Dependency and relationship traversal                                              |
| Deterministic lookup keys | Exact lookup for scope, IDs, tables, columns, accounts, flows, references          |
| Full-text search fields   | Keyword / lexical search                                                           |
| Vector embedding text     | Semantic retrieval over business meaning                                           |
| Metadata filters          | Filtering by card type, status, platform, scope, flow, confidence, domain, process |
| Evidence metadata         | Traceability from card back to raw markdown chunk                                  |
| Evidence chunk store      | Full source chunks available for lazy loading                                      |

This directly supports the retrieval strategy:

```text
Deterministic retrieval locks the world.
Semantic retrieval understands the ask.
Business Flow Binding identifies cross-platform account participation.
Graph traversal completes the context.
Evidence metadata keeps retrieval auditable.
```

---

## **12.14 Deterministic Lookup Keys**

Ingestion should generate exact lookup keys for fields that should not depend on embeddings.

Examples:

```text
canonical_id
tenant_name
tenant_code
group_name
group_code
platform_name
platform_type
platform_context_name
source_context_code
platform_account_name
source_account_identifier
business_scope_set_name
business_flow_binding_name
money_flow_path
participant_role
group_level_id
merchant_id
seller_id
gateway_account_id
payment_id
payout_id
settlement_id
refund_id
chargeback_id
bank_account_id
account_number_hash
bank_statement_account_id
utr_no
bank_reference
transaction_id
transaction_narration
credit_debit_indicator
awb_number
shipment_id
table_name
full_reference
column_name
metric_name
metric aliases
```

These keys support deterministic retrieval and scope locking.

---

## **12.15 Full-Text and Vector Fields**

Each canonical card should generate retrieval text.

### Full-text fields

Used for keyword and lexical search:

```text
canonical_id
name
aliases
source identifiers
table names
column names
business concepts
common questions
platform names
account names
money-flow path names
participant roles
reference IDs
```

### Vector text

Used for semantic retrieval:

```text
name
description
business definition
business meaning
aliases
common questions
failure modes
metric interpretation
process explanation
reconciliation semantics
business flow meaning
money-flow path explanation
```

Example for a Business Flow Binding:

```yaml
retrieval_text:
  full_text: Acme India Razorpay HDFC payout bank credit payment gateway to bank reconciliation
  vector_text: Acme India Razorpay to HDFC flow links Razorpay payout evidence to HDFC bank credit evidence for payment gateway to bank reconciliation. Razorpay is the payout source and HDFC is the bank destination.
```

---

## **12.16 Metadata Filters**

Ingestion should attach metadata that retrieval can filter on.

Recommended metadata:

```text
card_type
status
confidence
platform_type
platform_id
platform_context_id
tenant_id, if applicable
group_id, if applicable
platform_account_id, if applicable
business_scope_set_id, if applicable
business_flow_binding_id, if applicable
money_flow_path
participant_role
participating_platform_types
domain_id
business_process_id
reconciliation_profile_id
scope_level
source_documents
review_status
```

Example:

```text
status = active
card_type = business_flow_binding
money_flow_path = payment_gateway_to_bank
participant_role includes bank_destination
platform_id in [platform.razorpay, platform.hdfc_bank]
confidence in [curated, inferred]
```

---

## **12.17 Evidence Metadata and Chunk Store**

Every canonical card should retain evidence references.

Default retrieval should return evidence metadata, not full evidence chunks.

Example:

```yaml
evidence_metadata:
  - card_id: business_flow_binding.acme_india.razorpay_to_hdfc
    source_doc: acme_india_business_flow_applicability.md
    chunk_id: acme_india_business_flow_applicability.md::razorpay_to_hdfc
    source_span: lines 24-52
    extraction_confidence: curated
```

The full chunk should be stored separately and fetched only when needed for:

```text
human review
low-confidence cards
conflicting cards
source-backed explanation
retrieval debugging
```

Principle:

```text
Cards are working context.
Evidence metadata proves where they came from.
Full chunks are fetched on demand.
```

---

## **12.18 What Each Layer Owns**

| Layer             | Owns                                                     | Should not own                                |
| ----------------- | -------------------------------------------------------- | --------------------------------------------- |
| Raw Markdown      | Human-readable knowledge and flow applicability in prose | Full card schema, graph edges, canonical JSON |
| Semantic Chunks   | Evidence blocks with inherited context                   | Final card identity or retrieval optimization |
| Intermediate YAML | Candidate cards, edges, review items                     | Permanent truth before validation             |
| Canonical Cards   | Validated KB nodes                                       | Human-friendly authoring prose                |
| Graph Edges       | Relationships between cards                              | Card-specific business definitions            |
| Retrieval Indexes | Lookup, lexical, semantic, metadata access               | Business truth not present in cards           |
| Evidence Store    | Source traceability                                      | Primary runtime context by default            |

---

## **12.19 Raw Markdown Examples by Card Family**

### Business Hierarchy

```markdown
# Acme India Business Hierarchy

Acme Retail is the tenant. Acme India is the India operating group and reports primarily in INR.

Acme India uses Amazon India, Razorpay India, HDFC Bank, Shiprocket, and Shopify.

Amazon India has two seller accounts:
- Primary Amazon India account
- Secondary Amazon India account

In the Amazon settlement table:
- Primary account maps to group_level_id = 22
- Secondary account maps to group_level_id = 26

In Razorpay payout tables:
- Razorpay primary account maps to merchant_id = rzp_live_xxx

In HDFC bank statement tables:
- HDFC current account maps to bank_account_id = hdfc_current_xxx
```

Expected extracted cards:

```text
Tenant, Group, Platform, Platform Context, Platform Account, Account Data Binding, Business Scope Set if reusable
```

---

### Business Flow Applicability

```markdown
# Acme India Business Flow Applicability

For Shopify D2C orders, Acme India uses Shiprocket as the courier aggregator.
Shopify is the order source. Shiprocket is the logistics evidence source.

Shiprocket provides shipment status, AWB, courier partner, freight invoice, and COD settlement evidence.

For COD orders, Shiprocket COD settlement may be reconciled to HDFC bank credits when UTR or bank reference is available.

For Razorpay payments, Razorpay payouts should be reconciled against HDFC current account credits.
Razorpay is the payout source and HDFC is the bank destination.

For Amazon marketplace settlement, Amazon settlement should be reconciled to HDFC bank credits only when the question asks about actual bank realization.
Amazon is the settlement source and HDFC is the bank destination.
```

Expected extracted cards:

```text
Business Flow Binding, Business Scope Set if reusable, graph edges, review items for unresolved accounts or evidence paths
```

---

### Data Understanding

```markdown
# Amazon Settlement Data

The Amazon settlement table is zs_observe.amazon_settlement.
It is used for payout, fee, refund, tax deduction, reimbursement, and seller realization analysis.

Each row represents one settlement transaction line.

Important columns:
- total: net credited or debited amount
- product_sales: gross product sales amount
- type: transaction category
- created_date: safe reporting date
- date_time: display date; avoid for filtering

The type column can contain Order, Refund, Service Fee, and null.
Do not drop null type rows blindly.
```

Expected extracted cards:

```text
Table, Column, Relationship, Value Profile
```

---

### Metric Understanding

```markdown
# Seller Realization Rate

Seller Realization Rate measures the percentage of gross product sales that reaches the seller after deductions, fees, refunds, and adjustments.

For Amazon settlement data, calculate it as net settled amount divided by gross product sales.

Net settled amount comes from summing total.
Gross product sales should use product_sales where type = Order.

Use denominator protection to avoid divide-by-zero.
Account filters should be resolved separately through Account Data Binding.
Cross-platform realization-to-bank checks should resolve Business Flow Binding only when bank evidence is required.
```

Expected extracted cards:

```text
Metric, Metric Implementation, Formula Template, Metric Dependency
```

---

### Process Understanding

```markdown
# Payment Gateway to Bank Reconciliation Process

This process reconciles payment gateway payouts against actual bank credits.

Expected flow:
1. Payment is captured.
2. Captured payments become eligible for payout.
3. Payment gateway creates a payout batch.
4. Payout is processed.
5. Bank receives the credit.

Bank credit usually appears within two business days after payout processing.

Common failures include missing bank credit, amount mismatch, delayed bank credit, and missing bank reference.

This process is generic. Tenant/group-specific participating accounts should be resolved through Business Flow Binding.
```

Expected extracted cards:

```text
Domain, Business Process, Workflow Step, State Transition, Process Variant if needed
```

---

### Reconciliation Understanding

```markdown
# Payment Gateway Payout to Bank Credit Matching

This reconciliation compares payment gateway payout batches against bank credit transactions.

Expected side: payment gateway payout.
Actual side: bank credit.

Primary matching keys are UTR and bank reference.
Fallback matching uses amount, bank account, and date window.

One payout should usually map to one bank credit.
Bank credit can appear up to T+2 business days after payout.

Mismatch categories include missing bank credit, delayed bank credit, amount mismatch, unidentified bank credit, and reference missing.

This reconciliation profile defines what should match. The tenant/group-specific Razorpay-to-HDFC flow should be resolved through Business Flow Binding.
```

Expected extracted cards:

```text
Reconciliation Profile, Reconciliation Side, Reconciliation Unit, Matching Logic, Mismatch Category, Reconciliation Variant if needed
```

---

### Execution Guidance

```markdown
# Payment Gateway to Bank Reconciliation Execution Guidance

Build payout-side and bank-side aggregates before matching.

Required safeguards:
- Resolve Business Flow Binding when the query crosses payment gateway and bank platforms.
- Apply account scope filters from Account Data Binding.
- Use only processed or paid payouts.
- Use only bank credit transactions.
- Align payout and bank data at payout/reference grain.
- Do not join transaction-level payout details directly to bank credits without pre-aggregation.
- Apply the configured reconciliation window.
- Classify delayed credits separately from missing credits.

Validation checks:
- Business Flow Binding must be present for cross-platform reconciliation.
- Scope filters must be present.
- Unsafe date columns must not be used.
- Grain alignment must be valid.
```

Expected extracted cards:

```text
Query Pattern, Rule, Validation Test, Output Contract, Execution Constraint Set
```

---

## **12.20 Final Principle**

```text
Do not collapse authoring, extraction, validation, ingestion, and retrieval indexing into one format.

Raw markdown is for humans.
Semantic chunks are evidence.
Intermediate YAML is extracted structure.
Canonical cards are the KB artifact.
Graph edges connect the KB.
Retrieval indexes make the KB discoverable.
Evidence metadata makes retrieval auditable.
Business Flow Binding makes cross-platform flow applicability explicit without making raw markdown card-heavy.
```

---

