# Domain 6: Generative Interactive Worlds

## Overview

Generative interactive worlds represent the frontier of AI-assisted game development: fully neural environments that can be played in real-time. This domain covers world models for reinforcement learning, neural game engines, and video generation as world simulation.

**Thesis Relevance:** This is the most directly relevant domain for the Relics project. These papers explore whether AI can generate entire playable game worlds, addressing the central thesis question of restoring the creator-to-creation ratio.

**NOTE:** Some citation counts estimated. Verify with Google Scholar when rate limit resets.

---

## Paper Selection Methodology

Papers selected using tiered citation approach:
- **Tier 1 (>1,000 citations):** MUST include
- **Tier 2 (100-1,000 citations):** MUST include if venue is strong
- **Tier 3 (<100 citations):** Strong justification required (recent/frontier work)

*Citation counts from Semantic Scholar/Web Search (December 2025)*

---

## Tier 1: Foundational Papers (>1,000 citations)

### Ha & Schmidhuber (2018) - "World Models"
**1,290 citations** | NeurIPS 2018

The foundational paper on neural world models:
- **VAE + RNN + Controller:** Three-component architecture
- **Dream training:** Train agents entirely in hallucinated environments
- **Compressed representation:** Learn spatial and temporal features
- **Transfer to reality:** Policies trained in dreams work in real environments

*Thesis relevance:* Foundational concept - can we train game content generators in "world model" space?

*Venue:* NeurIPS - Premier ML conference

---

### van den Oord, Vinyals & Kavukcuoglu (2017) - "Neural Discrete Representation Learning" (VQ-VAE)
**~1,963 citations** | NeurIPS 2017

Foundation for discrete neural representations:
- **Vector quantization:** Discrete latent codes instead of continuous
- **Learned prior:** Prior distribution is learned, not fixed
- **No posterior collapse:** Avoids common VAE failure mode
- **Multi-modal:** Works for images, audio, video

*Thesis relevance:* VQ-VAE underpins modern world models (IRIS, Oasis) that tokenize game frames for prediction.

*Venue:* NeurIPS - Premier ML conference

---

## Tier 2: Major Recent Papers (100-1,000 citations)

### Hafner, Pasukonis, Ba & Lillicrap (2023) - "DreamerV3: Mastering Diverse Domains through World Models"
**792 citations** | arXiv → Nature 2025

State-of-the-art world model for RL:
- **Single configuration:** Works across 150+ diverse tasks
- **Robust techniques:** Normalization, balancing, transformations
- **Minecraft diamonds:** First algorithm to achieve this from scratch
- **Imagined rollouts:** Train policy entirely in world model

*Thesis relevance:* Shows world models can handle complex open-world games like Minecraft - directly relevant to Relics.

*Venue:* Published in Nature (2025) - Highest scientific prestige

---

### Bruce, Dennis, Edwards et al. (2024) - "Genie: Generative Interactive Environments"
**~341 citations** | ICML 2024

First foundation world model:
- **11B parameters:** Largest generative world model
- **Unsupervised from video:** No action labels needed
- **Multiple input modalities:** Text, images, sketches
- **Latent action model:** Discovers actions from video

*Thesis relevance:* CRITICAL - shows AI can generate playable 2D worlds from single images. Direct path to AI-assisted worldbuilding.

*Venue:* ICML - Premier ML conference

---

### Valevski, Leviathan, Arar & Fruchter (2024) - "Diffusion Models Are Real-Time Game Engines" (GameNGen)
**~152 citations** | arXiv (Google Research/DeepMind)

Neural game engine playing DOOM:
- **20 FPS on TPU:** Real-time neural rendering
- **Stable long trajectories:** Multi-minute play sessions
- **PSNR 29.4:** Quality comparable to JPEG compression
- **Two-phase training:** RL agent → diffusion model

*Thesis relevance:* Proof-of-concept that complex games can run entirely on neural networks. Paradigm shift potential.

---

### Kim, Zhou, Philion, Torralba & Fidler (2020) - "Learning to Simulate Dynamic Environments with GameGAN"
**~400 citations** | CVPR 2020

GAN-based game simulator:
- **Pac-Man recreation:** Learns game rules from observation
- **Dynamics engine:** Maintains internal state
- **Memory module:** Remembers generated content
- **No game code:** Pure neural simulation

*Thesis relevance:* Early proof that GANs can learn game mechanics - precursor to diffusion-based approaches.

*Venue:* CVPR - Premier vision conference

---

### Micheli, Alonso & Fleuret (2023) - "Transformers are Sample-Efficient World Models" (IRIS)
**~117 citations** | ICLR 2023 (Notable Top 5%)

Transformer-based world model:
- **Discrete tokenization:** VQ-VAE + autoregressive transformer
- **Sample efficiency:** Only 2 hours of gameplay
- **Superhuman:** Outperforms humans on 10/26 Atari games
- **Pixel-perfect:** Accurate game predictions

*Thesis relevance:* Shows transformers can efficiently learn game dynamics - architecturally relevant for PCG.

*Venue:* ICLR Notable Top 5% - Exceptional recognition

---

## Tier 3: Frontier Work (<100 citations, justified)

### Decart (2024) - "Oasis: Real-Time AI Game Generation"
**Technical Report** | Industry (Decart/Etched)

Real-time Minecraft generation:
- **20 FPS real-time:** Playable open-world generation
- **DiT architecture:** Spatial autoencoder + diffusion backbone
- **Dynamic noising:** Solves temporal stability
- **100x faster than Sora:** Optimized for interaction

*Justification:* Most directly relevant to thesis - demonstrates AI generating Minecraft-like worlds in real-time. Industry breakthrough.

*Thesis relevance:* CRITICAL - if Oasis works for Minecraft, similar approaches could work for Relics.

---

### OpenAI (2024) - "Video Generation Models as World Simulators" (Sora)
**Technical Report** | OpenAI

Video generation as world simulation:
- **Spacetime patches:** Transformer on video latents
- **Variable duration/resolution:** Flexible generation
- **Emergent 3D:** 3D consistency without explicit 3D
- **Game simulation:** Can generate Minecraft gameplay

*Justification:* Frames video generation as world modeling - conceptually important for understanding AI worldbuilding.

*Thesis relevance:* Sora's framing of video-as-world-simulation directly supports thesis argument about AI enabling new creative possibilities.

---

## Evolution of the Field

```
2017: VQ-VAE - Discrete neural representations
   ↓
2018: World Models - Dream training for RL
   ↓
2020: GameGAN - GAN-based game simulation
   ↓
2023: DreamerV3 - Robust world models at scale
      IRIS - Transformer world models
   ↓
2024: Genie - Foundation world model (11B)
      GameNGen - Diffusion game engine
      Oasis - Real-time Minecraft
      Sora - Video as world simulation
   ↓
2025: Genie 2/3 - Scaling foundation world models
```

---

## Key Concepts for Thesis

| Concept | Paper | Application |
|---------|-------|-------------|
| **World models** | Ha & Schmidhuber | Train in hallucinated environments |
| **Discrete tokenization** | VQ-VAE, IRIS | Compress game frames for prediction |
| **Dream training** | DreamerV3 | Learn policies from imagination |
| **Foundation world model** | Genie | Generate worlds from prompts |
| **Neural game engine** | GameNGen | Replace code with weights |
| **Real-time generation** | Oasis | Playable AI-generated worlds |

---

## Practical Implications for Relics

| Task | Recommended Approach | Key Papers |
|------|---------------------|------------|
| **World generation** | Foundation model fine-tuning | Genie, Oasis |
| **Environment simulation** | World model training | DreamerV3, IRIS |
| **Level tokenization** | VQ-VAE encoding | VQ-VAE, IRIS |
| **Real-time rendering** | Diffusion backbone | GameNGen, Oasis |
| **NPC training** | Dream training | World Models, DreamerV3 |

---

## The Central Question

These papers directly address the thesis question:

**"Can AI restore the creator-to-creation ratio?"**

| Paper | Answer | Evidence |
|-------|--------|----------|
| **GameGAN** | Partial | Can simulate simple games |
| **World Models** | Partial | Works for simple environments |
| **DreamerV3** | Yes | Minecraft diamonds from scratch |
| **Genie** | Yes | Generates playable 2D worlds |
| **GameNGen** | Yes | DOOM runs on neural network |
| **Oasis** | Yes | Real-time Minecraft generation |

The trajectory is clear: AI-generated playable worlds are moving from research to reality.

---

## Limitations and Challenges

| Challenge | Current State | Thesis Implication |
|-----------|--------------|-------------------|
| **Memory/persistence** | Oasis "forgets" layouts | Need persistent world state |
| **Resolution** | 720p-1080p achievable | Sufficient for indie games |
| **Game complexity** | DOOM/Minecraft proven | 3D action RPG unproven |
| **Control fidelity** | Limited action spaces | RPG needs complex actions |
| **Training data** | Needs gameplay footage | May need custom data |

---

## Summary: Papers by Tier

| Tier | Count | Papers |
|------|-------|--------|
| **Tier 1** | 2 | World Models, VQ-VAE |
| **Tier 2** | 5 | DreamerV3, Genie, GameNGen, GameGAN, IRIS |
| **Tier 3** | 2 | Oasis, Sora |
| **Total** | 9 | |

---

## BibTeX

See `data/exports/domain_6.bib` for full citations.

## Sources

- [World Models Interactive](https://worldmodels.github.io/)
- [Genie Project Page](https://sites.google.com/view/genie-2024)
- [GameNGen](https://gamengen.github.io/)
- [Oasis](https://oasis-model.github.io/)
- [DreamerV3](https://danijar.com/project/dreamerv3/)
- [IRIS GitHub](https://github.com/eloialonso/iris)
