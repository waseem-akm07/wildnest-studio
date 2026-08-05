# Image Prompts — AI Image Generation Templates

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [Image/](file:///e:/Animation/wildnest-studio/prompts/Image/index.md) ──► `index.md`  
> 🎯 **Canonical Source:** [WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)  
> 📜 **Governing Standard:** [STD-PROMPT-001 Prompt Standard](file:///e:/Animation/wildnest-studio/standards/Prompt_Standard.md)  

---


> **Purpose:** Reusable prompt templates for character renders, environment sets, and prop assets.

## Primary Tools

| Tool | Use Case |
| :--- | :--- |
| Flux Dev 1.0 (Local GPU) | Primary character turnarounds and environment renders |
| Midjourney v6.1 | Style exploration and concept art |
| SDXL Turbo | Rapid iteration and batch testing |

## Prompt Structure

Every image prompt must include:
1. **Subject description** — character/environment with locked visual specs
2. **Style tokens** — `stylized 3D, Pixar-quality, cozy tactile, soft fur texture`
3. **Lighting spec** — `5500K warm golden key light, 6500K cyan fill, 3000K amber rim`
4. **Camera spec** — lens angle, depth of field, eye-level perspective
5. **Negative prompt** — explicitly block common AI failures

## References

- Master prompt guidelines: `production/current/CHR-001/prompts/00_Prompt_Guidelines.md`
- Negative prompt library: `production/current/CHR-001/prompts/02_Negative_Prompt.md`