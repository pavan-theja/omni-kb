# Repository Bootstrap, Gitignore, and LFS Plan

Date captured: 2026-05-29

This note records the proposed first-pass plan for turning this workspace into a Git repository and pushing it safely.

## Current State

- The workspace is not currently initialized as a Git repository.
- Total workspace size is approximately 4.2 GB.
- Large local/generated areas observed:
  - `.venv/`: about 487 MB
  - `cognee/runtime/`: about 1.9 GB
  - `raw/saved_stage/`: about 1.2 GB
- Local graph/vector DB artifacts were removed after choosing Cognee-only retrieval.
- `git lfs` is not installed in the current shell.
- Local secret/config files exist, including:
  - `cognee/.env`
  - `cognee/.env.vertex`
  - `cognee/.env.vertex.gemini35`
  - runtime `cognee.env` files

## Recommended Repository Shape

Use a lean, reproducible source repository.

Commit:

- Source code under `src/`
- Tests under `tests/`
- Project documentation under `docs/`
- Runtime orchestration scripts and examples under `cognee/` and `services/`
- Authored source KB files under `raw/Source/cleaned/`
- Canonical review artifacts that are intended to be versioned, such as `canonical/*.jsonl` and manifests

Do not commit:

- Local Python virtual environments
- Local runtime databases
- Vector stores
- SQLite write-ahead/shm files
- Local Cognee runtime state
- Local graph/vector retrieval state
- Generated export caches unless explicitly treated as deliverables
- Local env files or credentials

## Gitignore Updates

Keep the existing `.gitignore` rules and add coverage for these categories.

General local files:

```gitignore
.DS_Store
.vscode/
.idea/
```

Python/cache artifacts:

```gitignore
.ruff_cache/
.mypy_cache/
.coverage
htmlcov/
```

Secrets and local env files:

```gitignore
**/.env
**/.env.*
!**/.env.example
**/cognee.env
**/current_runtime.env
**/*credentials*.json
**/*service-account*.json
*.pem
*.key
```

Runtime and local database state:

```gitignore
cognee/runtime/*
!cognee/runtime/README.md
raw/saved_stage/*
!raw/saved_stage/README.md
.chromadb_data/
```

Generated exports and debug outputs:

```gitignore
cognee/export/*
!cognee/export/README.md
cognee/shaped_export/*
!cognee/shaped_export/README.md
cognee/custom_shaped_export/*
!cognee/custom_shaped_export/README.md
cognee/bundled_export/*
!cognee/bundled_export/README.md
cognee/query_outputs/*
!cognee/query_outputs/README.md
build/chunks/*
!build/chunks/README.md
build/intermediate/*
!build/intermediate/README.md
```

Open decision:

```gitignore
# Decide whether these are committed benchmark artifacts or local generated output.
# build/gemini*/
```

## LFS Decision

Decision: do not use Git LFS for this repository for now.

Recommended first push:

- Avoid committing binary/prebuilt runtime artifacts.
- Keep large but reviewable text artifacts in normal Git only if they are truly canonical outputs.
- Ignore DB/vector artifacts rather than storing them in LFS.
- Remove local-only graph/vector stores when the project standardizes on Cognee.
- Keep ignored runtime/output directories visible with lightweight `README.md` placeholders.

If we later decide that binary artifacts must be versioned, revisit storage first rather than adding them directly to Git history. Git LFS can still be considered later, but it is not part of the current bootstrap plan.

Reference LFS patterns that would apply only if the decision changes:

```gitattributes
*.sqlite filter=lfs diff=lfs merge=lfs -text
*.sqlite-wal filter=lfs diff=lfs merge=lfs -text
*.sqlite-shm filter=lfs diff=lfs merge=lfs -text
*.lance filter=lfs diff=lfs merge=lfs -text
*.parquet filter=lfs diff=lfs merge=lfs -text
*.arrow filter=lfs diff=lfs merge=lfs -text
*.feather filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs diff=lfs merge=lfs -text
*.tar filter=lfs diff=lfs merge=lfs -text
*.tar.gz filter=lfs diff=lfs merge=lfs -text
```

Potential large text artifacts observed:

- `canonical/edges.jsonl`: about 34 MB
- `canonical/cards.jsonl`: about 17 MB
- `processed_kb_docs/cleaned/edges.jsonl`: about 27 MB
- `processed_kb_docs/cleaned/cards.jsonl`: about 13 MB
- `cognee/bundled_export/documents/canonical_all.md`: about 11 MB

These are below common single-file hard limits, but they can still make repo history heavy. Prefer committing only the canonical text artifacts that are useful for review or reproducibility.

## Execution Checklist

1. Finalize the `build/gemini*` decision.
2. Update `.gitignore`.
3. Do not add `.gitattributes` for Git LFS.
4. Run a secret/file safety check before staging.
5. Initialize the repo:

   ```bash
   git init -b main
   ```

6. Stage files:

   ```bash
   git add .
   ```

7. Review staged files:

   ```bash
   git status --short
   git diff --cached --stat
   ```

8. Commit:

   ```bash
   git commit -m "Initial commit"
   ```

9. Push to a remote after choosing:
   - Repository owner/org
   - Repository name
   - Public or private visibility

Possible GitHub CLI flow, if authenticated:

```bash
gh repo create <owner-or-user>/<repo-name> --private --source=. --remote=origin --push
```

Possible existing remote flow:

```bash
git remote add origin <repo-url>
git push -u origin main
```

## Pending Decisions

- Should `build/gemini*` benchmark/report outputs be committed, ignored, or selectively curated?
- Should `raw/archive/` be committed as historical source material or ignored as local archive state?
- Should `cognee/export/` and other generated exports remain fully ignored, or should selected manifests/results be committed?
- Git LFS is intentionally deferred. Binary/runtime artifacts should stay ignored.
