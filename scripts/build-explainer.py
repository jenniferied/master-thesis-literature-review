#!/usr/bin/env python3
"""
Build explainer PDF from Markdown file.

This script converts the AI/ML foundations explainer document to PDF
using Pandoc and LuaLaTeX.

Usage:
    python scripts/build-explainer.py
    python scripts/build-explainer.py --output custom-name
    python scripts/build-explainer.py --merge-only  # Just copy to export/

Requirements:
    - Pandoc (https://pandoc.org/)
    - LuaLaTeX (via TeX Live or MacTeX)
"""

import argparse
import subprocess
import sys
import shutil
from pathlib import Path


def build_pdf(
    input_file: Path,
    output_path: Path,
    template: Path,
    figures_dir: Path,
) -> int:
    """Build PDF from markdown using Pandoc."""

    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        return 1

    if not template.exists():
        print(f"Error: Template not found: {template}")
        return 1

    print(f"Building PDF from: {input_file}")
    print(f"  Template: {template}")
    print(f"  Output: {output_path}")

    # Build pandoc command
    cmd = [
        "pandoc",
        str(input_file),
        "-o", str(output_path),
        f"--template={template}",
        "--pdf-engine=lualatex",
        # Enable figures
        f"--resource-path={figures_dir}",
        # Table of contents
        "--toc",
        "--toc-depth=3",
        # Variables
        "-V", "documentclass=article",
        "-V", "papersize=a4",
        "-V", "geometry:margin=2.54cm",
        "-V", "fontsize=11pt",
        # List of figures
        "-V", "lof=true",
    ]

    print(f"  Command: {' '.join(cmd)}")
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print(f"  PDF generated successfully: {output_path}")
    else:
        print(f"  Error: Pandoc failed with code {result.returncode}")

    return result.returncode


def copy_to_export(input_file: Path, output_dir: Path) -> int:
    """Copy markdown file to export directory."""
    output_path = output_dir / input_file.name
    shutil.copy(input_file, output_path)
    print(f"Copied: {input_file} -> {output_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build explainer PDF")
    parser.add_argument(
        "--output",
        type=str,
        default="ai_ml_foundations_explainer",
        help="Output filename (without extension)",
    )
    parser.add_argument(
        "--merge-only",
        action="store_true",
        help="Only copy markdown to export (no PDF)",
    )
    args = parser.parse_args()

    # Paths
    project_root = Path(__file__).parent.parent
    input_file = project_root / "drafts" / "ai_ml_foundations_explainer.md"
    template = project_root / "templates" / "explainer.tex"
    export_dir = project_root / "export"
    figures_dir = project_root / "figures"

    # Ensure export directory exists
    export_dir.mkdir(parents=True, exist_ok=True)

    if args.merge_only:
        return copy_to_export(input_file, export_dir)

    # Build PDF
    output_path = export_dir / f"{args.output}.pdf"
    return build_pdf(input_file, output_path, template, figures_dir)


if __name__ == "__main__":
    sys.exit(main())
