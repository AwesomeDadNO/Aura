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
