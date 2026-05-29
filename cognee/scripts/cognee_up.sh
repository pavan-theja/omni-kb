#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COGNEE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${COGNEE_DIR}/.." && pwd)"

cd "${REPO_ROOT}"

PREPARE_ARGS=()
FORCE_RECREATE=false
BUILD_IMAGE=false
ENV_FILE="cognee/.env"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --llm-provider|--embedding-provider)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for $1" >&2
        exit 2
      fi
      PREPARE_ARGS+=("$1" "$2")
      FORCE_RECREATE=true
      shift 2
      ;;
    --env-file|--profile|--runtime-key)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for $1" >&2
        exit 2
      fi
      if [[ "$1" == "--env-file" ]]; then
        ENV_FILE="$2"
      fi
      PREPARE_ARGS+=("$1" "$2")
      FORCE_RECREATE=true
      shift 2
      ;;
    --force-recreate)
      FORCE_RECREATE=true
      shift
      ;;
    --build)
      BUILD_IMAGE=true
      shift
      ;;
    -h|--help)
      cat <<'EOF'
Usage: cognee/scripts/cognee_up.sh [options]

Options:
  --env-file PATH                     Source env file. Defaults to cognee/.env.
  --profile plain|canonical|custom    Runtime profile used in provider-keyed DB paths.
  --runtime-key KEY                   Explicit runtime key override.
  --llm-provider azure|gemini|vertex
  --embedding-provider azure|gemini|vertex
  --build
  --force-recreate

Starts the local Cognee Docker stack after preparing a provider-keyed runtime env.
EOF
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

if [[ ! -f "${ENV_FILE}" ]]; then
  if [[ "${ENV_FILE}" == "cognee/.env" ]]; then
    cp cognee/.env.example cognee/.env
    echo "Created cognee/.env from cognee/.env.example."
    echo "Set provider credentials in cognee/.env, then rerun this command."
    exit 1
  fi
  echo "Missing env file: ${ENV_FILE}" >&2
  exit 1
fi

python3 cognee/scripts/prepare_cognee_env.py "${PREPARE_ARGS[@]}"
if [[ -f cognee/runtime/current_runtime.env ]]; then
  set -a
  # shellcheck disable=SC1091
  source cognee/runtime/current_runtime.env
  set +a
fi
COMPOSE_ARGS=(-f cognee/compose.yaml up -d)
if [[ "${BUILD_IMAGE}" == "true" ]]; then
  COMPOSE_ARGS+=(--build)
fi
if [[ "${FORCE_RECREATE}" == "true" ]]; then
  COMPOSE_ARGS+=(--force-recreate)
fi
docker compose "${COMPOSE_ARGS[@]}"
echo "Cognee runtime key: ${COGNEE_RUNTIME_KEY:-unknown}"
echo "Cognee API: http://localhost:8000"
echo "Cognee docs: http://localhost:8000/docs"
