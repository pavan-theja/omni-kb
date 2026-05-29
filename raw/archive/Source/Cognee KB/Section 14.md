# **14. Retrieval Strategy**

**Status:** Draft — V4.0
**Phase:** 1 — KB Schema & Card Design
**Scope:** Retrieval strategy for analytics, reconciliation, diagnostics, operational lookup, and cross-platform money-flow reasoning

---

## **Purpose of this section**

This section defines how ZenStatement should retrieve the right KB cards for analytics, reconciliation, diagnostics, operational lookups, and money-flow tracing.

The retrieval layer should not retrieve raw documents by default. It should retrieve the minimum correct set of cards, confidence metadata, scope metadata, Business Flow Binding context, and evidence references needed by the orchestrator.

Core principle:

```text
Deterministic retrieval locks identity and scope.
Semantic retrieval understands business intent.
Business Flow Binding resolves cross-platform account participation.
Graph traversal completes the context.
Metadata filters enforce applicability.
Completeness checks prevent unsafe handoff.
Evidence metadata keeps retrieval auditable.
```

Retrieval does not generate SQL, execute queries, repair errors, or create final business answers. It assembles the right context bundle for the orchestrator.

---

## **14.1 Retrieval Inputs**

Retrieval starts with a user question and any available session context.

Input may include:

```text
User question
Tenant / group context, if already known
Conversation history
User-selected filters
Date range
Platform hints
Platform account hints
Business scope hints
Business flow hints
Metric hints
Table or column names
Reference identifiers
Uploaded file context, if applicable
```

Reference identifiers may include:

```text
group_level_id
merchant_id
seller_id
payment_id
payout_id
settlement_id
refund_id
chargeback_id
bank_account_id
UTR / bank reference
AWB / shipment ID
order ID
invoice number
transaction ID
```

Example:

```text
Why does Razorpay payout not match HDFC bank credit for Acme India last month?
```

---

## **14.2 Retrieval Stores**

Retrieval should operate over four stores:

| Store                | Purpose                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| Card graph           | Typed graph of cards and relationships                                                             |
| Card search index    | Keyword / full-text search over names, aliases, descriptions, IDs, and source identifiers          |
| Card vector index    | Semantic search over card meanings, business definitions, common questions, and failure modes      |
| Evidence chunk store | Source markdown chunks used for traceability, review, conflict resolution, and explanation support |

Default retrieval should return:

```text
cards + confidence + metadata + evidence references
```

It should not return full raw markdown or full chunks by default.

---

## **14.3 Retrieval Modes**

ZenStatement should combine four retrieval modes.

---

### **1. Deterministic Retrieval**

Use deterministic retrieval when the query contains exact identifiers, structured entities, or hard constraints.

Examples:

```text
tenant name
group name
platform name
platform context
platform account name
business scope set name
business flow binding name
group_level_id
merchant_id
seller_id
bank_account_id
table name
column name
metric canonical name
payment_id
payout_id
settlement_id
UTR / bank reference
AWB / shipment ID
date range
currency
```

Use:

```text
exact lookup
metadata filters
keyword / full-text search
graph lookup
```

Do not rely on embeddings for these.

---

### **2. Semantic Retrieval**

Use semantic retrieval when the user expresses business intent or meaning.

Examples:

```text
seller realization
payout lower than expected
cash leakage
payment not matching bank
COD pending
refund impact
where did money get stuck
unidentified bank credit
shipment delivered but cash missing
freight overcharge
marketplace settlement mismatch
```

Use semantic search over:

```text
card names
aliases
descriptions
business definitions
common questions
failure modes
process explanations
reconciliation semantics
business flow descriptions
money-flow path descriptions
```

Semantic retrieval is best for:

```text
Metric
Domain
Business Process
Reconciliation Profile
Matching Logic
Mismatch Category
Query Pattern
Business Flow Binding, when the user describes a flow without exact account names
```

---

### **3. Business Flow Binding Retrieval**

Use Business Flow Binding retrieval when the question crosses platform families or requires role-based participation across accounts.

Examples:

```text
Razorpay payout not matching HDFC bank credit
Amazon settlement not received in bank
Shopify COD delivered but not remitted by Shiprocket
Courier COD remittance not matching bank credit
Marketplace refund processed but bank debit not visible
ERP ledger not matching bank transaction
```

Business Flow Binding retrieval should identify:

```text
tenant
group
flow type / money-flow path
participating platform accounts
participant roles
conditions
expected evidence tables
account data bindings
related business process
related reconciliation profile
```

This is the retrieval mode that prevents domain-specific route cards such as:

```text
Logistics Route Binding
Payment Route Binding
Bank Route Binding
```

The generic primitive is:

```text
Business Flow Binding
```

---

### **4. Graph Traversal**

Use graph traversal after a reliable anchor card is found.

Example anchor:

```text
metric.seller_realization_rate
```

Expand to:

```text
Metric Implementation
Formula Template
Metric Dependencies
Required Tables
Required Columns
Rules
Validation Tests
Query Patterns
```

Example anchor:

```text
business_flow_binding.acme_india.razorpay_to_hdfc
```

Expand to:

```text
Participating Platform Accounts
Account Data Bindings
Business Process
Reconciliation Profile
Evidence Tables
Relationships
Query Pattern
Execution Constraint Set
Output Contract
```

Example anchor:

```text
reconciliation_profile.payment_gateway_payout_to_bank_credit
```

Expand to:

```text
Reconciliation Sides
Reconciliation Units
Matching Logic
Mismatch Categories
Business Process
Query Pattern
Output Contract
Validation Tests
```

Graph traversal should be typed and bounded. Do not recursively expand the whole graph.

---

## **14.4 Retrieval Mode by Card Family**

| Card family              | Primary retrieval mode                 | Notes                                               |
| ------------------------ | -------------------------------------- | --------------------------------------------------- |
| Tenant                   | Deterministic                          | Identity must be exact                              |
| Group                    | Deterministic                          | Scope must be exact                                 |
| Platform                 | Deterministic + keyword                | Platform names are known entities                   |
| Platform Context         | Deterministic                          | Country / region / instance context                 |
| Platform Account         | Deterministic                          | Account selection must be precise                   |
| Account Data Binding     | Graph traversal                        | From selected account + table                       |
| Business Scope Set       | Deterministic + semantic               | Named scopes can be exact or intent-based           |
| Business Flow Binding    | Deterministic + semantic + graph       | Required for cross-platform flow participation      |
| Table                    | Deterministic + semantic               | Exact if named, semantic if described               |
| Column                   | Deterministic + semantic               | Exact if named, semantic if business concept        |
| Relationship             | Graph traversal                        | Structural joins from table/flow/recon context      |
| Value Profile            | Graph traversal                        | Usually from table/column                           |
| Metric                   | Semantic + alias search                | Users ask in business terms                         |
| Metric Implementation    | Graph traversal + applicability filter | From metric + platform/context/table                |
| Formula Template         | Graph traversal + semantic             | Needed for derived metrics                          |
| Metric Dependency        | Graph traversal                        | From metric or implementation                       |
| Domain                   | Semantic                               | Used for intent classification                      |
| Business Process         | Semantic + graph                       | Used for workflow reasoning                         |
| Workflow Step            | Graph traversal                        | From business process                               |
| State Transition         | Graph traversal                        | From business process                               |
| Process Variant          | Graph traversal + applicability filter | Only when process changes materially                |
| Reconciliation Profile   | Semantic + graph                       | Used for matching/gap questions                     |
| Reconciliation Side      | Graph traversal                        | From reconciliation profile                         |
| Reconciliation Unit      | Graph traversal                        | From reconciliation profile                         |
| Matching Logic           | Graph traversal                        | From reconciliation profile                         |
| Mismatch Category        | Graph traversal                        | From reconciliation profile or matching logic       |
| Reconciliation Variant   | Graph traversal + applicability filter | Only when matching model changes materially         |
| Query Pattern            | Graph traversal + semantic fallback    | Usually from metric/process/recon/flow              |
| Rule                     | Graph traversal                        | Attached to selected cards                          |
| Validation Test          | Graph traversal                        | Attached to rules/query patterns                    |
| Output Contract          | Deterministic + graph                  | From query type or query pattern                    |
| Execution Constraint Set | Graph traversal                        | From query pattern, process, recon profile, or flow |

---

## **14.5 Retrieval Flow**

Recommended retrieval flow:

```text
1. Classify query type
2. Extract hard constraints
3. Resolve deterministic identity and runtime scope
4. Detect whether cross-platform flow resolution is required
5. Resolve Business Flow Binding when required
6. Retrieve intent cards semantically
7. Apply metadata and applicability filters
8. Graph-expand required dependencies
9. Score and rank retrieved cards
10. Run completeness checks
11. Return retrieval bundle
```

Key rule:

```text
Do not always resolve Business Flow Binding.
Resolve it when the question crosses platform families or when account roles/evidence paths matter.
```

---

## **14.6 Query Type Classification**

Classify the user question into one of:

```text
analytical
reconciliation
diagnostic
lookup / operational
money_flow_trace
```

Examples:

```text
“What is my Amazon net settlement?”
→ analytical

“Why does Razorpay not match HDFC?”
→ reconciliation

“Why did realization drop?”
→ diagnostic

“What does group_level_id 26 refer to?”
→ lookup / operational

“Where did this payout get stuck?”
→ money_flow_trace
```

Query type controls the retrieval path.

---

## **14.7 Cross-Platform Flow Detection**

Before retrieving Business Flow Binding, determine whether the question crosses platform families.

### Business Flow Binding usually required

Use Business Flow Binding when the question involves:

```text
marketplace → logistics
marketplace → payment gateway
payment gateway → bank
marketplace → bank
logistics COD → bank
refund → gateway/bank
ERP/accounting → bank
```

Examples:

| User phrase                              | Flow requirement               |
| ---------------------------------------- | ------------------------------ |
| Razorpay payout not received in HDFC     | Business Flow Binding required |
| Amazon settlement not matching bank      | Business Flow Binding required |
| COD delivered but cash not received      | Business Flow Binding required |
| Shopify order shipped through Shiprocket | Business Flow Binding required |
| Refund processed but bank debit missing  | Business Flow Binding required |
| NetSuite ledger not matching bank        | Business Flow Binding required |

### Business Flow Binding usually not required

Do not force Business Flow Binding for simple single-platform questions.

Examples:

| User phrase                                   | Flow requirement                          |
| --------------------------------------------- | ----------------------------------------- |
| Show Amazon seller realization                | Account Data Binding usually enough       |
| List Razorpay payments last month             | Account Data Binding usually enough       |
| Show HDFC bank credits yesterday              | Account Data Binding usually enough       |
| Count Shiprocket delivered shipments          | Account Data Binding usually enough       |
| What does Amazon settlement type Refund mean? | Value Profile / Data Understanding enough |

---

## **14.8 Money-Flow Path Detection**

Money-flow path is a generic classification of the flow.

Business Flow Binding maps that generic path to tenant/group-specific participating accounts.

Examples:

| User phrase                              | Detected money-flow path             | Possible Business Flow Binding                             |
| ---------------------------------------- | ------------------------------------ | ---------------------------------------------------------- |
| Razorpay payout not received in HDFC     | `payment_gateway_to_bank`            | `business_flow_binding.acme_india.razorpay_to_hdfc`        |
| Amazon settlement not matching bank      | `marketplace_to_bank`                | `business_flow_binding.acme_india.amazon_to_hdfc`          |
| COD delivered but cash not received      | `logistics_cod_to_bank`              | `business_flow_binding.acme_india.shiprocket_cod_to_hdfc`  |
| Shopify order delivered but not remitted | `cod_delivery_to_courier_remittance` | `business_flow_binding.acme_india.shopify_to_shiprocket`   |
| Refund processed but debit not visible   | `refund_to_bank`                     | `business_flow_binding.acme_india.razorpay_refund_to_hdfc` |
| Unidentified HDFC credit                 | `bank_credit_identification`         | May not require a single flow binding initially            |

Money-flow path detection prevents retrieval from expanding into every connected domain.

---

## **14.9 Scope Resolution**

Scope should be resolved early and deterministically wherever possible.

Retrieve:

```text
Tenant
Group
Platform
Platform Context
Platform Account
Business Scope Set, if named/reusable
Business Flow Binding, if cross-platform flow is required
Account Data Binding
```

If scope is missing or ambiguous, retrieval should not hallucinate defaults.

Return:

```text
resolved_scope.status = resolved | partial | unresolved
```

and include unresolved items as metadata.

Example:

```yaml
resolved_scope:
  status: partial
  confidence: medium
  deterministic_matches:
    tenant: tenant.acme_retail
    platforms:
      - platform.razorpay
      - platform.hdfc_bank
  unresolved_items:
    - type: missing_group
      detail: User mentioned Razorpay and HDFC but did not specify group.
      severity: blocking
```

---

## **14.10 Account Data Binding Resolution**

Once platform accounts and tables are selected, retrieve Account Data Bindings.

Account Data Binding answers:

```text
How does this selected account map to this table?
```

Examples:

```text
Amazon account → amazon_settlement → group_level_id = 22
Razorpay account → razorpay_payouts → merchant_id = rzp_live_xxx
HDFC account → bank_statement → bank_account_id = hdfc_current_xxx
Shiprocket account → shiprocket_oms → group_level_id = 203
```

Rules:

```text
Do not use table cards to infer account filters.
Do not use metric cards to store account filters.
Do not use Business Flow Binding as a replacement for Account Data Binding.
```

Business Flow Binding tells which accounts participate.
Account Data Binding tells how each selected account filters each selected table.

---

## **14.11 Business Flow Binding Resolution**

Business Flow Binding retrieval should happen when cross-platform participation matters.

Retrieval should match on:

```text
tenant
group
platforms
platform accounts
business scope set
money-flow path
business process
reconciliation profile
participant roles
conditions
flow aliases
common questions
```

Business Flow Binding should return:

```text
binding ID
participating platform accounts
participant roles
conditions
money-flow paths
business process IDs
reconciliation profile IDs
evidence table IDs
relationship IDs
account data binding IDs, if known
confidence
unresolved assumptions
```

Example:

```yaml
business_flow_binding:
  card_id: business_flow_binding.acme_india.razorpay_to_hdfc
  confidence: high
  money_flow_paths:
    - payment_gateway_to_bank
  participating_accounts:
    - platform_account_id: platform_account.acme.razorpay.primary
      role: payout_source
    - platform_account_id: platform_account.acme.hdfc.current
      role: bank_destination
  evidence_tables:
    - table.zs_observe.razorpay_payouts
    - table.zs_observe.bank_statement
```

---

## **14.12 Retrieval Paths by Query Type**

### **Analytical Query Path**

Use for questions like:

```text
Show seller realization rate for Acme India Amazon.
```

Retrieve in this order:

```text
1. Business Hierarchy
2. Runtime Scope
3. Account Data Binding
4. Metric
5. Metric Implementation
6. Data Understanding
7. Execution Guidance
```

Business Flow Binding is not required unless the analytic question crosses systems.

---

### **Reconciliation Query Path**

Use for questions like:

```text
Reconcile Razorpay payouts with HDFC bank credits.
```

Retrieve in this order:

```text
1. Business Hierarchy
2. Runtime Scope
3. Money-flow path
4. Business Flow Binding, if cross-platform
5. Process Understanding
6. Reconciliation Understanding
7. Data Understanding
8. Account Data Binding
9. Metric Understanding
10. Execution Guidance
```

---

### **Diagnostic Query Path**

Use for questions like:

```text
Why did marketplace realization drop this month?
```

Retrieve in this order:

```text
1. Business Hierarchy
2. Runtime Scope
3. Domain / Process Understanding
4. Metric Understanding
5. Candidate driver paths
6. Business Flow Binding only for cross-platform driver branches
7. Data Understanding
8. Reconciliation / Failure Modes
9. Execution Guidance
```

Diagnostic retrieval may start broad, then branch into specific flows only when the suspected driver crosses systems.

---

### **Money-Flow Trace Path**

Use for questions like:

```text
Where did this payout get stuck?
Why did this COD amount not reach the bank?
Which system has the missing money?
```

Retrieve in this order:

```text
1. Deterministic identifiers and scope
2. Money-flow path
3. Business Flow Binding
4. Participating Platform Accounts
5. Account Data Bindings
6. Business Process
7. Reconciliation Profile
8. Reconciliation Units and Matching Logic
9. Tables, Relationships, Columns, Value Profiles
10. Rules, Validation Tests, Output Contract
```

---

### **Lookup / Operational Query Path**

Use for questions like:

```text
What is group_level_id 26?
Which table has Razorpay payout data?
What does Amazon settlement type = Refund mean?
Which flow connects Razorpay to HDFC?
```

Retrieve in this order:

```text
1. Deterministic card lookup
2. Immediate graph neighbors
3. Evidence metadata
```

---

## **14.13 Conditional Domain Expansion**

Do not expand into all domains by default.

Expand into marketplace when the query mentions:

```text
marketplace settlement
seller realization
commission
marketplace fee
cashback
reimbursement
refund
order settlement
Amazon
Flipkart
Myntra
Nykaa
```

Expand into logistics when the query mentions:

```text
shipment
AWB
tracking
courier
freight
COD
RTO
return pickup
delivery
remittance
Shiprocket
Delhivery
DTDC
Ekart
XpressBees
Shadowfax
Ecom Express
```

Expand into payment gateway when the query mentions:

```text
payment captured
gateway
Razorpay
Cashfree
PayU
Stripe
payment_id
payout
settlement
refund
chargeback
payment fee
```

Expand into banking when the query mentions:

```text
bank credit
bank debit
statement
UTR
NEFT
IMPS
narration
unidentified credit
received in bank
not received
settled to bank
HDFC
ICICI
Axis
```

Expand into accounting / ERP when the query mentions:

```text
ledger
journal
invoice posting
revenue recognition
receivable
payable
book entry
Tally
NetSuite
QuickBooks
ERP
```

Business Flow Binding should constrain which of these expanded domains are actually relevant for the tenant/group.

---

## **14.14 Graph Expansion Rules**

Graph expansion should be typed, shallow, and purpose-driven.

Good expansion:

```text
Metric → Metric Implementation → Table → Columns → Rules → Validation Tests
```

Good expansion:

```text
Business Flow Binding → Platform Accounts → Account Data Bindings → Tables → Relationships
```

Good expansion:

```text
Business Flow Binding → Business Process → Reconciliation Profile → Sides → Units → Matching Logic → Mismatch Categories
```

Good expansion:

```text
Reconciliation Profile → Query Pattern → Rules → Validation Tests → Output Contract
```

Avoid:

```text
Expand all neighbors recursively.
Expand unrelated domains.
Expand every table connected to a platform.
Expand every metric in a domain.
Expand every Business Flow Binding for a group when only one flow path is relevant.
Expand into banking/payment/logistics unless the query or selected Business Flow Binding requires it.
```

Recommended expansion depth:

```text
1–2 hops by default
3 hops only for known dependency chains
```

---

## **14.15 Ranking and Confidence**

Each retrieved card should carry retrieval metadata.

Recommended fields:

```yaml
card_id: business_flow_binding.acme_india.razorpay_to_hdfc
card_type: business_flow_binding
retrieval_mode: deterministic | semantic | graph_expansion | flow_resolution
match_reason: exact_id | alias_match | money_flow_path_match | participant_account_match | graph_neighbor | applicability_filter
confidence: high | medium | low
score: 0.92
```

Confidence should combine:

```text
retrieval match strength
card confidence
scope compatibility
Business Flow Binding compatibility
money-flow path compatibility
participant role compatibility
status
source quality
whether graph dependency is complete
```

Deterministic matches do not automatically mean complete retrieval. They only mean that one anchor is reliable.

---

## **14.16 Evidence Metadata**

Default retrieval should include evidence metadata, not full evidence chunks.

Example:

```yaml
evidence_metadata:
  - card_id: business_flow_binding.acme_india.razorpay_to_hdfc
    source_doc: acme_india_business_flow_applicability.md
    chunk_id: acme_india_business_flow_applicability.md::razorpay_to_hdfc
    source_span: lines 24-52
    extraction_confidence: curated
```

Full evidence chunks should be fetched lazily only when needed:

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

## **14.17 Retrieval Bundle**

Retrieval should return a structured bundle, not SQL and not an execution plan.

Example:

```yaml
retrieval_bundle:
  query: Why does Razorpay payout not match HDFC bank credit for Acme India last month?
  query_type: reconciliation

  money_flow_path:
    detected_path: payment_gateway_to_bank
    confidence: high
    participating_platform_types:
      - payment_gateway
      - banking
    expected_start_object: payout
    expected_end_object: bank_credit

  resolved_scope:
    status: partial
    confidence: medium
    deterministic_matches:
      tenant: tenant.acme_retail
      group: group.acme_india
      platforms:
        - platform.razorpay
        - platform.hdfc_bank
    platform_accounts:
      - platform_account.acme.razorpay.primary
      - platform_account.acme.hdfc.current
    business_scope_sets:
      - business_scope_set.acme_india.razorpay_to_hdfc
    account_data_bindings:
      - account_data_binding.acme.razorpay.primary.razorpay_payouts
      - account_data_binding.acme.hdfc.current.bank_statement
    unresolved_items: []

  business_flow_binding:
    required: true
    status: resolved
    selected:
      card_id: business_flow_binding.acme_india.razorpay_to_hdfc
      confidence: high
      participating_accounts:
        - platform_account_id: platform_account.acme.razorpay.primary
          role: payout_source
        - platform_account_id: platform_account.acme.hdfc.current
          role: bank_destination
      evidence_tables:
        - table.zs_observe.razorpay_payouts
        - table.zs_observe.bank_statement
    unresolved_items: []

  retrieved_cards:
    business_hierarchy: []
    data_understanding: []
    metric_understanding: []
    process_understanding: []
    reconciliation_understanding: []
    execution_guidance: []

  confidence:
    scope: medium
    money_flow_path: high
    business_flow_binding: high
    data: high
    metric: medium
    process: high
    reconciliation: high
    execution_guidance: medium

  evidence_metadata:
    mode: references_only
    items: []

  unresolved_items: []
```

---

## **14.18 Completeness Checks**

Before handoff to the orchestrator, retrieval should check whether required context is missing.

### Analytical checks

```text
Resolved scope exists.
Metric is resolved.
Metric implementation is applicable.
Required table exists.
Required columns exist.
Account Data Binding exists for selected accounts and tables.
Execution rules and validation tests are available.
Business Flow Binding is not required unless the analytic question crosses systems.
```

### Reconciliation checks

```text
Resolved scope exists for all participating sides.
Money-flow path is detected or explicitly unresolved.
Business Flow Binding is resolved if reconciliation crosses platform families.
Business process is resolved.
Reconciliation profile is resolved.
Reconciliation sides are known.
Primary and fallback units are known.
Matching logic is available.
Required tables and columns exist.
Account Data Bindings exist for selected accounts and tables.
Output contract is available.
```

### Diagnostic checks

```text
Domain/process is resolved.
Primary metric or symptom is resolved.
Potential drivers are available.
Candidate money-flow paths are identified when needed.
Business Flow Binding is resolved for cross-platform driver branches.
Relevant data sources are available.
Failure modes or mismatch categories are available.
Execution guidance is available.
```

### Money-flow trace checks

```text
Start object is known or explicitly unresolved.
End object is known or explicitly unresolved.
Money-flow path is detected.
Participating platform types are known.
Business Flow Binding is resolved or explicitly unresolved.
Participating platform accounts are known.
Account Data Bindings exist for selected accounts and evidence tables.
At least one reconciliation profile exists for the detected path.
Tables exist for expected and actual sides.
Matching keys or fallback matching logic exist.
```

Unresolved items should be explicit:

```yaml
unresolved_items:
  - type: missing_business_flow_binding
    detail: Razorpay and HDFC were detected, but no active Business Flow Binding was found for Acme India.
    severity: blocking
```

```yaml
unresolved_items:
  - type: missing_account_data_binding
    detail: HDFC account was selected, but no Account Data Binding was found for bank_statement table.
    severity: blocking
```

---

## **14.19 Anti-Patterns**

Avoid:

```text
Vector-searching everything.
Graph-expanding everything.
Retrieving raw markdown first when canonical cards exist.
Using embeddings for exact IDs, table names, account IDs, UTRs, AWBs, or dates.
Letting semantic retrieval override deterministic scope.
Letting graph traversal override deterministic scope locks.
Using table cards to resolve account filters.
Using Business Flow Binding to store account filters.
Using Business Flow Binding to store detailed matching logic.
Creating execution plans inside retrieval.
Returning full evidence chunks by default.
Returning cards without confidence metadata.
Expanding into every platform family when one money-flow path is enough.
Creating Logistics Route Binding, Payment Route Binding, or Bank Route Binding as separate retrieval concepts.
Treating Business Scope Set as equivalent to Business Flow Binding.
Treating Account Data Binding as equivalent to Business Flow Binding.
Treating payment captured as bank-realized cash.
Treating COD delivered as COD remitted.
Treating marketplace settlement as bank credit without reconciliation.
```

---

## **14.20 Final Principle**

```text
Deterministic retrieval locks identity and scope.
Semantic retrieval finds business intent.
Money-flow path detection classifies the kind of cross-system movement.
Business Flow Binding maps that movement to tenant/group-specific participating accounts.
Account Data Binding maps selected accounts to table filters.
Graph traversal collects dependencies.
Metadata filters enforce applicability.
Completeness checks prevent unsafe handoff.
Evidence metadata preserves auditability.
```

This keeps retrieval precise while allowing ZenStatement to evolve from marketplace analytics into full cross-platform money-flow reasoning across marketplaces, logistics, payment gateways, banks, ERP, accounting systems, and custom sources.
