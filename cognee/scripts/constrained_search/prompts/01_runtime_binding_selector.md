# 01 Runtime binding selector

You receive runtime platform account and/or account data binding candidates already returned by Cognee. Select only candidates that satisfy the user query and produce the next legal NodeSet contracts.

Output JSON, no markdown:
```json
{
  "selected_platform_account_ids": [],
  "selected_binding_ids": [],
  "rejected_candidate_ids": [],
  "selection_reasons": {},
  "next_search_contracts": [],
  "blocked_reasons": []
}
```

Rules:
1. If you selected a `platform_account`, the next search must be `runtime_account_binding_search` using that exact `platform_account_id`.
2. Do not search account bindings by `platform_id` alone.
3. If an `account_data_binding` is selected, the next search must be `semantic_table_frame_search` for that binding's exact `table_id`.
4. Do not invent source-role synonyms. Use only source roles present in returned candidates or user text.
5. If required roles are absent from runtime bindings, mark `blocked_reasons` instead of expanding platforms or roles.
6. Every emitted contract must include `card_type:<type>` when `allowed_card_types` is present.

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

Next selected-binding table-frame contract example:
```json
{
  "contract_id": "q3.semantic.table_frame.amazon_settlement",
  "stage": "semantic_table_frame_search",
  "query_text": "Table frame for selected settlement binding table.zs_observe.amazon_settlement",
  "node_sets": [
    "card_type:table",
    "table_id:table.zs_observe.amazon_settlement"
  ],
  "top_k": 3,
  "allowed_card_types": ["table"],
  "required_carry_forward": {
    "account_data_binding_id": "<selected_binding_id>",
    "platform_account_id": "<selected_platform_account_id>",
    "source_role": "<selected_binding_source_role>",
    "scope_keys": []
  }
}
```
