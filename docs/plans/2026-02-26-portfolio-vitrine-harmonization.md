# Portfolio Vitrine Harmonization Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a harmonized portfolio platform with shared infrastructure and enforced hexagonal architecture.

**Architecture:** Shared base stack (proxy, web, api), demo stack (streamlit + nlp api), and optional heavy stack. Metadata and runtime mode semantics come from one normalized project catalog.

**Tech Stack:** Docker Compose, Python, Streamlit, Nginx, Traefik.

---

## Executed tasks

1. Scaffolded repository and smoke checks.
2. Added compose split for `base`, `demos`, `heavy`.
3. Implemented hexagonal `portfolio-api` (domain/application/adapters/composition_root).
4. Added normalized project catalog with runtime mode and skills metadata.
5. Built consolidated Streamlit showcase.
6. Added static web vitrine consuming API metadata.
7. Integrated always-on NLP spam demo route.
8. Added architecture boundary checker + CI workflow.
9. Added resource budgets and service limit checks.
10. Added deploy and rollback runbooks.
