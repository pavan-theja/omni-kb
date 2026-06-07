# Rosenza International Trading L.L.C — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `rosenza_international_trading_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Noon UAE/KSA
  config: OMS (order report + export report), Settlement
  reason: Noon marketplace pack not uploaded
- label: Namshi UAE/KSA
  config: OMS (order report + return report + KSA export), Settlement
  reason: Namshi marketplace pack not uploaded
- label: Noon Namshi ASIN–SKU noon_namshi_lookup
  config: Maps Noon/Namshi item IDs to brand SKUs — shared across both platforms
  reason: Noon marketplace pack not uploaded
- label: Native marketplace OMS feeds
  config: Amazon/marketplace native OMS
  reason: Native marketplace OMS is already represented through marketplace runtime bindings; no separate OMS Business
    KB binding emitted in this pass.
  source_family: oms
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 12
  account_data_binding: 17
  business_scope_set: 2
  business_flow_binding: 2
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 34
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 17
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 17
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 2
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 17
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 12
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 2
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 2
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 17
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 2
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 12
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 3
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 2
  GROUP_HAS_BUSINESS_SCOPE_SET: 2
  GROUP_HAS_PLATFORM_ACCOUNT: 12
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 12
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 17
  PLATFORM_ACCOUNT_USES_PLATFORM: 12
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 12
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

#### tenant.rosenza_international_trading_l_l_c

```yaml
canonical_card:
  canonical_id: tenant.rosenza_international_trading_l_l_c
  card_type: tenant
  canonical_name: Rosenza International Trading L.L.C
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
    vendor_or_system: Rosenza International Trading L.L.C
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Rosenza International Trading L.L.C
    - rosenza_international_trading_l_l_c
    - Rosenza International Trading L.L.C runtime tenant
    colloquial_phrases:
    - Rosenza International Trading L.L.C client runtime
    - Rosenza International Trading L.L.C source configuration
    - Rosenza International Trading L.L.C scoped reconciliation setup
    business_meaning: Runtime tenant identity for Rosenza International Trading L.L.C. It anchors the client's marketplace,
      logistics, OMS, WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from
      reusable domain semantics.
    business_questions:
    - Which source families and configured accounts belong to Rosenza International Trading L.L.C?
    - Which group and account bindings should constrain Rosenza International Trading L.L.C's SQL handoff?
    - After Rosenza International Trading L.L.C's runtime scope is resolved, which domain layer should receive the
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    embedding_text: Rosenza International Trading L.L.C is the runtime tenant root for the client's marketplace,
      logistics, OMS, WMS, payment-gateway, and bank-statement configuration. Use it to reach group, platform-account,
      and account-data-binding nodes before invoking reusable canonical packs.
    search_keywords:
    - Rosenza International Trading L.L.C
    - rosenza_international_trading_l_l_c
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.rosenza_international_trading_l_l_c
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
  fields:
    tenant_slug: rosenza_international_trading_l_l_c
    tenant_name: Rosenza International Trading L.L.C
    legal_name: Rosenza International Trading L.L.C
    active: true
```

### 2.2 Group Cards

#### group.rosenza_international_trading_l_l_c.g9.gl133

```yaml
canonical_card:
  canonical_id: group.rosenza_international_trading_l_l_c.g9.gl133
  card_type: group
  canonical_name: Rosenza International Trading L.L.C group 9/133
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
    vendor_or_system: Rosenza International Trading L.L.C
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mensa Brands
    - Rosenza International Trading L.L.C group 9/133
    - group_id 9
    - group_level_id 133
    colloquial_phrases:
    - Rosenza International Trading L.L.C group scope
    - Mensa Brands runtime scope
    - group 9 level 133 query boundary
    business_meaning: 'Runtime group scope for Rosenza International Trading L.L.C: group_id=9 and group_level_id=133.
      It is the client-specific filter boundary that must be applied before resolving account bindings for US in
      USD.'
    business_questions:
    - Which bindings use group_id=9 and group_level_id=133?
    - Which source families are active under Mensa Brands?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - group_id_value:9
    - group_level_id_value:133
    embedding_text: Mensa Brands is the runtime group node for Rosenza International Trading L.L.C. Apply group_id=9
      and group_level_id=133 when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Mensa Brands
    - group_id 9
    - group_level_id 133
    - runtime group scope
    exact_match_keys:
    - group.rosenza_international_trading_l_l_c.g9.gl133
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    group_level_id: '133'
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id_value: '9'
    group_level_id_value: '133'
    group_name: Mensa Brands
    default_currency: USD
    country: US
```

### 2.3 Platform Account Cards

#### platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon Canada
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
    - Amazon Canada
    - Rosenza International Trading L.L.C Amazon Canada
    - Amazon
    - Amazon Canada marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon Canada source account
    - Amazon Canada marketplace runtime account
    - Amazon Canada configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon Canada marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.international and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Amazon Canada table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon Canada questions traverse
      through?
    - Which source roles under Amazon Canada are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon Canada
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon Canada platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon Canada
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon Canada
    account_type: marketplace_seller_account
    source_account_identifier: Amazon Canada
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon fee preview amazon_fee_preview
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
    - Amazon fee preview amazon_fee_preview
    - Rosenza International Trading L.L.C Amazon fee preview amazon_fee_preview
    - Amazon
    - Amazon fee preview amazon_fee_preview marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon fee preview amazon_fee_preview source account
    - Amazon fee preview amazon_fee_preview marketplace runtime account
    - Amazon fee preview amazon_fee_preview configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon fee preview amazon_fee_preview
      marketplace sources. It points traversal to platform.amazon and platform_context.amazon.international and
      groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Amazon fee preview amazon_fee_preview table bindings are available for Rosenza International Trading
      L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon fee preview amazon_fee_preview
      questions traverse through?
    - Which source roles under Amazon fee preview amazon_fee_preview are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Projected fee estimates ahead of settlement close'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon fee preview amazon_fee_preview
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon fee preview amazon_fee_preview platform account
      routes marketplace questions to platform.amazon / platform_context.amazon.international. Use it to collect
      the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon fee preview amazon_fee_preview
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon fee preview amazon_fee_preview
    account_type: marketplace_seller_account
    source_account_identifier: Amazon fee preview amazon_fee_preview
    active: true
    configured_source_description: Projected fee estimates ahead of settlement close
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon France
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
    - Amazon France
    - Rosenza International Trading L.L.C Amazon France
    - Amazon
    - Amazon France marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon France source account
    - Amazon France marketplace runtime account
    - Amazon France configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon France marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.international and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Amazon France table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon France questions traverse
      through?
    - Which source roles under Amazon France are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon France
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon France platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon France
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon France
    account_type: marketplace_seller_account
    source_account_identifier: Amazon France
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon Germany
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
    - Amazon Germany
    - Rosenza International Trading L.L.C Amazon Germany
    - Amazon
    - Amazon Germany marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon Germany source account
    - Amazon Germany marketplace runtime account
    - Amazon Germany configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon Germany marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.international and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Amazon Germany table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon Germany questions traverse
      through?
    - Which source roles under Amazon Germany are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon Germany
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon Germany platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon Germany
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon Germany
    account_type: marketplace_seller_account
    source_account_identifier: Amazon Germany
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon KSA
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
    - Amazon KSA
    - Rosenza International Trading L.L.C Amazon KSA
    - Amazon
    - Amazon KSA marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon KSA source account
    - Amazon KSA marketplace runtime account
    - Amazon KSA configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon KSA marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.international and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Amazon KSA table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon KSA questions traverse
      through?
    - Which source roles under Amazon KSA are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon KSA
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon KSA platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon KSA
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon KSA
    account_type: marketplace_seller_account
    source_account_identifier: Amazon KSA
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon Mexico
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
    - Amazon Mexico
    - Rosenza International Trading L.L.C Amazon Mexico
    - Amazon
    - Amazon Mexico marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon Mexico source account
    - Amazon Mexico marketplace runtime account
    - Amazon Mexico configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon Mexico marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.international and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Amazon Mexico table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon Mexico questions traverse
      through?
    - Which source roles under Amazon Mexico are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon Mexico
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon Mexico platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon Mexico
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon Mexico
    account_type: marketplace_seller_account
    source_account_identifier: Amazon Mexico
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon Spain
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
    - Amazon Spain
    - Rosenza International Trading L.L.C Amazon Spain
    - Amazon
    - Amazon Spain marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon Spain source account
    - Amazon Spain marketplace runtime account
    - Amazon Spain configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon Spain marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon Spain table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon Spain questions traverse
      through?
    - Which source roles under Amazon Spain are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.in
    - Amazon Spain
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon Spain platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.in. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon Spain
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.in
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_name: Amazon Spain
    account_type: marketplace_seller_account
    source_account_identifier: Amazon Spain
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon Sweden
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
    - Amazon Sweden
    - Rosenza International Trading L.L.C Amazon Sweden
    - Amazon
    - Amazon Sweden marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon Sweden source account
    - Amazon Sweden marketplace runtime account
    - Amazon Sweden configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon Sweden marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.international and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Amazon Sweden table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon Sweden questions traverse
      through?
    - Which source roles under Amazon Sweden are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon Sweden
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon Sweden platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon Sweden
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon Sweden
    account_type: marketplace_seller_account
    source_account_identifier: Amazon Sweden
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon UAE
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
    - Amazon UAE
    - Rosenza International Trading L.L.C Amazon UAE
    - Amazon
    - Amazon UAE marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon UAE source account
    - Amazon UAE marketplace runtime account
    - Amazon UAE configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon UAE marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.international and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Amazon UAE table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon UAE questions traverse
      through?
    - Which source roles under Amazon UAE are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon UAE
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon UAE platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon UAE
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon UAE
    account_type: marketplace_seller_account
    source_account_identifier: Amazon UAE
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon UK
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
    - Amazon UK
    - Rosenza International Trading L.L.C Amazon UK
    - Amazon
    - Amazon UK marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon UK source account
    - Amazon UK marketplace runtime account
    - Amazon UK configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon UK marketplace sources.
      It points traversal to platform.amazon and platform_context.amazon.international and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon UK table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon UK questions traverse
      through?
    - Which source roles under Amazon UK are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon UK
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon UK platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon UK
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon UK
    account_type: marketplace_seller_account
    source_account_identifier: Amazon UK
    active: true
    configured_source_description: Settlement
```

#### platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C — Amazon US
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
    - Amazon US
    - Rosenza International Trading L.L.C Amazon US
    - Amazon
    - Amazon US marketplace account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon US source account
    - Amazon US marketplace runtime account
    - Amazon US configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Amazon US marketplace sources.
      It points traversal to platform.amazon and platform_context.amazon.international and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon US table bindings are available for Rosenza International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Amazon US questions traverse
      through?
    - Which source roles under Amazon US are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS, Settlement, Returns, Fee preview'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon US
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    embedding_text: Rosenza International Trading L.L.C's Amazon US platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.international. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon US
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon US
    account_type: marketplace_seller_account
    source_account_identifier: Amazon US
    active: true
    configured_source_description: OMS, Settlement, Returns, Fee preview
```

#### platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms

```yaml
canonical_card:
  canonical_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  card_type: platform_account
  canonical_name: Rosenza International Trading L.L.C Shopify D2C OMS account
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
    vendor_or_system: Rosenza International Trading L.L.C
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Rosenza International Trading L.L.C Shopify D2C OMS account
    - Rosenza International Trading L.L.C Rosenza International Trading L.L.C Shopify D2C OMS account
    - Shopify
    - Rosenza International Trading L.L.C Shopify D2C OMS account OMS account
    colloquial_phrases:
    - Rosenza International Trading L.L.C Rosenza International Trading L.L.C Shopify D2C OMS account source account
    - Rosenza International Trading L.L.C Shopify D2C OMS account OMS runtime account
    - Rosenza International Trading L.L.C Shopify D2C OMS account configured source family
    business_meaning: Runtime platform account for Rosenza International Trading L.L.C's Rosenza International Trading
      L.L.C Shopify D2C OMS account OMS sources. It points traversal to platform.shopify and platform_context.shopify.in.d2c_oms
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Rosenza International Trading L.L.C Shopify D2C OMS account table bindings are available for Rosenza
      International Trading L.L.C?
    - Which canonical platform/context should Rosenza International Trading L.L.C's Rosenza International Trading
      L.L.C Shopify D2C OMS account questions traverse through?
    - Which source roles under Rosenza International Trading L.L.C Shopify D2C OMS account are active or review-required
      for this client?
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - runtime_source_family:oms
    embedding_text: Rosenza International Trading L.L.C's Rosenza International Trading L.L.C Shopify D2C OMS account
      platform account routes OMS questions to platform.shopify / platform_context.shopify.in.d2c_oms. Use it to
      collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Rosenza International Trading L.L.C Shopify D2C OMS account
    - Shopify
    - OMS
    - platform.shopify
    - platform_context.shopify.in.d2c_oms
    exact_match_keys:
    - platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    - shopify_d2c_oms.md
    source_path: Rosenza International Trading L.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    runtime_source_family: oms
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_name: Rosenza International Trading L.L.C Shopify D2C OMS account
    account_type: d2c_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Shopify D2C OMS and returns/refund events
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: shopify_pack_exposes_in_context_non_in_client_review_currency_and_country_before_production
    group_scope_values:
      group_id: '9'
      group_level_id: '133'
```

### 2.4 Account Data Binding Cards

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon Canada — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon fee preview amazon_fee_preview — fee_preview
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
    - Amazon fee preview
    - amazon_fee_preview
    - zs_observe.amazon_fee_preview
    - Projected fee estimates ahead of settlement close
    - Rosenza International Trading L.L.C Amazon fee preview
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon fee preview source
    - Amazon fee preview runtime binding
    - amazon_fee_preview for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      fee preview evidence should use zs_observe.amazon_fee_preview. Apply group_id=9, group_level_id=133 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon fee preview file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_fee_preview limited to Rosenza International Trading L.L.C?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - fee_preview
    included_concepts:
    - zs_observe.amazon_fee_preview
    - fee preview
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:fee_preview
    - table_id:table.zs_observe.amazon_fee_preview
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon fee preview binding selects zs_observe.amazon_fee_preview
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - fee preview
    - marketplace
    - zs_observe.amazon_fee_preview
    - amazon_fee_preview
    - fee_preview
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
    source_entity: Amazon
    scope_keys:
    active: true
    source_configuration_text: Projected fee estimates ahead of settlement close
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon fee preview amazon_fee_preview — settlement
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
    - Projected fee estimates ahead of settlement close
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Projected fee estimates ahead of settlement close
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon France — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon Germany — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon KSA — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon Mexico — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon Spain — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon Sweden — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon UAE — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon UK — settlement
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
    - Settlement
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon US — fee_preview
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
    - Amazon fee preview
    - amazon_fee_preview
    - zs_observe.amazon_fee_preview
    - OMS, Settlement, Returns, Fee preview
    - Rosenza International Trading L.L.C Amazon fee preview
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon fee preview source
    - Amazon fee preview runtime binding
    - amazon_fee_preview for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      fee preview evidence should use zs_observe.amazon_fee_preview. Apply group_id=9, group_level_id=133 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon fee preview file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_fee_preview limited to Rosenza International Trading L.L.C?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - fee_preview
    included_concepts:
    - zs_observe.amazon_fee_preview
    - fee preview
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:fee_preview
    - table_id:table.zs_observe.amazon_fee_preview
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon fee preview binding selects zs_observe.amazon_fee_preview
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - fee preview
    - marketplace
    - zs_observe.amazon_fee_preview
    - amazon_fee_preview
    - fee_preview
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
    source_entity: Amazon
    scope_keys:
    active: true
    source_configuration_text: OMS, Settlement, Returns, Fee preview
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon US — oms_sales
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
    - OMS, Settlement, Returns, Fee preview
    - Rosenza International Trading L.L.C Amazon OMS sales
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon OMS sales source
    - Amazon OMS sales runtime binding
    - amazon_oms for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      OMS sales evidence should use zs_observe.amazon_oms. Apply group_id=9, group_level_id=133 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon OMS sales file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_oms limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:oms_sales
    - table_id:table.zs_observe.amazon_oms
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon OMS sales binding selects zs_observe.amazon_oms
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - OMS sales
    - marketplace
    - zs_observe.amazon_oms
    - amazon_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_oms.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_oms.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Fee preview
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon US — returns
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
    - OMS, Settlement, Returns, Fee preview
    - Rosenza International Trading L.L.C Amazon returns
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon returns source
    - Amazon returns runtime binding
    - amazon_returns for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      returns evidence should use zs_observe.amazon_returns. Apply group_id=9, group_level_id=133 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon returns file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_returns limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:returns
    - table_id:table.zs_observe.amazon_returns
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon returns binding selects zs_observe.amazon_returns
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - returns
    - marketplace
    - zs_observe.amazon_returns
    - amazon_returns
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
    table_id: table.zs_observe.amazon_returns
    source_role: returns
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    table_id: table.zs_observe.amazon_returns
    source_role: returns
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_returns.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Fee preview
```

#### account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C — Amazon US — settlement
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
    - OMS, Settlement, Returns, Fee preview
    - Rosenza International Trading L.L.C Amazon settlement
    colloquial_phrases:
    - Rosenza International Trading L.L.C Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=133 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Rosenza International Trading L.L.C?
    - Which group filters keep amazon_settlement limited to Rosenza International Trading L.L.C?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Rosenza International Trading L.L.C, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '133'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Fee preview
```

#### account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C Shopify D2C OMS oms_sales binding
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
    vendor_or_system: Rosenza International Trading L.L.C
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
    - Rosenza International Trading L.L.C Shopify D2C OMS OMS sales
    colloquial_phrases:
    - Rosenza International Trading L.L.C Shopify D2C OMS OMS sales source
    - Shopify D2C OMS OMS sales runtime binding
    - shopify_oms for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Shopify
      D2C OMS OMS sales evidence should use zs_observe.shopify_oms. Apply group_id=9, group_level_id=133 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Rosenza International Trading L.L.C's OMS sales question?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:oms_sales
    - table_id:table.zs_observe.shopify_oms
    - runtime_source_family:oms
    embedding_text: 'For Rosenza International Trading L.L.C, the Shopify D2C OMS OMS sales binding selects zs_observe.shopify_oms
      as OMS evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Shopify D2C OMS
    - OMS sales
    - OMS
    - zs_observe.shopify_oms
    - shopify_oms
    - oms_sales
    - shopify_d2c_oms.md
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    - shopify_d2c_oms.md
    source_path: Rosenza International Trading L.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    source_entity: Shopify D2C OMS
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.shopify_oms.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '133'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shopify_oms.group_level_id
      runtime_value: '133'
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Shopify D2C OMS and returns/refund events
    canonical_table_coverage_status: active
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: shopify_pack_exposes_in_context_non_in_client_review_currency_and_country_before_production
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  card_type: account_data_binding
  canonical_name: Rosenza International Trading L.L.C Shopify D2C OMS returns binding
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
    vendor_or_system: Rosenza International Trading L.L.C
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
    - Rosenza International Trading L.L.C Shopify D2C OMS returns
    colloquial_phrases:
    - Rosenza International Trading L.L.C Shopify D2C OMS returns source
    - Shopify D2C OMS returns runtime binding
    - shopify_returns for Rosenza International Trading L.L.C
    business_meaning: This account-data binding tells the resolver that Rosenza International Trading L.L.C's Shopify
      D2C OMS returns evidence should use zs_observe.shopify_returns. Apply group_id=9, group_level_id=133 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Rosenza International Trading L.L.C's returns question?
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
    - group_id=9
    - group_level_id=133
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - platform_account_id:platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:returns
    - table_id:table.zs_observe.shopify_returns
    - runtime_source_family:oms
    embedding_text: 'For Rosenza International Trading L.L.C, the Shopify D2C OMS returns binding selects zs_observe.shopify_returns
      as OMS evidence. Scope: group_id=9, group_level_id=133. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Rosenza International Trading L.L.C
    - Shopify D2C OMS
    - returns
    - OMS
    - zs_observe.shopify_returns
    - shopify_returns
    - shopify_d2c_oms.md
    - group_id=9
    - group_level_id=133
    exact_match_keys:
    - account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    - shopify_d2c_oms.md
    source_path: Rosenza International Trading L.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
    domain_id: domain.shopify.refunds_returns
    table_id: table.zs_observe.shopify_returns
    source_role: returns
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
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

### 2.5 Business Scope Set Cards

#### business_scope_set.rosenza_international_trading_l_l_c.marketplace

```yaml
canonical_card:
  canonical_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  card_type: business_scope_set
  canonical_name: Rosenza International Trading L.L.C marketplace scope
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
    vendor_or_system: Rosenza International Trading L.L.C
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Rosenza International Trading L.L.C marketplace scope
    - marketplace runtime scope set
    colloquial_phrases:
    - Rosenza International Trading L.L.C marketplace scope
    - marketplace accounts and bindings
    - Rosenza International Trading L.L.C marketplace resolver input
    business_meaning: Business scope set for Rosenza International Trading L.L.C's marketplace runtime resolution.
      It groups 11 platform accounts and 15 account-data bindings so the resolver can choose client-scoped sources
      before entering reusable canonical packs.
    business_questions:
    - Which marketplace accounts and bindings are active for Rosenza International Trading L.L.C?
    - Which runtime table bindings should be considered together under Rosenza International Trading L.L.C marketplace
      scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - marketplace
    - resolver_scope
    included_concepts:
    - 11 platform accounts
    - 15 account-data bindings
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - business_scope_set_id:business_scope_set.rosenza_international_trading_l_l_c.marketplace
    embedding_text: Rosenza International Trading L.L.C marketplace scope groups Rosenza International Trading L.L.C's
      marketplace runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Rosenza International Trading L.L.C marketplace scope
    - marketplace
    - business scope set
    - 11 accounts
    - 15 bindings
    exact_match_keys:
    - business_scope_set.rosenza_international_trading_l_l_c.marketplace
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    business_scope_set_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    scope_name: Rosenza International Trading L.L.C marketplace scope
    scope_type: marketplace_only
    platform_account_ids:
    - platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
    - platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
    platform_ids:
    - platform.amazon
    platform_context_ids:
    - platform_context.amazon.in
    - platform_context.amazon.international
    account_data_binding_ids:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
```

#### business_scope_set.rosenza_international_trading_l_l_c.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  card_type: business_scope_set
  canonical_name: Rosenza International Trading L.L.C OMS runtime scope
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
    vendor_or_system: Rosenza International Trading L.L.C
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Rosenza International Trading L.L.C OMS runtime scope
    - Rosenza International Trading L.L.C OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Rosenza International Trading L.L.C OMS scope
    - OMS accounts and bindings
    - Rosenza International Trading L.L.C OMS resolver input
    business_meaning: Business scope set for Rosenza International Trading L.L.C's OMS runtime resolution. It groups
      1 platform accounts and 2 account-data bindings so the resolver can choose client-scoped sources before entering
      reusable canonical packs.
    business_questions:
    - Which OMS accounts and bindings are active for Rosenza International Trading L.L.C?
    - Which runtime table bindings should be considered together under Rosenza International Trading L.L.C OMS runtime
      scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - OMS
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - 1 deferred sources
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - runtime_source_family:oms
    embedding_text: Rosenza International Trading L.L.C OMS runtime scope groups Rosenza International Trading L.L.C's
      OMS runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Rosenza International Trading L.L.C OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.rosenza_international_trading_l_l_c.oms
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
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    binding_name: Rosenza International Trading L.L.C OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.rosenza_international_trading_l_l_c.oms
    account_data_binding_ids:
    - account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
      account_name: Rosenza International Trading L.L.C Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources:
    - label: Native marketplace OMS feeds
      config: Amazon/marketplace native OMS
      reason: Native marketplace OMS is already represented through marketplace runtime bindings; no separate OMS
        Business KB binding emitted in this pass.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

### 2.6 Business Flow Binding Cards

#### business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Rosenza International Trading L.L.C marketplace runtime resolution
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
    vendor_or_system: Rosenza International Trading L.L.C
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Rosenza International Trading L.L.C marketplace runtime resolution
    - Rosenza International Trading L.L.C marketplace flow
    - marketplace runtime resolution flow
    colloquial_phrases:
    - Rosenza International Trading L.L.C marketplace resolution flow
    - marketplace source routing
    - Rosenza International Trading L.L.C runtime traversal plan
    business_meaning: Business flow binding for Rosenza International Trading L.L.C's marketplace source resolution.
      It connects the scope set to 11 platform accounts and 15 account-data bindings so questions enter the right
      client-scoped evidence before reusable semantics run.
    business_questions:
    - Which marketplace bindings should be traversed for Rosenza International Trading L.L.C's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - marketplace
    - runtime_traversal
    included_concepts:
    - 11 platform accounts
    - 15 account-data bindings
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - business_flow_binding_id:business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
    embedding_text: Rosenza International Trading L.L.C marketplace runtime resolution is Rosenza International
      Trading L.L.C's marketplace runtime traversal binding. It connects the business scope set to account and table
      bindings so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Rosenza International Trading L.L.C marketplace runtime resolution
    - marketplace
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  evidence:
    source_documents:
    - Rosenza International Trading L.docx
    source_path: Rosenza International Trading L.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    business_flow_binding_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
    business_scope_set_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    binding_name: Rosenza International Trading L.L.C marketplace runtime resolution
    binding_type: marketplace_source_resolution
    business_scope_set_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
    account_data_binding_ids:
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
    - account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
    participating_accounts:
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
      account_name: Amazon US
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
      account_name: Amazon Canada
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
      account_name: Amazon Mexico
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
      account_name: Amazon UK
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
      account_name: Amazon Germany
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
      account_name: Amazon France
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
      account_name: Amazon Spain
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
      account_name: Amazon Sweden
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
      account_name: Amazon UAE
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
      account_name: Amazon KSA
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
      account_name: Amazon fee preview amazon_fee_preview
    money_flow_paths:
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
      source_role: oms_sales
      table_id: table.zs_observe.amazon_oms
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
      source_role: fee_preview
      table_id: table.zs_observe.amazon_fee_preview
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
      source_role: returns
      table_id: table.zs_observe.amazon_returns
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
      source_role: fee_preview
      table_id: table.zs_observe.amazon_fee_preview
    deferred_sources:
    - label: Noon UAE/KSA
      config: OMS (order report + export report), Settlement
      reason: Noon marketplace pack not uploaded
    - label: Namshi UAE/KSA
      config: OMS (order report + return report + KSA export), Settlement
      reason: Namshi marketplace pack not uploaded
    - label: Noon Namshi ASIN–SKU noon_namshi_lookup
      config: Maps Noon/Namshi item IDs to brand SKUs — shared across both platforms
      reason: Noon marketplace pack not uploaded
```

#### business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Rosenza International Trading L.L.C OMS runtime resolution flow
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
    vendor_or_system: Rosenza International Trading L.L.C
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Rosenza International Trading L.L.C OMS runtime resolution flow
    - Rosenza International Trading L.L.C OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Rosenza International Trading L.L.C OMS resolution flow
    - OMS source routing
    - Rosenza International Trading L.L.C runtime traversal plan
    business_meaning: Business flow binding for Rosenza International Trading L.L.C's OMS source resolution. It
      connects the scope set to 1 platform accounts and 2 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Rosenza International Trading L.L.C's runtime question?
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
    - tenant_id:tenant.rosenza_international_trading_l_l_c
    - group_id:group.rosenza_international_trading_l_l_c.g9.gl133
    - runtime_source_family:oms
    embedding_text: Rosenza International Trading L.L.C OMS runtime resolution flow is Rosenza International Trading
      L.L.C's OMS runtime traversal binding. It connects the business scope set to account and table bindings so
      retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Rosenza International Trading L.L.C
    - Rosenza International Trading L.L.C OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
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
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
  fields:
    tenant_id: tenant.rosenza_international_trading_l_l_c
    group_id: group.rosenza_international_trading_l_l_c.g9.gl133
    binding_name: Rosenza International Trading L.L.C OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.rosenza_international_trading_l_l_c.oms
    account_data_binding_ids:
    - account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
      account_name: Rosenza International Trading L.L.C Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources:
    - label: Native marketplace OMS feeds
      config: Amazon/marketplace native OMS
      reason: Native marketplace OMS is already represented through marketplace runtime bindings; no separate OMS
        Business KB binding emitted in this pass.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  target_card_id: column.zs_observe.amazon_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  target_card_id: column.zs_observe.amazon_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: table.zs_observe.amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: table.zs_observe.amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  target_card_id: table.zs_observe.amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_binds_to_table.table_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_binds_to_table.table_zs_observe_amazon_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  target_card_id: table.zs_observe.amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: table.zs_observe.shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: table.zs_observe.shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
  target_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_rosenza_international_trading_l_l_c_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_rosenza_international_trading_l_l_c_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  target_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_rosenza_international_trading_l_l_c_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_rosenza_international_trading_l_l_c_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
  target_card_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform.platform_amazon
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_platform.platform_shopify
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  target_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_international
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_rosenza_international_trading_l_l_c_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_belongs_to_tenant.tenant_rosenza_international_trading_l_l_c

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_belongs_to_tenant.tenant_rosenza_international_trading_l_l_c
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: tenant.rosenza_international_trading_l_l_c
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_business_flow_binding.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_business_flow_binding.business_flow_binding_rosenza_international_trading_l_l_c_marketplace_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: business_flow_binding.rosenza_international_trading_l_l_c.marketplace_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_business_flow_binding.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_business_flow_binding.business_flow_binding_rosenza_international_trading_l_l_c_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: business_flow_binding.rosenza_international_trading_l_l_c.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_business_scope_set.business_scope_set_rosenza_international_trading_l_l_c_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_business_scope_set.business_scope_set_rosenza_international_trading_l_l_c_marketplace
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: business_scope_set.rosenza_international_trading_l_l_c.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_business_scope_set.business_scope_set_rosenza_international_trading_l_l_c_oms

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_business_scope_set.business_scope_set_rosenza_international_trading_l_l_c_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: business_scope_set.rosenza_international_trading_l_l_c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.group_rosenza_international_trading_l_l_c_g9_gl133.group_has_platform_account.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  target_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_belongs_to_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_canada_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_canada.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_france_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_france.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_germany_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_germany.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_ksa_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_ksa.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_mexico_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_mexico.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_spain_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_spain.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_sweden_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_sweden.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uae_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uae.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_uk_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_uk.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_fee_preview_zs_observe_amazon_fee_preview
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_oms_sales_zs_observe_amazon_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_returns_zs_observe_amazon_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_amazon_us_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.amazon_us.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_rosenza_international_trading_l_l_c_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  target_card_id: account_data_binding.rosenza_international_trading_l_l_c.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_uses_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_uses_platform.platform_shopify
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_canada_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_canada.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_france_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_france.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_germany_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_germany.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_ksa_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_ksa.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_mexico_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_mexico.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace.platform_account_uses_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_spain_marketplace.platform_account_uses_platform_context.platform_context_amazon_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_spain.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_sweden_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_sweden.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_uae_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uae.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_uk_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_uk.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_amazon_us_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.amazon_us.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_rosenza_international_trading_l_l_c_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.rosenza_international_trading_l_l_c.shopify_d2c.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### TENANT_HAS_GROUP

#### edge.tenant_rosenza_international_trading_l_l_c.tenant_has_group.group_rosenza_international_trading_l_l_c_g9_gl133

```yaml
canonical_edge:
  edge_id: edge.tenant_rosenza_international_trading_l_l_c.tenant_has_group.group_rosenza_international_trading_l_l_c_g9_gl133
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.rosenza_international_trading_l_l_c
  target_card_id: group.rosenza_international_trading_l_l_c.g9.gl133
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```
