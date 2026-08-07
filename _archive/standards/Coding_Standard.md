# WildNest Studio Automation & Scripting Coding Standard

> **Document ID:** STD-CODE-001  
> **Version:** 1.0  
> **Status:** Mandatory Studio Standard  
> **Owner:** Lead Pipeline Engineer  

---

> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** [Studio README](file:///e:/Animation/wildnest-studio/README.md) ──► [standards/](file:///e:/Animation/wildnest-studio/standards/index.md) ──► `Coding_Standard.md`  
> 🎯 **Canonical Source:** [PRD-001 Master PRD](file:///e:/Animation/wildnest-studio/docs/00_Vision/01_WildNest_Product_Requirements_Document.md)  
> 📜 **Governing Standard:** [STD-DOC-001 Documentation Standard](file:///e:/Animation/wildnest-studio/standards/Documentation_Standard.md)  

---


## 1. Overview

This document specifies coding, automation, and scripting standards for all Python scripts, utilities, and helper tools written for **WildNest Studio** inside `automation/` and `tools/`.

---

## 2. Language & Environment

- **Primary Language:** Python `3.10+`
- **Shell Environment:** PowerShell Core (Windows) / Bash (Linux fallbacks)
- **Dependency Management:** Standard library preferred; pin external requirements in `requirements.txt`
- **Code Style:** PEP 8 compliance with 4-space indentation

---

## 3. Mandatory Script Standards

### 3.1 Docstrings & Metadata
Every script must begin with a clear module docstring specifying purpose, author, dependencies, and CLI usage:

```python
"""
Script ID:     AUTO-RENDER-001
Purpose:       Automated batch generator for Flux/SDXL character turnarounds.
Usage:         python automation/batch_render.py --prod_id CHR-001 --batch_size 10
Dependencies:  requests, pillow, pyyaml
Author:        WildNest Pipeline Engineering
"""
```

### 3.2 Type Hints & Error Handling
- Use Python type annotations for all function parameters and return values.
- Implement explicit `try...except` blocks with meaningful log messages—never swallow exceptions silently.
- Return standard exit codes (`0` for success, `1` for error).

```python
import sys
from typing import Path

def validate_asset_path(path: Path) -> bool:
    """Validates if target asset exists and is non-empty."""
    try:
        return path.is_file() and path.stat().st_size > 0
    except Exception as e:
        print(f"[ERROR] Path validation failed: {e}", file=sys.stderr)
        return False
```

---

## 4. Logging & Path Handling

- **Use `pathlib.Path`** for all cross-platform file system operations—never hardcode raw string paths with `\` or `/`.
- **Log Levels:** Use standard logging levels (`INFO`, `WARNING`, `ERROR`, `DEBUG`).
- **Never mutate source assets directly:** Always write generated or modified outputs to timestamped temporary or output folders.