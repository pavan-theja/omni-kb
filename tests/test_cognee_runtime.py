import tempfile
import unittest
import importlib.util
from pathlib import Path

from zenkb.cognee_runtime.config import CogneeRuntimeConfig
from zenkb.cognee_runtime.ingestion import (
    IngestOptions,
    IngestionProfile,
    build_cognify_payload,
    ingest_documents,
)
from zenkb.cognee_runtime.runtime_key import build_runtime_key
from zenkb.cognee_runtime.status import progress_snapshot_from_response, status_summary


class CogneeRuntimeTest(unittest.TestCase):
    def test_plain_cognify_payload_matches_v1_shape(self):
        payload = build_cognify_payload(
            "zenstatement_canonical",
            run_in_background=True,
            graph_model=None,
            custom_prompt="",
            data_per_batch=None,
            chunks_per_batch=None,
            chunk_size=None,
        )

        self.assertEqual(
            {
                "datasets": ["zenstatement_canonical"],
                "runInBackground": True,
            },
            payload,
        )

    def test_canonical_cognify_payload_matches_v2_shape(self):
        payload = build_cognify_payload(
            "zenstatement_canonical",
            run_in_background=True,
            graph_model={"title": "CanonicalGraph", "type": "object"},
            custom_prompt="justify every edge",
            data_per_batch=1,
            chunks_per_batch=5,
            chunk_size=2048,
        )

        self.assertEqual(["zenstatement_canonical"], payload["datasets"])
        self.assertEqual(True, payload["runInBackground"])
        self.assertEqual(1, payload["dataPerBatch"])
        self.assertEqual(5, payload["chunksPerBatch"])
        self.assertEqual(2048, payload["chunkSize"])
        self.assertEqual({"title": "CanonicalGraph", "type": "object"}, payload["graphModel"])
        self.assertEqual("justify every edge", payload["customPrompt"])

    def test_runtime_key_changes_by_provider_and_model(self):
        base = {
            "ZENKB_COGNEE_LLM_PROVIDER": "vertex",
            "LLM_MODEL": "vertex_ai/gemini-2.0-flash",
            "ZENKB_COGNEE_EMBEDDING_PROVIDER": "vertex",
            "EMBEDDING_MODEL": "vertex_ai/gemini-embedding-001",
            "EMBEDDING_DIMENSIONS": "1536",
        }
        changed = dict(base)
        changed["ZENKB_COGNEE_EMBEDDING_PROVIDER"] = "azure"
        changed["EMBEDDING_MODEL"] = "azure/text-embedding-3-small"

        self.assertNotEqual(
            build_runtime_key(base, profile="canonical"),
            build_runtime_key(changed, profile="canonical"),
        )

    def test_staged_prepare_adds_documents_without_cognify(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs_dir = root / "docs"
            docs_dir.mkdir()
            (docs_dir / "card.md").write_text("# Card\n", encoding="utf-8")
            client = _FakeClient()

            result = ingest_documents(
                CogneeRuntimeConfig(
                    base_url="http://localhost:8000",
                    dataset="test_dataset",
                    docs_dir=docs_dir,
                    runtime_env=root / "missing.env",
                    request_timeout=1,
                    status_timeout=1,
                    poll_interval=1,
                    cognify_timeout=1,
                ),
                IngestionProfile(name="canonical"),
                IngestOptions(mode="staged", stage="build-embeddings", no_progress=True),
                client=client,
            )

        self.assertEqual(0, result)
        self.assertEqual(1, len(client.multipart_calls))
        self.assertEqual([], client.post_json_calls)

    def test_staged_edge_cognify_skips_add_and_updates_schema(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs_dir = root / "docs"
            docs_dir.mkdir()
            (docs_dir / "card.md").write_text("# Card\n", encoding="utf-8")
            graph_model = root / "graph.json"
            graph_model.write_text('{"title":"CanonicalGraph","type":"object"}', encoding="utf-8")
            prompt = root / "prompt.md"
            prompt.write_text("justify every edge", encoding="utf-8")
            client = _FakeClient()

            result = ingest_documents(
                CogneeRuntimeConfig(
                    base_url="http://localhost:8000",
                    dataset="test_dataset",
                    docs_dir=docs_dir,
                    runtime_env=root / "missing.env",
                    request_timeout=1,
                    status_timeout=1,
                    poll_interval=0.01,
                    cognify_timeout=1,
                ),
                IngestionProfile(
                    name="canonical",
                    graph_model=graph_model,
                    custom_prompt=prompt,
                    update_schema=True,
                    cognify_data_per_batch=1,
                    cognify_chunks_per_batch=5,
                    cognify_chunk_size=2048,
                ),
                IngestOptions(mode="staged", stage="edge-cognify", no_progress=True),
                client=client,
            )

        self.assertEqual(0, result)
        self.assertEqual([], client.multipart_calls)
        self.assertEqual(1, len(client.put_json_calls))
        self.assertEqual(1, len(client.post_json_calls))
        self.assertEqual("/api/v1/cognify", client.post_json_calls[0][0])

    def test_prepare_env_writes_provider_keyed_runtime_paths(self):
        module = _load_prepare_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_file = root / ".env.azure"
            env_file.write_text(
                "\n".join(
                    [
                        "COGNEE_LLM_PROVIDER=azure",
                        "COGNEE_EMBEDDING_PROVIDER=azure",
                        "AZURE_API_BASE=https://example.openai.azure.com",
                        "AZURE_API_KEY=test-key",
                        "AZURE_API_VERSION=2024-02-01",
                        "AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini",
                        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small",
                    ]
                ),
                encoding="utf-8",
            )
            graph_model = root / "graph.json"
            graph_model.write_text('{"title":"CanonicalGraph","type":"object"}', encoding="utf-8")
            prompt = root / "prompt.md"
            prompt.write_text("justify every edge", encoding="utf-8")

            module.RUNTIME_ENV = root / "runtime" / "cognee.env"
            module.CURRENT_RUNTIME_ENV = root / "runtime" / "current_runtime.env"
            module.RUNTIME_INSTANCES_DIR = root / "runtime" / "instances"

            result = module.main(
                [
                    "--env-file",
                    str(env_file),
                    "--profile",
                    "canonical",
                    "--graph-model",
                    str(graph_model),
                    "--custom-prompt",
                    str(prompt),
                ]
            )

            current = module.CURRENT_RUNTIME_ENV.read_text(encoding="utf-8")
            active = module.RUNTIME_ENV.read_text(encoding="utf-8")

        self.assertEqual(0, result)
        self.assertIn("COGNEE_RUNTIME_KEY=canonical__", active)
        self.assertIn("COGNEE_RUNTIME_ENV_FILE=", current)
        self.assertIn("COGNEE_RUNTIME_SYSTEM_DIR=", current)
        self.assertIn("COGNEE_RUNTIME_DATA_DIR=", current)

    def test_prepare_env_defaults_to_external_cognee_backends(self):
        module = _load_prepare_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_file = root / ".env.azure"
            env_file.write_text(
                "\n".join(
                    [
                        "COGNEE_LLM_PROVIDER=azure",
                        "COGNEE_EMBEDDING_PROVIDER=azure",
                        "AZURE_API_BASE=https://example.openai.azure.com",
                        "AZURE_API_KEY=test-key",
                        "AZURE_API_VERSION=2024-02-01",
                        "AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini",
                        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small",
                    ]
                ),
                encoding="utf-8",
            )

            module.RUNTIME_ENV = root / "runtime" / "cognee.env"
            module.CURRENT_RUNTIME_ENV = root / "runtime" / "current_runtime.env"
            module.RUNTIME_INSTANCES_DIR = root / "runtime" / "instances"

            result = module.main(["--env-file", str(env_file), "--profile", "canonical"])

            active = module.RUNTIME_ENV.read_text(encoding="utf-8")

        self.assertEqual(0, result)
        self.assertIn("DB_PROVIDER=postgres", active)
        self.assertIn("DB_NAME=cognee_db", active)
        self.assertIn("DB_HOST=host.docker.internal", active)
        self.assertIn("DB_PORT=5432", active)
        self.assertIn("DB_USERNAME=cognee", active)
        self.assertIn("DB_PASSWORD=cognee", active)
        self.assertIn("GRAPH_DATABASE_PROVIDER=neo4j", active)
        self.assertIn("GRAPH_DATABASE_URL=bolt://host.docker.internal:7687", active)
        self.assertIn("VECTOR_DB_PROVIDER=qdrant", active)
        self.assertIn("VECTOR_DB_URL=http://host.docker.internal:6333", active)

    def test_prepare_env_uses_runtime_key_from_env_file(self):
        module = _load_prepare_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_file = root / ".env.vertex"
            env_file.write_text(
                "\n".join(
                    [
                        "COGNEE_RUNTIME_KEY=constrained-gemini35",
                        "COGNEE_LLM_PROVIDER=vertex",
                        "COGNEE_EMBEDDING_PROVIDER=vertex",
                        "VERTEX_AI_PROJECT_ID=test-project",
                        "VERTEX_AI_LOCATION=global",
                        "VERTEX_AI_LLM_MODEL=gemini-3.5-flash",
                        "VERTEX_AI_EMBEDDING_MODEL=gemini-embedding-2",
                        "VERTEX_AI_EMBEDDING_DIMENSIONALITY=3072",
                        "GOOGLE_APPLICATION_CREDENTIALS=/app/.google-credentials/service-account.json",
                    ]
                ),
                encoding="utf-8",
            )

            module.RUNTIME_ENV = root / "runtime" / "cognee.env"
            module.CURRENT_RUNTIME_ENV = root / "runtime" / "current_runtime.env"
            module.RUNTIME_INSTANCES_DIR = root / "runtime" / "instances"

            result = module.main(["--env-file", str(env_file)])

            active = module.RUNTIME_ENV.read_text(encoding="utf-8")
            current = module.CURRENT_RUNTIME_ENV.read_text(encoding="utf-8")

        self.assertEqual(0, result)
        self.assertIn("COGNEE_RUNTIME_KEY=constrained-gemini35", active)
        self.assertIn("instances/constrained-gemini35/cognee.env", current)

    def test_status_summary_prefers_cognify_chunk_progress(self):
        response = {
            "pipelines": [
                {"name": "add_pipeline", "status": "completed"},
                {
                    "name": "cognify_pipeline",
                    "status": "running",
                    "progress": {
                        "processed_chunks": 12,
                        "total_chunks": 100,
                    },
                },
            ]
        }

        snapshot = progress_snapshot_from_response(response)
        summary = status_summary(response, verbose=False)

        self.assertIsNotNone(snapshot)
        self.assertEqual(12, snapshot.current)
        self.assertEqual(100, snapshot.total)
        self.assertEqual("chunks", snapshot.unit)
        self.assertIn("12/100 chunks", summary)
        self.assertIn("cognify_pipeline=running", summary)

    def test_status_summary_falls_back_to_pipeline_status_without_counts(self):
        response = {"name": "cognify_pipeline", "status": "running"}

        self.assertIsNone(progress_snapshot_from_response(response))
        self.assertEqual("cognify_pipeline=running", status_summary(response, verbose=False))


class _FakeClient:
    def __init__(self):
        self.multipart_calls = []
        self.post_json_calls = []
        self.put_json_calls = []

    def post_multipart(self, path, *, fields, files, timeout):
        self.multipart_calls.append((path, fields, files, timeout))
        return {"status": "ok", "data_ingestion_info": list(files)}

    def resolve_dataset_id(self, dataset_name, *, timeout):
        return f"id-{dataset_name}"

    def put_json(self, path, payload, *, timeout):
        self.put_json_calls.append((path, payload, timeout))
        return {"status": "schema-updated"}

    def post_json(self, path, payload, *, timeout):
        self.post_json_calls.append((path, payload, timeout))
        return {"status": "started", "pipeline_run_id": "run-1"}

    def dataset_status(self, *, dataset_name, dataset_id, timeout):
        return {"name": "cognify_pipeline", "status": "completed"}


def _load_prepare_module():
    path = Path(__file__).resolve().parents[1] / "cognee" / "scripts" / "prepare_cognee_env.py"
    spec = importlib.util.spec_from_file_location("prepare_cognee_env_for_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
