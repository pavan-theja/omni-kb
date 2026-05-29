import json
import unittest
from pathlib import Path
from unittest.mock import patch

from zenkb.retrieval import build_sql_context_bundle


ROOT = Path(__file__).resolve().parents[1]


class TenantRetrievalFixtureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = _load_jsonl(ROOT / "canonical/cards.jsonl")
        cls.edges = _load_jsonl(ROOT / "canonical/edges.jsonl")

    def test_ardeur_amazon_scope_path(self):
        expected_ids = {
            "tenant.ardeur_fashion",
            "group.ardeur_fashion.zeal_bizfashion_ventures",
            "platform.amazon",
            "platform_account.ardeur_fashion.amazon_in.primary",
            "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",
            "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement",
            "table.zs_observe.amazon_oms",
        }
        bundle = self._bundle(
            "Show Ardeur Amazon order and settlement context.",
            expected_ids,
            tenant="tenant.ardeur_fashion",
            platform="platform.amazon",
        )

        self.assert_has_cards(bundle, expected_ids)
        self.assertFalse(any("platform_account.ardeur_fashion.flipkart" in card_id for card_id in _card_ids(bundle)))

    def test_seller_realization_metric_context(self):
        expected_ids = {
            "metric.seller_realization_rate",
            "metric_implementation.myntra_settlement.seller_realization_rate",
            "metric_implementation.flipkart.realization_rate",
            "metric_implementation.amazon.amazon_settlement.seller_realization_rate",
        }
        bundle = self._bundle("Generate seller realization rate context.", expected_ids)

        self.assert_has_cards(bundle, expected_ids)

    def test_shiprocket_context_does_not_require_client_scope(self):
        expected_ids = {
            "platform.shiprocket",
            "table.zs_observe.shiprocket_oms",
            "table.zs_observe.shiprocket_settlement",
            "relationship.shiprocket_oms.shiprocket_settlement.awb",
        }
        bundle = self._bundle("Show Shiprocket OMS to settlement relationship context.", expected_ids)

        self.assert_has_cards(bundle, expected_ids)

    def _bundle(self, query, candidate_ids, **scope):
        with patch(
            "zenkb.retrieval._cognee_discovery_results",
            return_value=_cognee_discovery_payload(candidate_ids),
        ):
            return build_sql_context_bundle(
                query,
                self.cards,
                self.edges,
                max_seed_cards=100,
                max_cards=100,
                scope_overrides=scope or None,
            )

    def assert_has_cards(self, bundle, expected_ids):
        missing = sorted(expected_ids - _card_ids(bundle))
        self.assertEqual([], missing)


def _load_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _card_ids(bundle):
    return {card["canonical_id"] for card in bundle["cards"]}


def _cognee_discovery_payload(candidate_ids):
    return [
        {
            "query_type": "answer_context",
            "query": "fixture answer context",
            "results": ["Use canonical candidates."],
        },
        {
            "query_type": "canonical_candidate_discovery",
            "query": "fixture candidate discovery",
            "results": ["Relevant canonical IDs: " + ", ".join(sorted(candidate_ids))],
        },
    ]


if __name__ == "__main__":
    unittest.main()

