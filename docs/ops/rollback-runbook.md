# Rollback Runbook

## Rollback latest deployment

1. Identify previous known-good image tags.
2. Pin image tags in compose files.
3. Redeploy pinned version.

```bash
docker compose -f docker-compose.base.yml down
docker compose -f docker-compose.base.yml up -d
```

## Emergency fallback

If demo services consume too much memory, stop demo profile and keep core online:

```bash
docker compose -f docker-compose.base.yml -f docker-compose.demos.yml stop showcase-streamlit nlp-spam-api
```
