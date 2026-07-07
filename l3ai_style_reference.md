# L3AI Landing Page — Style Reference (ripped from odyssey.ml)

Source studied: https://odyssey.ml/ (Framer site, inspected live DOM + computed styles, 6 Jul 2026)
Rule: steal the style, not the structure. One change — invert black↔white. Blues stay (may be recolored later).

---

## 1. Typefaces

| Role | Odyssey uses | What it is | For our build |
|---|---|---|---|
| Headings (all H1/H2/H3/card titles) | **"Oliveira Regular"** — custom woff2, single weight 400 | High-contrast editorial serif: hairline thins, sharp wedge serifs, tall ascenders, slightly condensed. Designed for large display sizes | Closest free match: **Instrument Serif** (Google Fonts, also single-weight display serif, same high-contrast editorial DNA). Premium match: **PP Editorial New** (Pangram Pangram). Their asset: framerusercontent.com/assets/z1nF5kn4SN6AdOt4oFPFPdHgkRQ.woff2 (unknown license — don't ship it, match it) |
| Eyebrows, labels, buttons, links | **"NeueBit Bold"** (700) | **PP NeueBit** — Pangram Pangram's pixel/bitmap font. THE signature quirk of the site: retro-terminal pixel type at small sizes against an elegant serif | License PP NeueBit Bold (cheap, trial available at pangrampangram.com). No good Google clone — Silkscreen/VT323 are noticeably worse. This font is worth buying |
| Body, nav, UI | **Geist** (300/400/500/700) | Vercel's free neo-grotesque sans | Free on Google Fonts / vercel.com/font. Use as-is |
| Terminal micro-UI chips | Fragment Mono / JetBrains Mono / IBM Plex Mono | Mono for "Generating… ETA: 50ms" HUD chips | JetBrains Mono (free) if we use the motif |
| Logo wordmark | (ignored per Kevin) | — | — |

## 2. Type scale (desktop, exact computed values)

| Element | Font | Size | Line-height | Letter-spacing | Notes |
|---|---|---|---|---|---|
| H1 / hero display | Oliveira 400 | 68px | 71.4px (1.05) | −2.04px (−3%) | Sentence case, never bold — the single weight IS the look |
| H2 / section heads | Oliveira 400 | 48px | 52.8px (1.10) | −0.96px (−2%) | |
| H3 / card titles | Oliveira 400 | 38px | 39.9px (1.05) | −0.76px (−2%) | |
| Eyebrow / kicker | NeueBit Bold | 20px | 14px (0.7!) | 0 | Blue #0054FF. Tight lh is intentional — pixel font sits small despite 20px size |
| Button label | NeueBit Bold | 20px | 14px | 0 | |
| Body | Geist 400 | 16px | 21.6px (1.35) | −0.32px (−2%) | 60% opacity ink |
| Nav / small | Geist 400 | 14px | 16.8px (1.2) | 0 | 50% opacity ink |

System logic: elegant serif carries all display sizes at a single regular weight; pixel font does every label/CTA; quiet grotesque does the reading. Tight negative tracking everywhere except the pixel font.

## 3. Palette — original (dark) → ours (inverted light)

| Token | Odyssey (dark) | L3AI (light) |
|---|---|---|
| Canvas | #090909 (near-black, not pure) | **#FFFFFF** |
| Display/heading ink | #E8EFEA (off-white, faint green cast — not pure white) | **#090909** (near-black, mirrors their not-pure canvas) |
| Body ink | rgba(232,239,234,0.60) | **rgba(9,9,9,0.60)** |
| Tertiary/nav ink | rgba(232,239,234,0.50) | **rgba(9,9,9,0.50)** |
| Accent (eyebrows, CTA fill, links) | **#0054FF** electric blue | **#0054FF — unchanged** (4.7:1 on white, passes AA for large/UI text) |
| Secondary link token | #9E9EFF periwinkle (Framer default, barely surfaces) | keep #9E9EFF only for hover tints if needed |
| Secondary button surface | #262626 dark grey | **#F0F0F0** light grey |
| Card/inset surface | #1A1A1A | **#F5F5F5** |
| Hairlines/dividers | rgba(255,255,255,~0.08) | **rgba(9,9,9,0.08)** |
| Terminal chip accents | #93FF35 green · #FF3535 red | keep as-is if HUD motif is used |
| CTA button | #0054FF fill · light label · **2px radius** · 8px/12px pad | identical, white label |

## 4. Style DNA to carry over (beyond tokens)

- Near-sharp corners: 2px radius on buttons — nothing pill-shaped, nothing over-rounded.
- Eyebrow → serif headline → 60%-ink body: every section opens with this exact stack.
- Pixel-font labels are the personality; use them for eyebrows, buttons, stat labels, "REQUEST INVITE".
- Hairline dividers + diagonal-hatch texture bands between sections (subtle, blueprint feel).
- Terminal/HUD chips (mono font, green/red states) for live-demo moments — maps well to our "build with AI" demos.
- Restraint: one serif weight, one accent color, lots of air. The drama comes from scale contrast (68px serif vs 14px sans), not weight or color variety.

## 5. Open items

- Blues may be recolored later (Kevin will confirm).
- Confirm heading font choice: Instrument Serif (free) vs PP Editorial New (paid) vs licensing the actual Oliveira if identifiable.
- Structure/wireframes: pending from Kevin — this doc covers style only.
