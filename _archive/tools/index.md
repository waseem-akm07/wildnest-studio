# Tools — Custom Utilities & Helpers

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [tools/](file:///e:/Animation/wildnest-studio/tools/index.md) ──► `index.md`  
> 🎯 **Canonical Source:** [PRD-001 Master PRD](file:///e:/Animation/wildnest-studio/docs/00_Vision/01_WildNest_Product_Requirements_Document.md)  
> 📜 **Governing Standard:** [STD-DOC-001 Documentation Standard](file:///e:/Animation/wildnest-studio/standards/Documentation_Standard.md)  

---


> **Purpose:** Standalone utility scripts and tools that support production but aren't part of the main automation pipeline.

## Planned Tools

| Tool | Purpose |
| :--- | :--- |
| Prompt formatter | Clean and standardize prompt text files |
| Asset indexer | Scan `assets/` and generate inventory report |
| File tree generator | Auto-generate repository map for README |
| Template copier | Initialize new episode/character folders from templates |
| LoRA dataset packager | Zip and organize approved turnarounds for LoRA training |

## Notes

- Tools in this directory are **one-off utilities**, not recurring pipeline automation
- For recurring pipeline scripts, use `automation/` instead
- Follow `standards/Coding_Standard.md` for all scripts