# Deploy Runbook

## Prerequisites

- Docker Engine with Compose plugin.
- DNS records set for `nilluv.com`, `www.nilluv.com`, and `*.nilluv.com`.
- GitHub Environment `production` with required secrets.

## Required GitHub Environment secrets

- `TAILSCALE_AUTHKEY`
- `VPS_HOST` (`prod-vps-3`)
- `VPS_USER` (`devops`)
- `GHCR_USERNAME`
- `GHCR_TOKEN`
- `PORTFOLIO_ENV_FILE` (multiline env file payload)

`prod-vps-3` must allow Tailscale SSH for the deploy principal.

## VPS bootstrap (one-time)

```bash
ssh devops@prod-vps-3
sudo mkdir -p /opt/portfolio/{compose,env,data,logs}
sudo chown -R devops:devops /opt/portfolio
```

## Manual deploy (fallback)

```bash
cp .env.example .env
docker compose \
  -f docker-compose.base.yml \
  -f docker-compose.demos.yml \
  -f docker-compose.projects.yml \
  up -d --build
```

## CI deploy (recommended)

Run the **Deploy Production** workflow in GitHub Actions. The workflow will:

1. Join Tailscale.
2. Sync this repository to `/opt/portfolio/compose`.
3. Write `/opt/portfolio/env/.env` from `PORTFOLIO_ENV_FILE`.
4. Pull GHCR images and restart the stack.
5. Run remote smoke checks.

## Optional heavy profile

```bash
docker compose -f docker-compose.heavy.yml --profile heavy up -d
```

## Health checks

```bash
docker compose -f docker-compose.base.yml -f docker-compose.demos.yml -f docker-compose.projects.yml ps
curl -sk --resolve nilluv.com:443:127.0.0.1 https://nilluv.com
curl -sk --resolve api.nilluv.com:443:127.0.0.1 https://api.nilluv.com/healthz
```

## Cache behavior verification

- `portfolio-api` responds to `/projects` with `Cache-Control: public, max-age=120, s-maxage=120, stale-while-revalidate=300`.
- `healthz` and non-catalog responses are marked `Cache-Control: no-store`.

```bash
curl -skI --resolve api.nilluv.com:443:127.0.0.1 https://api.nilluv.com/projects | grep -i cache-control
curl -skI --resolve api.nilluv.com:443:127.0.0.1 https://api.nilluv.com/healthz | grep -i cache-control
```
