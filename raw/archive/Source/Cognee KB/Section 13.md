# **13. Summary / Design Principles**

**Status:** Draft — V4.0
**Phase:** 1 — KB Schema & Card Design
**Scope:** Context Engineering KB for analytics, reconciliation, diagnostics, and cross-platform money-flow reasoning

---

## **Purpose of this section**

This section summarizes the final design principles behind the ZenStatement Context Engineering KB.

It answers:

* What is the KB fundamentally designed to do?
* What are the core card families?
* What should each layer own?
* What should each layer avoid owning?
* How do we prevent scope explosion?
* How do we keep the system reusable across marketplaces, payment gateways, banks, logistics platforms, ERP, accounting systems, and custom sources?
* How do we model end-to-end financial truth across systems?
* How does Business Flow Binding fit into the architecture without becoming another domain-specific route model?

---

## **13.1 Final Positioning**

ZenStatement should not be modeled as a simple Text-to-SQL system.

It should be modeled as a:

```text
Context Engineering KB for financial analytics, reconciliation, diagnostics, and money-flow reasoning.
```

Its job is to provide structured knowledge so downstream systems can:

```text
understand business meaning
resolve scope
choose the right evidence
reason across systems
constrain execution
validate results
explain outputs
```

The KB does not replace the orchestrator. It gives the orchestrator the right context.

---

## **13.2 What the KB Owns**

The KB owns:

```text
Business meaning
Tenant/group/platform/account structure
Platform context
Account-to-data bindings
Reusable named business scopes
Tenant/group-specific business flow bindings
Data structure knowledge
Metric definitions and implementations
Process expectations
Reconciliation semantics
Execution guardrails
Validation definitions
Output contract definitions
Money-flow path semantics
Evidence traceability
```

---

## **13.3 What the KB Does Not Own**

The KB does not own:

```text
Runtime planning
Tool selection
SQL generation retries
Query execution
Dataframe execution
Final orchestration
Automatic repair loops
User interaction strategy
Ad-hoc account combinations as permanent cards
Domain-specific route-binding card types for every new platform family
```

Those belong to the orchestrator and execution layer.

---

## **13.4 Core Card Families**

The KB is organized into six major card families:

```text
1. Business Hierarchy
   Who’s data?
   Which accounts exist?
   How do accounts map to data?
   Which accounts participate together in reusable flows?

2. Data Understanding
   Where is the data?

3. Metric Understanding
   What is being calculated?

4. Process Understanding
   What should happen?

5. Reconciliation Understanding
   What should match?

6. Execution Guidance
   How do we execute safely?
```

Business Flow Binding lives inside Business Hierarchy because it is about tenant/group-specific account participation, not generic process logic.

---

## **13.5 Financial Truth Layers**

The KB should model financial truth across systems:

```text
Marketplace KB
Commercial settlement truth:
orders, refunds, commissions, fees, reimbursements, marketplace payouts.

Payment Gateway KB
Collection and payout truth:
payments captured, fees, refunds, chargebacks, payout batches, gateway settlement.

Logistics KB
Shipment and COD truth:
shipments, AWBs, delivery, RTO, freight billing, COD collection, courier remittance.

Banking KB
Cash movement truth:
bank credits, bank debits, UTRs, references, narrations, actual money received or paid.

Accounting / ERP KB
Book truth:
invoices, journal entries, ledgers, receivables, payables, revenue recognition.
```

A user question may touch one layer or multiple layers.

Business Flow Binding helps identify which tenant/group platform accounts participate when the question crosses layers.

---

## **13.6 Business Hierarchy Principle**

Business Hierarchy should encode:

```text
Identity
Ownership
Platform account membership
Platform context
Account-to-data bindings
Named reusable business scopes
Role-based cross-platform business flow bindings
```

It should not encode:

```text
Metric formulas
SQL patterns
Workflow internals
Reconciliation matching internals
Validation tests
Output contracts
```

Key principle:

```text
Platform Account is atomic.
Account Data Binding maps accounts to table filters.
Business Scope Set names durable reusable account groups.
Business Flow Binding maps tenant/group-specific account participation in reusable business flows.
```

---

## **13.7 Account Data Binding Principle**

Account Data Binding answers:

```text
How does this platform account appear in this table?
```

Examples:

```text
Amazon seller account → amazon_settlement → group_level_id = 22
Razorpay merchant account → razorpay_payouts → merchant_id = rzp_live_xxx
HDFC current account → bank_statement → bank_account_id = hdfc_current_xxx
Shiprocket account → shiprocket_oms → group_level_id = 203
```

It should not answer:

```text
Which accounts participate together in a flow?
Which process is being executed?
What should match?
What SQL should run?
```

Those belong elsewhere.

---

## **13.8 Business Scope Set Principle**

Business Scope Set answers:

```text
Which accounts are included in this named reusable scope?
```

Use it for durable business groupings such as:

```text
Acme India Amazon All Accounts
Acme India Operating Bank Accounts
Acme India Marketplace Accounts
Acme India Razorpay to HDFC Reconciliation Scope
```

Do not create Business Scope Sets for every possible ad-hoc account combination.

Business Scope Set is about reusable grouping. It is not enough to model role-based flows.

---

## **13.9 Business Flow Binding Principle**

Business Flow Binding answers:

```text
For this tenant/group/business scope,
when this process or money-flow path is relevant,
which platform accounts participate,
what roles do they play,
under what conditions,
and which evidence path should retrieval consider?
```

It is the generic primitive for:

```text
marketplace → logistics
marketplace → payment gateway
payment gateway → bank
marketplace → bank
logistics COD → bank
refund → gateway/bank
ERP/accounting → bank
```

Do not create separate binding card types such as:

```text
Logistics Route Binding
Payment Route Binding
Bank Route Binding
Marketplace Settlement Route Binding
```

Use one abstraction:

```text
Business Flow Binding
```

---

## **13.10 Data Understanding Principle**

Data Understanding should encode:

```text
Tables
Columns
Relationships
Value profiles
Grain
Date safety
Join safety
Data quality caveats
Structural applicability
```

It should not encode:

```text
Tenant ownership
Account-level filters
Cross-platform tenant/group flow participation
Metric formulas
Process flow
Reconciliation matching logic
Query templates
```

Key principle:

```text
Tables and columns describe data structure.
Relationships describe structural joinability.
Account Data Binding describes account-specific filters.
Business Flow Binding describes tenant/group-specific applicability of cross-platform evidence paths.
```

---

## **13.11 Metric Understanding Principle**

Metric Understanding should encode:

```text
Metric meaning
Metric aliases
Metric type
Formula logic
Metric implementations
Formula templates
Metric dependencies
Allowed dimensions and grains
```

It should not encode:

```text
Runtime account selection
Account-specific filters
Cross-platform flow participation
Workflow steps
Reconciliation matching
Validation tests
Output contracts
```

Key principle:

```text
Metric Card = what the number means.
Metric Implementation = how the number is calculated when that formula is valid.
Runtime Scope = whose data the metric applies to for this question.
Account Data Binding = how selected accounts become filters.
Business Flow Binding = only needed when the metric question crosses platform families or requires a flow-specific evidence path.
```

---

## **13.12 Process Understanding Principle**

Process Understanding should encode:

```text
Domains
Business processes
Workflow steps
State transitions
Expected lags
Process failure modes
Process variants
```

It should not encode:

```text
Tenant/account participation
Table schemas
Metric formulas
Matching keys
SQL patterns
Validation tests
Output contracts
```

Key principle:

```text
Business Process defines what should happen generically.
Business Flow Binding defines which tenant/group accounts participate in that process.
Reconciliation Understanding defines what should match.
```

---

## **13.13 Reconciliation Understanding Principle**

Reconciliation Understanding should encode:

```text
Reconciliation profiles
Reconciliation sides
Reconciliation units
Matching logic
Mismatch categories
Tolerances
Alignment types
Reconciliation variants
```

It should not encode:

```text
Tenant/account participation
Table schemas
Account filters
SQL query shape
Output schemas
Validation checks
```

Key principle:

```text
There is no universal reconciliation grain.
Each reconciliation profile defines its own primary unit, secondary keys, fallback logic, and mismatch semantics.
Business Flow Binding decides which tenant/group platform accounts participate in that matching model.
```

---

## **13.14 Execution Guidance Principle**

Execution Guidance should encode:

```text
Query patterns
Rules
Validation tests
Output contracts
Execution constraint sets
Join constraints
Aggregation safeguards
Date safety rules
Double-counting prevention
Business Flow Binding requirement checks for cross-platform flows
```

It should not encode:

```text
Orchestrator planning
Tool execution
Retry logic
Runtime account selection
Raw business process definitions
Generic process semantics
Reconciliation concept definitions
```

Key principle:

```text
Execution Guidance constrains execution.
It does not replace the orchestrator.
```

---

## **13.15 Scope Explosion Prevention**

Do not create cards for every possible account combination.

Correct pattern:

```text
Create Platform Account cards for atomic accounts.
Create Account Data Binding cards for account-table filters.
Create Business Scope Set cards only for named, reusable business scopes.
Create Business Flow Binding cards only for durable, reusable, role-based cross-platform flows.
Use Runtime Scope for ad-hoc combinations.
```

Do not create:

```text
one metric implementation per account when formula is unchanged
one process card per customer account
one reconciliation profile per account pair
one Business Scope Set for every account combination
one Business Flow Binding for every temporary user query
logistics/payment/banking-specific route binding card types
```

---

## **13.16 Applicability vs Runtime Scope vs Binding**

Keep these separate:

```text
Applicability Scope:
Where a card’s knowledge is valid.

Runtime Scope:
Whose data the user wants for this question.

Account Data Binding:
How selected accounts map to table filters.

Business Scope Set:
What reusable account group has a business name.

Business Flow Binding:
Which platform accounts participate together in a reusable tenant/group-specific flow.
```

This prevents metric implementation, process, reconciliation, and execution guidance cards from becoming tenant/account-combination-specific by default.

---

## **13.17 Money-Flow Path Principle**

Money-flow path is not the same as platform type.

Examples:

```text
payment_gateway_to_bank
marketplace_to_bank
logistics_cod_to_bank
marketplace_to_payment_gateway
refund_to_bank
bank_credit_identification
order_to_shipment
shipment_to_freight_invoice
cod_delivery_to_courier_remittance
```

Money-flow path helps classify the kind of flow.

Business Flow Binding maps that generic path to tenant/group-specific participating accounts.

Example:

```text
payment_gateway_to_bank
= generic money-flow path

business_flow_binding.acme_india.razorpay_to_hdfc
= Acme India’s specific implementation using Razorpay as payout source and HDFC as bank destination
```

Example:

```text
logistics_cod_to_bank
= generic money-flow path

business_flow_binding.acme_india.shiprocket_cod_to_hdfc
= Acme India’s specific implementation using Shiprocket as COD remittance source and HDFC as bank destination
```

---

## **13.18 Platform-Agnostic Design Principle**

The KB should not be designed only around marketplaces.

It should support:

```text
Marketplaces
Payment gateways
Banking platforms
Logistics platforms
ERP systems
Accounting systems
D2C/ecommerce stores
Custom sources
```

That is why the design uses:

```text
Platform
Platform Context
Platform Account
Account Data Binding
Business Scope Set
Business Flow Binding
```

instead of only:

```text
Marketplace
Marketplace Account
```

---

## **13.19 Financial Truth vs Flow Participation**

Financial truth layers explain what each system knows.

Business Flow Binding explains how those systems participate together for a tenant/group.

Example:

```text
Marketplace KB tells commercial settlement truth.
Banking KB tells cash movement truth.
Business Flow Binding tells whether Acme India Amazon settlement should be matched to Acme India HDFC bank credits.
```

Example:

```text
Logistics KB tells shipment, freight, COD, and remittance truth.
Banking KB tells cash movement truth.
Business Flow Binding tells whether Shiprocket COD remittance should be matched to HDFC or ICICI bank credits for this tenant/group.
```

---

## **13.20 Raw Markdown Principle**

Raw markdown should be:

```text
Human-readable
Business-first
Editable by domain experts
Structured enough for semantic chunking
Consistent enough for card extraction
```

Raw markdown should not be:

```text
Card YAML
Canonical JSON
Graph-edge syntax
A code-generation artifact
A schema dump
```

Important:

```text
Business Flow Binding can be described in raw markdown prose.
The actual Business Flow Binding card should be extracted into intermediate YAML and validated before becoming canonical.
```

---

## **13.21 Retrieval Principle**

Retrieval should follow this logic:

```text
Deterministic retrieval locks identity and scope.
Semantic retrieval finds business intent.
Business Flow Binding resolves cross-platform account participation when needed.
Graph traversal collects dependencies.
Metadata filters enforce applicability.
Completeness checks prevent unsafe handoff.
Evidence metadata preserves auditability.
```

Business Flow Binding should be retrieved when the question crosses platform families, such as:

```text
marketplace → logistics
marketplace → bank
payment gateway → bank
logistics COD → bank
refund → gateway/bank
ERP/accounting → bank
```

It is usually not required for simple single-platform metric questions.

---

## **13.22 Key Anti-Patterns**

Avoid:

```text
Putting group_level_id directly on Group Card as a universal property.
Putting merchant_id directly on Metric Implementation as account logic.
Creating one metric implementation per account when the formula is unchanged.
Creating Business Scope Sets for every possible account combination.
Creating Business Flow Bindings for one-off user questions.
Creating Logistics Route Binding, Payment Route Binding, or Bank Route Binding as separate card types.
Putting SQL execution plans inside process cards.
Putting reconciliation matching logic inside data relationships.
Putting tenant/account participation inside generic business process cards.
Putting validation tests inside metric definitions.
Using platform_id as the only scoping mechanism.
Hardcoding tenant filters inside table cards.
Mixing Runtime Scope with Applicability Scope.
Treating bank statement as just another payout table.
Treating payment captured as equal to cash realized.
Treating COD delivered as equal to COD remitted.
Treating FBF as the logistics primitive instead of platform_fulfilled.
Treating group_level_id as the scope primitive instead of Account Data Binding.
Expanding into all domains when only one money-flow path is relevant.
```

---

## **13.23 Final Mental Model**

```text
Business Hierarchy tells us whose world we are in.
Platform Account tells us which connected accounts exist.
Account Data Binding tells us how selected accounts map to tables.
Business Scope Set tells us which named account group is reusable.
Business Flow Binding tells us which accounts participate together in a reusable flow.
Data Understanding tells us where evidence lives.
Metric Understanding tells us what numbers mean.
Process Understanding tells us what should happen.
Reconciliation Understanding tells us what should match.
Execution Guidance tells us how to stay safe.
Evidence metadata tells us where the knowledge came from.
```

---

## **13.24 Final Takeaway**

```text
Do not model only data systems.
Model how financial truth flows across marketplaces, payment gateways, logistics systems, banks, ERP, and accounting systems.

Do not solve every cross-platform problem with a new binding type.
Use Business Flow Binding as the generic tenant/group-specific flow primitive.

Do not make raw markdown into card YAML.
Let raw markdown stay human-readable and let the ingestion pipeline extract structured cards, edges, indexes, and evidence metadata.
```
