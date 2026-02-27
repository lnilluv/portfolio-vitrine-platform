# Portfolio Vitrine Platform

Unified platform to showcase data projects on a constrained VPS.

## Profiles

- `base`: edge, web, api, and shared state services.
- `demos`: lightweight interactive demos.
- `projects`: externally built project images routed through the shared edge.
- `heavy`: optional heavy data stacks for temporary sessions.

## Production topology

- Apex landing page: `nilluv.com`
- Shared API endpoint: `api.nilluv.com`
- Project subdomains: `<project>.nilluv.com`
- Single Traefik ingress owns ports `80/443`
- Runtime stack file set: `docker-compose.base.yml`, `docker-compose.demos.yml`, `docker-compose.projects.yml`

## Deployment

- Build and push images to GHCR per repository.
- Deploy from GitHub Actions over Tailscale SSH to `devops@prod-vps-3`.
- Runtime env file is injected from GitHub Environment secrets into `/opt/portfolio/env/.env`.

## Hexagonal architecture

Hexagonal architecture is enforced in active runtime services.

- Import direction is checked by `tools/architecture/check_hexagonal_boundaries.py`.
- CI runs the same guard on every push and pull request.
