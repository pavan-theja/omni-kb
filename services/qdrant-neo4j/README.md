# Cognee External Services

Local production-like services for Cognee experiments:

- Postgres for Cognee relational state
- Qdrant for vector storage
- Neo4j for graph storage

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
cognee/runtime/external/postgres
cognee/runtime/external/qdrant
cognee/runtime/external/neo4j/data
cognee/runtime/external/neo4j/logs
```

Cognee should connect from inside its Docker container using Docker Desktop's host bridge:

```bash
DB_PROVIDER=postgres
DB_NAME=cognee_db
DB_HOST=host.docker.internal
DB_PORT=5432
DB_USERNAME=cognee
DB_PASSWORD=cognee

VECTOR_DB_PROVIDER=qdrant
VECTOR_DB_URL=http://host.docker.internal:6333
VECTOR_DB_KEY=

GRAPH_DATABASE_PROVIDER=neo4j
GRAPH_DATABASE_URL=bolt://host.docker.internal:7687
GRAPH_DATABASE_NAME=neo4j
GRAPH_DATABASE_USERNAME=neo4j
GRAPH_DATABASE_PASSWORD=pleaseletmein
```

The Cognee image also needs the Qdrant adapter plus Neo4j and Postgres client libraries before these backends can be used. The local Dockerfile installs them directly:

```text
cognee-community-vector-adapter-qdrant
neo4j
asyncpg
pgvector
psycopg2-binary
```
