# Validation — 14 November 2026

## Scope

Repository initially had no refs or files. GitHub reports `main` as default. An empty root commit provides the PR base. Website and strategy are exclusively on `feat/aura-launch-website`; no merge or deployment performed.

## Checks completed

- `python3 scripts/check_site.py`: balanced HTML, duplicate-ID check, local assets and section anchors, approved HTTPS destinations, no forms/scripts/iframes, responsive/reduced-motion/focus styling hooks.
- Local HTTP response: 200 for the landing page.
- Browser visual inspection: desktop hero at 1280px, mobile hero and product navigation at 390px, tablet product/privacy sections at 768px.
- DOM width checks at 320, 390, 768 and 1280px: document width equals viewport width after fixing decorative halo overflow.
- Product anchor navigation verified in browser (`#products`).
- Content review: all six product/capability roles, optional sync, third-party data caveats, unverified integrations, release gates and honest calls to action are covered.
- No external images, fonts, scripts, telemetry or collection endpoints.

## Limits

No app code exists here to test or certify. No full accessibility audit, device-lab testing, provider API validation or security audit has been performed. No framework build is required for this static site. Public downloads, beta registration and deployment remain intentionally absent. Check hosting logs/privacy separately when selecting a host.

## Nordic Orbit test page

Added at `website/nordic-orbit/`, preserving the original landing page. Browser checks: light/dark switching, persistence after reload in both modes, exact dark body background `rgb(26, 29, 36)` (`#1a1d24`), hero image loads, ecosystem anchor navigation. No horizontal overflow at 320, 390, 768 or 1440px. Visual checks covered mobile light mode and desktop light/dark mode. Viewport override reset after testing. Theme script has no network calls and safely tolerates unavailable storage. System theme changes apply until a manual preference is selected. The hero is an AI-generated concept with transparency, stored in this repository.

## Nordic Living hero revision

Replaced the active orbital hero with new AI-generated photographs of the same cozy Nordic living room in daytime and evening. Generic AURA concept controls replace third-party provider branding. The theme determines which image is visible, including a CSS system-theme fallback. The original orbital asset is retained for design history, but is not referenced by the page.

Verified both images load (1774px natural width), only the correct image is displayed for each theme, and dark background remains `rgb(26, 29, 36)`. Visually inspected the evening hero on desktop and daytime crop at 390px; TV, tablet and phone remain visible. No horizontal overflow at 320, 390 or 1440px. Local HTML/assets/anchor check and JavaScript syntax check passed. Viewport override reset after testing.
