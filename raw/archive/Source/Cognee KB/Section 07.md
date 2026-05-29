# Cognee KB Design

**Status:** Draft - V4.0
**Phase:** 1 — KB Schema & Card Design   
**Scope:** Tenant-aware knowledge base for GraphRAG-driven SQL generation

---

# **7. Card Specifications**

**Status:** Draft — V4.0
**Phase:** 1 — KB Schema & Card Design
**Scope:** Tenant-aware, platform-agnostic knowledge base for GraphRAG-driven analytics, reconciliation, diagnostics, and execution guidance

---

## **7.0 Design Shift in This Version**

The earlier schema correctly separated:

```text
Platform Account = which connected account exists
Account Data Binding = how that account maps to warehouse/table filters
Business Scope Set = reusable named account grouping
```

However, it did not explicitly model this important cross-platform question:

```text
For this tenant/group, which platform accounts participate together in a business flow?
```

This matters because ZenStatement will not only connect marketplace data. It will also connect:

```text
marketplace → logistics
marketplace → payment gateway
payment gateway → bank
marketplace → bank
logistics COD → bank
refund → gateway/bank
ERP/accounting → bank
```

Therefore, this version introduces a generic primitive:

```text
Business Flow Binding
```

This should not be logistics-specific, payment-specific, or banking-specific.

It is the tenant/group-level applicability layer that says:

```text
For this tenant/group/business scope,
when this process or money-flow path is relevant,
these platform accounts participate in these roles,
under these conditions,
using these evidence paths.
```

---

# **7.1 Business Hierarchy Cards**

---

## **Purpose of this section**

Business Hierarchy cards define **whose data** the system is operating on and which connected platform accounts are available for that tenant/group.

This section answers:

* Which tenant does the data belong to?
* Which group, business unit, legal entity, region, brand, or operational unit is being queried?
* Which external platforms are connected?
* Which platform context applies?
* Which connected platform accounts exist?
* How does each platform account map to warehouse/table data?
* Which reusable business scopes exist?
* Which platform accounts participate together in reusable business flows?

This section should **not** define metric formulas, table structures, workflow internals, reconciliation matching logic, query patterns, validation tests, or output contracts.

The core responsibility of this section is to model:

```text
identity
ownership
connected platform accounts
account-to-data scoping
reusable business scopes
cross-platform flow applicability
```

---

## **Card 1 — Tenant Card**

**Purpose:** Represents the customer/company using ZenStatement.

**Answers:**

* Which customer does this data belong to?
* What is the top-level ownership boundary?
* Which groups ultimately belong to this tenant?
* Which platform accounts ultimately belong to this tenant?

**Fields:**

| Field              | Definition                           |
| ------------------ | ------------------------------------ |
| `card_type`        | Always `"tenant"`                    |
| `canonical_id`     | Stable tenant ID                     |
| `tenant_name`      | Human-readable tenant name           |
| `tenant_code`      | Short internal tenant code           |
| `description`      | What the tenant represents           |
| `active`           | Whether the tenant is active         |
| `status`           | `draft`, `active`, `deprecated`      |
| `source_documents` | Source docs used to create this card |

**Example:**

```json
{
  "card_type": "tenant",
  "canonical_id": "tenant.acme_retail",
  "tenant_name": "Acme Retail",
  "tenant_code": "ACME",
  "description": "Retail brand using ZenStatement for financial analytics, reconciliation, diagnostics, and money-flow reasoning.",
  "active": true,
  "status": "active",
  "source_documents": []
}
```

---

## **Card 2 — Group Card**

**Purpose:** Represents a business unit, legal entity, region, brand, country entity, or operational grouping inside a tenant.

**Answers:**

* Which group inside the tenant is being queried?
* Which legal entity, brand, region, or business unit does the question refer to?
* What is the business meaning of this group?
* Which platform accounts ultimately belong to this group?

**Fields:**

| Field               | Definition                                                                                     |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| `card_type`         | Always `"group"`                                                                               |
| `canonical_id`      | Stable group ID                                                                                |
| `tenant_id`         | Parent Tenant Card ID                                                                          |
| `group_name`        | Human-readable group name                                                                      |
| `group_code`        | Internal short code                                                                            |
| `group_type`        | `legal_entity`, `country_entity`, `brand`, `region`, `business_unit`, `operational_unit`, etc. |
| `business_meaning`  | What the group represents                                                                      |
| `country_or_region` | Country or region covered, if applicable                                                       |
| `default_currency`  | Default reporting currency, if applicable                                                      |
| `active`            | Whether group is active                                                                        |
| `status`            | `draft`, `active`, `deprecated`                                                                |
| `source_documents`  | Source docs used to create this card                                                           |

**Example:**

```json
{
  "card_type": "group",
  "canonical_id": "group.acme_india",
  "tenant_id": "tenant.acme_retail",
  "group_name": "Acme India",
  "group_code": "ACME_IN",
  "group_type": "country_entity",
  "business_meaning": "India operating group for Acme Retail.",
  "country_or_region": "India",
  "default_currency": "INR",
  "active": true,
  "status": "active",
  "source_documents": []
}
```

---

## **Card 3 — Platform Card**

**Purpose:** Represents an external source system, vendor platform, or internal source platform.

Examples include Amazon, Flipkart, Myntra, Nykaa, Shopify, Razorpay, Cashfree, HDFC Bank, Shiprocket, Delhivery, Tally, NetSuite, and custom sources.

**Answers:**

* Which external system does this data come from?
* What type of source system is this?
* Is this a marketplace, payment gateway, bank, logistics system, ERP, accounting system, ecommerce store, or custom source?
* What broad role does this platform play in ZenStatement?

**Fields:**

| Field              | Definition                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `card_type`        | Always `"platform"`                                                                                                            |
| `canonical_id`     | Stable platform ID                                                                                                             |
| `platform_name`    | Human-readable platform name                                                                                                   |
| `platform_type`    | `marketplace`, `payment_gateway`, `banking`, `logistics`, `erp`, `accounting_system`, `ecommerce_store`, `custom_source`, etc. |
| `description`      | Business role of the platform                                                                                                  |
| `active`           | Whether platform is active/supported                                                                                           |
| `status`           | `draft`, `active`, `deprecated`                                                                                                |
| `source_documents` | Source docs used to create this card                                                                                           |

**Example:**

```json
{
  "card_type": "platform",
  "canonical_id": "platform.shiprocket",
  "platform_name": "Shiprocket",
  "platform_type": "logistics",
  "description": "Courier aggregator platform used for shipment tracking, courier assignment, freight billing, COD settlement, and logistics reconciliation.",
  "active": true,
  "status": "active",
  "source_documents": []
}
```

---

## **Card 4 — Platform Context Card**

**Purpose:** Represents a platform-specific operating context.

A platform context may represent a marketplace country, payment gateway country, banking country, logistics region, ERP instance, accounting company, ecommerce store region, or platform-specific operating context.

This replaces the older marketplace-only `Marketplace Card`.

**Answers:**

* Which operating context inside the platform is being queried?
* Which country, region, currency, or timezone applies?
* Is this Amazon India, Razorpay India, HDFC India, Shiprocket India, etc.?
* What contextual metadata should downstream logic know?

**Fields:**

| Field                 | Definition                                                                                                                                          |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `card_type`           | Always `"platform_context"`                                                                                                                         |
| `canonical_id`        | Stable platform context ID                                                                                                                          |
| `platform_id`         | Parent Platform Card ID                                                                                                                             |
| `context_name`        | Human-readable context name                                                                                                                         |
| `context_type`        | `marketplace_country`, `payment_gateway_country`, `banking_country`, `logistics_region`, `erp_instance`, `accounting_company`, `store_region`, etc. |
| `source_context_code` | Source platform context code, if available                                                                                                          |
| `country`             | Country, if applicable                                                                                                                              |
| `region`              | Region, if applicable                                                                                                                               |
| `currency`            | Default currency                                                                                                                                    |
| `timezone`            | Default timezone                                                                                                                                    |
| `active`              | Whether this context is active                                                                                                                      |
| `status`              | `draft`, `active`, `deprecated`                                                                                                                     |
| `source_documents`    | Source docs used to create this card                                                                                                                |

**Example:**

```json
{
  "card_type": "platform_context",
  "canonical_id": "platform_context.shiprocket.in",
  "platform_id": "platform.shiprocket",
  "context_name": "Shiprocket India",
  "context_type": "logistics_region",
  "source_context_code": "IN",
  "country": "India",
  "region": "IN",
  "currency": "INR",
  "timezone": "Asia/Kolkata",
  "active": true,
  "status": "active",
  "source_documents": []
}
```

---

## **Card 5 — Platform Account Card**

**Purpose:** Represents an actual connected source account for a tenant/group on a platform.

Examples:

```text
Amazon seller account
Flipkart seller account
Shopify store account
Razorpay merchant account
HDFC current account
Shiprocket merchant account
Delhivery courier billing account
Tally company instance
NetSuite subsidiary/accounting instance
```

**Answers:**

* Which connected source account should be used?
* Which tenant and group does this account belong to?
* Which platform and platform context does this account belong to?
* What is the source account identifier?
* Is the account active?

**Fields:**

| Field                       | Definition                                                                                                                 |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `card_type`                 | Always `"platform_account"`                                                                                                |
| `canonical_id`              | Stable platform account ID                                                                                                 |
| `tenant_id`                 | Parent Tenant Card ID                                                                                                      |
| `group_id`                  | Parent Group Card ID                                                                                                       |
| `platform_id`               | Parent Platform Card ID                                                                                                    |
| `platform_context_id`       | Parent Platform Context Card ID                                                                                            |
| `account_name`              | Human-readable account name                                                                                                |
| `account_type`              | `seller_account`, `merchant_account`, `current_account`, `logistics_account`, `store_account`, `erp_company`, `test`, etc. |
| `source_account_identifier` | Source system account ID, merchant ID, seller ID, bank account reference, store ID, etc.                                   |
| `active`                    | Whether account is active                                                                                                  |
| `status`                    | `draft`, `active`, `deprecated`                                                                                            |
| `source_documents`          | Source docs used to create this card                                                                                       |

**Example:**

```json
{
  "card_type": "platform_account",
  "canonical_id": "platform_account.acme.shiprocket.primary",
  "tenant_id": "tenant.acme_retail",
  "group_id": "group.acme_india",
  "platform_id": "platform.shiprocket",
  "platform_context_id": "platform_context.shiprocket.in",
  "account_name": "Acme India Shiprocket Primary",
  "account_type": "logistics_account",
  "source_account_identifier": "shiprocket_account_abc",
  "active": true,
  "status": "active",
  "source_documents": []
}
```

---

## **Card 6 — Account Data Binding Card**

**Purpose:** Maps a platform account to warehouse/table-level scope keys required to query its data correctly.

This is where filters like the following should live:

```text
group_level_id = 22
merchant_id = ...
seller_id = ...
bank_account_id = ...
source_account_identifier = ...
store_id = ...
```

**Answers:**

* How does this platform account appear in a specific warehouse table?
* Which physical column should filter this account’s data?
* What value should be used?
* What is the correct data type?
* Are there table-specific scoping caveats?
* How do we avoid wrong account-level filtering?

**Fields:**

| Field                       | Definition                                                                                    |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| `card_type`                 | Always `"account_data_binding"`                                                               |
| `canonical_id`              | Stable account data binding ID                                                                |
| `platform_account_id`       | Platform Account Card ID                                                                      |
| `table_id`                  | Table Card ID this binding applies to                                                         |
| `scope_keys`                | List of scope/filter keys required for this account-table combination                         |
| `scope_keys[].business_key` | Business meaning of key, e.g. `group_level_id`, `merchant_id`, `seller_id`, `bank_account_id` |
| `scope_keys[].column`       | Physical column name                                                                          |
| `scope_keys[].operator`     | SQL operator, e.g. `=`, `IN`, `LIKE`                                                          |
| `scope_keys[].value`        | Required filter value                                                                         |
| `scope_keys[].data_type`    | Data type of filter value                                                                     |
| `notes`                     | Important caveats, e.g. integer vs string comparison                                          |
| `active`                    | Whether binding is active                                                                     |
| `status`                    | `draft`, `active`, `deprecated`                                                               |
| `source_documents`          | Source docs used to create this card                                                          |

**Example:**

```json
{
  "card_type": "account_data_binding",
  "canonical_id": "account_data_binding.acme.shiprocket.primary.shiprocket_oms",
  "platform_account_id": "platform_account.acme.shiprocket.primary",
  "table_id": "table.zs_observe.shiprocket_oms",
  "scope_keys": [
    {
      "business_key": "group_level_id",
      "column": "group_level_id",
      "operator": "=",
      "value": 22,
      "data_type": "integer"
    }
  ],
  "notes": [
    "Use this binding only when the selected runtime scope includes the Acme India Shiprocket account."
  ],
  "active": true,
  "status": "active",
  "source_documents": []
}
```

---

## **Card 7 — Business Scope Set Card**

**Purpose:** Represents a durable, reusable, named business scope.

A Business Scope Set is not created for every possible account combination. It should exist only when the scope has recurring business meaning.

Examples:

```text
Acme India Amazon All Accounts
Acme India Razorpay All Accounts
Acme India HDFC Operating Bank Accounts
Acme India Marketplace to Bank Reconciliation Scope
Acme India COD Logistics to Bank Scope
Acme India All Revenue Channels
```

**Answers:**

* Which accounts are included in this reusable business scope?
* Does this scope represent one account, multiple accounts, one platform, or multiple platforms?
* Is this scope analytical, reporting, operational, or reconciliation-oriented?
* Which tenant and group does this scope belong to?
* Can downstream cards reference this scope instead of duplicating account lists?

**Fields:**

| Field                  | Definition                                                                                                                                               |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `card_type`            | Always `"business_scope_set"`                                                                                                                            |
| `canonical_id`         | Stable business scope set ID                                                                                                                             |
| `tenant_id`            | Parent Tenant Card ID                                                                                                                                    |
| `group_id`             | Parent Group Card ID                                                                                                                                     |
| `scope_name`           | Human-readable scope name                                                                                                                                |
| `scope_type`           | `single_account`, `platform_account_group`, `group_platform_scope`, `cross_platform_reconciliation_scope`, `tenant_reporting_scope`, `operational_scope` |
| `platform_account_ids` | Platform Account IDs included in this scope                                                                                                              |
| `platform_ids`         | Platform IDs covered by this scope                                                                                                                       |
| `platform_context_ids` | Platform Context IDs covered by this scope                                                                                                               |
| `description`          | Business meaning of this reusable scope                                                                                                                  |
| `active`               | Whether scope is active                                                                                                                                  |
| `status`               | `draft`, `active`, `deprecated`                                                                                                                          |
| `source_documents`     | Source docs used to create this card                                                                                                                     |

**Example:**

```json
{
  "card_type": "business_scope_set",
  "canonical_id": "business_scope_set.acme_india.razorpay_to_hdfc",
  "tenant_id": "tenant.acme_retail",
  "group_id": "group.acme_india",
  "scope_name": "Acme India Razorpay to HDFC Reconciliation Scope",
  "scope_type": "cross_platform_reconciliation_scope",
  "platform_account_ids": [
    "platform_account.acme.razorpay.primary",
    "platform_account.acme.hdfc.current"
  ],
  "platform_ids": [
    "platform.razorpay",
    "platform.hdfc_bank"
  ],
  "platform_context_ids": [
    "platform_context.razorpay.in",
    "platform_context.hdfc.india"
  ],
  "description": "Reusable scope for reconciling Razorpay payouts against HDFC bank credits for Acme India.",
  "active": true,
  "status": "active",
  "source_documents": []
}
```

---

## **Card 8 — Business Flow Binding Card**

**Purpose:** Represents a tenant/group-specific binding between a business flow and the platform accounts that participate in that flow.

This is the generic abstraction that replaces logistics-specific, payment-specific, or banking-specific route bindings.

A Business Flow Binding answers:

```text
For this tenant/group/business scope,
when this process or money-flow path is relevant,
which platform accounts participate,
what roles do they play,
under what conditions,
and which evidence paths should retrieval consider?
```

**Why this card exists:**

Platform Account says an account exists.
Account Data Binding says how the account maps to table filters.
Business Scope Set names a reusable account set.
Business Flow Binding says how accounts participate together in a business flow.

**Examples of flows this card supports:**

```text
marketplace → logistics
marketplace → payment gateway
payment gateway → bank
marketplace → bank
logistics COD → bank
refund → gateway/bank
ERP/accounting → bank
```

**Answers:**

* Which platform accounts participate together in a tenant/group-specific flow?
* What business process or money-flow path does this binding support?
* Which account is the source side, operational evidence side, settlement side, bank side, or accounting side?
* Which conditions determine when this flow applies?
* Which Account Data Bindings are needed when this flow is selected?
* Which evidence tables and relationships are relevant?
* Is this binding active, partial, inferred, or low-confidence?

**Fields:**

| Field                                          | Definition                                                                                                                                                             |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `card_type`                                    | Always `"business_flow_binding"`                                                                                                                                       |
| `canonical_id`                                 | Stable business flow binding ID                                                                                                                                        |
| `tenant_id`                                    | Parent Tenant Card ID                                                                                                                                                  |
| `group_id`                                     | Parent Group Card ID                                                                                                                                                   |
| `binding_name`                                 | Human-readable binding name                                                                                                                                            |
| `binding_type`                                 | `analytics_flow`, `operational_flow`, `reconciliation_flow`, `money_flow`, `fulfilment_flow`, `diagnostic_flow`                                                        |
| `business_scope_set_id`                        | Optional Business Scope Set ID if this flow corresponds to a named reusable scope                                                                                      |
| `business_process_ids`                         | Business Process Card IDs this binding supports                                                                                                                        |
| `reconciliation_profile_ids`                   | Reconciliation Profile Card IDs this binding supports, if applicable                                                                                                   |
| `money_flow_paths`                             | Named paths such as `marketplace_to_bank`, `payment_gateway_to_bank`, `logistics_cod_to_bank`, `order_to_shipment`, etc.                                               |
| `participating_accounts`                       | Platform accounts participating in this flow and their roles                                                                                                           |
| `participating_accounts[].platform_account_id` | Platform Account Card ID                                                                                                                                               |
| `participating_accounts[].role`                | `order_source`, `settlement_source`, `payment_source`, `payout_source`, `logistics_source`, `bank_destination`, `accounting_destination`, `operational_evidence`, etc. |
| `participating_accounts[].required`            | Whether the account is required or optional for this flow                                                                                                              |
| `conditions`                                   | Conditions under which the flow applies; e.g. `payment_mode = COD`, `fulfilment_model = aggregator_routed`, `payout_status = processed`                                |
| `evidence_table_ids`                           | Table Card IDs commonly used when this binding is active                                                                                                               |
| `account_data_binding_ids`                     | Account Data Binding Cards needed for selected tables/accounts                                                                                                         |
| `relationship_ids`                             | Relationship Cards that connect the evidence path, if known                                                                                                            |
| `fulfilment_ownership_model`                   | Optional value for fulfilment/logistics flows: `platform_fulfilled`, `marketplace_assisted`, `seller_fulfilled`, `aggregator_routed`, `direct_courier`, etc.           |
| `confidence`                                   | `curated`, `inferred`, `low_confidence`, `experimental`                                                                                                                |
| `notes`                                        | Caveats, limitations, or unresolved assumptions                                                                                                                        |
| `active`                                       | Whether binding is active                                                                                                                                              |
| `status`                                       | `draft`, `active`, `deprecated`                                                                                                                                        |
| `source_documents`                             | Source docs used to create this card                                                                                                                                   |

**Example 1 — Marketplace to Logistics:**

```json
{
  "card_type": "business_flow_binding",
  "canonical_id": "business_flow_binding.acme_india.shopify_to_shiprocket",
  "tenant_id": "tenant.acme_retail",
  "group_id": "group.acme_india",
  "binding_name": "Acme India Shopify to Shiprocket Logistics Flow",
  "binding_type": "fulfilment_flow",
  "business_scope_set_id": null,
  "business_process_ids": [
    "business_process.order_to_shipment_flow"
  ],
  "reconciliation_profile_ids": [
    "reconciliation_profile.order_to_shipment_reconciliation",
    "reconciliation_profile.cod_logistics_to_bank"
  ],
  "money_flow_paths": [
    "order_to_shipment",
    "shipment_to_freight_invoice",
    "cod_delivery_to_courier_remittance"
  ],
  "participating_accounts": [
    {
      "platform_account_id": "platform_account.acme.shopify.primary",
      "role": "order_source",
      "required": true
    },
    {
      "platform_account_id": "platform_account.acme.shiprocket.primary",
      "role": "logistics_source",
      "required": true
    }
  ],
  "conditions": [
    {
      "concept": "fulfilment_ownership_model",
      "operator": "=",
      "value": "aggregator_routed"
    }
  ],
  "evidence_table_ids": [
    "table.zs_observe.shopify_oms",
    "table.zs_observe.shiprocket_oms",
    "table.zs_observe.shiprocket_invoice",
    "table.zs_observe.shiprocket_settlement"
  ],
  "account_data_binding_ids": [
    "account_data_binding.acme.shopify.primary.shopify_oms",
    "account_data_binding.acme.shiprocket.primary.shiprocket_oms",
    "account_data_binding.acme.shiprocket.primary.shiprocket_invoice",
    "account_data_binding.acme.shiprocket.primary.shiprocket_settlement"
  ],
  "relationship_ids": [
    "relationship.shopify_oms.shiprocket_oms.order_id",
    "relationship.shiprocket_oms.shiprocket_invoice.awb",
    "relationship.shiprocket_oms.shiprocket_settlement.awb"
  ],
  "fulfilment_ownership_model": "aggregator_routed",
  "confidence": "curated",
  "notes": [
    "This binding describes applicability and evidence path. Account-level filters are still resolved through Account Data Binding."
  ],
  "active": true,
  "status": "active",
  "source_documents": []
}
```

**Example 2 — Payment Gateway to Bank:**

```json
{
  "card_type": "business_flow_binding",
  "canonical_id": "business_flow_binding.acme_india.razorpay_to_hdfc",
  "tenant_id": "tenant.acme_retail",
  "group_id": "group.acme_india",
  "binding_name": "Acme India Razorpay to HDFC Bank Flow",
  "binding_type": "money_flow",
  "business_scope_set_id": "business_scope_set.acme_india.razorpay_to_hdfc",
  "business_process_ids": [
    "business_process.payment_gateway_to_bank_reconciliation"
  ],
  "reconciliation_profile_ids": [
    "reconciliation_profile.payment_gateway_payout_to_bank_credit"
  ],
  "money_flow_paths": [
    "payment_gateway_to_bank"
  ],
  "participating_accounts": [
    {
      "platform_account_id": "platform_account.acme.razorpay.primary",
      "role": "payout_source",
      "required": true
    },
    {
      "platform_account_id": "platform_account.acme.hdfc.current",
      "role": "bank_destination",
      "required": true
    }
  ],
  "conditions": [
    {
      "concept": "payout_status",
      "operator": "IN",
      "value": ["processed", "paid"]
    },
    {
      "concept": "bank_transaction_direction",
      "operator": "=",
      "value": "credit"
    }
  ],
  "evidence_table_ids": [
    "table.zs_observe.razorpay_payouts",
    "table.zs_observe.bank_statement"
  ],
  "account_data_binding_ids": [
    "account_data_binding.acme.razorpay.primary.razorpay_payouts",
    "account_data_binding.acme.hdfc.current.bank_statement"
  ],
  "relationship_ids": [
    "relationship.razorpay_payouts.bank_statement.utr"
  ],
  "fulfilment_ownership_model": null,
  "confidence": "curated",
  "notes": [
    "This binding activates the Razorpay-to-HDFC path for Acme India. Generic matching logic remains in Reconciliation Understanding."
  ],
  "active": true,
  "status": "active",
  "source_documents": []
}
```

---

## **7.1 Design Principle**

Business Hierarchy cards should encode:

* Tenant identity
* Group identity
* Platform identity
* Platform context
* Connected platform accounts
* Account-to-table data bindings
* Durable reusable business scopes
* Cross-platform flow applicability through Business Flow Binding

They should not encode:

* Metric formulas
* Table schemas
* Column semantics
* Workflow internals
* Reconciliation matching internals
* SQL query patterns
* Validation tests
* Output contracts

The main correction is:

```text
Do not create logistics-specific, payment-specific, or banking-specific route cards.
Create one generic Business Flow Binding that can represent any tenant/group-specific cross-platform flow.
```

---

# **7.2 Data Understanding Cards**

---

## **Purpose of this section**

Data Understanding cards define **where the data lives** and how the system should interpret warehouse structure.

This section answers:

* Which tables contain the relevant evidence?
* What does each table represent?
* What is the grain of each table?
* Which columns exist and what do they mean?
* Which columns are measures, dimensions, dates, identifiers, filters, join keys, or reconciliation keys?
* How do tables relate to each other structurally?
* What values can categorical columns take?
* Which columns are safe or unsafe for filtering, grouping, joining, aggregation, or reconciliation?

This section should **not** define tenant ownership, runtime account filters, metric formulas, process flows, reconciliation matching semantics, query patterns, validation tests, output contracts, or tenant-specific flow applicability.

Account-specific filtering belongs to **Account Data Binding**.
Cross-platform applicability belongs to **Business Flow Binding**.

---

## **Card 9 — Table Card**

**Purpose:** Represents a physical or logical warehouse table.

**Answers:**

* What does this table represent?
* What source-system data does it contain?
* What is the grain?
* Which platform or platform type does it generally come from?
* Which columns and relationships belong to this table?
* Which date columns are recommended?
* Which columns should be avoided or treated carefully?
* What structural applicability does this table support without hardcoding account filters?

**Fields:**

| Field                      | Definition                                                                       |
| -------------------------- | -------------------------------------------------------------------------------- |
| `card_type`                | Always `"table"`                                                                 |
| `canonical_id`             | Stable table ID                                                                  |
| `database`                 | Database/catalog name, if known                                                  |
| `schema`                   | Schema name                                                                      |
| `table_name`               | Physical table name                                                              |
| `full_reference`           | Fully qualified table reference                                                  |
| `engine`                   | Query engine, e.g. Athena, Trino, Postgres, BigQuery                             |
| `table_type`               | `fact`, `dimension`, `ledger`, `snapshot`, `bridge`, `report`, `staging`, etc.   |
| `source_platform_ids`      | Platform Card IDs associated with the table                                      |
| `source_platform_types`    | Platform types associated with the table                                         |
| `business_purpose`         | What the table is used for                                                       |
| `grain`                    | What one row represents                                                          |
| `grain_keys`               | Columns that define or approximate row grain                                     |
| `date_columns`             | Date/timestamp columns available                                                 |
| `recommended_date_columns` | Preferred date columns for filtering/reporting/reconciliation                    |
| `avoid_columns`            | Columns to avoid or treat carefully, with reasons                                |
| `columns`                  | Column Card IDs under this table                                                 |
| `relationships`            | Relationship Card IDs involving this table                                       |
| `value_profiles`           | Value Profile Card IDs for categorical columns                                   |
| `structural_applicability` | Platform/platform-context/table-level applicability; not tenant/account filters  |
| `coverage_status`          | `active`, `partial`, `empty`, `schema_only`, `low_confidence`, etc., if relevant |
| `status`                   | `draft`, `active`, `deprecated`                                                  |
| `source_documents`         | Source docs used to create this card                                             |

**Example:**

```json
{
  "card_type": "table",
  "canonical_id": "table.zs_observe.shiprocket_settlement",
  "schema": "zs_observe",
  "table_name": "shiprocket_settlement",
  "full_reference": "zs_observe.shiprocket_settlement",
  "engine": "Athena v3 / Trino SQL",
  "table_type": "ledger",
  "source_platform_ids": ["platform.shiprocket"],
  "source_platform_types": ["logistics"],
  "business_purpose": "Shiprocket COD settlement table used to identify COD amounts collected and remitted for AWB-level courier settlements.",
  "grain": "One row per AWB-level COD settlement record.",
  "grain_keys": ["awb_number", "settlement_date"],
  "date_columns": ["delivered_date", "settlement_date", "created_date"],
  "recommended_date_columns": ["settlement_date", "delivered_date"],
  "avoid_columns": [],
  "columns": [
    "column.zs_observe.shiprocket_settlement.awb_number",
    "column.zs_observe.shiprocket_settlement.charged_amount",
    "column.zs_observe.shiprocket_settlement.settlement_date"
  ],
  "relationships": [
    "relationship.shiprocket_oms.shiprocket_settlement.awb"
  ],
  "value_profiles": [],
  "structural_applicability": {
    "platform_ids": ["platform.shiprocket"],
    "platform_context_ids": ["platform_context.shiprocket.in"],
    "notes": [
      "Account filters are resolved through Account Data Binding.",
      "Tenant/group-specific flow applicability is resolved through Business Flow Binding."
    ]
  },
  "coverage_status": "active",
  "status": "active",
  "source_documents": []
}
```

---

## **Card 10 — Column Card**

**Purpose:** Represents a physical column and its semantic role within a table.

**Answers:**

* What does this column mean?
* Is it a measure, dimension, date, status, identifier, filter, join key, or reconciliation key?
* Can it be aggregated, grouped, filtered, joined, or used for reconciliation?
* What business concept does it represent?
* Does it have a sign convention or amount semantic caveat?
* Does it need a value profile?
* Are there quality issues, null patterns, formatting risks, or type-casting risks?

**Fields:**

| Field                       | Definition                                                                                               |
| --------------------------- | -------------------------------------------------------------------------------------------------------- |
| `card_type`                 | Always `"column"`                                                                                        |
| `canonical_id`              | Stable column ID                                                                                         |
| `table_id`                  | Parent Table Card ID                                                                                     |
| `column_name`               | Physical column name                                                                                     |
| `data_type`                 | SQL data type                                                                                            |
| `business_meaning`          | What the column means in business terms                                                                  |
| `semantic_roles`            | `measure`, `dimension`, `date`, `status`, `identifier`, `filter`, `join_key`, `reconciliation_key`, etc. |
| `business_concepts`         | Business concepts mapped to this column                                                                  |
| `default_aggregation`       | `SUM`, `COUNT`, `AVG`, `COUNT_DISTINCT`, `none`, etc.                                                    |
| `sign_convention`           | `positive`, `negative`, `net`, `varies`, `not_applicable`                                                |
| `amount_semantics`          | Meaning of amount fields, e.g. product value, freight, COD collected, bank credit, payout amount         |
| `usable_for_filtering`      | Whether safe for `WHERE` filters                                                                         |
| `usable_for_grouping`       | Whether safe for `GROUP BY`                                                                              |
| `usable_for_metrics`        | Whether usable in metric calculations                                                                    |
| `usable_for_joining`        | Whether usable as join key                                                                               |
| `usable_for_reconciliation` | Whether usable as reconciliation key or evidence                                                         |
| `value_profile_id`          | Value Profile Card ID, if applicable                                                                     |
| `quality_notes`             | Nulls, duplication, formatting, precision, known issues                                                  |
| `status`                    | `draft`, `active`, `deprecated`                                                                          |
| `source_documents`          | Source docs used to create this card                                                                     |

**Example:**

```json
{
  "card_type": "column",
  "canonical_id": "column.zs_observe.shiprocket_settlement.charged_amount",
  "table_id": "table.zs_observe.shiprocket_settlement",
  "column_name": "charged_amount",
  "data_type": "decimal(10,2)",
  "business_meaning": "COD amount collected/remitted for a Shiprocket COD settlement record.",
  "semantic_roles": ["measure", "financial_amount"],
  "business_concepts": ["cod_collected", "cod_remitted"],
  "default_aggregation": "SUM",
  "sign_convention": "positive",
  "amount_semantics": "COD settlement amount, not freight and not product GMV.",
  "usable_for_filtering": false,
  "usable_for_grouping": false,
  "usable_for_metrics": true,
  "usable_for_joining": false,
  "usable_for_reconciliation": true,
  "value_profile_id": null,
  "quality_notes": [
    "The same column name can mean different things in other logistics tables. Do not generalize this meaning outside shiprocket_settlement."
  ],
  "status": "active",
  "source_documents": []
}
```

---

## **Card 11 — Relationship Card**

**Purpose:** Represents a structural relationship or join path between tables.

A Relationship Card explains how tables can be connected, what business context the join adds, and whether the join is safe for analytics or reconciliation.

It should describe structural joinability. It should not decide whether a tenant/group should use that relationship at runtime. That applicability is handled by Business Flow Binding.

**Fields:**

| Field                      | Definition                                                                              |
| -------------------------- | --------------------------------------------------------------------------------------- |
| `card_type`                | Always `"relationship"`                                                                 |
| `canonical_id`             | Stable relationship ID                                                                  |
| `source_table`             | Starting Table Card ID                                                                  |
| `target_table`             | Target Table Card ID                                                                    |
| `relationship_type`        | `join`, `lookup`, `parent_child`, `aggregate_relation`, `reconciliation_relation`, etc. |
| `join_keys`                | Source and target join key mappings                                                     |
| `cardinality`              | `one_to_one`, `one_to_many`, `many_to_one`, `many_to_many`, `unknown`                   |
| `join_type_recommendation` | `left_join`, `inner_join`, `full_outer_join`, etc.                                      |
| `business_use`             | Why this relationship exists                                                            |
| `safe_for_metrics`         | Whether safe in metric calculations                                                     |
| `safe_for_reconciliation`  | Whether usable for reconciliation                                                       |
| `aggregation_risk`         | Double-counting or grain mismatch risk                                                  |
| `caveats`                  | Known join risks or limitations                                                         |
| `confidence`               | `high`, `medium`, `low`                                                                 |
| `status`                   | `draft`, `active`, `deprecated`                                                         |
| `source_documents`         | Source docs used to create this card                                                    |

**Example:**

```json
{
  "card_type": "relationship",
  "canonical_id": "relationship.shiprocket_oms.shiprocket_settlement.awb",
  "source_table": "table.zs_observe.shiprocket_oms",
  "target_table": "table.zs_observe.shiprocket_settlement",
  "relationship_type": "reconciliation_relation",
  "join_keys": [
    {
      "source_column": "awb_code",
      "target_column": "awb_number"
    }
  ],
  "cardinality": "one_to_zero_or_one",
  "join_type_recommendation": "left_join",
  "business_use": "Checks whether COD shipments in Shiprocket OMS have corresponding COD settlement/remittance evidence.",
  "safe_for_metrics": false,
  "safe_for_reconciliation": true,
  "aggregation_risk": "Pre-aggregate to AWB grain before comparing COD expected and COD remitted amounts.",
  "caveats": [
    "This relationship is structurally valid for Shiprocket data. Tenant/group applicability is resolved through Business Flow Binding."
  ],
  "confidence": "high",
  "status": "active",
  "source_documents": []
}
```

---

## **Card 12 — Value Profile Card**

**Purpose:** Represents known or allowed values in a categorical or semi-categorical column and explains their business meaning.

**Fields:**

| Field                       | Definition                                                                  |
| --------------------------- | --------------------------------------------------------------------------- |
| `card_type`                 | Always `"value_profile"`                                                    |
| `canonical_id`              | Stable value profile ID                                                     |
| `table_id`                  | Parent Table Card ID                                                        |
| `column_id`                 | Parent Column Card ID                                                       |
| `value_type`                | `enum`, `enum_with_nulls`, `free_text`, `numeric_range`, `date_range`, etc. |
| `values`                    | Known values and their meanings                                             |
| `values[].value`            | Raw value appearing in data                                                 |
| `values[].business_meaning` | Business interpretation                                                     |
| `values[].category`         | Higher-level grouping                                                       |
| `values[].metric_usage`     | How this value should be used in metrics, if relevant                       |
| `null_handling`             | What to do with null values                                                 |
| `business_usage`            | How this column is used analytically/operationally                          |
| `status`                    | `draft`, `active`, `deprecated`                                             |
| `source_documents`          | Source docs used to create this card                                        |

**Example:**

```json
{
  "card_type": "value_profile",
  "canonical_id": "value_profile.ekart_settlement.transaction_type",
  "table_id": "table.zs_observe.ekart_settlement",
  "column_id": "column.zs_observe.ekart_settlement.transaction_type",
  "value_type": "enum",
  "values": [
    {
      "value": "COD",
      "business_meaning": "Cash collected at delivery and remitted through Ekart settlement.",
      "category": "cod_settlement",
      "metric_usage": "Use for COD settlement and remittance metrics."
    },
    {
      "value": "POS",
      "business_meaning": "Digital/prepaid/POS settlement through marketplace fulfilment infrastructure.",
      "category": "prepaid_or_pos_settlement",
      "metric_usage": "Use separately from COD settlement metrics."
    }
  ],
  "null_handling": "Do not infer COD or POS when transaction_type is null.",
  "business_usage": "Used to separate COD remittance from prepaid/POS logistics settlement.",
  "status": "active",
  "source_documents": []
}
```

---

## **7.2 Design Principle**

Data Understanding cards should encode:

* Table structure
* Column semantics
* Grain
* Join relationships
* Value meanings
* Date safety
* Data quality caveats
* Structural applicability

They should not encode:

* Tenant ownership
* Runtime account filters
* Cross-platform tenant/group flow applicability
* Metric formulas
* Business process sequence
* Reconciliation matching semantics
* Query templates
* Validation tests
* Output contracts

Main principle:

```text
Tables and columns describe data structure.
Account Data Binding describes account-specific filters.
Business Flow Binding describes tenant/group-specific cross-platform applicability.
```

---

# **7.3 Metric Understanding Cards**

---

## **Purpose of this section**

Metric Understanding cards define **what is being calculated** and how business language maps to measurable financial, operational, or reconciliation metrics.

This section answers:

* What metric is the user asking for?
* What does the metric mean?
* Is it an amount, count, rate, ratio, percentage, variance, status, or derived metric?
* Which implementation should be used for a platform/table/process context?
* Which tables and columns are needed?
* Which semantic filters are required?
* Which grains and dimensions are valid?
* Which formula template should be used?

This section should **not** define tenant ownership, account filters, cross-platform flow applicability, workflow steps, reconciliation matching logic, SQL query patterns, validation tests, or output contracts.

---

## **Card 13 — Metric Card**

**Purpose:** Represents a business metric independent of source-system implementation.

**Fields:**

| Field                  | Definition                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------- |
| `card_type`            | Always `"metric"`                                                                       |
| `canonical_id`         | Stable metric ID                                                                        |
| `metric_name`          | Human-readable metric name                                                              |
| `aliases`              | Alternate names users may use                                                           |
| `business_definition`  | Business meaning of metric                                                              |
| `metric_type`          | `amount`, `count`, `rate`, `ratio`, `percentage`, `variance`, `status`, `derived`, etc. |
| `unit`                 | `currency`, `percentage`, `count`, `days`, etc.                                         |
| `default_aggregation`  | `SUM`, `COUNT`, `AVG`, `ratio`, `latest`, `none`, etc.                                  |
| `default_grain`        | Default reporting grain, if applicable                                                  |
| `polarity`             | `higher_is_better`, `lower_is_better`, `neutral`, `context_dependent`                   |
| `business_concepts`    | Concepts represented by this metric                                                     |
| `domain_ids`           | Domain Card IDs commonly using this metric                                              |
| `business_process_ids` | Business Process Card IDs commonly using this metric                                    |
| `implementations`      | Metric Implementation Card IDs                                                          |
| `status`               | `draft`, `active`, `deprecated`                                                         |
| `source_documents`     | Source docs used to create this card                                                    |

**Example:**

```json
{
  "card_type": "metric",
  "canonical_id": "metric.cod_remitted_amount",
  "metric_name": "COD Remitted Amount",
  "aliases": ["COD settlement amount", "COD received from courier", "COD remittance"],
  "business_definition": "Amount remitted by a courier, aggregator, or fulfilment platform for cash-on-delivery orders after collection from customers.",
  "metric_type": "amount",
  "unit": "currency",
  "default_aggregation": "SUM",
  "default_grain": "shipment_or_settlement_batch_depending_on_implementation",
  "polarity": "higher_is_better",
  "business_concepts": ["cod_remittance", "cash_collection", "logistics_settlement"],
  "domain_ids": ["domain.logistics_reconciliation", "domain.cash_flow"],
  "business_process_ids": ["business_process.logistics_cod_to_bank_reconciliation"],
  "implementations": ["metric_impl.shiprocket_settlement.cod_remitted_amount"],
  "status": "active",
  "source_documents": []
}
```

---

## **Card 14 — Metric Implementation Card**

**Purpose:** Represents how a metric is calculated for a valid source-system, table, process, or durable formula-validity scope.

A Metric Implementation should define formula applicability. It should not create every tenant/account combination.

**Fields:**

| Field                      | Definition                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `card_type`                | Always `"metric_implementation"`                                                                                   |
| `canonical_id`             | Stable metric implementation ID                                                                                    |
| `metric_id`                | Parent Metric Card ID                                                                                              |
| `implementation_name`      | Human-readable implementation name                                                                                 |
| `applicability`            | Scope where formula is valid; platform type, platform, platform context, table, process, or durable business scope |
| `base_tables`              | Table Card IDs required                                                                                            |
| `required_columns`         | Column Card IDs required                                                                                           |
| `semantic_filters`         | Business filters required for metric meaning, not account filters                                                  |
| `formula_description`      | Plain-English formula explanation                                                                                  |
| `formula_sql`              | SQL expression or pseudo-SQL                                                                                       |
| `dependent_metrics`        | Other Metric IDs needed                                                                                            |
| `formula_template_id`      | Formula Template ID, if used                                                                                       |
| `allowed_dimensions`       | Dimensions safe to group by                                                                                        |
| `allowed_grains`           | Safe grains for calculation                                                                                        |
| `recommended_date_columns` | Recommended date columns                                                                                           |
| `unit`                     | Output unit                                                                                                        |
| `precision`                | Recommended rounding/precision                                                                                     |
| `caveats`                  | Known assumptions/limitations                                                                                      |
| `confidence`               | `curated`, `inferred`, `experimental`                                                                              |
| `status`                   | `draft`, `active`, `deprecated`                                                                                    |
| `source_documents`         | Source docs used                                                                                                   |

**Example:**

```json
{
  "card_type": "metric_implementation",
  "canonical_id": "metric_impl.shiprocket_settlement.cod_remitted_amount",
  "metric_id": "metric.cod_remitted_amount",
  "implementation_name": "Shiprocket COD Remitted Amount",
  "applicability": {
    "scope_level": "table",
    "platform_types": ["logistics"],
    "platform_ids": ["platform.shiprocket"],
    "platform_context_ids": ["platform_context.shiprocket.in"],
    "table_ids": ["table.zs_observe.shiprocket_settlement"],
    "notes": [
      "Formula is valid for Shiprocket COD settlement data. Account filters are resolved through Account Data Binding. Tenant/group applicability to a broader flow is resolved through Business Flow Binding."
    ]
  },
  "base_tables": ["table.zs_observe.shiprocket_settlement"],
  "required_columns": [
    "column.zs_observe.shiprocket_settlement.charged_amount",
    "column.zs_observe.shiprocket_settlement.settlement_date"
  ],
  "semantic_filters": [],
  "formula_description": "Sum the COD amount remitted in Shiprocket settlement rows.",
  "formula_sql": "SUM(charged_amount)",
  "dependent_metrics": [],
  "formula_template_id": null,
  "allowed_dimensions": ["courier_partner", "settlement_date", "awb_number"],
  "allowed_grains": ["awb", "day", "month", "courier_partner"],
  "recommended_date_columns": ["settlement_date"],
  "unit": "currency",
  "precision": "2_decimal_places",
  "caveats": [
    "charged_amount in shiprocket_settlement means COD amount, not freight."
  ],
  "confidence": "curated",
  "status": "active",
  "source_documents": []
}
```

---

## **Card 15 — Formula Template Card**

**Purpose:** Represents reusable calculation logic such as rate, ratio, variance, gap, share, growth, average, or lag.

**Fields:**

| Field                   | Definition                                                                    |
| ----------------------- | ----------------------------------------------------------------------------- |
| `card_type`             | Always `"formula_template"`                                                   |
| `canonical_id`          | Stable formula template ID                                                    |
| `template_name`         | Human-readable template name                                                  |
| `description`           | What this template calculates                                                 |
| `formula_type`          | `growth`, `ratio`, `rate`, `share`, `variance`, `gap`, `average`, `lag`, etc. |
| `required_inputs`       | Required inputs                                                               |
| `optional_inputs`       | Optional dimensions/windows/comparison periods                                |
| `formula_plain_english` | Business explanation                                                          |
| `formula_sql_pattern`   | SQL or pseudo-SQL pattern                                                     |
| `allowed_metric_types`  | Metric types this template applies to                                         |
| `required_date_logic`   | Date logic, if any                                                            |
| `denominator_handling`  | Denominator safety rule                                                       |
| `null_handling`         | Null handling guidance                                                        |
| `output_unit_logic`     | Output unit interpretation                                                    |
| `status`                | `draft`, `active`, `deprecated`                                               |
| `source_documents`      | Source docs used                                                              |

---

## **Card 16 — Metric Dependency Card**

**Purpose:** Represents dependency relationships between metrics.

**Fields:**

| Field                         | Definition                                                                    |
| ----------------------------- | ----------------------------------------------------------------------------- |
| `card_type`                   | Always `"metric_dependency"`                                                  |
| `canonical_id`                | Stable metric dependency ID                                                   |
| `parent_metric_id`            | Metric being calculated                                                       |
| `dependent_metric_ids`        | Required dependent metrics                                                    |
| `dependency_type`             | `additive`, `subtractive`, `ratio`, `rate`, `comparison`, `conditional`, etc. |
| `formula_template_id`         | Formula Template ID, if applicable                                            |
| `grain_alignment_required`    | Whether dependent metrics must align by grain                                 |
| `time_alignment_required`     | Whether same time window is required                                          |
| `scope_alignment_required`    | Whether same resolved runtime scope is required                               |
| `missing_dependency_behavior` | What happens if dependency is missing                                         |
| `business_explanation`        | Plain-English explanation                                                     |
| `status`                      | `draft`, `active`, `deprecated`                                               |
| `source_documents`            | Source docs used                                                              |

---

## **7.3 Design Principle**

Metric Understanding cards should encode:

* Metric business meaning
* Metric aliases
* Metric type and unit
* Metric implementation logic
* Formula applicability
* Required input columns
* Semantic filters
* Allowed dimensions and grains
* Formula templates
* Metric dependencies

They should not encode:

* Tenant ownership
* Account-specific filters
* Cross-platform flow applicability
* Business workflow internals
* Reconciliation matching logic
* Query templates
* Validation tests
* Output contracts

Main principle:

```text
Metric definitions are global business concepts.
Metric implementations define formula validity.
Runtime scope and Account Data Binding decide whose data is filtered.
Business Flow Binding decides which cross-platform path is applicable.
```

---

# **7.4 Process Understanding Cards**

---

## **Purpose of this section**

Process Understanding cards define **what should happen** in the real-world business flow.

This section answers:

* Which business domain does the question belong to?
* Which business process is being discussed?
* What is the expected sequence of steps?
* Which platform types participate?
* What state should each business object move through?
* What lag or SLA is expected?
* Where can the process fail or become delayed?

This section should **not** define tenant ownership, runtime account filters, table schemas, metric formulas, reconciliation matching keys, SQL patterns, validation tests, or output contracts.

Business Flow Binding handles which tenant/group platform accounts participate in this process at runtime.

---

## **Card 17 — Domain Card**

**Purpose:** Represents a broad business area or financial operations domain.

**Fields:**

| Field                | Definition                                                                        |
| -------------------- | --------------------------------------------------------------------------------- |
| `card_type`          | Always `"domain"`                                                                 |
| `canonical_id`       | Stable domain ID                                                                  |
| `domain_name`        | Human-readable domain name                                                        |
| `description`        | What this domain covers                                                           |
| `domain_type`        | `analytics`, `reconciliation`, `diagnostics`, `operations`, `reporting`, or mixed |
| `platform_types`     | Platform types commonly involved                                                  |
| `common_metrics`     | Metric IDs commonly used                                                          |
| `business_processes` | Business Process IDs under this domain                                            |
| `common_questions`   | Typical user questions                                                            |
| `status`             | `draft`, `active`, `deprecated`                                                   |
| `source_documents`   | Source docs used                                                                  |

---

## **Card 18 — Business Process Card**

**Purpose:** Represents an end-to-end business process or operational flow.

A Business Process Card defines the reusable process model. It is not a tenant/account execution card.

**Fields:**

| Field                          | Definition                                                                             |
| ------------------------------ | -------------------------------------------------------------------------------------- |
| `card_type`                    | Always `"business_process"`                                                            |
| `canonical_id`                 | Stable business process ID                                                             |
| `process_name`                 | Human-readable process name                                                            |
| `description`                  | What the process does                                                                  |
| `domain_id`                    | Parent Domain ID                                                                       |
| `process_type`                 | `analytics`, `reconciliation`, `diagnostics`, `operational_workflow`, or mixed         |
| `participating_platform_types` | Platform types involved in the generic process                                         |
| `typical_platform_roles`       | Role played by each platform type                                                      |
| `business_objects`             | Objects moving through the process, e.g. order, payment, payout, shipment, bank_credit |
| `expected_start_state`         | Expected start state                                                                   |
| `expected_end_state`           | Expected end state                                                                     |
| `workflow_steps`               | Workflow Step IDs                                                                      |
| `state_transitions`            | State Transition IDs                                                                   |
| `common_metrics`               | Metric IDs used to evaluate process                                                    |
| `common_failure_modes`         | Common failure modes                                                                   |
| `applicability_scope`          | Scope where process model is valid; not runtime account selection                      |
| `status`                       | `draft`, `active`, `deprecated`                                                        |
| `source_documents`             | Source docs used                                                                       |

**Example:**

```json
{
  "card_type": "business_process",
  "canonical_id": "business_process.logistics_cod_to_bank_reconciliation",
  "process_name": "Logistics COD to Bank Reconciliation",
  "description": "Reconciles courier or logistics COD remittance against actual bank credits.",
  "domain_id": "domain.logistics_reconciliation",
  "process_type": "reconciliation",
  "participating_platform_types": ["logistics", "banking"],
  "typical_platform_roles": [
    {
      "platform_type": "logistics",
      "role": "Collects COD and creates remittance or settlement evidence."
    },
    {
      "platform_type": "banking",
      "role": "Receives actual bank credit corresponding to COD remittance."
    }
  ],
  "business_objects": ["shipment", "cod_remittance", "bank_credit"],
  "expected_start_state": "cod_collected_by_courier",
  "expected_end_state": "bank_credit_received",
  "workflow_steps": [
    "workflow_step.cod_collected_by_courier",
    "workflow_step.cod_remittance_batch_created",
    "workflow_step.bank_credit_received"
  ],
  "state_transitions": [],
  "common_metrics": [
    "metric.cod_remitted_amount",
    "metric.bank_credit_amount",
    "metric.reconciliation_gap_amount"
  ],
  "common_failure_modes": [
    "delivered_cod_not_remitted",
    "cod_remitted_but_bank_credit_missing",
    "partial_cod_remittance"
  ],
  "applicability_scope": {
    "scope_level": "platform_type",
    "platform_types": ["logistics", "banking"],
    "notes": [
      "Runtime account selection and tenant/group-specific applicability are resolved through Business Flow Binding."
    ]
  },
  "status": "active",
  "source_documents": []
}
```

---

## **Card 19 — Workflow Step Card**

**Purpose:** Represents one expected step inside a business process.

**Fields:**

| Field                 | Definition                                                                 |
| --------------------- | -------------------------------------------------------------------------- |
| `card_type`           | Always `"workflow_step"`                                                   |
| `canonical_id`        | Stable workflow step ID                                                    |
| `business_process_id` | Parent Business Process ID                                                 |
| `step_name`           | Human-readable step name                                                   |
| `step_order`          | Expected sequence order                                                    |
| `platform_type`       | Platform type usually responsible                                          |
| `platform_role`       | Role of the platform in this step                                          |
| `business_object`     | Main business object affected                                              |
| `expected_input`      | Input before this step                                                     |
| `expected_output`     | Output after this step                                                     |
| `expected_state`      | State created or confirmed                                                 |
| `expected_lag`        | Expected time lag, if applicable                                           |
| `required_evidence`   | Evidence that confirms step occurred; table/column concepts, not final SQL |
| `failure_modes`       | Failure modes for this step                                                |
| `status`              | `draft`, `active`, `deprecated`                                            |
| `source_documents`    | Source docs used                                                           |

---

## **Card 20 — State Transition Card**

**Purpose:** Represents an expected movement from one business state to another.

**Fields:**

| Field                   | Definition                                                          |
| ----------------------- | ------------------------------------------------------------------- |
| `card_type`             | Always `"state_transition"`                                         |
| `canonical_id`          | Stable state transition ID                                          |
| `business_process_id`   | Parent Business Process ID                                          |
| `from_state`            | Starting state                                                      |
| `to_state`              | Expected next state                                                 |
| `triggering_step_id`    | Workflow Step ID causing/confirming transition                      |
| `business_object`       | Object moving through transition                                    |
| `expected_lag`          | Expected time between states                                        |
| `lag_type`              | `instant`, `same_day`, `T+1`, `business_days`, `configurable`, etc. |
| `confirmation_evidence` | Evidence confirming transition                                      |
| `failure_if_missing`    | Failure mode if transition does not occur                           |
| `severity_if_breached`  | `low`, `medium`, `high`, `critical`                                 |
| `status`                | `draft`, `active`, `deprecated`                                     |
| `source_documents`      | Source docs used                                                    |

---

## **Card 21 — Process Variant Card**

**Purpose:** Represents a specific variation of a business process when the expected process changes materially by platform, region, channel, or operating model.

Create a Process Variant only when the process itself differs, not because tenant/group/account selection differs.

**Fields:**

| Field                          | Definition                                                                        |
| ------------------------------ | --------------------------------------------------------------------------------- |
| `card_type`                    | Always `"process_variant"`                                                        |
| `canonical_id`                 | Stable process variant ID                                                         |
| `base_business_process_id`     | Business Process ID this variant extends                                          |
| `variant_name`                 | Human-readable variant name                                                       |
| `variant_reason`               | Why this variant exists                                                           |
| `applicability_scope`          | Scope where this variant applies; process validity, not runtime account selection |
| `overridden_workflow_steps`    | Workflow Step IDs replaced/modified                                               |
| `additional_workflow_steps`    | Workflow Step IDs added                                                           |
| `removed_workflow_steps`       | Workflow Step IDs removed                                                         |
| `overridden_state_transitions` | State Transition IDs replaced/modified                                            |
| `lag_overrides`                | Expected lag changes                                                              |
| `failure_mode_overrides`       | Failure modes added/removed/changed                                               |
| `status`                       | `draft`, `active`, `deprecated`                                                   |
| `source_documents`             | Source docs used                                                                  |

---

## **7.4 Design Principle**

Process Understanding cards should encode:

* Business domains
* Generic business processes
* Expected workflow steps
* Expected state transitions
* Participating platform types
* Business objects moving through the process
* Expected lags and SLAs
* Process-level failure modes
* Process variants where expected flow changes materially

They should not encode:

* Tenant ownership
* Runtime account filters
* Tenant/group-specific platform account participation
* Table schema details
* Metric formulas
* Reconciliation matching keys
* SQL query patterns
* Validation tests
* Output contracts

Main principle:

```text
Business Process defines the generic expected flow.
Business Flow Binding decides which tenant/group platform accounts participate in that flow.
```

---

# **7.5 Reconciliation Understanding Cards**

---

## **Purpose of this section**

Reconciliation Understanding cards define **what should match** across systems, records, batches, states, or financial amounts.

This section answers:

* What kind of reconciliation is being performed?
* Which platform types participate?
* Which side is expected and which side is actual?
* What is the primary reconciliation unit?
* What secondary keys can be used?
* Should matching be exact, fuzzy, aggregated, staged, or hybrid?
* What amount and time tolerances apply?
* What mismatch categories should be recognized?

This section should **not** define table schemas, column semantics, account filters, metric formulas, process sequence, SQL patterns, validation tests, output contracts, or tenant/group-specific flow applicability.

Business Flow Binding selects which tenant/group platform accounts participate in a reconciliation at runtime.

---

## **Card 22 — Reconciliation Profile Card**

**Purpose:** Represents a reusable reconciliation model for a business process.

A Reconciliation Profile defines the matching model. It is not a tenant-specific execution card.

**Fields:**

| Field                               | Definition                                                                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `card_type`                         | Always `"reconciliation_profile"`                                                                                                |
| `canonical_id`                      | Stable reconciliation profile ID                                                                                                 |
| `profile_name`                      | Human-readable profile name                                                                                                      |
| `description`                       | What this profile compares                                                                                                       |
| `business_process_id`               | Business Process ID this profile supports                                                                                        |
| `process_variant_id`                | Process Variant ID, if applicable                                                                                                |
| `reconciliation_type`               | `order_to_shipment`, `shipment_to_invoice`, `cod_to_bank`, `payout_to_bank`, `settlement_to_bank`, `refund_reconciliation`, etc. |
| `participating_platform_types`      | Platform types involved                                                                                                          |
| `reconciliation_sides`              | Reconciliation Side IDs                                                                                                          |
| `business_object`                   | Main object reconciled                                                                                                           |
| `primary_reconciliation_unit_id`    | Primary Reconciliation Unit ID                                                                                                   |
| `secondary_reconciliation_unit_ids` | Fallback/supporting units                                                                                                        |
| `expected_alignment_type`           | `one_to_one`, `one_to_many`, `many_to_one`, `many_to_many`, `aggregated`                                                         |
| `matching_logic_id`                 | Matching Logic ID                                                                                                                |
| `mismatch_categories`               | Mismatch Category IDs                                                                                                            |
| `applicability_scope`               | Model validity scope, not runtime account selection                                                                              |
| `status`                            | `draft`, `active`, `deprecated`                                                                                                  |
| `source_documents`                  | Source docs used                                                                                                                 |

**Example:**

```json
{
  "card_type": "reconciliation_profile",
  "canonical_id": "reconciliation_profile.payment_gateway_payout_to_bank_credit",
  "profile_name": "Payment Gateway Payout to Bank Credit Reconciliation",
  "description": "Compares payment gateway payout batches against actual bank credits received in bank statements.",
  "business_process_id": "business_process.payment_gateway_to_bank_reconciliation",
  "process_variant_id": null,
  "reconciliation_type": "payout_to_bank",
  "participating_platform_types": ["payment_gateway", "banking"],
  "reconciliation_sides": [
    "reconciliation_side.payment_gateway_payout",
    "reconciliation_side.bank_credit"
  ],
  "business_object": "payout",
  "primary_reconciliation_unit_id": "reconciliation_unit.payout_reference",
  "secondary_reconciliation_unit_ids": [
    "reconciliation_unit.utr",
    "reconciliation_unit.amount_date_bank_account"
  ],
  "expected_alignment_type": "one_to_one",
  "matching_logic_id": "matching_logic.payment_gateway_payout_to_bank_credit",
  "mismatch_categories": [
    "mismatch_category.bank_credit_missing",
    "mismatch_category.amount_mismatch",
    "mismatch_category.reference_missing",
    "mismatch_category.unidentified_bank_credit",
    "mismatch_category.delayed_credit"
  ],
  "applicability_scope": {
    "scope_level": "platform_type",
    "platform_types": ["payment_gateway", "banking"],
    "notes": [
      "Runtime account participation is resolved through Business Flow Binding."
    ]
  },
  "status": "active",
  "source_documents": []
}
```

---

## **Card 23 — Reconciliation Side Card**

**Purpose:** Represents one side of a reconciliation comparison.

**Fields:**

| Field                 | Definition                                                                          |
| --------------------- | ----------------------------------------------------------------------------------- |
| `card_type`           | Always `"reconciliation_side"`                                                      |
| `canonical_id`        | Stable reconciliation side ID                                                       |
| `side_name`           | Human-readable side name                                                            |
| `side_role`           | `expected`, `actual`, `source`, `target`, `reference`, `operational_evidence`, etc. |
| `platform_type`       | Platform type usually providing this side                                           |
| `business_object`     | Object represented on this side                                                     |
| `expected_state`      | Expected state of records on this side                                              |
| `amount_concept`      | Amount concept used for comparison                                                  |
| `date_concept`        | Date concept used for timing comparison                                             |
| `identifier_concepts` | Business identifiers expected on this side                                          |
| `recommended_metrics` | Metric IDs commonly used                                                            |
| `typical_tables`      | Table IDs commonly used as evidence, if known                                       |
| `notes`               | Caveats or interpretation notes                                                     |
| `status`              | `draft`, `active`, `deprecated`                                                     |
| `source_documents`    | Source docs used                                                                    |

---

## **Card 24 — Reconciliation Unit Card**

**Purpose:** Represents the grain or business identifier at which reconciliation should happen.

**Fields:**

| Field                    | Definition                                                                                                        |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `card_type`              | Always `"reconciliation_unit"`                                                                                    |
| `canonical_id`           | Stable reconciliation unit ID                                                                                     |
| `unit_name`              | Human-readable unit name                                                                                          |
| `unit_type`              | `order`, `payment`, `payout`, `settlement`, `shipment`, `remittance_batch`, `bank_transaction`, `composite`, etc. |
| `description`            | What this unit represents                                                                                         |
| `identifier_concepts`    | Business identifiers that represent this unit                                                                     |
| `typical_platform_types` | Platform types where this unit appears                                                                            |
| `expected_uniqueness`    | `unique`, `mostly_unique`, `not_unique`, `composite_required`, `unknown`                                          |
| `preferred_usage`        | `primary`, `secondary`, `fallback`, `diagnostic_only`                                                             |
| `known_issues`           | Missing references, duplicate IDs, formatting differences, batch aggregation, etc.                                |
| `status`                 | `draft`, `active`, `deprecated`                                                                                   |
| `source_documents`       | Source docs used                                                                                                  |

---

## **Card 25 — Matching Logic Card**

**Purpose:** Defines how reconciliation sides should be matched.

**Fields:**

| Field                       | Definition                                                       |
| --------------------------- | ---------------------------------------------------------------- |
| `card_type`                 | Always `"matching_logic"`                                        |
| `canonical_id`              | Stable matching logic ID                                         |
| `logic_name`                | Human-readable logic name                                        |
| `description`               | What this matching logic does                                    |
| `reconciliation_profile_id` | Reconciliation Profile ID this supports                          |
| `matching_strategy`         | `exact`, `fuzzy`, `aggregated`, `staged`, `rule_based`, `hybrid` |
| `primary_match_keys`        | Primary key concepts/column concepts                             |
| `secondary_match_keys`      | Secondary key concepts                                           |
| `fallback_match_strategy`   | Fallback strategy                                                |
| `expected_alignment_type`   | Alignment type                                                   |
| `amount_tolerance`          | Amount tolerance rule                                            |
| `time_tolerance`            | Time lag tolerance                                               |
| `match_confidence_rules`    | High/medium/low confidence rules                                 |
| `unmatched_handling`        | How unmatched records should be classified                       |
| `notes`                     | Caveats or known issues                                          |
| `status`                    | `draft`, `active`, `deprecated`                                  |
| `source_documents`          | Source docs used                                                 |

---

## **Card 26 — Mismatch Category Card**

**Purpose:** Represents a reusable type of reconciliation discrepancy.

**Fields:**

| Field                      | Definition                                                                                                                              |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `card_type`                | Always `"mismatch_category"`                                                                                                            |
| `canonical_id`             | Stable mismatch category ID                                                                                                             |
| `category_name`            | Human-readable category name                                                                                                            |
| `category_type`            | `missing`, `extra`, `delayed`, `partial`, `duplicate`, `amount_mismatch`, `reference_mismatch`, `timing_mismatch`, `data_quality`, etc. |
| `description`              | What this mismatch means                                                                                                                |
| `affected_side`            | `expected_side`, `actual_side`, `both`, `unknown`                                                                                       |
| `business_interpretation`  | Business meaning                                                                                                                        |
| `severity`                 | `low`, `medium`, `high`, `critical`                                                                                                     |
| `temporary_or_final`       | `temporary`, `final`, `depends_on_window`, `unknown`                                                                                    |
| `typical_root_causes`      | Common causes                                                                                                                           |
| `recommended_next_actions` | Suggested investigation actions                                                                                                         |
| `status`                   | `draft`, `active`, `deprecated`                                                                                                         |
| `source_documents`         | Source docs used                                                                                                                        |

---

## **Card 27 — Reconciliation Variant Card**

**Purpose:** Represents a material variation in reconciliation behavior for a platform, context, process variant, or operating model.

Create only when the matching model changes materially, not when tenant/account selection changes.

**Fields:**

| Field                            | Definition                                          |
| -------------------------------- | --------------------------------------------------- |
| `card_type`                      | Always `"reconciliation_variant"`                   |
| `canonical_id`                   | Stable reconciliation variant ID                    |
| `base_reconciliation_profile_id` | Base Reconciliation Profile ID                      |
| `variant_name`                   | Human-readable variant name                         |
| `variant_reason`                 | Why this variant exists                             |
| `applicability_scope`            | Model-validity scope, not runtime account selection |
| `side_overrides`                 | Side IDs added/removed/replaced                     |
| `unit_overrides`                 | Unit IDs added/removed/replaced                     |
| `matching_logic_override_id`     | Matching Logic ID used instead of base              |
| `tolerance_overrides`            | Amount/time tolerance changes                       |
| `mismatch_category_overrides`    | Mismatch categories added/removed/changed           |
| `status`                         | `draft`, `active`, `deprecated`                     |
| `source_documents`               | Source docs used                                    |

---

## **7.5 Design Principle**

Reconciliation Understanding cards should encode:

* Reconciliation profiles
* Reconciliation sides
* Reconciliation units
* Matching logic
* Match confidence semantics
* Amount tolerance
* Time tolerance
* Expected alignment type
* Mismatch categories
* Reconciliation variants where matching behavior changes materially

They should not encode:

* Tenant ownership
* Runtime account filters
* Tenant/group-specific platform participation
* Table schemas
* Metric formulas
* Business workflow sequence
* SQL query templates
* Validation tests
* Output contracts

Main principle:

```text
Reconciliation Profile defines what should match.
Business Flow Binding decides which tenant/group platform accounts participate in that matching model.
```

---

# **7.6 Execution Guidance Cards**

---

## **Purpose of this section**

Execution Guidance cards define **how downstream execution should stay safe, valid, and structured**.

This section answers:

* Which query pattern should be followed?
* Which constraints must generated SQL or reconciliation logic obey?
* Which filters are mandatory?
* Which joins are allowed or unsafe?
* Which aggregation rules prevent double counting?
* Which validation tests must pass?
* What should the structured output look like?

This section should **not** define tenant ownership, account filters, table schemas, metric definitions, process flow, or conceptual reconciliation semantics.

Execution Guidance does not replace the orchestrator. The orchestrator still owns planning, tool selection, SQL generation, execution, retries, and repair.

---

## **Card 28 — Query Pattern Card**

**Purpose:** Represents an approved query shape or analytical/reconciliation query pattern.

Runtime scope, Account Data Binding, and Business Flow Binding are injected/used during execution planning. Query Pattern itself should not hardcode tenant/group/account filters.

**Fields:**

| Field                      | Definition                                                            |
| -------------------------- | --------------------------------------------------------------------- |
| `card_type`                | Always `"query_pattern"`                                              |
| `canonical_id`             | Stable query pattern ID                                               |
| `pattern_name`             | Human-readable pattern name                                           |
| `description`              | What this pattern does                                                |
| `pattern_type`             | `analytical`, `reconciliation`, `diagnostic`, `operational`, or mixed |
| `supported_intents`        | User intents this pattern supports                                    |
| `applicability_scope`      | Pattern-validity scope, not runtime account selection                 |
| `required_tables`          | Required Table IDs                                                    |
| `optional_tables`          | Optional Table IDs                                                    |
| `required_metrics`         | Metric IDs produced/used                                              |
| `allowed_dimensions`       | Dimensions safe to group by                                           |
| `allowed_grains`           | Supported grains                                                      |
| `recommended_date_columns` | Recommended date columns                                              |
| `semantic_filters`         | Non-account filters required for correctness                          |
| `join_constraints`         | Relationship IDs or join constraints                                  |
| `aggregation_rules`        | Rules to prevent double counting/grain mismatch                       |
| `query_shape`              | Pseudo-SQL or structural outline                                      |
| `linked_rules`             | Rule IDs required                                                     |
| `validation_tests`         | Validation Test IDs                                                   |
| `output_contract_id`       | Expected Output Contract ID                                           |
| `confidence`               | `high`, `medium`, `low`                                               |
| `status`                   | `draft`, `active`, `deprecated`                                       |
| `source_documents`         | Source docs used                                                      |

---

## **Card 29 — Rule Card**

**Purpose:** Represents a mandatory execution constraint, warning, or guardrail.

**Fields:**

| Field               | Definition                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `card_type`         | Always `"rule"`                                                                                                                                                    |
| `canonical_id`      | Stable rule ID                                                                                                                                                     |
| `rule_name`         | Human-readable rule name                                                                                                                                           |
| `description`       | What this rule enforces                                                                                                                                            |
| `rule_type`         | `scope_filter`, `date_safety`, `null_handling`, `join_safety`, `aggregation_safety`, `status_filter`, `reconciliation_window`, `casting`, `metric_semantics`, etc. |
| `severity`          | `critical`, `high`, `medium`, `low`                                                                                                                                |
| `applies_to`        | Cards/card types this rule applies to                                                                                                                              |
| `rule_statement`    | Plain-English rule statement                                                                                                                                       |
| `required_pattern`  | Required SQL/logical pattern, if applicable                                                                                                                        |
| `forbidden_pattern` | Forbidden SQL/logical pattern, if applicable                                                                                                                       |
| `failure_mode`      | What goes wrong if ignored                                                                                                                                         |
| `auto_fix_hint`     | Suggested correction                                                                                                                                               |
| `validator_type`    | `sql_contains`, `sql_not_contains`, `regex`, `ast_check`, `semantic_check`, `grain_check`, etc.                                                                    |
| `status`            | `draft`, `active`, `deprecated`                                                                                                                                    |
| `source_documents`  | Source docs used                                                                                                                                                   |

**Example rule update:**

```json
{
  "card_type": "rule",
  "canonical_id": "rule.required_scope_and_flow_context",
  "rule_name": "Required scope and flow context must be resolved",
  "description": "Generated SQL must include resolved account/table scope filters and must use the correct Business Flow Binding for cross-platform workflows.",
  "rule_type": "scope_filter",
  "severity": "critical",
  "applies_to": [
    "card_type.query_pattern",
    "card_type.reconciliation_profile",
    "card_type.business_flow_binding"
  ],
  "rule_statement": "Every query against tenant-scoped source tables must apply Account Data Binding filters. Cross-platform reconciliation queries must also use the selected Business Flow Binding when one exists.",
  "required_pattern": "resolved_scope_filters_present_and_flow_binding_checked",
  "forbidden_pattern": null,
  "failure_mode": "Query may compare the wrong platform accounts or miss the correct cross-platform evidence path.",
  "auto_fix_hint": "Resolve Business Flow Binding first, then inject Account Data Binding filters for each selected platform account/table combination.",
  "validator_type": "semantic_check",
  "status": "active",
  "source_documents": []
}
```

---

## **Card 30 — Validation Test Card**

**Purpose:** Represents a deterministic test that checks whether generated SQL, matching logic, or structured output follows required rules.

**Fields:**

| Field                | Definition                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `card_type`          | Always `"validation_test"`                                                                                                           |
| `canonical_id`       | Stable validation test ID                                                                                                            |
| `test_name`          | Human-readable test name                                                                                                             |
| `description`        | What the test validates                                                                                                              |
| `test_type`          | `sql_contains`, `sql_not_contains`, `regex`, `ast_check`, `semantic_check`, `grain_check`, `join_check`, `output_schema_check`, etc. |
| `linked_rule_id`     | Rule ID this test enforces                                                                                                           |
| `applies_to`         | Cards/card types this applies to                                                                                                     |
| `required_pattern`   | Required SQL/logical/output pattern                                                                                                  |
| `forbidden_pattern`  | Forbidden pattern                                                                                                                    |
| `semantic_condition` | Higher-level condition                                                                                                               |
| `severity`           | `critical`, `high`, `medium`, `low`                                                                                                  |
| `failure_message`    | Message when validation fails                                                                                                        |
| `auto_fix_hint`      | Suggested correction                                                                                                                 |
| `blocking`           | Whether failure blocks execution                                                                                                     |
| `status`             | `draft`, `active`, `deprecated`                                                                                                      |
| `source_documents`   | Source docs used                                                                                                                     |

---

## **Card 31 — Output Contract Card**

**Purpose:** Defines the required structured output shape for analytical, reconciliation, diagnostic, or operational responses.

**Fields:**

| Field                  | Definition                                                               |
| ---------------------- | ------------------------------------------------------------------------ |
| `card_type`            | Always `"output_contract"`                                               |
| `canonical_id`         | Stable output contract ID                                                |
| `contract_name`        | Human-readable contract name                                             |
| `description`          | What this output contract is used for                                    |
| `output_type`          | `analytical`, `reconciliation`, `diagnostic`, `operational`, `reporting` |
| `required_sections`    | Required top-level output sections                                       |
| `optional_sections`    | Optional output sections                                                 |
| `schema`               | JSON-style expected output schema                                        |
| `required_fields`      | Fields that must be present                                              |
| `record_grouping`      | How record outputs should be grouped                                     |
| `sorting_guidance`     | Preferred sorting                                                        |
| `display_guidance`     | UI/reporting guidance                                                    |
| `failure_output_shape` | Output shape when execution cannot complete                              |
| `status`               | `draft`, `active`, `deprecated`                                          |
| `source_documents`     | Source docs used                                                         |

---

## **Card 32 — Execution Constraint Set Card**

**Purpose:** Groups rules, validation tests, query patterns, and output contracts into a reusable execution guardrail bundle.

**Fields:**

| Field                 | Definition                                                            |
| --------------------- | --------------------------------------------------------------------- |
| `card_type`           | Always `"execution_constraint_set"`                                   |
| `canonical_id`        | Stable execution constraint set ID                                    |
| `constraint_set_name` | Human-readable name                                                   |
| `description`         | What this set enforces                                                |
| `constraint_set_type` | `analytical`, `reconciliation`, `diagnostic`, `operational`, or mixed |
| `applies_to`          | Cards/card types this applies to                                      |
| `rules`               | Rule IDs included                                                     |
| `validation_tests`    | Validation Test IDs included                                          |
| `query_patterns`      | Query Pattern IDs covered                                             |
| `output_contract_id`  | Expected Output Contract ID                                           |
| `blocking_failures`   | Validation failures that block execution                              |
| `warning_failures`    | Validation failures that create warnings                              |
| `status`              | `draft`, `active`, `deprecated`                                       |
| `source_documents`    | Source docs used                                                      |

---

## **7.6 Design Principle**

Execution Guidance cards should encode:

* Query patterns
* Execution rules
* Validation tests
* Output contracts
* Guardrail bundles
* Mandatory semantic filters
* Join constraints
* Aggregation safeguards
* Date safety rules
* Double-counting prevention
* Structured output expectations

They should not encode:

* Tenant ownership
* Account-specific filter values
* Table schemas
* Column semantics
* Metric business definitions
* Business workflow sequence
* Conceptual reconciliation semantics
* Orchestrator planning steps

Main principle:

```text
Execution Guidance defines constraints, patterns, validations, and contracts.
The orchestrator owns planning and execution.
Account Data Binding supplies table filters.
Business Flow Binding supplies cross-platform flow applicability.
```

---

# **7.7 Section Summary**

The updated Section 07 has one key evolutionary correction:

```text
Do not create domain-specific binding cards such as Logistics Route Binding, Payment Route Binding, or Banking Route Binding.

Create one generic Business Flow Binding that can represent cross-platform applicability for any tenant/group flow.
```

Final card-family responsibilities:

| Family                       | Owns                                                                                    |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| Business Hierarchy           | Identity, connected accounts, account bindings, reusable scopes, business flow bindings |
| Data Understanding           | Tables, columns, relationships, values, structural applicability                        |
| Metric Understanding         | Metric meaning, formulas, implementations, dependencies                                 |
| Process Understanding        | Expected process flow and process variants                                              |
| Reconciliation Understanding | Matching model, sides, units, logic, mismatch categories                                |
| Execution Guidance           | Query patterns, rules, validation tests, output contracts                               |

Core model:

```text
Tenant / Group
→ Platform Accounts
→ Account Data Bindings
→ Business Scope Sets
→ Business Flow Bindings
→ Process / Reconciliation / Data / Metric / Execution cards
```

Business Flow Binding becomes the bridge between tenant/group identity and cross-platform business reality.
