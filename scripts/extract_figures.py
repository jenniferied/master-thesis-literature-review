#!/usr/bin/env python3
"""
Extract figures from academic PDFs for the AI/ML Explainer chapter.

This script extracts images from downloaded academic papers and saves them
with appropriate filenames for inclusion in the thesis.
"""

import fitz  # PyMuPDF
import os
from pathlib import Path

# Configuration
BASE_DIR = Path("/Users/jennifer/Documents/GitHub/master-thesis-literature-review")
PDF_DIR = BASE_DIR / "figures" / "ch-explainer"
OUTPUT_DIR = PDF_DIR / "extracted"

# PDFs and their target figures with page numbers (0-indexed)
PDF_CONFIGS = {
    "paper-ddpm-ho-2020.pdf": {
        "pages": [2],  # Page 3 in PDF (0-indexed = 2)
        "target_figure": "fig-diffusion-process",
        "description": "Forward and reverse diffusion process"
    },
    "paper-controlnet-zhang-2023.pdf": {
        "pages": [0, 2],  # Pages 1 and 3 (figures 1 and 3)
        "target_figure": "fig-controlnet-examples",
        "description": "ControlNet spatial control examples"
    },
    "paper-nerf-mildenhall-2020.pdf": {
        "pages": [3, 4],  # Pages 4-5
        "target_figure": "fig-nerf-architecture",
        "description": "NeRF neural network architecture"
    },
    "paper-dreamfusion-poole-2022.pdf": {
        "pages": [0, 4],  # Page 1 (results) and page 5 (Janus)
        "target_figure": "fig-dreamfusion",
        "description": "DreamFusion text-to-3D results and Janus problem"
    },
    "paper-chatdev-qian-2023.pdf": {
        "pages": [2, 3],  # Pages 3-4
        "target_figure": "fig-chatdev-architecture",
        "description": "ChatDev multi-agent workflow"
    }
}


def extract_images_from_pdf(pdf_path: Path, pages: list, output_prefix: str) -> list:
    """Extract all images from specified pages of a PDF."""
    extracted = []

    try:
        doc = fitz.open(pdf_path)
        print(f"\nProcessing: {pdf_path.name} ({len(doc)} pages)")

        for page_num in pages:
            if page_num >= len(doc):
                print(f"  Warning: Page {page_num + 1} doesn't exist (PDF has {len(doc)} pages)")
                continue

            page = doc[page_num]
            image_list = page.get_images()

            print(f"  Page {page_num + 1}: Found {len(image_list)} images")

            for img_idx, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                # Save image
                output_filename = f"{output_prefix}_p{page_num + 1}_img{img_idx + 1}.{image_ext}"
                output_path = OUTPUT_DIR / output_filename

                with open(output_path, "wb") as f:
                    f.write(image_bytes)

                extracted.append(output_path)
                print(f"    Saved: {output_filename} ({len(image_bytes)} bytes)")

        doc.close()

    except Exception as e:
        print(f"  Error: {e}")

    return extracted


def render_page_as_image(pdf_path: Path, page_num: int, output_prefix: str, dpi: int = 200) -> Path:
    """Render a full page as a high-resolution image."""
    try:
        doc = fitz.open(pdf_path)

        if page_num >= len(doc):
            print(f"  Warning: Page {page_num + 1} doesn't exist")
            return None

        page = doc[page_num]

        # Render at high DPI
        zoom = dpi / 72  # 72 is default PDF DPI
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        output_filename = f"{output_prefix}_p{page_num + 1}_full.png"
        output_path = OUTPUT_DIR / output_filename
        pix.save(output_path)

        print(f"  Rendered page {page_num + 1}: {output_filename} ({pix.width}x{pix.height})")
        doc.close()

        return output_path

    except Exception as e:
        print(f"  Error rendering page: {e}")
        return None


def main():
    """Main extraction routine."""
    print("=" * 60)
    print("Figure Extraction from Academic PDFs")
    print("=" * 60)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\nOutput directory: {OUTPUT_DIR}")

    all_extracted = []

    for pdf_name, config in PDF_CONFIGS.items():
        pdf_path = PDF_DIR / pdf_name

        if not pdf_path.exists():
            print(f"\n[SKIP] {pdf_name} not found")
            continue

        # Extract embedded images
        extracted = extract_images_from_pdf(
            pdf_path,
            config["pages"],
            config["target_figure"]
        )
        all_extracted.extend(extracted)

        # Also render full pages for manual cropping
        print(f"  Rendering full pages for manual cropping...")
        for page_num in config["pages"]:
            render_page_as_image(pdf_path, page_num, config["target_figure"])

    print("\n" + "=" * 60)
    print(f"Extraction complete! {len(all_extracted)} images extracted")
    print(f"Review images in: {OUTPUT_DIR}")
    print("\nNext steps:")
    print("1. Review extracted images")
    print("2. Identify the correct figure for each target")
    print("3. Copy/rename to final filenames (fig-*.png)")
    print("=" * 60)


if __name__ == "__main__":
    main()
