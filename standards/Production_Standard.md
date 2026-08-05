# WildNest Studio Production Standard

> **Document ID:** STD-PROD-001  
> **Version:** 1.0  
> **Status:** Mandatory Studio Standard  
> **Owner:** Head of Production & Operations  

---

## 1. Overview

This document specifies the technical and operational production standards for all animated content produced by **WildNest Studio**. It defines render specs, frame rates, color pipelines, audio mix targets, and quality thresholds across 15-second Shorts, 2.5-minute standard episodes, and 12-minute seasonal specials.

---

## 2. Technical Render Specifications

### 2.1 Video Render Standards

| Parameter | Master Standard (Episodes) | Short-Form Standard (Shorts/Reels) |
| :--- | :--- | :--- |
| **Aspect Ratio** | 16:9 Landscape (`3840x2160` 4K UHD) | 9:16 Vertical (`1080x1920` FHD) |
| **Frame Rate** | 24.0 fps Progressive (Native Cinematic) | 24.0 fps Progressive |
| **Color Space** | Rec.709 / DCI-P3 Gamma 2.4 | Rec.709 Gamma 2.4 |
| **Container & Codec** | MP4 (H.264 / ProRes 422 HQ Master) | MP4 (H.264 High Profile) |
| **Bitrate Target** | 45–60 Mbps (4K Master) | 15–20 Mbps (Vertical HD) |

### 2.2 Audio Mix Standards

| Parameter | Standard Target |
| :--- | :--- |
| **Sample Rate** | 48.0 kHz / 24-bit PCM Stereo |
| **Integrated Loudness** | **-14.0 LUFS** (± 1.0 LUFS YouTube Standard) |
| **Max True Peak** | -1.0 dBTP |
| **Dialogue Stem** | Hinglish dialogue centered; Max 8 words per line |
| **Audio Buffer Space** | 20% silent buffer space between dialogue lines for global dubbing |

---

## 3. The 14-Stage Production Chain

All studio production must proceed sequentially through the 14-stage pipeline defined in `WPOS-001` and `WSPW-001`:

```
01. Idea ──► 02. Brief ──► 03. Script ──► 04. Shot List ──► 05. Asset Gen ──► 06. Video Gen ──► 07. Voice Gen
                                                                                                     │
14. Retro ◄── 13. Analytics ◄── 12. Upload ◄── 11. Thumbnail ◄── 10. QA Audit ◄── 09. Editing ◄── 08. Music & SFX
```

No stage may be skipped or bypassed.

---

## 4. The 8-Gate Quality Assurance Inspection

Before any finished media file is cleared for upload, it must achieve a **100% Pass Rate** across the 8 Quality Gates:

1. **Gate 1 (Story Integrity):** 6-Beat hybrid structure verified; script passes the Silent Mute Test.
2. **Gate 2 (Character Consistency):** Character matches locked color hexes and geometry in 100% of frames.
3. **Gate 3 (Visual Consistency):** Zero set drift, background warping, or camera perspective shifts.
4. **Gate 4 (Animation Quality):** Smooth 24fps render with zero AI melting artifacts.
5. **Gate 5 (Voice & Audio):** Hinglish dialogue cadence clear; non-verbal soundbank integrated.
6. **Gate 6 (Music & SFX Mix):** Stereo music balanced; audio normalized to -14 LUFS.
7. **Gate 7 (Branding & End Cards):** Official 3D end card & subscriber callout attached.
8. **Gate 8 (Thumbnail & Metadata):** 3-Element CTR rule satisfied; 3 SRT subtitle tracks attached.

---

## 5. Asset Reuse & Velocity Targets

- **Asset Reuse Target:** `>= 75%` environment set and prop reuse per episode.
- **AI First-Pass Yield Target:** `>= 85%` usable raw generation outputs.
- **Compute Cost Budget:** `< $15 USD` per Short; `< $40 USD` per 2.5-minute episode.
