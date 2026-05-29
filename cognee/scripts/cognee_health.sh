#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import json
import urllib.request

url = "http://localhost:8000/health"
with urllib.request.urlopen(url, timeout=10) as response:
    body = response.read().decode("utf-8")
    print(body or json.dumps({"status": response.status}))
PY
