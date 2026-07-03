# Camera Grammar — Five Cinema Modes (M1-M5)

Five canned camera languages. Pick by scene type, drop the camera block at the end of the prompt (before the photoreal stack). Each mode shares an ARRI body and either Panavision Ultra Vintage anamorphic or Cooke S4/i spherical glass — they differ in **movement, filtration, grade, palette, and texture**, not in body or lens family.

Works for both stills and video. The differences for video: movement gets described as continuous (handheld breath, shaky throughout, locked-off slow push), and runtime is baked into the camera block.

---

## MODE-SELECT TABLE

| Mode | Use when scene is... | Body | Lens | Movement | Filter | Grade |
|---|---|---|---|---|---|---|
| **M1 — Narrative** | Real-world dramatic — streets, kitchens, cars, bars, interior/exterior locations | Alexa 35 | Panavision Ultra Vintage anamorphic 40/55/75/100mm T2.3 | Handheld, slight breath, occasional slow dolly | Tiffen Black Pro-Mist 1/4 | Kodak 250D, 800 ASA, teal-amber split |
| **M2 — Studio / Editorial** | Studio, void, clean set, fashion film, editorial portrait, performance-on-set | Alexa Mini LF | Cooke S4/i spherical 32/50/75/100mm T2 | Locked + optional 4–6" slow push | Tiffen Black Pro-Mist 1/2 + Glimmerglass on chrome/rhinestone | Saturated editorial, warm-retained blacks, 400 ASA |
| **M3 — Action / Combat** | Combat, chase, stunts, war, debris, smoke, dust | Alexa 35 | Panavision Ultra Vintage anamorphic 40/55/75/100mm T2.3 | Handheld + shaky **throughout**, no stabilized shots | Tiffen Black Pro-Mist 1/4 | Kodak 250D, 800 ASA, dusty haze, gritty documentary-meets-cinema |
| **M4 — Performance / Concert** | Stadium, arena, stage, jumbotron, lightstick crowd, festival pit | Alexa 35 | Panavision Ultra Vintage anamorphic 40/55/75/100mm T2.3 | Mixed pit-photographer + shaky operator + orbital, hard cuts | Tiffen Black Pro-Mist 1/4 | Kodak 250D, desaturated cool + warm bloom, stage-light cast |
| **M5 — Atmospheric / Empty** | Abandoned environments, no-humans plates, landscapes, weather pieces | Alexa Mini LF | Panavision Ultra Vintage anamorphic 35→85mm T2.3 | Locked-off or extremely slow push-in / pull-back | Tiffen Black Pro-Mist 1/4 | Kodak 250D, 400 ASA, palette-driven (specify hex) |

---

## LENS LENGTH GUIDE (UNIVERSAL)

- **24/32/35/40mm** — Wide establishing, full-body, group framing, environmental context
- **50/55mm** — Medium portrait, two-shot, waist-up, dialogue framing
- **75mm** — Tight editorial portrait, single-character isolation, performance close-up
- **85/100mm** — Extreme close-up — eyes, lips, jewelry, fabric texture, surface detail

Default to 55mm (M1 / M3 / M4) or 50mm (M2) for medium framing. M5 typically uses the wider end (35→55mm) for environmental reach. For face macros and eye reflections, push to 100mm.

---

## FRAME RATE NOTES

All modes default to **24fps with 180° shutter** for cinema-standard motion blur.

For slow-motion beats in video (impact, hair whip, fabric on a hit, water splash, weapon recoil), add inline: `intercut a 96fps high-speed slow-motion frame at the [moment], holding shutter at 180 degrees for natural motion blur even in slow motion.` Keep this inside the camera block — don't change the base frame rate.

---

## MODE 1 — NARRATIVE (Real-World, Lived-In)

**Use when:** Real-world dramatic scenes. Streets, apartments, kitchens, cars, bars, diners, locker rooms, exterior locations, anywhere a person could plausibly walk into and shoot.

**Drop-in block** (paste at end of prompt, before photoreal stack — replace `[XX]` with lens length, `[YY]` with runtime if video):

```
Shot on ARRI Alexa 35 in ProRes 4444 LogC4, Panavision Ultra Vintage 2x
anamorphic [XX]mm at T2.3 with Tiffen Black Pro-Mist 1/4 filter, handheld
with natural breath and slight shake, photoreal cinematic grit with oval
bokeh and horizontal streak flares, warm anamorphic falloff toward frame
edges, Kodak Vision3 250D film emulation grade with slight halation on
highlights and 800 ASA grain structure, teal-amber color split with cool
teal-blue shadows and warm amber highlights, organic lens breathing on
focus racks, shallow depth of field, 24fps base shutter 180 degrees[, total
runtime roughly [YY] seconds].
```

---

## MODE 2 — STUDIO / EDITORIAL (Crafted, Not Photographed)

**Use when:** White void, clean studio sets, editorial portraits, hyperpop saturated worlds, fashion film, performance-on-set, scenes that are *crafted* rather than *photographed*.

**Lens picks:**
- 32mm — full-body wide on the void / group framing
- 50mm — medium portrait
- 75mm — tight editorial face cuts
- 100mm — extreme close-ups (lips, eyes, jewelry, fabric)

**Drop-in block:**

```
Shot on ARRI Alexa Mini LF in ProRes 4444 LogC4, Cooke S4/i spherical prime
[XX]mm at T2 with Tiffen Black Pro-Mist 1/2 filter, locked-off tripod with
optional 4-to-6 inch slow push-in, photoreal editorial fashion film aesthetic
with gentle halation bloom on highlights and soft warm falloff in the Cooke
signature, fine 400 ASA film grain structure retaining warmth in the shadows,
highlights allowed to bloom slightly around fabric and chrome surfaces,
saturated editorial grade with warm-retained blacks not crushed to pure black,
slight skin tone warmth from the Cooke color rendition, 24fps base shutter 180
degrees[, total runtime roughly [YY] seconds]. Not CGI, not plastic, shot-on-film
analog aesthetic with real-world lens character.
```

**For rhinestone, chrome, or surface-detail close-ups, append:** `Glimmerglass diffusion added to the front element to bloom highlights on reflective surfaces.`

---

## MODE 3 — ACTION / COMBAT (Documentary-Sci-Fi)

**Use when:** Combat, chase, stunts, war, mech battles, alien encounters, fight choreography, any high-physicality scene with debris, smoke, dust, destruction.

**Drop-in block:**

```
Shot on ARRI Alexa 35 in ProRes 4444 LogC4, Panavision Ultra Vintage 2x
anamorphic [XX]mm at T2.3 with Tiffen Black Pro-Mist 1/4 filter, all camera
work is handheld and shaky throughout with constant operator micro-jitter,
reactive movement, and chaotic shake, no stabilized or locked-off or
dolly-smooth shots anywhere, gritty documentary-meets-sci-fi war film
aesthetic with no stylization and everything grounded in physical realism,
Kodak Vision3 250D film emulation with 800 ASA grain structure, [palette
descriptor] with dusty atmospheric haze, slight halation on highlights,
24fps base shutter 180 degrees[, total runtime roughly [YY] seconds].
```

**Palette descriptors:** `daylight overcast palette`, `golden hour warm palette`, `blue-hour cool palette`, `stormy desaturated palette`, `night neon-lit palette`.

---

## MODE 4 — PERFORMANCE / CONCERT (Pit-Photographer Documentary)

**Use when:** Stadium and arena performance shots, festival pits, concert footage, jumbotron-and-lightstick worlds, anywhere a performer is on stage with a crowd and stage lighting.

**Drop-in block:**

```
Shot on ARRI Alexa 35 in ProRes 4444 LogC4, Panavision Ultra Vintage 2x
anamorphic [XX]mm at T2.3 with Tiffen Black Pro-Mist 1/4 filter, mixed handheld
pit-photographer energy with rapid handhelds and shaky low-angle operator work
and orbital handheld passes around the performers, hard cuts between angles,
no stabilized or locked-off shots, photoreal concert documentary aesthetic,
Kodak Vision3 250D film emulation with fine grain structure overlaid throughout,
slightly desaturated cool tones with warm highlight bloom and deep blacks
holding shadow detail, [stage-lighting color cast descriptor], heavy volumetric
haze with dust suspended in every beam, real sweat sheen on skin and real
fabric darkening from exertion, gentle halation on light sources, 24fps base
shutter 180 degrees[, total runtime roughly [YY] seconds].
```

**Stage-lighting descriptors:** `magenta-red color cast from the LED cube above`, `amber and ultraviolet wash from side rigs`, `cyan and white strobe punching through warm tungsten`, `golden side-key with deep blue back-wash`.

---

## MODE 5 — ATMOSPHERIC / EMPTY (Environment & Mood)

**Use when:** Abandoned cityscapes, no-humans environment plates, landscapes, weather pieces, slow-burn mood shots, world-establishing footage where the environment is the subject.

**Also triggered by:** "no humans," "abandoned," "empty," "ghost city," "deserted," "weather plate," "establishing wide" requests.

**Drop-in block:**

```
Shot on ARRI Alexa Mini LF in ProRes 4444 LogC4, Panavision Ultra Vintage 2x
anamorphic [XX]mm at T2.3 with Tiffen Black Pro-Mist 1/4 filter, locked-off or
extremely slow push-in motion only, no handheld energy, photoreal atmospheric
environment plate aesthetic, Kodak Vision3 250D film emulation with fine 400
ASA grain structure, palette-driven grade with [palette descriptor] and hex
values [list 4-8 hex values from the user's palette], strong negative space,
deep depth of field, light atmospheric haze with dust particles suspended in
air, weathered material detail with oxidized metal and dust-covered glass and
cracked paint and moisture stains, slight anamorphic flares on any directional
light sources, 24fps base shutter 180 degrees[, total runtime roughly [YY]
seconds]. No humans, no silhouettes, no living beings — the environment is
the subject.
```

---

## MODE STACKING (MULTI-WORLD VIDEO SEQUENCES)

If a single video cuts between two worlds — e.g., a music video that intercuts a white void (M2) with a kitchen (M1), or action (M3) intercut with performance (M4) — write each shot's camera block separately according to its mode. Don't blend the specs into one averaged grade.

The cut between modes is the visual punch; collapsing them kills the contrast.

For multi-shot sequences in the **same** mode, compose one continuous prompt with hard-cut triggers in the action description (`Shot 1 (0–3s): ... hard cut to Shot 2 (3–8s): ...`) and a single shared camera block at the end.

---

## CHOOSING A MODE — FAST RULES

| Scene element | Mode |
|---|---|
| Real interior, real exterior, "lived in" | M1 |
| White / void / set / studio / editorial | M2 |
| Combat, chase, debris, fight choreography | M3 |
| Stage, pit, festival, crowd, performer | M4 |
| No humans, environment is the subject | M5 |
| Wedding / event / documentary style | M1 |
| Music video → editorial sequence | M2 |
| Music video → action sequence | M3 |
| Music video → performance sequence | M4 |
| Lookbook / fashion film | M2 |
| Beauty / cosmetic close-up | M2 |
| Crime / thriller location | M1 |
| Sci-fi mech / alien / VFX-heavy | M3 |
| Post-apocalyptic landscape | M5 |
| Dance video on set | M2 |
| Dance video on location | M1 |

---

## ANTI-PATTERNS (ALL MODES)

- **Mixing two film stocks** — pick one. 250D, 500T, or 5219 — never two.
- **Stabilized + handheld in the same shot** — pick one motion register.
- **"Cinematic" without specifying the mode** — useless. Pick M1-M5 explicitly.
- **Writing the aspect ratio in the camera block** — aspect lives in the API parameter, not the prompt.
- **Specifying ISO ranges without ASA emulation** — say `800 ASA grain` not `ISO 800 sensor noise`.
- **Generic "shallow depth of field"** — be specific: `T/2 anamorphic shallow DOF with oval bokeh`.
