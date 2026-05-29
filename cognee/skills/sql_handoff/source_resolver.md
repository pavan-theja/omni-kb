# Source Resolver Skill

Resolve candidate sources. Do not produce SQL.

Resolution order:
1. tenant/account scope from user input
2. account_data_binding/platform_account only to identify candidate platforms and source bindings
3. physical table cards for those bindings
4. column cards for selected physical tables
5. relationship cards for join keys between selected physical tables
6. query_pattern cards only to reuse grounded SQL logic
7. business_flow_binding/business_process only for process context if table/relationship context is insufficient

Question:
{{query}}

{{scope}}

Intent JSON:
{{intent_json}}

Retrieved context:
{{context}}

Rules:
- First decide `answer_mode`:
  - `physical_sql`: the user request can be answered by querying runtime SQL tables.
  - `metadata_inventory`: the user asks for source topology, account/platform bindings, OMS-marketplace mappings, supported marketplaces, workflow dependencies, or other catalog/inventory facts that live in canonical metadata.
  - `partial`: useful evidence exists, but required tables/columns/join keys/deduplication rules are missing.
- Prefer the smallest complete source set.
- Stop once 1-3 sources are enough.
- Do not expand into every retrieved artifact.
- For `physical_sql`, `selected? = Yes` only for physical runtime SQL tables that should be used later.
- For `metadata_inventory`, `selected? = Yes` for the smallest canonical metadata cards or physical table cards that prove the mapping/inventory. These selected cards are evidence, not SQL tables.
- Canonical metadata selected as evidence must be clearly labeled with roles such as `Selected Metadata Evidence` or `Supporting Metadata Evidence`.
- Do not treat one marketplace as representative of all marketplaces unless the question explicitly asks for that marketplace or the context proves it is the only applicable source.

Classify each candidate:
- direct: contains the requested grain and required metric/status fields.
- supporting: helps identify scope, channel, platform, process, or join path but cannot answer alone.
- risky: appears relevant but lacks join keys, filters, status fields, grain, or dedupe rules.
- irrelevant: retrieved but not useful.

Return a top-level JSON object with exactly one key named `content`.
The `content` value must be a string containing a JSON-serialized object with keys:
`answer_mode`, `selected_sources`, `candidates`, `supporting_metadata`, `rejected_sources`, `missing_or_risky`, `reason`.
