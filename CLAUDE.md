# CLAUDE.md - Literature Review Agent Context

This file provides guidance to Claude Code when working in this repository.

## Project Overview

Automated literature review system for master thesis:
**"Worlds Within Reach: AI-Assisted Worldbuilding for Independent Development"**

**Central Research Question:** Can AI and procedural tools restore the creator-to-creation ratio that existed before games went 3D, enabling small teams to create open-world RPG experiences?

**Focus:** Investigating how AI and procedural generation can enable small teams (or solo developers) to create open-world RPG experiences that previously required large studios and massive budgets.

**North Star:** Create "Relics" - a Skyrim-scale open-world dark fantasy RPG in the Shadow Realm, as a solo/small team using AI and procedural tools.

## Autonomous Behavior Rules

### Code Style & Rituals
- Use `gh` CLI for all GitHub interactions
- Commits follow Conventional Commits: `feat:`, `docs:`, `chore:`, `fix:`
- Self-correction is mandatory before any PR is finalized

### Autonomous Execution
- You are authorized to install npm/pip packages if needed for data analysis
- If a search query yields no results, pivot keywords and try 3 more times before marking as 'blocked'
- Maintain `todo.md` in real-time
- Update `checkpoint.md` after completing each domain
- Commit progress after each domain completion

### Checkpoint & Recovery
- After each domain: write state to `checkpoint.md`
- If context window fills: summarize to `checkpoint.md` and refresh
- On session restart: read `checkpoint.md` first, resume from last incomplete domain

### Self-Critique Loop
- For each domain summary, spin up a critique subagent
- Review for: bias, gaps, missing citations, logical coherence
- Log critiques to `reviews.log`
- Revise based on feedback before marking complete

## Research Domains (Priority Order)

### Domain 1: Language Models & Transformers (Foundation)

- **Key terms:** transformer, attention, GPT, BERT, LLM, few-shot learning
- **Key papers:** Vaswani "Attention Is All You Need" (158k citations), Brown "GPT-3" (51k citations)
- **Use for:** Understanding the foundation that enables all other AI tools

### Domain 2a: PCG Foundations

- **Key terms:** PCG, procedural generation, WFC, wave function collapse, search-based, L-systems
- **Key papers:** Togelius "Search-Based PCG" (751 citations), Shaker PCG textbook
- **Use for:** Classic procedural generation theory and techniques

### Domain 2b: PCG + AI/ML

- **Key terms:** PCGML, machine learning PCG, neural terrain, deep learning level generation, WFC+ML
- **Key papers:** Summerville "PCGML" (425 citations), neural terrain generation papers
- **Use for:** AI-enhanced procedural generation, learned content generation

### Domain 3: Text-to-Image/Video

- **Key terms:** diffusion, latent diffusion, Stable Diffusion, CLIP, text-to-image, SDXL
- **Key papers:** Rombach "Latent Diffusion" (20k citations), Radford "CLIP" (40k citations)
- **Use for:** Concept art, texture generation, visual development

### Domain 4: 3D Generation & Neural Rendering

- **Key terms:** NeRF, Gaussian splatting, text-to-3D, DreamFusion, Magic3D
- **Key papers:** Mildenhall "NeRF" (~10k citations), Kerbl "3D Gaussian Splatting" (6k citations), Poole "DreamFusion" (3k citations)
- **Use for:** 3D asset generation, scene representation, real-time rendering

### Domain 5: NPCs & Believable Agents

- **Key terms:** believable agents, generative agents, LLM NPCs, emergent behavior, interactive characters
- **Key papers:** Bates "Believable Agents" (1.4k citations), Park "Generative Agents" (2.9k citations)
- **Use for:** NPC behavior, dialogue systems, emergent narrative

### Domain 6: Generative Interactive Worlds (Frontier)

- **Key terms:** Genie, GameGAN, world models, neural game engine, GameNGen
- **Key papers:** Bruce "Genie" (341 citations), GameNGen (152 citations)
- **Use for:** Understanding the frontier of fully generative game environments

### Domain 7: Worldbuilding Theory

- **Key terms:** worldbuilding, subcreation, transmedia, imaginary worlds, secondary worlds
- **Key papers:** Wolf "Building Imaginary Worlds" (298 citations), Jenkins "Convergence Culture" (3.5k citations)
- **Use for:** Theoretical foundation for worldbuilding practice

### Domain 8: Exploratory / Unexplored Domains

- **Key terms:** procedural animation, motion matching, learned locomotion, Audio2Face, ML muscle deformation, physics-based characters, Houdini ML, tileable textures, UE5 PCG, indie game dev AI
- **Key papers:** To be discovered
- **Use for:** Finding research strands not covered by domains 1-7, especially:
  - Animation pipeline automation
  - Houdini + machine learning integration
  - NVIDIA research (Omniverse, Replicator, Isaac Sim)
  - Indie/solo game development feasibility studies

## Available MCP Tools

Use these tools for literature searches:

| MCP | Best For | Key Features |
|-----|----------|--------------|
| **Semantic Scholar** | Primary searches | Full-text PDF, citation networks, SPECTER embeddings, 200M+ papers |
| **OpenAlex** | Trends & institutions | Author networks, topic trends, geographic analysis, 250M+ works |
| **Zotero** | Your library | Curated collection, annotations, notes, collections |
| **Paper Search** | Preprints & medical | arXiv, PubMed, bioRxiv, medRxiv, Google Scholar |

## Search Workflow Instructions

1. **For broad searches:** Use `mcp__semantic-scholar__semantic_search` first, then cross-reference with OpenAlex for institution/trend data

2. **For finding key papers:** Look for papers with >500 citations in the domain, use `mcp__semantic-scholar__get_citation_network` to find seminal works

3. **For recent work:** Filter to 2022-2025, sort by citation count, focus on papers with rapid citation growth

4. **For your library:** Search Zotero first with `mcp__zotero__zotero_semantic_search` to avoid duplicates

5. **Export format:** Generate BibTeX for Zotero import with complete metadata (author, year, title, journal/venue, DOI)

## Citation Tiers

When evaluating papers, consider citation count as an indicator of influence:

- **Tier 1 (Mega-foundational):** >50,000 citations - Transformers, BERT, GPT-3
- **Tier 2 (Major foundational):** 10,000-50,000 citations - CLIP, GANs, Latent Diffusion
- **Tier 3 (Field-defining):** 1,000-10,000 citations - Codex, 3DGS, Generative Agents
- **Tier 4 (Important modern):** 100-1,000 citations - Domain-specific key papers

## Output Formats

When saving search results:

- **JSON:** `data/searches/{domain}_{date}.json` - Full metadata for processing
- **CSV:** `data/searches/{domain}_{date}.csv` - For spreadsheet analysis
- **BibTeX:** `data/exports/{domain}.bib` - For Zotero import

## Related Repository

This literature review supports the main thesis project at:
`~/Documents/GitHub/master-thesis/`

Key files to reference:
- `docs/research-strategy.md` - Full thesis outline and reading order
- `docs/ai-procedural-worldgen-research.md` - Existing research collection

## Common Commands

```bash
# Run Jupyter notebooks
jupyter notebook notebooks/

# Install dependencies
pip install -r requirements.txt
```
