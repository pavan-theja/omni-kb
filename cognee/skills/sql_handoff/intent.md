# Deprecated Intent Skill

The staged handoff no longer uses this file directly.

Current intent flow:
1. `raw_intent` is computed locally from only the user query and explicit scope.
2. `discovery.md` retrieves evidence guided by raw intent.
3. `grounded_intent.md` refines raw intent using retrieved evidence.

Edit `grounded_intent.md` for grounded intent behavior.
