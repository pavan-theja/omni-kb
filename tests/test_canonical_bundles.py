import importlib.util
import tempfile
import unittest
from pathlib import Path


class CanonicalBundlesTest(unittest.TestCase):
    def test_default_bundle_shape_is_single_add_document(self):
        module = _load_bundle_module()
        cards = [
            _card("table.zs_observe.orders", "table"),
            _card("column.zs_observe.orders.order_id", "column"),
        ]
        edges = [
            {
                "source_id": "table.zs_observe.orders",
                "edge_type": "HAS_COLUMN",
                "target_id": "column.zs_observe.orders.order_id",
            }
        ]

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            result = module.dump_canonical_bundles(cards, edges, output_dir)
            documents = sorted((output_dir / "documents").glob("*.md"))

        self.assertEqual(1, result["document_count"])
        self.assertEqual(["canonical_all.md"], [path.name for path in documents])


def _card(canonical_id: str, card_type: str):
    return {
        "canonical_id": canonical_id,
        "card_type": card_type,
        "name": canonical_id,
        "description": "Test card.",
        "status": "draft",
    }


def _load_bundle_module():
    path = Path(__file__).resolve().parents[1] / "processed_kb_docs" / "dump_canonical_bundles.py"
    spec = importlib.util.spec_from_file_location("dump_canonical_bundles_for_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
