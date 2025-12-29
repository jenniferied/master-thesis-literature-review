# Figure Extraction Guide

The source PDFs have been downloaded. This guide explains how to extract the specific figures needed for the AI/ML Foundations Explainer.

## Downloaded Papers

| Paper | File | Size |
|-------|------|------|
| DDPM (Ho et al., 2020) | paper-ddpm-ho-2020.pdf | 10.3 MB |
| ControlNet (Zhang et al., 2023) | paper-controlnet-zhang-2023.pdf | 16.3 MB |
| NeRF (Mildenhall et al., 2020) | paper-nerf-mildenhall-2020.pdf | 8.3 MB |
| DreamFusion (Poole et al., 2022) | paper-dreamfusion-poole-2022.pdf | 11.0 MB |
| ChatDev (Qian et al., 2023) | paper-chatdev-qian-2023.pdf | 3.5 MB |

## Figures to Extract

### 1. Diffusion Process (DDPM)

**Source:** paper-ddpm-ho-2020.pdf
**Figure:** Figure 2 (page 3) - The forward and reverse diffusion process
**Save as:** `fig-diffusion-process.png`
**Caption:** "The diffusion process adds noise gradually (forward) and learns to remove it (reverse). Adapted from Ho et al. (2020)."

### 2. ControlNet Examples

**Source:** paper-controlnet-zhang-2023.pdf
**Figure:** Figure 1 (page 1) or Figure 3 (page 4) - Shows input conditions and outputs
**Save as:** `fig-controlnet-examples.png`
**Caption:** "ControlNet enables spatial control through edge maps, depth maps, and pose skeletons. Adapted from Zhang et al. (2023)."

### 3. NeRF Architecture

**Source:** paper-nerf-mildenhall-2020.pdf
**Figure:** Figure 2 (page 4) - The neural network architecture
**Save as:** `fig-nerf-architecture.png`
**Caption:** "NeRF represents scenes as continuous functions mapping 3D coordinates to color and density. Adapted from Mildenhall et al. (2020)."

### 4. NeRF Results (Novel View Synthesis)

**Source:** paper-nerf-mildenhall-2020.pdf
**Figure:** Figure 4 or 5 - Comparison of rendered views
**Save as:** `fig-nerf-results.png`
**Caption:** "NeRF produces photorealistic novel views from learned scene representations. Adapted from Mildenhall et al. (2020)."

### 5. DreamFusion/Janus Problem

**Source:** paper-dreamfusion-poole-2022.pdf
**Figure:** Figure 3 (page 5) or supplementary - Shows multi-view inconsistency
**Save as:** `fig-janus-problem.png`
**Caption:** "The Janus problem: text-to-3D models may generate faces on multiple sides of an object. Adapted from Poole et al. (2022)."

### 6. DreamFusion Results

**Source:** paper-dreamfusion-poole-2022.pdf
**Figure:** Figure 1 (page 1) - Example 3D generations from text
**Save as:** `fig-dreamfusion-results.png`
**Caption:** "DreamFusion generates 3D objects from text prompts using 2D diffusion guidance. Adapted from Poole et al. (2022)."

### 7. ChatDev Architecture

**Source:** paper-chatdev-qian-2023.pdf
**Figure:** Figure 2 (page 3-4) - The multi-agent workflow
**Save as:** `fig-chatdev-architecture.png`
**Caption:** "ChatDev simulates a software company with specialized AI agents collaborating to produce code. Adapted from Qian et al. (2023)."

## Extraction Methods

### Method 1: Screenshot (Recommended for Quality)

1. Open PDF in Preview (macOS) or your preferred viewer
2. Zoom to 200-300% for high resolution
3. Use screenshot tool (Cmd+Shift+4 on macOS)
4. Crop tightly around the figure
5. Save as PNG

### Method 2: PDF Export (macOS Preview)

1. Open PDF in Preview
2. Go to File → Export
3. Select PNG format
4. Export the page containing the figure
5. Crop in an image editor

### Method 3: Poppler Tools (if installed)

```bash
# Install poppler (macOS)
brew install poppler

# Extract all images from a PDF
pdfimages -png paper-ddpm-ho-2020.pdf ddpm-

# Convert specific page to PNG
pdftoppm -png -f 3 -l 3 -r 300 paper-ddpm-ho-2020.pdf ddpm-page3
```

### Method 4: Online Tools

- [PDF24 Tools](https://tools.pdf24.org/en/extract-images)
- [iLovePDF](https://www.ilovepdf.com/pdf_to_jpg)

## Quality Guidelines

| Requirement | Specification |
|-------------|---------------|
| Minimum resolution | 300 DPI or 1920px wide |
| Format | PNG (lossless) preferred |
| Background | White or transparent |
| Cropping | Tight crop, include caption if helpful |

## After Extraction

1. Save extracted figures in `figures/ch-explainer/`
2. Update `figures/README.md` with actual file entries
3. Replace placeholders in `ai_ml_foundations_explainer.md`
4. Test in LaTeX build pipeline

## File Checklist

- [ ] fig-diffusion-process.png
- [ ] fig-controlnet-examples.png
- [ ] fig-nerf-architecture.png
- [ ] fig-nerf-results.png (optional)
- [ ] fig-janus-problem.png
- [ ] fig-dreamfusion-results.png (optional)
- [ ] fig-chatdev-architecture.png
- [ ] comfyui-workflow-txt2img.png (user-generated)
- [ ] comfyui-workflow-controlnet.png (user-generated)
- [ ] comfyui-workflow-lora.png (user-generated)
