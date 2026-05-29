import json
import tempfile
import unittest
from pathlib import Path

from zenkb.cognee_export import export_cognee, render_cognee_document


class CogneeExportTest(unittest.TestCase):
    def test_render_document_includes_metadata_relationships_and_evidence(self):
        card = _card("table.zs_observe.shiprocket_settlement", "table")
        outgoing = [
            {
                "source_id": "table.zs_observe.shiprocket_settlement",
                "edge_type": "HAS_COLUMN",
                "target_id": "column.zs_observe.shiprocket_settlement.awb_number",
            }
        ]

        markdown = render_cognee_document(card, outgoing, [])

        self.assertIn("canonical_id: \"table.zs_observe.shiprocket_settlement\"", markdown)
        self.assertIn("# Shiprocket Settlement", markdown)
        self.assertIn("## Retrieval Fields", markdown)
        self.assertIn("outgoing `HAS_COLUMN`", markdown)
        self.assertIn("chunk `chunk-1`", markdown)

    def test_export_writes_documents_metadata_and_manifest(self):
        cards = [
            _card("table.zs_observe.shiprocket_settlement", "table"),
            _card("column.zs_observe.shiprocket_settlement.awb_number", "column"),
        ]
        edges = [
            {
                "source_id": "table.zs_observe.shiprocket_settlement",
                "edge_type": "HAS_COLUMN",
                "target_id": "column.zs_observe.shiprocket_settlement.awb_number",
                "confidence": "inferred",
            }
        ]

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            result = export_cognee(cards, edges, output_dir)

            self.assertEqual(result.document_count, 2)
            self.assertTrue((output_dir / "metadata.jsonl").exists())
            self.assertTrue((output_dir / "manifest.json").exists())
            metadata = [
                json.loads(line)
                for line in (output_dir / "metadata.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual(len(metadata), 2)
            self.assertTrue((output_dir / metadata[0]["document_path"]).exists())


def _card(canonical_id: str, card_type: str):
    name = canonical_id.split(".")[-1].replace("_", " ").title()
    return {
        "card_type": card_type,
        "canonical_id": canonical_id,
        "name": name,
        "description": "Test card.",
        "status": "draft",
        "confidence": "inferred",
        "review_status": "unreviewed",
        "version": "0.1",
        "source_documents": ["Source/Test.md"],
        "tags": ["test"],
        "table_name": "shiprocket_settlement",
        "full_reference": "zs_observe.shiprocket_settlement",
        "evidence_refs": [
            {
                "source_doc": "Source/Test.md",
                "source_span": "lines 1-2",
                "chunk_id": "chunk-1",
            }
        ],
    }


if __name__ == "__main__":
    unittest.main()
