import unittest

from zenkb.canonical import validate_canonical


class CanonicalValidationTest(unittest.TestCase):
    def test_valid_card_and_edge(self):
        cards = [
            {
                "card_type": "table",
                "canonical_id": "table.zs_observe.shiprocket_settlement",
                "name": "Shiprocket Settlement",
                "description": "Settlement table.",
                "status": "active",
                "confidence": "curated",
                "source_documents": ["Source/Logistics KB/01 shiprocket_logistics.md"],
                "created_by": "kb_pipeline",
                "updated_by": "kb_pipeline",
                "created_at": "2026-05-20",
                "updated_at": "2026-05-20",
                "evidence_refs": [{"chunk_id": "chunk-1"}],
            },
            {
                "card_type": "column",
                "canonical_id": "column.zs_observe.shiprocket_settlement.awb_number",
                "name": "AWB Number",
                "description": "Shipment identifier.",
                "status": "active",
                "confidence": "curated",
                "source_documents": ["Source/Logistics KB/01 shiprocket_logistics.md"],
                "created_by": "kb_pipeline",
                "updated_by": "kb_pipeline",
                "created_at": "2026-05-20",
                "updated_at": "2026-05-20",
                "evidence_refs": [{"chunk_id": "chunk-1"}],
            },
        ]
        edges = [
            {
                "source_id": "table.zs_observe.shiprocket_settlement",
                "edge_type": "HAS_COLUMN",
                "target_id": "column.zs_observe.shiprocket_settlement.awb_number",
                "confidence": "curated",
                "evidence_refs": [{"chunk_id": "chunk-1"}],
            }
        ]

        result = validate_canonical(cards, edges, known_chunk_ids=["chunk-1"])

        self.assertTrue(result.ok)
        self.assertEqual(result.card_count, 2)
        self.assertEqual(result.edge_count, 1)

    def test_invalid_edge_endpoint_fails(self):
        result = validate_canonical(
            cards=[],
            edges=[
                {
                    "source_id": "table.missing",
                    "edge_type": "HAS_COLUMN",
                    "target_id": "column.missing",
                    "confidence": "curated",
                    "evidence_refs": [{"chunk_id": "chunk-1"}],
                }
            ],
        )

        self.assertFalse(result.ok)

    def test_metric_implementation_id_prefix_alias_is_valid(self):
        result = validate_canonical(
            cards=[
                {
                    "card_type": "metric_implementation",
                    "canonical_id": "metric_impl.shiprocket_settlement.cod_remitted_amount",
                    "name": "COD Remitted Amount",
                    "description": "Implementation.",
                    "status": "draft",
                    "confidence": "inferred",
                    "source_documents": ["Source/Logistics KB/01 shiprocket_logistics.md"],
                    "created_by": "kb_pipeline",
                    "updated_by": "kb_pipeline",
                    "created_at": "2026-05-20",
                    "updated_at": "2026-05-20",
                    "evidence_refs": [{"chunk_id": "chunk-1"}],
                }
            ],
            edges=[],
            known_chunk_ids=["chunk-1"],
        )

        self.assertTrue(result.ok)

    def test_rejects_invalid_canonical_id_shape(self):
        result = validate_canonical(cards=[_card("Table.Bad ID", "table")], edges=[])

        self.assertFalse(result.ok)
        self.assertIn("invalid canonical_id format", _messages(result))

    def test_rejects_card_type_prefix_mismatch(self):
        result = validate_canonical(cards=[_card("metric.amazon_gross_sales", "table")], edges=[])

        self.assertFalse(result.ok)
        self.assertIn("canonical_id must be prefixed by card_type", _messages(result))

    def test_rejects_duplicate_canonical_ids(self):
        result = validate_canonical(
            cards=[
                _card("table.zs_observe.shiprocket_settlement", "table"),
                _card("table.zs_observe.shiprocket_settlement", "table"),
            ],
            edges=[],
        )

        self.assertFalse(result.ok)
        self.assertIn("duplicate canonical_id", _messages(result))

    def test_validation_test_id_prefix_alias_is_valid(self):
        result = validate_canonical(cards=[_card("validation.awb_not_null", "validation_test")], edges=[])

        self.assertTrue(result.ok)


def _card(canonical_id, card_type):
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
        "evidence_refs": [{"chunk_id": "chunk-1"}],
    }


def _messages(result):
    return {issue.message for issue in result.issues}


if __name__ == "__main__":
    unittest.main()
