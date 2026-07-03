# Photoreal Stack — The Locked Hyperreal Block

The closing paragraph that ships at the end of every still prompt. Bakes in skin texture, hair detail, fabric weave, lens character, film grain, and color grade — the texture-and-realism foundation that separates "photograph" from "AI render."

For pure environment plates (no humans), drop the skin/hair lines and keep light/lens/grain/grade.

---

## STACK v3 — DEFAULT (HUMANS IN FRAME)

```
Hyperrealistic photography. Real human skin texture with visible pores, subtle
subsurface scattering on the cheeks, nose bridge, and ears, fine peach fuzz
catching light along the jawline and cheekbones, slight skin imperfections —
natural unevenness, not retouched. Hair rendered strand by strand with realistic
flyaways, baby hairs at the hairline, individual strands catching light, light
transmission through the hair ends, natural texture and movement. Fabric
rendered with real weave detail, real weight, real drape, visible texture
variation across the surface. Eyes with real reflection, real moisture, real
depth in the iris. Jewelry with real metal surface detail and tarnish or polish
appropriate to the piece. Kodak Vision3 500T film emulation, visible fine film
grain, subtle chromatic aberration at the edges of the frame, soft lens vignette,
cinematic color grade with warm mid-tones and slightly cooled shadows. Lived-in,
not pristine. Photographic, not rendered.
```

**Shorthand reference:** `(use locked photoreal stack v3)` — only safe to use when the prompt is already long and the user has accepted a stack reference instead of the full inline block. Most models do not resolve this shorthand on their own; default to inlining the full block.

---

## STACK v3-ENV — ENVIRONMENT PLATE (NO HUMANS)

```
Hyperrealistic photography. Fabric rendered with real weave detail, real weight,
real drape, visible texture variation across the surface. Surface materials with
real wear patterns, oxidization, dust accumulation, moisture stains where
appropriate. Glass with real reflection and refraction, signage with real
substrate texture, neon with real bloom and color bleed onto adjacent surfaces.
Kodak Vision3 500T film emulation, visible fine film grain, subtle chromatic
aberration at the edges of the frame, soft lens vignette, cinematic color grade
with warm mid-tones and slightly cooled shadows. Atmospheric dust suspended in
directional light beams. Lived-in, not pristine. Photographic, not rendered. No
humans, no silhouettes, no living beings.
```

---

## STACK v3-FACE — TIGHT PORTRAIT / FACE DETAIL

Use when the shot is face-fills-frame (chest-up, shoulders-up, eye macro). Stack v3 plus this extension:

```
Extreme face fidelity. Real skin texture with visible pores, fine peach fuzz
catching light along the jawline and upper lip, subtle subsurface scattering on
the nose bridge cheeks and ears, micro-expression detail in the eyes and mouth
corners, individual lash detail, real moisture and reflection in the iris with
visible iris pattern, real lip texture with subtle natural lip lines, hair
rendered strand by strand at the hairline with visible baby hairs and flyaways,
fabric weave visible at the collar and shoulder.
```

---

## WHEN TO USE WHICH

| Shot type | Stack |
|---|---|
| Single still, full body, character on white seamless | v3 |
| 6-panel character sheet | v3 |
| 3x3 / 9-angle contact sheet | v3 |
| Wide / medium scene plate with cast | v3 |
| Tight portrait / chest-up / eye macro | v3 + v3-FACE extension |
| 2x2 empty location plate | v3-ENV |
| Pure environment establishing shot | v3-ENV |
| Atmospheric plate (M5 Atmospheric) | v3-ENV |
| Video — single shot or sequence | v3 or v3-ENV (matching cast presence) — closes the static description block |

---

## STACK CUSTOMIZATION

Custom style tokens (`<STYLE-XXX>`) can override parts of the stack. The order of precedence:

1. Style token's full technical lock (if specified)
2. Cinema mode camera block (M1-M5)
3. Photoreal stack (default v3)

When a style token sets its own grain, halation, contrast, or palette, those override the stack defaults. The stack still provides the skin/hair/fabric/eye detail language — only the lens/grade/grain layer gets overridden.

---

## ANTI-PATTERNS

- **"Photorealistic" alone** — meaningless. Always include the texture detail language (pores, peach fuzz, strand-by-strand hair, fabric weave).
- **Multiple film stocks in one prompt** — pick one. Kodak Vision3 250D for daylight grounded, 500T for tungsten-mixed, 5219 for low-light scene. Don't stack two.
- **"4K" or "8K" in the prompt body** — resolution is an API parameter, not prompt content. Drop it.
- **"HDR" / "ray-traced"** — diffusion models don't render these terms meaningfully. Cut them.
- **"Award-winning" / "masterpiece" / "highly detailed"** — bait words. Cut them — the texture language is what produces detail.
- **Skipping the stack on grids** — every panel needs the stack. If the prompt gets too long, drop variants from the stack but keep the core skin/hair/fabric block.

---

## STACK VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| v1 | 2026-04 | Initial stack — pores, fabric, Kodak Vision3 500T |
| v2 | 2026-04 | Added subsurface scattering, peach fuzz, strand detail |
| **v3** | **2026-05 (current)** | Added eye moisture/depth, jewelry surface detail, chromatic aberration, vignette. Split into default / env / face variants. |

When updating the stack, bump the version and keep prior versions accessible — old projects may want their original look.
