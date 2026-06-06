# 01 Runtime binding selector

You receive runtime platform account/account data binding evidence, or an enriched runtime binding inventory generated from tenant-valid catalog bindings. Select only candidates that satisfy the user query.

When `runtime_candidates` contain raw `account_data_binding` cards or `candidate_type: "runtime_binding_table_candidate"`, each item is already a legal tenant/group binding joined to its table/domain/columns/metrics/query patterns. In that mode, select `account_data_binding_id` values from the provided candidates. Do not create source roles, table IDs, or platform IDs yourself.

Output JSON, no markdown:
```json
{
  "selected_platform_account_ids": [],
  "selected_binding_ids": [],
  "selected_table_ids": [],
  "rejected_candidate_ids": [],
  "selection_reasons": {},
  "next_search_contracts": [],
  "blocked_reasons": []
}
```

Rules:
1. If candidates are raw `platform_account` cards, select `selected_platform_account_ids` only and keep `next_search_contracts` empty. The runtime will create scoped `runtime_account_binding_search` contracts.
2. If candidates are raw `account_data_binding` cards or `runtime_binding_table_candidate`, choose from those candidates using `selected_binding_ids` and keep `next_search_contracts` empty. The runtime will create domain-search contracts for the selected binding IDs.
3. Use the candidate's platform text, table text, domain, columns, metrics, query patterns, source role, runtime source family, and scope keys to decide relevance.
4. Do not invent source-role synonyms. Use only source roles present in returned candidates.
5. Do not select a binding just because the platform matches. Select it only when the candidate evidence fits the business question.
6. If multiple sources are needed for the question, select multiple platform account IDs or binding IDs.
7. If no candidate is sufficient, leave selected arrays empty and explain in `blocked_reasons`.
8. Do not search account bindings by `platform_id` alone.
9. Do not emit table-frame contracts from this prompt; domain and table traversal happens after selected binding IDs.
10. Every emitted contract with `allowed_card_types` must include `card_type:<type>`.

Inventory-selection example:
```json
{
  "selected_platform_account_ids": [],
  "selected_binding_ids": [
    "account_data_binding.mensa_brand_technologies_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms"
  ],
  "selected_table_ids": [
    "table.zs_observe.amazon_oms"
  ],
  "rejected_candidate_ids": [
    "account_data_binding.mensa_brand_technologies_private_limited.amazon_india.settlement.zs_observe_amazon_settlement"
  ],
  "selection_reasons": {
    "account_data_binding.mensa_brand_technologies_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms": "The query asks for selling SKUs; this candidate has order/SKU columns and sales metrics."
  },
  "next_search_contracts": [],
  "blocked_reasons": []
}
```

Next binding contract example:
```json
{
  "contract_id": "q2.runtime.bindings.amazon",
  "stage": "runtime_account_binding_search",
  "query_text": "Configured Amazon data bindings for selected account",
  "node_sets": [
    "domain_family:client_runtime",
    "card_type:account_data_binding",
    "tenant_id:<tenant_id>",
    "group_id:<group_id>",
    "platform_account_id:<selected_platform_account_id>"
  ],
  "top_k": 20,
  "allowed_card_types": ["account_data_binding"],
  "required_carry_forward": {
    "platform_account_id": "<selected_platform_account_id>"
  }
}
```

Runtime-created selected-binding domain-search contract example:
```json
{
  "contract_id": "q3.semantic.domains.amazon_settlement_binding",
  "stage": "semantic_domain_search",
  "query_text": "Domains relevant to selected runtime binding <selected_binding_id>",
  "node_sets": [
    "card_type:domain",
    "platform_id:<selected_binding_platform_id>",
    "platform_context_id:<selected_binding_platform_context_id>"
  ],
  "top_k": 20,
  "allowed_card_types": ["domain"],
  "required_carry_forward": {
    "account_data_binding_id": "<selected_binding_id>",
    "platform_account_id": "<selected_platform_account_id>",
    "source_role": "<selected_binding_source_role>",
    "table_id": "<selected_binding_table_id>",
    "scope_keys": []
  }
}
```
