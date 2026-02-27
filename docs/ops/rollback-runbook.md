# Rollback Runbook

## Rollback latest deployment

1. Identify previous known-good image tags.
2. Pin image tags in compose files.
3. Redeploy pinned version.

```bash
docker compose -f docker-compose.base.yml -f docker-compose.demos.yml -f docker-compose.projects.yml down
docker compose -f docker-compose.base.yml -f docker-compose.demos.yml -f docker-compose.projects.yml up -d
```

## Emergency fallback

If demo services consume too much memory, stop demo profile and keep core online:

```bash
docker compose -f docker-compose.base.yml -f docker-compose.demos.yml stop showcase-streamlit nlp-spam-api
```

If project services are causing pressure, stop non-core viewers first:

```bash
docker compose -f docker-compose.base.yml -f docker-compose.projects.yml stop brainsight getaround
```

## Cache policy rollback

If catalog updates appear delayed, temporarily disable cacheability on `/projects` by rolling back `services/portfolio-api/src/portfolio_api/adapters/http/server.py` to a known-good commit and redeploying base stack.
