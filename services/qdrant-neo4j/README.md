# Qdrant + Neo4j Services

Local external services for Cognee experiments with Qdrant vectors and Neo4j graph storage.

Start from the repo root:

```bash
docker compose -f services/qdrant-neo4j/compose.yaml up -d
```

Stop:

```bash
docker compose -f services/qdrant-neo4j/compose.yaml down
```

Persisted data lives under:

```text
cognee/runtime/external/qdrant
cognee/runtime/external/neo4j/data
cognee/runtime/external/neo4j/logs
```

Cognee should connect from inside its Docker container using Docker Desktop's host bridge:

```bash
VECTOR_DB_PROVIDER=qdrant
VECTOR_DB_URL=http://host.docker.internal:6333
VECTOR_DB_KEY=

GRAPH_DATABASE_PROVIDER=neo4j
GRAPH_DATABASE_URL=bolt://host.docker.internal:7687
GRAPH_DATABASE_NAME=neo4j
GRAPH_DATABASE_USERNAME=neo4j
GRAPH_DATABASE_PASSWORD=pleaseletmein
```

The Cognee image also needs the Qdrant adapter and Neo4j extra installed before these backends can be used:

```text
cognee-community-vector-adapter-qdrant
cognee[neo4j]
```
