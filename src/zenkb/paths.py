from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_SOURCE_DIR = REPO_ROOT / "raw" / "Source"
CLEANED_V2_SOURCE_DIR = REPO_ROOT / "raw" / "Source" / "cleaned"
BUILD_DIR = REPO_ROOT / "build"
CHUNKS_DIR = BUILD_DIR / "chunks"
INTERMEDIATE_DIR = BUILD_DIR / "intermediate"
PROCESSED_KB_DIR = REPO_ROOT / "processed_kb_docs" / "cleaned"
CANONICAL_DIR = REPO_ROOT / "canonical"
COGNEE_DIR = REPO_ROOT / "cognee"
COGNEE_EXPORT_DIR = COGNEE_DIR / "export"
