# WildNest Negative Prompt System: CHR-001 (Barnaby Q. Whiskers)

> **Document ID:** PROMPT-NEG-001  
> **Target Asset ID:** CHR-001 (*Barnaby Q. Whiskers*)  
> **Version:** 1.0.0 (Master Lock)  
> **Status:** Canonical QA Negative Prompt Standard  
> **Owner:** Quality Assurance Prompt Engineer & Technical Director  
> **Last Updated:** 2026-08-05  

---

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [prompts/](file:///e:/Animation/wildnest-studio/docs/index.md) ──► `02_Negative_Prompt.md`  
> 🎯 **Canonical Source:** [WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)  
> 📜 **Governing Standard:** [STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)  

---


## 1. Executive Summary & QA Philosophy

This document defines the official **Negative Prompt Specification (PROMPT-NEG-001)** for Barnaby Q. Whiskers (CHR-001). Engineered by the Quality Assurance Prompt Engineer, this system provides a defense-in-depth negative prompting framework designed to neutralize AI model bias, eliminate visual artifacts, prevent anatomical drift, and enforce 100% brand adherence across image and video generation pipelines.

Rather than providing an arbitrary list of keywords, this document explains **WHY every negative token exists** and what specific underlying AI training bias it counteracts.

---

## 2. Categorized Negative Token Architecture & Rationale

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. ANATOMY & GEOMETRY         ──► Prevents extra limbs, human hands, rat snouts        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. RENDERING & TEXTURE        ──► Prevents photorealistic wire fur & specular plastic  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. COMPOSITION & FRAMING      ──► Prevents head cutoffs & off-center camera drift      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. LIGHTING & SHADING         ──► Prevents pitch-black occlusions & blown highlights   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 5. CHARACTER CONSISTENCY      ──► Prevents fur color drift & 1:2 head ratio            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 6. STYLE DRIFT                ──► Prevents 2D anime lines, horror, & gritty tones      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 7. QUALITY & ARTIFACTS        ──► Prevents blurriness, JPEG noise, & compression       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 8. ACCESSORY & APPAREL        ──► Prevents fabric/silk bowties, shirts, & pants        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 9. BACKGROUND PROBLEMS        ──► Prevents cluttered background noise & real-world scale│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 10. INJECTION & WATERMARKS    ──► Prevents text overlays, logos, & copyright marks     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### Category 1: Anatomy & Geometry
* **Tokens:** `extra limbs, extra paws, 5-finger human hands, long snout, sharp rat snout, mouse tail, long tail, human ears, pointy elf ears, deformed paws, asymmetrical eyes, missing whiskers, double heads, fused limbs`
* **Technical Rationale (WHY it exists):** Diffusion models trained on general animal datasets frequently conflate hamsters with rats or mice (generating long tails or pointy snouts) or inject human hand topology (5 fingers) when rendering paws. Excluding these tokens locks Barnaby's species-pure Syrian hamster anatomy and short chubby 4-toed paws.

---

### Category 2: Rendering & Material Shading
* **Tokens:** `photorealistic wire fur, hyper-realism, 8k photographic texture, glossy specular plastic, flat clay lumps, un-groomed fur, coarse wire hair, metallic skin, transparent skin`
* **Technical Rationale (WHY it exists):** High-resolution image prompts often trigger photorealistic rendering modes that create coarse, individual wire hairs or specular plastic toy sheen. Excluding these tokens forces the rendering engine to default to WildNest's signature 3D tactile peach-fuzz grooming with soft subsurface scattering (SSS).

---

### Category 3: Composition & Framing
* **Tokens:** `cropped head, cut-off ears, out of frame torso, extreme close-up nose, off-center camera drift, tilted horizon, Dutch angle, fisheye distortion`
* **Technical Rationale (WHY it exists):** AI models tend to zoom in aggressively on cute animal faces, cutting off ear tips or lower body proportions. Excluding framing distortions ensures clean, full-body 360 turnaround framing locked at a 3-inch eye-level macro perspective.

---

### Category 4: Lighting & Shading
* **Tokens:** `pitch-black deep shadows, harsh direct sunlight, overexposed white blowouts, green ambient light tint, flash photography glare, flat rim-less lighting`
* **Technical Rationale (WHY it exists):** Uncontrolled lighting prompts lead to high-contrast specular blowouts or pitch-black shadow crevices that obscure character geometry. Excluding harsh lighting preserves the studio's soft 5500K warm key lighting and 4000K rim lighting.

---

### Category 5: Character & Color Consistency
* **Tokens:** `dark brown fur, orange fur, grey fur, black spots, missing cream chest patch, white eye patches, blue eyes, brown eyes, 1:2 head body ratio, tall lean body`
* **Technical Rationale (WHY it exists):** Prevents fur color drift away from Barnaby's locked Golden Amber (`#D48C46`) and Cream White chest (`#FFF8E7`) swatches, while enforcing his Kindchenschema 1:1 head-to-body vertical ratio.

---

### Category 6: Style Drift & Aesthetic Integrity
* **Tokens:** `2D anime lines, cel shading, sketch, watercolor, comic book ink, dark fantasy, horror aesthetic, monster teeth, scary eyes, gritty cyber-punk, photorealistic CGI movie`
* **Technical Rationale (WHY it exists):** Neutralizes model tendencies to pull toward 2D anime styles, dark fantasy art, or overly aggressive monster expressions. Preserves WildNest's warm, cozy, disarming 3D Pixar/Nintendo aesthetic.

---

### Category 7: Quality & Compression Artifacts
* **Tokens:** `blurry, low resolution, JPEG compression noise, pixelated, banding artifacts, motion blur, duplicate ghosting, canvas texture, film grain`
* **Technical Rationale (WHY it exists):** Cleans up low-pass render artifacts, video keyframe ghosting, and compression noise in batch diffusion steps.

---

### Category 8: Accessory & Apparel Integrity
* **Tokens:** `fabric bowtie, silk bowtie, cloth necktie, ribbon, suit jacket, pants, shoes, hat, glasses, belt, pocket watch`
* **Technical Rationale (WHY it exists):** AI models automatically associate the word "bowtie" with silk tuxedos or fabric ties. Excluding fabric bowties forces the engine to render Barnaby's unique scavenged **red metallic plastic bread-bag twist-tie bowtie (`#D62828`)**.

---

### Category 9: Background & Environmental Contamination
* **Tokens:** `cluttered human room, messy floor, real-world human feet, giant human hands, furniture background, outdoor grass field, natural forest`
* **Technical Rationale (WHY it exists):** Ensures studio turnaround renders remain on a clean solid white sweep without accidental room clutter or real-world human scale contamination.

---

### Category 10: Prompt Injection & Watermarks
* **Tokens:** `text, overlay, watermark, logo, artist signature, UI frame, borders, letterbox, copyright mark, sample text`
* **Technical Rationale (WHY it exists):** Suppresses unwanted stock image artifacts, artist signatures, or UI overlays embedded in web training data.

---

## 3. Master Negative Prompt Code Block

Below is the production-grade master negative prompt block ready for insertion into ComfyUI, Stable Diffusion, or API manifests:

```text
fabric bowtie, silk bowtie, cloth necktie, ribbon, suit jacket, photorealistic wire fur, hyper-realism, 8k photographic texture, glossy specular plastic, extra limbs, extra paws, 5-finger human hands, long snout, sharp rat snout, mouse tail, long tail, human ears, pointy elf ears, dark brown fur, grey fur, missing cream chest patch, 1:2 head body ratio, tall lean body, cropped head, cut-off ears, off-center camera drift, pitch-black deep shadows, harsh sunlight, overexposed white blowouts, 2D anime lines, cel shading, dark fantasy, horror, blurry, low resolution, JPEG compression noise, pixelated, text, watermark, logo, artist signature.
```

---

## 4. Short Negative Prompt Manifest

For high-speed batch rendering or token-constrained APIs (DALL-E / Flux API), use this high-impact 50-token short manifest:

```text
fabric bowtie, silk bowtie, photorealistic wire fur, extra limbs, 5-finger hands, long snout, rat, mouse, long tail, dark brown fur, missing cream chest patch, 1:2 head ratio, cropped head, harsh shadows, 2D anime, horror, blurry, low resolution, watermark, text.
```

---

## 5. Model-Specific Adaptation Notes

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MODEL ENGINE          NEGATIVE PROMPT INGESTION METHOD & SPECIAL HANDLING              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Flux Dev 1.0          Does not use negative text prompts natively. Embed negative      │
│                       exclusions directly into positive natural language prompt:       │
│                       "wearing a red metallic plastic twist-tie (not fabric silk)..."  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Midjourney v6         Use `--no` parameter string:                                     │
│                       `--no fabric bowtie, silk, photorealistic fur, extra limbs, rat`│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ DALL-E 3 / ChatGPT    Integrate negative instructions into prompt framing:             │
│                       "Ensure the bowtie is strictly metallic plastic, not fabric..." │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ ComfyUI / SDXL        Pass Master Negative Block directly into Negative CLIP Text Encode│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Negative Prompt QA Testing Checklist

Before approving any new model pipeline or prompt update, verify:

- [ ] **Check 1 (Accessory Safety):** 0% of test renders contain fabric or silk bowties.
- [ ] **Check 2 (Anatomy Safety):** 0% of test renders contain 5-finger hands or long rat snouts.
- [ ] **Check 3 (Color Safety):** Barnaby's fur remains strictly Golden Amber (`#D48C46`) and Cream White (`#FFF8E7`).
- [ ] **Check 4 (Proportion Safety):** 1:1 head-to-body vertical ratio preserved in 100% of renders.
- [ ] **Check 5 (Artifact Safety):** Renders are 100% free of watermarks, text overlays, and compression noise.

---

## 7. Revision Log & Future Improvements Roadmap

### Revision Log
* **`v1.0.0` (2026-08-05):** Initial Master Lock of PROMPT-NEG-001 with 10-category rationale architecture and model adaptation matrix.

### Future Improvements Roadmap
* **`v1.1.0` (Post-LoRA Training):** Fine-tune negative tokens based on custom Barnaby LoRA dataset edge-cases.
* **`v1.2.0` (Video Pipeline Optimization):** Add video keyframe motion artifacts (e.g., `ghosting, frame warping, temporal jittering`) to negative specs for Runway/Veo video runs.

---

## 8. References

* PROMPT-NEG-001 Specification (UNI-001, CHR-BIBLE-001, CHR-001, ART-001, BRAND-001, WPOS-001, PROD-CHR-001, 00_Prompt_Guidelines.md, 01_Master_Image_Prompt.md).
* WildNest Studio QA Prompt Depot (August 5, 2026).