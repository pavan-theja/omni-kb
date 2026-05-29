FROM cognee/cognee:main

USER root

ENV PYTHONPATH=/app/provider-site-packages

RUN set -eux; \
    mkdir -p /app/provider-site-packages; \
    pip install --no-cache-dir --upgrade --target /app/provider-site-packages \
        anthropic \
        boto3 \
        google-auth \
        google-cloud-aiplatform \
        google-generativeai \
        mistralai \
        "neo4j>=5.28,<6" \
        openai \
        "qdrant-client>=1.16"; \
    pip install --no-cache-dir --upgrade --no-deps --target /app/provider-site-packages \
        "cognee-community-vector-adapter-qdrant==0.2.4"; \
    printf '%s\n' \
        'try:' \
        '    from cognee_community_vector_adapter_qdrant import register  # noqa: F401' \
        'except Exception:' \
        '    pass' \
        > /app/provider-site-packages/sitecustomize.py
