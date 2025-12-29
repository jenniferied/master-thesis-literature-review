# Figures Directory

This directory contains figures for the master thesis literature review.

## Directory Structure

```
figures/
├── ch-explainer/                    # AI/ML Foundations Explainer figures
│   ├── placeholders/                # Instructions for user-generated content
│   │   ├── comfyui-instructions.md  # ComfyUI screenshot guide (3 variations)
│   │   └── figure-extraction-guide.md # How to extract figures from PDFs
│   ├── paper-*.pdf                  # Downloaded source papers
│   └── fig-*.png                    # Extracted figures (to be created)
└── README.md                        # This file
```

## Source PDFs (Downloaded)

The following papers have been downloaded for figure extraction:

| Paper | File | arXiv ID |
|-------|------|----------|
| DDPM (Ho et al., 2020) | paper-ddpm-ho-2020.pdf | 2006.11239 |
| ControlNet (Zhang et al., 2023) | paper-controlnet-zhang-2023.pdf | 2302.05543 |
| NeRF (Mildenhall et al., 2020) | paper-nerf-mildenhall-2020.pdf | 2003.08934 |
| DreamFusion (Poole et al., 2022) | paper-dreamfusion-poole-2022.pdf | 2209.14988 |
| ChatDev (Qian et al., 2023) | paper-chatdev-qian-2023.pdf | 2307.07924 |

See `ch-explainer/placeholders/figure-extraction-guide.md` for extraction instructions.

## Figure Sources and Licenses

### Figures from Academic Papers (Open Access)

All academic figures are from arXiv preprints or open-access publications. They should be cited in figure captions using the format:

> Adapted from Author et al. (Year), "Paper Title."

| Figure | Source | License | Status |
|--------|--------|---------|--------|
| fig-diffusion-process.png | Ho et al. (2020), DDPM | arXiv (open access) | To extract |
| fig-controlnet-examples.png | Zhang et al. (2023), ControlNet | arXiv (open access) | To extract |
| fig-nerf-architecture.png | Mildenhall et al. (2020), NeRF | arXiv (open access) | To extract |
| fig-janus-problem.png | Poole et al. (2022), DreamFusion | arXiv (open access) | To extract |
| fig-chatdev-architecture.png | Qian et al. (2023), ChatDev | arXiv (open access) | To extract |

### User-Generated Figures

The following figures must be created by the thesis author:

1. **ComfyUI workflow screenshots** - Demonstrate node-based image generation
2. **Same seed comparison** - Show how same random seed with different prompts produces structurally similar but semantically different images
3. **ComfyUI 3D workflow** - If available, show 3D generation pipeline

See `ch-explainer/placeholders/` for detailed instructions.

## LaTeX Usage

```latex
\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{figures/ch-explainer/fig-diffusion-process.pdf}
\caption{The diffusion denoising process. Adapted from Ho et al. (2020).}
\label{fig:diffusion-process}
\end{figure}
```

## Adding New Figures

1. Place academic figures in the appropriate chapter subfolder
2. Use descriptive filenames with `fig-` prefix
3. Add entry to this README with source and license
4. Update the figure placeholder in the markdown document
5. Add proper caption with citation
