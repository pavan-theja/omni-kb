# Bear House Clothing Private Limited — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `bear_house_clothing_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Bluedart
  config: Settlement + Invoice (PP Teabox variant)
  reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: GoSwift
  config: Settlement + Invoice
  reason: No GoSwift canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 6
  account_data_binding: 19
  business_scope_set: 4
  business_flow_binding: 4
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 36
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 19
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 19
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 4
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 19
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 6
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 4
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 4
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 19
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 6
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 6
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 6
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 4
  GROUP_HAS_BUSINESS_SCOPE_SET: 4
  GROUP_HAS_PLATFORM_ACCOUNT: 6
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 6
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 19
  PLATFORM_ACCOUNT_USES_PLATFORM: 6
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 6
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
  added_runtime_cards: 0
  added_runtime_edges: 0
  supported_payment_bindings: 0
  supported_bank_bindings: 0
  deferred_financial_sources_added_or_updated: 0
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.bear_house_clothing_private_limited

```yaml
canonical_card:
  canonical_id: tenant.bear_house_clothing_private_limited
  card_type: tenant
  canonical_name: Bear House Clothing Private Limited
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bear House Clothing Private Limited
    - bear_house_clothing_private_limited
    - Bear House Clothing Private Limited runtime tenant
    colloquial_phrases:
    - Bear House Clothing Private Limited client runtime
    - Bear House Clothing Private Limited source configuration
    - Bear House Clothing Private Limited scoped reconciliation setup
    business_meaning: Runtime tenant identity for Bear House Clothing Private Limited. It anchors the client's marketplace,
      logistics, OMS, WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from
      reusable domain semantics.
    business_questions:
    - Which source families and configured accounts belong to Bear House Clothing Private Limited?
    - Which group and account bindings should constrain Bear House Clothing Private Limited's SQL handoff?
    - After Bear House Clothing Private Limited's runtime scope is resolved, which domain layer should receive the
      query next?
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    embedding_text: Bear House Clothing Private Limited is the runtime tenant root for the client's marketplace,
      logistics, OMS, WMS, payment-gateway, and bank-statement configuration. Use it to reach group, platform-account,
      and account-data-binding nodes before invoking reusable canonical packs.
    search_keywords:
    - Bear House Clothing Private Limited
    - bear_house_clothing_private_limited
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.bear_house_clothing_private_limited
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
  fields:
    tenant_slug: bear_house_clothing_private_limited
    tenant_name: Bear House Clothing Private Limited
    legal_name: Bear House Clothing Private Limited
    active: true
```

### 2.2 Group Cards

#### group.bear_house_clothing_private_limited.g116.gl330

```yaml
canonical_card:
  canonical_id: group.bear_house_clothing_private_limited.g116.gl330
  card_type: group
  canonical_name: Bear House Clothing Private Limited group 116/330
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bear House
    - Bear House Clothing Private Limited group 116/330
    - group_id 116
    - group_level_id 330
    colloquial_phrases:
    - Bear House Clothing Private Limited group scope
    - Bear House runtime scope
    - group 116 level 330 query boundary
    business_meaning: 'Runtime group scope for Bear House Clothing Private Limited: group_id=116 and group_level_id=330.
      It is the client-specific filter boundary that must be applied before resolving account bindings for IN in
      INR.'
    business_questions:
    - Which bindings use group_id=116 and group_level_id=330?
    - Which source families are active under Bear House?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - group_id_value:116
    - group_level_id_value:330
    embedding_text: Bear House is the runtime group node for Bear House Clothing Private Limited. Apply group_id=116
      and group_level_id=330 when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House
    - group_id 116
    - group_level_id 330
    - runtime group scope
    exact_match_keys:
    - group.bear_house_clothing_private_limited.g116.gl330
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    group_level_id: '330'
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id_value: '116'
    group_level_id_value: '330'
    group_name: Bear House
    default_currency: INR
    country: IN
```

### 2.3 Platform Account Cards

#### platform_account.bear_house_clothing_private_limited.ajio.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  card_type: platform_account
  canonical_name: Bear House Clothing Private Limited — Ajio
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
    vendor_or_system: AJIO
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Ajio
    - Bear House Clothing Private Limited Ajio
    - Ajio marketplace account
    colloquial_phrases:
    - Bear House Clothing Private Limited Ajio source account
    - Ajio marketplace runtime account
    - Ajio configured source family
    business_meaning: Runtime platform account for Bear House Clothing Private Limited's Ajio marketplace sources.
      It points traversal to platform.ajio and platform_context.ajio.in and groups the client's table-level account-data
      bindings for this source.
    business_questions:
    - Which Ajio table bindings are available for Bear House Clothing Private Limited?
    - Which canonical platform/context should Bear House Clothing Private Limited's Ajio questions traverse through?
    - Which source roles under Ajio are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS, Settlement, Credit note, Returns'
    - platform.ajio
    - platform_context.ajio.in
    - Ajio
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_id:platform.ajio
    - platform_context_id:platform_context.ajio.in
    - platform_account_id:platform_account.bear_house_clothing_private_limited.ajio.marketplace
    embedding_text: Bear House Clothing Private Limited's Ajio platform account routes marketplace questions to
      platform.ajio / platform_context.ajio.in. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Bear House Clothing Private Limited
    - Ajio
    - marketplace
    - platform.ajio
    - platform_context.ajio.in
    exact_match_keys:
    - platform_account.bear_house_clothing_private_limited.ajio.marketplace
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.ajio
    platform_context_id: platform_context.ajio.in
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.ajio
    platform_context_id: platform_context.ajio.in
    account_name: Ajio
    account_type: marketplace_seller_account
    source_account_identifier: Ajio
    active: true
    configured_source_description: OMS, Settlement, Credit note, Returns
```

#### platform_account.bear_house_clothing_private_limited.amazon_india.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  card_type: platform_account
  canonical_name: Bear House Clothing Private Limited — Amazon India
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
    - Amazon India
    - Bear House Clothing Private Limited Amazon India
    - Amazon
    - Amazon India marketplace account
    colloquial_phrases:
    - Bear House Clothing Private Limited Amazon India source account
    - Amazon India marketplace runtime account
    - Amazon India configured source family
    business_meaning: Runtime platform account for Bear House Clothing Private Limited's Amazon India marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon India table bindings are available for Bear House Clothing Private Limited?
    - Which canonical platform/context should Bear House Clothing Private Limited's Amazon India questions traverse
      through?
    - Which source roles under Amazon India are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS (B2C + B2B), Settlement, Disbursement'
    - platform.amazon
    - platform_context.amazon.in
    - Amazon India
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - platform_account_id:platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    embedding_text: Bear House Clothing Private Limited's Amazon India platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.in. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Bear House Clothing Private Limited
    - Amazon India
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.in
    exact_match_keys:
    - platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    platform_account_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_name: Amazon India
    account_type: marketplace_seller_account
    source_account_identifier: Amazon India
    active: true
    configured_source_description: OMS (B2C + B2B), Settlement, Disbursement
```

#### platform_account.bear_house_clothing_private_limited.flipkart.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  card_type: platform_account
  canonical_name: Bear House Clothing Private Limited — Flipkart
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart
    - Bear House Clothing Private Limited Flipkart
    - Flipkart marketplace account
    colloquial_phrases:
    - Bear House Clothing Private Limited Flipkart source account
    - Flipkart marketplace runtime account
    - Flipkart configured source family
    business_meaning: Runtime platform account for Bear House Clothing Private Limited's Flipkart marketplace sources.
      It points traversal to platform.flipkart and platform_context.flipkart.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Flipkart table bindings are available for Bear House Clothing Private Limited?
    - Which canonical platform/context should Bear House Clothing Private Limited's Flipkart questions traverse
      through?
    - Which source roles under Flipkart are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)'
    - platform.flipkart
    - platform_context.flipkart.in
    - Flipkart
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - platform_account_id:platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    embedding_text: Bear House Clothing Private Limited's Flipkart platform account routes marketplace questions
      to platform.flipkart / platform_context.flipkart.in. Use it to collect the client's table bindings; do not
      use this account card as a table or metric definition.
    search_keywords:
    - Bear House Clothing Private Limited
    - Flipkart
    - marketplace
    - platform.flipkart
    - platform_context.flipkart.in
    exact_match_keys:
    - platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_name: Flipkart
    account_type: marketplace_seller_account
    source_account_identifier: Flipkart
    active: true
    configured_source_description: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### platform_account.bear_house_clothing_private_limited.myntra.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  card_type: platform_account
  canonical_name: Bear House Clothing Private Limited — Myntra
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra
    - Bear House Clothing Private Limited Myntra
    - Myntra marketplace account
    colloquial_phrases:
    - Bear House Clothing Private Limited Myntra source account
    - Myntra marketplace runtime account
    - Myntra configured source family
    business_meaning: Runtime platform account for Bear House Clothing Private Limited's Myntra marketplace sources.
      It points traversal to platform.myntra and platform_context.myntra.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Myntra table bindings are available for Bear House Clothing Private Limited?
    - Which canonical platform/context should Bear House Clothing Private Limited's Myntra questions traverse through?
    - Which source roles under Myntra are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order
      settlement (PPMP), Non-order expenses, Returns/RTO (PPMP)'
    - platform.myntra
    - platform_context.myntra.in
    - Myntra
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - platform_account_id:platform_account.bear_house_clothing_private_limited.myntra.marketplace
    embedding_text: Bear House Clothing Private Limited's Myntra platform account routes marketplace questions to
      platform.myntra / platform_context.myntra.in. Use it to collect the client's table bindings; do not use this
      account card as a table or metric definition.
    search_keywords:
    - Bear House Clothing Private Limited
    - Myntra
    - marketplace
    - platform.myntra
    - platform_context.myntra.in
    exact_match_keys:
    - platform_account.bear_house_clothing_private_limited.myntra.marketplace
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_name: Myntra
    account_type: marketplace_seller_account
    source_account_identifier: Myntra
    active: true
    configured_source_description: OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP),
      Non-order settlement (PPMP), Non-order expenses, Returns/RTO (PPMP)
```

#### platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  card_type: platform_account
  canonical_name: Bear House Clothing Private Limited — Tata Cliq
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
    vendor_or_system: TataCliq
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Tata Cliq
    - Bear House Clothing Private Limited Tata Cliq
    - TataCliq
    - Tata Cliq marketplace account
    colloquial_phrases:
    - Bear House Clothing Private Limited Tata Cliq source account
    - Tata Cliq marketplace runtime account
    - Tata Cliq configured source family
    business_meaning: Runtime platform account for Bear House Clothing Private Limited's Tata Cliq marketplace sources.
      It points traversal to platform.tatacliq and platform_context.tatacliq.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Tata Cliq table bindings are available for Bear House Clothing Private Limited?
    - Which canonical platform/context should Bear House Clothing Private Limited's Tata Cliq questions traverse
      through?
    - Which source roles under Tata Cliq are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS, Settlement'
    - platform.tatacliq
    - platform_context.tatacliq.in
    - Tata Cliq
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_id:platform.tatacliq
    - platform_context_id:platform_context.tatacliq.in
    - platform_account_id:platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
    embedding_text: Bear House Clothing Private Limited's Tata Cliq platform account routes marketplace questions
      to platform.tatacliq / platform_context.tatacliq.in. Use it to collect the client's table bindings; do not
      use this account card as a table or metric definition.
    search_keywords:
    - Bear House Clothing Private Limited
    - Tata Cliq
    - TataCliq
    - marketplace
    - platform.tatacliq
    - platform_context.tatacliq.in
    exact_match_keys:
    - platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.tatacliq
    platform_context_id: platform_context.tatacliq.in
    platform_account_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.tatacliq
    platform_context_id: platform_context.tatacliq.in
    account_name: Tata Cliq
    account_type: marketplace_seller_account
    source_account_identifier: Tata Cliq
    active: true
    configured_source_description: OMS, Settlement
```

#### platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms

```yaml
canonical_card:
  canonical_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  card_type: platform_account
  canonical_name: Bear House Clothing Private Limited — Unicommerce WMS
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Unicommerce WMS
    - Bear House Clothing Private Limited Unicommerce WMS
    - Unicommerce
    - Unicommerce WMS WMS account
    colloquial_phrases:
    - Bear House Clothing Private Limited Unicommerce WMS source account
    - Unicommerce WMS WMS runtime account
    - Unicommerce WMS configured source family
    business_meaning: Runtime platform account for Bear House Clothing Private Limited's Unicommerce WMS WMS sources.
      It points traversal to platform.unicommerce and platform_context.unicommerce.in_wms and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Unicommerce WMS table bindings are available for Bear House Clothing Private Limited?
    - Which canonical platform/context should Bear House Clothing Private Limited's Unicommerce WMS questions traverse
      through?
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - platform_account_id:platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
    - runtime_source_family:wms
    embedding_text: Bear House Clothing Private Limited's Unicommerce WMS platform account routes WMS questions
      to platform.unicommerce / platform_context.unicommerce.in_wms. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Bear House Clothing Private Limited
    - Unicommerce WMS
    - Unicommerce
    - WMS
    - platform.unicommerce
    - platform_context.unicommerce.in_wms
    exact_match_keys:
    - platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    - unicommerce_wms.md
    source_path: Bear House Clothing Private Limited.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
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
      group_id: '116'
      group_level_id: '330'
```

### 2.4 Account Data Binding Cards

#### account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Ajio — credit_note
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
    vendor_or_system: AJIO
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AJIO credit note
    - ajio_credit_note
    - zs_observe.ajio_credit_note
    - OMS, Settlement, Credit note, Returns
    - Bear House Clothing Private Limited AJIO credit note
    colloquial_phrases:
    - Bear House Clothing Private Limited AJIO credit note source
    - AJIO credit note runtime binding
    - ajio_credit_note for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's AJIO
      credit note evidence should use zs_observe.ajio_credit_note. Apply group_id=116, group_level_id=330 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which AJIO credit note file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep ajio_credit_note limited to Bear House Clothing Private Limited?
    - What AJIO canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - credit_note
    included_concepts:
    - zs_observe.ajio_credit_note
    - credit note
    - AJIO
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.ajio.marketplace
    - platform_id:platform.ajio
    - platform_context_id:platform_context.ajio.in
    - source_role:credit_note
    - table_id:table.zs_observe.ajio_credit_note
    embedding_text: 'For Bear House Clothing Private Limited, the AJIO credit note binding selects zs_observe.ajio_credit_note
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - AJIO
    - credit note
    - marketplace
    - zs_observe.ajio_credit_note
    - ajio_credit_note
    - credit_note
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
    platform_id: platform.ajio
    platform_context_id: platform_context.ajio.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
    table_id: table.zs_observe.ajio_credit_note
    source_role: credit_note
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
    table_id: table.zs_observe.ajio_credit_note
    source_role: credit_note
    source_entity: AJIO
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.ajio_credit_note.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.ajio_credit_note.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS, Settlement, Credit note, Returns
```

#### account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Ajio — marketplace_settlement
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
    vendor_or_system: AJIO
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AJIO marketplace settlement
    - ajio_settlement
    - zs_observe.ajio_settlement
    - OMS, Settlement, Credit note, Returns
    - Bear House Clothing Private Limited AJIO marketplace settlement
    colloquial_phrases:
    - Bear House Clothing Private Limited AJIO marketplace settlement source
    - AJIO marketplace settlement runtime binding
    - ajio_settlement for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's AJIO
      marketplace settlement evidence should use zs_observe.ajio_settlement. Apply group_id=116, group_level_id=330
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which AJIO marketplace settlement file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep ajio_settlement limited to Bear House Clothing Private Limited?
    - What AJIO canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - marketplace_settlement
    included_concepts:
    - zs_observe.ajio_settlement
    - marketplace settlement
    - AJIO
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.ajio.marketplace
    - platform_id:platform.ajio
    - platform_context_id:platform_context.ajio.in
    - source_role:marketplace_settlement
    - table_id:table.zs_observe.ajio_settlement
    embedding_text: 'For Bear House Clothing Private Limited, the AJIO marketplace settlement binding selects zs_observe.ajio_settlement
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - AJIO
    - marketplace settlement
    - marketplace
    - zs_observe.ajio_settlement
    - ajio_settlement
    - marketplace_settlement
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
    platform_id: platform.ajio
    platform_context_id: platform_context.ajio.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
    table_id: table.zs_observe.ajio_settlement
    source_role: marketplace_settlement
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
    table_id: table.zs_observe.ajio_settlement
    source_role: marketplace_settlement
    source_entity: AJIO
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.ajio_settlement.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.ajio_settlement.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS, Settlement, Credit note, Returns
```

#### account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Ajio — oms_sales
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
    vendor_or_system: AJIO
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AJIO OMS sales
    - ajio_oms
    - zs_observe.ajio_oms
    - OMS, Settlement, Credit note, Returns
    - Bear House Clothing Private Limited AJIO OMS sales
    colloquial_phrases:
    - Bear House Clothing Private Limited AJIO OMS sales source
    - AJIO OMS sales runtime binding
    - ajio_oms for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's AJIO
      OMS sales evidence should use zs_observe.ajio_oms. Apply group_id=116, group_level_id=330 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which AJIO OMS sales file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep ajio_oms limited to Bear House Clothing Private Limited?
    - What AJIO canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.ajio_oms
    - OMS sales
    - AJIO
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.ajio.marketplace
    - platform_id:platform.ajio
    - platform_context_id:platform_context.ajio.in
    - source_role:oms_sales
    - table_id:table.zs_observe.ajio_oms
    embedding_text: 'For Bear House Clothing Private Limited, the AJIO OMS sales binding selects zs_observe.ajio_oms
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - AJIO
    - OMS sales
    - marketplace
    - zs_observe.ajio_oms
    - ajio_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
    platform_id: platform.ajio
    platform_context_id: platform_context.ajio.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
    table_id: table.zs_observe.ajio_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
    table_id: table.zs_observe.ajio_oms
    source_role: oms_sales
    source_entity: AJIO
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.ajio_oms.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.ajio_oms.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS, Settlement, Credit note, Returns
```

#### account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Ajio — returns
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
    vendor_or_system: AJIO
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AJIO returns
    - ajio_reverse
    - zs_observe.ajio_reverse
    - OMS, Settlement, Credit note, Returns
    - Bear House Clothing Private Limited AJIO returns
    colloquial_phrases:
    - Bear House Clothing Private Limited AJIO returns source
    - AJIO returns runtime binding
    - ajio_reverse for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's AJIO
      returns evidence should use zs_observe.ajio_reverse. Apply group_id=116, group_level_id=330 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which AJIO returns file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep ajio_reverse limited to Bear House Clothing Private Limited?
    - What AJIO canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - returns
    included_concepts:
    - zs_observe.ajio_reverse
    - returns
    - AJIO
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.ajio.marketplace
    - platform_id:platform.ajio
    - platform_context_id:platform_context.ajio.in
    - source_role:returns
    - table_id:table.zs_observe.ajio_reverse
    embedding_text: 'For Bear House Clothing Private Limited, the AJIO returns binding selects zs_observe.ajio_reverse
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - AJIO
    - returns
    - marketplace
    - zs_observe.ajio_reverse
    - ajio_reverse
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
    platform_id: platform.ajio
    platform_context_id: platform_context.ajio.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
    table_id: table.zs_observe.ajio_reverse
    source_role: returns
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
    table_id: table.zs_observe.ajio_reverse
    source_role: returns
    source_entity: AJIO
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.ajio_reverse.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS, Settlement, Credit note, Returns
```

#### account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Amazon India — disbursement
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
    - Amazon disbursement
    - amazon_disbursment
    - zs_observe.amazon_disbursment
    - OMS (B2C + B2B), Settlement, Disbursement
    - Bear House Clothing Private Limited Amazon disbursement
    colloquial_phrases:
    - Bear House Clothing Private Limited Amazon disbursement source
    - Amazon disbursement runtime binding
    - amazon_disbursment for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Amazon
      disbursement evidence should use zs_observe.amazon_disbursment. Apply group_id=116, group_level_id=330 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon disbursement file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep amazon_disbursment limited to Bear House Clothing Private Limited?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - disbursement
    included_concepts:
    - zs_observe.amazon_disbursment
    - disbursement
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:disbursement
    - table_id:table.zs_observe.amazon_disbursment
    embedding_text: 'For Bear House Clothing Private Limited, the Amazon disbursement binding selects zs_observe.amazon_disbursment
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Amazon
    - disbursement
    - marketplace
    - zs_observe.amazon_disbursment
    - amazon_disbursment
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
    table_id: table.zs_observe.amazon_disbursment
    source_role: disbursement
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    table_id: table.zs_observe.amazon_disbursment
    source_role: disbursement
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_disbursment.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_disbursment.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement
```

#### account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Amazon India — oms_sales
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
    - Amazon OMS sales
    - amazon_oms
    - zs_observe.amazon_oms
    - OMS (B2C + B2B), Settlement, Disbursement
    - Bear House Clothing Private Limited Amazon OMS sales
    colloquial_phrases:
    - Bear House Clothing Private Limited Amazon OMS sales source
    - Amazon OMS sales runtime binding
    - amazon_oms for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Amazon
      OMS sales evidence should use zs_observe.amazon_oms. Apply group_id=116, group_level_id=330 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon OMS sales file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep amazon_oms limited to Bear House Clothing Private Limited?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.amazon_oms
    - OMS sales
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:oms_sales
    - table_id:table.zs_observe.amazon_oms
    embedding_text: 'For Bear House Clothing Private Limited, the Amazon OMS sales binding selects zs_observe.amazon_oms
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Amazon
    - OMS sales
    - marketplace
    - zs_observe.amazon_oms
    - amazon_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_oms.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_oms.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement
```

#### account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Amazon India — settlement
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
    - OMS (B2C + B2B), Settlement, Disbursement
    - Bear House Clothing Private Limited Amazon settlement
    colloquial_phrases:
    - Bear House Clothing Private Limited Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=116, group_level_id=330 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep amazon_settlement limited to Bear House Clothing Private Limited?
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
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Bear House Clothing Private Limited, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement
```

#### account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Flipkart — cashback_credit_debit_note
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart cashback / credit-debit note
    - flipkart_cashback
    - zs_observe.flipkart_cashback
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
    - Bear House Clothing Private Limited Flipkart cashback / credit-debit note
    colloquial_phrases:
    - Bear House Clothing Private Limited Flipkart cashback / credit-debit note source
    - Flipkart cashback / credit-debit note runtime binding
    - flipkart_cashback for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Flipkart
      cashback / credit-debit note evidence should use zs_observe.flipkart_cashback. Apply group_id=116, group_level_id=330
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart cashback / credit-debit note file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep flipkart_cashback limited to Bear House Clothing Private Limited?
    - What Flipkart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - cashback_credit_debit_note
    included_concepts:
    - zs_observe.flipkart_cashback
    - cashback / credit-debit note
    - Flipkart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:cashback_credit_debit_note
    - table_id:table.zs_observe.flipkart_cashback
    embedding_text: 'For Bear House Clothing Private Limited, the Flipkart cashback / credit-debit note binding
      selects zs_observe.flipkart_cashback as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable
      semantics come from uploaded marketplace canonical pack. Use this card for runtime source resolution, not
      for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Flipkart
    - cashback / credit-debit note
    - marketplace
    - zs_observe.flipkart_cashback
    - flipkart_cashback
    - cashback_credit_debit_note
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    table_id: table.zs_observe.flipkart_cashback
    source_role: cashback_credit_debit_note
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    table_id: table.zs_observe.flipkart_cashback
    source_role: cashback_credit_debit_note
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_cashback.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_cashback.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Flipkart — commission_fee_invoice
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart commission invoice
    - flipkart_commission
    - zs_observe.flipkart_commission
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
    - Bear House Clothing Private Limited Flipkart commission invoice
    colloquial_phrases:
    - Bear House Clothing Private Limited Flipkart commission invoice source
    - Flipkart commission invoice runtime binding
    - flipkart_commission for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Flipkart
      commission invoice evidence should use zs_observe.flipkart_commission. Apply group_id=116, group_level_id=330
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart commission invoice file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep flipkart_commission limited to Bear House Clothing Private Limited?
    - What Flipkart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - commission_fee_invoice
    included_concepts:
    - zs_observe.flipkart_commission
    - commission invoice
    - Flipkart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:commission_fee_invoice
    - table_id:table.zs_observe.flipkart_commission
    embedding_text: 'For Bear House Clothing Private Limited, the Flipkart commission invoice binding selects zs_observe.flipkart_commission
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Flipkart
    - commission invoice
    - marketplace
    - zs_observe.flipkart_commission
    - flipkart_commission
    - commission_fee_invoice
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    table_id: table.zs_observe.flipkart_commission
    source_role: commission_fee_invoice
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    table_id: table.zs_observe.flipkart_commission
    source_role: commission_fee_invoice
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_commission.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_commission.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Flipkart — oms_sales
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart OMS sales
    - flipkart_oms
    - zs_recon_processor.flipkart_oms
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
    - Bear House Clothing Private Limited Flipkart OMS sales
    colloquial_phrases:
    - Bear House Clothing Private Limited Flipkart OMS sales source
    - Flipkart OMS sales runtime binding
    - flipkart_oms for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Flipkart
      OMS sales evidence should use zs_recon_processor.flipkart_oms. Apply group_id=116, group_level_id=330 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart OMS sales file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep flipkart_oms limited to Bear House Clothing Private Limited?
    - What Flipkart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_recon_processor.flipkart_oms
    - OMS sales
    - Flipkart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:oms_sales
    - table_id:table.zs_recon_processor.flipkart_oms
    embedding_text: 'For Bear House Clothing Private Limited, the Flipkart OMS sales binding selects zs_recon_processor.flipkart_oms
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Flipkart
    - OMS sales
    - marketplace
    - zs_recon_processor.flipkart_oms
    - flipkart_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    table_id: table.zs_recon_processor.flipkart_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    table_id: table.zs_recon_processor.flipkart_oms
    source_role: oms_sales
    source_entity: Flipkart
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_recon_processor.flipkart_oms.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Flipkart — settlement
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart settlement
    - flipkart_settlement
    - zs_observe.flipkart_settlement
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
    - Bear House Clothing Private Limited Flipkart settlement
    colloquial_phrases:
    - Bear House Clothing Private Limited Flipkart settlement source
    - Flipkart settlement runtime binding
    - flipkart_settlement for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Flipkart
      settlement evidence should use zs_observe.flipkart_settlement. Apply group_id=116, group_level_id=330 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart settlement file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep flipkart_settlement limited to Bear House Clothing Private Limited?
    - What Flipkart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.flipkart_settlement
    - settlement
    - Flipkart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:settlement
    - table_id:table.zs_observe.flipkart_settlement
    embedding_text: 'For Bear House Clothing Private Limited, the Flipkart settlement binding selects zs_observe.flipkart_settlement
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Flipkart
    - settlement
    - marketplace
    - zs_observe.flipkart_settlement
    - flipkart_settlement
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
    table_id: table.zs_observe.flipkart_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    table_id: table.zs_observe.flipkart_settlement
    source_role: settlement
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_settlement.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_settlement.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Myntra — non_order_settlement
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra non-order settlement
    - myntra_non_order_settlement
    - zs_observe.myntra_non_order_settlement
    - OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order settlement (PPMP),
      Non-order expenses, Returns/RTO (PPMP)
    - Bear House Clothing Private Limited Myntra non-order settlement
    colloquial_phrases:
    - Bear House Clothing Private Limited Myntra non-order settlement source
    - Myntra non-order settlement runtime binding
    - myntra_non_order_settlement for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Myntra
      non-order settlement evidence should use zs_observe.myntra_non_order_settlement. Apply group_id=116, group_level_id=330
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra non-order settlement file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep myntra_non_order_settlement limited to Bear House Clothing Private Limited?
    - What Myntra canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - non_order_settlement
    included_concepts:
    - zs_observe.myntra_non_order_settlement
    - non-order settlement
    - Myntra
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:non_order_settlement
    - table_id:table.zs_observe.myntra_non_order_settlement
    embedding_text: 'For Bear House Clothing Private Limited, the Myntra non-order settlement binding selects zs_observe.myntra_non_order_settlement
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Myntra
    - non-order settlement
    - marketplace
    - zs_observe.myntra_non_order_settlement
    - myntra_non_order_settlement
    - non_order_settlement
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    table_id: table.zs_observe.myntra_non_order_settlement
    source_role: non_order_settlement
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
    table_id: table.zs_observe.myntra_non_order_settlement
    source_role: non_order_settlement
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_non_order_settlement.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_non_order_settlement.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order
      settlement (PPMP), Non-order expenses, Returns/RTO (PPMP)
```

#### account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Myntra — oms_sales
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra OMS sales
    - myntra_oms
    - zs_observe.myntra_oms
    - OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order settlement (PPMP),
      Non-order expenses, Returns/RTO (PPMP)
    - Bear House Clothing Private Limited Myntra OMS sales
    colloquial_phrases:
    - Bear House Clothing Private Limited Myntra OMS sales source
    - Myntra OMS sales runtime binding
    - myntra_oms for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Myntra
      OMS sales evidence should use zs_observe.myntra_oms. Apply group_id=116, group_level_id=330 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra OMS sales file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep myntra_oms limited to Bear House Clothing Private Limited?
    - What Myntra canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.myntra_oms
    - OMS sales
    - Myntra
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:oms_sales
    - table_id:table.zs_observe.myntra_oms
    embedding_text: 'For Bear House Clothing Private Limited, the Myntra OMS sales binding selects zs_observe.myntra_oms
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Myntra
    - OMS sales
    - marketplace
    - zs_observe.myntra_oms
    - myntra_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
    table_id: table.zs_observe.myntra_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
    table_id: table.zs_observe.myntra_oms
    source_role: oms_sales
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_oms.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_oms.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order
      settlement (PPMP), Non-order expenses, Returns/RTO (PPMP)
```

#### account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Myntra — returns
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra returns
    - myntra_reverse
    - zs_observe.myntra_reverse
    - OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order settlement (PPMP),
      Non-order expenses, Returns/RTO (PPMP)
    - Bear House Clothing Private Limited Myntra returns
    colloquial_phrases:
    - Bear House Clothing Private Limited Myntra returns source
    - Myntra returns runtime binding
    - myntra_reverse for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Myntra
      returns evidence should use zs_observe.myntra_reverse. Apply group_id=116, group_level_id=330 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra returns file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep myntra_reverse limited to Bear House Clothing Private Limited?
    - What Myntra canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - returns
    included_concepts:
    - zs_observe.myntra_reverse
    - returns
    - Myntra
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:returns
    - table_id:table.zs_observe.myntra_reverse
    embedding_text: 'For Bear House Clothing Private Limited, the Myntra returns binding selects zs_observe.myntra_reverse
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Myntra
    - returns
    - marketplace
    - zs_observe.myntra_reverse
    - myntra_reverse
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
    table_id: table.zs_observe.myntra_reverse
    source_role: returns
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
    table_id: table.zs_observe.myntra_reverse
    source_role: returns
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_reverse.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_reverse.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order
      settlement (PPMP), Non-order expenses, Returns/RTO (PPMP)
```

#### account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Myntra — settlement
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra settlement
    - myntra_settlement
    - zs_observe.myntra_settlement
    - OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order settlement (PPMP),
      Non-order expenses, Returns/RTO (PPMP)
    - Bear House Clothing Private Limited Myntra settlement
    colloquial_phrases:
    - Bear House Clothing Private Limited Myntra settlement source
    - Myntra settlement runtime binding
    - myntra_settlement for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Myntra
      settlement evidence should use zs_observe.myntra_settlement. Apply group_id=116, group_level_id=330 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra settlement file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep myntra_settlement limited to Bear House Clothing Private Limited?
    - What Myntra canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.myntra_settlement
    - settlement
    - Myntra
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:settlement
    - table_id:table.zs_observe.myntra_settlement
    embedding_text: 'For Bear House Clothing Private Limited, the Myntra settlement binding selects zs_observe.myntra_settlement
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Myntra
    - settlement
    - marketplace
    - zs_observe.myntra_settlement
    - myntra_settlement
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
    table_id: table.zs_observe.myntra_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
    table_id: table.zs_observe.myntra_settlement
    source_role: settlement
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_settlement.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_settlement.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS (PPMP only), Seller reports (Fwd + Rev PPMP), Fwd/Rev settlement (PPMP), Non-order
      settlement (PPMP), Non-order expenses, Returns/RTO (PPMP)
```

#### account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Tata Cliq — oms_invoice
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
    vendor_or_system: TataCliq
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - TataCliq OMS invoice
    - tatacliq_oms
    - zs_observe.tatacliq_oms
    - OMS, Settlement
    - Bear House Clothing Private Limited TataCliq OMS invoice
    colloquial_phrases:
    - Bear House Clothing Private Limited TataCliq OMS invoice source
    - TataCliq OMS invoice runtime binding
    - tatacliq_oms for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's TataCliq
      OMS invoice evidence should use zs_observe.tatacliq_oms. Apply group_id=116, group_level_id=330 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which TataCliq OMS invoice file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep tatacliq_oms limited to Bear House Clothing Private Limited?
    - What TataCliq canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_invoice
    included_concepts:
    - zs_observe.tatacliq_oms
    - OMS invoice
    - TataCliq
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
    - platform_id:platform.tatacliq
    - platform_context_id:platform_context.tatacliq.in
    - source_role:oms_invoice
    - table_id:table.zs_observe.tatacliq_oms
    embedding_text: 'For Bear House Clothing Private Limited, the TataCliq OMS invoice binding selects zs_observe.tatacliq_oms
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - TataCliq
    - OMS invoice
    - marketplace
    - zs_observe.tatacliq_oms
    - tatacliq_oms
    - oms_invoice
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
    platform_id: platform.tatacliq
    platform_context_id: platform_context.tatacliq.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
    table_id: table.zs_observe.tatacliq_oms
    source_role: oms_invoice
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
    table_id: table.zs_observe.tatacliq_oms
    source_role: oms_invoice
    source_entity: TataCliq
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '116'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.tatacliq_oms.group_id
      runtime_value: '116'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.tatacliq_oms.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS, Settlement
```

#### account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited — Tata Cliq — settlement_payout
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
    vendor_or_system: TataCliq
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - TataCliq settlement payout
    - tatacliq_settlement
    - zs_observe.tatacliq_settlement
    - OMS, Settlement
    - Bear House Clothing Private Limited TataCliq settlement payout
    colloquial_phrases:
    - Bear House Clothing Private Limited TataCliq settlement payout source
    - TataCliq settlement payout runtime binding
    - tatacliq_settlement for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's TataCliq
      settlement payout evidence should use zs_observe.tatacliq_settlement. Apply group_id=116, group_level_id=330
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which TataCliq settlement payout file/table is active for Bear House Clothing Private Limited?
    - Which group filters keep tatacliq_settlement limited to Bear House Clothing Private Limited?
    - What TataCliq canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement_payout
    included_concepts:
    - zs_observe.tatacliq_settlement
    - settlement payout
    - TataCliq
    - marketplace source role
    - client-scoped marketplace table
    - group_id=116
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
    - platform_id:platform.tatacliq
    - platform_context_id:platform_context.tatacliq.in
    - source_role:settlement_payout
    - table_id:table.zs_observe.tatacliq_settlement
    embedding_text: 'For Bear House Clothing Private Limited, the TataCliq settlement payout binding selects zs_observe.tatacliq_settlement
      as marketplace evidence. Scope: group_id=116, group_level_id=330. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - TataCliq
    - settlement payout
    - marketplace
    - zs_observe.tatacliq_settlement
    - tatacliq_settlement
    - settlement_payout
    - uploaded marketplace canonical pack
    - group_id=116
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
    platform_id: platform.tatacliq
    platform_context_id: platform_context.tatacliq.in
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
    table_id: table.zs_observe.tatacliq_settlement
    source_role: settlement_payout
  fields:
    platform_account_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
    table_id: table.zs_observe.tatacliq_settlement
    source_role: settlement_payout
    source_entity: TataCliq
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '330'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.tatacliq_settlement.group_level_id
      runtime_value: '330'
    active: true
    source_configuration_text: OMS, Settlement
```

#### account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited Unicommerce WMS invoice transaction ledger binding
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
    vendor_or_system: Bear House Clothing Private Limited
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
    - Bear House Clothing Private Limited Unicommerce WMS WMS invoice transaction ledger
    colloquial_phrases:
    - Bear House Clothing Private Limited Unicommerce WMS WMS invoice transaction ledger source
    - Unicommerce WMS WMS invoice transaction ledger runtime binding
    - unicommerce for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Unicommerce
      WMS WMS invoice transaction ledger evidence should use zs_observe.unicommerce. Apply group_level_id=330 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in unicommerce_wms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Unicommerce WMS WMS rows should answer Bear House Clothing Private Limited's WMS invoice transaction
      ledger question?
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
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - domain_id:domain.wms.unicommerce.fulfilment_operations
    - table_id:table.zs_observe.unicommerce
    - source_role:wms_invoice_transaction_ledger
    - runtime_source_family:wms
    embedding_text: 'For Bear House Clothing Private Limited, the Unicommerce WMS WMS invoice transaction ledger
      binding selects zs_observe.unicommerce as WMS evidence. Scope: group_level_id=330. Reusable semantics come
      from unicommerce_wms.md. Coverage status: active. Use this card for runtime source resolution, not for defining
      table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Unicommerce WMS
    - WMS invoice transaction ledger
    - WMS
    - zs_observe.unicommerce
    - unicommerce
    - wms_invoice_transaction_ledger
    - unicommerce_wms.md
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    - unicommerce_wms.md
    source_path: Bear House Clothing Private Limited.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce
    source_role: wms_invoice_transaction_ledger
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
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
      value: '330'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.unicommerce.group_level_id
      runtime_value: '330'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - runtime group_level_id filter
    - metadata filter when separating sales, returns, or cancellations
    grain_from_reusable_pack: order or SKU invoice transaction row carrying sales, reverse return, or cancellation
      classification
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report

```yaml
canonical_card:
  canonical_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  card_type: account_data_binding
  canonical_name: Bear House Clothing Private Limited Unicommerce WMS order sales report shipment tracking binding
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
    vendor_or_system: Bear House Clothing Private Limited
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
    - Bear House Clothing Private Limited Unicommerce WMS WMS shipment tracking
    colloquial_phrases:
    - Bear House Clothing Private Limited Unicommerce WMS WMS shipment tracking source
    - Unicommerce WMS WMS shipment tracking runtime binding
    - unicommerce_order_sales_report for Bear House Clothing Private Limited
    business_meaning: This account-data binding tells the resolver that Bear House Clothing Private Limited's Unicommerce
      WMS WMS shipment tracking evidence should use zs_observe.unicommerce_order_sales_report. Apply group_level_id=330
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in unicommerce_wms.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Unicommerce WMS WMS rows should answer Bear House Clothing Private Limited's WMS shipment tracking question?
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
    - group_level_id=330
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - platform_account_id:platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - domain_id:domain.wms.unicommerce.fulfilment_operations
    - table_id:table.zs_observe.unicommerce_order_sales_report
    - source_role:wms_shipment_tracking
    - runtime_source_family:wms
    embedding_text: 'For Bear House Clothing Private Limited, the Unicommerce WMS WMS shipment tracking binding
      selects zs_observe.unicommerce_order_sales_report as WMS evidence. Scope: group_level_id=330. Reusable semantics
      come from unicommerce_wms.md. Coverage status: active. Use this card for runtime source resolution, not for
      defining table columns or metrics.'
    search_keywords:
    - Bear House Clothing Private Limited
    - Unicommerce WMS
    - WMS shipment tracking
    - WMS
    - zs_observe.unicommerce_order_sales_report
    - unicommerce_order_sales_report
    - wms_shipment_tracking
    - unicommerce_wms.md
    - group_level_id=330
    exact_match_keys:
    - account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    - unicommerce_wms.md
    source_path: Bear House Clothing Private Limited.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce_order_sales_report
    source_role: wms_shipment_tracking
    account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
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
      value: '330'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
      runtime_value: '330'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - runtime group_level_id filter when available
    grain_from_reusable_pack: shipment or order-SKU operational row carrying delivery status, AWB, courier method,
      MRP and package dimensions
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

### 2.5 Business Scope Set Cards

#### business_scope_set.bear_house_clothing_private_limited.logistics

```yaml
canonical_card:
  canonical_id: business_scope_set.bear_house_clothing_private_limited.logistics
  card_type: business_scope_set
  canonical_name: Bear House Clothing Private Limited logistics scope
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    - logistics_integrated.md
    source_path: Bear House Clothing Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.logistics
    runtime_source_family: logistics
  semantic:
    aliases:
    - Bear House Clothing Private Limited logistics scope
    - Bear House Clothing Private Limited logistics / courier scope
    - logistics / courier runtime scope set
    colloquial_phrases:
    - Bear House Clothing Private Limited logistics / courier scope
    - logistics / courier accounts and bindings
    - Bear House Clothing Private Limited logistics / courier resolver input
    business_meaning: Business scope set for Bear House Clothing Private Limited's logistics / courier runtime resolution.
      It groups 0 platform accounts and 0 account-data bindings so the resolver can choose client-scoped sources
      before entering reusable canonical packs.
    business_questions:
    - Which logistics / courier accounts and bindings are active for Bear House Clothing Private Limited?
    - Which runtime table bindings should be considered together under Bear House Clothing Private Limited logistics
      scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - logistics_courier
    - resolver_scope
    included_concepts:
    - 0 platform accounts
    - 0 account-data bindings
    - 2 deferred sources
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - business_scope_set_id:business_scope_set.bear_house_clothing_private_limited.logistics
    - runtime_source_family:logistics
    embedding_text: Bear House Clothing Private Limited logistics scope groups Bear House Clothing Private Limited's
      logistics / courier runtime accounts and table bindings. Use it to restrict traversal to the client's configured
      sources; unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House Clothing Private Limited logistics scope
    - logistics / courier
    - business scope set
    - 0 accounts
    - 0 bindings
    exact_match_keys:
    - business_scope_set.bear_house_clothing_private_limited.logistics
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    scope_name: Bear House Clothing Private Limited logistics scope
    scope_type: logistics_courier_reconciliation
    platform_account_ids: []
    platform_ids: []
    platform_context_ids: []
    account_data_binding_ids: []
    group_scope_values:
      group_id: '116'
      group_level_id: '330'
    deferred_sources:
    - label: Bluedart
      config: Settlement + Invoice (PP Teabox variant)
      reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: GoSwift
      config: Settlement + Invoice
      reason: No GoSwift canonical logistics platform/table cards in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.bear_house_clothing_private_limited.marketplace

```yaml
canonical_card:
  canonical_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  card_type: business_scope_set
  canonical_name: Bear House Clothing Private Limited marketplace scope
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bear House Clothing Private Limited marketplace scope
    - marketplace runtime scope set
    colloquial_phrases:
    - Bear House Clothing Private Limited marketplace scope
    - marketplace accounts and bindings
    - Bear House Clothing Private Limited marketplace resolver input
    business_meaning: Business scope set for Bear House Clothing Private Limited's marketplace runtime resolution.
      It groups 5 platform accounts and 17 account-data bindings so the resolver can choose client-scoped sources
      before entering reusable canonical packs.
    business_questions:
    - Which marketplace accounts and bindings are active for Bear House Clothing Private Limited?
    - Which runtime table bindings should be considered together under Bear House Clothing Private Limited marketplace
      scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - marketplace
    - resolver_scope
    included_concepts:
    - 5 platform accounts
    - 17 account-data bindings
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - business_scope_set_id:business_scope_set.bear_house_clothing_private_limited.marketplace
    embedding_text: Bear House Clothing Private Limited marketplace scope groups Bear House Clothing Private Limited's
      marketplace runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House Clothing Private Limited marketplace scope
    - marketplace
    - business scope set
    - 5 accounts
    - 17 bindings
    exact_match_keys:
    - business_scope_set.bear_house_clothing_private_limited.marketplace
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    scope_name: Bear House Clothing Private Limited marketplace scope
    scope_type: marketplace_only
    platform_account_ids:
    - platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
    - platform_account.bear_house_clothing_private_limited.flipkart.marketplace
    - platform_account.bear_house_clothing_private_limited.myntra.marketplace
    - platform_account.bear_house_clothing_private_limited.ajio.marketplace
    - platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
    platform_ids:
    - platform.ajio
    - platform.amazon
    - platform.flipkart
    - platform.myntra
    - platform.tatacliq
    platform_context_ids:
    - platform_context.ajio.in
    - platform_context.amazon.in
    - platform_context.flipkart.in
    - platform_context.myntra.in
    - platform_context.tatacliq.in
    account_data_binding_ids:
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
    - account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    - account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
    - account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    - account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    - account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
    - account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
    - account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    - account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
    - account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
    - account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
    - account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
    - account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
    - account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
    - account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
```

#### business_scope_set.bear_house_clothing_private_limited.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.bear_house_clothing_private_limited.oms
  card_type: business_scope_set
  canonical_name: Bear House Clothing Private Limited OMS runtime scope
  status: review_required
  review_status: review_required
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bear House Clothing Private Limited OMS runtime scope
    - Bear House Clothing Private Limited OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Bear House Clothing Private Limited OMS scope
    - OMS accounts and bindings
    - Bear House Clothing Private Limited OMS resolver input
    business_meaning: Business scope set for Bear House Clothing Private Limited's OMS runtime resolution. It groups
      0 platform accounts and 0 account-data bindings so the resolver can choose client-scoped sources before entering
      reusable canonical packs.
    business_questions:
    - Which OMS accounts and bindings are active for Bear House Clothing Private Limited?
    - Which runtime table bindings should be considered together under Bear House Clothing Private Limited OMS runtime
      scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - OMS
    - resolver_scope
    included_concepts:
    - 0 platform accounts
    - 0 account-data bindings
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - runtime_source_family:oms
    embedding_text: Bear House Clothing Private Limited OMS runtime scope groups Bear House Clothing Private Limited's
      OMS runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House Clothing Private Limited OMS runtime scope
    - OMS
    - business scope set
    - 0 accounts
    - 0 bindings
    exact_match_keys:
    - business_scope_set.bear_house_clothing_private_limited.oms
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
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.oms
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    binding_name: Bear House Clothing Private Limited OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.oms
    account_data_binding_ids: []
    participating_accounts: []
    source_flow_paths: []
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.bear_house_clothing_private_limited.wms

```yaml
canonical_card:
  canonical_id: business_scope_set.bear_house_clothing_private_limited.wms
  card_type: business_scope_set
  canonical_name: Bear House Clothing Private Limited WMS runtime scope
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bear House Clothing Private Limited WMS runtime scope
    - Bear House Clothing Private Limited WMS scope
    - WMS runtime scope set
    colloquial_phrases:
    - Bear House Clothing Private Limited WMS scope
    - WMS accounts and bindings
    - Bear House Clothing Private Limited WMS resolver input
    business_meaning: Business scope set for Bear House Clothing Private Limited's WMS runtime resolution. It groups
      1 platform accounts and 2 account-data bindings so the resolver can choose client-scoped sources before entering
      reusable canonical packs.
    business_questions:
    - Which WMS accounts and bindings are active for Bear House Clothing Private Limited?
    - Which runtime table bindings should be considered together under Bear House Clothing Private Limited WMS runtime
      scope?
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - runtime_source_family:wms
    embedding_text: Bear House Clothing Private Limited WMS runtime scope groups Bear House Clothing Private Limited's
      WMS runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House Clothing Private Limited WMS runtime scope
    - WMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.bear_house_clothing_private_limited.wms
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
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
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    runtime_source_family: wms
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.wms
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    binding_name: Bear House Clothing Private Limited WMS runtime scope
    binding_type: wms_source_resolution
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.wms
    platform_account_ids:
    - platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
    account_data_binding_ids:
    - account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    - account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    included_platform_ids:
    - platform.unicommerce
    included_platform_context_ids:
    - platform_context.unicommerce.in_wms
    source_flow_paths:
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
      platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
      source_role: wms_invoice_transaction_ledger
      table_id: table.zs_observe.unicommerce
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
      platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
      source_role: wms_shipment_tracking
      table_id: table.zs_observe.unicommerce_order_sales_report
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

### 2.6 Business Flow Binding Cards

#### business_flow_binding.bear_house_clothing_private_limited.logistics_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.bear_house_clothing_private_limited.logistics_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bear House Clothing Private Limited logistics runtime resolution
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    - logistics_integrated.md
    source_path: Bear House Clothing Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    business_flow_binding_id: business_flow_binding.bear_house_clothing_private_limited.logistics_runtime_resolution
    runtime_source_family: logistics
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.logistics
  semantic:
    aliases:
    - Bear House Clothing Private Limited logistics runtime resolution
    - Bear House Clothing Private Limited logistics / courier flow
    - logistics / courier runtime resolution flow
    colloquial_phrases:
    - Bear House Clothing Private Limited logistics / courier resolution flow
    - logistics / courier source routing
    - Bear House Clothing Private Limited runtime traversal plan
    business_meaning: Business flow binding for Bear House Clothing Private Limited's logistics / courier source
      resolution. It connects the scope set to 0 platform accounts and 0 account-data bindings so questions enter
      the right client-scoped evidence before reusable semantics run.
    business_questions:
    - Which logistics / courier bindings should be traversed for Bear House Clothing Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - logistics_courier
    - runtime_traversal
    included_concepts:
    - 0 platform accounts
    - 0 account-data bindings
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - business_flow_binding_id:business_flow_binding.bear_house_clothing_private_limited.logistics_runtime_resolution
    - runtime_source_family:logistics
    embedding_text: Bear House Clothing Private Limited logistics runtime resolution is Bear House Clothing Private
      Limited's logistics / courier runtime traversal binding. It connects the business scope set to account and
      table bindings so retrieval selects client evidence first and then delegates semantics to external canonical
      packs.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House Clothing Private Limited logistics runtime resolution
    - logistics / courier
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bear_house_clothing_private_limited.logistics_runtime_resolution
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    binding_name: Bear House Clothing Private Limited logistics runtime resolution
    binding_type: logistics_source_resolution
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.logistics
    account_data_binding_ids: []
    participating_accounts: []
    money_flow_paths: []
    deferred_sources:
    - label: Bluedart
      config: Settlement + Invoice (PP Teabox variant)
      reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: GoSwift
      config: Settlement + Invoice
      reason: No GoSwift canonical logistics platform/table cards in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bear House Clothing Private Limited marketplace runtime resolution
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bear House Clothing Private Limited marketplace runtime resolution
    - Bear House Clothing Private Limited marketplace flow
    - marketplace runtime resolution flow
    colloquial_phrases:
    - Bear House Clothing Private Limited marketplace resolution flow
    - marketplace source routing
    - Bear House Clothing Private Limited runtime traversal plan
    business_meaning: Business flow binding for Bear House Clothing Private Limited's marketplace source resolution.
      It connects the scope set to 5 platform accounts and 17 account-data bindings so questions enter the right
      client-scoped evidence before reusable semantics run.
    business_questions:
    - Which marketplace bindings should be traversed for Bear House Clothing Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - marketplace
    - runtime_traversal
    included_concepts:
    - 5 platform accounts
    - 17 account-data bindings
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - business_flow_binding_id:business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
    embedding_text: Bear House Clothing Private Limited marketplace runtime resolution is Bear House Clothing Private
      Limited's marketplace runtime traversal binding. It connects the business scope set to account and table bindings
      so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House Clothing Private Limited marketplace runtime resolution
    - marketplace
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
    source_path: Bear House Clothing Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    business_flow_binding_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    binding_name: Bear House Clothing Private Limited marketplace runtime resolution
    binding_type: marketplace_source_resolution
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.marketplace
    account_data_binding_ids:
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
    - account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
    - account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    - account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
    - account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    - account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    - account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
    - account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
    - account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    - account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
    - account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
    - account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
    - account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
    - account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
    - account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
    - account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
    participating_accounts:
    - platform_account_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
      account_name: Amazon India
    - platform_account_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
      account_name: Flipkart
    - platform_account_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
      account_name: Myntra
    - platform_account_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
      account_name: Ajio
    - platform_account_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
      account_name: Tata Cliq
    money_flow_paths:
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
      source_role: oms_sales
      table_id: table.zs_observe.amazon_oms
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
      source_role: disbursement
      table_id: table.zs_observe.amazon_disbursment
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
      source_role: oms_sales
      table_id: table.zs_recon_processor.flipkart_oms
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
      source_role: settlement
      table_id: table.zs_observe.flipkart_settlement
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
      source_role: commission_fee_invoice
      table_id: table.zs_observe.flipkart_commission
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
      source_role: cashback_credit_debit_note
      table_id: table.zs_observe.flipkart_cashback
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
      source_role: oms_sales
      table_id: table.zs_observe.myntra_oms
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
      source_role: settlement
      table_id: table.zs_observe.myntra_settlement
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
      source_role: non_order_settlement
      table_id: table.zs_observe.myntra_non_order_settlement
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
      source_role: returns
      table_id: table.zs_observe.myntra_reverse
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
      source_role: oms_sales
      table_id: table.zs_observe.ajio_oms
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
      source_role: marketplace_settlement
      table_id: table.zs_observe.ajio_settlement
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
      source_role: returns
      table_id: table.zs_observe.ajio_reverse
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
      source_role: credit_note
      table_id: table.zs_observe.ajio_credit_note
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
      source_role: oms_invoice
      table_id: table.zs_observe.tatacliq_oms
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
      source_role: settlement_payout
      table_id: table.zs_observe.tatacliq_settlement
```

#### business_flow_binding.bear_house_clothing_private_limited.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.bear_house_clothing_private_limited.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bear House Clothing Private Limited OMS runtime resolution flow
  status: review_required
  review_status: review_required
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bear House Clothing Private Limited OMS runtime resolution flow
    - Bear House Clothing Private Limited OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Bear House Clothing Private Limited OMS resolution flow
    - OMS source routing
    - Bear House Clothing Private Limited runtime traversal plan
    business_meaning: Business flow binding for Bear House Clothing Private Limited's OMS source resolution. It
      connects the scope set to 0 platform accounts and 0 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Bear House Clothing Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - OMS
    - runtime_traversal
    included_concepts:
    - 0 platform accounts
    - 0 account-data bindings
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - runtime_source_family:oms
    embedding_text: Bear House Clothing Private Limited OMS runtime resolution flow is Bear House Clothing Private
      Limited's OMS runtime traversal binding. It connects the business scope set to account and table bindings
      so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House Clothing Private Limited OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bear_house_clothing_private_limited.oms_runtime_resolution
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
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.bear_house_clothing_private_limited.oms_runtime_resolution
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    binding_name: Bear House Clothing Private Limited OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.oms
    account_data_binding_ids: []
    participating_accounts: []
    source_flow_paths: []
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bear House Clothing Private Limited WMS runtime resolution
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
    vendor_or_system: Bear House Clothing Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bear House Clothing Private Limited WMS runtime resolution
    - Bear House Clothing Private Limited WMS flow
    - WMS runtime resolution flow
    colloquial_phrases:
    - Bear House Clothing Private Limited WMS resolution flow
    - WMS source routing
    - Bear House Clothing Private Limited runtime traversal plan
    business_meaning: Business flow binding for Bear House Clothing Private Limited's WMS source resolution. It
      connects the scope set to 1 platform accounts and 2 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which WMS bindings should be traversed for Bear House Clothing Private Limited's runtime question?
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
    - tenant_id:tenant.bear_house_clothing_private_limited
    - group_id:group.bear_house_clothing_private_limited.g116.gl330
    - runtime_source_family:wms
    embedding_text: Bear House Clothing Private Limited WMS runtime resolution is Bear House Clothing Private Limited's
      WMS runtime traversal binding. It connects the business scope set to account and table bindings so retrieval
      selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Bear House Clothing Private Limited
    - Bear House Clothing Private Limited WMS runtime resolution
    - WMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
  evidence:
    source_documents:
    - Bear House Clothing Private Limited.docx
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
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    runtime_source_family: wms
    business_flow_binding_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.wms
  fields:
    tenant_id: tenant.bear_house_clothing_private_limited
    group_id: group.bear_house_clothing_private_limited.g116.gl330
    business_flow_binding_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
    business_scope_set_id: business_scope_set.bear_house_clothing_private_limited.wms
    flow_name: Bear House Clothing Private Limited WMS runtime resolution
    flow_type: wms_source_resolution
    platform_account_ids:
    - platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
    account_data_binding_ids:
    - account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    - account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    source_flow_paths:
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
      platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
      source_role: wms_invoice_transaction_ledger
      table_id: table.zs_observe.unicommerce
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
      platform_account_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
      source_role: wms_shipment_tracking
      table_id: table.zs_observe.unicommerce_order_sales_report
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note.account_data_binding_applies_scope_column.column_zs_observe_ajio_credit_note_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note.account_data_binding_applies_scope_column.column_zs_observe_ajio_credit_note_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  target_card_id: column.zs_observe.ajio_credit_note.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note.account_data_binding_applies_scope_column.column_zs_observe_ajio_credit_note_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note.account_data_binding_applies_scope_column.column_zs_observe_ajio_credit_note_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  target_card_id: column.zs_observe.ajio_credit_note.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement.account_data_binding_applies_scope_column.column_zs_observe_ajio_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement.account_data_binding_applies_scope_column.column_zs_observe_ajio_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  target_card_id: column.zs_observe.ajio_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement.account_data_binding_applies_scope_column.column_zs_observe_ajio_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement.account_data_binding_applies_scope_column.column_zs_observe_ajio_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  target_card_id: column.zs_observe.ajio_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms.account_data_binding_applies_scope_column.column_zs_observe_ajio_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms.account_data_binding_applies_scope_column.column_zs_observe_ajio_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  target_card_id: column.zs_observe.ajio_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms.account_data_binding_applies_scope_column.column_zs_observe_ajio_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms.account_data_binding_applies_scope_column.column_zs_observe_ajio_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  target_card_id: column.zs_observe.ajio_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse.account_data_binding_applies_scope_column.column_zs_observe_ajio_reverse_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse.account_data_binding_applies_scope_column.column_zs_observe_ajio_reverse_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  target_card_id: column.zs_observe.ajio_reverse.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse.account_data_binding_applies_scope_column.column_zs_observe_ajio_reverse_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse.account_data_binding_applies_scope_column.column_zs_observe_ajio_reverse_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  target_card_id: column.zs_observe.ajio_reverse.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: column.zs_observe.amazon_disbursment.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: column.zs_observe.amazon_disbursment.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: column.zs_observe.flipkart_cashback.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: column.zs_observe.flipkart_cashback.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: column.zs_observe.flipkart_commission.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: column.zs_observe.flipkart_commission.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: column.zs_recon_processor.flipkart_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: column.zs_recon_processor.flipkart_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: column.zs_observe.flipkart_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: column.zs_observe.flipkart_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: column.zs_observe.myntra_non_order_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: column.zs_observe.myntra_non_order_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: column.zs_observe.myntra_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: column.zs_observe.myntra_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  target_card_id: column.zs_observe.myntra_reverse.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  target_card_id: column.zs_observe.myntra_reverse.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: column.zs_observe.myntra_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: column.zs_observe.myntra_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: column.zs_observe.unicommerce.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '330'
```

#### edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_order_sales_report_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_order_sales_report_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '330'
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  target_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  target_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  target_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  target_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  target_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  target_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  target_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_belongs_to_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note.account_data_binding_binds_to_table.table_zs_observe_ajio_credit_note

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note.account_data_binding_binds_to_table.table_zs_observe_ajio_credit_note
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  target_card_id: table.zs_observe.ajio_credit_note
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement.account_data_binding_binds_to_table.table_zs_observe_ajio_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement.account_data_binding_binds_to_table.table_zs_observe_ajio_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  target_card_id: table.zs_observe.ajio_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms.account_data_binding_binds_to_table.table_zs_observe_ajio_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms.account_data_binding_binds_to_table.table_zs_observe_ajio_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  target_card_id: table.zs_observe.ajio_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse.account_data_binding_binds_to_table.table_zs_observe_ajio_reverse

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse.account_data_binding_binds_to_table.table_zs_observe_ajio_reverse
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  target_card_id: table.zs_observe.ajio_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_binds_to_table.table_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_binds_to_table.table_zs_observe_amazon_disbursment
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: table.zs_observe.amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: table.zs_observe.amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_binds_to_table.table_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_binds_to_table.table_zs_observe_flipkart_cashback
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: table.zs_observe.flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_binds_to_table.table_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_binds_to_table.table_zs_observe_flipkart_commission
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: table.zs_observe.flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_binds_to_table.table_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_binds_to_table.table_zs_recon_processor_flipkart_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: table.zs_recon_processor.flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_binds_to_table.table_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_binds_to_table.table_zs_observe_flipkart_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: table.zs_observe.flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_non_order_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: table.zs_observe.myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_binds_to_table.table_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_binds_to_table.table_zs_observe_myntra_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: table.zs_observe.myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse.account_data_binding_binds_to_table.table_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse.account_data_binding_binds_to_table.table_zs_observe_myntra_reverse
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  target_card_id: table.zs_observe.myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: table.zs_observe.myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_binds_to_table.table_zs_observe_tatacliq_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_binds_to_table.table_zs_observe_tatacliq_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  target_card_id: table.zs_observe.tatacliq_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_binds_to_table.table_zs_observe_tatacliq_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_binds_to_table.table_zs_observe_tatacliq_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  target_card_id: table.zs_observe.tatacliq_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_binds_to_table.table_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_binds_to_table.table_zs_observe_unicommerce
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: table.zs_observe.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_binds_to_table.table_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_binds_to_table.table_zs_observe_unicommerce_order_sales_report
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: table.zs_observe.unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_bear_house_clothing_private_limited_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.logistics_runtime_resolution
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.oms_runtime_resolution
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
  target_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
  target_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_bear_house_clothing_private_limited_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bear_house_clothing_private_limited_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bear_house_clothing_private_limited_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.logistics_runtime_resolution
  target_card_id: business_scope_set.bear_house_clothing_private_limited.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bear_house_clothing_private_limited_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bear_house_clothing_private_limited_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  target_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bear_house_clothing_private_limited_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bear_house_clothing_private_limited_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.oms_runtime_resolution
  target_card_id: business_scope_set.bear_house_clothing_private_limited.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bear_house_clothing_private_limited_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bear_house_clothing_private_limited_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
  target_card_id: business_scope_set.bear_house_clothing_private_limited.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_bear_house_clothing_private_limited_logistics.business_scope_set_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_logistics.business_scope_set_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bear_house_clothing_private_limited.logistics
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_oms.business_scope_set_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_oms.business_scope_set_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bear_house_clothing_private_limited.oms
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bear_house_clothing_private_limited.wms
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.wms
  target_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bear_house_clothing_private_limited.wms
  target_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_ajio

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_ajio
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform.ajio
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_amazon
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_flipkart

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_flipkart
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform.flipkart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_myntra

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_myntra
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform.myntra
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_tatacliq

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform.platform_tatacliq
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform.tatacliq
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_platform.platform_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_platform.platform_unicommerce
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bear_house_clothing_private_limited.wms
  target_card_id: platform.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.wms
  target_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_ajio_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_ajio_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_context.ajio.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_flipkart_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_flipkart_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_context.flipkart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_myntra_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_myntra_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_context.myntra.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_tatacliq_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_marketplace.business_scope_set_includes_platform_context.platform_context_tatacliq_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  target_card_id: platform_context.tatacliq.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_platform_context.platform_context_unicommerce_in_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bear_house_clothing_private_limited_wms.business_scope_set_includes_platform_context.platform_context_unicommerce_in_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bear_house_clothing_private_limited.wms
  target_card_id: platform_context.unicommerce.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_belongs_to_tenant.tenant_bear_house_clothing_private_limited

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_belongs_to_tenant.tenant_bear_house_clothing_private_limited
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: tenant.bear_house_clothing_private_limited
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_flow_binding.business_flow_binding_bear_house_clothing_private_limited_logistics_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_flow_binding.business_flow_binding_bear_house_clothing_private_limited_logistics_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: business_flow_binding.bear_house_clothing_private_limited.logistics_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_flow_binding.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_flow_binding.business_flow_binding_bear_house_clothing_private_limited_marketplace_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: business_flow_binding.bear_house_clothing_private_limited.marketplace_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_flow_binding.business_flow_binding_bear_house_clothing_private_limited_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_flow_binding.business_flow_binding_bear_house_clothing_private_limited_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: business_flow_binding.bear_house_clothing_private_limited.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_flow_binding.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_flow_binding.business_flow_binding_bear_house_clothing_private_limited_wms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: business_flow_binding.bear_house_clothing_private_limited.wms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_scope_set.business_scope_set_bear_house_clothing_private_limited_logistics

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_scope_set.business_scope_set_bear_house_clothing_private_limited_logistics
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: business_scope_set.bear_house_clothing_private_limited.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_scope_set.business_scope_set_bear_house_clothing_private_limited_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_scope_set.business_scope_set_bear_house_clothing_private_limited_marketplace
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: business_scope_set.bear_house_clothing_private_limited.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_scope_set.business_scope_set_bear_house_clothing_private_limited_oms

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_scope_set.business_scope_set_bear_house_clothing_private_limited_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: business_scope_set.bear_house_clothing_private_limited.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_scope_set.business_scope_set_bear_house_clothing_private_limited_wms

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_business_scope_set.business_scope_set_bear_house_clothing_private_limited_wms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: business_scope_set.bear_house_clothing_private_limited.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_ajio_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_flipkart_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_myntra_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.group_bear_house_clothing_private_limited_g116_gl330.group_has_platform_account.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bear_house_clothing_private_limited.g116.gl330
  target_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_belongs_to_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_credit_note_zs_observe_ajio_credit_note
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.credit_note.zs_observe_ajio_credit_note
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_marketplace_settlement_zs_observe_ajio_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.marketplace_settlement.zs_observe_ajio_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_oms_sales_zs_observe_ajio_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.oms_sales.zs_observe_ajio_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_ajio_returns_zs_observe_ajio_reverse
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.ajio.returns.zs_observe_ajio_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_returns_zs_observe_myntra_reverse
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_myntra_settlement_zs_observe_myntra_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_oms_invoice_zs_observe_tatacliq_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  target_card_id: account_data_binding.bear_house_clothing_private_limited.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  target_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_bear_house_clothing_private_limited_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  target_card_id: account_data_binding.bear_house_clothing_private_limited.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_uses_platform.platform_ajio

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_uses_platform.platform_ajio
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  target_card_id: platform.ajio
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_uses_platform.platform_flipkart

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_uses_platform.platform_flipkart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  target_card_id: platform.flipkart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_uses_platform.platform_myntra

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_uses_platform.platform_myntra
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  target_card_id: platform.myntra
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_uses_platform.platform_tatacliq

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_uses_platform.platform_tatacliq
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  target_card_id: platform.tatacliq
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_uses_platform.platform_unicommerce

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_uses_platform.platform_unicommerce
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  target_card_id: platform.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_uses_platform_context.platform_context_ajio_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_ajio_marketplace.platform_account_uses_platform_context.platform_context_ajio_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bear_house_clothing_private_limited.ajio.marketplace
  target_card_id: platform_context.ajio.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_uses_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_amazon_india_marketplace.platform_account_uses_platform_context.platform_context_amazon_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bear_house_clothing_private_limited.amazon_india.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_uses_platform_context.platform_context_flipkart_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_flipkart_marketplace.platform_account_uses_platform_context.platform_context_flipkart_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bear_house_clothing_private_limited.flipkart.marketplace
  target_card_id: platform_context.flipkart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_uses_platform_context.platform_context_myntra_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_myntra_marketplace.platform_account_uses_platform_context.platform_context_myntra_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bear_house_clothing_private_limited.myntra.marketplace
  target_card_id: platform_context.myntra.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_uses_platform_context.platform_context_tatacliq_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_tata_cliq_marketplace.platform_account_uses_platform_context.platform_context_tatacliq_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bear_house_clothing_private_limited.tata_cliq.marketplace
  target_card_id: platform_context.tatacliq.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_uses_platform_context.platform_context_unicommerce_in_wms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bear_house_clothing_private_limited_unicommerce_wms_wms.platform_account_uses_platform_context.platform_context_unicommerce_in_wms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bear_house_clothing_private_limited.unicommerce_wms.wms
  target_card_id: platform_context.unicommerce.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### TENANT_HAS_GROUP

#### edge.tenant_bear_house_clothing_private_limited.tenant_has_group.group_bear_house_clothing_private_limited_g116_gl330

```yaml
canonical_edge:
  edge_id: edge.tenant_bear_house_clothing_private_limited.tenant_has_group.group_bear_house_clothing_private_limited_g116_gl330
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.bear_house_clothing_private_limited
  target_card_id: group.bear_house_clothing_private_limited.g116.gl330
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```
