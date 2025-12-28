# Domain 2b: PCG + AI/ML (PCGML)

## Overview

Procedural Content Generation via Machine Learning (PCGML) extends classical PCG by using learned models to generate game content. Where classical PCG uses hand-crafted rules, PCGML learns patterns from existing content, enabling generation that captures design intent without explicit programming.

**Thesis Relevance:** PCGML addresses the key limitations of classical PCG (quality ceiling, control difficulty, semantic poverty) by learning from examples. For solo developers, this means generating content that matches professional quality without manually encoding every design rule.

---

## Paper Selection Methodology

Papers selected using tiered citation approach (niche domain thresholds):
- **Tier 1 (>1,000 citations):** MUST include
- **Tier 2 (300-1,000 citations):** MUST include
- **Tier 3 (50-300 citations):** Include if venue is strong
- **Tier 4 (<50 citations):** Strong justification required

*Citation counts from Google Scholar (December 2025)*

**Note:** PCGML is a newer subfield (~2015+), so no Tier 1 papers exist yet. Tier 2 papers represent the foundational work.

---

## Tier 2: Major Foundational Papers (300-1,000 citations)

### Summerville, Snodgrass, Guzdial et al. (2018) - "Procedural Content Generation via Machine Learning (PCGML)"
**603 citations** | IEEE Transactions on Games

The definitive PCGML survey and taxonomy. Introduced the term "PCGML" and categorized approaches:
- **Sequence models:** LSTMs, Markov chains for level generation
- **Constructive models:** Autoencoders, GANs for content synthesis
- **Quality-diversity:** Combining ML with evolutionary search

Covers applications to levels, textures, audio, narratives.

*Thesis relevance:* Conceptual framework for understanding ML-enhanced generation. Essential reading.

---

### Volz, Schrum, Liu, Lucas, Smith & Togelius (2018) - "Evolving Mario Levels in the Latent Space of a Deep Convolutional GAN"
**343 citations** | GECCO (ACM)

Seminal paper combining GANs with evolutionary search:
- Train GAN on Mario levels to learn latent representation
- Use CMA-ES to search latent space for levels with desired properties
- Enables controllable generation with quality guarantees

*Thesis relevance:* Demonstrates hybrid approach - ML provides quality, search provides control. Applicable to RPG dungeon/environment generation.

---

## Tier 3: Field-Defining Papers (50-300 citations)

### Liu, Snodgrass, Khalifa, Risi et al. (2021) - "Deep Learning for Procedural Content Generation"
**252 citations** | Neural Computing and Applications (Springer)

Comprehensive survey of deep learning methods for PCG:
- CNNs for spatial content (levels, terrain)
- RNNs/LSTMs for sequential content (quests, dialogue)
- GANs for diverse generation
- Autoencoders for latent space exploration

*Thesis relevance:* Implementation guide for choosing appropriate DL architecture per content type.

---

### Khalifa, Bontrager, Earle & Togelius (2020) - "PCGRL: Procedural Content Generation via Reinforcement Learning"
**250 citations** | AAAI Conference on AI and Interactive Digital Entertainment (AIIDE)

Novel approach treating level generation as RL problem:
- Agent learns to place tiles to maximize level quality
- Controllable through reward function design
- Iterative refinement rather than one-shot generation

*Thesis relevance:* RL approach enables generation that respects playability constraints. Applicable to dungeon layouts.

---

### Risi & Togelius (2020) - "Increasing Generality in Machine Learning Through Procedural Content Generation"
**190 citations** | Nature Machine Intelligence

Argues PCG is essential for training robust AI:
- Procedurally generated environments prevent overfitting
- Co-evolution of content and agents
- PCG as curriculum learning

*Thesis relevance:* High-prestige venue (Nature). Connects PCG to broader ML research agenda.

*Venue:* Nature Machine Intelligence (top-tier)

---

### Torrado, Khalifa, Green et al. (2020) - "Bootstrapping Conditional GANs for Video Game Level Generation"
**133 citations** | IEEE Conference on Games (CoG)

Addresses GAN training with limited data:
- Bootstrap from small dataset
- Conditional generation for control
- Demonstrated on Mario levels

*Thesis relevance:* Critical for indie context where training data is limited.

---

### Fontaine, Liu, Khalifa, Modi et al. (2021) - "Illuminating Mario Scenes in the Latent Space of a GAN"
**108 citations** | AAAI

Quality-diversity approach to latent space exploration:
- MAP-Elites algorithm in GAN latent space
- Generates diverse, high-quality level collections
- Enables designer exploration of possibility space

*Thesis relevance:* Quality-diversity is key for generating varied RPG content.

---

### Gisslén, Eakins, Gordillo et al. (2021) - "Adversarial Reinforcement Learning for Procedural Content Generation"
**86 citations** | IEEE Conference on Games (CoG)

Generator-discriminator setup for level generation:
- Generator produces levels
- Discriminator evaluates quality
- Adversarial training improves both

*Thesis relevance:* Alternative to pure GAN approach with RL benefits.

---

### Schrum, Gutierrez, Volz et al. (2020) - "Interactive Evolution and Exploration Within Latent Level-Design Space of GANs"
**74 citations** | GECCO (ACM)

Mixed-initiative PCGML:
- Human explores GAN latent space interactively
- Combines machine generation with human curation
- Maintains designer agency

*Thesis relevance:* Directly relevant to thesis vision of AI-assisted (not AI-replaced) creation.

---

### Giacomello, Lanzi & Loiacono (2018) - "DOOM Level Generation Using Generative Adversarial Networks"
**71 citations** | IEEE Games, Entertainment, Media Conference

First application of GANs to 3D game levels:
- Generates DOOM WAD files
- 3D spatial layouts, not just 2D tiles
- Demonstrates applicability beyond platformers

*Thesis relevance:* 3D level generation directly relevant to RPG environments.

---

### Park, Mott, Min, Boyer et al. (2019) - "Generating Educational Game Levels with Multistep DCGAN"
**60 citations** | IEEE Conference on Games (CoG)

Controllable level generation for educational games:
- Multistep generation for larger levels
- Difficulty control through conditioning
- Player-adaptive generation

*Thesis relevance:* Difficulty control applicable to RPG progression.

---

## Tier 4: Emerging/Justified Inclusions

### Di Liello, Ardino, Gobbi et al. (2020) - "Efficient Generation of Structured Objects with Constrained Adversarial Networks"
**47 citations** | NeurIPS

**Justification:** Top venue (NeurIPS), addresses constraint satisfaction in neural generation - critical for playable levels.

---

### Wulff-Jensen, Rant, Møller et al. (2017) - "Deep Convolutional GAN for Procedural 3D Landscape Generation Based on DEM"
**36 citations** | Springer

**Justification:** Gap-filling - 3D terrain generation using GANs, directly relevant to open-world RPG.

---

### Guzdial, Snodgrass & Summerville (2022) - "Procedural Content Generation via Machine Learning" (Textbook)
**24 citations** | Springer Synthesis Lectures

**Justification:** Recent, authoritative textbook by PCGML pioneers. Extends Tier 2 survey paper.

---

## Historical Context: Pre-Deep-Learning

### Olsen (2004) - "Realtime Procedural Terrain Generation"
**149 citations** | MIT Technical Report

**Justification: Historical Significance**
- Pre-dates deep learning era but foundational for neural terrain work
- Erosion simulation, hydraulic modeling
- Referenced by all subsequent terrain papers

---

## Techniques Summary

| Technique | Best For | Key Papers |
|-----------|----------|------------|
| **GANs** | Levels, terrain, diverse content | Volz 2018, Giacomello 2018 |
| **Reinforcement Learning** | Playable levels, constraint satisfaction | Khalifa PCGRL 2020 |
| **LSTMs/Sequence Models** | Quests, dialogue, sequential content | Liu 2021 |
| **Latent Space Search** | Controllable, quality-guaranteed generation | Volz 2018, Fontaine 2021 |
| **Quality-Diversity** | Varied content libraries | Fontaine 2021 |
| **Mixed-Initiative** | Human-AI collaboration | Schrum 2020 |

---

## Key Takeaways for Thesis

1. **PCGML is mature enough for production** - 603+ citations on foundational work, proven in multiple game domains

2. **GANs + Search = Best of Both Worlds** - ML provides quality, evolutionary search provides control (Volz 2018)

3. **RL for Playability** - PCGRL approach ensures generated content is actually playable (Khalifa 2020)

4. **Limited Data Solutions Exist** - Bootstrapping (Torrado 2020) addresses indie developer data scarcity

5. **3D is Emerging** - Less mature than 2D, but Giacomello (DOOM) and Wulff-Jensen (terrain) show feasibility

6. **Mixed-Initiative PCGML** - Schrum 2020 shows how to maintain designer agency with ML generation

---

## Summary: Papers by Tier

| Tier | Count | Papers |
|------|-------|--------|
| **Tier 1** | 0 | (Field too new) |
| **Tier 2** | 2 | Summerville PCGML, Volz GAN Mario |
| **Tier 3** | 8 | Liu, Khalifa PCGRL, Risi Nature, Torrado, Fontaine, Gisslén, Schrum, Giacomello, Park |
| **Tier 4** | 3 | Di Liello (NeurIPS), Wulff-Jensen (3D terrain), Guzdial textbook |
| **Historical** | 1 | Olsen terrain |
| **Total** | 14 | |

---

## BibTeX

See `data/exports/domain_2b.bib` for full citations.

## Sources

- [PCGML Survey - IEEE](https://ieeexplore.ieee.org/document/8382283)
- [PCGRL - AIIDE](https://ojs.aaai.org/index.php/AIIDE/article/view/7416)
- [Latent Space Evolution - GECCO](https://dl.acm.org/doi/10.1145/3205455.3205517)
