# Domain 8c: Quest & Dialogue Generation

## Overview

RPGs require extensive narrative content: branching dialogues, quest chains, and emergent storylines. This subdomain covers AI-assisted generation of interactive narratives, quest structures, and NPC conversation systems.

**Thesis Relevance:** A Skyrim-scale RPG needs hundreds of quests and thousands of dialogue lines. AI-assisted quest and dialogue generation is essential for solo development of narrative-rich RPGs.

---

## Paper Selection Methodology

- Recent work (2022-2025) prioritized due to rapid LLM advancement
- Game-specific papers preferred over general NLP
- Both academic and industry sources included

---

## Section A: Quest Generation

### Värtinen, Hämäläinen & Guckelsberger (2022) - "Generating Role-Playing Game Quests With GPT Language Models"
**~50 citations** | IEEE CoG 2022

LLM-based quest generation:
- **GPT-3 prompting:** Generate quest structures
- **Skyrim dataset:** Trained on Elder Scrolls quests
- **Quality evaluation:** Human ratings comparable to real quests
- **Limitations:** Coherence over long quest chains

*Thesis relevance:* DIRECTLY RELEVANT - Skyrim quest generation with GPT.

---

### Ammanabrolu & Riedl (2020) - "Graph Constrained Reinforcement Learning for Natural Language Action Spaces"
**~200 citations** | ICLR 2020

Knowledge graph constrained generation:
- **KG-A2C:** Knowledge-graph aware agent
- **Structured output:** Quests follow logical constraints
- **Interactive fiction:** Tested on text adventures
- **Commonsense:** Uses world knowledge

*Thesis relevance:* Ensures generated quests are logically coherent.

---

### Martin et al. (2018) - "Event Representations for Automated Story Generation with Deep Neural Nets"
**~300 citations** | AAAI 2018

Neural story planning:
- **Event sequences:** Model narrative as events
- **Causal reasoning:** Events have consequences
- **Story continuation:** Generate coherent plot points
- **Foundation:** Cited by most quest generation work

*Thesis relevance:* Theoretical foundation for quest event sequences.

---

### Farrokhi Maleki & Zhao (2024) - "Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration"
**Recent** | AAAI AIIDE 2024

Comprehensive PCG + LLM survey:
- **Quest generation taxonomy:** Different approaches categorized
- **LLM integration:** How GPT enhances PCG
- **Challenges:** Coherence, controllability, diversity
- **Future directions:** Identified research gaps

*Thesis relevance:* Survey providing landscape of the field.

---

## Section B: Dialogue Systems

### Young et al. (2024) - "LLM-Driven NPCs: Cross-Platform Dialogue System"
**Recent** | arXiv 2024

Practical dialogue implementation:
- **DeepSeek-R1:** LLM backbone
- **Unity + Discord:** Cross-platform NPCs
- **RAG integration:** Long-term memory via retrieval
- **Real-world tested:** User studies conducted

*Thesis relevance:* Practical architecture for game dialogue.

---

### Conversational NPC Guidelines (2024) - "Conversational Interactions with NPCs in LLM-Driven Gaming"
**Recent** | CHI 2024

Player feedback analysis:
- **Content analysis:** What players want from AI NPCs
- **Guidelines:** Design recommendations
- **Authenticity:** Maintaining character consistency
- **Limitations:** Where LLMs break immersion

*Thesis relevance:* Design guidelines for implementing LLM dialogue.

---

### Mateas & Stern (2003) - "Façade: An Experiment in Building a Fully-Realized Interactive Drama"
**~1,500 citations** | Game Developers Conference

Foundational interactive drama:
- **Beat-based:** Drama structured as emotional beats
- **ABL language:** AI behavior language for NPCs
- **Real-time:** Continuous player interaction
- **Influential:** Cited by all subsequent work

*Thesis relevance:* Historical foundation showing what's possible.

---

## Section C: Narrative Generation

### Kreminski & Wardrip-Fruin (2019) - "Generative Methods for Textual Games and Interactive Fiction"
**~100 citations** | IEEE ToG

Generative narrative theory:
- **Taxonomy:** Different generative approaches
- **Storylets:** Modular narrative units
- **Mixed initiative:** Human + AI collaboration
- **Practical:** Applicable to games

*Thesis relevance:* Bridges theory and implementation for game narratives.

---

### Wang et al. (2024) - "StoryVerse: Plot-Driven Narrative with LLMs"
**Recent** | arXiv 2024

Plot-guided generation:
- **Abstract acts:** High-level plot points
- **Character actions:** LLM fills in details
- **Author control:** Maintains narrative arc
- **Dynamic:** Adapts to player choices

*Thesis relevance:* Balances authored story with generative flexibility.

---

### Survey on LLMs for Story Generation (2025)
**EMNLP 2025**

Comprehensive story survey:
- **177 articles reviewed:** (122 from 2024)
- **GPT dominance:** 85%+ of studies use GPT
- **Applications:** Quest, dialogue, world lore
- **Challenges:** Context length, coherence

*Thesis relevance:* State-of-the-art landscape.

---

## Section D: Interactive Fiction & Text Games

### Hausknecht et al. (2020) - "Interactive Fiction Games: A Colossal Adventure"
**~200 citations** | AAAI 2020

Text game benchmark:
- **Jericho:** Framework for text game research
- **Colossal Cave:** Classic adventure as testbed
- **Language understanding:** What LLMs need for games
- **Benchmarks:** Evaluation metrics

*Thesis relevance:* Understanding narrative game requirements.

---

### Urbanek et al. (2019) - "Learning to Speak and Act in a Fantasy World"
**~300 citations** | EMNLP 2019

LIGHT dataset:
- **Fantasy dialogue:** 11k+ dialogue episodes
- **Grounded:** Characters, settings, objects
- **Actions:** Beyond just conversation
- **Open source:** Available for training

*Thesis relevance:* Fantasy RPG dialogue training data.

---

## Evolution of Quest/Dialogue Generation

```
2003: Façade - First interactive drama
    ↓
2018: Martin event representations
2019: LIGHT fantasy dialogue
2020: Ammanabrolu KG-constrained generation
    ↓
2022: GPT-3 quest generation (Värtinen)
2023: ChatGPT for game dialogue experiments
    ↓
2024: LLM-NPC systems, StoryVerse
       Cross-platform dialogue (Young)
    ↓
2025: Integrated narrative engines
```

---

## Key Concepts for Thesis

| Concept | Paper | Application |
|---------|-------|-------------|
| **Quest structure** | Värtinen 2022 | Skyrim-style quest templates |
| **KG constraints** | Ammanabrolu 2020 | Coherent quest logic |
| **Event sequences** | Martin 2018 | Narrative planning |
| **Dialogue systems** | Young 2024 | NPC conversation |
| **Storylets** | Kreminski 2019 | Modular narrative |
| **Interactive drama** | Façade | Beat-based structure |

---

## Practical Implications for Relics

| Task | Recommended Approach | Key Papers |
|------|---------------------|------------|
| **Main quests** | Authored + LLM expansion | StoryVerse |
| **Side quests** | GPT generation with templates | Värtinen 2022 |
| **NPC dialogue** | LLM + RAG memory | Young 2024 |
| **Lore/books** | LLM generation | General GPT |
| **Branching paths** | Storylet architecture | Kreminski 2019 |
| **Faction rep dialogue** | Conditional generation | Various |

---

## Hybrid Architecture for Relics

```
┌─────────────────────────────────────────────┐
│            NARRATIVE CONTROLLER             │
│  (Authored main plot beats + constraints)   │
└─────────────────┬───────────────────────────┘
                  │
    ┌─────────────┴─────────────┐
    │                           │
┌───▼───┐                 ┌─────▼─────┐
│ QUEST │                 │ DIALOGUE  │
│ GEN   │                 │ GEN       │
│       │                 │           │
│ GPT + │                 │ LLM +     │
│ KG    │                 │ RAG       │
└───┬───┘                 └─────┬─────┘
    │                           │
    └─────────────┬─────────────┘
                  │
         ┌────────▼────────┐
         │  WORLD STATE    │
         │  (Knowledge     │
         │   Graph)        │
         └─────────────────┘
```

---

## Summary: Papers by Category

| Category | Count | Papers |
|----------|-------|--------|
| **Quest Generation** | 4 | Värtinen, Ammanabrolu, Martin, Survey |
| **Dialogue Systems** | 3 | Young, CHI Guidelines, Façade |
| **Narrative Theory** | 2 | Kreminski, StoryVerse |
| **Interactive Fiction** | 2 | Jericho, LIGHT |
| **Total** | 11 | |

---

## BibTeX

See `data/exports/domain_8c.bib` for full citations.

## Sources

- [Jericho Framework](https://github.com/microsoft/jericho)
- [LIGHT Dataset](https://github.com/facebookresearch/LIGHT)
- [Façade](https://www.interactivestory.net/)
