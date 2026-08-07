# Experiments — R&D and Workflow Tests

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [experiments/](file:///e:/Animation/wildnest-studio/experiments/index.md) ──► `index.md`  
> 🎯 **Canonical Source:** [PRD-001 Master PRD](file:///e:/Animation/wildnest-studio/docs/00_Vision/01_WildNest_Product_Requirements_Document.md)  
> 📜 **Governing Standard:** [STD-DOC-001 Documentation Standard](file:///e:/Animation/wildnest-studio/standards/Documentation_Standard.md)  

---


> **Purpose:** Sandbox for testing new AI tools, workflow experiments, and technique R&D.

## What Goes Here

- New AI model evaluations (e.g., testing Kling AI vs. Runway Gen-3)
- Prompt engineering experiments
- Style exploration renders (non-production)
- ControlNet pose experiments
- LoRA training experiments with different parameters
- Lighting and shader tests

## Rules

- **Nothing in this folder is canonical.** Experiments are throwaway.
- Successful experiments should be documented and graduated to the production pipeline
- Use clear date-stamped folders: `YYYY-MM-DD_[experiment_name]/`
- Write a brief `README.md` in each experiment folder explaining what was tested and the result

## Folder Convention

```
experiments/
├── 2026-08-10_flux_lora_weight_test/
│   ├── README.md          ◄── What was tested + results
│   ├── outputs/           ◄── Generated images/videos
│   └── prompts/           ◄── Prompts used
└── 2026-08-15_veo_vs_runway_comparison/
    └── ...
```