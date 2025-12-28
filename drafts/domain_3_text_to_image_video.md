# Domain 3: Text-to-Image and Video Generation

## Overview

Text-to-image and video generation has undergone a revolution with diffusion models, enabling photorealistic synthesis from natural language descriptions. This domain covers the evolution from GANs to modern diffusion-based systems, **style consistency techniques** for maintaining visual coherence across generations, and the emerging field of **text-to-video generation**.

**Thesis Relevance:** Text-to-image models enable concept art generation, texture creation, and visual prototyping. Style consistency techniques (LoRA, DreamBooth) are critical for maintaining character and asset consistency across a game's visual identity. Text-to-video opens possibilities for cinematic content and animation reference.

---

## Paper Selection Methodology

Papers selected using tiered citation approach:
- **Tier 1 (>10,000 citations):** MUST include
- **Tier 2 (1,000-10,000 citations):** MUST include
- **Tier 3 (100-1,000 citations):** Include if venue is strong
- **Tier 4 (<100 citations):** Strong justification required (recent/highly relevant)

*Citation counts from Semantic Scholar/Google Scholar (December 2025)*

---

## Section A: Foundation Papers (Text-to-Image)

### Tier 1: Mega-Foundational Papers (>10,000 citations)

#### Radford, Kim, Hallacy et al. (2021) - "Learning Transferable Visual Models From Natural Language Supervision" (CLIP)
**~40,000 citations** | ICML 2021

Contrastive language-image pre-training:
- **400 million image-text pairs:** Massive web-scraped training data
- **Zero-shot transfer:** Classify images using natural language
- **Dual encoder:** Separate image and text encoders with shared embedding space
- **Foundation for text-to-image:** CLIP embeddings used in DALL-E, Stable Diffusion

*Thesis relevance:* CLIP enables text-guided image generation and editing. Foundation of most modern text-to-image systems.

---

#### Ho, Jain & Abbeel (2020) - "Denoising Diffusion Probabilistic Models" (DDPM)
**~25,000 citations** | NeurIPS 2020

The paper that launched the diffusion revolution:
- **Forward process:** Gradually add Gaussian noise to images
- **Reverse process:** Learn to denoise, generating images from noise
- **High-quality synthesis:** Achieved FID 3.17 on CIFAR-10
- **Theoretical foundation:** Connected to score matching and Langevin dynamics

*Thesis relevance:* THE foundational diffusion paper. All modern image generators build on this.

---

#### Rombach, Blattmann, Lorenz, Esser & Ommer (2022) - "High-Resolution Image Synthesis with Latent Diffusion Models"
**~20,000 citations** | CVPR 2022 (Oral)

Stable Diffusion's foundation:
- **Latent space diffusion:** Operate in compressed latent space, not pixels
- **Computational efficiency:** 10-100x faster than pixel-space diffusion
- **Cross-attention conditioning:** Flexible text/image conditioning
- **Open source:** Enabled Stable Diffusion ecosystem

*Thesis relevance:* THE practical text-to-image paper. Enables indie developers to generate art locally.

---

#### Karras, Laine & Aila (2019) - "A Style-Based Generator Architecture for Generative Adversarial Networks" (StyleGAN)
**~15,000 citations** | CVPR 2019

Pre-diffusion state-of-the-art:
- **Style-based synthesis:** Control generation at different scales
- **W latent space:** More disentangled than standard GAN latents
- **High-resolution faces:** Photorealistic 1024x1024 faces

*Thesis relevance:* GAN baseline and concepts (style mixing) inform diffusion work.

---

### Tier 2: Major Foundational Papers (1,000-10,000 citations)

#### Ramesh et al. (2022) - "Hierarchical Text-Conditional Image Generation with CLIP Latents" (DALL-E 2)
**~8,000 citations** | arXiv

OpenAI's flagship text-to-image:
- **CLIP + Diffusion:** Two-stage generation
- **High photorealism:** State-of-the-art image quality
- **Language-guided manipulation:** Zero-shot editing

---

#### Saharia et al. (2022) - "Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding" (Imagen)
**~6,500 citations** | NeurIPS 2022

Google's emphasis on language understanding:
- **T5 text encoder:** Large language model for text understanding
- **Cascaded diffusion:** Progressive upsampling
- **Finding:** Scaling language model helps more than scaling image model

---

#### Zhang, Rao & Agrawala (2023) - "Adding Conditional Control to Text-to-Image Diffusion Models" (ControlNet)
**~5,400 citations** | ICCV 2023

Spatial control over generation:
- **Zero convolutions:** Add control without destroying pre-trained weights
- **Multiple conditions:** Edges, depth, pose, segmentation maps
- **Composable:** Multiple controls can be combined

*Thesis relevance:* Critical for game art - generate assets matching specific layouts.

---

#### Podell et al. (2023) - "SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis"
**~3,700 citations** | ICLR 2024

Stable Diffusion XL improvements:
- **Larger UNet:** 3x more parameters than SD 1.5
- **Dual text encoders:** CLIP + OpenCLIP
- **Multiple aspect ratios:** Native training on various dimensions

---

## Section B: Style Consistency & Personalization

This section covers techniques for maintaining visual consistency across generated images - **critical for game development** where characters, environments, and assets must maintain coherent style.

### Hu et al. (2021) - "LoRA: Low-Rank Adaptation of Large Language Models"
**~15,000 citations** | ICLR 2022

Efficient fine-tuning method (adapted for diffusion):
- **Low-rank matrices:** Inject trainable matrices into frozen model
- **Parameter efficiency:** 10,000x fewer trainable parameters than full fine-tuning
- **No inference overhead:** Merged with base weights at deployment
- **Diffusion adaptation:** Widely used for Stable Diffusion character/style consistency

*Thesis relevance:* CRITICAL - Train consistent characters, environments, and art styles with minimal data (5-20 images). Essential for maintaining visual coherence in Relics.

---

### Ruiz et al. (2022) - "DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation"
**~3,500 citations** | CVPR 2023

Subject-specific personalization:
- **Few-shot learning:** 3-5 images to capture a subject
- **Prior preservation loss:** Prevents forgetting general knowledge
- **Novel contexts:** Place learned subjects in new scenes
- **Identity preservation:** Maintains key subject features

*Thesis relevance:* Train on specific character designs, then generate that character in diverse poses/scenes. Essential for consistent NPCs and protagonist.

---

### Gal et al. (2022) - "An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion"
**~2,000 citations** | ICLR 2023

Learning concepts as embeddings:
- **Pseudo-word:** Learn new "word" in embedding space
- **Frozen model:** No model weights modified
- **Composable:** Combine multiple learned concepts
- **Lightweight:** Only store small embedding vector

*Thesis relevance:* Capture unique concepts (architectural styles, creature designs) as reusable tokens.

---

### Ye et al. (2023) - "IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models"
**~500 citations** | Tencent AI Lab

Image-guided generation:
- **Decoupled cross-attention:** Separate text and image features
- **22M parameters:** Lightweight adapter
- **ControlNet compatible:** Works with existing tools
- **Style transfer:** Use reference image for consistent style

*Thesis relevance:* Use reference images to maintain style consistency without training.

---

### ConsisLoRA / Style Consistency Methods (2024)
**Recent** | Various venues

Emerging work on multi-image consistency:
- **Character consistency:** Same character across multiple generations
- **Scene consistency:** Coherent environments
- **Cross-image attention:** Share features between generations

*Thesis relevance:* Active research area directly addressing game asset consistency.

---

## Section C: Text-to-Video Generation

The frontier of generative media - transforming text into moving images.

### Singer et al. (2022) - "Make-A-Video: Text-to-Video Generation without Text-Video Data"
**~1,500 citations** | Meta AI

Pioneering text-to-video:
- **No text-video pairs needed:** Leverage text-image data + unsupervised video
- **Spatiotemporal decomposition:** Separate spatial and temporal learning
- **High resolution:** Up to 768x768 video output
- **Super-resolution:** Cascaded model for quality

*Thesis relevance:* Foundation for understanding video generation capabilities.

---

### OpenAI Sora (2024)
**Technical Report** | OpenAI

State-of-the-art video generation:
- **Diffusion transformer:** Spacetime patches as tokens
- **60+ seconds:** Long-form coherent video
- **World simulation:** Physical understanding of scenes
- **Multi-character:** Complex scene composition

*Thesis relevance:* Represents the frontier - potential for cutscene generation, animation reference.

---

### Runway Gen-2 (2023)
**Commercial System** | Runway ML

Practical text-to-video:
- **Multimodal input:** Text, image, or video conditioning
- **4-16 second clips:** Practical output lengths
- **Style transfer:** Apply styles to video
- **Accessible:** Commercial availability

*Thesis relevance:* Currently usable tool for indie developers.

---

### Blattmann et al. (2023) - "Stable Video Diffusion: Scaling Latent Video Diffusion Models"
**~800 citations** | Stability AI

Open-source video diffusion:
- **Image-to-video:** Strong image conditioning
- **14-25 frames:** Short clip generation
- **SVD-XT:** Extended temporal model
- **Open weights:** Available for experimentation

*Thesis relevance:* Open-source option for video generation experimentation.

---

### Ho et al. (2022) - "Video Diffusion Models"
**~1,200 citations** | NeurIPS 2022

Foundational video diffusion:
- **3D U-Net:** Space-time factorized architecture
- **Gradient-guided:** Reconstruction guidance
- **Unconditional/conditional:** Both modes supported

*Thesis relevance:* Technical foundation for understanding video diffusion.

---

## Evolution of the Field

```
2014-2018: GAN Era (StyleGAN peak)
    ↓
2020: DDPM - Diffusion models competitive with GANs
    ↓
2021: CLIP - Vision-language foundation
      LoRA - Efficient fine-tuning
    ↓
2022: DALL-E 2, Imagen, Stable Diffusion - Text-to-image revolution
      DreamBooth, Textual Inversion - Personalization
      Make-A-Video - Text-to-video emerges
    ↓
2023: ControlNet, SDXL - Control and quality improvements
      Gen-2, SVD - Practical video generation
      IP-Adapter - Image-guided generation
    ↓
2024: Sora - Long-form video
      Flux - Next-gen image models
      ConsisLoRA - Multi-image consistency
    ↓
2025+: Real-time generation, game integration
```

---

## Key Concepts for Thesis

| Concept | Paper | Application |
|---------|-------|-------------|
| **Diffusion** | Ho DDPM | Iterative denoising for generation |
| **Latent diffusion** | Rombach LDM | Efficient high-res generation |
| **CLIP conditioning** | Radford CLIP | Text-guided generation |
| **ControlNet** | Zhang | Spatial control over generation |
| **LoRA** | Hu | Efficient style/character fine-tuning |
| **DreamBooth** | Ruiz | Subject-specific personalization |
| **Textual Inversion** | Gal | Concept learning as embeddings |
| **IP-Adapter** | Ye | Image-guided consistency |
| **Video Diffusion** | Ho/Singer | Temporal extension of diffusion |

---

## Practical Implications for Relics

| Task | Recommended Approach | Key Papers |
|------|---------------------|------------|
| **Concept art** | SDXL + ControlNet | Podell, Zhang |
| **Texture generation** | Stable Diffusion tiling | Rombach LDM |
| **Character consistency** | LoRA + DreamBooth | Hu, Ruiz |
| **Environment style** | IP-Adapter + style reference | Ye |
| **NPC portraits** | Fine-tuned model per race/faction | DreamBooth |
| **Cutscene storyboards** | Gen-2 / SVD | Runway, Blattmann |
| **Animation reference** | Sora / video models | OpenAI |
| **UI/Icon design** | Fine-tuned SDXL | Various |

---

## Style Consistency Workflow for RPG Development

```
1. DEFINE VISUAL STYLE
   Reference art → IP-Adapter / style extraction

2. TRAIN BASE MODELS
   Character races → DreamBooth per race
   Architecture → LoRA for building styles
   Creatures → DreamBooth per creature type

3. GENERATE ASSETS
   Controlled generation → ControlNet + LoRA
   Batch consistency → Same seed + style LoRA

4. ITERATE
   Refine → Inpainting + ControlNet
   Upscale → Tile-based super-resolution
```

---

## Summary: Papers by Category

| Category | Count | Papers |
|----------|-------|--------|
| **Foundation (T1)** | 4 | CLIP, DDPM, LDM, StyleGAN |
| **Text-to-Image (T2)** | 4 | DALL-E 2, Imagen, ControlNet, SDXL |
| **Style Consistency** | 4 | LoRA, DreamBooth, Textual Inversion, IP-Adapter |
| **Text-to-Video** | 5 | Make-A-Video, Sora, Gen-2, SVD, Video Diffusion |
| **Total** | 17 | |

---

## BibTeX

See `data/exports/domain_3.bib` for full citations.

## Sources

- [CLIP - arXiv](https://arxiv.org/abs/2103.00020)
- [Latent Diffusion - CVPR](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html)
- [ControlNet - ICCV](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html)
- [LoRA - ICLR](https://openreview.net/forum?id=nZeVKeeFYf9)
- [DreamBooth - CVPR](https://openaccess.thecvf.com/content/CVPR2023/papers/Ruiz_DreamBooth_Fine_Tuning_Text-to-Image_Diffusion_Models_for_Subject-Driven_Generation_CVPR_2023_paper.pdf)
- [Textual Inversion - arXiv](https://arxiv.org/abs/2208.01618)
- [IP-Adapter - GitHub](https://github.com/tencent-ailab/IP-Adapter)
- [Sora - OpenAI](https://openai.com/sora)
- [Stable Video Diffusion - Stability AI](https://stability.ai/stable-video)
