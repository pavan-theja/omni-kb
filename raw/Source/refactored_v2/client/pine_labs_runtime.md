# Pine Labs — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `pine_labs_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Nearby Settlement → nearby_marketplace
  config: ''
  reason: Nearby marketplace/partner pack not uploaded
- label: Maximize Pay
  config: maximize_settlement (multi-sheet)
  reason: Fintech/partner pack not uploaded
- label: Credit limit report credit_limit_report
  config: Credit-based GC program limits
  reason: Cred marketplace pack not uploaded
- label: Amazon / Flipkart / Paytm / PhonePe gift-card distribution
  config: Gift-card/SVC settlement and partner reports
  reason: Gift-card distribution semantics are not the same as standard e-commerce marketplace seller packs; wait
    for Pine/Woohoo/partner domain packs.
- label: Flipkart gift-card settlement
  config: settlement + adhoc ads/TDS/rebates/VAS
  reason: Flipkart partner settlement for Pine Labs is not represented in the uploaded OMS Business KB tables; marketplace
    pack may cover generic Flipkart settlement but not Pine gift-card-specific partner settlement.
  source_family: oms
- label: PhonePe settlement report
  config: settlement report + mapper
  reason: No PhonePe gift-card settlement/mapper canonical OMS tables in uploaded OMS packs.
  source_family: oms
- label: Woohoo Adhoc
  config: woohoo_oms_adhoc
  reason: No woohoo_oms_adhoc table card in uploaded OMS packs.
  source_family: oms
- label: Maximize Pay
  config: maximize_settlement
  reason: No Maximize Pay canonical OMS table card in uploaded OMS packs.
  source_family: oms
- label: Navi
  config: navi_settlement
  reason: No Navi canonical OMS table card in uploaded OMS packs.
  source_family: oms
- label: DreamPlug
  config: dreamplug_settlement
  reason: No DreamPlug canonical OMS table card in uploaded OMS packs.
  source_family: oms
- label: Tata Digital
  config: tata_digital_settlement
  reason: No Tata Digital canonical OMS table card in uploaded OMS packs.
  source_family: oms
- label: Pinelabs commission invoice
  config: pinelabs_commission_invoice
  reason: No pinelabs_commission_invoice table card in uploaded OMS packs.
  source_family: oms
- label: Pinelabs tally
  config: pinelabs_tally
  reason: No pinelabs_tally table card in uploaded OMS packs.
  source_family: oms
- label: Pinelabs adhoc amount
  config: pinelab_adhoc_amount
  reason: No pinelab_adhoc_amount table card in uploaded OMS packs.
  source_family: oms
- label: Pine PG
  config: pine_payments
  reason: No pine_payments table card in uploaded OMS packs; payment gateway pack expected later.
  source_family: oms
- label: Amazon.in mapper
  config: amazon_in_mapper
  reason: No amazon_in_mapper table card in uploaded OMS packs.
  source_family: oms
- label: PhonePe mapper
  config: phonepe_mapper
  reason: No phonepe_mapper table card in uploaded OMS packs.
  source_family: oms
- label: Treasury reports
  config: revalidation_report, sclp_billing_report, credit_limit_report, ignore_card_number_report, merchant_interest_sheet
  reason: Treasury/stored-card-liability reports are outside the uploaded OMS packs and should be integrated only
    with a treasury/liability pack.
  source_family: oms
- label: PayU
  config: payu_settlement
  reason: No PayU canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
- label: PhonePe settlement
  config: phonepe_settlement
  reason: Uploaded payment_gateway.md has PhonePe pay-in only, not phonepe_settlement; exact Pine Labs settlement
    report needs a canonical table before binding
  source_family: payment_gateway
- label: IndusInd Bank
  config: indusind_bank_statement
  reason: No IndusInd canonical platform/table cards in uploaded bank_statement.md
  source_family: bank_statement
- label: Maximize Pay / DreamPlug / Amica Technologies / First Pay / Red Giraffe / Gullak Technologies
  config: fintech settlement files
  reason: No matching canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 9
  account_data_binding: 14
  business_scope_set: 2
  business_flow_binding: 2
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 20
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 14
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 14
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 2
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 14
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 9
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 2
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 2
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 14
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 5
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 9
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 5
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 2
  GROUP_HAS_BUSINESS_SCOPE_SET: 2
  GROUP_HAS_PLATFORM_ACCOUNT: 9
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 9
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 14
  PLATFORM_ACCOUNT_USES_PLATFORM: 9
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 9
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
- payment_gateway
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
  added_runtime_cards: 10
  added_runtime_edges: 57
  supported_payment_bindings: 4
  supported_bank_bindings: 0
  deferred_financial_sources_added_or_updated: 4
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.pine_labs

```yaml
canonical_card:
  canonical_id: tenant.pine_labs
  card_type: tenant
  canonical_name: Pine Labs
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs
    - pine_labs
    - Pine Labs runtime tenant
    colloquial_phrases:
    - Pine Labs client runtime
    - Pine Labs source configuration
    - Pine Labs scoped reconciliation setup
    business_meaning: Runtime tenant identity for Pine Labs. It anchors the client's marketplace, logistics, OMS,
      WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from reusable domain
      semantics.
    business_questions:
    - Which source families and configured accounts belong to Pine Labs?
    - Which group and account bindings should constrain Pine Labs's SQL handoff?
    - After Pine Labs's runtime scope is resolved, which domain layer should receive the query next?
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
    - tenant_id:tenant.pine_labs
    embedding_text: Pine Labs is the runtime tenant root for the client's marketplace, logistics, OMS, WMS, payment-gateway,
      and bank-statement configuration. Use it to reach group, platform-account, and account-data-binding nodes
      before invoking reusable canonical packs.
    search_keywords:
    - Pine Labs
    - pine_labs
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.pine_labs
  evidence:
    source_documents:
    - Pine Labs.docx
    source_path: Pine Labs.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
  fields:
    tenant_slug: pine_labs
    tenant_name: Pine Labs
    legal_name: Pine Labs
    active: true
```

### 2.2 Group Cards

#### group.pine_labs.g44.gl168

```yaml
canonical_card:
  canonical_id: group.pine_labs.g44.gl168
  card_type: group
  canonical_name: Pine Labs group 44/168
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs Private Limited
    - Pine Labs group 44/168
    - group_id 44
    - group_level_id 168
    colloquial_phrases:
    - Pine Labs group scope
    - Pine Labs Private Limited runtime scope
    - group 44 level 168 query boundary
    business_meaning: 'Runtime group scope for Pine Labs: group_id=44 and group_level_id=168. It is the client-specific
      filter boundary that must be applied before resolving account bindings for IN in INR.'
    business_questions:
    - Which bindings use group_id=44 and group_level_id=168?
    - Which source families are active under Pine Labs Private Limited?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=44
    - group_level_id=168
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - group_id_value:44
    - group_level_id_value:168
    embedding_text: Pine Labs Private Limited is the runtime group node for Pine Labs. Apply group_id=44 and group_level_id=168
      when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Pine Labs
    - Pine Labs Private Limited
    - group_id 44
    - group_level_id 168
    - runtime group scope
    exact_match_keys:
    - group.pine_labs.g44.gl168
  evidence:
    source_documents:
    - Pine Labs.docx
    source_path: Pine Labs.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    group_level_id: '168'
  fields:
    tenant_id: tenant.pine_labs
    group_id_value: '44'
    group_level_id_value: '168'
    group_name: Pine Labs Private Limited
    default_currency: INR
    country: IN
```

### 2.3 Platform Account Cards

#### platform_account.pine_labs.amazon_giftcard_settlement.oms

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  card_type: platform_account
  canonical_name: Pine Labs Amazon Gift Card Settlement account
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs Amazon Gift Card Settlement account
    - Pine Labs Pine Labs Amazon Gift Card Settlement account
    - Zenstatement Oms Business Kb
    - Pine Labs Amazon Gift Card Settlement account OMS account
    colloquial_phrases:
    - Pine Labs Pine Labs Amazon Gift Card Settlement account source account
    - Pine Labs Amazon Gift Card Settlement account OMS runtime account
    - Pine Labs Amazon Gift Card Settlement account configured source family
    business_meaning: Runtime platform account for Pine Labs's Pine Labs Amazon Gift Card Settlement account OMS
      sources. It points traversal to platform.zenstatement_oms_business_kb and platform_context.zenstatement.oms_business_kb
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Pine Labs Amazon Gift Card Settlement account table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Pine Labs Amazon Gift Card Settlement account questions
      traverse through?
    - Which source roles under Pine Labs Amazon Gift Card Settlement account are active or review-required for this
      client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: Amazon GC settlement, NAB settlement, and SVC transaction context where supported'
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.amazon_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - runtime_source_family:oms
    embedding_text: Pine Labs's Pine Labs Amazon Gift Card Settlement account platform account routes OMS questions
      to platform.zenstatement_oms_business_kb / platform_context.zenstatement.oms_business_kb. Use it to collect
      the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Pine Labs Amazon Gift Card Settlement account
    - Zenstatement Oms Business Kb
    - OMS
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    exact_match_keys:
    - platform_account.pine_labs.amazon_giftcard_settlement.oms
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    runtime_source_family: oms
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_name: Pine Labs Amazon Gift Card Settlement account
    account_type: partner_settlement_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Amazon GC settlement, NAB settlement, and SVC transaction context where supported
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```

#### platform_account.pine_labs.amazon_seller_flex_oms.oms

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  card_type: platform_account
  canonical_name: Pine Labs Amazon Seller Flex OMS account
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs Amazon Seller Flex OMS account
    - Pine Labs Pine Labs Amazon Seller Flex OMS account
    - Zenstatement Oms Business Kb
    - Pine Labs Amazon Seller Flex OMS account OMS account
    colloquial_phrases:
    - Pine Labs Pine Labs Amazon Seller Flex OMS account source account
    - Pine Labs Amazon Seller Flex OMS account OMS runtime account
    - Pine Labs Amazon Seller Flex OMS account configured source family
    business_meaning: Runtime platform account for Pine Labs's Pine Labs Amazon Seller Flex OMS account OMS sources.
      It points traversal to platform.zenstatement_oms_business_kb and platform_context.zenstatement.oms_business_kb
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Pine Labs Amazon Seller Flex OMS account table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Pine Labs Amazon Seller Flex OMS account questions traverse
      through?
    - Which source roles under Pine Labs Amazon Seller Flex OMS account are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: Amazon Seller Flex fulfilment and gift-card activation data'
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.amazon_seller_flex_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - runtime_source_family:oms
    embedding_text: Pine Labs's Pine Labs Amazon Seller Flex OMS account platform account routes OMS questions to
      platform.zenstatement_oms_business_kb / platform_context.zenstatement.oms_business_kb. Use it to collect the
      client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Pine Labs Amazon Seller Flex OMS account
    - Zenstatement Oms Business Kb
    - OMS
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    exact_match_keys:
    - platform_account.pine_labs.amazon_seller_flex_oms.oms
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    runtime_source_family: oms
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_name: Pine Labs Amazon Seller Flex OMS account
    account_type: gift_card_activation_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Amazon Seller Flex fulfilment and gift-card activation data
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```

#### platform_account.pine_labs.partner_giftcard_settlement.oms

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  card_type: platform_account
  canonical_name: Pine Labs B2B Partner Gift Card Settlements account
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs B2B Partner Gift Card Settlements account
    - Pine Labs Pine Labs B2B Partner Gift Card Settlements account
    - Zenstatement Oms Business Kb
    - Pine Labs B2B Partner Gift Card Settlements account OMS account
    colloquial_phrases:
    - Pine Labs Pine Labs B2B Partner Gift Card Settlements account source account
    - Pine Labs B2B Partner Gift Card Settlements account OMS runtime account
    - Pine Labs B2B Partner Gift Card Settlements account configured source family
    business_meaning: Runtime platform account for Pine Labs's Pine Labs B2B Partner Gift Card Settlements account
      OMS sources. It points traversal to platform.zenstatement_oms_business_kb and platform_context.zenstatement.oms_business_kb
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Pine Labs B2B Partner Gift Card Settlements account table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Pine Labs B2B Partner Gift Card Settlements account questions
      traverse through?
    - Which source roles under Pine Labs B2B Partner Gift Card Settlements account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement
      files'
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.partner_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - runtime_source_family:oms
    embedding_text: Pine Labs's Pine Labs B2B Partner Gift Card Settlements account platform account routes OMS
      questions to platform.zenstatement_oms_business_kb / platform_context.zenstatement.oms_business_kb. Use it
      to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Pine Labs B2B Partner Gift Card Settlements account
    - Zenstatement Oms Business Kb
    - OMS
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    exact_match_keys:
    - platform_account.pine_labs.partner_giftcard_settlement.oms
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    runtime_source_family: oms
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_name: Pine Labs B2B Partner Gift Card Settlements account
    account_type: partner_settlement_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement
      files
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```

#### platform_account.pine_labs.pinelabs_accounts_receivable.oms

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  card_type: platform_account
  canonical_name: Pine Labs Pine Labs Accounts Receivable SOA account
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs Pine Labs Accounts Receivable SOA account
    - Pine Labs Pine Labs Pine Labs Accounts Receivable SOA account
    - Zenstatement Oms Business Kb
    - Pine Labs Pine Labs Accounts Receivable SOA account OMS account
    colloquial_phrases:
    - Pine Labs Pine Labs Pine Labs Accounts Receivable SOA account source account
    - Pine Labs Pine Labs Accounts Receivable SOA account OMS runtime account
    - Pine Labs Pine Labs Accounts Receivable SOA account configured source family
    business_meaning: Runtime platform account for Pine Labs's Pine Labs Pine Labs Accounts Receivable SOA account
      OMS sources. It points traversal to platform.zenstatement_oms_business_kb and platform_context.zenstatement.oms_business_kb
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Pine Labs Pine Labs Accounts Receivable SOA account table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Pine Labs Pine Labs Accounts Receivable SOA account questions
      traverse through?
    - Which source roles under Pine Labs Pine Labs Accounts Receivable SOA account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: Pinelabs SOA accounts receivable statement'
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.pinelabs_accounts_receivable.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - runtime_source_family:oms
    embedding_text: Pine Labs's Pine Labs Pine Labs Accounts Receivable SOA account platform account routes OMS
      questions to platform.zenstatement_oms_business_kb / platform_context.zenstatement.oms_business_kb. Use it
      to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Pine Labs Pine Labs Accounts Receivable SOA account
    - Zenstatement Oms Business Kb
    - OMS
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    exact_match_keys:
    - platform_account.pine_labs.pinelabs_accounts_receivable.oms
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    runtime_source_family: oms
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_name: Pine Labs Pine Labs Accounts Receivable SOA account
    account_type: accounts_receivable_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Pinelabs SOA accounts receivable statement
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```

#### platform_account.pine_labs.woohoo_giftcard_oms.oms

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  card_type: platform_account
  canonical_name: Pine Labs Woohoo Gift Card OMS account
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs Woohoo Gift Card OMS account
    - Pine Labs Pine Labs Woohoo Gift Card OMS account
    - Zenstatement Oms Business Kb
    - Pine Labs Woohoo Gift Card OMS account OMS account
    colloquial_phrases:
    - Pine Labs Pine Labs Woohoo Gift Card OMS account source account
    - Pine Labs Woohoo Gift Card OMS account OMS runtime account
    - Pine Labs Woohoo Gift Card OMS account configured source family
    business_meaning: Runtime platform account for Pine Labs's Pine Labs Woohoo Gift Card OMS account OMS sources.
      It points traversal to platform.zenstatement_oms_business_kb and platform_context.zenstatement.oms_business_kb
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Pine Labs Woohoo Gift Card OMS account table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Pine Labs Woohoo Gift Card OMS account questions traverse
      through?
    - Which source roles under Pine Labs Woohoo Gift Card OMS account are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: Woohoo OMS, OMS rectified/corrections, and adhoc gift card order context'
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.woohoo_giftcard_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - runtime_source_family:oms
    embedding_text: Pine Labs's Pine Labs Woohoo Gift Card OMS account platform account routes OMS questions to
      platform.zenstatement_oms_business_kb / platform_context.zenstatement.oms_business_kb. Use it to collect the
      client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Pine Labs Woohoo Gift Card OMS account
    - Zenstatement Oms Business Kb
    - OMS
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    exact_match_keys:
    - platform_account.pine_labs.woohoo_giftcard_oms.oms
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    runtime_source_family: oms
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_name: Pine Labs Woohoo Gift Card OMS account
    account_type: gift_card_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Woohoo OMS, OMS rectified/corrections, and adhoc gift card order context
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```

#### platform_account.pine_labs.cashfree.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.cashfree.payment_gateway
  card_type: platform_account
  canonical_name: Pine Labs — Cashfree payment gateway
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Cashfree
    - Pine Labs Cashfree
    - Cashfree payment gateway account
    colloquial_phrases:
    - Pine Labs Cashfree source account
    - Cashfree payment gateway runtime account
    - Cashfree configured source family
    business_meaning: Runtime platform account for Pine Labs's Cashfree payment gateway sources. It points traversal
      to platform.cashfree and platform_context.cashfree.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Cashfree table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Cashfree questions traverse through?
    - Which source roles under Cashfree are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: Cashfree'
    - platform.cashfree
    - platform_context.cashfree.in
    - Cashfree
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_id:platform.cashfree
    - platform_context_id:platform_context.cashfree.in
    - platform_account_id:platform_account.pine_labs.cashfree.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Pine Labs's Cashfree platform account routes payment gateway questions to platform.cashfree
      / platform_context.cashfree.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Cashfree
    - payment gateway
    - platform.cashfree
    - platform_context.cashfree.in
    exact_match_keys:
    - platform_account.pine_labs.cashfree.payment_gateway
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: Pine Labs.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    platform_account_id: platform_account.pine_labs.cashfree.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    account_name: Cashfree
    account_type: payment_gateway_account
    source_account_identifier: Cashfree
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```

#### platform_account.pine_labs.paytm.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.paytm.payment_gateway
  card_type: platform_account
  canonical_name: Pine Labs — Paytm payment gateway
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Paytm
    - Pine Labs Paytm
    - Paytm payment gateway account
    colloquial_phrases:
    - Pine Labs Paytm source account
    - Paytm payment gateway runtime account
    - Paytm configured source family
    business_meaning: Runtime platform account for Pine Labs's Paytm payment gateway sources. It points traversal
      to platform.paytm and platform_context.paytm.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Paytm table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Paytm questions traverse through?
    - Which source roles under Paytm are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: Paytm'
    - platform.paytm
    - platform_context.paytm.in
    - Paytm
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_id:platform.paytm
    - platform_context_id:platform_context.paytm.in
    - platform_account_id:platform_account.pine_labs.paytm.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Pine Labs's Paytm platform account routes payment gateway questions to platform.paytm / platform_context.paytm.in.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Paytm
    - payment gateway
    - platform.paytm
    - platform_context.paytm.in
    exact_match_keys:
    - platform_account.pine_labs.paytm.payment_gateway
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: Pine Labs.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    platform_account_id: platform_account.pine_labs.paytm.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    account_name: Paytm
    account_type: payment_gateway_account
    source_account_identifier: Paytm
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```

#### platform_account.pine_labs.navi.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.navi.payment_gateway
  card_type: platform_account
  canonical_name: Pine Labs — Navi payment gateway
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Navi
    - Pine Labs Navi
    - Navi payment gateway account
    colloquial_phrases:
    - Pine Labs Navi source account
    - Navi payment gateway runtime account
    - Navi configured source family
    business_meaning: Runtime platform account for Pine Labs's Navi payment gateway sources. It points traversal
      to platform.navi and platform_context.navi.in and groups the client's table-level account-data bindings for
      this source.
    business_questions:
    - Which Navi table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Navi questions traverse through?
    - Which source roles under Navi are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: Navi'
    - platform.navi
    - platform_context.navi.in
    - Navi
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_id:platform.navi
    - platform_context_id:platform_context.navi.in
    - platform_account_id:platform_account.pine_labs.navi.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Pine Labs's Navi platform account routes payment gateway questions to platform.navi / platform_context.navi.in.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Navi
    - payment gateway
    - platform.navi
    - platform_context.navi.in
    exact_match_keys:
    - platform_account.pine_labs.navi.payment_gateway
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: Pine Labs.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.navi
    platform_context_id: platform_context.navi.in
    platform_account_id: platform_account.pine_labs.navi.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.navi
    platform_context_id: platform_context.navi.in
    account_name: Navi
    account_type: fintech_settlement_account
    source_account_identifier: Navi
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```

#### platform_account.pine_labs.tata_digital.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.pine_labs.tata_digital.payment_gateway
  card_type: platform_account
  canonical_name: Pine Labs — Tata Digital / Tata Neu payment gateway
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Tata Digital / Tata Neu
    - Pine Labs Tata Digital / Tata Neu
    - Tata Digital
    - Tata Digital / Tata Neu payment gateway account
    colloquial_phrases:
    - Pine Labs Tata Digital / Tata Neu source account
    - Tata Digital / Tata Neu payment gateway runtime account
    - Tata Digital / Tata Neu configured source family
    business_meaning: Runtime platform account for Pine Labs's Tata Digital / Tata Neu payment gateway sources.
      It points traversal to platform.tata_digital and platform_context.tata_digital.in and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Tata Digital / Tata Neu table bindings are available for Pine Labs?
    - Which canonical platform/context should Pine Labs's Tata Digital / Tata Neu questions traverse through?
    - Which source roles under Tata Digital / Tata Neu are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: Tata Digital / Tata Neu'
    - platform.tata_digital
    - platform_context.tata_digital.in
    - Tata Digital / Tata Neu
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_id:platform.tata_digital
    - platform_context_id:platform_context.tata_digital.in
    - platform_account_id:platform_account.pine_labs.tata_digital.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Pine Labs's Tata Digital / Tata Neu platform account routes payment gateway questions to platform.tata_digital
      / platform_context.tata_digital.in. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Pine Labs
    - Tata Digital / Tata Neu
    - Tata Digital
    - payment gateway
    - platform.tata_digital
    - platform_context.tata_digital.in
    exact_match_keys:
    - platform_account.pine_labs.tata_digital.payment_gateway
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: Pine Labs.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.tata_digital
    platform_context_id: platform_context.tata_digital.in
    platform_account_id: platform_account.pine_labs.tata_digital.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_id: platform.tata_digital
    platform_context_id: platform_context.tata_digital.in
    account_name: Tata Digital / Tata Neu
    account_type: fintech_settlement_account
    source_account_identifier: Tata Digital / Tata Neu
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '44'
      group_level_id: '168'
```


### 2.4 Account Data Binding Cards

#### account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  card_type: account_data_binding
  canonical_name: Pine Labs Amazon Gift Card Settlement amazon_giftcard_settlement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon Gift Card Settlement amazon giftcard settlement
    - amazon_gc_settlement
    - zs_observe.amazon_gc_settlement
    - Amazon GC settlement, NAB settlement, and SVC transaction context where supported
    - Pine Labs Amazon Gift Card Settlement amazon giftcard settlement
    colloquial_phrases:
    - Pine Labs Amazon Gift Card Settlement amazon giftcard settlement source
    - Amazon Gift Card Settlement amazon giftcard settlement runtime binding
    - amazon_gc_settlement for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's Amazon Gift Card Settlement
      amazon giftcard settlement evidence should use zs_observe.amazon_gc_settlement. Apply group_id=44, group_level_id=168
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon Gift Card Settlement OMS rows should answer Pine Labs's amazon giftcard settlement question?
    - Which runtime scope must be injected before using amazon_gc_settlement?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - amazon_giftcard_settlement
    included_concepts:
    - zs_observe.amazon_gc_settlement
    - amazon giftcard settlement
    - Amazon Gift Card Settlement
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.amazon_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:amazon_giftcard_settlement
    - table_id:table.zs_observe.amazon_gc_settlement
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the Amazon Gift Card Settlement amazon giftcard settlement binding selects zs_observe.amazon_gc_settlement
      as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable semantics come from oms_business_kb.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - Amazon Gift Card Settlement
    - amazon giftcard settlement
    - OMS
    - zs_observe.amazon_gc_settlement
    - amazon_gc_settlement
    - amazon_giftcard_settlement
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
    domain_id: domain.oms_business.amazon_gift_card_settlement
    table_id: table.zs_observe.amazon_gc_settlement
    source_role: amazon_giftcard_settlement
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
    domain_id: domain.oms_business.amazon_gift_card_settlement
    table_id: table.zs_observe.amazon_gc_settlement
    source_role: amazon_giftcard_settlement
    source_entity: Amazon Gift Card Settlement
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Amazon GC settlement, NAB settlement, and SVC transaction context where supported
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  card_type: account_data_binding
  canonical_name: Pine Labs Amazon Seller Flex OMS giftcard_activation_oms binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon Seller Flex OMS giftcard activation oms
    - amazon_seller_flex
    - zs_observe.amazon_seller_flex
    - Amazon Seller Flex fulfilment and gift-card activation data
    - Pine Labs Amazon Seller Flex OMS giftcard activation oms
    colloquial_phrases:
    - Pine Labs Amazon Seller Flex OMS giftcard activation oms source
    - Amazon Seller Flex OMS giftcard activation oms runtime binding
    - amazon_seller_flex for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's Amazon Seller Flex OMS giftcard
      activation oms evidence should use zs_observe.amazon_seller_flex. Apply group_id=44, group_level_id=168 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon Seller Flex OMS OMS rows should answer Pine Labs's giftcard activation oms question?
    - Which runtime scope must be injected before using amazon_seller_flex?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - giftcard_activation_oms
    included_concepts:
    - zs_observe.amazon_seller_flex
    - giftcard activation oms
    - Amazon Seller Flex OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.amazon_seller_flex_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:giftcard_activation_oms
    - table_id:table.zs_observe.amazon_seller_flex
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the Amazon Seller Flex OMS giftcard activation oms binding selects zs_observe.amazon_seller_flex
      as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable semantics come from oms_business_kb.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - Amazon Seller Flex OMS
    - giftcard activation oms
    - OMS
    - zs_observe.amazon_seller_flex
    - amazon_seller_flex
    - giftcard_activation_oms
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
    domain_id: domain.oms_business.gift_card_oms
    table_id: table.zs_observe.amazon_seller_flex
    source_role: giftcard_activation_oms
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
    domain_id: domain.oms_business.gift_card_oms
    table_id: table.zs_observe.amazon_seller_flex
    source_role: giftcard_activation_oms
    source_entity: Amazon Seller Flex OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Amazon Seller Flex fulfilment and gift-card activation data
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  card_type: account_data_binding
  canonical_name: Pine Labs B2B Partner Gift Card Settlements partner_giftcard_settlement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - B2B Partner Gift Card Settlements partner giftcard settlement
    - amica_technologies_settlement
    - zs_observe.amica_technologies_settlement
    - Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement files
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement
    colloquial_phrases:
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement source
    - B2B Partner Gift Card Settlements partner giftcard settlement runtime binding
    - amica_technologies_settlement for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's B2B Partner Gift Card Settlements
      partner giftcard settlement evidence should use zs_observe.amica_technologies_settlement. Apply group_id=44,
      group_level_id=168 before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which B2B Partner Gift Card Settlements OMS rows should answer Pine Labs's partner giftcard settlement question?
    - Which runtime scope must be injected before using amica_technologies_settlement?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - partner_giftcard_settlement
    included_concepts:
    - zs_observe.amica_technologies_settlement
    - partner giftcard settlement
    - B2B Partner Gift Card Settlements
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.partner_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:partner_giftcard_settlement
    - table_id:table.zs_observe.amica_technologies_settlement
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the B2B Partner Gift Card Settlements partner giftcard settlement binding selects
      zs_observe.amica_technologies_settlement as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable
      semantics come from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution,
      not for defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - B2B Partner Gift Card Settlements
    - partner giftcard settlement
    - OMS
    - zs_observe.amica_technologies_settlement
    - amica_technologies_settlement
    - partner_giftcard_settlement
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.amica_technologies_settlement
    source_role: partner_giftcard_settlement
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.amica_technologies_settlement
    source_role: partner_giftcard_settlement
    source_entity: B2B Partner Gift Card Settlements
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement
      files
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  card_type: account_data_binding
  canonical_name: Pine Labs B2B Partner Gift Card Settlements partner_giftcard_settlement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - B2B Partner Gift Card Settlements partner giftcard settlement
    - first_pay_settlement
    - zs_observe.first_pay_settlement
    - Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement files
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement
    colloquial_phrases:
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement source
    - B2B Partner Gift Card Settlements partner giftcard settlement runtime binding
    - first_pay_settlement for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's B2B Partner Gift Card Settlements
      partner giftcard settlement evidence should use zs_observe.first_pay_settlement. Apply group_id=44, group_level_id=168
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which B2B Partner Gift Card Settlements OMS rows should answer Pine Labs's partner giftcard settlement question?
    - Which runtime scope must be injected before using first_pay_settlement?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - partner_giftcard_settlement
    included_concepts:
    - zs_observe.first_pay_settlement
    - partner giftcard settlement
    - B2B Partner Gift Card Settlements
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.partner_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:partner_giftcard_settlement
    - table_id:table.zs_observe.first_pay_settlement
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the B2B Partner Gift Card Settlements partner giftcard settlement binding selects
      zs_observe.first_pay_settlement as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable semantics
      come from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution, not for
      defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - B2B Partner Gift Card Settlements
    - partner giftcard settlement
    - OMS
    - zs_observe.first_pay_settlement
    - first_pay_settlement
    - partner_giftcard_settlement
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.first_pay_settlement
    source_role: partner_giftcard_settlement
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.first_pay_settlement
    source_role: partner_giftcard_settlement
    source_entity: B2B Partner Gift Card Settlements
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement
      files
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  card_type: account_data_binding
  canonical_name: Pine Labs B2B Partner Gift Card Settlements partner_giftcard_settlement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - B2B Partner Gift Card Settlements partner giftcard settlement
    - gullak_technologies_settlement
    - zs_observe.gullak_technologies_settlement
    - Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement files
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement
    colloquial_phrases:
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement source
    - B2B Partner Gift Card Settlements partner giftcard settlement runtime binding
    - gullak_technologies_settlement for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's B2B Partner Gift Card Settlements
      partner giftcard settlement evidence should use zs_observe.gullak_technologies_settlement. Apply group_id=44,
      group_level_id=168 before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which B2B Partner Gift Card Settlements OMS rows should answer Pine Labs's partner giftcard settlement question?
    - Which runtime scope must be injected before using gullak_technologies_settlement?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - partner_giftcard_settlement
    included_concepts:
    - zs_observe.gullak_technologies_settlement
    - partner giftcard settlement
    - B2B Partner Gift Card Settlements
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.partner_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:partner_giftcard_settlement
    - table_id:table.zs_observe.gullak_technologies_settlement
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the B2B Partner Gift Card Settlements partner giftcard settlement binding selects
      zs_observe.gullak_technologies_settlement as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable
      semantics come from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution,
      not for defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - B2B Partner Gift Card Settlements
    - partner giftcard settlement
    - OMS
    - zs_observe.gullak_technologies_settlement
    - gullak_technologies_settlement
    - partner_giftcard_settlement
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.gullak_technologies_settlement
    source_role: partner_giftcard_settlement
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.gullak_technologies_settlement
    source_role: partner_giftcard_settlement
    source_entity: B2B Partner Gift Card Settlements
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement
      files
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  card_type: account_data_binding
  canonical_name: Pine Labs B2B Partner Gift Card Settlements partner_giftcard_settlement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - B2B Partner Gift Card Settlements partner giftcard settlement
    - nearby_marketplace
    - zs_observe.nearby_marketplace
    - Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement files
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement
    colloquial_phrases:
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement source
    - B2B Partner Gift Card Settlements partner giftcard settlement runtime binding
    - nearby_marketplace for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's B2B Partner Gift Card Settlements
      partner giftcard settlement evidence should use zs_observe.nearby_marketplace. Apply group_id=44, group_level_id=168
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which B2B Partner Gift Card Settlements OMS rows should answer Pine Labs's partner giftcard settlement question?
    - Which runtime scope must be injected before using nearby_marketplace?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - partner_giftcard_settlement
    included_concepts:
    - zs_observe.nearby_marketplace
    - partner giftcard settlement
    - B2B Partner Gift Card Settlements
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.partner_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:partner_giftcard_settlement
    - table_id:table.zs_observe.nearby_marketplace
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the B2B Partner Gift Card Settlements partner giftcard settlement binding selects
      zs_observe.nearby_marketplace as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable semantics
      come from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution, not for
      defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - B2B Partner Gift Card Settlements
    - partner giftcard settlement
    - OMS
    - zs_observe.nearby_marketplace
    - nearby_marketplace
    - partner_giftcard_settlement
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.nearby_marketplace
    source_role: partner_giftcard_settlement
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.nearby_marketplace
    source_role: partner_giftcard_settlement
    source_entity: B2B Partner Gift Card Settlements
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement
      files
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  card_type: account_data_binding
  canonical_name: Pine Labs B2B Partner Gift Card Settlements partner_giftcard_settlement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - B2B Partner Gift Card Settlements partner giftcard settlement
    - paytm_giftcard_settlement
    - zs_observe.paytm_giftcard_settlement
    - Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement files
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement
    colloquial_phrases:
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement source
    - B2B Partner Gift Card Settlements partner giftcard settlement runtime binding
    - paytm_giftcard_settlement for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's B2B Partner Gift Card Settlements
      partner giftcard settlement evidence should use zs_observe.paytm_giftcard_settlement. Apply group_id=44, group_level_id=168
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which B2B Partner Gift Card Settlements OMS rows should answer Pine Labs's partner giftcard settlement question?
    - Which runtime scope must be injected before using paytm_giftcard_settlement?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - partner_giftcard_settlement
    included_concepts:
    - zs_observe.paytm_giftcard_settlement
    - partner giftcard settlement
    - B2B Partner Gift Card Settlements
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.partner_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:partner_giftcard_settlement
    - table_id:table.zs_observe.paytm_giftcard_settlement
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the B2B Partner Gift Card Settlements partner giftcard settlement binding selects
      zs_observe.paytm_giftcard_settlement as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable semantics
      come from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution, not for
      defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - B2B Partner Gift Card Settlements
    - partner giftcard settlement
    - OMS
    - zs_observe.paytm_giftcard_settlement
    - paytm_giftcard_settlement
    - partner_giftcard_settlement
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.paytm_giftcard_settlement
    source_role: partner_giftcard_settlement
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.paytm_giftcard_settlement
    source_role: partner_giftcard_settlement
    source_entity: B2B Partner Gift Card Settlements
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement
      files
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  card_type: account_data_binding
  canonical_name: Pine Labs B2B Partner Gift Card Settlements partner_giftcard_settlement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - B2B Partner Gift Card Settlements partner giftcard settlement
    - red_giraffe_settlement
    - zs_observe.red_giraffe_settlement
    - Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement files
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement
    colloquial_phrases:
    - Pine Labs B2B Partner Gift Card Settlements partner giftcard settlement source
    - B2B Partner Gift Card Settlements partner giftcard settlement runtime binding
    - red_giraffe_settlement for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's B2B Partner Gift Card Settlements
      partner giftcard settlement evidence should use zs_observe.red_giraffe_settlement. Apply group_id=44, group_level_id=168
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which B2B Partner Gift Card Settlements OMS rows should answer Pine Labs's partner giftcard settlement question?
    - Which runtime scope must be injected before using red_giraffe_settlement?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - partner_giftcard_settlement
    included_concepts:
    - zs_observe.red_giraffe_settlement
    - partner giftcard settlement
    - B2B Partner Gift Card Settlements
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.partner_giftcard_settlement.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:partner_giftcard_settlement
    - table_id:table.zs_observe.red_giraffe_settlement
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the B2B Partner Gift Card Settlements partner giftcard settlement binding selects
      zs_observe.red_giraffe_settlement as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable semantics
      come from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution, not for
      defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - B2B Partner Gift Card Settlements
    - partner giftcard settlement
    - OMS
    - zs_observe.red_giraffe_settlement
    - red_giraffe_settlement
    - partner_giftcard_settlement
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.red_giraffe_settlement
    source_role: partner_giftcard_settlement
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
    domain_id: domain.oms_business.partner_settlement
    table_id: table.zs_observe.red_giraffe_settlement
    source_role: partner_giftcard_settlement
    source_entity: B2B Partner Gift Card Settlements
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Gullak, Paytm, Red Giraffe, Nearby, FirstPay, and Amica/Jupiter partner settlement
      files
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  card_type: account_data_binding
  canonical_name: Pine Labs Pine Labs Accounts Receivable SOA accounts_receivable_statement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs Accounts Receivable SOA accounts receivable statement
    - pinelabs_soa
    - zs_observe.pinelabs_soa
    - Pinelabs SOA accounts receivable statement
    - Pine Labs Pine Labs Accounts Receivable SOA accounts receivable statement
    colloquial_phrases:
    - Pine Labs Pine Labs Accounts Receivable SOA accounts receivable statement source
    - Pine Labs Accounts Receivable SOA accounts receivable statement runtime binding
    - pinelabs_soa for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's Pine Labs Accounts Receivable
      SOA accounts receivable statement evidence should use zs_observe.pinelabs_soa. Apply group_id=44, group_level_id=168
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Pine Labs Accounts Receivable SOA OMS rows should answer Pine Labs's accounts receivable statement question?
    - Which runtime scope must be injected before using pinelabs_soa?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - accounts_receivable_statement
    included_concepts:
    - zs_observe.pinelabs_soa
    - accounts receivable statement
    - Pine Labs Accounts Receivable SOA
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.pinelabs_accounts_receivable.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:accounts_receivable_statement
    - table_id:table.zs_observe.pinelabs_soa
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the Pine Labs Accounts Receivable SOA accounts receivable statement binding
      selects zs_observe.pinelabs_soa as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable semantics
      come from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution, not for
      defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - Pine Labs Accounts Receivable SOA
    - accounts receivable statement
    - OMS
    - zs_observe.pinelabs_soa
    - pinelabs_soa
    - accounts_receivable_statement
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
    domain_id: domain.oms_business.accounts_receivable
    table_id: table.zs_observe.pinelabs_soa
    source_role: accounts_receivable_statement
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
    domain_id: domain.oms_business.accounts_receivable
    table_id: table.zs_observe.pinelabs_soa
    source_role: accounts_receivable_statement
    source_entity: Pine Labs Accounts Receivable SOA
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Pinelabs SOA accounts receivable statement
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  card_type: account_data_binding
  canonical_name: Pine Labs Woohoo Gift Card OMS giftcard_order_oms binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Woohoo Gift Card OMS giftcard order oms
    - woohoo_oms
    - zs_observe.woohoo_oms
    - Woohoo OMS, OMS rectified/corrections, and adhoc gift card order context
    - Pine Labs Woohoo Gift Card OMS giftcard order oms
    colloquial_phrases:
    - Pine Labs Woohoo Gift Card OMS giftcard order oms source
    - Woohoo Gift Card OMS giftcard order oms runtime binding
    - woohoo_oms for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's Woohoo Gift Card OMS giftcard
      order oms evidence should use zs_observe.woohoo_oms. Apply group_id=44, group_level_id=168 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Woohoo Gift Card OMS OMS rows should answer Pine Labs's giftcard order oms question?
    - Which runtime scope must be injected before using woohoo_oms?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - giftcard_order_oms
    included_concepts:
    - zs_observe.woohoo_oms
    - giftcard order oms
    - Woohoo Gift Card OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=44
    - group_level_id=168
    - oms_business_kb.md
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.woohoo_giftcard_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:giftcard_order_oms
    - table_id:table.zs_observe.woohoo_oms
    - runtime_source_family:oms
    embedding_text: 'For Pine Labs, the Woohoo Gift Card OMS giftcard order oms binding selects zs_observe.woohoo_oms
      as OMS evidence. Scope: group_id=44, group_level_id=168. Reusable semantics come from oms_business_kb.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - Woohoo Gift Card OMS
    - giftcard order oms
    - OMS
    - zs_observe.woohoo_oms
    - woohoo_oms
    - giftcard_order_oms
    - oms_business_kb.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  evidence:
    source_documents:
    - Pine Labs.docx
    - oms_business_kb.md
    source_path: Pine Labs.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
    domain_id: domain.oms_business.gift_card_oms
    table_id: table.zs_observe.woohoo_oms
    source_role: giftcard_order_oms
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
    domain_id: domain.oms_business.gift_card_oms
    table_id: table.zs_observe.woohoo_oms
    source_role: giftcard_order_oms
    source_entity: Woohoo Gift Card OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Woohoo OMS, OMS rectified/corrections, and adhoc gift card order context
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
  card_type: account_data_binding
  canonical_name: Pine Labs Cashfree payment gateway reconciliation binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Cashfree settlement
    - cashfree_payin
    - zs_observe.cashfree_payin
    - Pine Labs Cashfree settlement
    colloquial_phrases:
    - Pine Labs Cashfree settlement source
    - Cashfree settlement runtime binding
    - cashfree_payin for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's Cashfree settlement evidence
      should use zs_observe.cashfree_payin. Apply group_id=44, group_level_id=168 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Cashfree settlement rows represent expected gateway evidence for Pine Labs?
    - Which merchant/account filters are still needed before querying cashfree_payin?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.cashfree_payin
    - settlement
    - Cashfree
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=44
    - group_level_id=168
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.cashfree.payment_gateway
    - platform_id:platform.cashfree
    - platform_context_id:platform_context.cashfree.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.cashfree_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Pine Labs, the Cashfree settlement binding selects zs_observe.cashfree_payin as payment
      gateway evidence. Scope: group_id=44, group_level_id=168. Reusable semantics come from payment_gateway.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - Cashfree
    - settlement
    - payment gateway
    - zs_observe.cashfree_payin
    - cashfree_payin
    - payment_gateway.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: Pine Labs.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.cashfree.payment_gateway
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.cashfree_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.cashfree.payment_gateway
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.cashfree_payin
    canonical_table_id: table.zs_observe.cashfree_payin
    physical_table_reference: zs_observe.cashfree_payin
    configured_pipeline_target: cashfree_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: Cashfree payment gateway reconciliation
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '44'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '44'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '168'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '168'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    business_keys_from_reusable_pack:
    - transaction_id
    - cashfree_reference_id
    - merchant_reference_id
    - customer_reference_id
    - settlement_id
    - refund_arn
    - utr
    amount_columns_from_reusable_pack:
    - settlement_id
    - amount
    - event_amount
    - transaction_amount
    - transaction_service_charge
    - fee
    - tax
    - txn_st_gst
    - net_settlement_amount
    - event_settlement_amount
    - settled_amount
    - refund_arn
    - refund_type
    - credit_ref_no
    - redemption_amount
    grain_from_reusable_pack: one row per payin/payment/refund/adjustment gateway event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
  card_type: account_data_binding
  canonical_name: Pine Labs Paytm payment gateway pay-in binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Paytm settlement
    - paytm_payin
    - zs_observe.paytm_payin
    - paytm_payin multi-sheet
    - Pine Labs Paytm settlement
    colloquial_phrases:
    - Pine Labs Paytm settlement source
    - Paytm settlement runtime binding
    - paytm_payin for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's Paytm settlement evidence should
      use zs_observe.paytm_payin. Apply group_id=44, group_level_id=168 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Paytm settlement rows represent expected gateway evidence for Pine Labs?
    - Which merchant/account filters are still needed before querying paytm_payin?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.paytm_payin
    - settlement
    - Paytm
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=44
    - group_level_id=168
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.paytm.payment_gateway
    - platform_id:platform.paytm
    - platform_context_id:platform_context.paytm.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.paytm_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Pine Labs, the Paytm settlement binding selects zs_observe.paytm_payin as payment gateway
      evidence. Scope: group_id=44, group_level_id=168. Reusable semantics come from payment_gateway.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - Paytm
    - settlement
    - payment gateway
    - zs_observe.paytm_payin
    - paytm_payin
    - paytm_payin multi-sheet
    - payment_gateway.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: Pine Labs.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.paytm.payment_gateway
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.paytm_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.paytm.payment_gateway
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.paytm_payin
    canonical_table_id: table.zs_observe.paytm_payin
    physical_table_reference: zs_observe.paytm_payin
    configured_pipeline_target: paytm_payin multi-sheet
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: Paytm payment gateway pay-in
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '44'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '44'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '168'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '168'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    - transaction_date
    - payout_date
    business_keys_from_reusable_pack:
    - transaction_id
    - payout_id
    - settlement_id
    - bank_transaction_id
    - utr_no
    - rrn
    - reference_no
    - reference_transaction_id
    - split_transaction_id
    amount_columns_from_reusable_pack:
    - settlement_id
    - amount
    - fee
    - tax
    - gst
    - commission
    - settled_amount
    - txn_amount
    - bill_amount
    - card_network
    - settlement_type
    - discount_amount
    - subvention_amount
    - loan_amount
    - bank_offer_cashback
    - protection_plan_amount
    grain_from_reusable_pack: one row per payin/payment/refund/adjustment gateway event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
  card_type: account_data_binding
  canonical_name: Pine Labs Navi fintech settlement binding
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Navi settlement
    - navi_settlement
    - zs_observe.navi_settlement
    - navi_settlement multi-sheet
    - Pine Labs Navi settlement
    colloquial_phrases:
    - Pine Labs Navi settlement source
    - Navi settlement runtime binding
    - navi_settlement for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's Navi settlement evidence should
      use zs_observe.navi_settlement. Apply group_id=44, group_level_id=168 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Navi settlement rows represent expected gateway evidence for Pine Labs?
    - Which merchant/account filters are still needed before querying navi_settlement?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.navi_settlement
    - settlement
    - Navi
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=44
    - group_level_id=168
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.navi.payment_gateway
    - platform_id:platform.navi
    - platform_context_id:platform_context.navi.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.navi_settlement
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Pine Labs, the Navi settlement binding selects zs_observe.navi_settlement as payment gateway
      evidence. Scope: group_id=44, group_level_id=168. Reusable semantics come from payment_gateway.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Pine Labs
    - Navi
    - settlement
    - payment gateway
    - zs_observe.navi_settlement
    - navi_settlement
    - navi_settlement multi-sheet
    - payment_gateway.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: Pine Labs.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.navi.payment_gateway
    platform_id: platform.navi
    platform_context_id: platform_context.navi.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.navi_settlement
    source_role: settlement
    account_data_binding_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.navi.payment_gateway
    platform_id: platform.navi
    platform_context_id: platform_context.navi.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.navi_settlement
    canonical_table_id: table.zs_observe.navi_settlement
    physical_table_reference: zs_observe.navi_settlement
    configured_pipeline_target: navi_settlement multi-sheet
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: Navi fintech settlement
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '44'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '44'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '168'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '168'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - created_date
    - settlement_date
    business_keys_from_reusable_pack:
    - settlement_id
    amount_columns_from_reusable_pack:
    - settlement_id
    - charged_amount
    - settled_amount
    - discount
    - mp_fees
    - actuals
    - commission
    - gst_split
    - tds_splitn
    grain_from_reusable_pack: one row per settlement/balance event or settlement line
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
  card_type: account_data_binding
  canonical_name: Pine Labs Tata Digital / Tata Neu settlement binding
  status: review_required
  review_status: review_required
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Tata Digital / Tata Neu settlement
    - tata_digital_settlement
    - zs_observe.tata_digital_settlement
    - Pine Labs Tata Digital / Tata Neu settlement
    colloquial_phrases:
    - Pine Labs Tata Digital / Tata Neu settlement source
    - Tata Digital / Tata Neu settlement runtime binding
    - tata_digital_settlement for Pine Labs
    business_meaning: This account-data binding tells the resolver that Pine Labs's Tata Digital / Tata Neu settlement
      evidence should use zs_observe.tata_digital_settlement. Apply group_id=44, group_level_id=168 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Tata Digital / Tata Neu settlement rows represent expected gateway evidence for Pine Labs?
    - Which merchant/account filters are still needed before querying tata_digital_settlement?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.tata_digital_settlement
    - settlement
    - Tata Digital / Tata Neu
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=44
    - group_level_id=168
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - platform_account_id:platform_account.pine_labs.tata_digital.payment_gateway
    - platform_id:platform.tata_digital
    - platform_context_id:platform_context.tata_digital.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.tata_digital_settlement
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Pine Labs, the Tata Digital / Tata Neu settlement binding selects zs_observe.tata_digital_settlement
      as payment gateway evidence. Scope: group_id=44, group_level_id=168. Reusable semantics come from payment_gateway.md.
      Coverage status: source_described_missing. Use this card for runtime source resolution, not for defining table
      columns or metrics.'
    search_keywords:
    - Pine Labs
    - Tata Digital / Tata Neu
    - settlement
    - payment gateway
    - zs_observe.tata_digital_settlement
    - tata_digital_settlement
    - payment_gateway.md
    - group_id=44
    - group_level_id=168
    exact_match_keys:
    - account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: Pine Labs.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.tata_digital.payment_gateway
    platform_id: platform.tata_digital
    platform_context_id: platform_context.tata_digital.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.tata_digital_settlement
    source_role: settlement
    account_data_binding_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    platform_account_id: platform_account.pine_labs.tata_digital.payment_gateway
    platform_id: platform.tata_digital
    platform_context_id: platform_context.tata_digital.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.tata_digital_settlement
    canonical_table_id: table.zs_observe.tata_digital_settlement
    physical_table_reference: zs_observe.tata_digital_settlement
    configured_pipeline_target: tata_digital_settlement
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: Tata Digital / Tata Neu settlement
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: source_described_missing
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '44'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '44'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '168'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '168'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - created_date
    - settlement_date
    business_keys_from_reusable_pack:
    - reference_number
    - settlement_id
    - utr
    amount_columns_from_reusable_pack:
    - settlement_id
    - charged_amount
    - settled_amount
    - pre_discount
    - pre_discountamount
    - payable_amount
    - amount_paid
    - discount
    - discount_amount
    grain_from_reusable_pack: one row per settlement/balance event or settlement line
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.5 Business Scope Set Cards

#### business_scope_set.pine_labs.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.pine_labs.oms
  card_type: business_scope_set
  canonical_name: Pine Labs OMS runtime scope
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs OMS runtime scope
    - Pine Labs OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Pine Labs OMS scope
    - OMS accounts and bindings
    - Pine Labs OMS resolver input
    business_meaning: Business scope set for Pine Labs's OMS runtime resolution. It groups 5 platform accounts and
      10 account-data bindings so the resolver can choose client-scoped sources before entering reusable canonical
      packs.
    business_questions:
    - Which OMS accounts and bindings are active for Pine Labs?
    - Which runtime table bindings should be considered together under Pine Labs OMS runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - OMS
    - resolver_scope
    included_concepts:
    - 5 platform accounts
    - 10 account-data bindings
    - 14 deferred sources
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - runtime_source_family:oms
    embedding_text: Pine Labs OMS runtime scope groups Pine Labs's OMS runtime accounts and table bindings. Use
      it to restrict traversal to the client's configured sources; unresolved sources remain deferred until supported
      canonical packs exist.
    search_keywords:
    - Pine Labs
    - Pine Labs OMS runtime scope
    - OMS
    - business scope set
    - 5 accounts
    - 10 bindings
    exact_match_keys:
    - business_scope_set.pine_labs.oms
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
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.pine_labs.oms
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    binding_name: Pine Labs OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.pine_labs.oms
    account_data_binding_ids:
    - account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
    - account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
    - account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
    - account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
    participating_accounts:
    - platform_account_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
      account_name: Pine Labs Amazon Gift Card Settlement account
    - platform_account_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
      account_name: Pine Labs Amazon Seller Flex OMS account
    - platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
      account_name: Pine Labs B2B Partner Gift Card Settlements account
    - platform_account_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
      account_name: Pine Labs Pine Labs Accounts Receivable SOA account
    - platform_account_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
      account_name: Pine Labs Woohoo Gift Card OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
      source_role: amazon_giftcard_settlement
      table_id: table.zs_observe.amazon_gc_settlement
      domain_id: domain.oms_business.amazon_gift_card_settlement
    - account_data_binding_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
      source_role: giftcard_activation_oms
      table_id: table.zs_observe.amazon_seller_flex
      domain_id: domain.oms_business.gift_card_oms
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.amica_technologies_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.first_pay_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.gullak_technologies_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.nearby_marketplace
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.paytm_giftcard_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.red_giraffe_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
      source_role: accounts_receivable_statement
      table_id: table.zs_observe.pinelabs_soa
      domain_id: domain.oms_business.accounts_receivable
    - account_data_binding_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
      source_role: giftcard_order_oms
      table_id: table.zs_observe.woohoo_oms
      domain_id: domain.oms_business.gift_card_oms
    deferred_sources:
    - label: Flipkart gift-card settlement
      config: settlement + adhoc ads/TDS/rebates/VAS
      reason: Flipkart partner settlement for Pine Labs is not represented in the uploaded OMS Business KB tables;
        marketplace pack may cover generic Flipkart settlement but not Pine gift-card-specific partner settlement.
      source_family: oms
    - label: PhonePe settlement report
      config: settlement report + mapper
      reason: No PhonePe gift-card settlement/mapper canonical OMS tables in uploaded OMS packs.
      source_family: oms
    - label: Woohoo Adhoc
      config: woohoo_oms_adhoc
      reason: No woohoo_oms_adhoc table card in uploaded OMS packs.
      source_family: oms
    - label: Maximize Pay
      config: maximize_settlement
      reason: No Maximize Pay canonical OMS table card in uploaded OMS packs.
      source_family: oms
    - label: Navi
      config: navi_settlement
      reason: No Navi canonical OMS table card in uploaded OMS packs.
      source_family: oms
    - label: DreamPlug
      config: dreamplug_settlement
      reason: No DreamPlug canonical OMS table card in uploaded OMS packs.
      source_family: oms
    - label: Tata Digital
      config: tata_digital_settlement
      reason: No Tata Digital canonical OMS table card in uploaded OMS packs.
      source_family: oms
    - label: Pinelabs commission invoice
      config: pinelabs_commission_invoice
      reason: No pinelabs_commission_invoice table card in uploaded OMS packs.
      source_family: oms
    - label: Pinelabs tally
      config: pinelabs_tally
      reason: No pinelabs_tally table card in uploaded OMS packs.
      source_family: oms
    - label: Pinelabs adhoc amount
      config: pinelab_adhoc_amount
      reason: No pinelab_adhoc_amount table card in uploaded OMS packs.
      source_family: oms
    - label: Pine PG
      config: pine_payments
      reason: No pine_payments table card in uploaded OMS packs; payment gateway pack expected later.
      source_family: oms
    - label: Amazon.in mapper
      config: amazon_in_mapper
      reason: No amazon_in_mapper table card in uploaded OMS packs.
      source_family: oms
    - label: PhonePe mapper
      config: phonepe_mapper
      reason: No phonepe_mapper table card in uploaded OMS packs.
      source_family: oms
    - label: Treasury reports
      config: revalidation_report, sclp_billing_report, credit_limit_report, ignore_card_number_report, merchant_interest_sheet
      reason: Treasury/stored-card-liability reports are outside the uploaded OMS packs and should be integrated
        only with a treasury/liability pack.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.pine_labs.payment_gateway

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
  canonical_id: business_scope_set.pine_labs.payment_gateway
  card_type: business_scope_set
  canonical_name: Pine Labs payment gateway runtime scope
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs payment gateway runtime scope
    - Pine Labs payment gateway scope
    - payment gateway runtime scope set
    colloquial_phrases:
    - Pine Labs payment gateway scope
    - payment gateway accounts and bindings
    - Pine Labs payment gateway resolver input
    business_meaning: Business scope set for Pine Labs's payment gateway runtime resolution. It groups 4 platform
      accounts and 4 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which payment gateway accounts and bindings are active for Pine Labs?
    - Which runtime table bindings should be considered together under Pine Labs payment gateway runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - payment_gateway
    - resolver_scope
    included_concepts:
    - 4 platform accounts
    - 4 account-data bindings
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - runtime_source_family:payment_gateway
    embedding_text: Pine Labs payment gateway runtime scope groups Pine Labs's payment gateway runtime accounts
      and table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain
      deferred until supported canonical packs exist.
    search_keywords:
    - Pine Labs
    - Pine Labs payment gateway runtime scope
    - payment gateway
    - business scope set
    - 4 accounts
    - 4 bindings
    exact_match_keys:
    - business_scope_set.pine_labs.payment_gateway
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    runtime_source_family: payment_gateway
    business_scope_set_id: business_scope_set.pine_labs.payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    binding_name: Pine Labs payment gateway runtime scope
    binding_type: payment_gateway_source_resolution
    business_scope_set_id: business_scope_set.pine_labs.payment_gateway
    platform_account_ids:
    - platform_account.pine_labs.cashfree.payment_gateway
    - platform_account.pine_labs.navi.payment_gateway
    - platform_account.pine_labs.paytm.payment_gateway
    - platform_account.pine_labs.tata_digital.payment_gateway
    account_data_binding_ids:
    - account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
    - account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
    - account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
    - account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
    included_platform_ids:
    - platform.cashfree
    - platform.navi
    - platform.paytm
    - platform.tata_digital
    included_platform_context_ids:
    - platform_context.cashfree.in
    - platform_context.navi.in
    - platform_context.paytm.in
    - platform_context.tata_digital.in
    source_flow_paths:
    - platform_account_id: platform_account.pine_labs.cashfree.payment_gateway
      account_data_binding_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
      platform_id: platform.cashfree
      platform_context_id: platform_context.cashfree.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.cashfree_payin
      source_role: settlement
      configured_pipeline_target: cashfree_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.pine_labs.paytm.payment_gateway
      account_data_binding_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
      platform_id: platform.paytm
      platform_context_id: platform_context.paytm.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.paytm_payin
      source_role: settlement
      configured_pipeline_target: paytm_payin multi-sheet
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.pine_labs.navi.payment_gateway
      account_data_binding_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
      platform_id: platform.navi
      platform_context_id: platform_context.navi.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.navi_settlement
      source_role: settlement
      configured_pipeline_target: navi_settlement multi-sheet
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.pine_labs.tata_digital.payment_gateway
      account_data_binding_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
      platform_id: platform.tata_digital
      platform_context_id: platform_context.tata_digital.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.tata_digital_settlement
      source_role: settlement
      configured_pipeline_target: tata_digital_settlement
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.6 Business Flow Binding Cards

#### business_flow_binding.pine_labs.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.pine_labs.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Pine Labs OMS runtime resolution flow
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
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs OMS runtime resolution flow
    - Pine Labs OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Pine Labs OMS resolution flow
    - OMS source routing
    - Pine Labs runtime traversal plan
    business_meaning: Business flow binding for Pine Labs's OMS source resolution. It connects the scope set to
      5 platform accounts and 10 account-data bindings so questions enter the right client-scoped evidence before
      reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Pine Labs's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - OMS
    - runtime_traversal
    included_concepts:
    - 5 platform accounts
    - 10 account-data bindings
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - runtime_source_family:oms
    embedding_text: Pine Labs OMS runtime resolution flow is Pine Labs's OMS runtime traversal binding. It connects
      the business scope set to account and table bindings so retrieval selects client evidence first and then delegates
      semantics to external canonical packs.
    search_keywords:
    - Pine Labs
    - Pine Labs OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.pine_labs.oms_runtime_resolution
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
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.pine_labs.oms_runtime_resolution
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    binding_name: Pine Labs OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.pine_labs.oms
    account_data_binding_ids:
    - account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
    - account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
    - account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
    - account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
    - account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
    participating_accounts:
    - platform_account_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
      account_name: Pine Labs Amazon Gift Card Settlement account
    - platform_account_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
      account_name: Pine Labs Amazon Seller Flex OMS account
    - platform_account_id: platform_account.pine_labs.partner_giftcard_settlement.oms
      account_name: Pine Labs B2B Partner Gift Card Settlements account
    - platform_account_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
      account_name: Pine Labs Pine Labs Accounts Receivable SOA account
    - platform_account_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
      account_name: Pine Labs Woohoo Gift Card OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
      source_role: amazon_giftcard_settlement
      table_id: table.zs_observe.amazon_gc_settlement
      domain_id: domain.oms_business.amazon_gift_card_settlement
    - account_data_binding_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
      source_role: giftcard_activation_oms
      table_id: table.zs_observe.amazon_seller_flex
      domain_id: domain.oms_business.gift_card_oms
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.amica_technologies_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.first_pay_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.gullak_technologies_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.nearby_marketplace
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.paytm_giftcard_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
      source_role: partner_giftcard_settlement
      table_id: table.zs_observe.red_giraffe_settlement
      domain_id: domain.oms_business.partner_settlement
    - account_data_binding_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
      source_role: accounts_receivable_statement
      table_id: table.zs_observe.pinelabs_soa
      domain_id: domain.oms_business.accounts_receivable
    - account_data_binding_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
      source_role: giftcard_order_oms
      table_id: table.zs_observe.woohoo_oms
      domain_id: domain.oms_business.gift_card_oms
    deferred_sources:
    - label: Flipkart gift-card settlement
      config: settlement + adhoc ads/TDS/rebates/VAS
      reason: Flipkart partner settlement for Pine Labs is not represented in the uploaded OMS Business KB tables;
        marketplace pack may cover generic Flipkart settlement but not Pine gift-card-specific partner settlement.
      source_family: oms
    - label: PhonePe settlement report
      config: settlement report + mapper
      reason: No PhonePe gift-card settlement/mapper canonical OMS tables in uploaded OMS packs.
      source_family: oms
    - label: Woohoo Adhoc
      config: woohoo_oms_adhoc
      reason: No woohoo_oms_adhoc table card in uploaded OMS packs.
      source_family: oms
    - label: Maximize Pay
      config: maximize_settlement
      reason: No Maximize Pay canonical OMS table card in uploaded OMS packs.
      source_family: oms
    - label: Navi
      config: navi_settlement
      reason: No Navi canonical OMS table card in uploaded OMS packs.
      source_family: oms
    - label: DreamPlug
      config: dreamplug_settlement
      reason: No DreamPlug canonical OMS table card in uploaded OMS packs.
      source_family: oms
    - label: Tata Digital
      config: tata_digital_settlement
      reason: No Tata Digital canonical OMS table card in uploaded OMS packs.
      source_family: oms
    - label: Pinelabs commission invoice
      config: pinelabs_commission_invoice
      reason: No pinelabs_commission_invoice table card in uploaded OMS packs.
      source_family: oms
    - label: Pinelabs tally
      config: pinelabs_tally
      reason: No pinelabs_tally table card in uploaded OMS packs.
      source_family: oms
    - label: Pinelabs adhoc amount
      config: pinelab_adhoc_amount
      reason: No pinelab_adhoc_amount table card in uploaded OMS packs.
      source_family: oms
    - label: Pine PG
      config: pine_payments
      reason: No pine_payments table card in uploaded OMS packs; payment gateway pack expected later.
      source_family: oms
    - label: Amazon.in mapper
      config: amazon_in_mapper
      reason: No amazon_in_mapper table card in uploaded OMS packs.
      source_family: oms
    - label: PhonePe mapper
      config: phonepe_mapper
      reason: No phonepe_mapper table card in uploaded OMS packs.
      source_family: oms
    - label: Treasury reports
      config: revalidation_report, sclp_billing_report, credit_limit_report, ignore_card_number_report, merchant_interest_sheet
      reason: Treasury/stored-card-liability reports are outside the uploaded OMS packs and should be integrated
        only with a treasury/liability pack.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.pine_labs.payment_gateway_runtime_resolution

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
  canonical_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Pine Labs payment gateway runtime resolution
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Pine Labs
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Pine Labs payment gateway runtime resolution
    - Pine Labs payment gateway flow
    - payment gateway runtime resolution flow
    colloquial_phrases:
    - Pine Labs payment gateway resolution flow
    - payment gateway source routing
    - Pine Labs runtime traversal plan
    business_meaning: Business flow binding for Pine Labs's payment gateway source resolution. It connects the scope
      set to 4 platform accounts and 4 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which payment gateway bindings should be traversed for Pine Labs's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - payment_gateway
    - runtime_traversal
    included_concepts:
    - 4 platform accounts
    - 4 account-data bindings
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
    - tenant_id:tenant.pine_labs
    - group_id:group.pine_labs.g44.gl168
    - runtime_source_family:payment_gateway
    embedding_text: Pine Labs payment gateway runtime resolution is Pine Labs's payment gateway runtime traversal
      binding. It connects the business scope set to account and table bindings so retrieval selects client evidence
      first and then delegates semantics to external canonical packs.
    search_keywords:
    - Pine Labs
    - Pine Labs payment gateway runtime resolution
    - payment gateway
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  evidence:
    source_documents:
    - Pine Labs.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_flow
    evidence_ids:
    - client_runtime.payment_gateway_flow
    source_line: null
  traversal:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    runtime_source_family: payment_gateway
    business_flow_binding_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.pine_labs.payment_gateway
  fields:
    tenant_id: tenant.pine_labs
    group_id: group.pine_labs.g44.gl168
    business_flow_binding_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.pine_labs.payment_gateway
    flow_name: Pine Labs payment gateway runtime resolution
    flow_type: payment_gateway_source_resolution
    platform_account_ids:
    - platform_account.pine_labs.cashfree.payment_gateway
    - platform_account.pine_labs.navi.payment_gateway
    - platform_account.pine_labs.paytm.payment_gateway
    - platform_account.pine_labs.tata_digital.payment_gateway
    account_data_binding_ids:
    - account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
    - account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
    - account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
    - account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
    source_flow_paths:
    - platform_account_id: platform_account.pine_labs.cashfree.payment_gateway
      account_data_binding_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
      platform_id: platform.cashfree
      platform_context_id: platform_context.cashfree.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.cashfree_payin
      source_role: settlement
      configured_pipeline_target: cashfree_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.pine_labs.paytm.payment_gateway
      account_data_binding_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
      platform_id: platform.paytm
      platform_context_id: platform_context.paytm.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.paytm_payin
      source_role: settlement
      configured_pipeline_target: paytm_payin multi-sheet
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.pine_labs.navi.payment_gateway
      account_data_binding_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
      platform_id: platform.navi
      platform_context_id: platform_context.navi.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.navi_settlement
      source_role: settlement
      configured_pipeline_target: navi_settlement multi-sheet
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.pine_labs.tata_digital.payment_gateway
      account_data_binding_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
      platform_id: platform.tata_digital
      platform_context_id: platform_context.tata_digital.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.tata_digital_settlement
      source_role: settlement
      configured_pipeline_target: tata_digital_settlement
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_gc_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_gc_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  target_card_id: column.zs_observe.amazon_gc_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_gc_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_gc_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  target_card_id: column.zs_observe.amazon_gc_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex.account_data_binding_applies_scope_column.column_zs_observe_amazon_seller_flex_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex.account_data_binding_applies_scope_column.column_zs_observe_amazon_seller_flex_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  target_card_id: column.zs_observe.amazon_seller_flex.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex.account_data_binding_applies_scope_column.column_zs_observe_amazon_seller_flex_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex.account_data_binding_applies_scope_column.column_zs_observe_amazon_seller_flex_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  target_card_id: column.zs_observe.amazon_seller_flex.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement.account_data_binding_applies_scope_column.column_zs_observe_amica_technologies_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement.account_data_binding_applies_scope_column.column_zs_observe_amica_technologies_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  target_card_id: column.zs_observe.amica_technologies_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement.account_data_binding_applies_scope_column.column_zs_observe_amica_technologies_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement.account_data_binding_applies_scope_column.column_zs_observe_amica_technologies_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  target_card_id: column.zs_observe.amica_technologies_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement.account_data_binding_applies_scope_column.column_zs_observe_first_pay_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement.account_data_binding_applies_scope_column.column_zs_observe_first_pay_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  target_card_id: column.zs_observe.first_pay_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement.account_data_binding_applies_scope_column.column_zs_observe_first_pay_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement.account_data_binding_applies_scope_column.column_zs_observe_first_pay_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  target_card_id: column.zs_observe.first_pay_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement.account_data_binding_applies_scope_column.column_zs_observe_gullak_technologies_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement.account_data_binding_applies_scope_column.column_zs_observe_gullak_technologies_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  target_card_id: column.zs_observe.gullak_technologies_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement.account_data_binding_applies_scope_column.column_zs_observe_gullak_technologies_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement.account_data_binding_applies_scope_column.column_zs_observe_gullak_technologies_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  target_card_id: column.zs_observe.gullak_technologies_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace.account_data_binding_applies_scope_column.column_zs_observe_nearby_marketplace_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace.account_data_binding_applies_scope_column.column_zs_observe_nearby_marketplace_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  target_card_id: column.zs_observe.nearby_marketplace.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace.account_data_binding_applies_scope_column.column_zs_observe_nearby_marketplace_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace.account_data_binding_applies_scope_column.column_zs_observe_nearby_marketplace_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  target_card_id: column.zs_observe.nearby_marketplace.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement.account_data_binding_applies_scope_column.column_zs_observe_paytm_giftcard_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement.account_data_binding_applies_scope_column.column_zs_observe_paytm_giftcard_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  target_card_id: column.zs_observe.paytm_giftcard_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement.account_data_binding_applies_scope_column.column_zs_observe_paytm_giftcard_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement.account_data_binding_applies_scope_column.column_zs_observe_paytm_giftcard_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  target_card_id: column.zs_observe.paytm_giftcard_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement.account_data_binding_applies_scope_column.column_zs_observe_red_giraffe_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement.account_data_binding_applies_scope_column.column_zs_observe_red_giraffe_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  target_card_id: column.zs_observe.red_giraffe_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement.account_data_binding_applies_scope_column.column_zs_observe_red_giraffe_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement.account_data_binding_applies_scope_column.column_zs_observe_red_giraffe_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  target_card_id: column.zs_observe.red_giraffe_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa.account_data_binding_applies_scope_column.column_zs_observe_pinelabs_soa_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa.account_data_binding_applies_scope_column.column_zs_observe_pinelabs_soa_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  target_card_id: column.zs_observe.pinelabs_soa.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa.account_data_binding_applies_scope_column.column_zs_observe_pinelabs_soa_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa.account_data_binding_applies_scope_column.column_zs_observe_pinelabs_soa_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  target_card_id: column.zs_observe.pinelabs_soa.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms.account_data_binding_applies_scope_column.column_zs_observe_woohoo_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms.account_data_binding_applies_scope_column.column_zs_observe_woohoo_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  target_card_id: column.zs_observe.woohoo_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms.account_data_binding_applies_scope_column.column_zs_observe_woohoo_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms.account_data_binding_applies_scope_column.column_zs_observe_woohoo_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  target_card_id: column.zs_observe.woohoo_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_amazon_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_amazon_giftcard_settlement_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  target_card_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_amazon_seller_flex_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_amazon_seller_flex_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  target_card_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_pinelabs_accounts_receivable_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_pinelabs_accounts_receivable_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  target_card_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_woohoo_giftcard_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_woohoo_giftcard_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  target_card_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_gc_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_gc_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  target_card_id: table.zs_observe.amazon_gc_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex.account_data_binding_binds_to_table.table_zs_observe_amazon_seller_flex

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex.account_data_binding_binds_to_table.table_zs_observe_amazon_seller_flex
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  target_card_id: table.zs_observe.amazon_seller_flex
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement.account_data_binding_binds_to_table.table_zs_observe_amica_technologies_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement.account_data_binding_binds_to_table.table_zs_observe_amica_technologies_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  target_card_id: table.zs_observe.amica_technologies_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement.account_data_binding_binds_to_table.table_zs_observe_first_pay_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement.account_data_binding_binds_to_table.table_zs_observe_first_pay_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  target_card_id: table.zs_observe.first_pay_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement.account_data_binding_binds_to_table.table_zs_observe_gullak_technologies_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement.account_data_binding_binds_to_table.table_zs_observe_gullak_technologies_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  target_card_id: table.zs_observe.gullak_technologies_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace.account_data_binding_binds_to_table.table_zs_observe_nearby_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace.account_data_binding_binds_to_table.table_zs_observe_nearby_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  target_card_id: table.zs_observe.nearby_marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement.account_data_binding_binds_to_table.table_zs_observe_paytm_giftcard_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement.account_data_binding_binds_to_table.table_zs_observe_paytm_giftcard_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  target_card_id: table.zs_observe.paytm_giftcard_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement.account_data_binding_binds_to_table.table_zs_observe_red_giraffe_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement.account_data_binding_binds_to_table.table_zs_observe_red_giraffe_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  target_card_id: table.zs_observe.red_giraffe_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa.account_data_binding_binds_to_table.table_zs_observe_pinelabs_soa

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa.account_data_binding_binds_to_table.table_zs_observe_pinelabs_soa
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  target_card_id: table.zs_observe.pinelabs_soa
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms.account_data_binding_binds_to_table.table_zs_observe_woohoo_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms.account_data_binding_binds_to_table.table_zs_observe_woohoo_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  target_card_id: table.zs_observe.woohoo_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_amazon_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_amazon_giftcard_settlement_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_amazon_seller_flex_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_amazon_seller_flex_oms_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_pinelabs_accounts_receivable_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_pinelabs_accounts_receivable_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_woohoo_giftcard_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_woohoo_giftcard_oms_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_pine_labs_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_pine_labs_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  target_card_id: business_scope_set.pine_labs.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_pine_labs_oms.business_scope_set_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform.platform_zenstatement_oms_business_kb
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_amazon_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_amazon_giftcard_settlement_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_amazon_seller_flex_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_amazon_seller_flex_oms_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_pinelabs_accounts_receivable_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_pinelabs_accounts_receivable_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_woohoo_giftcard_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_account.platform_account_pine_labs_woohoo_giftcard_oms_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_oms.business_scope_set_includes_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.pine_labs.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_pine_labs_g44_gl168.group_belongs_to_tenant.tenant_pine_labs

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_belongs_to_tenant.tenant_pine_labs
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: tenant.pine_labs
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_pine_labs_g44_gl168.group_has_business_flow_binding.business_flow_binding_pine_labs_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_business_flow_binding.business_flow_binding_pine_labs_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: business_flow_binding.pine_labs.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_pine_labs_g44_gl168.group_has_business_scope_set.business_scope_set_pine_labs_oms

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_business_scope_set.business_scope_set_pine_labs_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: business_scope_set.pine_labs.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_amazon_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_amazon_giftcard_settlement_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_amazon_seller_flex_oms_oms

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_amazon_seller_flex_oms_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_partner_giftcard_settlement_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_pinelabs_accounts_receivable_oms

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_pinelabs_accounts_receivable_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_woohoo_giftcard_oms_oms

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_woohoo_giftcard_oms_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_pine_labs_amazon_giftcard_settlement_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_amazon_giftcard_settlement_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_amazon_seller_flex_oms_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_amazon_seller_flex_oms_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_pinelabs_accounts_receivable_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_pinelabs_accounts_receivable_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_woohoo_giftcard_oms_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_woohoo_giftcard_oms_oms.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_pine_labs_amazon_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_amazon_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_amazon_giftcard_settlement_amazon_giftcard_settlement_zs_observe_amazon_gc_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  target_card_id: account_data_binding.pine_labs.amazon_giftcard_settlement.amazon_giftcard_settlement.zs_observe_amazon_gc_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_amazon_seller_flex_oms_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_amazon_seller_flex_oms_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_amazon_seller_flex_oms_giftcard_activation_oms_zs_observe_amazon_seller_flex
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  target_card_id: account_data_binding.pine_labs.amazon_seller_flex_oms.giftcard_activation_oms.zs_observe_amazon_seller_flex
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_amica_technologies_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_amica_technologies_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_first_pay_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_first_pay_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_gullak_technologies_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_gullak_technologies_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_nearby_marketplace
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_nearby_marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_paytm_giftcard_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_paytm_giftcard_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_partner_giftcard_settlement_partner_giftcard_settlement_zs_observe_red_giraffe_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: account_data_binding.pine_labs.partner_giftcard_settlement.partner_giftcard_settlement.zs_observe_red_giraffe_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_pinelabs_accounts_receivable_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_pinelabs_accounts_receivable_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_pinelabs_accounts_receivable_accounts_receivable_statement_zs_observe_pinelabs_soa
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  target_card_id: account_data_binding.pine_labs.pinelabs_accounts_receivable.accounts_receivable_statement.zs_observe_pinelabs_soa
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_woohoo_giftcard_oms_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_woohoo_giftcard_oms_oms.platform_account_has_account_data_binding.account_data_binding_pine_labs_woohoo_giftcard_oms_giftcard_order_oms_zs_observe_woohoo_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  target_card_id: account_data_binding.pine_labs.woohoo_giftcard_oms.giftcard_order_oms.zs_observe_woohoo_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_pine_labs_amazon_giftcard_settlement_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_amazon_giftcard_settlement_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_amazon_seller_flex_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_amazon_seller_flex_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_pinelabs_accounts_receivable_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_pinelabs_accounts_receivable_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_woohoo_giftcard_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_woohoo_giftcard_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_pine_labs_amazon_giftcard_settlement_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_amazon_giftcard_settlement_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.amazon_giftcard_settlement.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_amazon_seller_flex_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_amazon_seller_flex_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.amazon_seller_flex_oms.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_partner_giftcard_settlement_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.partner_giftcard_settlement.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_pinelabs_accounts_receivable_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_pinelabs_accounts_receivable_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.pinelabs_accounts_receivable.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_pine_labs_woohoo_giftcard_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_woohoo_giftcard_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.woohoo_giftcard_oms.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### TENANT_HAS_GROUP

#### edge.tenant_pine_labs.tenant_has_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.tenant_pine_labs.tenant_has_group.group_pine_labs_g44_gl168
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.pine_labs
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```


<!-- Added bank/payment runtime edges -->

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_cashfree_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
  target_card_id: platform_account.pine_labs.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_navi_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_navi_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
  target_card_id: platform_account.pine_labs.navi.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_paytm_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
  target_card_id: platform_account.pine_labs.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_tata_digital_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement.account_data_binding_belongs_to_platform_account.platform_account_pine_labs_tata_digital_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
  target_card_id: platform_account.pine_labs.tata_digital.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_binds_to_table.table_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_binds_to_table.table_zs_observe_cashfree_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
  target_card_id: table.zs_observe.cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement.account_data_binding_binds_to_table.table_zs_observe_navi_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement.account_data_binding_binds_to_table.table_zs_observe_navi_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
  target_card_id: table.zs_observe.navi_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin.account_data_binding_binds_to_table.table_zs_observe_paytm_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin.account_data_binding_binds_to_table.table_zs_observe_paytm_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
  target_card_id: table.zs_observe.paytm_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement.account_data_binding_binds_to_table.table_zs_observe_tata_digital_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement.account_data_binding_binds_to_table.table_zs_observe_tata_digital_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
  target_card_id: table.zs_observe.tata_digital_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_cashfree_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: platform_account.pine_labs.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_navi_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_navi_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: platform_account.pine_labs.navi.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_paytm_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: platform_account.pine_labs.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_tata_digital_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_pine_labs_tata_digital_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: platform_account.pine_labs.tata_digital.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_pine_labs_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_pine_labs_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_pine_labs_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  target_card_id: business_scope_set.pine_labs.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform.platform_cashfree

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform.platform_cashfree
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform.cashfree
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform.platform_navi

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform.platform_navi
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform.navi
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform.platform_paytm

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform.platform_paytm
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform.paytm
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform.platform_tata_digital

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform.platform_tata_digital
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform.tata_digital
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_account.platform_account_pine_labs_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_account.platform_account_pine_labs_cashfree_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform_account.pine_labs.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_account.platform_account_pine_labs_navi_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_account.platform_account_pine_labs_navi_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform_account.pine_labs.navi.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_account.platform_account_pine_labs_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_account.platform_account_pine_labs_paytm_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform_account.pine_labs.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_account.platform_account_pine_labs_tata_digital_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_account.platform_account_pine_labs_tata_digital_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform_account.pine_labs.tata_digital.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_context.platform_context_cashfree_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_context.platform_context_cashfree_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform_context.cashfree.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_context.platform_context_navi_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_context.platform_context_navi_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform_context.navi.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_context.platform_context_paytm_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_context.platform_context_paytm_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform_context.paytm.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_context.platform_context_tata_digital_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_pine_labs_payment_gateway.business_scope_set_includes_platform_context.platform_context_tata_digital_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.pine_labs.payment_gateway
  target_card_id: platform_context.tata_digital.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_pine_labs_g44_gl168.group_has_business_flow_binding.business_flow_binding_pine_labs_payment_gateway_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_business_flow_binding.business_flow_binding_pine_labs_payment_gateway_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: business_flow_binding.pine_labs.payment_gateway_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_pine_labs_g44_gl168.group_has_business_scope_set.business_scope_set_pine_labs_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_business_scope_set.business_scope_set_pine_labs_payment_gateway
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: business_scope_set.pine_labs.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_cashfree_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_navi_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_navi_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.navi.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_paytm_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_tata_digital_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_pine_labs_g44_gl168.group_has_platform_account.platform_account_pine_labs_tata_digital_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.pine_labs.g44.gl168
  target_card_id: platform_account.pine_labs.tata_digital.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_pine_labs_cashfree_payment_gateway.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_cashfree_payment_gateway.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.cashfree.payment_gateway
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_navi_payment_gateway.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_navi_payment_gateway.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.navi.payment_gateway
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_paytm_payment_gateway.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_paytm_payment_gateway.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.paytm.payment_gateway
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_tata_digital_payment_gateway.platform_account_belongs_to_group.group_pine_labs_g44_gl168

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_tata_digital_payment_gateway.platform_account_belongs_to_group.group_pine_labs_g44_gl168
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.pine_labs.tata_digital.payment_gateway
  target_card_id: group.pine_labs.g44.gl168
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_pine_labs_cashfree_payment_gateway.platform_account_has_account_data_binding.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_cashfree_payment_gateway.platform_account_has_account_data_binding.account_data_binding_pine_labs_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.cashfree.payment_gateway
  target_card_id: account_data_binding.pine_labs.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_navi_payment_gateway.platform_account_has_account_data_binding.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_navi_payment_gateway.platform_account_has_account_data_binding.account_data_binding_pine_labs_navi_settlement_zs_observe_navi_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.navi.payment_gateway
  target_card_id: account_data_binding.pine_labs.navi.settlement.zs_observe_navi_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_paytm_payment_gateway.platform_account_has_account_data_binding.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_paytm_payment_gateway.platform_account_has_account_data_binding.account_data_binding_pine_labs_paytm_settlement_zs_observe_paytm_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.paytm.payment_gateway
  target_card_id: account_data_binding.pine_labs.paytm.settlement.zs_observe_paytm_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_tata_digital_payment_gateway.platform_account_has_account_data_binding.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_tata_digital_payment_gateway.platform_account_has_account_data_binding.account_data_binding_pine_labs_tata_digital_settlement_zs_observe_tata_digital_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.pine_labs.tata_digital.payment_gateway
  target_card_id: account_data_binding.pine_labs.tata_digital.settlement.zs_observe_tata_digital_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_pine_labs_cashfree_payment_gateway.platform_account_uses_platform.platform_cashfree

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_cashfree_payment_gateway.platform_account_uses_platform.platform_cashfree
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.cashfree.payment_gateway
  target_card_id: platform.cashfree
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_navi_payment_gateway.platform_account_uses_platform.platform_navi

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_navi_payment_gateway.platform_account_uses_platform.platform_navi
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.navi.payment_gateway
  target_card_id: platform.navi
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_paytm_payment_gateway.platform_account_uses_platform.platform_paytm

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_paytm_payment_gateway.platform_account_uses_platform.platform_paytm
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.paytm.payment_gateway
  target_card_id: platform.paytm
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_tata_digital_payment_gateway.platform_account_uses_platform.platform_tata_digital

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_tata_digital_payment_gateway.platform_account_uses_platform.platform_tata_digital
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.pine_labs.tata_digital.payment_gateway
  target_card_id: platform.tata_digital
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_pine_labs_cashfree_payment_gateway.platform_account_uses_platform_context.platform_context_cashfree_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_cashfree_payment_gateway.platform_account_uses_platform_context.platform_context_cashfree_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.cashfree.payment_gateway
  target_card_id: platform_context.cashfree.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_navi_payment_gateway.platform_account_uses_platform_context.platform_context_navi_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_navi_payment_gateway.platform_account_uses_platform_context.platform_context_navi_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.navi.payment_gateway
  target_card_id: platform_context.navi.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_paytm_payment_gateway.platform_account_uses_platform_context.platform_context_paytm_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_paytm_payment_gateway.platform_account_uses_platform_context.platform_context_paytm_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.paytm.payment_gateway
  target_card_id: platform_context.paytm.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_pine_labs_tata_digital_payment_gateway.platform_account_uses_platform_context.platform_context_tata_digital_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_pine_labs_tata_digital_payment_gateway.platform_account_uses_platform_context.platform_context_tata_digital_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.pine_labs.tata_digital.payment_gateway
  target_card_id: platform_context.tata_digital.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```
