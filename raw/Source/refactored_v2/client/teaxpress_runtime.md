# Teaxpress Private Limited — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `teaxpress_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Bluedart
  config: Settlement + Invoice
  reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: XpressBees invoice/report
  config: Settlement report + Invoice
  reason: No native XpressBees invoice or settlement-report table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: India Post
  config: Via amazon_shipping_settlement_report
  reason: No India Post canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: PayU
  config: payu_settlement Teabox + Sammvaad
  reason: No PayU canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 10
  account_data_binding: 14
  business_scope_set: 6
  business_flow_binding: 6
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 12
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 14
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 14
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 6
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 14
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 10
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 6
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 6
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 14
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 10
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 10
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 10
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 6
  GROUP_HAS_BUSINESS_SCOPE_SET: 6
  GROUP_HAS_PLATFORM_ACCOUNT: 10
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 10
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 14
  PLATFORM_ACCOUNT_USES_PLATFORM: 10
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 10
  TENANT_HAS_GROUP: 1
allowed_card_types:
- tenant
- group
- platform_account
- account_data_binding
- business_scope_set
- business_flow_binding
render_order:
- tenant
- group
- platform_account
- account_data_binding
- business_scope_set
- business_flow_binding
boundary_policy: client runtime only; no reusable semantic card bodies are emitted in this file
integration_layers:
- marketplace
- logistics
- oms
- wms
- payment_gateway
- bank_statement
wms_integration:
  source_packs:
  - increff_wms.md
  - unicommerce_wms.md
  added_runtime_cards: 5
  added_runtime_edges: 25
  supported_wms_accounts: 1
  supported_wms_bindings: 2
  resolved_deferred_mentions: 1
bank_payment_integration:
  source_packs:
  - payment_gateway.md
  - bank_statement.md
  added_runtime_cards: 10
  added_runtime_edges: 49
  supported_payment_bindings: 1
  supported_bank_bindings: 2
  deferred_financial_sources_added_or_updated: 1
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.teaxpress_private_limited

```yaml
canonical_card:
  canonical_id: tenant.teaxpress_private_limited
  card_type: tenant
  canonical_name: Teaxpress Private Limited
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited
    - teaxpress_private_limited
    - Teaxpress Private Limited runtime tenant
    colloquial_phrases:
    - Teaxpress Private Limited client runtime
    - Teaxpress Private Limited source configuration
    - Teaxpress Private Limited scoped reconciliation setup
    business_meaning: Runtime tenant identity for Teaxpress Private Limited. It anchors the client's marketplace,
      logistics, OMS, WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from
      reusable domain semantics.
    business_questions:
    - Which source families and configured accounts belong to Teaxpress Private Limited?
    - Which group and account bindings should constrain Teaxpress Private Limited's SQL handoff?
    - After Teaxpress Private Limited's runtime scope is resolved, which domain layer should receive the query next?
    semantic_tags:
    - client_runtime
    - tenant_identity
    - source_scope_root
    - runtime_boundary
    included_concepts:
    - client legal identity
    - runtime source routing
    - group/account traversal root
    excluded_concepts:
    - reusable platform semantics
    - physical table definitions
    - metric formulas
    caveats:
    - Do not infer platform coverage from this tenant card alone; use the linked platform-account and account-data-binding
      cards.
    examples: []
  retrieval:
    node_sets:
    - card_type:tenant
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    embedding_text: Teaxpress Private Limited is the runtime tenant root for the client's marketplace, logistics,
      OMS, WMS, payment-gateway, and bank-statement configuration. Use it to reach group, platform-account, and
      account-data-binding nodes before invoking reusable canonical packs.
    search_keywords:
    - Teaxpress Private Limited
    - teaxpress_private_limited
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.teaxpress_private_limited
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    source_path: Teaxpress Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
  fields:
    tenant_slug: teaxpress_private_limited
    tenant_name: Teaxpress Private Limited
    legal_name: Teaxpress Private Limited
    active: true
```

### 2.2 Group Cards

#### group.teaxpress_private_limited.g52.gl190

```yaml
canonical_card:
  canonical_id: group.teaxpress_private_limited.g52.gl190
  card_type: group
  canonical_name: Teaxpress Private Limited group 52/190
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - TeaBox
    - Teaxpress Private Limited group 52/190
    - group_id 52
    - group_level_id 190
    colloquial_phrases:
    - Teaxpress Private Limited group scope
    - TeaBox runtime scope
    - group 52 level 190 query boundary
    business_meaning: 'Runtime group scope for Teaxpress Private Limited: group_id=52 and group_level_id=190. It
      is the client-specific filter boundary that must be applied before resolving account bindings for IN in INR.'
    business_questions:
    - Which bindings use group_id=52 and group_level_id=190?
    - Which source families are active under TeaBox?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=52
    - group_level_id=190
    - client group runtime scope
    excluded_concepts:
    - domain metric logic
    - platform table schemas
    - bank or gateway account ownership by itself
    caveats:
    - Treat this as runtime scope only; do not create reusable tenant or platform semantics from group IDs.
    examples: []
  retrieval:
    node_sets:
    - card_type:group
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - group_id_value:52
    - group_level_id_value:190
    embedding_text: TeaBox is the runtime group node for Teaxpress Private Limited. Apply group_id=52 and group_level_id=190
      when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Teaxpress Private Limited
    - TeaBox
    - group_id 52
    - group_level_id 190
    - runtime group scope
    exact_match_keys:
    - group.teaxpress_private_limited.g52.gl190
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    source_path: Teaxpress Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    group_level_id: '190'
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id_value: '52'
    group_level_id_value: '190'
    group_name: TeaBox
    default_currency: INR
    country: IN
```

### 2.3 Platform Account Cards

#### platform_account.teaxpress_private_limited.delhivery.logistics

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.delhivery.logistics
  card_type: platform_account
  canonical_name: Teaxpress Private Limited Delhivery Logistics account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited Delhivery Logistics account
    - Teaxpress Private Limited Teaxpress Private Limited Delhivery Logistics account
    - Delhivery
    - Teaxpress Private Limited Delhivery Logistics account logistics / courier account
    colloquial_phrases:
    - Teaxpress Private Limited Teaxpress Private Limited Delhivery Logistics account source account
    - Teaxpress Private Limited Delhivery Logistics account logistics / courier runtime account
    - Teaxpress Private Limited Delhivery Logistics account configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's Teaxpress Private Limited Delhivery
      Logistics account logistics / courier sources. It points traversal to platform.delhivery and platform_context.delhivery.in
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Teaxpress Private Limited Delhivery Logistics account table bindings are available for Teaxpress Private
      Limited?
    - Which canonical platform/context should Teaxpress Private Limited's Teaxpress Private Limited Delhivery Logistics
      account questions traverse through?
    - Which source roles under Teaxpress Private Limited Delhivery Logistics account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.delhivery
    - platform_context.delhivery.in
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.delhivery.logistics
    - platform_id:platform.delhivery
    - platform_context_id:platform_context.delhivery.in
    - runtime_source_family:logistics
    embedding_text: Teaxpress Private Limited's Teaxpress Private Limited Delhivery Logistics account platform account
      routes logistics / courier questions to platform.delhivery / platform_context.delhivery.in. Use it to collect
      the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited Delhivery Logistics account
    - Delhivery
    - logistics / courier
    - platform.delhivery
    - platform_context.delhivery.in
    exact_match_keys:
    - platform_account.teaxpress_private_limited.delhivery.logistics
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.delhivery.logistics
    platform_id: platform.delhivery
    platform_context_id: platform_context.delhivery.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.delhivery
    platform_context_id: platform_context.delhivery.in
    account_name: Teaxpress Private Limited Delhivery Logistics account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```

#### platform_account.teaxpress_private_limited.dtdc.logistics

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.dtdc.logistics
  card_type: platform_account
  canonical_name: Teaxpress Private Limited DTDC Logistics account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited DTDC Logistics account
    - Teaxpress Private Limited Teaxpress Private Limited DTDC Logistics account
    - DTDC
    - Teaxpress Private Limited DTDC Logistics account logistics / courier account
    colloquial_phrases:
    - Teaxpress Private Limited Teaxpress Private Limited DTDC Logistics account source account
    - Teaxpress Private Limited DTDC Logistics account logistics / courier runtime account
    - Teaxpress Private Limited DTDC Logistics account configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's Teaxpress Private Limited DTDC Logistics
      account logistics / courier sources. It points traversal to platform.dtdc and platform_context.dtdc.in and
      groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Teaxpress Private Limited DTDC Logistics account table bindings are available for Teaxpress Private
      Limited?
    - Which canonical platform/context should Teaxpress Private Limited's Teaxpress Private Limited DTDC Logistics
      account questions traverse through?
    - Which source roles under Teaxpress Private Limited DTDC Logistics account are active or review-required for
      this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.dtdc
    - platform_context.dtdc.in
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.dtdc.logistics
    - platform_id:platform.dtdc
    - platform_context_id:platform_context.dtdc.in
    - runtime_source_family:logistics
    embedding_text: Teaxpress Private Limited's Teaxpress Private Limited DTDC Logistics account platform account
      routes logistics / courier questions to platform.dtdc / platform_context.dtdc.in. Use it to collect the client's
      table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited DTDC Logistics account
    - DTDC
    - logistics / courier
    - platform.dtdc
    - platform_context.dtdc.in
    exact_match_keys:
    - platform_account.teaxpress_private_limited.dtdc.logistics
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.dtdc.logistics
    platform_id: platform.dtdc
    platform_context_id: platform_context.dtdc.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.dtdc
    platform_context_id: platform_context.dtdc.in
    account_name: Teaxpress Private Limited DTDC Logistics account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```

#### platform_account.teaxpress_private_limited.ekart.logistics

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.ekart.logistics
  card_type: platform_account
  canonical_name: Teaxpress Private Limited Ekart Logistics account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited Ekart Logistics account
    - Teaxpress Private Limited Teaxpress Private Limited Ekart Logistics account
    - Ekart
    - Teaxpress Private Limited Ekart Logistics account logistics / courier account
    colloquial_phrases:
    - Teaxpress Private Limited Teaxpress Private Limited Ekart Logistics account source account
    - Teaxpress Private Limited Ekart Logistics account logistics / courier runtime account
    - Teaxpress Private Limited Ekart Logistics account configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's Teaxpress Private Limited Ekart Logistics
      account logistics / courier sources. It points traversal to platform.ekart and platform_context.ekart.in and
      groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Teaxpress Private Limited Ekart Logistics account table bindings are available for Teaxpress Private
      Limited?
    - Which canonical platform/context should Teaxpress Private Limited's Teaxpress Private Limited Ekart Logistics
      account questions traverse through?
    - Which source roles under Teaxpress Private Limited Ekart Logistics account are active or review-required for
      this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.ekart
    - platform_context.ekart.in
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.ekart.logistics
    - platform_id:platform.ekart
    - platform_context_id:platform_context.ekart.in
    - runtime_source_family:logistics
    embedding_text: Teaxpress Private Limited's Teaxpress Private Limited Ekart Logistics account platform account
      routes logistics / courier questions to platform.ekart / platform_context.ekart.in. Use it to collect the
      client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited Ekart Logistics account
    - Ekart
    - logistics / courier
    - platform.ekart
    - platform_context.ekart.in
    exact_match_keys:
    - platform_account.teaxpress_private_limited.ekart.logistics
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.ekart.logistics
    platform_id: platform.ekart
    platform_context_id: platform_context.ekart.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.ekart
    platform_context_id: platform_context.ekart.in
    account_name: Teaxpress Private Limited Ekart Logistics account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```

#### platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  card_type: platform_account
  canonical_name: Teaxpress Private Limited — India Post Via amazon_shipping_settlement_report
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - India Post Via amazon_shipping_settlement_report
    - Teaxpress Private Limited India Post Via amazon_shipping_settlement_report
    - Amazon
    - India Post Via amazon_shipping_settlement_report marketplace account
    colloquial_phrases:
    - Teaxpress Private Limited India Post Via amazon_shipping_settlement_report source account
    - India Post Via amazon_shipping_settlement_report marketplace runtime account
    - India Post Via amazon_shipping_settlement_report configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's India Post Via amazon_shipping_settlement_report
      marketplace sources. It points traversal to platform.amazon and platform_context.amazon.in and groups the
      client's table-level account-data bindings for this source.
    business_questions:
    - Which India Post Via amazon_shipping_settlement_report table bindings are available for Teaxpress Private
      Limited?
    - Which canonical platform/context should Teaxpress Private Limited's India Post Via amazon_shipping_settlement_report
      questions traverse through?
    - Which source roles under India Post Via amazon_shipping_settlement_report are active or review-required for
      this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Single (shared)'
    - platform.amazon
    - platform_context.amazon.in
    - India Post Via amazon_shipping_settlement_report
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - platform_account_id:platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
    embedding_text: Teaxpress Private Limited's India Post Via amazon_shipping_settlement_report platform account
      routes marketplace questions to platform.amazon / platform_context.amazon.in. Use it to collect the client's
      table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - India Post Via amazon_shipping_settlement_report
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.in
    exact_match_keys:
    - platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    source_path: Teaxpress Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    platform_account_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_name: India Post Via amazon_shipping_settlement_report
    account_type: marketplace_seller_account
    source_account_identifier: India Post Via amazon_shipping_settlement_report
    active: true
    configured_source_description: Single (shared)
```

#### platform_account.teaxpress_private_limited.shopify_d2c.oms

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  card_type: platform_account
  canonical_name: Teaxpress Private Limited Shopify D2C OMS account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited Shopify D2C OMS account
    - Teaxpress Private Limited Teaxpress Private Limited Shopify D2C OMS account
    - Shopify
    - Teaxpress Private Limited Shopify D2C OMS account OMS account
    colloquial_phrases:
    - Teaxpress Private Limited Teaxpress Private Limited Shopify D2C OMS account source account
    - Teaxpress Private Limited Shopify D2C OMS account OMS runtime account
    - Teaxpress Private Limited Shopify D2C OMS account configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's Teaxpress Private Limited Shopify
      D2C OMS account OMS sources. It points traversal to platform.shopify and platform_context.shopify.in.d2c_oms
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Teaxpress Private Limited Shopify D2C OMS account table bindings are available for Teaxpress Private
      Limited?
    - Which canonical platform/context should Teaxpress Private Limited's Teaxpress Private Limited Shopify D2C
      OMS account questions traverse through?
    - Which source roles under Teaxpress Private Limited Shopify D2C OMS account are active or review-required for
      this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: Shopify D2C OMS and returns/refund events'
    - platform.shopify
    - platform_context.shopify.in.d2c_oms
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - runtime_source_family:oms
    embedding_text: Teaxpress Private Limited's Teaxpress Private Limited Shopify D2C OMS account platform account
      routes OMS questions to platform.shopify / platform_context.shopify.in.d2c_oms. Use it to collect the client's
      table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited Shopify D2C OMS account
    - Shopify
    - OMS
    - platform.shopify
    - platform_context.shopify.in.d2c_oms
    exact_match_keys:
    - platform_account.teaxpress_private_limited.shopify_d2c.oms
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - shopify_d2c_oms.md
    source_path: Teaxpress Private Limited.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    runtime_source_family: oms
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_name: Teaxpress Private Limited Shopify D2C OMS account
    account_type: d2c_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Shopify D2C OMS and returns/refund events
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: available_shopify_pack_context
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```

#### platform_account.teaxpress_private_limited.unicommerce_wms.wms

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  card_type: platform_account
  canonical_name: Teaxpress Private Limited — Unicommerce WMS
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Unicommerce WMS
    - Teaxpress Private Limited Unicommerce WMS
    - Unicommerce
    - Unicommerce WMS WMS account
    colloquial_phrases:
    - Teaxpress Private Limited Unicommerce WMS source account
    - Unicommerce WMS WMS runtime account
    - Unicommerce WMS configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's Unicommerce WMS WMS sources. It points
      traversal to platform.unicommerce and platform_context.unicommerce.in_wms and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Unicommerce WMS table bindings are available for Teaxpress Private Limited?
    - Which canonical platform/context should Teaxpress Private Limited's Unicommerce WMS questions traverse through?
    - Which source roles under Unicommerce WMS are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - WMS
    - source_router
    included_concepts:
    - 'client configuration: order management / marketplace sync / WMS fulfilment'
    - platform.unicommerce
    - platform_context.unicommerce.in_wms
    - Unicommerce WMS
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - platform_account_id:platform_account.teaxpress_private_limited.unicommerce_wms.wms
    - runtime_source_family:wms
    embedding_text: Teaxpress Private Limited's Unicommerce WMS platform account routes WMS questions to platform.unicommerce
      / platform_context.unicommerce.in_wms. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - Unicommerce WMS
    - Unicommerce
    - WMS
    - platform.unicommerce
    - platform_context.unicommerce.in_wms
    exact_match_keys:
    - platform_account.teaxpress_private_limited.unicommerce_wms.wms
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - unicommerce_wms.md
    source_path: Teaxpress Private Limited.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
    runtime_source_family: wms
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    account_name: Unicommerce WMS
    account_type: wms_operator_account
    source_account_identifier: Unicommerce WMS
    source_account_identifier_status: client_docx_names_wms_system_without_separate_account_number
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: order management / marketplace sync / WMS fulfilment
    canonical_source_pack: unicommerce_wms.md
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```

#### platform_account.teaxpress_private_limited.xpressbees.logistics

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  card_type: platform_account
  canonical_name: Teaxpress Private Limited XpressBees Logistics account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited XpressBees Logistics account
    - Teaxpress Private Limited Teaxpress Private Limited XpressBees Logistics account
    - XpressBees
    - Teaxpress Private Limited XpressBees Logistics account logistics / courier account
    colloquial_phrases:
    - Teaxpress Private Limited Teaxpress Private Limited XpressBees Logistics account source account
    - Teaxpress Private Limited XpressBees Logistics account logistics / courier runtime account
    - Teaxpress Private Limited XpressBees Logistics account configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's Teaxpress Private Limited XpressBees
      Logistics account logistics / courier sources. It points traversal to platform.xpressbees and platform_context.xpressbees.in
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Teaxpress Private Limited XpressBees Logistics account table bindings are available for Teaxpress Private
      Limited?
    - Which canonical platform/context should Teaxpress Private Limited's Teaxpress Private Limited XpressBees Logistics
      account questions traverse through?
    - Which source roles under Teaxpress Private Limited XpressBees Logistics account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.xpressbees
    - platform_context.xpressbees.in
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.xpressbees.logistics
    - platform_id:platform.xpressbees
    - platform_context_id:platform_context.xpressbees.in
    - runtime_source_family:logistics
    embedding_text: Teaxpress Private Limited's Teaxpress Private Limited XpressBees Logistics account platform
      account routes logistics / courier questions to platform.xpressbees / platform_context.xpressbees.in. Use
      it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited XpressBees Logistics account
    - XpressBees
    - logistics / courier
    - platform.xpressbees
    - platform_context.xpressbees.in
    exact_match_keys:
    - platform_account.teaxpress_private_limited.xpressbees.logistics
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.xpressbees.logistics
    platform_id: platform.xpressbees
    platform_context_id: platform_context.xpressbees.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.xpressbees
    platform_context_id: platform_context.xpressbees.in
    account_name: Teaxpress Private Limited XpressBees Logistics account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```

#### platform_account.teaxpress_private_limited.razorpay.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  card_type: platform_account
  canonical_name: Teaxpress Private Limited — Razorpay payment gateway
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Razorpay
    - Teaxpress Private Limited Razorpay
    - Razorpay payment gateway account
    colloquial_phrases:
    - Teaxpress Private Limited Razorpay source account
    - Razorpay payment gateway runtime account
    - Razorpay configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's Razorpay payment gateway sources.
      It points traversal to platform.razorpay and platform_context.razorpay.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Razorpay table bindings are available for Teaxpress Private Limited?
    - Which canonical platform/context should Teaxpress Private Limited's Razorpay questions traverse through?
    - Which source roles under Razorpay are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: Razorpay'
    - platform.razorpay
    - platform_context.razorpay.in
    - Razorpay
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - platform_account_id:platform_account.teaxpress_private_limited.razorpay.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Teaxpress Private Limited's Razorpay platform account routes payment gateway questions to platform.razorpay
      / platform_context.razorpay.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - Razorpay
    - payment gateway
    - platform.razorpay
    - platform_context.razorpay.in
    exact_match_keys:
    - platform_account.teaxpress_private_limited.razorpay.payment_gateway
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - payment_gateway.md
    source_path: Teaxpress Private Limited.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    platform_account_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    account_name: Razorpay
    account_type: payment_gateway_account
    source_account_identifier: Razorpay
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```

#### platform_account.teaxpress_private_limited.axis_bank.bank_statement

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  card_type: platform_account
  canonical_name: Teaxpress Private Limited — Axis Bank bank statement
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Axis Bank
    - Teaxpress Private Limited Axis Bank
    - Axis Bank bank statement account
    colloquial_phrases:
    - Teaxpress Private Limited Axis Bank source account
    - Axis Bank bank statement runtime account
    - Axis Bank configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's Axis Bank bank statement sources.
      It points traversal to platform.axis_bank and platform_context.axis_bank.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Axis Bank table bindings are available for Teaxpress Private Limited?
    - Which canonical platform/context should Teaxpress Private Limited's Axis Bank questions traverse through?
    - Which source roles under Axis Bank are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - bank_statement
    - source_router
    included_concepts:
    - 'client configuration: Axis Bank'
    - platform.axis_bank
    - platform_context.axis_bank.in
    - Axis Bank
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_id:platform.axis_bank
    - platform_context_id:platform_context.axis_bank.in
    - platform_account_id:platform_account.teaxpress_private_limited.axis_bank.bank_statement
    - runtime_source_family:bank_statement
    embedding_text: Teaxpress Private Limited's Axis Bank platform account routes bank statement questions to platform.axis_bank
      / platform_context.axis_bank.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - Axis Bank
    - bank statement
    - platform.axis_bank
    - platform_context.axis_bank.in
    exact_match_keys:
    - platform_account.teaxpress_private_limited.axis_bank.bank_statement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - bank_statement.md
    source_path: Teaxpress Private Limited.docx plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.axis_bank
    platform_context_id: platform_context.axis_bank.in
    platform_account_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
    runtime_source_family: bank_statement
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.axis_bank
    platform_context_id: platform_context.axis_bank.in
    account_name: Axis Bank
    account_type: bank_statement_account
    source_account_identifier: Axis Bank
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: bank_statement
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: bank_statement.md
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```

#### platform_account.teaxpress_private_limited.hdfc_bank.bank_statement

```yaml
canonical_card:
  canonical_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  card_type: platform_account
  canonical_name: Teaxpress Private Limited — HDFC Bank bank statement
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - HDFC Bank
    - Teaxpress Private Limited HDFC Bank
    - HDFC Bank bank statement account
    colloquial_phrases:
    - Teaxpress Private Limited HDFC Bank source account
    - HDFC Bank bank statement runtime account
    - HDFC Bank configured source family
    business_meaning: Runtime platform account for Teaxpress Private Limited's HDFC Bank bank statement sources.
      It points traversal to platform.hdfc_bank and platform_context.hdfc_bank.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which HDFC Bank table bindings are available for Teaxpress Private Limited?
    - Which canonical platform/context should Teaxpress Private Limited's HDFC Bank questions traverse through?
    - Which source roles under HDFC Bank are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - bank_statement
    - source_router
    included_concepts:
    - 'client configuration: HDFC Bank'
    - platform.hdfc_bank
    - platform_context.hdfc_bank.in
    - HDFC Bank
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_id:platform.hdfc_bank
    - platform_context_id:platform_context.hdfc_bank.in
    - platform_account_id:platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
    - runtime_source_family:bank_statement
    embedding_text: Teaxpress Private Limited's HDFC Bank platform account routes bank statement questions to platform.hdfc_bank
      / platform_context.hdfc_bank.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Teaxpress Private Limited
    - HDFC Bank
    - bank statement
    - platform.hdfc_bank
    - platform_context.hdfc_bank.in
    exact_match_keys:
    - platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - bank_statement.md
    source_path: Teaxpress Private Limited.docx plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.hdfc_bank
    platform_context_id: platform_context.hdfc_bank.in
    platform_account_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
    runtime_source_family: bank_statement
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_id: platform.hdfc_bank
    platform_context_id: platform_context.hdfc_bank.in
    account_name: HDFC Bank
    account_type: bank_statement_account
    source_account_identifier: HDFC Bank
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: bank_statement
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: bank_statement.md
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
```


### 2.4 Account Data Binding Cards

#### account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Delhivery Logistics direct_courier_cod_settlement binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Delhivery Logistics direct courier COD settlement
    - delhivery_settlement
    - zs_observe.delhivery_settlement
    - table.zs_observe.delhivery_settlement, table.zs_observe.delhivery_invoice
    - Teaxpress Private Limited Delhivery Logistics direct courier COD settlement
    colloquial_phrases:
    - Teaxpress Private Limited Delhivery Logistics direct courier COD settlement source
    - Delhivery Logistics direct courier COD settlement runtime binding
    - delhivery_settlement for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Delhivery Logistics
      direct courier COD settlement evidence should use zs_observe.delhivery_settlement. Apply group_level_id=190
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Delhivery Logistics logistics rows should answer Teaxpress Private Limited's direct courier COD settlement
      question?
    - Which courier/account scope must be applied before using delhivery_settlement?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - direct_courier_cod_settlement
    included_concepts:
    - zs_observe.delhivery_settlement
    - direct courier COD settlement
    - Delhivery Logistics
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=190
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.delhivery.logistics
    - platform_id:platform.delhivery
    - platform_context_id:platform_context.delhivery.in
    - source_role:direct_courier_cod_settlement
    - table_id:table.zs_observe.delhivery_settlement
    - runtime_source_family:logistics
    embedding_text: 'For Teaxpress Private Limited, the Delhivery Logistics direct courier COD settlement binding
      selects zs_observe.delhivery_settlement as logistics / courier evidence. Scope: group_level_id=190. Reusable
      semantics come from logistics_integrated.md. Coverage status: active. Use this card for runtime source resolution,
      not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Delhivery Logistics
    - direct courier COD settlement
    - logistics / courier
    - zs_observe.delhivery_settlement
    - delhivery_settlement
    - direct_courier_cod_settlement
    - logistics_integrated.md
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.delhivery.logistics
    platform_id: platform.delhivery
    platform_context_id: platform_context.delhivery.in
    account_data_binding_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
    table_id: table.zs_observe.delhivery_settlement
    source_role: direct_courier_cod_settlement
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.delhivery.logistics
    table_id: table.zs_observe.delhivery_settlement
    source_role: direct_courier_cod_settlement
    source_entity: Delhivery Logistics
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '190'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.delhivery_settlement.group_level_id
      runtime_value: '190'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.delhivery_settlement, table.zs_observe.delhivery_invoice
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Delhivery Logistics direct_courier_freight_invoice binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Delhivery Logistics direct courier freight invoice
    - delhivery_invoice
    - zs_observe.delhivery_invoice
    - table.zs_observe.delhivery_settlement, table.zs_observe.delhivery_invoice
    - Teaxpress Private Limited Delhivery Logistics direct courier freight invoice
    colloquial_phrases:
    - Teaxpress Private Limited Delhivery Logistics direct courier freight invoice source
    - Delhivery Logistics direct courier freight invoice runtime binding
    - delhivery_invoice for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Delhivery Logistics
      direct courier freight invoice evidence should use zs_observe.delhivery_invoice. Apply group_level_id=190
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Delhivery Logistics logistics rows should answer Teaxpress Private Limited's direct courier freight
      invoice question?
    - Which courier/account scope must be applied before using delhivery_invoice?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - direct_courier_freight_invoice
    included_concepts:
    - zs_observe.delhivery_invoice
    - direct courier freight invoice
    - Delhivery Logistics
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=190
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.delhivery.logistics
    - platform_id:platform.delhivery
    - platform_context_id:platform_context.delhivery.in
    - source_role:direct_courier_freight_invoice
    - table_id:table.zs_observe.delhivery_invoice
    - runtime_source_family:logistics
    embedding_text: 'For Teaxpress Private Limited, the Delhivery Logistics direct courier freight invoice binding
      selects zs_observe.delhivery_invoice as logistics / courier evidence. Scope: group_level_id=190. Reusable
      semantics come from logistics_integrated.md. Coverage status: active. Use this card for runtime source resolution,
      not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Delhivery Logistics
    - direct courier freight invoice
    - logistics / courier
    - zs_observe.delhivery_invoice
    - delhivery_invoice
    - direct_courier_freight_invoice
    - logistics_integrated.md
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.delhivery.logistics
    platform_id: platform.delhivery
    platform_context_id: platform_context.delhivery.in
    account_data_binding_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
    table_id: table.zs_observe.delhivery_invoice
    source_role: direct_courier_freight_invoice
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.delhivery.logistics
    table_id: table.zs_observe.delhivery_invoice
    source_role: direct_courier_freight_invoice
    source_entity: Delhivery Logistics
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '190'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.delhivery_invoice.group_level_id
      runtime_value: '190'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.delhivery_settlement, table.zs_observe.delhivery_invoice
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited DTDC Logistics empty_courier_invoice_guardrail binding
  status: review_required
  review_status: review_required
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - DTDC Logistics empty courier invoice guardrail
    - dtdc_invoice
    - zs_observe.dtdc_invoice
    - table.zs_observe.dtdc_invoice
    - Teaxpress Private Limited DTDC Logistics empty courier invoice guardrail
    colloquial_phrases:
    - Teaxpress Private Limited DTDC Logistics empty courier invoice guardrail source
    - DTDC Logistics empty courier invoice guardrail runtime binding
    - dtdc_invoice for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's DTDC Logistics
      empty courier invoice guardrail evidence should use zs_observe.dtdc_invoice. Apply client runtime scope before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which DTDC Logistics logistics rows should answer Teaxpress Private Limited's empty courier invoice guardrail
      question?
    - Which courier/account scope must be applied before using dtdc_invoice?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - empty_courier_invoice_guardrail
    included_concepts:
    - zs_observe.dtdc_invoice
    - empty courier invoice guardrail
    - DTDC Logistics
    - courier settlement or invoice evidence
    - shipment references
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.dtdc.logistics
    - platform_id:platform.dtdc
    - platform_context_id:platform_context.dtdc.in
    - source_role:empty_courier_invoice_guardrail
    - table_id:table.zs_observe.dtdc_invoice
    - runtime_source_family:logistics
    embedding_text: 'For Teaxpress Private Limited, the DTDC Logistics empty courier invoice guardrail binding selects
      zs_observe.dtdc_invoice as logistics / courier evidence. Runtime scope must be supplied before SQL. Reusable
      semantics come from logistics_integrated.md. Coverage status: review_required. Use this card for runtime source
      resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - DTDC Logistics
    - empty courier invoice guardrail
    - logistics / courier
    - zs_observe.dtdc_invoice
    - dtdc_invoice
    - empty_courier_invoice_guardrail
    - logistics_integrated.md
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.dtdc.logistics
    platform_id: platform.dtdc
    platform_context_id: platform_context.dtdc.in
    account_data_binding_id: account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
    table_id: table.zs_observe.dtdc_invoice
    source_role: empty_courier_invoice_guardrail
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.dtdc.logistics
    table_id: table.zs_observe.dtdc_invoice
    source_role: empty_courier_invoice_guardrail
    source_entity: DTDC Logistics
    scope_keys: []
    scope_key_status: no_documented_group_level_scope_column_in_reusable_logistics_table_card
    active: false
    source_configuration_text: table.zs_observe.dtdc_invoice
    canonical_table_coverage_status: review_required
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Ekart Logistics logistics_invoice_empty binding
  status: review_required
  review_status: review_required
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Ekart Logistics empty logistics invoice guardrail
    - ekart_invoice
    - zs_observe.ekart_invoice
    - table.zs_observe.ekart_settlement, table.zs_observe.ekart_invoice
    - Teaxpress Private Limited Ekart Logistics empty logistics invoice guardrail
    colloquial_phrases:
    - Teaxpress Private Limited Ekart Logistics empty logistics invoice guardrail source
    - Ekart Logistics empty logistics invoice guardrail runtime binding
    - ekart_invoice for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Ekart Logistics
      empty logistics invoice guardrail evidence should use zs_observe.ekart_invoice. Apply client runtime scope
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Ekart Logistics logistics rows should answer Teaxpress Private Limited's empty logistics invoice guardrail
      question?
    - Which courier/account scope must be applied before using ekart_invoice?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - logistics_invoice_empty
    included_concepts:
    - zs_observe.ekart_invoice
    - empty logistics invoice guardrail
    - Ekart Logistics
    - courier settlement or invoice evidence
    - shipment references
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.ekart.logistics
    - platform_id:platform.ekart
    - platform_context_id:platform_context.ekart.in
    - source_role:logistics_invoice_empty
    - table_id:table.zs_observe.ekart_invoice
    - runtime_source_family:logistics
    embedding_text: 'For Teaxpress Private Limited, the Ekart Logistics empty logistics invoice guardrail binding
      selects zs_observe.ekart_invoice as logistics / courier evidence. Runtime scope must be supplied before SQL.
      Reusable semantics come from logistics_integrated.md. Coverage status: review_required. Use this card for
      runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Ekart Logistics
    - empty logistics invoice guardrail
    - logistics / courier
    - zs_observe.ekart_invoice
    - ekart_invoice
    - logistics_invoice_empty
    - logistics_integrated.md
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.ekart.logistics
    platform_id: platform.ekart
    platform_context_id: platform_context.ekart.in
    account_data_binding_id: account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
    table_id: table.zs_observe.ekart_invoice
    source_role: logistics_invoice_empty
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.ekart.logistics
    table_id: table.zs_observe.ekart_invoice
    source_role: logistics_invoice_empty
    source_entity: Ekart Logistics
    scope_keys: []
    scope_key_status: no_documented_group_level_scope_column_in_reusable_logistics_table_card
    active: false
    source_configuration_text: table.zs_observe.ekart_settlement, table.zs_observe.ekart_invoice
    canonical_table_coverage_status: review_required
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Ekart Logistics logistics_settlement binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Ekart Logistics logistics settlement
    - ekart_settlement
    - zs_observe.ekart_settlement
    - table.zs_observe.ekart_settlement, table.zs_observe.ekart_invoice
    - Teaxpress Private Limited Ekart Logistics logistics settlement
    colloquial_phrases:
    - Teaxpress Private Limited Ekart Logistics logistics settlement source
    - Ekart Logistics logistics settlement runtime binding
    - ekart_settlement for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Ekart Logistics
      logistics settlement evidence should use zs_observe.ekart_settlement. Apply group_level_id=190 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Ekart Logistics logistics rows should answer Teaxpress Private Limited's logistics settlement question?
    - Which courier/account scope must be applied before using ekart_settlement?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - logistics_settlement
    included_concepts:
    - zs_observe.ekart_settlement
    - logistics settlement
    - Ekart Logistics
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=190
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.ekart.logistics
    - platform_id:platform.ekart
    - platform_context_id:platform_context.ekart.in
    - source_role:logistics_settlement
    - table_id:table.zs_observe.ekart_settlement
    - runtime_source_family:logistics
    embedding_text: 'For Teaxpress Private Limited, the Ekart Logistics logistics settlement binding selects zs_observe.ekart_settlement
      as logistics / courier evidence. Scope: group_level_id=190. Reusable semantics come from logistics_integrated.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Ekart Logistics
    - logistics settlement
    - logistics / courier
    - zs_observe.ekart_settlement
    - ekart_settlement
    - logistics_settlement
    - logistics_integrated.md
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.ekart.logistics
    platform_id: platform.ekart
    platform_context_id: platform_context.ekart.in
    account_data_binding_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
    table_id: table.zs_observe.ekart_settlement
    source_role: logistics_settlement
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.ekart.logistics
    table_id: table.zs_observe.ekart_settlement
    source_role: logistics_settlement
    source_entity: Ekart Logistics
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '190'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.ekart_settlement.group_level_id
      runtime_value: '190'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.ekart_settlement, table.zs_observe.ekart_invoice
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited — India Post Via amazon_shipping_settlement_report — settlement
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon settlement
    - amazon_settlement
    - zs_observe.amazon_settlement
    - Single (shared)
    - Teaxpress Private Limited Amazon settlement
    colloquial_phrases:
    - Teaxpress Private Limited Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Amazon settlement
      evidence should use zs_observe.amazon_settlement. Apply group_id=52, group_level_id=190 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Teaxpress Private Limited?
    - Which group filters keep amazon_settlement limited to Teaxpress Private Limited?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.amazon_settlement
    - settlement
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=52
    - group_level_id=190
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Teaxpress Private Limited, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=52, group_level_id=190. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=52
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    source_path: Teaxpress Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '190'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '190'
    active: true
    source_configuration_text: Single (shared)
```

#### account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Shopify D2C OMS oms_sales binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Shopify D2C OMS OMS sales
    - shopify_oms
    - zs_observe.shopify_oms
    - Shopify D2C OMS and returns/refund events
    - Teaxpress Private Limited Shopify D2C OMS OMS sales
    colloquial_phrases:
    - Teaxpress Private Limited Shopify D2C OMS OMS sales source
    - Shopify D2C OMS OMS sales runtime binding
    - shopify_oms for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Shopify D2C
      OMS OMS sales evidence should use zs_observe.shopify_oms. Apply group_id=52, group_level_id=190 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Teaxpress Private Limited's OMS sales question?
    - Which runtime scope must be injected before using shopify_oms?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - oms_sales
    included_concepts:
    - zs_observe.shopify_oms
    - OMS sales
    - Shopify D2C OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=52
    - group_level_id=190
    - shopify_d2c_oms.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - OMS rows define order or expected-side evidence; actual payment, bank, shipment, or warehouse proof must come
      from linked packs.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:oms_sales
    - table_id:table.zs_observe.shopify_oms
    - runtime_source_family:oms
    embedding_text: 'For Teaxpress Private Limited, the Shopify D2C OMS OMS sales binding selects zs_observe.shopify_oms
      as OMS evidence. Scope: group_id=52, group_level_id=190. Reusable semantics come from shopify_d2c_oms.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Shopify D2C OMS
    - OMS sales
    - OMS
    - zs_observe.shopify_oms
    - shopify_oms
    - oms_sales
    - shopify_d2c_oms.md
    - group_id=52
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - shopify_d2c_oms.md
    source_path: Teaxpress Private Limited.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    source_entity: Shopify D2C OMS
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '52'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.shopify_oms.group_id
      runtime_value: '52'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '190'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shopify_oms.group_level_id
      runtime_value: '190'
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Shopify D2C OMS and returns/refund events
    canonical_table_coverage_status: active
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: available_shopify_pack_context
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Shopify D2C OMS returns binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Shopify D2C OMS returns
    - shopify_returns
    - zs_observe.shopify_returns
    - Shopify D2C OMS and returns/refund events
    - Teaxpress Private Limited Shopify D2C OMS returns
    colloquial_phrases:
    - Teaxpress Private Limited Shopify D2C OMS returns source
    - Shopify D2C OMS returns runtime binding
    - shopify_returns for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Shopify D2C
      OMS returns evidence should use zs_observe.shopify_returns. Apply group_id=52, group_level_id=190 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Teaxpress Private Limited's returns question?
    - Which runtime scope must be injected before using shopify_returns?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - returns
    included_concepts:
    - zs_observe.shopify_returns
    - returns
    - Shopify D2C OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=52
    - group_level_id=190
    - shopify_d2c_oms.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - OMS rows define order or expected-side evidence; actual payment, bank, shipment, or warehouse proof must come
      from linked packs.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:returns
    - table_id:table.zs_observe.shopify_returns
    - runtime_source_family:oms
    embedding_text: 'For Teaxpress Private Limited, the Shopify D2C OMS returns binding selects zs_observe.shopify_returns
      as OMS evidence. Scope: group_id=52, group_level_id=190. Reusable semantics come from shopify_d2c_oms.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Shopify D2C OMS
    - returns
    - OMS
    - zs_observe.shopify_returns
    - shopify_returns
    - shopify_d2c_oms.md
    - group_id=52
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - shopify_d2c_oms.md
    source_path: Teaxpress Private Limited.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
    domain_id: domain.shopify.refunds_returns
    table_id: table.zs_observe.shopify_returns
    source_role: returns
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
    domain_id: domain.shopify.refunds_returns
    table_id: table.zs_observe.shopify_returns
    source_role: returns
    source_entity: Shopify D2C OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Shopify D2C OMS and returns/refund events
    canonical_table_coverage_status: active
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: available_shopify_pack_context
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Unicommerce WMS invoice transaction ledger binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Unicommerce WMS WMS invoice transaction ledger
    - unicommerce
    - zs_observe.unicommerce
    - order management / marketplace sync / WMS fulfilment
    - Teaxpress Private Limited Unicommerce WMS WMS invoice transaction ledger
    colloquial_phrases:
    - Teaxpress Private Limited Unicommerce WMS WMS invoice transaction ledger source
    - Unicommerce WMS WMS invoice transaction ledger runtime binding
    - unicommerce for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Unicommerce
      WMS WMS invoice transaction ledger evidence should use zs_observe.unicommerce. Apply group_level_id=190 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in unicommerce_wms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Unicommerce WMS WMS rows should answer Teaxpress Private Limited's WMS invoice transaction ledger question?
    - Which group scope and active-row filters apply before querying unicommerce?
    - Which marketplace, logistics, or OMS binding should be joined only through a documented cross-domain profile?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - WMS
    - wms_invoice_transaction_ledger
    included_concepts:
    - zs_observe.unicommerce
    - WMS invoice transaction ledger
    - Unicommerce WMS
    - warehouse operations
    - fulfilment/return traceability
    - group_level_id=190
    - unicommerce_wms.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - WMS evidence is operational fulfilment or return evidence; do not treat it as payout, bank, or marketplace
      settlement proof.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.unicommerce_wms.wms
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - domain_id:domain.wms.unicommerce.fulfilment_operations
    - table_id:table.zs_observe.unicommerce
    - source_role:wms_invoice_transaction_ledger
    - runtime_source_family:wms
    embedding_text: 'For Teaxpress Private Limited, the Unicommerce WMS WMS invoice transaction ledger binding selects
      zs_observe.unicommerce as WMS evidence. Scope: group_level_id=190. Reusable semantics come from unicommerce_wms.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Unicommerce WMS
    - WMS invoice transaction ledger
    - WMS
    - zs_observe.unicommerce
    - unicommerce
    - wms_invoice_transaction_ledger
    - unicommerce_wms.md
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - unicommerce_wms.md
    source_path: Teaxpress Private Limited.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce
    source_role: wms_invoice_transaction_ledger
    account_data_binding_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    runtime_source_family: wms
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce
    canonical_table_id: table.zs_observe.unicommerce
    physical_table_reference: zs_observe.unicommerce
    source_role: wms_invoice_transaction_ledger
    source_role_label: invoice transaction ledger
    source_family: wms
    configured_source_description: order management / marketplace sync / WMS fulfilment
    canonical_source_pack: unicommerce_wms.md
    coverage_status: active
    active: true
    runtime_scope_status: runtime_group_level_scope_available
    runtime_scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '190'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.unicommerce.group_level_id
      runtime_value: '190'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - runtime group_level_id filter
    - metadata filter when separating sales, returns, or cancellations
    grain_from_reusable_pack: order or SKU invoice transaction row carrying sales, reverse return, or cancellation
      classification
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Unicommerce WMS order sales report shipment tracking binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Unicommerce WMS WMS shipment tracking
    - unicommerce_order_sales_report
    - zs_observe.unicommerce_order_sales_report
    - order management / marketplace sync / WMS fulfilment
    - Teaxpress Private Limited Unicommerce WMS WMS shipment tracking
    colloquial_phrases:
    - Teaxpress Private Limited Unicommerce WMS WMS shipment tracking source
    - Unicommerce WMS WMS shipment tracking runtime binding
    - unicommerce_order_sales_report for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Unicommerce
      WMS WMS shipment tracking evidence should use zs_observe.unicommerce_order_sales_report. Apply group_level_id=190
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in unicommerce_wms.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Unicommerce WMS WMS rows should answer Teaxpress Private Limited's WMS shipment tracking question?
    - Which group scope and active-row filters apply before querying unicommerce_order_sales_report?
    - Which marketplace, logistics, or OMS binding should be joined only through a documented cross-domain profile?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - WMS
    - wms_shipment_tracking
    included_concepts:
    - zs_observe.unicommerce_order_sales_report
    - WMS shipment tracking
    - Unicommerce WMS
    - warehouse operations
    - fulfilment/return traceability
    - group_level_id=190
    - unicommerce_wms.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - WMS evidence is operational fulfilment or return evidence; do not treat it as payout, bank, or marketplace
      settlement proof.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.unicommerce_wms.wms
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - domain_id:domain.wms.unicommerce.fulfilment_operations
    - table_id:table.zs_observe.unicommerce_order_sales_report
    - source_role:wms_shipment_tracking
    - runtime_source_family:wms
    embedding_text: 'For Teaxpress Private Limited, the Unicommerce WMS WMS shipment tracking binding selects zs_observe.unicommerce_order_sales_report
      as WMS evidence. Scope: group_level_id=190. Reusable semantics come from unicommerce_wms.md. Coverage status:
      active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Unicommerce WMS
    - WMS shipment tracking
    - WMS
    - zs_observe.unicommerce_order_sales_report
    - unicommerce_order_sales_report
    - wms_shipment_tracking
    - unicommerce_wms.md
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - unicommerce_wms.md
    source_path: Teaxpress Private Limited.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce_order_sales_report
    source_role: wms_shipment_tracking
    account_data_binding_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    runtime_source_family: wms
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce_order_sales_report
    canonical_table_id: table.zs_observe.unicommerce_order_sales_report
    physical_table_reference: zs_observe.unicommerce_order_sales_report
    source_role: wms_shipment_tracking
    source_role_label: order sales report shipment tracking
    source_family: wms
    configured_source_description: order management / marketplace sync / WMS fulfilment
    canonical_source_pack: unicommerce_wms.md
    coverage_status: active
    active: true
    runtime_scope_status: runtime_group_level_scope_available
    runtime_scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '190'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
      runtime_value: '190'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - runtime group_level_id filter when available
    grain_from_reusable_pack: shipment or order-SKU operational row carrying delivery status, AWB, courier method,
      MRP and package dimensions
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited XpressBees Logistics native_courier_cod_settlement_sparse binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - XpressBees Logistics native courier COD settlement
    - xpressbees_settlement
    - zs_observe.xpressbees_settlement
    - table.zs_observe.xpressbees_settlement
    - Teaxpress Private Limited XpressBees Logistics native courier COD settlement
    colloquial_phrases:
    - Teaxpress Private Limited XpressBees Logistics native courier COD settlement source
    - XpressBees Logistics native courier COD settlement runtime binding
    - xpressbees_settlement for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's XpressBees Logistics
      native courier COD settlement evidence should use zs_observe.xpressbees_settlement. Apply group_level_id=190
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which XpressBees Logistics logistics rows should answer Teaxpress Private Limited's native courier COD settlement
      question?
    - Which courier/account scope must be applied before using xpressbees_settlement?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - native_courier_cod_settlement_sparse
    included_concepts:
    - zs_observe.xpressbees_settlement
    - native courier COD settlement
    - XpressBees Logistics
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=190
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.xpressbees.logistics
    - platform_id:platform.xpressbees
    - platform_context_id:platform_context.xpressbees.in
    - source_role:native_courier_cod_settlement_sparse
    - table_id:table.zs_observe.xpressbees_settlement
    - runtime_source_family:logistics
    embedding_text: 'For Teaxpress Private Limited, the XpressBees Logistics native courier COD settlement binding
      selects zs_observe.xpressbees_settlement as logistics / courier evidence. Scope: group_level_id=190. Reusable
      semantics come from logistics_integrated.md. Coverage status: schema_partial. Use this card for runtime source
      resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - XpressBees Logistics
    - native courier COD settlement
    - logistics / courier
    - zs_observe.xpressbees_settlement
    - xpressbees_settlement
    - native_courier_cod_settlement_sparse
    - logistics_integrated.md
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.xpressbees.logistics
    platform_id: platform.xpressbees
    platform_context_id: platform_context.xpressbees.in
    account_data_binding_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
    table_id: table.zs_observe.xpressbees_settlement
    source_role: native_courier_cod_settlement_sparse
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.teaxpress_private_limited.xpressbees.logistics
    table_id: table.zs_observe.xpressbees_settlement
    source_role: native_courier_cod_settlement_sparse
    source_entity: XpressBees Logistics
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '190'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.xpressbees_settlement.group_level_id
      runtime_value: '190'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.xpressbees_settlement
    canonical_table_coverage_status: schema_partial
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Razorpay shared payment gateway reconciliation binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Razorpay settlement
    - razorpay_payin
    - zs_observe.razorpay_payin
    - razorpay_payin Teabox + Sammvaad
    - Teaxpress Private Limited Razorpay settlement
    colloquial_phrases:
    - Teaxpress Private Limited Razorpay settlement source
    - Razorpay settlement runtime binding
    - razorpay_payin for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Razorpay settlement
      evidence should use zs_observe.razorpay_payin. Apply group_id=52, group_level_id=190 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Razorpay settlement rows represent expected gateway evidence for Teaxpress Private Limited?
    - Which merchant/account filters are still needed before querying razorpay_payin?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.razorpay_payin
    - settlement
    - Razorpay
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=52
    - group_level_id=190
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.razorpay.payment_gateway
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.razorpay_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Teaxpress Private Limited, the Razorpay settlement binding selects zs_observe.razorpay_payin
      as payment gateway evidence. Scope: group_id=52, group_level_id=190. Reusable semantics come from payment_gateway.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Razorpay
    - settlement
    - payment gateway
    - zs_observe.razorpay_payin
    - razorpay_payin
    - razorpay_payin Teabox + Sammvaad
    - payment_gateway.md
    - group_id=52
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - payment_gateway.md
    source_path: Teaxpress Private Limited.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.razorpay_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.razorpay_payin
    canonical_table_id: table.zs_observe.razorpay_payin
    physical_table_reference: zs_observe.razorpay_payin
    configured_pipeline_target: razorpay_payin Teabox + Sammvaad
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: Razorpay shared payment gateway reconciliation
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '52'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '52'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '190'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '190'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    business_keys_from_reusable_pack:
    - transaction_id
    - settlement_id
    - arn
    - settlement_utr
    - utr
    amount_columns_from_reusable_pack:
    - settlement_id
    - amount
    - fee
    - tax
    - settled_amount
    - sale_type
    - cards_network
    - settlement_utr
    - settled_at
    - settled_by
    - debit
    - credit
    grain_from_reusable_pack: one row per payin/payment/refund/adjustment gateway event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited Axis Bank shared Axis Bank settlement statement binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Axis Bank bank settlement credit
    - axis_bank_settlement
    - zs_ingest.axis_bank_settlement
    - Teaxpress Private Limited Axis Bank bank settlement credit
    colloquial_phrases:
    - Teaxpress Private Limited Axis Bank bank settlement credit source
    - Axis Bank bank settlement credit runtime binding
    - axis_bank_settlement for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's Axis Bank bank
      settlement credit evidence should use zs_ingest.axis_bank_settlement. Apply group_id=52, group_level_id=190
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in bank_statement.md. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Axis Bank bank rows provide actual cash evidence for Teaxpress Private Limited?
    - Which account or group scope must be applied before reading axis_bank_settlement?
    - Which gateway, marketplace, or payout binding should be matched against this bank feed?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - bank_statement
    - bank_settlement_credit_source
    included_concepts:
    - zs_ingest.axis_bank_settlement
    - bank settlement credit
    - Axis Bank
    - actual credits/debits
    - bank references
    - cash confirmation
    - group_id=52
    - group_level_id=190
    - bank_statement.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Bank statement rows are actual cash evidence, but this binding still needs client account scope before production
      SQL.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.axis_bank.bank_statement
    - platform_id:platform.axis_bank
    - platform_context_id:platform_context.axis_bank.in
    - domain_id:domain.bank_statement.core
    - table_id:table.zs_ingest.axis_bank_settlement
    - source_role:bank_settlement_credit_source
    - runtime_source_family:bank_statement
    embedding_text: 'For Teaxpress Private Limited, the Axis Bank bank settlement credit binding selects zs_ingest.axis_bank_settlement
      as bank statement evidence. Scope: group_id=52, group_level_id=190. Reusable semantics come from bank_statement.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - Axis Bank
    - bank settlement credit
    - bank statement
    - zs_ingest.axis_bank_settlement
    - axis_bank_settlement
    - bank_settlement_credit_source
    - bank_statement.md
    - group_id=52
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - bank_statement.md
    source_path: Teaxpress Private Limited.docx plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
    platform_id: platform.axis_bank
    platform_context_id: platform_context.axis_bank.in
    domain_id: domain.bank_statement.core
    table_id: table.zs_ingest.axis_bank_settlement
    source_role: bank_settlement_credit_source
    account_data_binding_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
    runtime_source_family: bank_statement
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
    platform_id: platform.axis_bank
    platform_context_id: platform_context.axis_bank.in
    domain_id: domain.bank_statement.core
    table_id: table.zs_ingest.axis_bank_settlement
    canonical_table_id: table.zs_ingest.axis_bank_settlement
    physical_table_reference: zs_ingest.axis_bank_settlement
    configured_pipeline_target: axis_bank_settlement
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: bank_settlement_credit_source
    source_role_label: shared Axis Bank settlement statement
    source_family: bank_statement
    canonical_source_pack: bank_statement.md
    coverage_status: active
    active: true
    runtime_scope_status: bank_source_bound_but_account_number_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '52'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '52'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '190'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '190'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack:
    - account_no
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - (is_duplicated = false OR is_duplicated IS NULL)
    recommended_date_columns_from_reusable_pack:
    - created_date
    - settlement_date
    - tran_date
    business_keys_from_reusable_pack:
    - account_no
    - description
    - transaction_particulars
    - settlement_id
    - chqno
    - branch_name
    - txn_uuid
    amount_columns_from_reusable_pack:
    - settled_amount
    - amount
    - balance
    grain_from_reusable_pack: one raw bank statement transaction row or bank-provided account movement row
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
  card_type: account_data_binding
  canonical_name: Teaxpress Private Limited HDFC Bank shared HDFC Bank settlement statement binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - HDFC Bank bank settlement credit
    - hdfc_bank_settlement
    - zs_ingest.hdfc_bank_settlement
    - Teaxpress Private Limited HDFC Bank bank settlement credit
    colloquial_phrases:
    - Teaxpress Private Limited HDFC Bank bank settlement credit source
    - HDFC Bank bank settlement credit runtime binding
    - hdfc_bank_settlement for Teaxpress Private Limited
    business_meaning: This account-data binding tells the resolver that Teaxpress Private Limited's HDFC Bank bank
      settlement credit evidence should use zs_ingest.hdfc_bank_settlement. Apply group_id=52, group_level_id=190
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in bank_statement.md. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which HDFC Bank bank rows provide actual cash evidence for Teaxpress Private Limited?
    - Which account or group scope must be applied before reading hdfc_bank_settlement?
    - Which gateway, marketplace, or payout binding should be matched against this bank feed?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - bank_statement
    - bank_settlement_credit_source
    included_concepts:
    - zs_ingest.hdfc_bank_settlement
    - bank settlement credit
    - HDFC Bank
    - actual credits/debits
    - bank references
    - cash confirmation
    - group_id=52
    - group_level_id=190
    - bank_statement.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Bank statement rows are actual cash evidence, but this binding still needs client account scope before production
      SQL.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - platform_account_id:platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
    - platform_id:platform.hdfc_bank
    - platform_context_id:platform_context.hdfc_bank.in
    - domain_id:domain.bank_statement.core
    - table_id:table.zs_ingest.hdfc_bank_settlement
    - source_role:bank_settlement_credit_source
    - runtime_source_family:bank_statement
    embedding_text: 'For Teaxpress Private Limited, the HDFC Bank bank settlement credit binding selects zs_ingest.hdfc_bank_settlement
      as bank statement evidence. Scope: group_id=52, group_level_id=190. Reusable semantics come from bank_statement.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Teaxpress Private Limited
    - HDFC Bank
    - bank settlement credit
    - bank statement
    - zs_ingest.hdfc_bank_settlement
    - hdfc_bank_settlement
    - bank_settlement_credit_source
    - bank_statement.md
    - group_id=52
    - group_level_id=190
    exact_match_keys:
    - account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - bank_statement.md
    source_path: Teaxpress Private Limited.docx plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
    platform_id: platform.hdfc_bank
    platform_context_id: platform_context.hdfc_bank.in
    domain_id: domain.bank_statement.core
    table_id: table.zs_ingest.hdfc_bank_settlement
    source_role: bank_settlement_credit_source
    account_data_binding_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
    runtime_source_family: bank_statement
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    platform_account_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
    platform_id: platform.hdfc_bank
    platform_context_id: platform_context.hdfc_bank.in
    domain_id: domain.bank_statement.core
    table_id: table.zs_ingest.hdfc_bank_settlement
    canonical_table_id: table.zs_ingest.hdfc_bank_settlement
    physical_table_reference: zs_ingest.hdfc_bank_settlement
    configured_pipeline_target: hdfc_bank_settlement
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: bank_settlement_credit_source
    source_role_label: shared HDFC Bank settlement statement
    source_family: bank_statement
    canonical_source_pack: bank_statement.md
    coverage_status: active
    active: true
    runtime_scope_status: bank_source_bound_but_account_number_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '52'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '52'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '190'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '190'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack:
    - account_no
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - (is_duplicated = false OR is_duplicated IS NULL)
    recommended_date_columns_from_reusable_pack:
    - created_date
    - date
    - value_dt
    business_keys_from_reusable_pack:
    - account_no
    - narration
    - description
    - chq__ref_no_
    - settlement_id
    amount_columns_from_reusable_pack:
    - settled_amount
    - deposit_amt_
    - withdrawal_amt_
    - closing_balance
    grain_from_reusable_pack: one raw bank statement transaction row or bank-provided account movement row
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.5 Business Scope Set Cards

#### business_scope_set.teaxpress_private_limited.logistics

```yaml
canonical_card:
  canonical_id: business_scope_set.teaxpress_private_limited.logistics
  card_type: business_scope_set
  canonical_name: Teaxpress Private Limited logistics scope
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    business_scope_set_id: business_scope_set.teaxpress_private_limited.logistics
    runtime_source_family: logistics
  semantic:
    aliases:
    - Teaxpress Private Limited logistics scope
    - Teaxpress Private Limited logistics / courier scope
    - logistics / courier runtime scope set
    colloquial_phrases:
    - Teaxpress Private Limited logistics / courier scope
    - logistics / courier accounts and bindings
    - Teaxpress Private Limited logistics / courier resolver input
    business_meaning: Business scope set for Teaxpress Private Limited's logistics / courier runtime resolution.
      It groups 4 platform accounts and 6 account-data bindings so the resolver can choose client-scoped sources
      before entering reusable canonical packs.
    business_questions:
    - Which logistics / courier accounts and bindings are active for Teaxpress Private Limited?
    - Which runtime table bindings should be considered together under Teaxpress Private Limited logistics scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - logistics_courier
    - resolver_scope
    included_concepts:
    - 4 platform accounts
    - 6 account-data bindings
    - 3 deferred sources
    excluded_concepts:
    - table schema definitions
    - metric implementations
    - unbound client sources
    caveats:
    - A scope set is a resolver grouping; individual account-data-binding cards still control exact table selection
      and filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_scope_set
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - business_scope_set_id:business_scope_set.teaxpress_private_limited.logistics
    - runtime_source_family:logistics
    embedding_text: Teaxpress Private Limited logistics scope groups Teaxpress Private Limited's logistics / courier
      runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources; unresolved
      sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited logistics scope
    - logistics / courier
    - business scope set
    - 4 accounts
    - 6 bindings
    exact_match_keys:
    - business_scope_set.teaxpress_private_limited.logistics
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    scope_name: Teaxpress Private Limited logistics scope
    scope_type: logistics_courier_reconciliation
    platform_account_ids:
    - platform_account.teaxpress_private_limited.delhivery.logistics
    - platform_account.teaxpress_private_limited.dtdc.logistics
    - platform_account.teaxpress_private_limited.ekart.logistics
    - platform_account.teaxpress_private_limited.xpressbees.logistics
    platform_ids:
    - platform.delhivery
    - platform.dtdc
    - platform.ekart
    - platform.xpressbees
    platform_context_ids:
    - platform_context.delhivery.in
    - platform_context.dtdc.in
    - platform_context.ekart.in
    - platform_context.xpressbees.in
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
    - account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
    - account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
    - account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
    - account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
    - account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
    group_scope_values:
      group_id: '52'
      group_level_id: '190'
    deferred_sources:
    - label: Bluedart
      config: Settlement + Invoice
      reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: XpressBees invoice/report
      config: Settlement report + Invoice
      reason: No native XpressBees invoice or settlement-report table cards in uploaded logistics_integrated.md
    - label: India Post
      config: Via amazon_shipping_settlement_report
      reason: No India Post canonical logistics platform/table cards in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.teaxpress_private_limited.marketplace

```yaml
canonical_card:
  canonical_id: business_scope_set.teaxpress_private_limited.marketplace
  card_type: business_scope_set
  canonical_name: Teaxpress Private Limited marketplace scope
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited marketplace scope
    - marketplace runtime scope set
    colloquial_phrases:
    - Teaxpress Private Limited marketplace scope
    - marketplace accounts and bindings
    - Teaxpress Private Limited marketplace resolver input
    business_meaning: Business scope set for Teaxpress Private Limited's marketplace runtime resolution. It groups
      1 platform accounts and 1 account-data bindings so the resolver can choose client-scoped sources before entering
      reusable canonical packs.
    business_questions:
    - Which marketplace accounts and bindings are active for Teaxpress Private Limited?
    - Which runtime table bindings should be considered together under Teaxpress Private Limited marketplace scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - marketplace
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 1 account-data bindings
    - 0 deferred sources
    excluded_concepts:
    - table schema definitions
    - metric implementations
    - unbound client sources
    caveats:
    - A scope set is a resolver grouping; individual account-data-binding cards still control exact table selection
      and filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_scope_set
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - business_scope_set_id:business_scope_set.teaxpress_private_limited.marketplace
    embedding_text: Teaxpress Private Limited marketplace scope groups Teaxpress Private Limited's marketplace runtime
      accounts and table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources
      remain deferred until supported canonical packs exist.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited marketplace scope
    - marketplace
    - business scope set
    - 1 accounts
    - 1 bindings
    exact_match_keys:
    - business_scope_set.teaxpress_private_limited.marketplace
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    source_path: Teaxpress Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    business_scope_set_id: business_scope_set.teaxpress_private_limited.marketplace
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    scope_name: Teaxpress Private Limited marketplace scope
    scope_type: marketplace_only
    platform_account_ids:
    - platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
    platform_ids:
    - platform.amazon
    platform_context_ids:
    - platform_context.amazon.in
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
```

#### business_scope_set.teaxpress_private_limited.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.teaxpress_private_limited.oms
  card_type: business_scope_set
  canonical_name: Teaxpress Private Limited OMS runtime scope
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited OMS runtime scope
    - Teaxpress Private Limited OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Teaxpress Private Limited OMS scope
    - OMS accounts and bindings
    - Teaxpress Private Limited OMS resolver input
    business_meaning: Business scope set for Teaxpress Private Limited's OMS runtime resolution. It groups 1 platform
      accounts and 2 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which OMS accounts and bindings are active for Teaxpress Private Limited?
    - Which runtime table bindings should be considered together under Teaxpress Private Limited OMS runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - OMS
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - 0 deferred sources
    excluded_concepts:
    - table schema definitions
    - metric implementations
    - unbound client sources
    caveats:
    - A scope set is a resolver grouping; individual account-data-binding cards still control exact table selection
      and filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_scope_set
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - runtime_source_family:oms
    embedding_text: Teaxpress Private Limited OMS runtime scope groups Teaxpress Private Limited's OMS runtime accounts
      and table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain
      deferred until supported canonical packs exist.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.teaxpress_private_limited.oms
  evidence:
    source_documents:
    - client DOCX files
    - oms_business_kb.md
    - shopify_d2c_oms.md
    source_path: client DOCX files plus uploaded OMS canonical packs
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.teaxpress_private_limited.oms
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    binding_name: Teaxpress Private Limited OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.oms
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
      account_name: Teaxpress Private Limited Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.teaxpress_private_limited.wms

```yaml
canonical_card:
  canonical_id: business_scope_set.teaxpress_private_limited.wms
  card_type: business_scope_set
  canonical_name: Teaxpress Private Limited WMS runtime scope
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited WMS runtime scope
    - Teaxpress Private Limited WMS scope
    - WMS runtime scope set
    colloquial_phrases:
    - Teaxpress Private Limited WMS scope
    - WMS accounts and bindings
    - Teaxpress Private Limited WMS resolver input
    business_meaning: Business scope set for Teaxpress Private Limited's WMS runtime resolution. It groups 1 platform
      accounts and 2 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which WMS accounts and bindings are active for Teaxpress Private Limited?
    - Which runtime table bindings should be considered together under Teaxpress Private Limited WMS runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - WMS
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - 0 deferred sources
    excluded_concepts:
    - table schema definitions
    - metric implementations
    - unbound client sources
    caveats:
    - A scope set is a resolver grouping; individual account-data-binding cards still control exact table selection
      and filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_scope_set
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - runtime_source_family:wms
    embedding_text: Teaxpress Private Limited WMS runtime scope groups Teaxpress Private Limited's WMS runtime accounts
      and table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain
      deferred until supported canonical packs exist.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited WMS runtime scope
    - WMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.teaxpress_private_limited.wms
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - increff_wms.md
    - unicommerce_wms.md
    source_path: client DOCX plus uploaded WMS canonical packs
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    runtime_source_family: wms
    business_scope_set_id: business_scope_set.teaxpress_private_limited.wms
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    binding_name: Teaxpress Private Limited WMS runtime scope
    binding_type: wms_source_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.wms
    platform_account_ids:
    - platform_account.teaxpress_private_limited.unicommerce_wms.wms
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    - account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    included_platform_ids:
    - platform.unicommerce
    included_platform_context_ids:
    - platform_context.unicommerce.in_wms
    source_flow_paths:
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
      platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
      source_role: wms_invoice_transaction_ledger
      table_id: table.zs_observe.unicommerce
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
      platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
      source_role: wms_shipment_tracking
      table_id: table.zs_observe.unicommerce_order_sales_report
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.teaxpress_private_limited.payment_gateway

```yaml
canonical_card:
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  canonical_id: business_scope_set.teaxpress_private_limited.payment_gateway
  card_type: business_scope_set
  canonical_name: Teaxpress Private Limited payment gateway runtime scope
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited payment gateway runtime scope
    - Teaxpress Private Limited payment gateway scope
    - payment gateway runtime scope set
    colloquial_phrases:
    - Teaxpress Private Limited payment gateway scope
    - payment gateway accounts and bindings
    - Teaxpress Private Limited payment gateway resolver input
    business_meaning: Business scope set for Teaxpress Private Limited's payment gateway runtime resolution. It
      groups 1 platform accounts and 1 account-data bindings so the resolver can choose client-scoped sources before
      entering reusable canonical packs.
    business_questions:
    - Which payment gateway accounts and bindings are active for Teaxpress Private Limited?
    - Which runtime table bindings should be considered together under Teaxpress Private Limited payment gateway
      runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - payment_gateway
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 1 account-data bindings
    - 0 deferred sources
    excluded_concepts:
    - table schema definitions
    - metric implementations
    - unbound client sources
    caveats:
    - A scope set is a resolver grouping; individual account-data-binding cards still control exact table selection
      and filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_scope_set
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - runtime_source_family:payment_gateway
    embedding_text: Teaxpress Private Limited payment gateway runtime scope groups Teaxpress Private Limited's payment
      gateway runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited payment gateway runtime scope
    - payment gateway
    - business scope set
    - 1 accounts
    - 1 bindings
    exact_match_keys:
    - business_scope_set.teaxpress_private_limited.payment_gateway
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    runtime_source_family: payment_gateway
    business_scope_set_id: business_scope_set.teaxpress_private_limited.payment_gateway
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    binding_name: Teaxpress Private Limited payment gateway runtime scope
    binding_type: payment_gateway_source_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.payment_gateway
    platform_account_ids:
    - platform_account.teaxpress_private_limited.razorpay.payment_gateway
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
    included_platform_ids:
    - platform.razorpay
    included_platform_context_ids:
    - platform_context.razorpay.in
    source_flow_paths:
    - platform_account_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.razorpay_payin
      source_role: settlement
      configured_pipeline_target: razorpay_payin Teabox + Sammvaad
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### business_scope_set.teaxpress_private_limited.bank_statement

```yaml
canonical_card:
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  canonical_id: business_scope_set.teaxpress_private_limited.bank_statement
  card_type: business_scope_set
  canonical_name: Teaxpress Private Limited bank statement runtime scope
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited bank statement runtime scope
    - Teaxpress Private Limited bank statement scope
    - bank statement runtime scope set
    colloquial_phrases:
    - Teaxpress Private Limited bank statement scope
    - bank statement accounts and bindings
    - Teaxpress Private Limited bank statement resolver input
    business_meaning: Business scope set for Teaxpress Private Limited's bank statement runtime resolution. It groups
      2 platform accounts and 2 account-data bindings so the resolver can choose client-scoped sources before entering
      reusable canonical packs.
    business_questions:
    - Which bank statement accounts and bindings are active for Teaxpress Private Limited?
    - Which runtime table bindings should be considered together under Teaxpress Private Limited bank statement
      runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - bank_statement
    - resolver_scope
    included_concepts:
    - 2 platform accounts
    - 2 account-data bindings
    - 0 deferred sources
    excluded_concepts:
    - table schema definitions
    - metric implementations
    - unbound client sources
    caveats:
    - A scope set is a resolver grouping; individual account-data-binding cards still control exact table selection
      and filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_scope_set
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - runtime_source_family:bank_statement
    embedding_text: Teaxpress Private Limited bank statement runtime scope groups Teaxpress Private Limited's bank
      statement runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited bank statement runtime scope
    - bank statement
    - business scope set
    - 2 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.teaxpress_private_limited.bank_statement
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - bank_statement.md
    source_path: client DOCX plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    runtime_source_family: bank_statement
    business_scope_set_id: business_scope_set.teaxpress_private_limited.bank_statement
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    binding_name: Teaxpress Private Limited bank statement runtime scope
    binding_type: bank_statement_source_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.bank_statement
    platform_account_ids:
    - platform_account.teaxpress_private_limited.axis_bank.bank_statement
    - platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
    - account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
    included_platform_ids:
    - platform.axis_bank
    - platform.hdfc_bank
    included_platform_context_ids:
    - platform_context.axis_bank.in
    - platform_context.hdfc_bank.in
    source_flow_paths:
    - platform_account_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
      account_data_binding_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
      platform_id: platform.axis_bank
      platform_context_id: platform_context.axis_bank.in
      domain_id: domain.bank_statement.core
      table_id: table.zs_ingest.axis_bank_settlement
      source_role: bank_settlement_credit_source
      configured_pipeline_target: axis_bank_settlement
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
      account_data_binding_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
      platform_id: platform.hdfc_bank
      platform_context_id: platform_context.hdfc_bank.in
      domain_id: domain.bank_statement.core
      table_id: table.zs_ingest.hdfc_bank_settlement
      source_role: bank_settlement_credit_source
      configured_pipeline_target: hdfc_bank_settlement
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.6 Business Flow Binding Cards

#### business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Teaxpress Private Limited logistics runtime resolution
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - logistics_integrated.md
    source_path: Teaxpress Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
    runtime_source_family: logistics
    business_scope_set_id: business_scope_set.teaxpress_private_limited.logistics
  semantic:
    aliases:
    - Teaxpress Private Limited logistics runtime resolution
    - Teaxpress Private Limited logistics / courier flow
    - logistics / courier runtime resolution flow
    colloquial_phrases:
    - Teaxpress Private Limited logistics / courier resolution flow
    - logistics / courier source routing
    - Teaxpress Private Limited runtime traversal plan
    business_meaning: Business flow binding for Teaxpress Private Limited's logistics / courier source resolution.
      It connects the scope set to 4 platform accounts and 6 account-data bindings so questions enter the right
      client-scoped evidence before reusable semantics run.
    business_questions:
    - Which logistics / courier bindings should be traversed for Teaxpress Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - logistics_courier
    - runtime_traversal
    included_concepts:
    - 4 platform accounts
    - 6 account-data bindings
    - documented source flow paths
    excluded_concepts:
    - SQL formulas
    - domain metrics
    - unconfigured source inference
    caveats:
    - Use this flow after resolving tenant and group scope; unsupported sources must stay deferred until their canonical
      packs are available.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_flow_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - business_flow_binding_id:business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
    - runtime_source_family:logistics
    embedding_text: Teaxpress Private Limited logistics runtime resolution is Teaxpress Private Limited's logistics
      / courier runtime traversal binding. It connects the business scope set to account and table bindings so retrieval
      selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited logistics runtime resolution
    - logistics / courier
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    binding_name: Teaxpress Private Limited logistics runtime resolution
    binding_type: logistics_source_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.logistics
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
    - account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
    - account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
    - account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
    - account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
    - account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
    participating_accounts:
    - platform_account_id: platform_account.teaxpress_private_limited.delhivery.logistics
      account_name: Teaxpress Private Limited Delhivery Logistics account
    - platform_account_id: platform_account.teaxpress_private_limited.dtdc.logistics
      account_name: Teaxpress Private Limited DTDC Logistics account
    - platform_account_id: platform_account.teaxpress_private_limited.ekart.logistics
      account_name: Teaxpress Private Limited Ekart Logistics account
    - platform_account_id: platform_account.teaxpress_private_limited.xpressbees.logistics
      account_name: Teaxpress Private Limited XpressBees Logistics account
    money_flow_paths:
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
      source_role: direct_courier_cod_settlement
      table_id: table.zs_observe.delhivery_settlement
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
      source_role: direct_courier_freight_invoice
      table_id: table.zs_observe.delhivery_invoice
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
      source_role: empty_courier_invoice_guardrail
      table_id: table.zs_observe.dtdc_invoice
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
      source_role: logistics_invoice_empty
      table_id: table.zs_observe.ekart_invoice
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
      source_role: logistics_settlement
      table_id: table.zs_observe.ekart_settlement
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
      source_role: native_courier_cod_settlement_sparse
      table_id: table.zs_observe.xpressbees_settlement
    deferred_sources:
    - label: Bluedart
      config: Settlement + Invoice
      reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: XpressBees invoice/report
      config: Settlement report + Invoice
      reason: No native XpressBees invoice or settlement-report table cards in uploaded logistics_integrated.md
    - label: India Post
      config: Via amazon_shipping_settlement_report
      reason: No India Post canonical logistics platform/table cards in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Teaxpress Private Limited marketplace runtime resolution
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited marketplace runtime resolution
    - Teaxpress Private Limited marketplace flow
    - marketplace runtime resolution flow
    colloquial_phrases:
    - Teaxpress Private Limited marketplace resolution flow
    - marketplace source routing
    - Teaxpress Private Limited runtime traversal plan
    business_meaning: Business flow binding for Teaxpress Private Limited's marketplace source resolution. It connects
      the scope set to 1 platform accounts and 1 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which marketplace bindings should be traversed for Teaxpress Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - marketplace
    - runtime_traversal
    included_concepts:
    - 1 platform accounts
    - 1 account-data bindings
    - documented source flow paths
    excluded_concepts:
    - SQL formulas
    - domain metrics
    - unconfigured source inference
    caveats:
    - Use this flow after resolving tenant and group scope; unsupported sources must stay deferred until their canonical
      packs are available.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_flow_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - business_flow_binding_id:business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
    embedding_text: Teaxpress Private Limited marketplace runtime resolution is Teaxpress Private Limited's marketplace
      runtime traversal binding. It connects the business scope set to account and table bindings so retrieval selects
      client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited marketplace runtime resolution
    - marketplace
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    source_path: Teaxpress Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.marketplace
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    binding_name: Teaxpress Private Limited marketplace runtime resolution
    binding_type: marketplace_source_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.marketplace
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
    participating_accounts:
    - platform_account_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
      account_name: India Post Via amazon_shipping_settlement_report
    money_flow_paths:
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
```

#### business_flow_binding.teaxpress_private_limited.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Teaxpress Private Limited OMS runtime resolution flow
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited OMS runtime resolution flow
    - Teaxpress Private Limited OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Teaxpress Private Limited OMS resolution flow
    - OMS source routing
    - Teaxpress Private Limited runtime traversal plan
    business_meaning: Business flow binding for Teaxpress Private Limited's OMS source resolution. It connects the
      scope set to 1 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Teaxpress Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - OMS
    - runtime_traversal
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - documented source flow paths
    excluded_concepts:
    - SQL formulas
    - domain metrics
    - unconfigured source inference
    caveats:
    - Use this flow after resolving tenant and group scope; unsupported sources must stay deferred until their canonical
      packs are available.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_flow_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - runtime_source_family:oms
    embedding_text: Teaxpress Private Limited OMS runtime resolution flow is Teaxpress Private Limited's OMS runtime
      traversal binding. It connects the business scope set to account and table bindings so retrieval selects client
      evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  evidence:
    source_documents:
    - client DOCX files
    - oms_business_kb.md
    - shopify_d2c_oms.md
    source_path: client DOCX files plus uploaded OMS canonical packs
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    binding_name: Teaxpress Private Limited OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.oms
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
      account_name: Teaxpress Private Limited Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.teaxpress_private_limited.wms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Teaxpress Private Limited WMS runtime resolution
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited WMS runtime resolution
    - Teaxpress Private Limited WMS flow
    - WMS runtime resolution flow
    colloquial_phrases:
    - Teaxpress Private Limited WMS resolution flow
    - WMS source routing
    - Teaxpress Private Limited runtime traversal plan
    business_meaning: Business flow binding for Teaxpress Private Limited's WMS source resolution. It connects the
      scope set to 1 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which WMS bindings should be traversed for Teaxpress Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - WMS
    - runtime_traversal
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - documented source flow paths
    excluded_concepts:
    - SQL formulas
    - domain metrics
    - unconfigured source inference
    caveats:
    - Use this flow after resolving tenant and group scope; unsupported sources must stay deferred until their canonical
      packs are available.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_flow_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - runtime_source_family:wms
    embedding_text: Teaxpress Private Limited WMS runtime resolution is Teaxpress Private Limited's WMS runtime
      traversal binding. It connects the business scope set to account and table bindings so retrieval selects client
      evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited WMS runtime resolution
    - WMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - increff_wms.md
    - unicommerce_wms.md
    source_path: client DOCX plus uploaded WMS canonical packs
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_flow
    evidence_ids:
    - client_runtime.wms_flow
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    runtime_source_family: wms
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.wms
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.wms
    flow_name: Teaxpress Private Limited WMS runtime resolution
    flow_type: wms_source_resolution
    platform_account_ids:
    - platform_account.teaxpress_private_limited.unicommerce_wms.wms
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    - account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    source_flow_paths:
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
      platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
      source_role: wms_invoice_transaction_ledger
      table_id: table.zs_observe.unicommerce
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
      platform_account_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
      source_role: wms_shipment_tracking
      table_id: table.zs_observe.unicommerce_order_sales_report
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution

```yaml
canonical_card:
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  canonical_id: business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Teaxpress Private Limited payment gateway runtime resolution
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited payment gateway runtime resolution
    - Teaxpress Private Limited payment gateway flow
    - payment gateway runtime resolution flow
    colloquial_phrases:
    - Teaxpress Private Limited payment gateway resolution flow
    - payment gateway source routing
    - Teaxpress Private Limited runtime traversal plan
    business_meaning: Business flow binding for Teaxpress Private Limited's payment gateway source resolution. It
      connects the scope set to 1 platform accounts and 1 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which payment gateway bindings should be traversed for Teaxpress Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - payment_gateway
    - runtime_traversal
    included_concepts:
    - 1 platform accounts
    - 1 account-data bindings
    - documented source flow paths
    excluded_concepts:
    - SQL formulas
    - domain metrics
    - unconfigured source inference
    caveats:
    - Use this flow after resolving tenant and group scope; unsupported sources must stay deferred until their canonical
      packs are available.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_flow_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - runtime_source_family:payment_gateway
    embedding_text: Teaxpress Private Limited payment gateway runtime resolution is Teaxpress Private Limited's
      payment gateway runtime traversal binding. It connects the business scope set to account and table bindings
      so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited payment gateway runtime resolution
    - payment gateway
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_flow
    evidence_ids:
    - client_runtime.payment_gateway_flow
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    runtime_source_family: payment_gateway
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.payment_gateway
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.payment_gateway
    flow_name: Teaxpress Private Limited payment gateway runtime resolution
    flow_type: payment_gateway_source_resolution
    platform_account_ids:
    - platform_account.teaxpress_private_limited.razorpay.payment_gateway
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
    source_flow_paths:
    - platform_account_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.razorpay_payin
      source_role: settlement
      configured_pipeline_target: razorpay_payin Teabox + Sammvaad
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution

```yaml
canonical_card:
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  canonical_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Teaxpress Private Limited bank statement runtime resolution
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Teaxpress Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Teaxpress Private Limited bank statement runtime resolution
    - Teaxpress Private Limited bank statement flow
    - bank statement runtime resolution flow
    colloquial_phrases:
    - Teaxpress Private Limited bank statement resolution flow
    - bank statement source routing
    - Teaxpress Private Limited runtime traversal plan
    business_meaning: Business flow binding for Teaxpress Private Limited's bank statement source resolution. It
      connects the scope set to 2 platform accounts and 2 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which bank statement bindings should be traversed for Teaxpress Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - bank_statement
    - runtime_traversal
    included_concepts:
    - 2 platform accounts
    - 2 account-data bindings
    - documented source flow paths
    excluded_concepts:
    - SQL formulas
    - domain metrics
    - unconfigured source inference
    caveats:
    - Use this flow after resolving tenant and group scope; unsupported sources must stay deferred until their canonical
      packs are available.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_flow_binding
    - domain_family:client_runtime
    - tenant_id:tenant.teaxpress_private_limited
    - group_id:group.teaxpress_private_limited.g52.gl190
    - runtime_source_family:bank_statement
    embedding_text: Teaxpress Private Limited bank statement runtime resolution is Teaxpress Private Limited's bank
      statement runtime traversal binding. It connects the business scope set to account and table bindings so retrieval
      selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Teaxpress Private Limited
    - Teaxpress Private Limited bank statement runtime resolution
    - bank statement
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  evidence:
    source_documents:
    - Teaxpress Private Limited.docx
    - bank_statement.md
    source_path: client DOCX plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_flow
    evidence_ids:
    - client_runtime.bank_statement_flow
    source_line: null
  traversal:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    runtime_source_family: bank_statement
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.bank_statement
  fields:
    tenant_id: tenant.teaxpress_private_limited
    group_id: group.teaxpress_private_limited.g52.gl190
    business_flow_binding_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
    business_scope_set_id: business_scope_set.teaxpress_private_limited.bank_statement
    flow_name: Teaxpress Private Limited bank statement runtime resolution
    flow_type: bank_statement_source_resolution
    platform_account_ids:
    - platform_account.teaxpress_private_limited.axis_bank.bank_statement
    - platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
    account_data_binding_ids:
    - account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
    - account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
    source_flow_paths:
    - platform_account_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
      account_data_binding_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
      platform_id: platform.axis_bank
      platform_context_id: platform_context.axis_bank.in
      domain_id: domain.bank_statement.core
      table_id: table.zs_ingest.axis_bank_settlement
      source_role: bank_settlement_credit_source
      configured_pipeline_target: axis_bank_settlement
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
      account_data_binding_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
      platform_id: platform.hdfc_bank
      platform_context_id: platform_context.hdfc_bank.in
      domain_id: domain.bank_statement.core
      table_id: table.zs_ingest.hdfc_bank_settlement
      source_role: bank_settlement_credit_source
      configured_pipeline_target: hdfc_bank_settlement
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_applies_scope_column.column_zs_observe_delhivery_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_applies_scope_column.column_zs_observe_delhivery_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  target_card_id: column.zs_observe.delhivery_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_applies_scope_column.column_zs_observe_delhivery_invoice_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_applies_scope_column.column_zs_observe_delhivery_invoice_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  target_card_id: column.zs_observe.delhivery_invoice.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement.account_data_binding_applies_scope_column.column_zs_observe_ekart_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement.account_data_binding_applies_scope_column.column_zs_observe_ekart_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
  target_card_id: column.zs_observe.ekart_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: column.zs_observe.unicommerce.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '190'
```

#### edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_order_sales_report_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_order_sales_report_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '190'
```

#### edge.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_applies_scope_column.column_zs_observe_xpressbees_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_applies_scope_column.column_zs_observe_xpressbees_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  target_card_id: column.zs_observe.xpressbees_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  target_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  target_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_dtdc_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  target_card_id: platform_account.teaxpress_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_ekart_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  target_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_ekart_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
  target_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_xpressbees_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_xpressbees_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  target_card_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_binds_to_table.table_zs_observe_delhivery_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_binds_to_table.table_zs_observe_delhivery_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  target_card_id: table.zs_observe.delhivery_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_binds_to_table.table_zs_observe_delhivery_invoice

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_binds_to_table.table_zs_observe_delhivery_invoice
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  target_card_id: table.zs_observe.delhivery_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice.account_data_binding_binds_to_table.table_zs_observe_dtdc_invoice

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice.account_data_binding_binds_to_table.table_zs_observe_dtdc_invoice
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  target_card_id: table.zs_observe.dtdc_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice.account_data_binding_binds_to_table.table_zs_observe_ekart_invoice

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice.account_data_binding_binds_to_table.table_zs_observe_ekart_invoice
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  target_card_id: table.zs_observe.ekart_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement.account_data_binding_binds_to_table.table_zs_observe_ekart_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement.account_data_binding_binds_to_table.table_zs_observe_ekart_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
  target_card_id: table.zs_observe.ekart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: table.zs_observe.shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: table.zs_observe.shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_binds_to_table.table_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_binds_to_table.table_zs_observe_unicommerce
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: table.zs_observe.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_binds_to_table.table_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_binds_to_table.table_zs_observe_unicommerce_order_sales_report
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: table.zs_observe.unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_binds_to_table.table_zs_observe_xpressbees_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_binds_to_table.table_zs_observe_xpressbees_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  target_card_id: table.zs_observe.xpressbees_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_dtdc_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_ekart_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_xpressbees_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_xpressbees_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  target_card_id: business_scope_set.teaxpress_private_limited.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
  target_card_id: business_scope_set.teaxpress_private_limited.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  target_card_id: business_scope_set.teaxpress_private_limited.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
  target_card_id: business_scope_set.teaxpress_private_limited.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.teaxpress_private_limited.marketplace
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.teaxpress_private_limited.oms
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.teaxpress_private_limited.wms
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.marketplace
  target_card_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.oms
  target_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.oms
  target_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.wms
  target_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.wms
  target_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform.platform_delhivery

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform.platform_delhivery
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform.delhivery
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform.platform_dtdc

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform.platform_dtdc
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform.dtdc
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform.platform_ekart

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform.platform_ekart
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform.ekart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform.platform_xpressbees

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform.platform_xpressbees
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform.xpressbees
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_includes_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_includes_platform.platform_amazon
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_platform.platform_shopify
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_platform.platform_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_platform.platform_unicommerce
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.wms
  target_card_id: platform.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_dtdc_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform_account.teaxpress_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_ekart_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_xpressbees_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_xpressbees_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.marketplace
  target_card_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.oms
  target_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.wms
  target_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_delhivery_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_delhivery_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform_context.delhivery.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_dtdc_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_dtdc_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform_context.dtdc.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_ekart_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_ekart_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform_context.ekart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_xpressbees_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_xpressbees_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.logistics
  target_card_id: platform_context.xpressbees.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_platform_context.platform_context_unicommerce_in_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_wms.business_scope_set_includes_platform_context.platform_context_unicommerce_in_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.wms
  target_card_id: platform_context.unicommerce.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_teaxpress_private_limited_g52_gl190.group_belongs_to_tenant.tenant_teaxpress_private_limited

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_belongs_to_tenant.tenant_teaxpress_private_limited
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: tenant.teaxpress_private_limited
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_logistics_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_flow_binding.teaxpress_private_limited.logistics_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_marketplace_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_flow_binding.teaxpress_private_limited.marketplace_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_flow_binding.teaxpress_private_limited.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_wms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_flow_binding.teaxpress_private_limited.wms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_logistics

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_logistics
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_scope_set.teaxpress_private_limited.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_marketplace
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_scope_set.teaxpress_private_limited.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_oms

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_scope_set.teaxpress_private_limited.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_wms

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_wms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_scope_set.teaxpress_private_limited.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_delhivery_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_dtdc_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_ekart_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_shopify_d2c_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_unicommerce_wms_wms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_xpressbees_logistics

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_xpressbees_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_dtdc_logistics.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_dtdc_logistics.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.dtdc.logistics
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_teaxpress_private_limited_xpressbees_logistics.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_xpressbees_logistics.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_dtdc_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_dtdc_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.dtdc.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_ekart_logistics_settlement_zs_observe_ekart_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.ekart.logistics_settlement.zs_observe_ekart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  target_card_id: account_data_binding.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  target_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  target_card_id: account_data_binding.teaxpress_private_limited.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  target_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  target_card_id: account_data_binding.teaxpress_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_teaxpress_private_limited_xpressbees_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_xpressbees_logistics.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  target_card_id: account_data_binding.teaxpress_private_limited.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_uses_platform.platform_delhivery

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_uses_platform.platform_delhivery
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  target_card_id: platform.delhivery
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_dtdc_logistics.platform_account_uses_platform.platform_dtdc

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_dtdc_logistics.platform_account_uses_platform.platform_dtdc
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.dtdc.logistics
  target_card_id: platform.dtdc
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_uses_platform.platform_ekart

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_uses_platform.platform_ekart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  target_card_id: platform.ekart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_uses_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_uses_platform.platform_shopify
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_uses_platform.platform_unicommerce

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_uses_platform.platform_unicommerce
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  target_card_id: platform.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_teaxpress_private_limited_xpressbees_logistics.platform_account_uses_platform.platform_xpressbees

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_xpressbees_logistics.platform_account_uses_platform.platform_xpressbees
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  target_card_id: platform.xpressbees
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_uses_platform_context.platform_context_delhivery_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_delhivery_logistics.platform_account_uses_platform_context.platform_context_delhivery_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.delhivery.logistics
  target_card_id: platform_context.delhivery.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_dtdc_logistics.platform_account_uses_platform_context.platform_context_dtdc_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_dtdc_logistics.platform_account_uses_platform_context.platform_context_dtdc_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.dtdc.logistics
  target_card_id: platform_context.dtdc.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_uses_platform_context.platform_context_ekart_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_ekart_logistics.platform_account_uses_platform_context.platform_context_ekart_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.ekart.logistics
  target_card_id: platform_context.ekart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace.platform_account_uses_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_india_post_via_amazon_shipping_settlement_report_marketplace.platform_account_uses_platform_context.platform_context_amazon_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.india_post_via_amazon_shipping_settlement_report.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.shopify_d2c.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_uses_platform_context.platform_context_unicommerce_in_wms

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_unicommerce_wms_wms.platform_account_uses_platform_context.platform_context_unicommerce_in_wms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.unicommerce_wms.wms
  target_card_id: platform_context.unicommerce.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_teaxpress_private_limited_xpressbees_logistics.platform_account_uses_platform_context.platform_context_xpressbees_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_xpressbees_logistics.platform_account_uses_platform_context.platform_context_xpressbees_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.xpressbees.logistics
  target_card_id: platform_context.xpressbees.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### TENANT_HAS_GROUP

#### edge.tenant_teaxpress_private_limited.tenant_has_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.tenant_teaxpress_private_limited.tenant_has_group.group_teaxpress_private_limited_g52_gl190
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.teaxpress_private_limited
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```


<!-- Added bank/payment runtime edges -->

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_axis_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_axis_bank_bank_statement
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
  target_card_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
  target_card_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_belongs_to_platform_account.platform_account_teaxpress_private_limited_razorpay_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  target_card_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement.account_data_binding_binds_to_table.table_zs_ingest_axis_bank_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement.account_data_binding_binds_to_table.table_zs_ingest_axis_bank_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
  target_card_id: table.zs_ingest.axis_bank_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement.account_data_binding_binds_to_table.table_zs_ingest_hdfc_bank_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement.account_data_binding_binds_to_table.table_zs_ingest_hdfc_bank_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
  target_card_id: table.zs_ingest.hdfc_bank_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_binds_to_table.table_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_binds_to_table.table_zs_observe_razorpay_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  target_card_id: table.zs_observe.razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_axis_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_axis_bank_bank_statement
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_teaxpress_private_limited_razorpay_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
  target_card_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_bank_statement
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  target_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_teaxpress_private_limited_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
  target_card_id: business_scope_set.teaxpress_private_limited.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.teaxpress_private_limited.payment_gateway
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.teaxpress_private_limited.payment_gateway
  target_card_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform.platform_axis_bank

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform.platform_axis_bank
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: platform.axis_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform.platform_hdfc_bank

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform.platform_hdfc_bank
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: platform.hdfc_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_includes_platform.platform_razorpay

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_includes_platform.platform_razorpay
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.teaxpress_private_limited.payment_gateway
  target_card_id: platform.razorpay
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_axis_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_axis_bank_bank_statement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_includes_platform_account.platform_account_teaxpress_private_limited_razorpay_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.teaxpress_private_limited.payment_gateway
  target_card_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform_context.platform_context_axis_bank_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform_context.platform_context_axis_bank_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: platform_context.axis_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform_context.platform_context_hdfc_bank_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_bank_statement.business_scope_set_includes_platform_context.platform_context_hdfc_bank_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  target_card_id: platform_context.hdfc_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_includes_platform_context.platform_context_razorpay_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_teaxpress_private_limited_payment_gateway.business_scope_set_includes_platform_context.platform_context_razorpay_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.teaxpress_private_limited.payment_gateway
  target_card_id: platform_context.razorpay.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_bank_statement_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_flow_binding.teaxpress_private_limited.bank_statement_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_flow_binding.business_flow_binding_teaxpress_private_limited_payment_gateway_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_flow_binding.teaxpress_private_limited.payment_gateway_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_bank_statement

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_bank_statement
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_scope_set.teaxpress_private_limited.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_business_scope_set.business_scope_set_teaxpress_private_limited_payment_gateway
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: business_scope_set.teaxpress_private_limited.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_axis_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_axis_bank_bank_statement
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_teaxpress_private_limited_g52_gl190.group_has_platform_account.platform_account_teaxpress_private_limited_razorpay_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.teaxpress_private_limited.g52.gl190
  target_card_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_teaxpress_private_limited_axis_bank_bank_statement.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_axis_bank_bank_statement.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_teaxpress_private_limited_razorpay_payment_gateway.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_razorpay_payment_gateway.platform_account_belongs_to_group.group_teaxpress_private_limited_g52_gl190
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  target_card_id: group.teaxpress_private_limited.g52.gl190
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_teaxpress_private_limited_axis_bank_bank_statement.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_axis_bank_bank_statement.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_axis_bank_bank_settlement_credit_source_zs_ingest_axis_bank_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  target_card_id: account_data_binding.teaxpress_private_limited.axis_bank.bank_settlement_credit_source.zs_ingest_axis_bank_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_hdfc_bank_bank_settlement_credit_source_zs_ingest_hdfc_bank_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  target_card_id: account_data_binding.teaxpress_private_limited.hdfc_bank.bank_settlement_credit_source.zs_ingest_hdfc_bank_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_teaxpress_private_limited_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_teaxpress_private_limited_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  target_card_id: account_data_binding.teaxpress_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_teaxpress_private_limited_axis_bank_bank_statement.platform_account_uses_platform.platform_axis_bank

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_axis_bank_bank_statement.platform_account_uses_platform.platform_axis_bank
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  target_card_id: platform.axis_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement.platform_account_uses_platform.platform_hdfc_bank

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement.platform_account_uses_platform.platform_hdfc_bank
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  target_card_id: platform.hdfc_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_teaxpress_private_limited_razorpay_payment_gateway.platform_account_uses_platform.platform_razorpay

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_razorpay_payment_gateway.platform_account_uses_platform.platform_razorpay
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  target_card_id: platform.razorpay
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_teaxpress_private_limited_axis_bank_bank_statement.platform_account_uses_platform_context.platform_context_axis_bank_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_axis_bank_bank_statement.platform_account_uses_platform_context.platform_context_axis_bank_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.axis_bank.bank_statement
  target_card_id: platform_context.axis_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement.platform_account_uses_platform_context.platform_context_hdfc_bank_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_hdfc_bank_bank_statement.platform_account_uses_platform_context.platform_context_hdfc_bank_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.hdfc_bank.bank_statement
  target_card_id: platform_context.hdfc_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_teaxpress_private_limited_razorpay_payment_gateway.platform_account_uses_platform_context.platform_context_razorpay_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_teaxpress_private_limited_razorpay_payment_gateway.platform_account_uses_platform_context.platform_context_razorpay_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.teaxpress_private_limited.razorpay.payment_gateway
  target_card_id: platform_context.razorpay.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```
