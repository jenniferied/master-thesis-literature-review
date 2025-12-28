# Domain 2a: PCG Foundations

## Overview

Procedural Content Generation (PCG) refers to the algorithmic creation of game content with limited or indirect user input. This domain covers the foundational techniques developed before the integration of machine learning, establishing the theoretical and practical basis for all modern PCG approaches.

## Key Papers & Resources

### 1. Search-Based PCG Taxonomy (Togelius et al., 2011)
**"Search-Based Procedural Content Generation: A Taxonomy and Survey"**

The definitive taxonomy for understanding PCG methods. Proposes classification based on:
- **What** content is generated (levels, rules, narratives, etc.)
- **How** content is represented (constructive vs. generate-and-test)
- **How** quality/fitness is evaluated (direct functions, simulation-based, interactive)

This paper established the vocabulary and conceptual framework for the entire field. Essential for understanding how different PCG approaches relate to each other.

**Relevance to thesis:** Provides the conceptual framework for evaluating which PCG techniques are suitable for open-world RPG development.

### 2. PCG Textbook (Shaker, Togelius, Nelson, 2016)
**"Procedural Content Generation in Games"**

The first comprehensive textbook, covering:
- Fractal/noise-based methods (terrain, textures)
- Grammar-based methods (L-systems, shape grammars)
- Search-based/evolutionary methods
- Constraint-based methods
- Applications to dungeons, terrain, quests, narratives

Available free online at pcgbook.com. Essential reading for anyone implementing PCG systems.

**Relevance to thesis:** Practical implementation guidance for the full PCG pipeline.

### 3. Perlin Noise (Perlin, 1985)
**"An Image Synthesizer"**

Ken Perlin's gradient noise function revolutionized procedural texture and terrain generation. Key properties:
- Smooth, natural-looking randomness
- Coherent across scales (octaves/fractal brownian motion)
- Deterministic (same seed = same output)
- Fast computation

Won a Technical Achievement Academy Award (1997) for its impact on film CGI.

**Relevance to thesis:** Foundation for procedural terrain heightmaps, texture variation, and natural randomness in world generation.

### 4. L-Systems (Prusinkiewicz & Lindenmayer, 1990)
**"The Algorithmic Beauty of Plants"**

Grammar-based approach to generating plant structures:
- Formal rewriting rules (alphabet + productions)
- Turtle graphics interpretation
- Self-similarity and fractal properties
- Stochastic variations for natural appearance

L-systems remain the standard for procedural vegetation in games.

**Relevance to thesis:** Essential for procedural forest/vegetation generation in the Shadow Realm biome.

### 5. Wave Function Collapse (Gumin, 2016)
**WaveFunctionCollapse Algorithm**

Constraint-solving approach to tile-based generation:
- Learns patterns from example images
- Propagates constraints to ensure coherent output
- Produces varied but consistent results
- 21,000+ GitHub stars, widely adopted

Karth & Smith (2017) provided academic analysis connecting WFC to constraint satisfaction literature.

**Relevance to thesis:** Useful for dungeon layouts, town structures, and any tile-based content that needs local coherence.

### 6. Cellular Automata (Conway/Gardner, 1970)
**Game of Life and Cave Generation**

Simple local rules produce emergent global patterns:
- Cell states influenced by neighbors
- Iterative refinement
- Natural-looking organic shapes
- Used extensively for cave/dungeon generation

**Relevance to thesis:** Cave systems, organic terrain features, erosion simulation.

## Synthesis: Foundational PCG for Game Development

These techniques share key properties valuable for indie development:

1. **Determinism:** Same seed produces same output (essential for multiplayer, saves)
2. **Efficiency:** Generate content on-demand, reducing storage requirements
3. **Variety:** Infinite variations from finite rules
4. **Controllability:** Parameters allow designer guidance

### PCG Pipeline for Open-World RPGs

```
[Designer Input] → [PCG Algorithms] → [Content] → [Validation] → [Game]
     ↓                    ↓              ↓            ↓
   Seeds              Noise           Terrain      Playability
   Rules            L-systems        Vegetation    Accessibility
   Constraints         WFC           Structures    Balance
```

### Limitations of Classical PCG

1. **Quality ceiling:** Output rarely matches hand-crafted content
2. **Control difficulty:** Achieving specific design intent is challenging
3. **Coherence issues:** Local rules don't guarantee global coherence
4. **Content variety:** Algorithms can produce samey-feeling content

These limitations motivate the ML-enhanced approaches covered in Domain 2b.

## Key Takeaways for Thesis

1. **Perlin noise** remains essential for terrain heightmaps and natural variation
2. **L-systems** are the standard for procedural vegetation
3. **WFC** offers a modern, powerful approach to tile-based content
4. **Cellular automata** useful for organic structures and erosion
5. **Search-based methods** (genetic algorithms, etc.) enable optimization toward design goals

The foundational techniques are mature, well-documented, and implemented in most game engines. The challenge is combining them effectively and addressing their limitations through AI/ML enhancement (Domain 2b).

## BibTeX

See `data/exports/domain_2a.bib` for full citations.

## Sources

- [Semantic Scholar - Search-Based PCG](https://www.semanticscholar.org/paper/Search-Based-Procedural-Content-Generation:-A-and-Togelius-Yannakakis/3288d7575f451d2e95f57cefc9566691ff272f1c)
- [PCG Textbook](https://www.pcgbook.com/)
- [Perlin Noise - Wikipedia](https://en.wikipedia.org/wiki/Perlin_noise)
- [The Algorithmic Beauty of Plants (PDF)](https://algorithmicbotany.org/papers/abop/abop.pdf)
- [WaveFunctionCollapse - GitHub](https://github.com/mxgmn/WaveFunctionCollapse)
- [WFC Academic Paper](https://dl.acm.org/doi/10.1145/3102071.3110566)
