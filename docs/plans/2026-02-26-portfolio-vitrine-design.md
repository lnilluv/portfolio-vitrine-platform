# Portfolio Vitrine Design

## Constraints

- Host: 2 vCPU / 4 GB RAM VPS.
- Requirement: every project remains visible at all times.
- Rule: hexagonal architecture enforced for maintained runtime services.

## Selected approach

Use a shared platform with:

- one edge router,
- one web vitrine,
- one hexagonal metadata API,
- one consolidated Streamlit showcase,
- one always-on lightweight NLP demo API,
- optional heavy profiles for resource-intensive stacks.

## Runtime modes

- `live-interactive`: running endpoint available.
- `artifacts-interactive`: precomputed outputs rendered interactively.
- `static-case-study`: architecture and outcomes only.

## Why this design

- avoids duplicated infra containers across projects,
- keeps steady-state memory in budget,
- preserves narrative coverage for all projects,
- keeps heavy stacks available without exhausting VPS resources.
