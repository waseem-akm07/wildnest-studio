# WildNest Studio Prompt Engineering Standard

> **Document ID:** STD-PROMPT-001  
> **Version:** 1.0  
> **Status:** Mandatory Studio Standard  
> **Owner:** Technical Director & AI Pipeline Architect  

---

## 1. Overview

This document specifies the mandatory prompt engineering structure, token sequencing, version control rules, and negative token manifests for all AI image and video generation prompts used at **WildNest Studio** (derived from `WPOS-001`).

---

## 2. Mandatory Prompt Structure

Every master image prompt created for production must follow a strict **5-Block Modular Architecture**:

```
[BLOCK 1: SUBJECT & CHARACTER SPECS]
  + [BLOCK 2: ENVIRONMENT & SCAVENGED PROPS]
  + [BLOCK 3: ART STYLE & SHADER PARAMETERS]
  + [BLOCK 4: LIGHTING & CAMERA SPECIFICATION]
  + [BLOCK 5: TRIGGER TAGS & LORA WEIGHTS]
```

### Example Structured Prompt
```text
3D stylized animation render of Barnaby, chubby Golden Syrian hamster with golden amber fur (#D48C46) and cream white chest patch (#FFF8E7), wearing a tiny crinkled red metallic twist-tie bowtie (#D62828). Standing inside a plastic hamster tube resort corridor with scavenged button plates and thimble cups. Pixar-quality stylized 3D render, soft velvet fur micro-texture, subsurface scattering on ears. 5500K warm golden key lighting, 6500K cyan fill, eye-level macro 85mm lens perspective, depth of field. <lora:barnaby_v1:0.8>
```

---

## 3. Negative Prompt Standards

All image generation runs must attach the locked studio **Negative Prompt Manifest** to prevent AI artifacts:

```text
(photorealistic, hyperrealistic, wire fur, clumpy fur:1.4), (fabric bowtie, silk bowtie, ribbon:1.3), (human hands, human fingers:1.4), (deformed limbs, extra legs, extra ears:1.4), (flat 2D, anime, vector, sketch:1.3), (mutated snout, elongated face:1.3), (dark gloomy lighting, harsh shadows:1.2), (blurry, lowres, watermark, text, signature:1.4)
```

---

## 4. Model & LoRA Weight Guidelines

- **Base LoRA Weight:** Keep custom character LoRAs between `0.75` and `0.85` weight to prevent prompt burning.
- **ControlNet Integration:** Always use OpenPose or Canny depth masks for multi-character interaction shots.
- **Seed Locking:** Always record and lock random seeds (`seed: XXXXXXXX`) in `prompts/` for reproducible outputs.
- **Regression Testing:** Before adopting a new AI generator version, run the **10 Master Test Prompts** to verify zero visual drift.
