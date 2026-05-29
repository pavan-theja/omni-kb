# **10. Graph Relationships**

**Status:** Draft - V4.0
**Phase:** 1 — KB Schema & Card Design   
**Scope:** Tenant-aware knowledge base for GraphRAG-driven SQL generation

## **Purpose of this section**

Graph Relationships define how cards connect to each other when ingested into Cognee or any graph-backed knowledge system.

This section answers:

* Which cards should be connected?
* What edge names should be used?
* Which relationships are structural?
* Which relationships are semantic?
* Which relationships support scope resolution?
* Which relationships support account-to-table filtering?
* Which relationships support cross-platform business flow resolution?
* Which relationships support metric, process, reconciliation, and execution guidance?
* How do we avoid embedding too many lists inside cards when graph edges can represent relationships better?

The major addition in this version is explicit graph support for:

```text
Business Flow Binding
```

Business Flow Binding connects tenant/group-specific business reality to reusable platform, data, process, reconciliation, and execution cards.

---

## **10.1 Design Principle**

Cards should be atomic knowledge units.

Relationships should explain how those units connect.

```text
Card = thing we know
Edge = how it relates to another thing
```

Use simple, uppercase, stable edge names.

The graph should support three kinds of traversal:

```text
1. Identity traversal
   Tenant → Group → Platform Account

2. Evidence traversal
   Platform Account → Account Data Binding → Table → Column / Relationship / Value Profile

3. Flow traversal
   Business Flow Binding → Participating Platform Accounts → Evidence Tables → Process / Reconciliation / Execution cards
```

---

## **10.2 Business Hierarchy Relationships**

| Source               | Edge                             | Target               | Meaning                                                         |
| -------------------- | -------------------------------- | -------------------- | --------------------------------------------------------------- |
| `Tenant`             | `HAS_GROUP`                      | `Group`              | Tenant contains a group / business unit.                        |
| `Group`              | `BELONGS_TO_TENANT`              | `Tenant`             | Group belongs to tenant.                                        |
| `Group`              | `HAS_PLATFORM_ACCOUNT`           | `PlatformAccount`    | Group owns or operates a platform account.                      |
| `PlatformAccount`    | `BELONGS_TO_GROUP`               | `Group`              | Platform account belongs to a group.                            |
| `PlatformAccount`    | `BELONGS_TO_TENANT`              | `Tenant`             | Platform account belongs to a tenant.                           |
| `PlatformAccount`    | `USES_PLATFORM`                  | `Platform`           | Platform account is on a source platform.                       |
| `PlatformAccount`    | `HAS_PLATFORM_CONTEXT`           | `PlatformContext`    | Platform account operates in a platform context.                |
| `Platform`           | `HAS_PLATFORM_CONTEXT`           | `PlatformContext`    | Platform has a country, region, instance, or operating context. |
| `PlatformContext`    | `BELONGS_TO_PLATFORM`            | `Platform`           | Platform context belongs to a platform.                         |
| `PlatformAccount`    | `HAS_DATA_BINDING`               | `AccountDataBinding` | Account has table-level data binding.                           |
| `AccountDataBinding` | `BINDS_PLATFORM_ACCOUNT`         | `PlatformAccount`    | Binding belongs to a platform account.                          |
| `AccountDataBinding` | `APPLIES_TO_TABLE`               | `Table`              | Binding applies to a specific table.                            |
| `BusinessScopeSet`   | `BELONGS_TO_GROUP`               | `Group`              | Named scope belongs to a group.                                 |
| `BusinessScopeSet`   | `BELONGS_TO_TENANT`              | `Tenant`             | Named scope belongs to a tenant.                                |
| `BusinessScopeSet`   | `INCLUDES_PLATFORM_ACCOUNT`      | `PlatformAccount`    | Named scope includes one or more accounts.                      |
| `PlatformAccount`    | `INCLUDED_IN_BUSINESS_SCOPE_SET` | `BusinessScopeSet`   | Platform account is part of a named scope.                      |

---

## **10.3 Business Flow Binding Relationships**

Business Flow Binding is the tenant/group-specific graph bridge for cross-platform flows.

It should be used for relationships such as:

```text
marketplace → logistics
marketplace → payment gateway
payment gateway → bank
marketplace → bank
logistics COD → bank
refund → gateway/bank
ERP/accounting → bank
```

It should not replace generic Business Process, Reconciliation Profile, or Relationship cards. It only says which tenant/group platform accounts participate in a reusable business flow.

| Source                | Edge                                | Target                   | Meaning                                                                                   |
| --------------------- | ----------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------- |
| `Group`               | `HAS_BUSINESS_FLOW_BINDING`         | `BusinessFlowBinding`    | Group has a tenant/group-specific business flow.                                          |
| `Tenant`              | `HAS_BUSINESS_FLOW_BINDING`         | `BusinessFlowBinding`    | Tenant has a business flow binding.                                                       |
| `BusinessFlowBinding` | `BELONGS_TO_GROUP`                  | `Group`                  | Flow binding belongs to group.                                                            |
| `BusinessFlowBinding` | `BELONGS_TO_TENANT`                 | `Tenant`                 | Flow binding belongs to tenant.                                                           |
| `BusinessFlowBinding` | `USES_PLATFORM_ACCOUNT`             | `PlatformAccount`        | Flow uses a platform account.                                                             |
| `BusinessFlowBinding` | `USES_SOURCE_ACCOUNT`               | `PlatformAccount`        | Flow uses this account as the source side.                                                |
| `BusinessFlowBinding` | `USES_TARGET_ACCOUNT`               | `PlatformAccount`        | Flow uses this account as the target/destination side.                                    |
| `BusinessFlowBinding` | `USES_OPERATIONAL_EVIDENCE_ACCOUNT` | `PlatformAccount`        | Flow uses this account for operational evidence, such as shipment or fulfilment evidence. |
| `BusinessFlowBinding` | `USES_SETTLEMENT_SOURCE_ACCOUNT`    | `PlatformAccount`        | Flow uses this account as a settlement, payout, or remittance source.                     |
| `BusinessFlowBinding` | `USES_BANK_DESTINATION_ACCOUNT`     | `PlatformAccount`        | Flow uses this account as bank destination or cash-realization side.                      |
| `BusinessFlowBinding` | `USES_ACCOUNT_DATA_BINDING`         | `AccountDataBinding`     | Flow requires account-to-table binding for execution.                                     |
| `BusinessFlowBinding` | `USES_TABLE`                        | `Table`                  | Flow commonly uses this evidence table.                                                   |
| `BusinessFlowBinding` | `USES_RELATIONSHIP`                 | `Relationship`           | Flow commonly uses this join or relationship path.                                        |
| `BusinessFlowBinding` | `SUPPORTS_PROCESS`                  | `BusinessProcess`        | Flow is an implementation/applicability binding for a generic business process.           |
| `BusinessFlowBinding` | `SUPPORTS_RECONCILIATION_PROFILE`   | `ReconciliationProfile`  | Flow supports a generic reconciliation model.                                             |
| `BusinessFlowBinding` | `USES_QUERY_PATTERN`                | `QueryPattern`           | Flow can use this query pattern when executing.                                           |
| `BusinessFlowBinding` | `USES_EXECUTION_CONSTRAINT_SET`     | `ExecutionConstraintSet` | Flow should respect this guardrail bundle.                                                |
| `BusinessScopeSet`    | `HAS_BUSINESS_FLOW_BINDING`         | `BusinessFlowBinding`    | Named scope has an associated role-based flow binding.                                    |
| `BusinessFlowBinding` | `USES_BUSINESS_SCOPE_SET`           | `BusinessScopeSet`       | Flow binding is tied to a named business scope, where applicable.                         |

### Example graph path — Shopify to Shiprocket

```text
group.acme_india
→ HAS_BUSINESS_FLOW_BINDING
business_flow_binding.acme_india.shopify_to_shiprocket
→ USES_SOURCE_ACCOUNT
platform_account.acme.shopify.primary
→ USES_OPERATIONAL_EVIDENCE_ACCOUNT
platform_account.acme.shiprocket.primary
→ USES_TABLE
table.zs_observe.shiprocket_oms
→ USES_TABLE
table.zs_observe.shiprocket_settlement
→ SUPPORTS_PROCESS
business_process.order_to_shipment_flow
→ SUPPORTS_RECONCILIATION_PROFILE
reconciliation_profile.cod_logistics_to_bank
```

### Example graph path — Razorpay to HDFC

```text
group.acme_india
→ HAS_BUSINESS_FLOW_BINDING
business_flow_binding.acme_india.razorpay_to_hdfc
→ USES_SETTLEMENT_SOURCE_ACCOUNT
platform_account.acme.razorpay.primary
→ USES_BANK_DESTINATION_ACCOUNT
platform_account.acme.hdfc.current
→ SUPPORTS_PROCESS
business_process.payment_gateway_to_bank_reconciliation
→ SUPPORTS_RECONCILIATION_PROFILE
reconciliation_profile.payment_gateway_payout_to_bank_credit
```

---

## **10.4 Data Understanding Relationships**

| Source                | Edge                            | Target            | Meaning                                                |
| --------------------- | ------------------------------- | ----------------- | ------------------------------------------------------ |
| `Table`               | `HAS_COLUMN`                    | `Column`          | Table contains column.                                 |
| `Column`              | `BELONGS_TO_TABLE`              | `Table`           | Column belongs to table.                               |
| `Table`               | `HAS_VALUE_PROFILE`             | `ValueProfile`    | Table has value profile for a categorical column.      |
| `Column`              | `HAS_VALUE_PROFILE`             | `ValueProfile`    | Column has value profile.                              |
| `ValueProfile`        | `PROFILES_COLUMN`               | `Column`          | Value profile explains column values.                  |
| `Table`               | `HAS_RELATIONSHIP`              | `Relationship`    | Table participates in relationship card.               |
| `Relationship`        | `SOURCE_TABLE`                  | `Table`           | Relationship starts from source table.                 |
| `Relationship`        | `TARGET_TABLE`                  | `Table`           | Relationship points to target table.                   |
| `Relationship`        | `USES_SOURCE_COLUMN`            | `Column`          | Relationship uses source-side column.                  |
| `Relationship`        | `USES_TARGET_COLUMN`            | `Column`          | Relationship uses target-side column.                  |
| `Table`               | `SOURCED_FROM_PLATFORM`         | `Platform`        | Table is associated with a source platform.            |
| `Table`               | `SOURCED_FROM_PLATFORM_CONTEXT` | `PlatformContext` | Table is associated with a platform operating context. |
| `Table`               | `SOURCED_FROM_PLATFORM_TYPE`    | `PlatformType`    | Table belongs to a broad platform type.                |
| `AccountDataBinding`  | `APPLIES_TO_TABLE`              | `Table`           | Account binding applies to specific table.             |
| `BusinessFlowBinding` | `USES_TABLE`                    | `Table`           | Flow uses table as evidence.                           |
| `BusinessFlowBinding` | `USES_RELATIONSHIP`             | `Relationship`    | Flow uses a known join/evidence path.                  |

Important distinction:

```text
Relationship Card = structural table joinability.
Business Flow Binding = tenant/group-specific applicability of that relationship path.
```

---

## **10.5 Metric Understanding Relationships**

| Source                 | Edge                               | Target                 | Meaning                                                                                              |
| ---------------------- | ---------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------- |
| `Metric`               | `HAS_IMPLEMENTATION`               | `MetricImplementation` | Metric has one or more implementations.                                                              |
| `MetricImplementation` | `IMPLEMENTS_METRIC`                | `Metric`               | Implementation calculates a metric.                                                                  |
| `MetricImplementation` | `USES_TABLE`                       | `Table`                | Implementation uses table.                                                                           |
| `MetricImplementation` | `USES_COLUMN`                      | `Column`               | Implementation uses column.                                                                          |
| `MetricImplementation` | `USES_FORMULA_TEMPLATE`            | `FormulaTemplate`      | Implementation uses reusable formula.                                                                |
| `Metric`               | `DEPENDS_ON_METRIC`                | `Metric`               | Metric depends on another metric.                                                                    |
| `MetricDependency`     | `PARENT_METRIC`                    | `Metric`               | Dependency belongs to parent metric.                                                                 |
| `MetricDependency`     | `USES_DEPENDENT_METRIC`            | `Metric`               | Dependency uses another metric.                                                                      |
| `Metric`               | `BELONGS_TO_DOMAIN`                | `Domain`               | Metric belongs to domain.                                                                            |
| `Metric`               | `USED_IN_PROCESS`                  | `BusinessProcess`      | Metric is used in process.                                                                           |
| `MetricImplementation` | `APPLIES_TO_BUSINESS_FLOW_BINDING` | `BusinessFlowBinding`  | Implementation applies to a specific flow only when formula truly changes for that flow. Use rarely. |

Default rule:

```text
Do not connect MetricImplementation to BusinessFlowBinding unless the formula itself is flow-specific.
Most metrics remain platform/table/process applicable and receive runtime filters through Account Data Binding.
```

---

## **10.6 Process Understanding Relationships**

| Source                | Edge                     | Target            | Meaning                                            |
| --------------------- | ------------------------ | ----------------- | -------------------------------------------------- |
| `Domain`              | `HAS_BUSINESS_PROCESS`   | `BusinessProcess` | Domain contains process.                           |
| `BusinessProcess`     | `BELONGS_TO_DOMAIN`      | `Domain`          | Process belongs to domain.                         |
| `BusinessProcess`     | `HAS_WORKFLOW_STEP`      | `WorkflowStep`    | Process contains workflow step.                    |
| `WorkflowStep`        | `BELONGS_TO_PROCESS`     | `BusinessProcess` | Step belongs to process.                           |
| `BusinessProcess`     | `HAS_STATE_TRANSITION`   | `StateTransition` | Process has state transition.                      |
| `StateTransition`     | `BELONGS_TO_PROCESS`     | `BusinessProcess` | Transition belongs to process.                     |
| `StateTransition`     | `TRIGGERED_BY_STEP`      | `WorkflowStep`    | Workflow step triggers transition.                 |
| `BusinessProcess`     | `HAS_PROCESS_VARIANT`    | `ProcessVariant`  | Process has variant.                               |
| `ProcessVariant`      | `EXTENDS_PROCESS`        | `BusinessProcess` | Variant extends process.                           |
| `BusinessProcess`     | `USES_METRIC`            | `Metric`          | Process uses metric.                               |
| `BusinessProcess`     | `INVOLVES_PLATFORM_TYPE` | `PlatformType`    | Process involves a platform type.                  |
| `BusinessFlowBinding` | `SUPPORTS_PROCESS`       | `BusinessProcess` | Tenant/group flow participates in generic process. |
| `BusinessFlowBinding` | `USES_PROCESS_VARIANT`   | `ProcessVariant`  | Flow uses a specific process variant, if needed.   |

Important distinction:

```text
Business Process = generic expected flow.
Business Flow Binding = tenant/group-specific account participation in that flow.
```

---

## **10.7 Reconciliation Understanding Relationships**

| Source                  | Edge                              | Target                  | Meaning                                                                 |
| ----------------------- | --------------------------------- | ----------------------- | ----------------------------------------------------------------------- |
| `BusinessProcess`       | `HAS_RECONCILIATION_PROFILE`      | `ReconciliationProfile` | Process has reconciliation profile.                                     |
| `ReconciliationProfile` | `SUPPORTS_PROCESS`                | `BusinessProcess`       | Profile supports process.                                               |
| `ReconciliationProfile` | `HAS_RECONCILIATION_SIDE`         | `ReconciliationSide`    | Profile has side.                                                       |
| `ReconciliationProfile` | `HAS_PRIMARY_UNIT`                | `ReconciliationUnit`    | Profile has primary reconciliation unit.                                |
| `ReconciliationProfile` | `HAS_SECONDARY_UNIT`              | `ReconciliationUnit`    | Profile has secondary/fallback reconciliation unit.                     |
| `ReconciliationProfile` | `USES_MATCHING_LOGIC`             | `MatchingLogic`         | Profile uses matching logic.                                            |
| `MatchingLogic`         | `SUPPORTS_RECONCILIATION_PROFILE` | `ReconciliationProfile` | Matching logic supports profile.                                        |
| `ReconciliationProfile` | `HAS_MISMATCH_CATEGORY`           | `MismatchCategory`      | Profile recognizes mismatch category.                                   |
| `ReconciliationVariant` | `EXTENDS_RECONCILIATION_PROFILE`  | `ReconciliationProfile` | Variant extends base profile.                                           |
| `ReconciliationVariant` | `OVERRIDES_MATCHING_LOGIC`        | `MatchingLogic`         | Variant uses different matching logic.                                  |
| `BusinessFlowBinding`   | `SUPPORTS_RECONCILIATION_PROFILE` | `ReconciliationProfile` | Tenant/group flow supports this reconciliation model.                   |
| `BusinessFlowBinding`   | `USES_RECONCILIATION_VARIANT`     | `ReconciliationVariant` | Flow uses a specific reconciliation variant, if matching model changes. |

Important distinction:

```text
Reconciliation Profile = what should match.
Business Flow Binding = which tenant/group platform accounts participate in that matching model.
```

---

## **10.8 Execution Guidance Relationships**

| Source                   | Edge                               | Target                   | Meaning                                                             |
| ------------------------ | ---------------------------------- | ------------------------ | ------------------------------------------------------------------- |
| `QueryPattern`           | `USES_TABLE`                       | `Table`                  | Query pattern uses table.                                           |
| `QueryPattern`           | `PRODUCES_METRIC`                  | `Metric`                 | Query pattern produces metric.                                      |
| `QueryPattern`           | `USES_RECONCILIATION_PROFILE`      | `ReconciliationProfile`  | Query pattern supports reconciliation profile.                      |
| `QueryPattern`           | `REQUIRES_RULE`                    | `Rule`                   | Query pattern requires rule.                                        |
| `QueryPattern`           | `HAS_VALIDATION_TEST`              | `ValidationTest`         | Query pattern has validation test.                                  |
| `QueryPattern`           | `USES_OUTPUT_CONTRACT`             | `OutputContract`         | Query pattern expects output shape.                                 |
| `Rule`                   | `HAS_VALIDATION_TEST`              | `ValidationTest`         | Rule is enforced by validation test.                                |
| `ValidationTest`         | `ENFORCES_RULE`                    | `Rule`                   | Validation test enforces rule.                                      |
| `ExecutionConstraintSet` | `INCLUDES_RULE`                    | `Rule`                   | Constraint set includes rule.                                       |
| `ExecutionConstraintSet` | `INCLUDES_VALIDATION_TEST`         | `ValidationTest`         | Constraint set includes validation test.                            |
| `ExecutionConstraintSet` | `USES_OUTPUT_CONTRACT`             | `OutputContract`         | Constraint set uses output contract.                                |
| `ExecutionConstraintSet` | `APPLIES_TO_QUERY_PATTERN`         | `QueryPattern`           | Constraint set applies to query pattern.                            |
| `BusinessFlowBinding`    | `USES_QUERY_PATTERN`               | `QueryPattern`           | Flow can use this query pattern.                                    |
| `BusinessFlowBinding`    | `USES_EXECUTION_CONSTRAINT_SET`    | `ExecutionConstraintSet` | Flow should use this guardrail bundle.                              |
| `Rule`                   | `APPLIES_TO_BUSINESS_FLOW_BINDING` | `BusinessFlowBinding`    | Rule applies to a specific flow, only when genuinely flow-specific. |

---

## **10.9 Applicability Relationships**

Applicability can be represented either as fields inside cards or as graph edges.

Recommended graph edges:

| Source          | Edge                                | Target                  | Meaning                                                                                        |
| --------------- | ----------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------- |
| Any scoped card | `APPLIES_TO_TENANT`                 | `Tenant`                | Card applies to tenant.                                                                        |
| Any scoped card | `APPLIES_TO_GROUP`                  | `Group`                 | Card applies to group.                                                                         |
| Any scoped card | `APPLIES_TO_PLATFORM`               | `Platform`              | Card applies to platform.                                                                      |
| Any scoped card | `APPLIES_TO_PLATFORM_CONTEXT`       | `PlatformContext`       | Card applies to platform context.                                                              |
| Any scoped card | `APPLIES_TO_PLATFORM_ACCOUNT`       | `PlatformAccount`       | Card applies to platform account. Use only when logic is truly account-specific.               |
| Any scoped card | `APPLIES_TO_BUSINESS_SCOPE_SET`     | `BusinessScopeSet`      | Card applies to named business scope.                                                          |
| Any scoped card | `APPLIES_TO_BUSINESS_FLOW_BINDING`  | `BusinessFlowBinding`   | Card applies to a tenant/group-specific business flow. Use when flow-specific validity exists. |
| Any scoped card | `APPLIES_TO_PROCESS`                | `BusinessProcess`       | Card applies to process.                                                                       |
| Any scoped card | `APPLIES_TO_RECONCILIATION_PROFILE` | `ReconciliationProfile` | Card applies to reconciliation profile.                                                        |

Use applicability edges carefully.

Most cards should remain reusable across tenants and accounts. Account-specific scope should usually be represented through Account Data Binding and runtime scope, not by over-scoping every card.

---

## **10.10 Edge Naming Convention**

Use:

```text
UPPERCASE_WITH_UNDERSCORES
```

Good examples:

```text
HAS_GROUP
USES_TABLE
HAS_IMPLEMENTATION
REQUIRES_RULE
HAS_VALIDATION_TEST
APPLIES_TO_PLATFORM_CONTEXT
USES_PLATFORM_ACCOUNT
SUPPORTS_RECONCILIATION_PROFILE
USES_ACCOUNT_DATA_BINDING
```

Avoid vague edge names:

```text
RELATED_TO
CONNECTED_TO
HAS_LINK
REFERENCES
```

Use vague edges only as temporary fallback during ingestion experiments.

---

## **10.11 Graph Traversal Principles**

A clean graph should support bounded traversal.

### Analytical traversal

```text
Tenant / Group
→ Platform Account
→ Account Data Binding
→ Metric
→ Metric Implementation
→ Table
→ Column
→ Rule / Validation Test
```

### Cross-platform reconciliation traversal

```text
Tenant / Group
→ Business Flow Binding
→ Participating Platform Accounts
→ Account Data Bindings
→ Business Process
→ Reconciliation Profile
→ Sides / Units / Matching Logic
→ Tables / Relationships / Columns
→ Query Pattern / Rules / Output Contract
```

### Logistics traversal

```text
Marketplace or channel account
→ Business Flow Binding
→ Logistics account
→ Shipment / AWB evidence tables
→ Freight / COD / remittance tables
→ Bank account, only if the flow crosses into bank reconciliation
```

### Payment-to-bank traversal

```text
Payment gateway account
→ Business Flow Binding
→ Bank account
→ Payout table
→ Bank statement table
→ Matching logic
→ Reconciliation output contract
```

---

## **10.12 Anti-Patterns**

Avoid:

```text
Embedding long account lists inside every metric, process, or query pattern card.
Using Table relationships to decide tenant/group-specific applicability.
Using Reconciliation Profile to decide which tenant accounts participate.
Creating separate graph edge types for Logistics Route Binding, Payment Route Binding, or Bank Route Binding.
Connecting every marketplace to every logistics vendor just because a structural join might exist.
Overusing APPLIES_TO_PLATFORM_ACCOUNT when Account Data Binding is sufficient.
Expanding all graph neighbors recursively during retrieval.
```

Correct model:

```text
Account Data Binding handles filters.
Business Flow Binding handles cross-platform tenant/group participation.
Process and Reconciliation cards stay generic unless the model itself changes.
```

---

## **10.13 Final Principle**

```text
Cards should stay focused.
Edges should carry relationship meaning.
Applicability should be explicit.
Business Flow Binding should connect tenant/group reality to reusable process, reconciliation, data, and execution knowledge.
```

A clean graph is what allows retrieval and context assembly to work deterministically without card explosion.

---