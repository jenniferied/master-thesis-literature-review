# Literature Review Methodology

## AI-Assisted Systematic Literature Discovery

This literature review employed a novel methodology: **AI-assisted systematic search** using Claude Code (Anthropic's Claude Opus 4.5) as a research collaborator. Rather than relying solely on traditional database queries, this approach combined human domain expertise with AI capabilities for cross-domain discovery, citation network analysis, and iterative refinement.

---

## 1. Research Question Alignment

The central thesis question drove all literature discovery:

> **Can AI and procedural tools restore the creator-to-creation ratio that existed before games went 3D, enabling small teams to create open-world RPG experiences?**

This question spans multiple disciplines:
- Computer science (AI/ML, procedural generation)
- Game studies (game design, player experience)
- Media production (3D graphics, animation, audio)
- Narrative theory (worldbuilding, interactive fiction)

Traditional single-database searches fail to capture this interdisciplinary scope. The AI-assisted approach enabled cross-domain discovery that a human researcher might miss due to disciplinary silos.

---

## 2. Domain Identification

### 2.1 Initial Domain Structure

Based on the researcher's existing knowledge of game development and AI tools, an initial domain structure was established:

| Domain | Focus Area | Rationale |
|--------|------------|-----------|
| **1: LLMs & Transformers** | Foundation models, attention mechanisms | Theoretical foundation for all modern AI tools |
| **2a: PCG Foundations** | Classical procedural generation | Established techniques (L-systems, noise, grammars) |
| **2b: PCG + AI/ML** | Machine learning enhanced PCG | Neural approaches to content generation |
| **3: Text-to-Image** | Diffusion models, CLIP | Concept art, texture generation pipeline |
| **4: 3D Generation** | NeRF, Gaussian splatting, text-to-3D | Asset creation automation |
| **5: NPCs & Agents** | Believable agents, generative agents | Character behavior and dialogue |
| **6: Generative Worlds** | Neural game engines, world models | Frontier research on fully generative environments |
| **7: Worldbuilding Theory** | Narrative design, subcreation | Theoretical grounding for world design |

### 2.2 Discovered Domains

The AI assistant was explicitly instructed to identify research areas the human researcher might not have considered. Through systematic exploration of citation networks and related work sections, three additional subdomains emerged:

| Domain | Focus Area | Discovery Method |
|--------|------------|------------------|
| **8a: Animation & Motion** | Procedural animation, motion matching | Citation network from NPC papers |
| **8b: Audio Generation** | Music, voice, sound effects | Gap analysis during critique loop |
| **8c: Quest & Dialogue** | Narrative generation, dialogue systems | Cross-reference from Domain 5 |

Additional research threads identified but not fully explored:

| Thread | Description | Status |
|--------|-------------|--------|
| **Multi-Agent Systems** | ChatDev, MetaGPT, AutoGPT | Papers identified, domain pending |
| **Auto-Rigging** | RigNet, HumanRig | Papers identified, domain pending |
| **Style Consistency** | LoRA, DreamBooth, ConsisLoRA | Papers identified, domain pending |
| **AI Localization** | LLM-based game translation | Papers identified, domain pending |
| **Houdini + ML** | HIVEai, MLOPS, synthetic data | Industry tools identified |
| **UE5 PCG Framework** | Engine-specific procedural tools | Documentation reviewed |

---

## 3. Tiered Citation Methodology

Papers were evaluated using a **tiered citation system** that balances historical influence with recent innovation:

| Tier | Citation Count | Interpretation | Examples |
|------|---------------|----------------|----------|
| **Tier 1** | >1,000 citations | Foundational/canonical | Transformers (158k), CLIP (40k), Perlin noise (5k) |
| **Tier 2** | 300-1,000 citations | Field-defining | Generative Agents (2.9k), 3DGS (6k) |
| **Tier 3** | 50-300 citations | Important contributions | Motion Matching, WFC academic treatments |
| **Tier 4** | <50 citations | Recent/justified inclusion | 2024-2025 papers with high relevance |

### Tier 4 Justification Criteria

Papers with fewer than 50 citations were included only when meeting at least two criteria:
1. **Recency**: Published 2023-2025 (insufficient time to accumulate citations)
2. **Direct relevance**: Explicitly addresses thesis use case (indie RPG development)
3. **Venue prestige**: Published at top venues (SIGGRAPH, NeurIPS, CVPR, CHI)
4. **Extension of Tier 1**: Directly builds on foundational work
5. **Practical tool**: Accompanies open-source implementation

---

## 4. Search Strategy

### 4.1 Primary Search Tools

| Tool | Purpose | Strengths |
|------|---------|-----------|
| **arXiv** | Preprint discovery | Latest research, open access |
| **Semantic Scholar** | Citation networks | Connected papers, influence metrics |
| **OpenAlex** | Broad academic coverage | 250M+ works, author networks |
| **Google Scholar** | Comprehensive index | Citation counts, grey literature |
| **ACM Digital Library** | Games/HCI research | CHI, FDG, SIGGRAPH proceedings |
| **IEEE Xplore** | Technical papers | ToG, CoG proceedings |

### 4.2 Search Query Evolution

Initial queries were refined through iterative expansion:

```
Round 1 (Specific):
  "procedural content generation games"
  "text-to-3D neural rendering"

Round 2 (Expanded):
  "PCGML machine learning level design"
  "neural terrain generation GAN"

Round 3 (Cross-domain):
  "world models video prediction games"
  "motion matching learned locomotion"
```

### 4.3 Citation Network Traversal

For each Tier 1 paper identified:
1. Forward citation search (papers citing this work)
2. Backward citation search (papers this work cites)
3. Related work section analysis
4. Co-author publication tracking

This revealed connections between seemingly disparate fields (e.g., video prediction research informing game world generation).

---

## 5. AI-Assisted Workflow

### 5.1 Session Structure

The literature review was conducted over multiple sessions with checkpoint-based continuity:

```
Session N:
  1. Load checkpoint.md (previous state)
  2. Continue from incomplete domain
  3. Execute searches with MCP tools
  4. Write domain summary draft
  5. Run critique subagent
  6. Revise based on feedback
  7. Export BibTeX citations
  8. Update checkpoint.md
  9. Commit progress
```

### 5.2 Checkpoint System

A `checkpoint.md` file maintained session state:
- Current domain progress
- Papers found per domain
- Files created
- Next actions
- Session recovery instructions

This enabled the AI assistant to resume work across context window limits and session boundaries.

### 5.3 Critique Loop

Each domain underwent automated critique:

```
For each domain summary:
  1. Spawn critique subagent
  2. Evaluate:
     - Thesis relevance (does this help build Relics?)
     - Citation coverage (missing seminal works?)
     - Temporal balance (recent + foundational?)
     - Logical coherence (clear narrative arc?)
     - Gap identification (what's missing?)
  3. Log critique to reviews.log
  4. Revise draft based on feedback
  5. Mark domain complete only after revision
```

### 5.4 Quality Control Measures

| Measure | Implementation |
|---------|----------------|
| **Duplicate detection** | Cross-reference against existing library |
| **Citation verification** | Confirm counts via multiple sources |
| **Venue validation** | Verify publication venue and year |
| **Relevance filtering** | Reject papers without thesis connection |
| **Recency balancing** | Ensure 2023-2025 papers in cutting-edge domains |

---

## 6. Results Summary

### 6.1 Final Domain Coverage

| Domain | Papers | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|--------|--------|--------|--------|--------|--------|
| 1: LLMs & Transformers | 11 | 4 | 3 | 2 | 2 |
| 2a: PCG Foundations | 11 | 4 | 1 | 3 | 3 |
| 2b: PCG + AI/ML | 14 | 2 | 4 | 5 | 3 |
| 3: Text-to-Image | 10 | 3 | 4 | 2 | 1 |
| 4: 3D Generation | 8 | 2 | 3 | 2 | 1 |
| 5: NPCs & Agents | 14 | 3 | 4 | 4 | 3 |
| 6: Generative Worlds | 9 | 2 | 3 | 2 | 2 |
| 7: Worldbuilding Theory | 12 | 2 | 3 | 4 | 3 |
| 8a: Animation & Motion | 11 | 2 | 4 | 3 | 2 |
| 8b: Audio Generation | 10 | 1 | 3 | 4 | 2 |
| 8c: Quest & Dialogue | 11 | 1 | 3 | 4 | 3 |
| **Total** | **121** | **26** | **35** | **35** | **25** |

### 6.2 Temporal Distribution

| Period | Paper Count | Percentage |
|--------|-------------|------------|
| Pre-2017 | 18 | 15% |
| 2017-2019 | 22 | 18% |
| 2020-2022 | 34 | 28% |
| 2023-2025 | 47 | 39% |

The distribution reflects the thesis focus on practical, contemporary tools while maintaining theoretical grounding in foundational work.

### 6.3 Venue Distribution

| Venue Type | Count | Examples |
|------------|-------|----------|
| Top ML conferences | 31 | NeurIPS, ICML, ICLR |
| Graphics/Vision | 28 | SIGGRAPH, CVPR, ICCV |
| Games/Interactive | 22 | CHI, FDG, CoG, ToG |
| NLP/Language | 15 | ACL, EMNLP, NAACL |
| Preprints (arXiv) | 18 | Recent work awaiting peer review |
| Books/Surveys | 7 | Textbooks, comprehensive surveys |

---

## 7. Limitations

### 7.1 Methodological Limitations

1. **AI hallucination risk**: Citation counts and publication details were verified against multiple sources, but some errors may persist
2. **Recency bias**: 2024-2025 papers lack citation history for impact assessment
3. **English-language bias**: Non-English publications were not systematically searched
4. **Commercial tool coverage**: Industry tools (Unity ML-Agents, NVIDIA Omniverse) have limited academic literature

### 7.2 Scope Limitations

1. **Game-specific focus**: General AI/ML advances were filtered for game development relevance
2. **Indie developer lens**: Enterprise-scale solutions were deprioritized
3. **Unreal Engine focus**: Unity-specific research was included but not prioritized

---

## 8. Reproducibility

All literature review artifacts are available in the project repository:

```
master-thesis-literature-review/
├── checkpoint.md           # Session state and progress
├── reviews.log             # Critique loop feedback
├── drafts/
│   ├── domain_1_llms_transformers.md
│   ├── domain_2a_pcg_foundations.md
│   ├── domain_2b_pcg_ml.md
│   ├── domain_3_text_to_image.md
│   ├── domain_4_3d_generation.md
│   ├── domain_5_npcs_agents.md
│   ├── domain_6_generative_worlds.md
│   ├── domain_7_worldbuilding.md
│   ├── domain_8_exploratory.md
│   ├── domain_8b_audio_generation.md
│   └── domain_8c_quest_dialogue.md
└── data/exports/
    └── domain_*.bib        # BibTeX citations per domain
```

---

## 9. Conclusion

This AI-assisted methodology enabled comprehensive cross-domain literature discovery that would be impractical through manual search alone. The combination of human domain expertise (initial domain structure, relevance filtering) with AI capabilities (citation network traversal, cross-domain connection discovery, iterative refinement) produced a literature foundation spanning 121 papers across 11 domains.

The approach demonstrates a model for AI-augmented academic research: the human researcher maintains intellectual direction and quality control while the AI assistant handles search execution, organization, and systematic coverage verification.
