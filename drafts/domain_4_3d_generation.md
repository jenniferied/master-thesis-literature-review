# Domain 4: 3D Generation & Neural Rendering

## Overview

3D generation has evolved from neural radiance fields (NeRF) to real-time Gaussian splatting and text-to-3D synthesis. This domain covers scene representation, novel view synthesis, and generative 3D content creation.

**Thesis Relevance:** 3D asset generation is critical for indie game development. This domain addresses automated creation of characters, props, environments, and scene reconstruction.

**NOTE:** Some citation counts estimated. Verify with Google Scholar in future session.

---

## Paper Selection Methodology

Papers selected using tiered citation approach:
- **Tier 1 (>5,000 citations):** MUST include
- **Tier 2 (1,000-5,000 citations):** MUST include
- **Tier 3 (100-1,000 citations):** Include if venue is strong
- **Tier 4 (<100 citations):** Strong justification required

*Citation counts from Semantic Scholar/Web Search (December 2025)*

---

## Tier 1: Mega-Foundational Papers (>5,000 citations)

### Mildenhall, Srinivasan, Tancik, Barron, Ramamoorthi & Ng (2020) - "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"
**7,013 citations** | ECCV 2020 (Best Paper Honorable Mention)

The paper that launched neural scene representation:
- **Continuous 5D function:** (x, y, z, θ, φ) → (RGB, σ)
- **Volume rendering:** Differentiable ray marching
- **Novel view synthesis:** Generate views from any angle
- **Photorealistic quality:** State-of-the-art visual fidelity

*Thesis relevance:* NeRF enables capturing real-world objects/scenes as game assets. Foundation for all subsequent neural 3D work.

*Venue:* ECCV - Premier vision conference

---

### Kerbl, Kopanas, Leimkühler & Drettakis (2023) - "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
**~5,599 citations** | ACM Transactions on Graphics (SIGGRAPH 2023)

Real-time neural rendering breakthrough:
- **3D Gaussians:** Explicit scene representation (not implicit)
- **Real-time rendering:** ≥30 fps at 1080p
- **Fast training:** Minutes instead of hours
- **Game-ready:** Direct integration with rasterization pipelines

*Thesis relevance:* CRITICAL for games - first neural method achieving real-time rendering. Could enable AI-generated environments in real-time.

*Venue:* ACM TOG/SIGGRAPH - Premier graphics venue

---

## Tier 2: Major Foundational Papers (1,000-5,000 citations)

### Poole, Jain, Barron & Mildenhall (2022) - "DreamFusion: Text-to-3D using 2D Diffusion"
**2,962 citations** | ICLR 2023

Text-to-3D without 3D training data:
- **Score Distillation Sampling (SDS):** Use 2D diffusion as 3D prior
- **NeRF optimization:** Generate 3D from text prompts
- **No 3D supervision:** Leverages pretrained image diffusion
- **Janus problem:** Multi-face issue from lack of 3D awareness

*Thesis relevance:* Generate 3D assets from text descriptions - revolutionary for asset creation.

---

### Müller, Evans, Schied & Keller (2022) - "Instant Neural Graphics Primitives with a Multiresolution Hash Encoding"
**~2,500 citations** | ACM TOG (SIGGRAPH 2022 Best Paper)

Massive speedup for neural graphics:
- **Multiresolution hash encoding:** Trainable feature grids
- **Seconds not hours:** NeRF training in seconds
- **Small networks:** Efficient inference
- **Versatile:** Works for NeRF, SDF, images, neural textures

*Thesis relevance:* Makes neural 3D practical for iteration-heavy game development workflows.

*Venue:* SIGGRAPH Best Paper - Highest graphics honor

---

### Lin, Gao, Tang et al. (2023) - "Magic3D: High-Resolution Text-to-3D Content Creation"
**~1,500 citations** | CVPR 2023 (Highlight)

Improved text-to-3D quality:
- **Two-stage optimization:** Coarse NeRF → fine mesh
- **8x higher resolution:** Than DreamFusion
- **2x faster:** 40 minutes vs 1.5 hours
- **Mesh output:** Export-ready for game engines

*Thesis relevance:* Higher quality text-to-3D with game-ready mesh output.

*Venue:* CVPR Highlight - Top vision paper

---

## Tier 3: Field-Defining Papers (100-1,000 citations)

### Gao, Shen, Wang et al. (2022) - "GET3D: A Generative Model of High Quality 3D Textured Shapes Learned from Images"
**~800 citations** | NeurIPS 2022

Generative 3D with textures:
- **Textured meshes:** Direct mesh + texture generation
- **Learned from images:** No 3D supervision needed
- **Diverse categories:** Cars, chairs, characters, buildings
- **Differentiable rendering:** End-to-end trainable

*Thesis relevance:* Generate textured game assets directly - characters, vehicles, props.

*Venue:* NeurIPS - Premier ML conference

---

### Nichol, Jun, Dhariwal, Mishkin & Chen (2022) - "Point-E: A System for Generating 3D Point Clouds from Complex Prompts"
**~600 citations** | arXiv (OpenAI)

Fast text-to-3D:
- **Point cloud diffusion:** Generate 3D as point clouds
- **Minutes not hours:** 1-2 minutes per object
- **Two-stage:** Text→image→3D
- **Practical tradeoff:** Speed over quality

*Thesis relevance:* Rapid prototyping of 3D concepts from text.

---

### Jun & Nichol (2023) - "Shap-E: Generating Conditional 3D Implicit Functions"
**~500 citations** | arXiv (OpenAI)

Improved Point-E:
- **Implicit functions:** NeRF + mesh output
- **Faster convergence:** Better than Point-E
- **Higher quality:** Multi-representation output
- **Open source:** Available for research

*Thesis relevance:* OpenAI's latest text-to-3D, open for experimentation.

---

## Evolution of the Field

```
2020: NeRF - Neural scene representation
   ↓
2021: NeRF variants (Mip-NeRF, NSVF, etc.)
   ↓
2022: Instant-NGP - Fast training
      DreamFusion - Text-to-3D
      GET3D - Generative meshes
   ↓
2023: 3D Gaussian Splatting - Real-time rendering
      Magic3D - High-res text-to-3D
   ↓
2024+: Gaussian splatting variants, video-to-4D
```

---

## Key Concepts for Thesis

| Concept | Paper | Application |
|---------|-------|-------------|
| **Neural radiance fields** | Mildenhall NeRF | Scene capture and novel views |
| **Gaussian splatting** | Kerbl 3DGS | Real-time neural rendering |
| **Score distillation** | Poole DreamFusion | Text-to-3D generation |
| **Hash encoding** | Müller Instant-NGP | Fast neural training |
| **Generative meshes** | Gao GET3D | Direct mesh generation |

---

## Practical Implications for Relics

| Task | Recommended Approach | Key Papers |
|------|---------------------|------------|
| **Environment capture** | Gaussian Splatting | Kerbl 2023 |
| **Asset from text** | Magic3D / DreamFusion | Lin, Poole |
| **Rapid prototyping** | Point-E / Shap-E | Nichol 2022-23 |
| **Character generation** | GET3D + refinement | Gao 2022 |
| **Scene reconstruction** | Instant-NGP | Müller 2022 |

---

## Game Engine Integration Notes

| Method | Real-time? | Export Format | Engine Support |
|--------|-----------|---------------|----------------|
| **NeRF** | No | Custom | Limited |
| **3DGS** | Yes | Splats/Mesh | Growing (UE5 plugins) |
| **DreamFusion** | No (generation) | NeRF→Mesh | Post-export |
| **GET3D** | Yes (output) | Mesh+Texture | Native |
| **Instant-NGP** | Near-real-time | Custom | Limited |

---

## Summary: Papers by Tier

| Tier | Count | Papers |
|------|-------|--------|
| **Tier 1** | 2 | NeRF, 3D Gaussian Splatting |
| **Tier 2** | 3 | DreamFusion, Instant-NGP, Magic3D |
| **Tier 3** | 3 | GET3D, Point-E, Shap-E |
| **Total** | 8 | |

---

## BibTeX

See `data/exports/domain_4.bib` for full citations.

## Sources

- [NeRF Project Page](https://www.matthewtancik.com/nerf)
- [3D Gaussian Splatting](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)
- [DreamFusion](https://dreamfusion3d.github.io/)
- [Instant-NGP](https://nvlabs.github.io/instant-ngp/)
- [GET3D](https://nv-tlabs.github.io/GET3D/)
