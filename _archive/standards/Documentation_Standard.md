# WildNest Studio Documentation Standard

> **Document ID:** STD-DOC-001  
> **Version:** 1.0  
> **Status:** Mandatory Studio Standard  
> **Owner:** Documentation Manager & Knowledge Architect  

---

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [standards/](file:///e:/Animation/wildnest-studio/standards/index.md) ──► `Documentation_Standard.md`  
> 🎯 **Canonical Source:** [PRD-001 Master PRD](file:///e:/Animation/wildnest-studio/docs/00_Vision/01_WildNest_Product_Requirements_Document.md)  
> 📜 **Governing Standard:** [STD-DOC-001 Documentation Standard](file:///e:/Animation/wildnest-studio/standards/Documentation_Standard.md)  

---


## 1. Overview

This document specifies the formatting, structure, version control, and maintenance standards for all markdown documentation in **WildNest Studio**. As a documentation-first AI studio, our documentation is our primary operating software.

---

## 2. Document Anatomy & Header Block

Every canonical document inside `docs/` must begin with a standardized metadata header block:

```markdown
# [Document Title]

> **Document ID:** [DOC-ID]  
> **Version:** [X.Y]  
> **Status:** [Draft / In Review / Official Studio Policy / Canonical North Star]  
> **Owner:** [Role / Title]  
> **Last Updated:** YYYY-MM-DD  

---
```

---

## 3. Writing Style Guidelines

- **Executive Tone:** Concise, professional, data-driven, practical, and action-oriented.
- **No Marketing Fluff:** Internal strategy documents must focus on actionable specs, decision tables, metrics, and workflows.
- **GitHub-Flavored Markdown:** Utilize ASCII diagrams, structured tables, code fences, and GitHub callout blocks (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!WARNING]`).
- **Clickable File Links:** Always link referenced local repository files using GitHub-style markdown links (e.g., `[UNI-001](file:///e:/Animation/wildnest-studio/docs/03_Universe/01_Universe_Bible.md)`).

---

## 4. Versioning Strategy (SemVer 2.0.0)

WildNest Studio documentation follows Semantic Versioning adapted for studio operations:

```
                  [MAJOR] . [MINOR] . [PATCH]  ──►  v1.0.0
                     │        │        │
                     │        │        └─► Typo fixes, minor clarifications, link updates.
                     │        └──────────► New bibles, new character profiles, new pipeline tools.
                     └───────────────────► Major architectural shifts, new IP greenlights, PRD overhauls.
```

All non-patch changes must be logged in `docs/CHANGELOG.md` following the standardized change entry template.

---

## 5. Maintenance & Preservation Rules

- **Documentation First:** No new character, universe rule, or pipeline tool is introduced into production without first updating the corresponding canonical bible.
- **Never Delete Canon:** Documents are not deleted when superseded; they are moved to `docs/99_Archive/` to preserve studio history.
- **Single Source of Truth:** PRD-001 (`docs/00_Vision/01_WildNest_Product_Requirements_Document.md`) remains the ultimate authority in case of conflicts.