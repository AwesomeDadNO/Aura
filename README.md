# AURA

Launch strategy and an early website for the AURA ecosystem. **Applications are not distributed by this repository.** Product descriptions are planned direction, not verified implementation claims.

- [Norwegian / English launch strategy](roadmap.md)
- [Website source](website/)

## Preview

No installation or build is needed. From the repository root:

```sh
python3 -m http.server 8080 --directory website
```

Open http://localhost:8080. You can also open `website/index.html` directly. Stop the server with Ctrl-C.

## Checks

```sh
python3 scripts/check_site.py
```

The dependency-free check validates HTML structure, local asset/fragment links and forbidden placeholder/form/script constructs. Responsive layout should also be inspected in a browser at phone, tablet and desktop sizes. This check is not a full accessibility audit.

## Deploy when ready

This branch does not enable deployment or change GitHub Pages settings. The publish directory is **`website/`** and no build command is required. Upload those files to a static host, or configure GitHub Pages with a workflow that uploads `website/` using the official Pages actions after reviewing it. GitHub Pages' branch-folder option does not directly select arbitrary `website/` folders; use an artifact workflow or a separately prepared publishing branch.

Before deployment choose the domain and hosting log policy, review public claims and test all links. The strategy link on the page currently points to the dedicated development branch; update it if the branch is renamed or removed. A host's access logs are separate from this site's lack of analytics.

## Status and scope

The repository was empty with `main` configured as default. A single empty initialization commit establishes the PR base; strategy and website changes live on `feat/aura-launch-website`. No application releases, working downloads, waitlist, provider partnerships or security audits are claimed. No third-party fonts, JavaScript, media requests or analytics are included. The interface illustration is explicitly labeled as a concept.
