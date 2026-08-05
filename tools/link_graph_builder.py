"""
Script ID:     TOOLS-GRAPH-001
Purpose:       Builds and updates graph navigation lineage blocks and breadcrumb links across all Markdown files in WildNest Studio.
Usage:         python tools/link_graph_builder.py
Author:        WildNest Studio Technical Architecture
"""

import os
import re
from pathlib import Path

ROOT_DIR = Path(r"e:\Animation\wildnest-studio")
README_PATH = ROOT_DIR / "README.md"

# Map of canonical source of truth per directory/module
CANONICAL_MAP = {
    "00_Vision": ("[PRD-001 Master PRD](file:///e:/Animation/wildnest-studio/docs/00_Vision/01_WildNest_Product_Requirements_Document.md)", "[STD-DOC-001 Documentation Standard](file:///e:/Animation/wildnest-studio/standards/Documentation_Standard.md)"),
    "01_Market_Research": ("[PRD-001 Master PRD](file:///e:/Animation/wildnest-studio/docs/00_Vision/01_WildNest_Product_Requirements_Document.md)", "[STD-RES-001 Research Standard](file:///e:/Animation/wildnest-studio/standards/Research_Standard.md)"),
    "02_Brand": ("[BRAND-001 Language & Localization Strategy](file:///e:/Animation/wildnest-studio/docs/02_Brand/Language_and_Localization_Strategy.md)", "[STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)"),
    "02_Creative_Development": ("[CEF-001 Creative Evaluation Framework](file:///e:/Animation/wildnest-studio/docs/02_Creative_Development/Creative_Evaluation_Framework.md)", "[STD-DOC-001 Documentation Standard](file:///e:/Animation/wildnest-studio/standards/Documentation_Standard.md)"),
    "03_Universe": ("[UNI-001 Critter Haven Resort Universe Bible](file:///e:/Animation/wildnest-studio/docs/03_Universe/01_Universe_Bible.md)", "[STD-DESIGN-001 Design Standard](file:///e:/Animation/wildnest-studio/standards/Design_Standard.md)"),
    "04_Characters": ("[CHR-BIBLE-001 Master Character Bible](file:///e:/Animation/wildnest-studio/docs/04_Characters/00_Character_Bible.md)", "[STD-DESIGN-001 Design Standard](file:///e:/Animation/wildnest-studio/standards/Design_Standard.md)"),
    "05_Story_Bible": ("[SB-001 Master Story Bible](file:///e:/Animation/wildnest-studio/docs/05_Story_Bible/00_Story_Bible.md)", "[STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)"),
    "06_Art_Direction": ("[ART-001 Visual Style Guide](file:///e:/Animation/wildnest-studio/docs/06_Art_Direction/01_Visual_Style_Guide.md)", "[STD-DESIGN-001 Design Standard](file:///e:/Animation/wildnest-studio/standards/Design_Standard.md)"),
    "09_Production": ("[WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)", "[STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)"),
    "10_Episodes": ("[SB-001 Master Story Bible](file:///e:/Animation/wildnest-studio/docs/05_Story_Bible/00_Story_Bible.md)", "[STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)"),
    "standards": ("[PRD-001 Master PRD](file:///e:/Animation/wildnest-studio/docs/00_Vision/01_WildNest_Product_Requirements_Document.md)", "[STD-DOC-001 Documentation Standard](file:///e:/Animation/wildnest-studio/standards/Documentation_Standard.md)"),
    "assets": ("[ART-001 Visual Style Guide](file:///e:/Animation/wildnest-studio/docs/06_Art_Direction/01_Visual_Style_Guide.md)", "[STD-NAMING-001 Naming Convention](file:///e:/Animation/wildnest-studio/standards/Naming_Convention.md)"),
    "production": ("[WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)", "[STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)"),
    "episodes": ("[SB-001 Master Story Bible](file:///e:/Animation/wildnest-studio/docs/05_Story_Bible/00_Story_Bible.md)", "[STD-PROD-001 Production Standard](file:///e:/Animation/wildnest-studio/standards/Production_Standard.md)"),
    "prompts": ("[WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)", "[STD-PROMPT-001 Prompt Standard](file:///e:/Animation/wildnest-studio/standards/Prompt_Standard.md)"),
    "automation": ("[WPOS-001 AI Production Pipeline OS](file:///e:/Animation/wildnest-studio/docs/09_Production/01_AI_Production_Pipeline.md)", "[STD-CODE-001 Coding Standard](file:///e:/Animation/wildnest-studio/standards/Coding_Standard.md)"),
    "research": ("[Research Standard WRS-001](file:///e:/Animation/wildnest-studio/research/Research_Standard.md)", "[STD-RES-001 Research Standard](file:///e:/Animation/wildnest-studio/standards/Research_Standard.md)"),
}

def get_file_href(path: Path) -> str:
    return f"file:///{path.as_posix()}"

def generate_lineage_block(filepath: Path) -> str:
    rel_path = filepath.relative_to(ROOT_DIR)
    parts = rel_path.parts
    
    # Root README doesn't get a header lineage block (it has the master map)
    if filepath == README_PATH:
        return ""
        
    # Determine Parent Index Path
    parent_dir = filepath.parent
    parent_index = parent_dir / "index.md"
    if not parent_index.exists() and parent_dir != ROOT_DIR:
        parent_index = ROOT_DIR / "docs" / "index.md"
    if parent_dir == ROOT_DIR:
        parent_index = ROOT_DIR / "docs" / "index.md"
        
    root_link = f"[Studio README]({get_file_href(README_PATH)})"
    parent_link = f"[{parent_dir.name}/]({get_file_href(parent_index)})"
    
    # Determine Canonical Source and Governing Standard
    canonical = "[PRD-001 Master PRD](file:///e:/Animation/wildnest-studio/docs/00_Vision/01_WildNest_Product_Requirements_Document.md)"
    governing = "[STD-DOC-001 Documentation Standard](file:///e:/Animation/wildnest-studio/standards/Documentation_Standard.md)"
    
    for key, (can, gov) in CANONICAL_MAP.items():
        if key in parts:
            canonical = can
            governing = gov
            break
            
    block = f"""
> **Navigation & Lineage:**  
> 📍 **Breadcrumbs:** {root_link} ──► {parent_link} ──► `{filepath.name}`  
> 🎯 **Canonical Source:** {canonical}  
> 📜 **Governing Standard:** {governing}  

---
"""
    return block.strip()

def process_markdown_file(filepath: Path):
    if filepath == README_PATH:
        return
        
    try:
        content = filepath.read_text(encoding="utf-8")
        
        # Check if lineage block already exists
        if "> **Navigation & Lineage:**" in content:
            return
            
        lineage_block = generate_lineage_block(filepath)
        if not lineage_block:
            return
            
        lines = content.splitlines()
        
        # Insert after the title header or metadata block
        insert_idx = 0
        in_header = False
        
        for i, line in enumerate(lines[:25]):
            if line.startswith("# "):
                insert_idx = i + 1
            elif line.startswith("> **Document ID:**") or line.startswith("> **Version:**"):
                in_header = True
            elif in_header and line.strip() == "---":
                insert_idx = i + 1
                break
                
        if insert_idx == 0:
            new_content = lineage_block + "\n\n" + content
        else:
            new_content = "\n".join(lines[:insert_idx]) + "\n\n" + lineage_block + "\n\n" + "\n".join(lines[insert_idx:])
            
        filepath.write_text(new_content, encoding="utf-8")
        print(f"[GRAPH UPDATED] {filepath.relative_to(ROOT_DIR)}")
    except Exception as e:
        print(f"[ERROR] Failed processing {filepath}: {e}")

def main():
    print("Building WildNest Studio Graph Linkage Network...")
    md_files = [p for p in ROOT_DIR.rglob("*.md") if ".git" not in p.parts]
    count = 0
    for md_file in md_files:
        process_markdown_file(md_file)
        count += 1
    print(f"Graph Linkage complete! Processed {count} files.")

if __name__ == "__main__":
    main()
