# Portfolio Vitrine Platform

Unified platform to showcase data projects on a constrained VPS.

## Profiles

- `base`: edge, web, api, and shared state services.
- `demos`: lightweight interactive demos.
- `heavy`: optional heavy data stacks for temporary sessions.

## Hexagonal architecture

Hexagonal architecture is enforced in active runtime services.

- Import direction is checked by `tools/architecture/check_hexagonal_boundaries.py`.
- CI runs the same guard on every push and pull request.
