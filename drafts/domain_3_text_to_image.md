# Domain 3: Text-to-Image Generation

## Overview

Text-to-image generation has undergone a revolution with diffusion models, enabling photorealistic image synthesis from natural language descriptions. This domain covers the evolution from GANs to modern diffusion-based systems.

**Thesis Relevance:** Text-to-image models enable concept art generation, texture creation, and visual prototyping - critical for indie developers without dedicated art teams.

**NOTE:** Verify citation counts with Google Scholar in future session (rate limited during initial research).

---

## Paper Selection Methodology

Papers selected using tiered citation approach:
- **Tier 1 (>10,000 citations):** MUST include
- **Tier 2 (1,000-10,000 citations):** MUST include
- **Tier 3 (100-1,000 citations):** Include if venue is strong
- **Tier 4 (<100 citations):** Strong justification required

*Citation counts from Semantic Scholar/Web Search (December 2025)*

---

## Tier 1: Mega-Foundational Papers (>10,000 citations)

### Radford, Kim, Hallacy et al. (2021) - "Learning Transferable Visual Models From Natural Language Supervision" (CLIP)
**40,352 citations** | ICML 2021

Contrastive language-image pre-training:
- **400 million image-text pairs:** Massive web-scraped training data
- **Zero-shot transfer:** Classify images using natural language
- **Dual encoder:** Separate image and text encoders with shared embedding space
- **Foundation for text-to-image:** CLIP embeddings used in DALL-E, Stable Diffusion

*Thesis relevance:* CLIP enables text-guided image generation and editing. Foundation of most modern text-to-image systems.

*Venue:* ICML - Premier ML conference

---

### Ho, Jain & Abbeel (2020) - "Denoising Diffusion Probabilistic Models" (DDPM)
**24,884 citations** | NeurIPS 2020

The paper that launched the diffusion revolution:
- **Forward process:** Gradually add Gaussian noise to images
- **Reverse process:** Learn to denoise, generating images from noise
- **High-quality synthesis:** Achieved FID 3.17 on CIFAR-10
- **Theoretical foundation:** Connected to score matching and Langevin dynamics

*Thesis relevance:* THE foundational diffusion paper. All modern image generators (Stable Diffusion, DALL-E 2, Midjourney) build on this.

*Venue:* NeurIPS - Premier ML conference

---

### Rombach, Blattmann, Lorenz, Esser & Ommer (2022) - "High-Resolution Image Synthesis with Latent Diffusion Models"
**20,519 citations** | CVPR 2022 (Oral)

Stable Diffusion's foundation:
- **Latent space diffusion:** Operate in compressed latent space, not pixels
- **Computational efficiency:** 10-100x faster than pixel-space diffusion
- **Cross-attention conditioning:** Flexible text/image conditioning
- **Open source:** Enabled Stable Diffusion ecosystem

*Thesis relevance:* THE practical text-to-image paper. Stable Diffusion enables indie developers to generate art locally.

*Venue:* CVPR - Premier vision conference

---

### Karras, Laine & Aila (2019) - "A Style-Based Generator Architecture for Generative Adversarial Networks" (StyleGAN)
**~15,000 citations** | CVPR 2019

Pre-diffusion state-of-the-art in image generation:
- **Style-based synthesis:** Control generation at different scales
- **W latent space:** More disentangled than standard GAN latents
- **High-resolution faces:** Photorealistic 1024x1024 faces
- **Latent manipulation:** Meaningful edits in latent space

*Thesis relevance:* GAN baseline for understanding diffusion improvements. StyleGAN concepts (latent spaces, style mixing) inform diffusion work.

*Venue:* CVPR - Premier vision conference

---

## Tier 2: Major Foundational Papers (1,000-10,000 citations)

### Ramesh, Dhariwal, Nichol, Chu & Chen (2022) - "Hierarchical Text-Conditional Image Generation with CLIP Latents" (DALL-E 2)
**8,178 citations** | arXiv

OpenAI's flagship text-to-image system:
- **CLIP + Diffusion:** Two-stage: prior generates CLIP embedding, decoder generates image
- **High photorealism:** State-of-the-art image quality
- **Image variations:** Generate variations preserving semantics/style
- **Language-guided manipulation:** Zero-shot editing

*Thesis relevance:* Demonstrated commercial viability of text-to-image for creative professionals.

---

### Saharia, Chan, Saxena et al. (2022) - "Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding" (Imagen)
**6,515 citations** | NeurIPS 2022

Google's text-to-image with emphasis on language:
- **T5 text encoder:** Large language model for text understanding
- **Cascaded diffusion:** Progressive upsampling for high resolution
- **DrawBench benchmark:** New evaluation framework
- **Finding:** Scaling language model helps more than scaling image model

*Thesis relevance:* Showed importance of language understanding in text-to-image - relevant for complex worldbuilding prompts.

*Venue:* NeurIPS - Premier ML conference

---

### Zhang, Rao & Agrawala (2023) - "Adding Conditional Control to Text-to-Image Diffusion Models" (ControlNet)
**5,390 citations** | ICCV 2023

Spatial control over diffusion generation:
- **Zero convolutions:** Add control without destroying pre-trained weights
- **Multiple conditions:** Edges, depth, pose, segmentation maps
- **Training efficiency:** Only train control network, freeze main model
- **Composable:** Multiple controls can be combined

*Thesis relevance:* Critical for game art - generate assets matching specific layouts, poses, or scene structures.

*Venue:* ICCV - Premier vision conference

---

### Ho & Salimans (2022) - "Classifier-Free Diffusion Guidance"
**~4,000 citations** | NeurIPS 2022 Workshop

Improved text-image alignment:
- **No separate classifier:** Joint training of conditional and unconditional models
- **Guidance scale:** Trade off between fidelity and diversity
- **Foundation technique:** Used in virtually all modern text-to-image systems
- **Simpler training:** No need for separate classifier

*Thesis relevance:* Explains the "CFG scale" parameter in Stable Diffusion - essential for controlling generation.

---

### Podell, English, Lacey et al. (2023) - "SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis"
**3,665 citations** | ICLR 2024

Stable Diffusion XL improvements:
- **Larger UNet:** 3x more parameters than SD 1.5
- **Dual text encoders:** CLIP + OpenCLIP for better text understanding
- **Multiple aspect ratios:** Native training on various dimensions
- **Refinement model:** Post-hoc quality enhancement

*Thesis relevance:* Current practical standard for open-source text-to-image generation.

---

## Tier 3: Field-Defining Papers (100-1,000 citations)

### Nichol & Dhariwal (2021) - "Improved Denoising Diffusion Probabilistic Models"
**~3,000 citations** | ICML 2021

Key improvements to DDPM:
- **Learned variance:** Better likelihood estimation
- **Cosine noise schedule:** More stable training
- **Faster sampling:** Fewer steps needed for generation

*Thesis relevance:* Technical improvements enabling practical diffusion models.

---

## Evolution of the Field

```
2014-2018: GAN Era (StyleGAN peak)
    ↓
2020: DDPM - Diffusion models competitive with GANs
    ↓
2021: CLIP - Vision-language foundation
    ↓
2022: DALL-E 2, Imagen, Stable Diffusion - Text-to-image revolution
    ↓
2023: ControlNet, SDXL - Control and quality improvements
    ↓
2024+: Flux, SD3 - Continued refinement
```

---

## Key Concepts for Thesis

| Concept | Paper | Application |
|---------|-------|-------------|
| **Diffusion** | Ho DDPM | Iterative denoising for generation |
| **Latent diffusion** | Rombach LDM | Efficient high-res generation |
| **CLIP conditioning** | Radford CLIP | Text-guided generation |
| **Classifier-free guidance** | Ho CFG | Control fidelity vs diversity |
| **ControlNet** | Zhang | Spatial control over generation |
| **Style-based synthesis** | Karras StyleGAN | Controllable generation |

---

## Practical Implications for Relics

| Task | Recommended Approach | Key Papers |
|------|---------------------|------------|
| **Concept art** | SDXL + ControlNet | Podell, Zhang |
| **Texture generation** | Stable Diffusion tiling | Rombach LDM |
| **Character design** | SDXL with pose control | SDXL + ControlNet |
| **Environment concepts** | Img2img workflows | LDM + ControlNet |
| **UI/Icon design** | Fine-tuned models | LDM, ControlNet |

---

## Summary: Papers by Tier

| Tier | Count | Papers |
|------|-------|--------|
| **Tier 1** | 4 | CLIP, DDPM, Latent Diffusion, StyleGAN |
| **Tier 2** | 5 | DALL-E 2, Imagen, ControlNet, CFG, SDXL |
| **Tier 3** | 1 | Improved DDPM |
| **Total** | 10 | |

---

## BibTeX

See `data/exports/domain_3.bib` for full citations.

## Sources

- [CLIP - arXiv](https://arxiv.org/abs/2103.00020)
- [DDPM - NeurIPS](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)
- [Latent Diffusion - CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html)
- [ControlNet - ICCV](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html)
