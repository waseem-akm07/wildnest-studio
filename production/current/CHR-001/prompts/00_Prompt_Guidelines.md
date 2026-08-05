# WildNest Character Prompt Engineering Guide

> **Document ID:** PROMPT-GUIDE-001  
> **Target Asset ID:** CHR-001 (*Barnaby Q. Whiskers*)  
> **Version:** 1.0  
> **Status:** Canonical Prompt Engineering Standard  
> **Owner:** Lead Prompt Engineer & Technical Director  
> **Last Updated:** 2026-08-05  

---

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [prompts/](file:///e:/Animation/wildnest-studio/docs/index.md) ──► `00_Prompt_Guidelines.md`  
> 🎯 **Canonical Source:** [WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)  
> 📜 **Governing Standard:** [STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)  

---


## 1. Executive Summary & Prompt Philosophy

This document defines the official **Character Prompt Engineering Standard** for WildNest Studio. Engineered by the Lead Prompt Engineer, this guide provides a universal, model-agnostic prompting framework for generating consistent animated characters across all major AI vision models—including **ChatGPT / DALL-E 3, Google Imagen 3, Gemini, Midjourney v6, Flux Dev/Pro, and future AI image generators**.

### Core Prompt Philosophy
```
  [1. MODEL-AGNOSTIC ARCHITECTURE] ──► [2. DETERMINISTIC ANCHOR TOKENS] ──► [3. 6-LAYER HIERARCHY]
                                                                                   │
  [6. ZERO VISUAL DRIFT POLICY]    ◄── [5. CROSS-MODEL TRANSLATION]     ◄── [4. EXACT COLOR HEXES]
```

1. **Tool-Agnostic Core:** Prompts are built around semantic physical anchors, not model-specific hacks or temporary syntax tricks that break across updates.
2. **Deterministic Anchor Tokens:** Every character is defined by 5 immutable physical anchor tokens (Species, Head-to-Body Ratio, Fur Color Hexes, Eye Geometry, Signature Scavenged Accessory).
3. **Layered Token Hierarchy:** Information is structured in a strict order of decreasing importance, ensuring AI models process core identity before style or lighting.
4. **Exact Color Hex Codes:** Fur, eye, and clothing colors are explicitly defined with 6-digit Hex codes (`#D48C46`, `#FFF8E7`, `#D62828`).
5. **Cross-Model Compatibility:** Prompts are easily translated between natural language paragraphs (DALL-E 3, Imagen, Gemini) and weighted token manifests (Midjourney, Flux, ComfyUI).
6. **Zero Visual Drift:** Character evolution is strictly controlled via versioned prompt increments, preserving 100% IP consistency.

---

## 2. The 6-Layer Master Prompt Hierarchy

To achieve maximum AI model adherence, prompts must follow the **WildNest 6-Layer Token Hierarchy**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: SUBJECT HIERARCHY      ──► Species, Anatomy, 1:1 Head Ratio, Color Hexes, Prop  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 2: STYLE HIERARCHY        ──► 3D Tactile Stylized, Pixar/Nintendo, SSS Shader    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 3: CAMERA & LENS HIERARCHY──► Macro 35mm/50mm, 2-4 Inch Eye-Level, Turnaround    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 4: LIGHTING HIERARCHY     ──► 5500K Key Light, 6500K Fill, 4000K Rim, Soft Shadow │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 5: ENVIRONMENT HIERARCHY  ──► White Turnaround / Central Lobby Tower Set         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ LAYER 6: EXCLUSION HIERARCHY    ──► Negative Prompts (Fabric bowtie, photorealism)     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Layer Breakdown

#### Layer 1: Subject Hierarchy (Non-Negotiable Core Identity)
* **Species:** `cute fluffy Syrian hamster`
* **Body Form:** `pear-shaped body, short chubby legs, 1:1 head-to-body ratio`
* **Fur Swatches:** `Golden Amber fur #D48C46, Cream White chest patch #FFF8E7`
* **Facial Geometry:** `large shiny pitch-black eyes occupying 40% vertical head space with dual specular highlights, tiny soft pink nose #FFB7B2, perky rounded ears`
* **Signature Scavenged Accessory:** `wearing a red metallic plastic twist-tie bowtie #D62828 around neck`

#### Layer 2: Style Hierarchy (Visual Tone & Shading)
* `3D stylized character render, Pixar style, tactile clay animation feel`
* `smooth peach-fuzz fur grooming, subtle subsurface scattering (SSS) on ear edges`

#### Layer 3: Camera & Lens Hierarchy (Perspective & Framing)
* `macro lens 50mm f/2.8, low camera angle strictly locked at 2-to-4 inch critter eye-level`
* `clean 360 turnaround pose, full body standing neutral pose`

#### Layer 4: Lighting & Shading Hierarchy (Atmosphere)
* `studio lighting, 5500K warm golden key light from top-right`
* `6500K cool fill light from left, 4000K rim light highlighting fur edges, soft contact shadows`

#### Layer 5: Environment & Background Hierarchy (Context)
* `solid white backdrop, seamless studio sweep` (Turnarounds)
* `re-purposed scavenged human prop resort set, plastic tube background` (In-Scene)

#### Layer 6: Exclusion Mechanics (Negative Prompting)
* `fabric bowtie, silk bowtie, ribbon, cloth, photorealistic wire fur, flat plastic texture, long snout, rat, mouse, dark fur, 1:2 head body ratio, aggressive expression, extra limbs, bad anatomy, noise, blurry`

---

## 3. Cross-Model Translation Matrix & Templates

Different AI image models process prompt syntax differently. WildNest provides two standardized master templates:

### Form A: Natural Language Paragraph
> **Target Models:** ChatGPT / DALL-E 3, Google Imagen 3, Gemini, Bing Image Creator.

```text
A high-quality 3D stylized character render of an adorable Syrian hamster named Barnaby, designed in a warm Pixar-like animation style. He has a pear-shaped body with a 1:1 head-to-body ratio, fluffy Golden Amber fur (#D48C46), and a soft Cream White patch on his chest (#FFF8E7). His face features large, shiny pitch-black eyes taking up 40% of his head with bright white dual specular highlights, a tiny soft pink nose (#FFB7B2), and perky rounded ears with subtle warm subsurface scattering. Around his neck, he wears a distinct red metallic plastic bread-bag twist-tie bowtie (#D62828) with subtle wire crinkles. He is standing in a clean, neutral pose on a solid white studio background. The scene is illuminated by 5500K warm key studio lighting with a soft rim light highlighting his peach-fuzz fur. Captured with a 50mm macro lens from a 3-inch eye-level perspective.
```

### Form B: Weighted Token Manifest
> **Target Models:** Midjourney v6, Flux Dev/Pro, Stable Diffusion XL, ComfyUI.

```text
masterpiece, best quality, 3d stylized character render, Pixar style, cute fluffy Syrian hamster, golden amber fur #D48C46, cream white chest patch #FFF8E7, (wearing a red metallic plastic twist-tie bowtie #D62828:1.2) around neck, pear-shaped body, 1:1 head to body ratio, (large shiny pitch-black eyes occupying 40% vertical head space with dual specular highlights:1.1), tiny soft pink nose #FFB7B2, perky rounded ears with subtle subsurface scattering, smooth peach-fuzz fur grooming, studio lighting 5500K warm key light, soft contact shadows, macro depth of field 50mm, 3-inch eye-level perspective, solid white background, clean turnaround pose --ar 16:9 --style raw --v 6.0
```

---

## 4. Standardized Prompt Naming Conventions

All prompt files in the studio depot must be saved using the standardized naming syntax:

```
  [CHR-ID]_[VIEW/SCENE]_[VERSION]_[MODEL].txt
```

### Naming Examples
* `CHR-001_FRONT_v1.0_FLUX.txt` (Barnaby Front Turnaround for Flux)
* `CHR-001_34VIEW_v1.0_MJ6.txt` (Barnaby 3/4 View for Midjourney v6)
* `CHR-001_PANIC_v1.2_DALLE3.txt` (Barnaby Reaction Pose for DALL-E 3)

---

## 5. Versioning, Testing & Iteration Strategy

Prompts undergo a 3-step testing protocol before being locked into `prompts/`:

```
  [STEP 1: SEED LOCK TEST]   ──► Test 10 fixed seeds to verify structural yield (Target >= 90%).
  [STEP 2: CFG MATRIX TEST]  ──► Test Guidance Scale CFG 4.0, 7.0, and 10.0 to find adherence sweet spot.
  [STEP 3: CROSS-MODEL TEST] ──► Test prompt across Flux, MJ6, and DALL-E 3 to verify cross-tool consistency.
```

### Versioning Rules
* **Patch Update (`v1.0.1`):** Minor word order adjustment or non-breaking negative token addition.
* **Minor Update (`v1.1.0`):** Adjusted lighting temperatures or camera distance tokens.
* **Major Update (`v2.0.0`):** New LoRA trigger token or updated character accessory specification.

---

## 6. Character Consistency Preservation Protocol

To evolve prompts for new episode scenes without losing character consistency, writers and prompt engineers must follow the **Anchor Lock Rule**:

> **THE ANCHOR LOCK RULE:**  
> When creating a new scene or expression prompt, **Layer 1 (Subject Hierarchy)** and **Layer 2 (Style Hierarchy)** tokens are strictly locked and must NEVER be modified. Only Layer 3 (Camera), Layer 4 (Lighting), and Layer 5 (Environment/Expression) tokens may be edited.

```
LOCKED TOKENS (NEVER CHANGE):   [Species, 1:1 Head Ratio, #D48C46 Fur, #D62828 Twist-Tie Bowtie, 3D Pixar Style]
VARIABLE TOKENS (SCENE ONLY):   [Expression (Panic/Joy), Camera Angle (Macro Close-Up), Background Set]
```

---

## 7. Success Criteria & QA Checklist

Before approving any new character prompt file into `prompts/`, verify:

- [ ] **Check 1 (6-Layer Order):** Follows the 6-layer hierarchy (Subject ──► Style ──► Camera ──► Lighting ──► Environment ──► Negative).
- [ ] **Check 2 (Hex Color Swatches):** Includes exact Hex codes for fur (`#D48C46`), chest (`#FFF8E7`), nose (`#FFB7B2`), and bowtie (`#D62828`).
- [ ] **Check 3 (Signature Accessory Anchor):** Explicitly specifies *red metallic plastic twist-tie bowtie* (and excludes fabric/silk in negative prompt).
- [ ] **Check 4 (Cross-Model Tested):** Form A (Natural Language) and Form B (Weighted Tokens) verified on target AI models.
- [ ] **Check 5 (Naming Syntax):** Saved cleanly as `[CHR-ID]_[VIEW]_[VERSION]_[MODEL].txt`.

---

## 8. References

* PROMPT-GUIDE-001 Master Foundations (UNI-001, CHR-BIBLE-001, CHR-001, ART-001, BRAND-001, WPOS-001, PROD-CHR-001).
* WildNest Studio Prompt Engineering Register (August 5, 2026).