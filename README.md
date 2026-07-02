# Kingdom Hearts 1FM AP Randomizer Website

Source for [kh1fmrando.com](https://kh1fmrando.com), the site for the Kingdom Hearts: Final Mix Archipelago Randomizer — a branch of the original KH1 randomizer that adds full Archipelago multiworld support, fully randomizable items (worlds, spells, trinities, summons, stat ups), GUI-based seed/mod generation with OpenKH integration, and a number of other features and stability fixes.

Plain static HTML/CSS, no build step. `header.html` is fetched and injected client-side on every page to keep navigation and page titles in one place.

## Structure

- World/topic pages (`agrabah.html`, `traverse_town.html`, etc.) — guides for each location
- `generate_a_seed.html` / `generating_a_seed.html` — seed generation instructions
- `setup_guide.html`, `software_setup.html`, `installing_the_mod.html` — getting started guides
- `locations_guide.html`, `videolocationsguide.html` — check location references
- `multiworld_guide.html` — Archipelago multiworld instructions
- `tracker/` — location/item tracker
- `header.html` — shared header/nav, loaded by every page via `fetch()`
- `style.css` — shared styling
- `images/` — site and guide assets

## Hosting

Served via GitHub Pages with a custom domain (`CNAME` file). Pushing to `main` deploys directly — no CI step.

## Dev site

Staging/in-progress changes live in a separate repo, [Kingdom-Hearts-1FM-AP-Randomizer-Website-Dev](https://github.com/gaithern/Kingdom-Hearts-1FM-AP-Randomizer-Website-Dev), served at [dev.kh1fmrando.com](https://dev.kh1fmrando.com). It used to be a `dev/` subfolder of this repo but was split out so it could get its own subdomain (GitHub Pages only supports one custom domain per repo).
