#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COGNEE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${COGNEE_DIR}/.." && pwd)"

cd "${REPO_ROOT}"
docker compose -f cognee/compose.yaml down
