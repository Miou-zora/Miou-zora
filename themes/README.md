# Themes

Alternative designs for the profile README. Each one carries the same content, so
only the presentation differs. Every asset ships as a light/dark pair under
`../assets/<theme>/`, served through `<picture>` so GitHub picks the variant that
matches the viewer's theme.

| Theme | File | Notes |
| :-- | :-- | :-- |
| **NieR: Automata** | [README.nier-automata.md](README.nier-automata.md) | Currently live as the profile README. Built on the yorha-css tokens: `#d1cdb7` field with a 5px grid, light uppercase title with a hard offset shadow, fat-bar plus thin-bar row markers, panels edged right and bottom only. |
| **Evangelion** | [README.evangelion.md](README.evangelion.md) | NERV-style title card. Drifting hazard band, cropped 創, blinking 起動中 chip, sections numbered as episodes. |
| **NieR Replicant** | [README.nier-replicant.md](README.nier-replicant.md) | No painted field at all: gold corner brackets, hairline rules and a breathing diamond over the page colour. |

To switch the live profile, copy a theme's file over `../README.md` and change the
asset paths from `../assets/` back to `assets/`.

The SVGs are generated rather than hand-edited one by one; palettes and templates
live in one script so the light and dark variants cannot drift apart.
