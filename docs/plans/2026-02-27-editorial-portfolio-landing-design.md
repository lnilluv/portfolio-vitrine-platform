# Editorial Portfolio Landing Design

## Context

- Replace the current static web vitrine with a modern portfolio landing page.
- Keep VPS-friendly architecture and existing `portfolio-api` as source of truth.
- Prioritize conversion toward project exploration.

## Product Decisions

- Visual direction: editorial premium.
- Primary action: `View Projects`.
- Hero style: name + value proposition.
- Framework: SvelteKit.
- Data source: existing `/projects` API.

## Selected Architecture (Approach B)

- Build a SvelteKit SSR frontend in `services/portfolio-web`.
- Server-load project metadata from `portfolio-api` (`/projects`) at request time.
- Add edge cache policy for the project catalog endpoint (short TTL) to reduce API pressure.
- Keep graceful fallback when catalog loading fails.

## Information Architecture

- Hero section with value proposition and CTA.
- Trust strip with domains and toolchain highlights.
- Featured projects section for top 3 entries.
- Full filterable project grid using runtime mode + skills.
- Project detail drawer/modal for quick exploration.
- Footer with contact links and availability statement.

## Visual System

- Typography pairing: expressive serif for headings + clean sans for body.
- Color direction: warm neutral base, deep ink text, emerald/teal interaction accent.
- Background depth: gradient layers and subtle texture details.
- Card style: refined borders/shadows and strong hierarchy.
- Motion: staggered reveals, meaningful hover/focus transitions.

## UX and Accessibility

- Mobile-first responsive layout.
- Keyboard-accessible controls and dialog behavior.
- Visible focus indicators and AA contrast targets.
- `prefers-reduced-motion` support.

## Deployment Notes

- Keep compose profile split (`base`, `demos`, `heavy`).
- Replace web service internals only; preserve API contracts.
- Route SvelteKit through existing edge proxy and enable cache for `/projects`.
