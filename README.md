# Master Thesis Literature Review

Automated literature review system for the master thesis: **"Worlds Within Reach: AI-Assisted Worldbuilding for Independent Development"**

## Current Status: Phase 1 Complete

**Phase 1 (Scoping Search)** has been completed. This phase cast a wide net across AI/ML and game development research to map the landscape before narrowing focus.

**Next:** Phase 2 - Manual review, narrow to 60-80 papers, choose focus domains (Houdini+ML, Generative Worlds, or similar).

## Purpose

This repository provides:

1. **Automated literature discovery** across multiple academic databases
2. **Bibliometric analysis** with visualization capabilities (notebooks scaffolded)
3. **Progress tracking** for research domains
4. **Integration with Claude Code** via MCP tools

## Research Domains

| Domain | Focus | Papers | Status |
|--------|-------|--------|--------|
| 1. Language Models | Transformers, GPT, LLMs | 11 | Complete |
| 2a. PCG Foundations | L-systems, WFC, Search-based | 11 | Complete |
| 2b. PCG + AI/ML | PCGML, Neural terrain | 14 | Complete |
| 3. Text-to-Image/Video | Diffusion, CLIP, LoRA, Sora | 17 | Complete |
| 4. 3D Generation | NeRF, Gaussian Splatting, DreamFusion | 8 | Complete |
| 5. NPCs & Agents | Believable agents, Generative Agents | 14 | Complete |
| 6. Generative Worlds | Genie, GameGAN, World Models | 9 | Complete |
| 7. Worldbuilding Theory | Subcreation, Transmedia | 12 | Complete |
| 8 (exploratory) | Indie Dev Tools, Textures | 11 | Complete |
| 8a. Animation & Rigging | Motion Matching, Learned Locomotion | 20 | Complete |
| 8b. Audio Generation | Music, Speech, SFX | 10 | Complete |
| 8c. Quest & Dialogue | Narrative, Dialogue Systems | 11 | Complete |
| 8d. Multi-Agent Systems | ChatDev, MetaGPT | 8 | Complete |
| 8f. Houdini + ML | MLOPS, Terrain Diffusion | 14 | Complete |
| 8g. UE5 + ML/PCG | PCG Framework, NNE | 15 | Complete |
| **Total** | | **~170** | (~150 academic + ~20 industry) |

## Repository Structure

```
master-thesis-literature-review/
├── CLAUDE.md              # Agent context for Claude Code
├── README.md              # This file
├── checkpoint.md          # Session state and progress
├── todo.md                # Task tracking
├── reviews.log            # Critique loop feedback
│
├── context/               # Reference materials from main thesis
│   └── thesis-vision.md
│
├── drafts/                # Domain summaries
│   ├── domain_1_llms_transformers.md
│   ├── domain_2a_pcg_foundations.md
│   ├── domain_2b_pcg_ml.md
│   ├── domain_3_text_to_image_video.md
│   ├── domain_4_3d_generation.md
│   ├── domain_5_npcs_agents.md
│   ├── domain_6_generative_worlds.md
│   ├── domain_7_worldbuilding.md
│   ├── domain_8_exploratory.md
│   ├── domain_8a_animation_rigging.md
│   ├── domain_8b_audio_generation.md
│   ├── domain_8c_quest_dialogue.md
│   ├── domain_8d_multi_agent_systems.md
│   ├── domain_8f_houdini_ml.md
│   ├── domain_8g_ue5_pcg_ml.md
│   ├── methodology_literature_review.md
│   ├── methodology_literature_review_de.md
│   └── ai_ml_foundations_explainer.md
│
├── data/
│   ├── searches/          # Raw search results (JSON/CSV)
│   └── exports/           # BibTeX for Zotero import
│       └── domain_*.bib
│
└── notebooks/             # Jupyter analysis notebooks (scaffolding for Phase 2)
    ├── 01_search_overview.ipynb
    ├── 02_citation_networks.ipynb
    ├── 03_bibliometrics.ipynb
    └── 04_topic_discovery.ipynb
```

## Tiered Citation Methodology

Papers are evaluated using a tiered system:

| Tier | Citations | Interpretation | Examples |
|------|-----------|----------------|----------|
| 1 | >1,000 | Foundational/canonical | Transformer, CLIP, Perlin |
| 2 | 300-1,000 | Field-defining | Generative Agents, 3DGS |
| 3 | 50-300 | Important contributions | Motion Matching, WFC |
| 4 | <50 | Recent/justified | 2024-2025 papers with high relevance |

## MCP Tools Available

| Tool | Database | Key Features |
|------|----------|--------------|
| `mcp__science__*` | arXiv, OpenAlex | Paper search, categories |
| `mcp__papers__*` | Multi-platform | arXiv, PubMed, bioRxiv, Semantic Scholar |
| `mcp__zotero__*` | Zotero | Library management |
| `mcp__github__*` | GitHub | Repository operations |

## Related

- **Main thesis repository:** `~/Documents/GitHub/master-thesis/`
- **Thesis topic:** AI-assisted worldbuilding for independent game development
- **Target project:** "Relics" - Skyrim-scale open-world dark fantasy RPG

## License

MIT
