# Deploy Runbook

## Prerequisites

- Docker Engine with Compose plugin.
- DNS records set for portfolio, api, demo, and spam hosts.

## Deploy base stack

```bash
cp .env.example .env
docker compose -f docker-compose.base.yml up -d --build
```

## Deploy demo stack

```bash
docker compose -f docker-compose.base.yml -f docker-compose.demos.yml up -d --build
```

## Optional heavy profile

```bash
docker compose -f docker-compose.heavy.yml --profile heavy up -d
```

## Health checks

```bash
curl -s http://localhost/healthz
docker compose -f docker-compose.base.yml ps
```
