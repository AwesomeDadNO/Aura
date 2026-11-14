# AURA

Launch strategy and an early website for the AURA ecosystem. **Applications are not distributed by this repository.** Product descriptions are planned direction, not verified implementation claims.

- [Norwegian / English launch strategy](roadmap.md)
- [Website source](website/)
- [Nordic Orbit test page](website/nordic-orbit/) — the selected light Nordic / orbital concept, with a dark mode using `#1a1d24`.

## Preview

No installation or build is needed. From the repository root:

```sh
python3 -m http.server 8080 --directory website
```

Open http://localhost:8080. The new test page is at http://localhost:8080/nordic-orbit/. You can also open `website/index.html` directly. Stop the server with Ctrl-C.

## Checks

```sh
python3 scripts/check_site.py
python3 scripts/check_nordic_orbit.py
node --check website/nordic-orbit/theme.js
```

The dependency-free check validates HTML structure, local asset/fragment links and forbidden placeholder/form/script constructs. Responsive layout should also be inspected in a browser at phone, tablet and desktop sizes. This check is not a full accessibility audit.

## Deploy when ready

This branch does not enable deployment or change GitHub Pages settings. The publish directory is **`website/`** and no build command is required. Upload those files to a static host, or configure GitHub Pages with a workflow that uploads `website/` using the official Pages actions after reviewing it. GitHub Pages' branch-folder option does not directly select arbitrary `website/` folders; use an artifact workflow or a separately prepared publishing branch.

Before deployment choose the domain and hosting log policy, review public claims and test all links. The strategy link on the page currently points to the dedicated development branch; update it if the branch is renamed or removed. A host's access logs are separate from this site's lack of analytics.

## Status and scope

The repository was empty with `main` configured as default. A single empty initialization commit establishes the PR base; strategy and website changes live on `feat/aura-launch-website`. No application releases, working downloads, waitlist, provider partnerships or security audits are claimed. No third-party fonts, remote media requests or analytics are included. The Nordic Orbit test page includes a small local theme script; its optional `aura-theme` preference stays in browser storage. It follows the system theme until a visitor chooses a mode. The interface illustration is explicitly labeled as a concept.

## Reliable preview from any folder

Use an absolute publish-directory path to avoid a 404 when starting from a different folder:

```sh
python3 -m http.server 8081 --bind 127.0.0.1 --directory /Users/awesomedad/Documents/ChatGPT/AuraOS/website
```

On this checkout, open http://127.0.0.1:8081/nordic-orbit/. On another computer substitute its checkout path. Deployment still publishes the whole `website/` directory; the test page is served at `/nordic-orbit/`. Its AI-generated transparent illustration is a concept; the real text, navigation, product sections and controls are HTML. No app interface functionality is implied.
