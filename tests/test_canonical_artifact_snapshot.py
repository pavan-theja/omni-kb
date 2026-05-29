import json
import unittest
from collections import Counter
from pathlib import Path

from zenkb.canonical import validate_canonical
from zenkb.chunker import chunk_markdown_files


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_CARD_TYPES = {
    "account_data_binding": 469,
    "business_flow_binding": 82,
    "business_process": 99,
    "business_scope_set": 82,
    "column": 4489,
    "domain": 154,
    "execution_constraint_set": 56,
    "formula_template": 206,
    "group": 18,
    "matching_logic": 102,
    "metric": 339,
    "metric_dependency": 84,
    "metric_implementation": 469,
    "mismatch_category": 244,
    "output_contract": 81,
    "platform": 51,
    "platform_account": 254,
    "platform_context": 53,
    "process_variant": 14,
    "query_pattern": 398,
    "reconciliation_profile": 98,
    "reconciliation_side": 171,
    "reconciliation_unit": 107,
    "reconciliation_variant": 44,
    "relationship": 131,
    "review_item": 4,
    "rule": 350,
    "state_transition": 166,
    "table": 113,
    "tenant": 18,
    "validation_test": 272,
    "value_profile": 537,
    "workflow_step": 330,
}


class CanonicalArtifactSnapshotTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = _load_jsonl(ROOT / "canonical/cards.jsonl")
        cls.edges = _load_jsonl(ROOT / "canonical/edges.jsonl")
        cls.manifest = json.loads((ROOT / "canonical/manifest.json").read_text(encoding="utf-8"))
        cls.chunk_ids = {chunk.chunk_id for chunk in chunk_markdown_files(ROOT / "raw/Source")}

    def test_manifest_counts_match_snapshot(self):
        self.assertEqual(10085, len(self.cards))
        self.assertEqual(30299, len(self.edges))
        self.assertEqual(EXPECTED_CARD_TYPES, dict(sorted(Counter(card["card_type"] for card in self.cards).items())))
        self.assertEqual(10085, self.manifest["counts"]["promoted_cards"])
        self.assertEqual(30299, self.manifest["counts"]["promoted_edges"])
        self.assertEqual(EXPECTED_CARD_TYPES, self.manifest["card_types"])
        self.assertTrue(self.manifest["validation"]["ok"])

    def test_canonical_jsonl_order_is_deterministic(self):
        card_ids = [card["canonical_id"] for card in self.cards]
        edge_keys = [
            (edge["source_id"], edge["edge_type"], edge["target_id"])
            for edge in self.edges
        ]

        self.assertEqual(sorted(card_ids), card_ids)
        self.assertEqual(sorted(edge_keys), edge_keys)

    def test_required_reference_cards_and_edges_exist(self):
        card_ids = {card["canonical_id"] for card in self.cards}
        edge_keys = {
            (edge["source_id"], edge["edge_type"], edge["target_id"])
            for edge in self.edges
        }

        self.assertTrue(
            {
                "tenant.ardeur_fashion",
                "group.ardeur_fashion.zeal_bizfashion_ventures",
                "metric.seller_realization_rate",
                "metric_implementation.amazon.amazon_settlement.seller_realization_rate",
                "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",
                "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement",
                "platform_account.ardeur_fashion.amazon_in.primary",
                "table.zs_observe.shiprocket_settlement",
            }.issubset(card_ids)
        )
        self.assertIn(
            (
                "metric.marketplace.seller_realization_rate",
                "HAS_IMPLEMENTATION",
                "metric_implementation.amazon.amazon_settlement.seller_realization_rate",
            ),
            edge_keys,
        )
        self.assertIn(
            ("tenant.ardeur_fashion", "HAS_GROUP", "group.ardeur_fashion.zeal_bizfashion_ventures"),
            edge_keys,
        )

    def test_committed_canonical_artifacts_validate_against_chunks(self):
        result = validate_canonical(self.cards, self.edges, self.chunk_ids)

        self.assertTrue(result.ok, [issue for issue in result.issues if issue.severity == "error"])


def _load_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


if __name__ == "__main__":
    unittest.main()
