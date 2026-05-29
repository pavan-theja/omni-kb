import io
import importlib.util
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


class CogneeIngestSimpleTest(unittest.TestCase):
    def test_shape_keeps_whole_cards_and_writes_token_capped_packs(self):
        module = _load_simple_ingest_module()
        cards = [
            _card("table.zs_observe.orders", "table", "orders " * 80),
            _card("column.zs_observe.orders.order_id", "column", "order id " * 80),
            _card("metric.amazon.gmv", "metric", "gross sales " * 80),
        ]
        edges = [
            {
                "source_id": "table.zs_observe.orders",
                "edge_type": "HAS_COLUMN",
                "target_id": "column.zs_observe.orders.order_id",
            }
        ]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cards_path = root / "cards.jsonl"
            edges_path = root / "edges.jsonl"
            _write_jsonl(cards_path, cards)
            _write_jsonl(edges_path, edges)

            manifest = module.shape_canonical_dataset(
                cards_path=cards_path,
                edges_path=edges_path,
                output_dir=root / "shaped",
                max_tokens=600,
            )
            documents = sorted((root / "shaped" / "documents").glob("*.md"))
            metadata = [
                json.loads(line)
                for line in (root / "shaped" / "metadata.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            markdown_documents = [path.read_text(encoding="utf-8") for path in documents]

        self.assertGreater(manifest["document_count"], 1)
        self.assertEqual(manifest["document_count"], len(documents))
        self.assertEqual(
            sorted(card["canonical_id"] for card in cards),
            sorted(card_id for record in metadata for card_id in record["canonical_ids"]),
        )
        for markdown in markdown_documents:
            self.assertEqual(markdown.count("BEGIN_CANONICAL_CARD"), markdown.count("END_CANONICAL_CARD"))

    def test_add_documents_batches_shaped_files(self):
        module = _load_simple_ingest_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = []
            for index in range(3):
                path = root / f"canonical_pack_{index + 1:04d}.md"
                path.write_text(f"# pack {index}\n", encoding="utf-8")
                docs.append(path)

            client = _FakeClient()
            with redirect_stdout(io.StringIO()):
                module.add_documents(
                    client,
                    dataset="test_dataset",
                    document_paths=docs,
                    batch_size=2,
                    timeout=1,
                    no_progress=True,
                )

        self.assertEqual(2, len(client.multipart_calls))
        self.assertEqual("/api/v1/add", client.multipart_calls[0][0])
        self.assertEqual("test_dataset", client.multipart_calls[0][1]["datasetName"])
        self.assertEqual([path.name for _, path in client.multipart_calls[0][2]], ["canonical_pack_0001.md", "canonical_pack_0002.md"])

    def test_cognify_dataset_posts_simple_background_payload(self):
        module = _load_simple_ingest_module()
        client = _FakeClient()

        with redirect_stdout(io.StringIO()):
            module.cognify_dataset(client, dataset="test_dataset", timeout=1)

        self.assertEqual(
            [
                (
                    "/api/v1/cognify",
                    {"datasets": ["test_dataset"], "runInBackground": True},
                    1,
                )
            ],
            client.post_json_calls,
        )

    def test_batched_cognify_uses_suffixed_datasets_and_foreground_cognify(self):
        module = _load_simple_ingest_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = []
            for index in range(3):
                path = root / f"canonical_pack_{index + 1:04d}.md"
                path.write_text(f"# pack {index}\n", encoding="utf-8")
                docs.append(path)

            client = _FakeClient()
            with redirect_stdout(io.StringIO()):
                dataset_names = module.add_and_cognify_dataset_batches(
                    client,
                    dataset="test_dataset",
                    document_paths=docs,
                    dataset_batch_size=2,
                    add_batch_size=2,
                    timeout=1,
                    no_progress=True,
                    wait_for_completion=False,
                )

        self.assertEqual(["test_dataset_batch_0001", "test_dataset_batch_0002"], dataset_names)
        self.assertEqual(
            ["test_dataset_batch_0001", "test_dataset_batch_0002"],
            [call[1]["datasetName"] for call in client.multipart_calls],
        )
        self.assertEqual(
            [
                (
                    "/api/v1/cognify",
                    {"datasets": ["test_dataset_batch_0001"], "runInBackground": True},
                    1,
                ),
                (
                    "/api/v1/cognify",
                    {"datasets": ["test_dataset_batch_0002"], "runInBackground": True},
                    1,
                ),
            ],
            client.post_json_calls,
        )

    def test_same_dataset_cognify_scope_adds_batches_to_one_dataset(self):
        module = _load_simple_ingest_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = []
            for index in range(3):
                path = root / f"canonical_pack_{index + 1:04d}.md"
                path.write_text(f"# pack {index}\n", encoding="utf-8")
                docs.append(path)

            client = _FakeClient()
            with redirect_stdout(io.StringIO()):
                dataset_names = module.add_and_cognify_dataset_batches(
                    client,
                    dataset="test_dataset",
                    document_paths=docs,
                    dataset_batch_size=2,
                    add_batch_size=2,
                    cognify_scope="same-dataset",
                    timeout=1,
                    no_progress=True,
                    wait_for_completion=False,
                )

        self.assertEqual(["test_dataset"], dataset_names)
        self.assertEqual(
            ["test_dataset", "test_dataset"],
            [call[1]["datasetName"] for call in client.multipart_calls],
        )
        self.assertEqual(
            [
                (
                    "/api/v1/cognify",
                    {"datasets": ["test_dataset"], "runInBackground": True},
                    1,
                ),
                (
                    "/api/v1/cognify",
                    {"datasets": ["test_dataset"], "runInBackground": True},
                    1,
                ),
            ],
            client.post_json_calls,
        )


class _FakeClient:
    def __init__(self):
        self.multipart_calls = []
        self.post_json_calls = []

    def post_multipart(self, path, *, fields, files, timeout):
        self.multipart_calls.append((path, fields, files, timeout))
        return {"status": "ok", "data_ingestion_info": list(files)}

    def post_json(self, path, payload, *, timeout):
        self.post_json_calls.append((path, payload, timeout))
        return {"status": "started", "pipeline_run_id": "run-1"}


def _card(canonical_id: str, card_type: str, description: str):
    return {
        "canonical_id": canonical_id,
        "card_type": card_type,
        "name": canonical_id,
        "description": description,
        "status": "active",
        "scope_keys": [{"column": "group_id", "operator": "=", "value": 1}],
    }


def _write_jsonl(path: Path, records):
    path.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )


def _load_simple_ingest_module():
    path = Path(__file__).resolve().parents[1] / "cognee" / "scripts" / "cognee_ingest_simple.py"
    spec = importlib.util.spec_from_file_location("cognee_ingest_simple_for_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
