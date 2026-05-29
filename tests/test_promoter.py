import json
import tempfile
import unittest
from pathlib import Path

from zenkb.promoter import promote_intermediate


class PromoterTest(unittest.TestCase):
    def test_promotes_valid_candidates(self):
        cards = [
            _card("table.zs_observe.shiprocket_settlement", "table", "chunk-1"),
            _card(
                "column.zs_observe.shiprocket_settlement.awb_number",
                "column",
                "chunk-1",
            ),
        ]
        edges = [
            {
                "source_id": "table.zs_observe.shiprocket_settlement",
                "edge_type": "HAS_COLUMN",
                "target_id": "column.zs_observe.shiprocket_settlement.awb_number",
                "confidence": "inferred",
                "evidence_refs": [{"chunk_id": "chunk-1"}],
            }
        ]

        with tempfile.TemporaryDirectory() as tmp:
            result = promote_intermediate(
                cards,
                edges,
                [],
                ["chunk-1"],
                Path(tmp),
            )

            self.assertEqual(result.promoted_card_count, 2)
            self.assertEqual(result.promoted_edge_count, 1)
            self.assertTrue((Path(tmp) / "cards.jsonl").exists())
            self.assertTrue((Path(tmp) / "edges.jsonl").exists())
            promoted_cards = [
                json.loads(line)
                for line in (Path(tmp) / "cards.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            table_card = next(
                card
                for card in promoted_cards
                if card["canonical_id"] == "table.zs_observe.shiprocket_settlement"
            )
            self.assertEqual(
                table_card["column_ids"],
                ["column.zs_observe.shiprocket_settlement.awb_number"],
            )
            manifest = json.loads((Path(tmp) / "manifest.json").read_text(encoding="utf-8"))
            self.assertTrue(manifest["validation"]["ok"])

    def test_normalizes_generic_metrics_and_implementation_links(self):
        cards = [
            _card("metric.amazon_gross_sales_gmv", "metric", "chunk-1"),
            _card("metric.flipkart_gross_sales_gmv", "metric", "chunk-1"),
            {
                **_card("metric_impl.amazon_oms.gross_sales_gmv", "metric_implementation", "chunk-1"),
                "metric_id": "metric.amazon_gross_sales_gmv",
                "base_tables": ["table.amazon_oms"],
            },
            {
                **_card("metric_impl.flipkart_oms.gross_sales_gmv", "metric_implementation", "chunk-1"),
                "metric_id": "metric.flipkart_gross_sales_gmv",
                "base_tables": ["table.flipkart_oms"],
            },
            _card("table.zs_observe.amazon_oms", "table", "chunk-1"),
            _card("table.amazon_oms", "table", "chunk-1"),
            _card("table.flipkart_oms", "table", "chunk-1"),
        ]
        edges = [
            {
                "source_id": "metric.amazon_gross_sales_gmv",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.amazon_oms.gross_sales_gmv",
                "confidence": "inferred",
                "evidence_refs": [{"chunk_id": "chunk-1"}],
            },
            {
                "source_id": "metric.flipkart_gross_sales_gmv",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.flipkart_oms.gross_sales_gmv",
                "confidence": "inferred",
                "evidence_refs": [{"chunk_id": "chunk-1"}],
            },
        ]

        with tempfile.TemporaryDirectory() as tmp:
            promote_intermediate(cards, edges, [], ["chunk-1"], Path(tmp))

            promoted_cards = [
                json.loads(line)
                for line in (Path(tmp) / "cards.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            promoted_edges = [
                json.loads(line)
                for line in (Path(tmp) / "edges.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            card_by_id = {card["canonical_id"]: card for card in promoted_cards}
            edge_keys = {
                (edge["source_id"], edge["edge_type"], edge["target_id"])
                for edge in promoted_edges
            }

            self.assertIn("metric.gross_sales_gmv", card_by_id)
            self.assertNotIn("metric.amazon_gross_sales_gmv", card_by_id)
            self.assertEqual(
                card_by_id["metric.gross_sales_gmv"]["implementation_ids"],
                [
                    "metric_impl.amazon_oms.gross_sales_gmv",
                    "metric_impl.flipkart_oms.gross_sales_gmv",
                ],
            )
            self.assertEqual(
                card_by_id["metric_impl.amazon_oms.gross_sales_gmv"]["metric_id"],
                "metric.gross_sales_gmv",
            )
            self.assertEqual(
                card_by_id["metric_impl.amazon_oms.gross_sales_gmv"]["base_tables"],
                ["table.zs_observe.amazon_oms"],
            )
            self.assertIn(
                (
                    "metric.gross_sales_gmv",
                    "HAS_IMPLEMENTATION",
                    "metric_impl.amazon_oms.gross_sales_gmv",
                ),
                edge_keys,
            )

    def test_infers_missing_metric_parent_for_implementation(self):
        cards = [
            _card("metric_impl.dtdc_settlement.cod_remitted_amount", "metric_implementation", "chunk-1"),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            promote_intermediate(cards, [], [], ["chunk-1"], Path(tmp))

            promoted_cards = [
                json.loads(line)
                for line in (Path(tmp) / "cards.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            card_by_id = {card["canonical_id"]: card for card in promoted_cards}

            self.assertIn("metric.cod_remitted_amount", card_by_id)
            self.assertEqual(
                card_by_id["metric_impl.dtdc_settlement.cod_remitted_amount"]["metric_id"],
                "metric.cod_remitted_amount",
            )

    def test_blocks_candidates_with_blocking_review_evidence(self):
        cards = [_card("table.zs_observe.shiprocket_settlement", "table", "chunk-1")]

        with tempfile.TemporaryDirectory() as tmp:
            result = promote_intermediate(
                cards,
                [],
                [
                    {
                        "severity": "blocking",
                        "review_type": "ambiguous",
                        "chunk_id": "chunk-1",
                    }
                ],
                ["chunk-1"],
                Path(tmp),
            )

            self.assertEqual(result.promoted_card_count, 0)
            self.assertEqual(result.blocked_card_count, 1)


def _card(canonical_id: str, card_type: str, chunk_id: str):
    return {
        "card_type": card_type,
        "canonical_id": canonical_id,
        "name": canonical_id.split(".")[-1],
        "description": "Test card.",
        "status": "draft",
        "confidence": "inferred",
        "source_documents": ["Source/Test.md"],
        "created_by": "test",
        "updated_by": "test",
        "created_at": "2026-05-20",
        "updated_at": "2026-05-20",
        "evidence_refs": [{"chunk_id": chunk_id}],
    }


if __name__ == "__main__":
    unittest.main()
