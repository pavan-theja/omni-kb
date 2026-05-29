# **9. Applicability & Scope Model**

**Status:** Draft — V4.0
**Phase:** 1 — KB Schema & Card Design
**Scope:** Tenant-aware, platform-agnostic scope model for analytics, reconciliation, diagnostics, and money-flow reasoning

---

## **Purpose of this section**

The Applicability & Scope Model explains how ZenStatement separates:

```text
Where knowledge is valid
from
Whose data is being queried
from
How accounts map to warehouse filters
from
Which platform accounts participate together in a business flow
```

This section answers:

* When should a card be global, platform-type-level, platform-level, platform-context-level, tenant-level, group-level, account-level, process-level, or flow-level?
* How should metric implementations apply across all accounts, selected accounts, or one account?
* When should we use a named Business Scope Set?
* When should we avoid creating Business Scope Sets?
* How do Account Data Bindings convert selected platform accounts into SQL filters?
* How does Business Flow Binding connect platform accounts for marketplace → logistics, payment gateway → bank, logistics COD → bank, marketplace → bank, refund → bank, or ERP/accounting flows?
* How should overrides work when a more specific rule, implementation, process variant, or reconciliation variant exists?

---

## **9.1 Core Principle**

Do not use one field like `platform_id`, `account_id`, or `group_level_id` to solve every scoping problem.

There are five different ideas:

```text
1. Applicability Scope
   Where a knowledge card is valid.

2. Runtime Scope
   Which tenant, group, platform, platform context, accounts, dates, and filters the user is asking about.

3. Account Data Binding
   How selected platform accounts become table-level filters.

4. Business Scope Set
   A durable, named, reusable group of platform accounts.

5. Business Flow Binding
   Which platform accounts participate together in a tenant/group-specific business process or money-flow path.
```

These must remain separate.

---

## **9.2 Applicability Scope**

Applicability Scope describes where a card's knowledge is valid.

Examples:

```text
This metric implementation is valid for Amazon India settlement data.
This process model is valid for payment-gateway-to-bank reconciliation.
This matching logic is valid for payout-to-bank-credit matching.
This query pattern is valid for settlement waterfall analysis.
This logistics metric implementation is valid for Shiprocket COD settlement rows.
```

Applicability is about **knowledge validity**, not runtime account selection.

Correct:

```text
metric_impl.amazon_settlement.seller_realization_rate is valid for Amazon settlement tables.
```

Incorrect:

```text
metric_impl.amazon_settlement.seller_realization_rate is only for group_level_id = 22.
```

If the formula is the same, the implementation should remain reusable. Account selection happens later.

---

## **9.3 Runtime Scope**

Runtime Scope is the scope selected for a specific user question.

Examples:

```text
Acme India Amazon all accounts
Acme India Razorpay primary account
Acme India Razorpay + HDFC reconciliation
Acme India Shopify → Shiprocket logistics flow
group_level_id 26 only
all revenue channels for Acme India
last month
COD orders only
```

Runtime Scope is usually resolved during retrieval/context assembly. It should not be pre-created as cards for every possible combination.

Runtime Scope can include:

```text
tenant
group
platform
platform context
platform account
business scope set
business flow binding
time range
user filters
semantic filters
```

---

## **9.4 Account Data Binding**

Account Data Binding maps a selected Platform Account to table-level filters.

Example:

```text
Platform Account:
Acme Amazon India Primary

Table:
zs_observe.amazon_settlement

Binding:
group_level_id = 22
```

Another example:

```text
Platform Account:
Acme Razorpay Primary

Table:
zs_observe.razorpay_payments

Binding:
merchant_id = 'rzp_live_xxx'
```

Another example:

```text
Platform Account:
Acme HDFC Current Account

Table:
zs_observe.bank_statement

Binding:
bank_account_id = 'hdfc_current_xxx'
```

This means table, metric, process, reconciliation, and query pattern cards do not need to hardcode account filters.

---

## **9.5 Business Scope Set**

A Business Scope Set is a named, reusable business scope.

It should exist only when the grouping has durable business meaning.

Examples:

```text
Acme India Amazon All Accounts
Acme India Razorpay All Accounts
Acme India HDFC Operating Bank Accounts
Acme India Razorpay → HDFC Reconciliation Scope
Acme India Marketplace → Bank Reconciliation Scope
Acme India COD Logistics → Bank Scope
Acme India All Revenue Channels
```

It should not be used to pre-create every possible account combination.

Business Scope Set is mostly about reusable account grouping.

It answers:

```text
Which accounts are included in this named business scope?
```

It does not fully answer:

```text
Which accounts play which roles in a process or money-flow path?
```

That is the job of Business Flow Binding.

---

## **9.6 Business Flow Binding**

Business Flow Binding represents tenant/group-specific cross-platform applicability.

It answers:

```text
For this tenant/group/business scope,
when this process or money-flow path is relevant,
which platform accounts participate,
what roles do they play,
under what conditions,
and which evidence paths should retrieval consider?
```

Business Flow Binding is the scalable replacement for narrow ideas like:

```text
Logistics Route Binding
Payment Route Binding
Bank Route Binding
Marketplace Settlement Route Binding
```

Use one generic primitive instead:

```text
Business Flow Binding
```

It can represent:

```text
marketplace → logistics
marketplace → bank
marketplace → payment gateway
payment gateway → bank
logistics COD → bank
refund → gateway/bank
ERP/accounting → bank
```

---

## **9.7 Why Business Flow Binding Is Separate**

Business Flow Binding is not the same as Platform Account.

```text
Platform Account = this connected account exists.
Business Flow Binding = these connected accounts participate together in this flow.
```

Business Flow Binding is not the same as Account Data Binding.

```text
Account Data Binding = this account maps to this table filter.
Business Flow Binding = these accounts and evidence paths are relevant together.
```

Business Flow Binding is not the same as Business Scope Set.

```text
Business Scope Set = reusable named account group.
Business Flow Binding = role-based flow participation across accounts.
```

Business Flow Binding is not the same as Business Process.

```text
Business Process = generic expected flow.
Business Flow Binding = tenant/group-specific accounts participating in that flow.
```

Business Flow Binding is not the same as Reconciliation Profile.

```text
Reconciliation Profile = what should match.
Business Flow Binding = which tenant/group accounts are involved in that matching.
```

---

## **9.8 Recommended Applicability Scope Shape**

Cards that need applicability should use a flexible structure like this:

```json
{
  "applicability_scope": {
    "scope_level": "global | platform_type | platform | platform_context | tenant | group | platform_account | business_scope_set | business_flow_binding | process | reconciliation_profile",
    "tenant_ids": [],
    "group_ids": [],
    "platform_types": [],
    "platform_ids": [],
    "platform_context_ids": [],
    "platform_account_ids": [],
    "business_scope_set_ids": [],
    "business_flow_binding_ids": [],
    "business_process_ids": [],
    "reconciliation_profile_ids": [],
    "notes": []
  }
}
```

Not every card needs every field. The shape is flexible.

Guidance:

```text
Use platform_type/platform/platform_context when the knowledge is broadly reusable.
Use platform_account only when the knowledge truly changes for a specific account.
Use business_scope_set only when the knowledge applies to a named reusable scope.
Use business_flow_binding only when the knowledge applies to a specific role-based cross-platform flow.
```

---

## **9.9 Runtime Scope Resolution Shape**

A resolved runtime scope can look like this:

```yaml
runtime_scope:
  tenant_id: tenant.acme_retail
  group_id: group.acme_india
  platform_ids:
    - platform.razorpay
    - platform.hdfc_bank
  platform_account_ids:
    - platform_account.acme.razorpay.primary
    - platform_account.acme.hdfc.current
  business_scope_set_ids:
    - business_scope_set.acme_india.razorpay_to_hdfc
  business_flow_binding_ids:
    - business_flow_binding.acme_india.razorpay_to_hdfc
  date_range:
    start_date: 2026-04-01
    end_date: 2026-04-30
  semantic_filters:
    - payout_status IN [processed, paid]
    - bank_transaction_direction = credit
  account_data_binding_ids:
    - account_data_binding.acme.razorpay.primary.razorpay_payouts
    - account_data_binding.acme.hdfc.current.bank_statement
```

This runtime scope is not necessarily persisted as a card. It is assembled during retrieval/context construction.

---

## **9.10 Example — Metric Applies to All Accounts**

User asks:

```text
Show seller realization for Acme India Amazon.
```

Metric Implementation:

```json
{
  "card_type": "metric_implementation",
  "canonical_id": "metric_impl.amazon_settlement.seller_realization_rate",
  "metric_id": "metric.seller_realization_rate",
  "applicability_scope": {
    "scope_level": "platform_context",
    "platform_ids": ["platform.amazon"],
    "platform_context_ids": ["platform_context.amazon.in"],
    "notes": [
      "Formula is valid for Amazon India settlement data. Runtime account filters come from Account Data Binding."
    ]
  },
  "base_tables": ["table.zs_observe.amazon_settlement"]
}
```

Runtime scope resolves to:

```text
Acme India Amazon all accounts
```

Account Data Bindings produce:

```sql
group_level_id IN (22, 26)
```

No separate metric implementation is needed for all accounts.

---

## **9.11 Example — Metric Applies to Selected Accounts**

User asks:

```text
Show seller realization for only the primary Amazon account.
```

Metric Implementation remains the same.

Runtime scope resolves to:

```text
platform_account.acme.amazon_in.primary
```

Account Data Binding produces:

```sql
group_level_id = 22
```

No new metric implementation is needed.

---

## **9.12 Example — Metric Applies to One Specific group_level_id**

User asks:

```text
Show seller realization for group_level_id 26.
```

Runtime scope maps `group_level_id = 26` to:

```text
platform_account.acme.amazon_in.secondary
```

Account Data Binding confirms:

```sql
group_level_id = 26
```

Metric Implementation remains the same.

---

## **9.13 Example — Marketplace to Logistics Flow**

User asks:

```text
Which Shopify COD orders were delivered but not remitted by courier?
```

Runtime scope needs more than a Shopify account. It needs the applicable logistics flow.

Business Flow Binding resolves:

```text
business_flow_binding.acme_india.shopify_to_shiprocket
```

Participants:

```text
Shopify account = order_source
Shiprocket account = logistics_source
```

Relevant process:

```text
business_process.order_to_shipment_flow
business_process.logistics_cod_to_bank_reconciliation, if bank credit is involved
```

Relevant evidence path:

```text
shopify_oms
→ shiprocket_oms
→ shiprocket_settlement
→ bank statement, only if bank reconciliation is required
```

Account Data Bindings then inject table filters for each selected account/table.

---

## **9.14 Example — Payment Gateway to Bank Flow**

User asks:

```text
Why does Razorpay payout not match HDFC bank credit for Acme India last month?
```

Business Flow Binding resolves:

```text
business_flow_binding.acme_india.razorpay_to_hdfc
```

Participants:

```text
Razorpay account = payout_source
HDFC account = bank_destination
```

Relevant process:

```text
business_process.payment_gateway_to_bank_reconciliation
```

Relevant reconciliation profile:

```text
reconciliation_profile.payment_gateway_payout_to_bank_credit
```

Relevant evidence path:

```text
razorpay_payouts
→ bank_statement
```

Account Data Bindings then inject:

```text
Razorpay merchant filter
HDFC bank account filter
```

---

## **9.15 Example — Logistics COD to Bank Flow**

User asks:

```text
COD was delivered but cash has not reached the bank.
```

Business Flow Binding may resolve one or more applicable COD-to-bank flows:

```text
business_flow_binding.acme_india.shiprocket_cod_to_hdfc
business_flow_binding.acme_india.ekart_cod_to_icici
business_flow_binding.acme_india.delhivery_cod_to_hdfc
```

Participants:

```text
logistics account = COD remittance source
bank account = bank destination
```

Conditions:

```text
payment_mode = COD
shipment status = delivered
remittance status = settled/remitted, where available
```

Evidence path:

```text
shipment / AWB
→ courier settlement / COD remittance
→ UTR / bank reference
→ bank credit
```

The generic reconciliation profile remains reusable. Business Flow Binding decides which tenant/group accounts and evidence tables participate.

---

## **9.16 When To Create a Business Scope Set**

Create a Business Scope Set only when the scope is:

```text
Named
Reusable
Business meaningful
Likely to be queried repeatedly
Useful for reporting, reconciliation, diagnostics, or operations
```

Examples:

```text
Acme India Amazon All Accounts
Acme India All Marketplace Accounts
Acme India Operating Bank Accounts
Acme India Razorpay to HDFC Reconciliation Scope
Acme India COD Logistics to Bank Scope
```

Do not create Business Scope Sets for temporary one-off combinations.

---

## **9.17 When To Create a Business Flow Binding**

Create a Business Flow Binding when all of these are true:

```text
The flow is tenant/group-specific.
Multiple platform accounts participate together.
The roles of the accounts matter.
The flow is expected to be reused.
The flow supports analytics, diagnostics, reconciliation, or operational investigation.
The flow changes which evidence tables or relationships should be considered.
```

Good examples:

```text
Acme India Shopify → Shiprocket fulfilment flow
Acme India Razorpay → HDFC payout-to-bank flow
Acme India Amazon → HDFC marketplace settlement-to-bank flow
Acme India Ekart COD → ICICI bank flow
Acme India marketplace refunds → Razorpay refunds → bank debit flow
```

Do not create a Business Flow Binding when:

```text
Only one platform account is involved.
The user asked a one-off ad hoc combination.
The flow does not change retrieval, evidence, or account roles.
A Business Scope Set is enough.
The relationship is purely structural and belongs in Relationship Card.
```

---

## **9.18 When To Create a More Specific Implementation**

Create a more specific metric implementation, process variant, reconciliation variant, or rule only when the underlying logic changes.

Examples:

```text
Amazon India and Amazon US use different tables or column meanings.
Razorpay and Amazon calculate net collected amount differently.
A specific account has special fee treatment.
A process variant changes expected workflow steps or lag.
A reconciliation variant changes matching unit, tolerance, or fallback logic.
A specific business flow changes the evidence path or required table family.
```

Do not create a new implementation merely because selected accounts changed.

---

## **9.19 Override Precedence**

When multiple cards could apply, use the most specific valid card.

Recommended precedence:

```text
1. Platform account-specific override
2. Business flow binding-specific override
3. Business scope set-specific override
4. Group-specific override
5. Tenant-specific override
6. Platform context-specific implementation
7. Platform-specific implementation
8. Platform type-specific implementation
9. Global/default implementation
```

This lets the system use generic knowledge by default while still allowing specific overrides.

Important:

```text
Business Flow Binding is usually not an override.
It is usually an applicability selector.
```

It becomes part of override precedence only when a rule, query pattern, process variant, or matching variant is explicitly valid for that flow.

---

## **9.20 What Not To Do**

Do not create combinations like:

```text
Amazon primary + Razorpay secondary + HDFC account 3
Amazon secondary + Shiprocket account 2 + ICICI account 1
Razorpay account 1 + HDFC account 1 + HDFC account 2 for one temporary question
```

These should be runtime scopes, not persisted cards, unless they become durable named business scopes or durable business flows.

Avoid:

```text
Putting group_level_id directly on Group Card as universal truth.
Putting merchant_id directly on Metric Implementation as account logic.
Putting bank_account_id directly on a bank reconciliation profile.
Creating one metric implementation per account when the formula is unchanged.
Creating Business Scope Sets for every possible account combination.
Creating Business Flow Bindings for one-off user questions.
Putting cross-platform participant roles inside Table Cards.
Putting reconciliation matching logic inside Business Flow Binding.
Putting SQL execution plans inside Business Flow Binding.
Using platform_id as the only scoping mechanism.
Mixing Runtime Scope with Applicability Scope.
```

---

## **9.21 Responsibility Matrix**

| Concept                | Owns                                                                     | Should not own                                        |
| ---------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------- |
| Applicability Scope    | Where knowledge is valid                                                 | Runtime selected accounts or filters                  |
| Runtime Scope          | The user-selected tenant/group/accounts/date/filter context              | Persistent card logic by default                      |
| Account Data Binding   | Account-to-table filter mapping                                          | Metric formulas, process logic, cross-platform roles  |
| Business Scope Set     | Durable named account group                                              | Every temporary combination or detailed process roles |
| Business Flow Binding  | Tenant/group-specific cross-platform participant roles and evidence path | Generic process logic, matching tolerances, SQL plans |
| Business Process       | Generic expected workflow                                                | Tenant/account-specific participation                 |
| Reconciliation Profile | Generic matching model                                                   | Tenant/account-specific account roles                 |
| Relationship Card      | Structural table joinability                                             | Tenant/group flow applicability                       |
| Query Pattern          | Safe query shape                                                         | Account filter values or flow participant selection   |

---

## **9.22 Final Principle**

```text
Applicability Scope decides whether knowledge is valid.
Runtime Scope decides whose data and which filters are involved now.
Account Data Binding decides how selected accounts become table filters.
Business Scope Set names reusable account groups.
Business Flow Binding decides which platform accounts participate together in a reusable tenant/group-specific flow.
```

Keeping these separate prevents card explosion, keeps the KB reusable, and lets ZenStatement evolve from marketplace-only analytics into full money-flow reasoning across marketplaces, logistics, payment gateways, banks, ERP, and accounting systems.
