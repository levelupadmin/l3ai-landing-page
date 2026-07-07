# L3AI — The LevelUp AI Builder Cohort · Landing Page

Static single-file site: open `index.html`. No build step, no dependencies — fonts load from Google Fonts (Instrument Serif, Geist, Geist Mono, VT323).

## Design system
Ripped from odyssey.ml (see `l3ai_style_reference.md`): dark #090909 canvas, ink #E8EFEA, electric blue #0054FF (+#4D8AFF text-on-dark, #0044D4 text-on-light), 2px radii, pixel-font eyebrows/CTAs, serif display, film grain overlay, light "breather" bands on The Stack/Who/Loop/Depth/Investment.

## Key assets
- `l3ai_hero_orbit_v3.mp4` — hero video (Seedance 2.0, 4:3 1080p 6s, logos orbiting w/ comet trails). Embedded full-bleed, 16:9 crop, object-position center 20%.
- `girlsitting_v2.png` — hero still (Kevin's Photoshop cutout, +20% contrast). Currently unused after video swap; keep for fallback/poster.
- `l3ai_ladder_steps.png` — leverage-ladder scene (labels are HTML overlays, % positioned).
- `levelup-logo-white-trimmed.png` / `-black-trimmed.png` — recolored from brand avif.
- `tools section/_web/` — 46 tool logos, black marks auto-inverted to white for dark bg (originals in `tools section/`). `tool-logos/` = the 11-logo set used for the video reference sheet.
- `l3ai_hero_prompts.md` — locked generation prompts + settings; `L3AI Content.pdf` — canonical copy source.

## Open items
- Mentor names/photos (5 TBA placeholders), cohort dates, community stats to confirm before publish.
- "Request Invite" buttons → application form URL (currently #apply anchor).
- Possible accent recolor (blues may change; all tokenized in `:root`).
- Optional: regen hero video 16:9 with top headroom for true full-screen cover.
