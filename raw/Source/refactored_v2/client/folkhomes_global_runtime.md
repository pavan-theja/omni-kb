# Folkhomes Global — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `folkhomes_global_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources: []
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 7
  account_data_binding: 8
  business_scope_set: 2
  business_flow_binding: 2
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 16
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 8
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 8
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 2
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 8
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 7
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 2
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 2
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 8
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 4
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 7
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 4
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 2
  GROUP_HAS_BUSINESS_SCOPE_SET: 2
  GROUP_HAS_PLATFORM_ACCOUNT: 7
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 7
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 8
  PLATFORM_ACCOUNT_USES_PLATFORM: 7
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 7
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
wms_integration:
  source_packs:
  - increff_wms.md
  - unicommerce_wms.md
  added_runtime_cards: 0
  added_runtime_edges: 0
  supported_wms_accounts: 0
  supported_wms_bindings: 0
  resolved_deferred_mentions: 0
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

#### tenant.folkhomes_global

```yaml
canonical_card:
  canonical_id: tenant.folkhomes_global
  card_type: tenant
  canonical_name: Folkhomes Global
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
    vendor_or_system: Folkhomes Global
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Folkhomes Global
    - folkhomes_global
    - Folkhomes Global runtime tenant
    colloquial_phrases:
    - Folkhomes Global client runtime
    - Folkhomes Global source configuration
    - Folkhomes Global scoped reconciliation setup
    business_meaning: Runtime tenant identity for Folkhomes Global. It anchors the client's marketplace, logistics,
      OMS, WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from reusable domain
      semantics.
    business_questions:
    - Which source families and configured accounts belong to Folkhomes Global?
    - Which group and account bindings should constrain Folkhomes Global's SQL handoff?
    - After Folkhomes Global's runtime scope is resolved, which domain layer should receive the query next?
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
    - tenant_id:tenant.folkhomes_global
    embedding_text: Folkhomes Global is the runtime tenant root for the client's marketplace, logistics, OMS, WMS,
      payment-gateway, and bank-statement configuration. Use it to reach group, platform-account, and account-data-binding
      nodes before invoking reusable canonical packs.
    search_keywords:
    - Folkhomes Global
    - folkhomes_global
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.folkhomes_global
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
  fields:
    tenant_slug: folkhomes_global
    tenant_name: Folkhomes Global
    legal_name: Folkhomes Global
    active: true
```

### 2.2 Group Cards

#### group.folkhomes_global.g8.gl123

```yaml
canonical_card:
  canonical_id: group.folkhomes_global.g8.gl123
  card_type: group
  canonical_name: Folkhomes Global group 8/123
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
    vendor_or_system: Folkhomes Global
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mensa Brands
    - Folkhomes Global group 8/123
    - group_id 8
    - group_level_id 123
    colloquial_phrases:
    - Folkhomes Global group scope
    - Mensa Brands runtime scope
    - group 8 level 123 query boundary
    business_meaning: 'Runtime group scope for Folkhomes Global: group_id=8 and group_level_id=123. It is the client-specific
      filter boundary that must be applied before resolving account bindings for US in USD.'
    business_questions:
    - Which bindings use group_id=8 and group_level_id=123?
    - Which source families are active under Mensa Brands?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - group_id_value:8
    - group_level_id_value:123
    embedding_text: Mensa Brands is the runtime group node for Folkhomes Global. Apply group_id=8 and group_level_id=123
      when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Folkhomes Global
    - Mensa Brands
    - group_id 8
    - group_level_id 123
    - runtime group scope
    exact_match_keys:
    - group.folkhomes_global.g8.gl123
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    group_level_id: '123'
  fields:
    tenant_id: tenant.folkhomes_global
    group_id_value: '8'
    group_level_id_value: '123'
    group_name: Mensa Brands
    default_currency: USD
    country: US
```

### 2.3 Platform Account Cards

#### platform_account.folkhomes_global.amazon_amazon_returns.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  card_type: platform_account
  canonical_name: Folkhomes Global — Amazon amazon_returns
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
    - Amazon amazon_returns
    - Folkhomes Global Amazon amazon_returns
    - Amazon
    - Amazon amazon_returns marketplace account
    colloquial_phrases:
    - Folkhomes Global Amazon amazon_returns source account
    - Amazon amazon_returns marketplace runtime account
    - Amazon amazon_returns configured source family
    business_meaning: Runtime platform account for Folkhomes Global's Amazon amazon_returns marketplace sources.
      It points traversal to platform.amazon and platform_context.amazon.international and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon amazon_returns table bindings are available for Folkhomes Global?
    - Which canonical platform/context should Folkhomes Global's Amazon amazon_returns questions traverse through?
    - Which source roles under Amazon amazon_returns are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Includes return reason codes, refund amt'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon amazon_returns
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.folkhomes_global.amazon_amazon_returns.marketplace
    embedding_text: Folkhomes Global's Amazon amazon_returns platform account routes marketplace questions to platform.amazon
      / platform_context.amazon.international. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Folkhomes Global
    - Amazon amazon_returns
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon amazon_returns
    account_type: marketplace_seller_account
    source_account_identifier: Amazon amazon_returns
    active: true
    configured_source_description: Includes return reason codes, refund amt
```

#### platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  card_type: platform_account
  canonical_name: Folkhomes Global — Amazon US, UK, MX, CA
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
    - Amazon US, UK, MX, CA
    - Folkhomes Global Amazon US, UK, MX, CA
    - Amazon
    - Amazon US, UK, MX, CA marketplace account
    colloquial_phrases:
    - Folkhomes Global Amazon US, UK, MX, CA source account
    - Amazon US, UK, MX, CA marketplace runtime account
    - Amazon US, UK, MX, CA configured source family
    business_meaning: Runtime platform account for Folkhomes Global's Amazon US, UK, MX, CA marketplace sources.
      It points traversal to platform.amazon and platform_context.amazon.international and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon US, UK, MX, CA table bindings are available for Folkhomes Global?
    - Which canonical platform/context should Folkhomes Global's Amazon US, UK, MX, CA questions traverse through?
    - Which source roles under Amazon US, UK, MX, CA are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: amazon_settlement (per country)'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon US, UK, MX, CA
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
    embedding_text: Folkhomes Global's Amazon US, UK, MX, CA platform account routes marketplace questions to platform.amazon
      / platform_context.amazon.international. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Folkhomes Global
    - Amazon US, UK, MX, CA
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon US, UK, MX, CA
    account_type: marketplace_seller_account
    source_account_identifier: Amazon US, UK, MX, CA
    active: true
    configured_source_description: amazon_settlement (per country)
```

#### platform_account.folkhomes_global.shopify_d2c.oms

```yaml
canonical_card:
  canonical_id: platform_account.folkhomes_global.shopify_d2c.oms
  card_type: platform_account
  canonical_name: Folkhomes Global Shopify D2C OMS account
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
    vendor_or_system: Folkhomes Global
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Folkhomes Global Shopify D2C OMS account
    - Folkhomes Global Folkhomes Global Shopify D2C OMS account
    - Shopify
    - Folkhomes Global Shopify D2C OMS account OMS account
    colloquial_phrases:
    - Folkhomes Global Folkhomes Global Shopify D2C OMS account source account
    - Folkhomes Global Shopify D2C OMS account OMS runtime account
    - Folkhomes Global Shopify D2C OMS account configured source family
    business_meaning: Runtime platform account for Folkhomes Global's Folkhomes Global Shopify D2C OMS account OMS
      sources. It points traversal to platform.shopify and platform_context.shopify.in.d2c_oms and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Folkhomes Global Shopify D2C OMS account table bindings are available for Folkhomes Global?
    - Which canonical platform/context should Folkhomes Global's Folkhomes Global Shopify D2C OMS account questions
      traverse through?
    - Which source roles under Folkhomes Global Shopify D2C OMS account are active or review-required for this client?
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - runtime_source_family:oms
    embedding_text: Folkhomes Global's Folkhomes Global Shopify D2C OMS account platform account routes OMS questions
      to platform.shopify / platform_context.shopify.in.d2c_oms. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Folkhomes Global
    - Folkhomes Global Shopify D2C OMS account
    - Shopify
    - OMS
    - platform.shopify
    - platform_context.shopify.in.d2c_oms
    exact_match_keys:
    - platform_account.folkhomes_global.shopify_d2c.oms
  evidence:
    source_documents:
    - Folkhomes Global.docx
    - shopify_d2c_oms.md
    source_path: Folkhomes Global.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    runtime_source_family: oms
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_name: Folkhomes Global Shopify D2C OMS account
    account_type: d2c_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Shopify D2C OMS and returns/refund events
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: shopify_pack_exposes_in_context_non_in_client_review_currency_and_country_before_production
    group_scope_values:
      group_id: '8'
      group_level_id: '123'
```

#### platform_account.folkhomes_global.target_target_returns.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.folkhomes_global.target_target_returns.marketplace
  card_type: platform_account
  canonical_name: Folkhomes Global — Target target_returns
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target target_returns
    - Folkhomes Global Target target_returns
    - Target Plus
    - Target target_returns marketplace account
    colloquial_phrases:
    - Folkhomes Global Target target_returns source account
    - Target target_returns marketplace runtime account
    - Target target_returns configured source family
    business_meaning: Runtime platform account for Folkhomes Global's Target target_returns marketplace sources.
      It points traversal to platform.target_plus and platform_context.target_plus.us and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Target target_returns table bindings are available for Folkhomes Global?
    - Which canonical platform/context should Folkhomes Global's Target target_returns questions traverse through?
    - Which source roles under Target target_returns are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Includes return reason codes, refund amt'
    - platform.target_plus
    - platform_context.target_plus.us
    - Target target_returns
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - platform_account_id:platform_account.folkhomes_global.target_target_returns.marketplace
    embedding_text: Folkhomes Global's Target target_returns platform account routes marketplace questions to platform.target_plus
      / platform_context.target_plus.us. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Folkhomes Global
    - Target target_returns
    - Target Plus
    - marketplace
    - platform.target_plus
    - platform_context.target_plus.us
    exact_match_keys:
    - platform_account.folkhomes_global.target_target_returns.marketplace
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    platform_account_id: platform_account.folkhomes_global.target_target_returns.marketplace
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_name: Target target_returns
    account_type: marketplace_seller_account
    source_account_identifier: Target target_returns
    active: true
    configured_source_description: Includes return reason codes, refund amt
```

#### platform_account.folkhomes_global.target_us.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.folkhomes_global.target_us.marketplace
  card_type: platform_account
  canonical_name: Folkhomes Global — Target US
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target US
    - Folkhomes Global Target US
    - Target Plus
    - Target US marketplace account
    colloquial_phrases:
    - Folkhomes Global Target US source account
    - Target US marketplace runtime account
    - Target US configured source family
    business_meaning: Runtime platform account for Folkhomes Global's Target US marketplace sources. It points traversal
      to platform.target_plus and platform_context.target_plus.us and groups the client's table-level account-data
      bindings for this source.
    business_questions:
    - Which Target US table bindings are available for Folkhomes Global?
    - Which canonical platform/context should Folkhomes Global's Target US questions traverse through?
    - Which source roles under Target US are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: target_settlement'
    - platform.target_plus
    - platform_context.target_plus.us
    - Target US
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - platform_account_id:platform_account.folkhomes_global.target_us.marketplace
    embedding_text: Folkhomes Global's Target US platform account routes marketplace questions to platform.target_plus
      / platform_context.target_plus.us. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Folkhomes Global
    - Target US
    - Target Plus
    - marketplace
    - platform.target_plus
    - platform_context.target_plus.us
    exact_match_keys:
    - platform_account.folkhomes_global.target_us.marketplace
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    platform_account_id: platform_account.folkhomes_global.target_us.marketplace
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_name: Target US
    account_type: marketplace_seller_account
    source_account_identifier: Target US
    active: true
    configured_source_description: target_settlement
```

#### platform_account.folkhomes_global.walmart.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.folkhomes_global.walmart.marketplace
  card_type: platform_account
  canonical_name: Folkhomes Global — Walmart —
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart —
    - Folkhomes Global Walmart —
    - Walmart
    - Walmart — marketplace account
    colloquial_phrases:
    - Folkhomes Global Walmart — source account
    - Walmart — marketplace runtime account
    - Walmart — configured source family
    business_meaning: Runtime platform account for Folkhomes Global's Walmart — marketplace sources. It points traversal
      to platform.walmart and platform_context.walmart.us and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Walmart — table bindings are available for Folkhomes Global?
    - Which canonical platform/context should Folkhomes Global's Walmart — questions traverse through?
    - Which source roles under Walmart — are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Returns embedded in walmart_settlement'
    - platform.walmart
    - platform_context.walmart.us
    - Walmart —
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - platform_account_id:platform_account.folkhomes_global.walmart.marketplace
    embedding_text: Folkhomes Global's Walmart — platform account routes marketplace questions to platform.walmart
      / platform_context.walmart.us. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Folkhomes Global
    - Walmart —
    - Walmart
    - marketplace
    - platform.walmart
    - platform_context.walmart.us
    exact_match_keys:
    - platform_account.folkhomes_global.walmart.marketplace
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    platform_account_id: platform_account.folkhomes_global.walmart.marketplace
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_name: Walmart —
    account_type: marketplace_seller_account
    source_account_identifier: Walmart —
    active: true
    configured_source_description: Returns embedded in walmart_settlement
```

#### platform_account.folkhomes_global.walmart_us.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.folkhomes_global.walmart_us.marketplace
  card_type: platform_account
  canonical_name: Folkhomes Global — Walmart US
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart US
    - Folkhomes Global Walmart US
    - Walmart
    - Walmart US marketplace account
    colloquial_phrases:
    - Folkhomes Global Walmart US source account
    - Walmart US marketplace runtime account
    - Walmart US configured source family
    business_meaning: Runtime platform account for Folkhomes Global's Walmart US marketplace sources. It points
      traversal to platform.walmart and platform_context.walmart.us and groups the client's table-level account-data
      bindings for this source.
    business_questions:
    - Which Walmart US table bindings are available for Folkhomes Global?
    - Which canonical platform/context should Folkhomes Global's Walmart US questions traverse through?
    - Which source roles under Walmart US are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: walmart_settlement'
    - platform.walmart
    - platform_context.walmart.us
    - Walmart US
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - platform_account_id:platform_account.folkhomes_global.walmart_us.marketplace
    embedding_text: Folkhomes Global's Walmart US platform account routes marketplace questions to platform.walmart
      / platform_context.walmart.us. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Folkhomes Global
    - Walmart US
    - Walmart
    - marketplace
    - platform.walmart
    - platform_context.walmart.us
    exact_match_keys:
    - platform_account.folkhomes_global.walmart_us.marketplace
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    platform_account_id: platform_account.folkhomes_global.walmart_us.marketplace
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_name: Walmart US
    account_type: marketplace_seller_account
    source_account_identifier: Walmart US
    active: true
    configured_source_description: walmart_settlement
```

### 2.4 Account Data Binding Cards

#### account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  card_type: account_data_binding
  canonical_name: Folkhomes Global — Amazon amazon_returns — returns
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
    - Amazon returns
    - amazon_returns
    - zs_observe.amazon_returns
    - Includes return reason codes, refund amt
    - Folkhomes Global Amazon returns
    colloquial_phrases:
    - Folkhomes Global Amazon returns source
    - Amazon returns runtime binding
    - amazon_returns for Folkhomes Global
    business_meaning: This account-data binding tells the resolver that Folkhomes Global's Amazon returns evidence
      should use zs_observe.amazon_returns. Apply group_id=8, group_level_id=123 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Amazon returns file/table is active for Folkhomes Global?
    - Which group filters keep amazon_returns limited to Folkhomes Global?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - returns
    included_concepts:
    - zs_observe.amazon_returns
    - returns
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.amazon_amazon_returns.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:returns
    - table_id:table.zs_observe.amazon_returns
    embedding_text: 'For Folkhomes Global, the Amazon returns binding selects zs_observe.amazon_returns as marketplace
      evidence. Scope: group_id=8, group_level_id=123. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Folkhomes Global
    - Amazon
    - returns
    - marketplace
    - zs_observe.amazon_returns
    - amazon_returns
    - uploaded marketplace canonical pack
    - group_id=8
    - group_level_id=123
    exact_match_keys:
    - account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
    table_id: table.zs_observe.amazon_returns
    source_role: returns
  fields:
    platform_account_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
    table_id: table.zs_observe.amazon_returns
    source_role: returns
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '123'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_returns.group_level_id
      runtime_value: '123'
    active: true
    source_configuration_text: Includes return reason codes, refund amt
```

#### account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Folkhomes Global — Amazon US, UK, MX, CA — settlement
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
    - amazon_settlement (per country)
    - Folkhomes Global Amazon settlement
    colloquial_phrases:
    - Folkhomes Global Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Folkhomes Global
    business_meaning: This account-data binding tells the resolver that Folkhomes Global's Amazon settlement evidence
      should use zs_observe.amazon_settlement. Apply group_id=8, group_level_id=123 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Folkhomes Global?
    - Which group filters keep amazon_settlement limited to Folkhomes Global?
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
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Folkhomes Global, the Amazon settlement binding selects zs_observe.amazon_settlement as
      marketplace evidence. Scope: group_id=8, group_level_id=123. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Folkhomes Global
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=8
    - group_level_id=123
    exact_match_keys:
    - account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '123'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '123'
    active: true
    source_configuration_text: amazon_settlement (per country)
```

#### account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  card_type: account_data_binding
  canonical_name: Folkhomes Global Shopify D2C OMS oms_sales binding
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
    vendor_or_system: Folkhomes Global
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
    - Folkhomes Global Shopify D2C OMS OMS sales
    colloquial_phrases:
    - Folkhomes Global Shopify D2C OMS OMS sales source
    - Shopify D2C OMS OMS sales runtime binding
    - shopify_oms for Folkhomes Global
    business_meaning: This account-data binding tells the resolver that Folkhomes Global's Shopify D2C OMS OMS sales
      evidence should use zs_observe.shopify_oms. Apply group_id=8, group_level_id=123 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Folkhomes Global's OMS sales question?
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
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:oms_sales
    - table_id:table.zs_observe.shopify_oms
    - runtime_source_family:oms
    embedding_text: 'For Folkhomes Global, the Shopify D2C OMS OMS sales binding selects zs_observe.shopify_oms
      as OMS evidence. Scope: group_id=8, group_level_id=123. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Folkhomes Global
    - Shopify D2C OMS
    - OMS sales
    - OMS
    - zs_observe.shopify_oms
    - shopify_oms
    - oms_sales
    - shopify_d2c_oms.md
    - group_id=8
    - group_level_id=123
    exact_match_keys:
    - account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  evidence:
    source_documents:
    - Folkhomes Global.docx
    - shopify_d2c_oms.md
    source_path: Folkhomes Global.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.folkhomes_global.shopify_d2c.oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    source_entity: Shopify D2C OMS
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '8'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.shopify_oms.group_id
      runtime_value: '8'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '123'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shopify_oms.group_level_id
      runtime_value: '123'
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Shopify D2C OMS and returns/refund events
    canonical_table_coverage_status: active
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: shopify_pack_exposes_in_context_non_in_client_review_currency_and_country_before_production
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  card_type: account_data_binding
  canonical_name: Folkhomes Global Shopify D2C OMS returns binding
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
    vendor_or_system: Folkhomes Global
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
    - Folkhomes Global Shopify D2C OMS returns
    colloquial_phrases:
    - Folkhomes Global Shopify D2C OMS returns source
    - Shopify D2C OMS returns runtime binding
    - shopify_returns for Folkhomes Global
    business_meaning: This account-data binding tells the resolver that Folkhomes Global's Shopify D2C OMS returns
      evidence should use zs_observe.shopify_returns. Apply group_id=8, group_level_id=123 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Folkhomes Global's returns question?
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
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:returns
    - table_id:table.zs_observe.shopify_returns
    - runtime_source_family:oms
    embedding_text: 'For Folkhomes Global, the Shopify D2C OMS returns binding selects zs_observe.shopify_returns
      as OMS evidence. Scope: group_id=8, group_level_id=123. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Folkhomes Global
    - Shopify D2C OMS
    - returns
    - OMS
    - zs_observe.shopify_returns
    - shopify_returns
    - shopify_d2c_oms.md
    - group_id=8
    - group_level_id=123
    exact_match_keys:
    - account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  evidence:
    source_documents:
    - Folkhomes Global.docx
    - shopify_d2c_oms.md
    source_path: Folkhomes Global.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
    domain_id: domain.shopify.refunds_returns
    table_id: table.zs_observe.shopify_returns
    source_role: returns
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.folkhomes_global.shopify_d2c.oms
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
    context_fit_status: shopify_pack_exposes_in_context_non_in_client_review_currency_and_country_before_production
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  card_type: account_data_binding
  canonical_name: Folkhomes Global — Target target_returns — returns
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target Plus returns
    - target_returns
    - zs_observe.target_returns
    - Includes return reason codes, refund amt
    - Folkhomes Global Target Plus returns
    colloquial_phrases:
    - Folkhomes Global Target Plus returns source
    - Target Plus returns runtime binding
    - target_returns for Folkhomes Global
    business_meaning: This account-data binding tells the resolver that Folkhomes Global's Target Plus returns evidence
      should use zs_observe.target_returns. Apply group_id=8, group_level_id=123 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Target Plus returns file/table is active for Folkhomes Global?
    - Which group filters keep target_returns limited to Folkhomes Global?
    - What Target Plus canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - returns
    included_concepts:
    - zs_observe.target_returns
    - returns
    - Target Plus
    - marketplace source role
    - client-scoped marketplace table
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.target_target_returns.marketplace
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - source_role:returns
    - table_id:table.zs_observe.target_returns
    embedding_text: 'For Folkhomes Global, the Target Plus returns binding selects zs_observe.target_returns as
      marketplace evidence. Scope: group_id=8, group_level_id=123. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Folkhomes Global
    - Target Plus
    - returns
    - marketplace
    - zs_observe.target_returns
    - target_returns
    - uploaded marketplace canonical pack
    - group_id=8
    - group_level_id=123
    exact_match_keys:
    - account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.target_target_returns.marketplace
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_data_binding_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
    table_id: table.zs_observe.target_returns
    source_role: returns
  fields:
    platform_account_id: platform_account.folkhomes_global.target_target_returns.marketplace
    table_id: table.zs_observe.target_returns
    source_role: returns
    source_entity: Target Plus
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '123'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.target_returns.group_level_id
      runtime_value: '123'
    active: true
    source_configuration_text: Includes return reason codes, refund amt
```

#### account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  card_type: account_data_binding
  canonical_name: Folkhomes Global — Target US — settlement
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target Plus settlement
    - target_settlement
    - zs_observe.target_settlement
    - Folkhomes Global Target Plus settlement
    colloquial_phrases:
    - Folkhomes Global Target Plus settlement source
    - Target Plus settlement runtime binding
    - target_settlement for Folkhomes Global
    business_meaning: This account-data binding tells the resolver that Folkhomes Global's Target Plus settlement
      evidence should use zs_observe.target_settlement. Apply group_id=8, group_level_id=123 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Target Plus settlement file/table is active for Folkhomes Global?
    - Which group filters keep target_settlement limited to Folkhomes Global?
    - What Target Plus canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.target_settlement
    - settlement
    - Target Plus
    - marketplace source role
    - client-scoped marketplace table
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.target_us.marketplace
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - source_role:settlement
    - table_id:table.zs_observe.target_settlement
    embedding_text: 'For Folkhomes Global, the Target Plus settlement binding selects zs_observe.target_settlement
      as marketplace evidence. Scope: group_id=8, group_level_id=123. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Folkhomes Global
    - Target Plus
    - settlement
    - marketplace
    - zs_observe.target_settlement
    - target_settlement
    - uploaded marketplace canonical pack
    - group_id=8
    - group_level_id=123
    exact_match_keys:
    - account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.target_us.marketplace
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_data_binding_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
    table_id: table.zs_observe.target_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.folkhomes_global.target_us.marketplace
    table_id: table.zs_observe.target_settlement
    source_role: settlement
    source_entity: Target Plus
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '123'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.target_settlement.group_level_id
      runtime_value: '123'
    active: true
    source_configuration_text: target_settlement
```

#### account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  card_type: account_data_binding
  canonical_name: Folkhomes Global — Walmart — — marketplace_settlement
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart Marketplace marketplace settlement
    - walmart_settlement
    - zs_observe.walmart_settlement
    - Returns embedded in walmart_settlement
    - Folkhomes Global Walmart Marketplace marketplace settlement
    colloquial_phrases:
    - Folkhomes Global Walmart Marketplace marketplace settlement source
    - Walmart Marketplace marketplace settlement runtime binding
    - walmart_settlement for Folkhomes Global
    business_meaning: This account-data binding tells the resolver that Folkhomes Global's Walmart Marketplace marketplace
      settlement evidence should use zs_observe.walmart_settlement. Apply group_id=8, group_level_id=123 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Walmart Marketplace marketplace settlement file/table is active for Folkhomes Global?
    - Which group filters keep walmart_settlement limited to Folkhomes Global?
    - What Walmart Marketplace canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - marketplace_settlement
    included_concepts:
    - zs_observe.walmart_settlement
    - marketplace settlement
    - Walmart Marketplace
    - marketplace source role
    - client-scoped marketplace table
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.walmart.marketplace
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - source_role:marketplace_settlement
    - table_id:table.zs_observe.walmart_settlement
    embedding_text: 'For Folkhomes Global, the Walmart Marketplace marketplace settlement binding selects zs_observe.walmart_settlement
      as marketplace evidence. Scope: group_id=8, group_level_id=123. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Folkhomes Global
    - Walmart Marketplace
    - marketplace settlement
    - marketplace
    - zs_observe.walmart_settlement
    - walmart_settlement
    - marketplace_settlement
    - uploaded marketplace canonical pack
    - group_id=8
    - group_level_id=123
    exact_match_keys:
    - account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.walmart.marketplace
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_data_binding_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
    table_id: table.zs_observe.walmart_settlement
    source_role: marketplace_settlement
  fields:
    platform_account_id: platform_account.folkhomes_global.walmart.marketplace
    table_id: table.zs_observe.walmart_settlement
    source_role: marketplace_settlement
    source_entity: Walmart Marketplace
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '123'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.walmart_settlement.group_level_id
      runtime_value: '123'
    active: true
    source_configuration_text: Returns embedded in walmart_settlement
```

#### account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  card_type: account_data_binding
  canonical_name: Folkhomes Global — Walmart US — marketplace_settlement
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart Marketplace marketplace settlement
    - walmart_settlement
    - zs_observe.walmart_settlement
    - Folkhomes Global Walmart Marketplace marketplace settlement
    colloquial_phrases:
    - Folkhomes Global Walmart Marketplace marketplace settlement source
    - Walmart Marketplace marketplace settlement runtime binding
    - walmart_settlement for Folkhomes Global
    business_meaning: This account-data binding tells the resolver that Folkhomes Global's Walmart Marketplace marketplace
      settlement evidence should use zs_observe.walmart_settlement. Apply group_id=8, group_level_id=123 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Walmart Marketplace marketplace settlement file/table is active for Folkhomes Global?
    - Which group filters keep walmart_settlement limited to Folkhomes Global?
    - What Walmart Marketplace canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - marketplace_settlement
    included_concepts:
    - zs_observe.walmart_settlement
    - marketplace settlement
    - Walmart Marketplace
    - marketplace source role
    - client-scoped marketplace table
    - group_id=8
    - group_level_id=123
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - platform_account_id:platform_account.folkhomes_global.walmart_us.marketplace
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - source_role:marketplace_settlement
    - table_id:table.zs_observe.walmart_settlement
    embedding_text: 'For Folkhomes Global, the Walmart Marketplace marketplace settlement binding selects zs_observe.walmart_settlement
      as marketplace evidence. Scope: group_id=8, group_level_id=123. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Folkhomes Global
    - Walmart Marketplace
    - marketplace settlement
    - marketplace
    - zs_observe.walmart_settlement
    - walmart_settlement
    - marketplace_settlement
    - uploaded marketplace canonical pack
    - group_id=8
    - group_level_id=123
    exact_match_keys:
    - account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    platform_account_id: platform_account.folkhomes_global.walmart_us.marketplace
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_data_binding_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
    table_id: table.zs_observe.walmart_settlement
    source_role: marketplace_settlement
  fields:
    platform_account_id: platform_account.folkhomes_global.walmart_us.marketplace
    table_id: table.zs_observe.walmart_settlement
    source_role: marketplace_settlement
    source_entity: Walmart Marketplace
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '123'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.walmart_settlement.group_level_id
      runtime_value: '123'
    active: true
    source_configuration_text: walmart_settlement
```

### 2.5 Business Scope Set Cards

#### business_scope_set.folkhomes_global.marketplace

```yaml
canonical_card:
  canonical_id: business_scope_set.folkhomes_global.marketplace
  card_type: business_scope_set
  canonical_name: Folkhomes Global marketplace scope
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
    vendor_or_system: Folkhomes Global
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Folkhomes Global marketplace scope
    - marketplace runtime scope set
    colloquial_phrases:
    - Folkhomes Global marketplace scope
    - marketplace accounts and bindings
    - Folkhomes Global marketplace resolver input
    business_meaning: Business scope set for Folkhomes Global's marketplace runtime resolution. It groups 6 platform
      accounts and 6 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which marketplace accounts and bindings are active for Folkhomes Global?
    - Which runtime table bindings should be considered together under Folkhomes Global marketplace scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - marketplace
    - resolver_scope
    included_concepts:
    - 6 platform accounts
    - 6 account-data bindings
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - business_scope_set_id:business_scope_set.folkhomes_global.marketplace
    embedding_text: Folkhomes Global marketplace scope groups Folkhomes Global's marketplace runtime accounts and
      table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain
      deferred until supported canonical packs exist.
    search_keywords:
    - Folkhomes Global
    - Folkhomes Global marketplace scope
    - marketplace
    - business scope set
    - 6 accounts
    - 6 bindings
    exact_match_keys:
    - business_scope_set.folkhomes_global.marketplace
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    business_scope_set_id: business_scope_set.folkhomes_global.marketplace
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    scope_name: Folkhomes Global marketplace scope
    scope_type: marketplace_only
    platform_account_ids:
    - platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
    - platform_account.folkhomes_global.walmart_us.marketplace
    - platform_account.folkhomes_global.target_us.marketplace
    - platform_account.folkhomes_global.amazon_amazon_returns.marketplace
    - platform_account.folkhomes_global.target_target_returns.marketplace
    - platform_account.folkhomes_global.walmart.marketplace
    platform_ids:
    - platform.amazon
    - platform.target_plus
    - platform.walmart
    platform_context_ids:
    - platform_context.amazon.international
    - platform_context.target_plus.us
    - platform_context.walmart.us
    account_data_binding_ids:
    - account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
    - account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
    - account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
    - account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
    - account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
    - account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
```

#### business_scope_set.folkhomes_global.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.folkhomes_global.oms
  card_type: business_scope_set
  canonical_name: Folkhomes Global OMS runtime scope
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
    vendor_or_system: Folkhomes Global
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Folkhomes Global OMS runtime scope
    - Folkhomes Global OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Folkhomes Global OMS scope
    - OMS accounts and bindings
    - Folkhomes Global OMS resolver input
    business_meaning: Business scope set for Folkhomes Global's OMS runtime resolution. It groups 1 platform accounts
      and 2 account-data bindings so the resolver can choose client-scoped sources before entering reusable canonical
      packs.
    business_questions:
    - Which OMS accounts and bindings are active for Folkhomes Global?
    - Which runtime table bindings should be considered together under Folkhomes Global OMS runtime scope?
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - runtime_source_family:oms
    embedding_text: Folkhomes Global OMS runtime scope groups Folkhomes Global's OMS runtime accounts and table
      bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain deferred
      until supported canonical packs exist.
    search_keywords:
    - Folkhomes Global
    - Folkhomes Global OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.folkhomes_global.oms
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
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.folkhomes_global.oms
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    binding_name: Folkhomes Global OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.folkhomes_global.oms
    account_data_binding_ids:
    - account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.folkhomes_global.shopify_d2c.oms
      account_name: Folkhomes Global Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

### 2.6 Business Flow Binding Cards

#### business_flow_binding.folkhomes_global.marketplace_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Folkhomes Global marketplace runtime resolution
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
    vendor_or_system: Folkhomes Global
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Folkhomes Global marketplace runtime resolution
    - Folkhomes Global marketplace flow
    - marketplace runtime resolution flow
    colloquial_phrases:
    - Folkhomes Global marketplace resolution flow
    - marketplace source routing
    - Folkhomes Global runtime traversal plan
    business_meaning: Business flow binding for Folkhomes Global's marketplace source resolution. It connects the
      scope set to 6 platform accounts and 6 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which marketplace bindings should be traversed for Folkhomes Global's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - marketplace
    - runtime_traversal
    included_concepts:
    - 6 platform accounts
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - business_flow_binding_id:business_flow_binding.folkhomes_global.marketplace_runtime_resolution
    embedding_text: Folkhomes Global marketplace runtime resolution is Folkhomes Global's marketplace runtime traversal
      binding. It connects the business scope set to account and table bindings so retrieval selects client evidence
      first and then delegates semantics to external canonical packs.
    search_keywords:
    - Folkhomes Global
    - Folkhomes Global marketplace runtime resolution
    - marketplace
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  evidence:
    source_documents:
    - Folkhomes Global.docx
    source_path: Folkhomes Global.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    business_flow_binding_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
    business_scope_set_id: business_scope_set.folkhomes_global.marketplace
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    binding_name: Folkhomes Global marketplace runtime resolution
    binding_type: marketplace_source_resolution
    business_scope_set_id: business_scope_set.folkhomes_global.marketplace
    account_data_binding_ids:
    - account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
    - account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
    - account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
    - account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
    - account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
    - account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
    participating_accounts:
    - platform_account_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
      account_name: Amazon US, UK, MX, CA
    - platform_account_id: platform_account.folkhomes_global.walmart_us.marketplace
      account_name: Walmart US
    - platform_account_id: platform_account.folkhomes_global.target_us.marketplace
      account_name: Target US
    - platform_account_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
      account_name: Amazon amazon_returns
    - platform_account_id: platform_account.folkhomes_global.target_target_returns.marketplace
      account_name: Target target_returns
    - platform_account_id: platform_account.folkhomes_global.walmart.marketplace
      account_name: Walmart —
    money_flow_paths:
    - account_data_binding_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
      source_role: marketplace_settlement
      table_id: table.zs_observe.walmart_settlement
    - account_data_binding_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
      source_role: settlement
      table_id: table.zs_observe.target_settlement
    - account_data_binding_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
      source_role: returns
      table_id: table.zs_observe.amazon_returns
    - account_data_binding_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
      source_role: returns
      table_id: table.zs_observe.target_returns
    - account_data_binding_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
      source_role: marketplace_settlement
      table_id: table.zs_observe.walmart_settlement
```

#### business_flow_binding.folkhomes_global.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.folkhomes_global.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Folkhomes Global OMS runtime resolution flow
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
    vendor_or_system: Folkhomes Global
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Folkhomes Global OMS runtime resolution flow
    - Folkhomes Global OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Folkhomes Global OMS resolution flow
    - OMS source routing
    - Folkhomes Global runtime traversal plan
    business_meaning: Business flow binding for Folkhomes Global's OMS source resolution. It connects the scope
      set to 1 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Folkhomes Global's runtime question?
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
    - tenant_id:tenant.folkhomes_global
    - group_id:group.folkhomes_global.g8.gl123
    - runtime_source_family:oms
    embedding_text: Folkhomes Global OMS runtime resolution flow is Folkhomes Global's OMS runtime traversal binding.
      It connects the business scope set to account and table bindings so retrieval selects client evidence first
      and then delegates semantics to external canonical packs.
    search_keywords:
    - Folkhomes Global
    - Folkhomes Global OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.folkhomes_global.oms_runtime_resolution
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
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.folkhomes_global.oms_runtime_resolution
  fields:
    tenant_id: tenant.folkhomes_global
    group_id: group.folkhomes_global.g8.gl123
    binding_name: Folkhomes Global OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.folkhomes_global.oms
    account_data_binding_ids:
    - account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.folkhomes_global.shopify_d2c.oms
      account_name: Folkhomes Global Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  target_card_id: column.zs_observe.amazon_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  target_card_id: column.zs_observe.amazon_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns.account_data_binding_applies_scope_column.column_zs_observe_target_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns.account_data_binding_applies_scope_column.column_zs_observe_target_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  target_card_id: column.zs_observe.target_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns.account_data_binding_applies_scope_column.column_zs_observe_target_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns.account_data_binding_applies_scope_column.column_zs_observe_target_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  target_card_id: column.zs_observe.target_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement.account_data_binding_applies_scope_column.column_zs_observe_target_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement.account_data_binding_applies_scope_column.column_zs_observe_target_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  target_card_id: column.zs_observe.target_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement.account_data_binding_applies_scope_column.column_zs_observe_target_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement.account_data_binding_applies_scope_column.column_zs_observe_target_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  target_card_id: column.zs_observe.target_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: column.zs_observe.walmart_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: column.zs_observe.walmart_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: column.zs_observe.walmart_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: column.zs_observe.walmart_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_amazon_amazon_returns_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_amazon_amazon_returns_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  target_card_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_target_target_returns_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_target_target_returns_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  target_card_id: platform_account.folkhomes_global.target_target_returns.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_target_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  target_card_id: platform_account.folkhomes_global.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_walmart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_walmart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: platform_account.folkhomes_global.walmart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_belongs_to_platform_account.platform_account_folkhomes_global_walmart_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: platform_account.folkhomes_global.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns.account_data_binding_binds_to_table.table_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns.account_data_binding_binds_to_table.table_zs_observe_amazon_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  target_card_id: table.zs_observe.amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: table.zs_observe.shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: table.zs_observe.shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns.account_data_binding_binds_to_table.table_zs_observe_target_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns.account_data_binding_binds_to_table.table_zs_observe_target_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  target_card_id: table.zs_observe.target_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement.account_data_binding_binds_to_table.table_zs_observe_target_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement.account_data_binding_binds_to_table.table_zs_observe_target_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  target_card_id: table.zs_observe.target_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_binds_to_table.table_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_binds_to_table.table_zs_observe_walmart_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: table.zs_observe.walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_binds_to_table.table_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_binds_to_table.table_zs_observe_walmart_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: table.zs_observe.walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.folkhomes_global.oms_runtime_resolution
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.folkhomes_global.oms_runtime_resolution
  target_card_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.folkhomes_global.oms_runtime_resolution
  target_card_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_amazon_amazon_returns_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_amazon_amazon_returns_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_target_target_returns_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_target_target_returns_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: platform_account.folkhomes_global.target_target_returns.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_target_us_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: platform_account.folkhomes_global.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_walmart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_walmart_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: platform_account.folkhomes_global.walmart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_walmart_us_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: platform_account.folkhomes_global.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_folkhomes_global_shopify_d2c_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.folkhomes_global.oms_runtime_resolution
  target_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_folkhomes_global_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_folkhomes_global_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  target_card_id: business_scope_set.folkhomes_global.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_folkhomes_global_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_folkhomes_global_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_folkhomes_global_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.folkhomes_global.oms_runtime_resolution
  target_card_id: business_scope_set.folkhomes_global.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_oms.business_scope_set_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_oms.business_scope_set_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.folkhomes_global.oms
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.folkhomes_global.oms
  target_card_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.folkhomes_global.oms
  target_card_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform.platform_amazon
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform.platform_target_plus

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform.platform_target_plus
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform.target_plus
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform.platform_walmart

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform.platform_walmart
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform.walmart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_platform.platform_shopify
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.folkhomes_global.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_amazon_amazon_returns_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_amazon_amazon_returns_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_target_target_returns_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_target_target_returns_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_account.folkhomes_global.target_target_returns.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_target_us_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_account.folkhomes_global.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_walmart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_walmart_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_account.folkhomes_global.walmart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_account.platform_account_folkhomes_global_walmart_us_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_account.folkhomes_global.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_platform_account.platform_account_folkhomes_global_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_platform_account.platform_account_folkhomes_global_shopify_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.folkhomes_global.oms
  target_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_international
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_context.platform_context_target_plus_us

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_context.platform_context_target_plus_us
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_context.target_plus.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_context.platform_context_walmart_us

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_marketplace.business_scope_set_includes_platform_context.platform_context_walmart_us
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.folkhomes_global.marketplace
  target_card_id: platform_context.walmart.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_folkhomes_global_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.folkhomes_global.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_folkhomes_global_g8_gl123.group_belongs_to_tenant.tenant_folkhomes_global

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_belongs_to_tenant.tenant_folkhomes_global
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: tenant.folkhomes_global
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_folkhomes_global_g8_gl123.group_has_business_flow_binding.business_flow_binding_folkhomes_global_marketplace_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_business_flow_binding.business_flow_binding_folkhomes_global_marketplace_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: business_flow_binding.folkhomes_global.marketplace_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_folkhomes_global_g8_gl123.group_has_business_flow_binding.business_flow_binding_folkhomes_global_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_business_flow_binding.business_flow_binding_folkhomes_global_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: business_flow_binding.folkhomes_global.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_folkhomes_global_g8_gl123.group_has_business_scope_set.business_scope_set_folkhomes_global_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_business_scope_set.business_scope_set_folkhomes_global_marketplace
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: business_scope_set.folkhomes_global.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_folkhomes_global_g8_gl123.group_has_business_scope_set.business_scope_set_folkhomes_global_oms

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_business_scope_set.business_scope_set_folkhomes_global_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: business_scope_set.folkhomes_global.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_amazon_amazon_returns_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_amazon_amazon_returns_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_shopify_d2c_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_target_target_returns_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_target_target_returns_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: platform_account.folkhomes_global.target_target_returns.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_target_us_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: platform_account.folkhomes_global.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_walmart_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_walmart_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: platform_account.folkhomes_global.walmart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_folkhomes_global_g8_gl123.group_has_platform_account.platform_account_folkhomes_global_walmart_us_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.folkhomes_global.g8.gl123
  target_card_id: platform_account.folkhomes_global.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_folkhomes_global_amazon_amazon_returns_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_amazon_amazon_returns_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_folkhomes_global_target_target_returns_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_target_target_returns_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.folkhomes_global.target_target_returns.marketplace
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_target_us_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_target_us_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.folkhomes_global.target_us.marketplace
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_walmart_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_walmart_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.folkhomes_global.walmart.marketplace
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_walmart_us_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_walmart_us_marketplace.platform_account_belongs_to_group.group_folkhomes_global_g8_gl123
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.folkhomes_global.walmart_us.marketplace
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_folkhomes_global_amazon_amazon_returns_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_amazon_amazon_returns_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_amazon_amazon_returns_returns_zs_observe_amazon_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  target_card_id: account_data_binding.folkhomes_global.amazon_amazon_returns.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_amazon_us_uk_mx_ca_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  target_card_id: account_data_binding.folkhomes_global.amazon_us_uk_mx_ca.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  target_card_id: account_data_binding.folkhomes_global.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  target_card_id: account_data_binding.folkhomes_global.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_folkhomes_global_target_target_returns_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_target_target_returns_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_target_target_returns_returns_zs_observe_target_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.folkhomes_global.target_target_returns.marketplace
  target_card_id: account_data_binding.folkhomes_global.target_target_returns.returns.zs_observe_target_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_target_us_settlement_zs_observe_target_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.folkhomes_global.target_us.marketplace
  target_card_id: account_data_binding.folkhomes_global.target_us.settlement.zs_observe_target_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_walmart_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_walmart_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_walmart_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.folkhomes_global.walmart.marketplace
  target_card_id: account_data_binding.folkhomes_global.walmart.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_walmart_us_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_walmart_us_marketplace.platform_account_has_account_data_binding.account_data_binding_folkhomes_global_walmart_us_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.folkhomes_global.walmart_us.marketplace
  target_card_id: account_data_binding.folkhomes_global.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_folkhomes_global_amazon_amazon_returns_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_amazon_amazon_returns_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_uses_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_uses_platform.platform_shopify
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_folkhomes_global_target_target_returns_marketplace.platform_account_uses_platform.platform_target_plus

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_target_target_returns_marketplace.platform_account_uses_platform.platform_target_plus
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.folkhomes_global.target_target_returns.marketplace
  target_card_id: platform.target_plus
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_target_us_marketplace.platform_account_uses_platform.platform_target_plus

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_target_us_marketplace.platform_account_uses_platform.platform_target_plus
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.folkhomes_global.target_us.marketplace
  target_card_id: platform.target_plus
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_walmart_marketplace.platform_account_uses_platform.platform_walmart

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_walmart_marketplace.platform_account_uses_platform.platform_walmart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.folkhomes_global.walmart.marketplace
  target_card_id: platform.walmart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_walmart_us_marketplace.platform_account_uses_platform.platform_walmart

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_walmart_us_marketplace.platform_account_uses_platform.platform_walmart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.folkhomes_global.walmart_us.marketplace
  target_card_id: platform.walmart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_folkhomes_global_amazon_amazon_returns_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_amazon_amazon_returns_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.folkhomes_global.amazon_amazon_returns.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_amazon_us_uk_mx_ca_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.folkhomes_global.amazon_us_uk_mx_ca.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.folkhomes_global.shopify_d2c.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_folkhomes_global_target_target_returns_marketplace.platform_account_uses_platform_context.platform_context_target_plus_us

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_target_target_returns_marketplace.platform_account_uses_platform_context.platform_context_target_plus_us
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.folkhomes_global.target_target_returns.marketplace
  target_card_id: platform_context.target_plus.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_target_us_marketplace.platform_account_uses_platform_context.platform_context_target_plus_us

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_target_us_marketplace.platform_account_uses_platform_context.platform_context_target_plus_us
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.folkhomes_global.target_us.marketplace
  target_card_id: platform_context.target_plus.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_walmart_marketplace.platform_account_uses_platform_context.platform_context_walmart_us

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_walmart_marketplace.platform_account_uses_platform_context.platform_context_walmart_us
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.folkhomes_global.walmart.marketplace
  target_card_id: platform_context.walmart.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_folkhomes_global_walmart_us_marketplace.platform_account_uses_platform_context.platform_context_walmart_us

```yaml
canonical_edge:
  edge_id: edge.platform_account_folkhomes_global_walmart_us_marketplace.platform_account_uses_platform_context.platform_context_walmart_us
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.folkhomes_global.walmart_us.marketplace
  target_card_id: platform_context.walmart.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### TENANT_HAS_GROUP

#### edge.tenant_folkhomes_global.tenant_has_group.group_folkhomes_global_g8_gl123

```yaml
canonical_edge:
  edge_id: edge.tenant_folkhomes_global.tenant_has_group.group_folkhomes_global_g8_gl123
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.folkhomes_global
  target_card_id: group.folkhomes_global.g8.gl123
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```
