# Editorial Portfolio Landing (SvelteKit + Edge Prefetch) Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the static portfolio web with a modern editorial-premium SvelteKit landing page that server-loads projects from `portfolio-api`.

**Architecture:** Keep `services/portfolio-api` as the metadata source (`data/projects/projects.json` -> `/projects`). Build `services/portfolio-web` as an SSR SvelteKit app. Keep existing edge/proxy and add short-lived cache policy for project catalog responses.

**Tech Stack:** SvelteKit, Vite, TypeScript, Docker Compose, Python unittest smoke checks.

---

### Task 1: Bootstrap SvelteKit web service

**Files:**
- Create: `services/portfolio-web/package.json`
- Create: `services/portfolio-web/svelte.config.js`
- Create: `services/portfolio-web/vite.config.ts`
- Create: `services/portfolio-web/tsconfig.json`
- Create: `services/portfolio-web/src/*`
- Modify: `services/portfolio-web/tests/test_card_rendering.py`
- Delete: legacy static assets (`index.html`, `assets/styles.css`, `assets/app.js`)

**Steps:**
1. Write failing test for SvelteKit scaffold files.
2. Run targeted unittest and confirm failure.
3. Add minimal SvelteKit app files.
4. Re-run test and confirm pass.

### Task 2: Implement server-side API loading

**Files:**
- Modify: `services/portfolio-web/src/routes/+page.server.ts`
- Create/Modify: `services/portfolio-web/src/lib/config.ts`, `services/portfolio-web/src/lib/types.ts`
- Modify: `services/portfolio-web/tests/test_card_rendering.py`

**Steps:**
1. Write failing test asserting `/projects` loader and API base config usage.
2. Run targeted unittest and confirm failure.
3. Implement SSR loader with fallback error contract.
4. Re-run test and confirm pass.

### Task 3: Build editorial-premium landing UI

**Files:**
- Modify: `services/portfolio-web/src/routes/+layout.svelte`
- Modify: `services/portfolio-web/src/routes/+page.svelte`
- Create: `services/portfolio-web/src/lib/components/*.svelte`
- Create: `services/portfolio-web/src/lib/styles/theme.css`
- Modify: `services/portfolio-web/tests/test_card_rendering.py`

**Steps:**
1. Write failing test for required sections and interaction affordances.
2. Run targeted unittest and confirm failure.
3. Implement hero, trust strip, featured projects, project grid, filters, modal.
4. Implement responsive styling, motion, reduced-motion handling.
5. Re-run test and confirm pass.

### Task 4: Wire container + compose runtime

**Files:**
- Create: `services/portfolio-web/Dockerfile`
- Modify: `docker-compose.base.yml`
- Modify: `.env.example`
- Modify: `README.md`
- Create/Modify: `tests/smoke/test_web_service_wiring.py`

**Steps:**
1. Write failing smoke test for web service compose wiring.
2. Run test and confirm failure.
3. Add Dockerfile and compose env wiring for `PORTFOLIO_API_BASE`.
4. Re-run smoke test and confirm pass.

### Task 5: Add edge caching for project catalog

**Files:**
- Modify: edge proxy config files used by current deployment.
- Modify: `docs/ops/deploy-runbook.md`
- Modify: `docs/ops/rollback-runbook.md`
- Add/Modify tests for cache policy presence.

**Steps:**
1. Write failing check for cache directives.
2. Add short TTL caching policy for `/projects`.
3. Ensure health checks and fallback routes unaffected.
4. Re-run checks and confirm pass.

### Task 6: Verify end-to-end behavior

**Files:**
- Modify: `README.md`
- Optional: `docs/ops/perf-checklist.md`

**Steps:**
1. Run unit/smoke suites.
2. Run compose config validation.
3. Build and run base stack for manual checks.
4. Verify desktop/mobile layout, filters, modal keyboard flow, and API outage fallback.
