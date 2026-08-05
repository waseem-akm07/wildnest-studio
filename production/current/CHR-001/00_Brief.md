# Character Production Brief: CHR-001 (Barnaby Q. Whiskers)

> **Production ID:** PROD-CHR-001  
> **Target Asset ID:** CHR-001 (*Barnaby Q. Whiskers*)  
> **Universe ID:** UNI-001 (*Critter Haven Resort*)  
> **Version:** 1.0  
> **Status:** Active Production Brief (In Review)  
> **Owner:** Production Director & Technical Director  
> **Last Updated:** 2026-08-05  

---

## 1. Executive Summary & Production Objective

This document is the official **Character Production Brief (PROD-CHR-001)** for Barnaby Q. Whiskers (CHR-001), the lead protagonist of WildNest Studio's flagship franchise, *Critter Haven Resort*.

This brief converts established creative specifications into an executable production sprint plan. Creative design decisions are not invented here; they are sourced directly from the Universe Bible (`UNI-001`), Character Bible (`CHR-BIBLE-001`), Visual Style Guide (`ART-001`), and CHR-001 Character Profile.

### Primary Objective
> **SPRINT GOAL:** Create the first production-ready, locked 360-degree visual asset pack for CHR-001 that can be consistently reproduced across AI image generation (Flux, SDXL, Midjourney) and AI video generation tools (Veo, Runway Gen-3) with zero visual drift.
> 
> *The desired outcome is not merely "beautiful artwork"—it is a **visually locked, production-ready character asset pack**.*

---

## 2. Input Documents & Source of Truth

The production team must adhere strictly to these canonical input documents as the single source of truth:

* **Universe Bible (`docs/03_Universe/01_Universe_Bible.md` - UNI-001):** Establishes bedroom cage context, scavenged prop rules, and hotel staff hierarchy.
* **Character Bible (`docs/04_Characters/00_Character_Bible.md` - CHR-BIBLE-001):** Establishes Kindchenschema geometry rules (1:1 head-to-body ratio, 40% eye height), 3-color palette rule, and flaw engines.
* **Main Character Profile (`docs/04_Characters/01_Main_Character_001.md` - CHR-001):** Establishes Barnaby's physical specs (Golden Amber fur `#D48C46`, Cream White chest patch `#FFF8E7`, Red Twist-Tie Bowtie `#D62828`, 3.5-inch height).
* **Visual Style Guide (`docs/06_Art_Direction/01_Visual_Style_Guide.md` - ART-001):** Establishes 3D tactile stylized aesthetic, fur grooming parameters, micro-depth of field, and 5500K warm golden key lighting.
* **Language & Localization Strategy (`docs/02_Brand/Language_and_Localization_Strategy.md` - BRAND-001):** Establishes Hinglish non-verbal squeak requirements.
* **Production Operating System (`docs/09_Production/01_AI_Production_Pipeline.md` - WPOS-001):** Establishes LoRA training requirements and ControlNet pose keyframing rules.

---

## 3. Measurable Production Goals

1. **Silhouette Recognition:** Barnaby's silhouette (pear-shaped body, oversized head, perky rounded ears, red twist-tie bowtie outline) must be instantly recognizable in pure black-and-white.
2. **Cross-Prompt Consistency:** Character maintains identical facial geometry, color hexes, and fur grooming across 10 consecutive prompt generations.
3. **Multi-View Capability:** Renders seamlessly in macro portrait close-up, medium desk-standing pose, and full-body 360 views.
4. **Camera Angle Stability:** Character maintains structural volume across extreme low-angle (eye-level), 3/4 angle, and high-angle overhead shots.
5. **Animation Riggability:** Geometry and fur mesh are clean, supporting 24fps motion, squash & stretch deformation, and 1.5s reaction hold keyframes without AI melting artifacts.
6. **Merchandising Alignment:** Visual asset matches 3D plushie manufacturing specifications and toy turnarounds.
7. **Brand Identity Fit:** 100% compliant with WildNest tactile stylized 3D aesthetic.

---

## 4. Sprint Scope & Deliverables

```
┌─────────────────────────────────────────┐     ┌─────────────────────────────────────────┐
│     MANDATORY DELIVERABLES (IN-SCOPE)   │     │    OUT-OF-SCOPE (FUTURE SPRINTS)       │
├─────────────────────────────────────────┤     ├─────────────────────────────────────────┤
│ • Front View (1:1 neutral standing)     │     │ • Expression Sheets (9 profiles)        │
│ • Left Side View (90-degree profile)    │     │ • Action Poses (Running, cheek panic)   │
│ • Right Side View (90-degree profile)   │     │ • Video Animation Tests (5 tests)       │
│ • Back View (Rear fur & tail check)     │     │ • ElevenLabs Voice Stem Soundbanks      │
│ • 3/4 Perspective View                  │     │ • Master Environment Background Sets    │
│ • Neutral Pose Master Renders           │     │                                         │
└─────────────────────────────────────────┘     └─────────────────────────────────────────┘
```

### Mandatory Deliverables (Sprint Focus)
- [x] **Front View:** Neutral standing pose, eye-level camera, white backdrop (`1920x1080` master PNG).
- [x] **Left Side View:** 90-degree profile showing snout length, cheek pouch boundary, and bowtie tie-knot.
- [x] **Right Side View:** 90-degree profile verifying symmetrical fur grooming and ear alignment.
- [x] **Back View:** Rear view showing spine fur pattern, tiny stub tail, and rear bowtie wrap.
- [x] **3/4 Perspective View:** Standard hero perspective shot demonstrating 3D volume and micro-depth.
- [x] **Neutral Pose Master Package:** High-resolution uncompressed PNG turnarounds ready for LoRA dataset training.

### Secondary Deliverables (Validation Assets)
* **Style Validation Images:** 3 renders verifying stylized tactile fur vs. photorealism boundaries.
* **Lighting Validation:** Renders under 8:00 AM morning key light (`5500K`) and 4:30 PM warm golden hour.
* **Color Validation Sheet:** Hex color swatch overlay verifying `#D48C46` (fur), `#FFF8E7` (chest), and `#D62828` (bowtie).
* **Scale Reference Chart:** Height comparison against a standard scavenged sewing thimble (1.0 inch) and human thumb.

---

## 5. Production Toolchain Architecture

The production workflow is **tool-agnostic** and modular, enabling seamless replacement of underlying software:

```
FUNCTIONAL CAPABILITY       PRIMARY TOOL             FALLBACK / ALTERNATIVE TOOL
---------------------       ------------             ───────────────────────────
Creative Direction          WildNest Core Bibles     Human Director Sign-Off
Prompt Engineering          ComfyUI Prompt Nodes     Local Master Text Manifests
Base Image Generation       Flux Dev 1.0 (Local)     Midjourney v6 / SDXL Turbo
LoRA Model Training         Kohya_ss (Local RTX)     Replicate Cloud LoRA Trainer
Pose Control & Depth        ControlNet OpenPose      Depth Anything V2 Midas
Asset Storage & Versioning  Git LFS / Local Depot    Cloud Studio Storage
```

---

## 6. Directory Infrastructure & Folder Purposes

All sprint assets must be organized strictly within `production/current/CHR-001/`:

```
production/current/CHR-001/
├── 00_Brief.md              <-- This master production contract
├── prompts/                 <-- Master positive, negative, & ControlNet prompt text files
├── outputs/                 <-- Raw AI generations (un-edited, timestamped batches)
├── review/                  <-- Selected candidate renders & side-by-side audit sheets
└── final/                   <-- Approved production assets (Locked canonical renders only)
```

### Folder Purpose Specifications
* `prompts/`: Contains master prompt manifests, negative prompt tokens, LoRA trigger tags (`barnaby_hamster`, `red_twist_bowtie`), and version logs.
* `outputs/`: Scratch directory for raw AI image generations. **No manual edits or hand-selected assets belong here.**
* `review/`: Contains candidate comparison grids, redline notes, color swatch checks, and QA audit feedback.
* `final/`: **Restricted Access Directory.** Holds ONLY 100% approved, CEO-locked production assets. No experimental or unverified files allowed.

---

## 7. Quality Gates & Approval Criteria

A character render cannot move to `final/` until it passes all **7 Quality Gates**:

- [ ] **Gate 1 (Silhouette Consistency):** Body forms a soft pear shape; head ratio is exactly 1:1 with torso; ears are rounded and perky.
- [ ] **Gate 2 (Color Hex Consistency):** Golden Amber fur (`#D48C46`), Cream White chest patch (`#FFF8E7`), and Red Twist-Tie Bowtie (`#D62828`) match color swatch tolerances (< 3% Delta-E variance).
- [ ] **Gate 3 (Facial Geometry & Kindchenschema):** Eyes occupy 40% of vertical head space; pupils are glossy pitch-black with 2 specular highlights; nose is tiny soft pink (`#FFB7B2`).
- [ ] **Gate 4 (Scavenged Accessory Check):** Bowtie is strictly a red metallic plastic bread-bag twist-tie with visible crinkles and wire core ends—NEVER a fabric silk bowtie.
- [ ] **Gate 5 (Fur Texture & Grooming):** Soft peach-fuzz grooming with tactile micro-depth; zero clumpy or photorealistic wire fur.
- [ ] **Gate 6 (Lighting & Material Shader):** 3-point warm lighting (`5500K` key, `6500K` fill, `4000K` rim) with subtle subsurface scattering (SSS) on ears.
- [ ] **Gate 7 (Prompt Reproducibility):** Master prompt package reproduces the character geometry in 10 out of 10 generation test runs.

---

## 8. Review Workflow & Exit Criteria

```
  [1. DRAFT PROMPTS]  ──►  [2. RAW OUTPUTS]  ──►  [3. INTERNAL REVIEW]
                                                           │
  [6. FINAL LOCK]     ◄──  [5. CEO APPROVAL] ◄──  [4. QA VALIDATION]
```

1. **Draft Stage:** Technical Lead drafts master prompt manifest in `prompts/`.
2. **Raw Output Stage:** Batch generates 50 raw images in `outputs/` using locked seeds and ControlNet pose guides.
3. **Internal Review Stage:** Art Director selects top 5 candidates per view angle and moves them to `review/`.
4. **QA Validation Stage:** QA Lead executes the 7 Quality Gates and color swatch audit.
5. **CEO Approval Stage:** Showrunner & Executive Producer review locked turnaround sheet.
6. **Final Stage:** Approved assets copied to `final/`; LoRA dataset locked; `CHANGELOG.md` updated.

---

## 9. Production Risks & Failure Mitigation

| Identified Risk | Risk Severity | Failure Symptom | Mitigation Strategy |
| :--- | :---: | :--- | :--- |
| **Proportion Drift** | High | Head shrinks to 1:2 ratio; snout elongates | Apply ControlNet Canny/OpenPose depth mask locked to 1:1 geometry template. |
| **Accessory Shift** | High | AI replaces twist-tie with fabric bowtie | Add negative prompts: `(fabric bowtie, silk bowtie, ribbon, cloth)`. |
| **Fur Texture Degradation** | Medium | Fur turns into flat plastic texture or hyper-real wire | Lock SSS subsurface scattering prompt tokens and 3D tactile shader references. |
| **Color Drift** | Medium | Fur shifts to orange or dark brown | Enforce RGB/Hex color correction filter pass in post-processing node. |
| **Prompt Instability** | High | Generation fails 40% of seed runs | Isolate trigger tokens; reduce LoRA weight to 0.75-0.85 sweet spot. |

---

## 10. Measurable Success Metrics

* **Visual Consistency Score:** `>= 95%` structural and color match across 50 test generations.
* **Silhouette Identification:** `100%` recognizable in solid black silhouette test.
* **Prompt Reproducibility:** `>= 90%` first-pass generation yield without manual retouching.
* **Manual Retouching Requirement:** `< 10%` pixel correction required per turnaround master.
* **Dataset Readiness:** Complete 360 turnaround dataset ready for Flux/SDXL LoRA training within 24 hours.

---

## 11. Production Sprint Checklist

- [ ] **Step 1:** Master positive and negative prompts compiled in `prompts/master_prompt.txt`.
- [ ] **Step 2:** ControlNet 360-degree pose turnaround templates loaded into ComfyUI.
- [ ] **Step 3:** 50 raw turnaround images generated in `outputs/`.
- [ ] **Step 4:** Top 5 candidate sets selected and moved to `review/`.
- [ ] **Step 5:** Color swatch & hex consistency audit completed (<3% Delta-E).
- [ ] **Step 6:** Front, Left Side, Right Side, Back, 3/4, and Neutral pose renders approved.
- [ ] **Step 7:** Approved turnarounds moved to `final/`.
- [ ] **Step 8:** LoRA dataset zip package archived in `final/dataset/`.
- [ ] **Step 9:** Production Brief sign-off completed by CEO & Technical Director.
- [ ] **Step 10:** Update `docs/CHANGELOG.md` to record `v1.1.0` Character Asset Lock.

---

## 12. CEO Approval Block & Production Status Lock

```
===============================================================================
                       WILDNEST STUDIO APPROVAL BLOCK
===============================================================================

Production ID:     PROD-CHR-001
Target Asset:      CHR-001 (Barnaby Q. Whiskers Master Turnaround)
Production Status: [ ] Draft   [X] In Review   [ ] Approved   [ ] Locked

Approval Date:     ________________________
Lead Producer:     ________________________ (Production Director)
Technical Lead:    ________________________ (CTO / Pipeline Architect)
Executive Sign-Off:________________________ (CEO / Showrunner)

===============================================================================
```

---

## 13. References

* PROD-CHR-001 Master Foundations (UNI-001, CHR-BIBLE-001, CHR-001, ART-001, BRAND-001, WPOS-001, WPOS-MVP-001, EP-001 Brief, CHANGELOG.md).
* WildNest Studio Character Production Register (August 5, 2026).
