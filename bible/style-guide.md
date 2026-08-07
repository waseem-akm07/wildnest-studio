# Visual Style Guide

> Art style, colors, lighting, camera rules, and rendering standards for all WildNest content.

---

## Art Style

**Stylized Cozy 3D Animation** — Pixar's character appeal meets Studio Ghibli's environmental warmth.

```
[PIXAR 3D CHARACTER APPEAL]  +  [GHIBLI ENVIRONMENTAL WARMTH]  =  WILDNEST COZY 3D IDENTITY
```

### Core Principles

1. **Simplicity** — Clean silhouettes and uncluttered compositions
2. **Appeal over Realism** — We pursue cuteness and warmth, NOT photorealism
3. **Warmth over Spectacle** — Every scene must feel cozy and inviting
4. **Readability** — Must be 100% legible at thumbnail scale in 0.1 seconds
5. **Characters First** — Characters are always the focal point; backgrounds support, never compete
6. **Visual Universality** — Every frame must communicate with audio muted

---

## Color Palette

### Master Studio Colors

```
PRIMARY GOLDEN AMBER     SECONDARY MINT GREEN     TERTIARY CYAN BLUE     ACCENT SIGNAL RED
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐   ┌──────────────────┐
│  #D48C46         │     │  #06D6A0         │     │  #00B4D8         │   │  #D62828         │
│  Warm Hero Base  │     │  Cozy Secondary  │     │  Tube & Sky Pop  │   │  Focal Accents   │
└──────────────────┘     └──────────────────┘     └──────────────────┘   └──────────────────┘
```

- **Primary (60%):** Golden Amber `#D48C46`, Cream White `#FFF8E7`, Soft Peach `#FFCBA4`
- **Secondary (30%):** Mint Green `#06D6A0`, Cyan Blue `#00B4D8`, Warm Wood `#800020`
- **Accent (10%):** Signal Red `#D62828`, Electric Lime `#70E000`, Radiant Gold `#FFD166`

### Day/Night Color Profiles

| Time Period | Lighting | Colors |
|:---|:---|:---|
| **Daytime (8AM–4:30PM)** | High-key warm sunlight (`5500K`) | Bright golden, soft cyan bounces |
| **Twilight/Deadline (4:30–5PM)** | Deep orange golden hour (`2700K`) | Long dramatic purple shadows |
| **Nighttime (5PM–7AM)** | Deep indigo ambient (`#10002B`) | Warm amber prop glows (`#FFD000`) |

---

## Lighting

Always use a **3-Point Warm Cinematic Lighting System:**

```
                          [KEY LIGHT: 5500K Warm Golden (50% Power)]
                                            │
                                            ▼
 [FILL LIGHT: 6500K Soft Cyan (25%)] ──► [CHARACTER] ◄── [RIM LIGHT: 3000K Amber Edge (25%)]
```

1. **Key Light (50%):** Warm golden sunlight, 45° off-axis for soft dimensional modeling
2. **Fill Light (25%):** Soft cyan/sky-blue to lift shadows and maintain cheerfulness
3. **Rim Light (25%):** Warm amber rim to pop character silhouettes off backgrounds
4. **Shadow rule:** Shadows are never pure black — fill with 20% ambient tint (`#1A1A2E`)

---

## Materials & Textures

| Surface | Treatment |
|:---|:---|
| **Fur** | Smooth soft clumps with velvet sheen — no individual strand noise |
| **Plastic Tubes** | Tinted semi-translucent (`75% opacity`) with smooth rounded specular highlights |
| **Fabric** | Soft felt, cotton-ball plush, coarse burlap with visible macro weave |
| **Metal (Scavenged)** | Brushed brass/tin/aluminum with soft edge scuffs — no mirror reflections |
| **Wood & Paper** | Warm polished mahogany, cardboard grain, torn paper edges |

---

## Character Rendering

- **Eyes:** Large deep pupils with **two crisp white catch-light reflections** (primary at 10 o'clock, secondary at 4 o'clock)
- **Geometry:** Exaggerated rounded proportions, 1:1.2 head-to-body ratios, smooth curves
- **Line Quality:** No hard black ink outlines — soft occlusion shadows define form
- **Squash & Stretch:** Cheek expansion during cheek-stuffing, smooth mesh deformers
- **Grounding:** Soft ambient occlusion shadows under feet/paws

---

## Camera Rules

| Shot Type | Lens | Use |
|:---|:---|:---|
| **Macro Close-Up** | 35mm/50mm | Emotional reactions, expressions, fidgeting |
| **Medium Action** | Standard | Dialogue, slapstick, character interactions |
| **Wide Establishing** | Wide | Environment scale, hub architecture |

### Critical Camera Rules

- **Height:** Camera at **critter eye-level** (2–4 inches off floor) — NEVER from human height
- **Lens Range:** Simulate 35mm–50mm macro lenses for miniature charm
- **Comedy Framing:** Use stationary wide-medium shots for slapstick — let the movement play out

---

## Animation Standards

- **Frame Rate:** 24fps progressive. "Ones" (24fps) during fast action, "twos" (12fps) during calm scenes
- **The 1.5-Second Reaction Hold:** Every comedic impact MUST hold on the reaction face for 36 frames (1.5s)
- **Squash & Stretch Limits:** Max 180% stretch on fast movement, max 50% squash on impacts
- **Eye Lead:** Pupils must lead body movement by 2 frames

---

## 9 Expression Profiles

Every character must be able to hit these 9 expressions:

```
1. JOY        — Enlarged pupils, high curved brows, wide open smile
2. PANIC      — Shrunk pin-prick pupils, wide sclera, jaw drop, sweat drop
3. ANGER      — V-angled brows, squinted eyelids, clenched jaw
4. SURPRISE   — O-shaped eyes & mouth, popped ears, mid-air freeze
5. SUSPICION  — One raised brow, half-lidded eyes, asymmetric smirk
6. EMBARRASS  — Blushing cheeks, squashed neck, eyes looking away
7. CONFUSION  — Tilted head, wavy mouth, mismatched eye sizes
8. SADNESS    — Drooped eyelids, downturned brows, quivering lip
9. MISCHIEF   — Narrowed eyes, wide toothy grin, rubbing paws
```

---

## Prop Design

Every prop follows the **Scavenged Human Object Rule** — props must look 100% like real-world items creatively adapted by tiny animal hands. See [world.md](file:///e:/Animation/wildnest-studio/bible/world.md) for the full prop reference table.

---

## Thumbnail Design (YouTube CTR)

Follow the **3-Element Rule** for maximum click-through:

```
60% — 1-2 LARGE HIGH-EMOTION CHARACTER FACES (Panic, Shock, Joy)
30% — HIGH-CONTRAST BRIGHT BACKGROUND (cyan tube or orange glow)
10% — 1 ICONIC PROP (exploding clock gear, dripping water bottle)
```

- **Text:** Zero or max 2 bold words in rounded 3D yellow type (`#FFD166`)
- **Typography:** Rounded sans-serif fonts (Outfit, Fredoka One, Rounded Mplus)

---

## VFX Rules

- ✅ Floating dust motes, steam puffs, water splashes, sparkle dust, speed lines
- ❌ Realistic blood/fire/smoke, photorealistic lens flares, gritty grime, complex fluid sims

---

## AI Master Prompts

### Character Portrait Prompt
> `Masterpiece 3D digital animation portrait of [CHARACTER], [description]. Stylized 3D Pixar animation style, warm 5500K key lighting, soft cyan fill light, clean studio depth of field, highly detailed soft fur texture, 8k resolution, Octane render --ar 1:1 --stylize 250`

### Environment Scene Prompt
> `Cinematic 3D animation concept art of [LOCATION] inside Critter Haven Resort. Bright colorful plastic cage tubes, [details], warm sunbeams with floating dust motes streaming through a suburban bedroom window, Pixar and Studio Ghibli warm aesthetic, 8k resolution --ar 16:9 --stylize 200`

### Action / Slapstick Prompt
> `High-speed 3D animation action scene of [CHARACTER] [action], wide panicked eyes, [details], dynamic motion blur, bright vibrant lighting, Pixar animation style --ar 16:9`

### Video Dialogue Prompt
> `3D animated video clip of [CHARACTER] [action]. Smooth 24fps Pixar-style animation, warm studio lighting, subtle depth of field, detailed fur movement --v 6.0`

---

## Language & Audio Notes

- **Primary Language:** Hinglish (75% Hindi grammar + 25% everyday English words)
- **Max dialogue:** 8 words per spoken line
- **The 80/20 Rule:** 80% visual storytelling, 20% dialogue enhancement
- **The Mute Test:** Every episode must be 100% understandable with 0 audio volume
- **Subtitles (3 tracks):** Hinglish Roman, Hindi Devanagari, English SDH

---

## Do's & Don'ts

| ✅ ALWAYS | ❌ NEVER |
|:---|:---|
| Use warm golden key lighting + soft cyan fill | Use pure black shadows or grim dark lighting |
| Keep shape language simple and rounded | Add hyper-detailed fur strand noise |
| Frame cameras at critter eye-level | Shoot from high human angles |
| Emphasize dual white catch-lights in eyes | Render dull, lifeless eyes without catch-lights |
| Make props look like re-purposed human objects | Use manufactured fantasy props |

---

*Original source: [_archive/docs/06_Art_Direction/01_Visual_Style_Guide.md](file:///e:/Animation/wildnest-studio/_archive/docs/06_Art_Direction/01_Visual_Style_Guide.md)*
