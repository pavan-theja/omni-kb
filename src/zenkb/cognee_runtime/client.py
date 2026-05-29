from __future__ import annotations

import json
import os
import socket
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import List, Sequence, Tuple

from .status import compact_json


class CogneeApiError(RuntimeError):
    def __init__(self, message: str, *, transient: bool = False) -> None:
        super().__init__(message)
        self.transient = transient


class CogneeClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def get_json(self, path_or_url: str, *, timeout: float) -> object:
        request = urllib.request.Request(self._url(path_or_url), headers=_headers({}), method="GET")
        return self._read_json(request, timeout=timeout)

    def post_json(self, path_or_url: str, payload: dict, *, timeout: float) -> object:
        return self._request_json(path_or_url, payload, timeout=timeout, method="POST")

    def put_json(self, path_or_url: str, payload: dict, *, timeout: float) -> object:
        return self._request_json(path_or_url, payload, timeout=timeout, method="PUT")

    def post_multipart(
        self,
        path_or_url: str,
        *,
        fields: dict[str, str],
        files: Sequence[Tuple[str, Path]],
        timeout: float,
    ) -> object:
        boundary = f"----zenkb-{uuid.uuid4().hex}"
        body = _multipart_body(boundary, fields, files)
        request = urllib.request.Request(
            self._url(path_or_url),
            data=body,
            headers=_headers({"Content-Type": f"multipart/form-data; boundary={boundary}"}),
            method="POST",
        )
        return self._read_json(request, timeout=timeout)

    def health(self, *, timeout: float) -> object:
        return self.get_json("/health", timeout=timeout)

    def datasets(self, *, timeout: float) -> object:
        return self.get_json("/api/v1/datasets", timeout=timeout)

    def resolve_dataset_id(self, dataset_name: str, *, timeout: float) -> str:
        response = self.datasets(timeout=timeout)
        if not isinstance(response, list):
            raise RuntimeError(f"Unexpected /api/v1/datasets response: {compact_json(response)}")
        for dataset in response:
            if not isinstance(dataset, dict):
                continue
            if dataset.get("name") == dataset_name:
                dataset_id = dataset.get("id") or dataset.get("dataset_id")
                if dataset_id:
                    return str(dataset_id)
        raise RuntimeError(f"Dataset not found: {dataset_name}")

    def dataset_status(
        self,
        *,
        dataset_name: str,
        dataset_id: str,
        timeout: float,
    ) -> object:
        if not dataset_id:
            dataset_id = self.resolve_dataset_id(dataset_name, timeout=timeout)
        params = urllib.parse.urlencode(
            [
                ("dataset", dataset_id),
                ("pipeline", "add_pipeline"),
                ("pipeline", "cognify_pipeline"),
            ]
        )
        return self.get_json(f"/api/v1/datasets/status?{params}", timeout=timeout)

    def _request_json(self, path_or_url: str, payload: dict, *, timeout: float, method: str) -> object:
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            self._url(path_or_url),
            data=body,
            headers=_headers({"Content-Type": "application/json"}),
            method=method,
        )
        return self._read_json(request, timeout=timeout)

    def _read_json(self, request: urllib.request.Request, *, timeout: float) -> object:
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise CogneeApiError(f"{exc.code} {exc.reason}: {detail}") from exc
        except (urllib.error.URLError, socket.timeout, ConnectionResetError) as exc:
            reason = getattr(exc, "reason", exc)
            raise CogneeApiError(f"Cognee API unavailable: {reason}", transient=True) from exc
        if not raw:
            return {}
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"raw": raw}

    def _url(self, path_or_url: str) -> str:
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            return path_or_url
        if not path_or_url.startswith("/"):
            path_or_url = "/" + path_or_url
        return self.base_url + path_or_url


def _headers(extra: dict[str, str]) -> dict[str, str]:
    headers = {"Accept": "application/json"}
    api_key = os.environ.get("COGNEE_API_KEY")
    if api_key:
        headers["X-Api-Key"] = api_key
    headers.update(extra)
    return headers


def _multipart_body(
    boundary: str,
    fields: dict[str, str],
    files: Sequence[Tuple[str, Path]],
) -> bytes:
    parts: List[bytes] = []
    for key, value in fields.items():
        parts.append(f"--{boundary}\r\n".encode("utf-8"))
        parts.append(f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode("utf-8"))
        parts.append(str(value).encode("utf-8"))
        parts.append(b"\r\n")
    for field_name, path in files:
        filename = path.name
        parts.append(f"--{boundary}\r\n".encode("utf-8"))
        parts.append(
            (
                f'Content-Disposition: form-data; name="{field_name}"; '
                f'filename="{filename}"\r\n'
                "Content-Type: text/markdown\r\n\r\n"
            ).encode("utf-8")
        )
        parts.append(path.read_bytes())
        parts.append(b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode("utf-8"))
    return b"".join(parts)

