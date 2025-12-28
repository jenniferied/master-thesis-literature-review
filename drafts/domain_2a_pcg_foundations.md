# Domain 2a: PCG Foundations

## Overview

Procedural Content Generation (PCG) refers to the algorithmic creation of game content with limited or indirect user input. This domain covers foundational techniques developed before deep learning integration.

**Thesis Relevance:** PCG enables small teams to create content-rich experiences. This is the technical foundation for "restoring the creator-to-creation ratio."

---

## Paper Selection Methodology

Papers selected using tiered citation approach (niche domain thresholds):
- **Tier 1 (>1,000 citations):** MUST include
- **Tier 2 (300-1,000 citations):** MUST include
- **Tier 3 (50-300 citations):** Include if venue is strong
- **Tier 4 (<50 citations):** Strong justification required

*Citation counts from Google Scholar (December 2025)*

---

## Tier 1: Mega-Foundational Papers (>1,000 citations)

### Perlin (1985) - "An Image Synthesizer"
**~5,000 citations** | SIGGRAPH

Ken Perlin's gradient noise function revolutionized procedural textures and terrain:
- Smooth, coherent randomness across scales
- Deterministic (same seed = same output)
- Won Technical Achievement Academy Award (1997)

*Thesis relevance:* Foundation for terrain heightmaps, texture variation, world generation.

---

### Prusinkiewicz & Lindenmayer (1990) - "The Algorithmic Beauty of Plants"
**~1,600 citations** | Springer (Book)

L-systems: grammar-based approach to organic structure generation:
- Formal rewriting rules with turtle graphics interpretation
- Self-similarity and fractal properties
- Stochastic variations for natural appearance

*Thesis relevance:* Essential for procedural vegetation in Shadow Realm biomes.

---

### Togelius, Yannakakis & Stanley (2011) - "Search-Based PCG: A Taxonomy and Survey"
**1,088 citations** | IEEE Transactions on Computational Intelligence and AI in Games

The definitive PCG taxonomy:
- Classification by content type, representation, evaluation method
- Established vocabulary for the entire field
- Framework for comparing PCG approaches

*Thesis relevance:* Conceptual framework for evaluating which PCG techniques suit open-world RPG development.

---

### Shaker, Togelius & Nelson (2016) - "Procedural Content Generation in Games"
**992 citations** | Springer (Textbook)

The comprehensive PCG textbook covering:
- Noise-based, grammar-based, search-based, constraint-based methods
- Applications to dungeons, terrain, quests, narratives
- Free at pcgbook.com

*Thesis relevance:* Implementation reference for full PCG pipeline.

---

## Tier 2: Major Foundational Papers (300-1,000 citations)

### Hendrikx, Meijer, Van Der Velden & Iosup (2013) - "Procedural Content Generation for Games"
**926 citations** | ACM Transactions on Multimedia Computing, Communications and Applications

Six-layered taxonomy: bits, space, systems, scenarios, design, derived. Maps methods to content layers, showing cross-domain transferability.

*Thesis relevance:* Framework for combining multiple PCG systems in unified pipeline.

---

## Tier 3: Field-Defining Papers (50-300 citations)

### Smith & Whitehead (2010) - "Analyzing the Expressive Range of a Level Generator"
**128 citations** | ACM Workshop on Procedural Content Generation in Games

Introduced **expressive range analysis**: visualizing generator output space across metrics like linearity and leniency.

*Thesis relevance:* Critical for validating PCG output matches design intent.

*Venue justification:* ACM workshop, but highly influential methodology paper cited by most subsequent PCG work.

---

### Dormans (2010) - "Adventures in Level Design"
**81 citations** | ACM Workshop on Procedural Content Generation in Games

Graph grammar approach separating mission structure from spatial layout:
- Generate mission graph first, then instantiate in space
- Keys, locks, progression emerge naturally

*Thesis relevance:* Directly applicable to RPG dungeon design where narrative pacing matters.

*Venue justification:* Workshop paper, but unique contribution (mission/space separation) not covered by higher-tier papers. Cited by Tier 1 textbook.

---

### Freiknecht & Effelsberg (2017) - "A Survey on the Procedural Generation of Virtual Worlds"
**136 citations** | MDPI Multimodal Technologies and Interaction

Comprehensive survey of virtual world generation including terrain, cities, roads, vegetation, and buildings.

*Thesis relevance:* Directly relevant to open-world generation pipeline.

---

## Tier 4: Emerging/Modern Papers (<50 citations)

### Liapis, Smith & Shaker (2016) - "Mixed-Initiative Content Creation"
**31 citations** | Book chapter in Tier 1 PCG Textbook

**Justification:**
- **Extension:** Chapter in Tier 1 textbook (Shaker 2016)
- **Gap-filling:** Mixed-initiative is KEY paradigm for thesis (AI assists, doesn't replace)
- **Venue:** Springer book chapter

Human-AI collaboration in content creation where designer maintains agency while leveraging automation.

*Thesis relevance:* Core paradigm - solo developer explores design spaces impossible to traverse alone.

---

### Karth & Smith (2017) - "WaveFunctionCollapse is Constraint Solving in the Wild"
**~150 citations** | ACM Foundations of Digital Games

**Justification:**
- Provides academic grounding for extremely popular technique (21K GitHub stars)
- Connects to constraint satisfaction literature

*Venue:* ACM FDG (top games venue)

---

## Historical Significance (Exception Category)

### Gardner (1970) - "The Fantastic Combinations of John Conway's New Solitaire Game 'Life'"
**N/A formal citations** | Scientific American

**Justification: Historical Significance**
- Introduced cellular automata to mainstream computing
- Foundational concept underlying cave generation, erosion simulation, organic terrain
- Referenced by virtually all PCG work involving emergence
- Predates modern peer-review era for CS

*Thesis relevance:* Cave systems, organic terrain features, erosion simulation in Shadow Realm.

---

## Excluded Papers (Failed Tier Criteria)

| Paper | Citations | Age | Reason for Exclusion |
|-------|-----------|-----|---------------------|
| Stammer "Spelunky" (2015) | 10 | 10 years | Low citations AND old |

---

## Non-Academic but Industry-Critical

### Gumin (2016) - WaveFunctionCollapse
**21,000+ GitHub stars** | Open source algorithm

**Justification for inclusion:**
- Massive industry adoption proves practical value
- Academic grounding provided by Karth & Smith (2017) above
- Directly usable for dungeon layouts, town structures

*Treatment:* Referenced as industry tool, formal citation uses Karth & Smith academic paper.

---

## Classic Algorithms (No Single Paper)

These techniques are foundational but lack a single canonical citation:

| Technique | Use Case | Standard Reference |
|-----------|----------|-------------------|
| BSP Trees | Dungeon room subdivision | Covered in Shaker 2016 textbook |
| Diamond-Square | Terrain heightmaps | Covered in Shaker 2016 textbook |
| Voronoi Diagrams | Biome distribution, regions | Covered in Shaker 2016 textbook |
| Cellular Automata | Cave generation, erosion | Covered in Shaker 2016 textbook |

*Treatment:* Reference Tier 1 textbook (Shaker 2016) for these techniques.

---

## Industry Success Stories

| Game | Team Size | PCG Contribution |
|------|-----------|------------------|
| **Minecraft** (2011) | 1 → Mojang | Infinite terrain, structures, biomes |
| **Spelunky** (2008) | 1 (Derek Yu) | Solvable chunked level generation |
| **Dwarf Fortress** (2006) | 2 | World history, civilizations, legends |
| **No Man's Sky** (2016) | ~15 | 18 quintillion planets |

---

## Summary: Papers by Tier

| Tier | Count | Papers |
|------|-------|--------|
| **Tier 1** | 4 | Perlin, L-systems, Togelius taxonomy, Shaker textbook |
| **Tier 2** | 1 | Hendrikx survey |
| **Tier 3** | 3 | Smith expressive range, Dormans graph grammar, Freiknecht virtual worlds |
| **Tier 4** | 2 | Liapis mixed-initiative, Karth WFC |
| **Historical** | 1 | Gardner Game of Life |
| **Total** | 11 | |

---

## Key Takeaways for Thesis

1. **Perlin noise** (Tier 1) - Foundation for terrain and natural variation
2. **L-systems** (Tier 1) - Standard for procedural vegetation
3. **Togelius taxonomy** (Tier 1) - Framework for understanding PCG approaches
4. **Mixed-initiative** (Tier 4 but critical) - Key paradigm for thesis: AI amplifies human creativity

**Limitations of classical PCG** (motivating Domain 2b):
1. Quality ceiling vs. hand-crafted content
2. Control difficulty for specific design intent
3. Semantic poverty - no understanding of content meaning

---

## BibTeX

See `data/exports/domain_2a.bib` for full citations.

## Sources

- [PCG Textbook](https://www.pcgbook.com/) (Free access)
- [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)
- [Algorithmic Beauty of Plants](https://algorithmicbotany.org/papers/abop/abop.pdf) (Free PDF)
