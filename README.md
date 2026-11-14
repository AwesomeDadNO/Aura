# AURA

Launch strategy and an early website for the AURA ecosystem. **Applications are not distributed by this repository.** Product descriptions are planned direction, not verified implementation claims.

- [Norwegian / English launch strategy](roadmap.md)
- [Website source](website/)
- [Nordic Orbit test page](website/nordic-orbit/) — the selected Nordic concept, now featuring a cozy living-room hero, with a dark mode using `#1a1d24`.

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

## GitHub Pages

The `Publish AURA website` workflow publishes on pushes to `main`. `python3 scripts/build_pages.py` stages the selected Nordic Living design at `_site/index.html`, so the public homepage is https://awesomedadno.github.io/Aura/.

The build retains previous URLs under `/Aura/website/`, including the original design and `/Aura/website/nordic-orbit/`. Root-page asset and original-design links are adjusted during staging. GitHub Pages must use **GitHub Actions** as its source. No framework dependencies are required. To preview the published layout locally:

```sh
python3 scripts/build_pages.py
python3 -m http.server 8082 --bind 127.0.0.1 --directory _site
```

Open http://127.0.0.1:8082/. `_site/` is generated and ignored by Git.

## Status and scope

The repository was empty with `main` configured as default. A single empty initialization commit establishes the PR base; strategy and website changes live on `feat/aura-launch-website`. No application releases, working downloads, waitlist, provider partnerships or security audits are claimed. No third-party fonts, remote media requests or analytics are included. The Nordic test page includes a small local theme script; its optional `aura-theme` preference stays in browser storage. It follows the system theme until a visitor chooses a mode. The interface illustration is explicitly labeled as a concept.

## Reliable preview from any folder

Use an absolute publish-directory path to avoid a 404 when starting from a different folder:

```sh
python3 -m http.server 8081 --bind 127.0.0.1 --directory /Users/awesomedad/Documents/ChatGPT/AuraOS/website
```

On this checkout, open http://127.0.0.1:8081/nordic-orbit/. On another computer substitute its checkout path. Local source preview serves the test page at `/nordic-orbit/`; the Pages workflow stages it at the public root. Its AI-generated home photographs and device interfaces are concepts; the real text, navigation, product sections and controls are HTML. No app interface functionality is implied.
