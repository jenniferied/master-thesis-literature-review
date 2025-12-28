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

## Citation Tiers & Paper Selection Methodology

### CRITICAL: Search for Tier 1-2 Gaps First

Before including ANY paper in a domain review:
1. **First pass:** Search exhaustively for Tier 1 and Tier 2 papers in the domain
2. **Second pass:** Only after Tier 1-2 are covered, search for Tier 3 papers
3. **Third pass:** Tier 4 papers only to fill specific gaps with strong justification

### Tier Definitions

#### For Major AI/ML Domains (LLMs, Diffusion, 3D Generation)

| Tier | Citations | Rule | Examples |
|------|-----------|------|----------|
| **Tier 1 (Mega-foundational)** | >10,000 | MUST include | Transformers (158k), GPT-3 (51k), CLIP (40k), NeRF (10k) |
| **Tier 2 (Major foundational)** | 1,000-10,000 | MUST include | 3DGS (6k), DreamFusion (3k), Generative Agents (2.9k) |
| **Tier 3 (Field-defining)** | 100-1,000 | Include if venue is strong | Domain-specific important papers |
| **Tier 4 (Emerging/Modern)** | <100 | Strong justification required | Very recent (<2 years) OR fills critical gap |

#### For Niche Domains (PCG, Game AI, Worldbuilding)

Smaller fields have lower absolute citation counts. Adjust thresholds:

| Tier | Citations | Rule | Examples |
|------|-----------|------|----------|
| **Tier 1 (Mega-foundational)** | >1,000 | MUST include | Perlin Noise (~5k), L-systems (~1.6k) |
| **Tier 2 (Major foundational)** | 300-1,000 | MUST include | Search-Based PCG (751), PCG Textbook (~500), Hendrikx Survey (346) |
| **Tier 3 (Field-defining)** | 50-300 | Include if venue is strong | Expressive Range (128), Dormans (81) |
| **Tier 4 (Emerging/Modern)** | <50 | Strong justification required | Must explain why included |

### Justification Requirements for Tier 4 Papers

When including a paper with <100 citations (major domains) or <50 citations (niche domains), you MUST provide:

1. **Recency justification:** Published within last 2-3 years, insufficient time to accumulate citations
2. **Gap-filling justification:** Covers a critical concept not addressed by higher-tier papers
3. **Extension justification:** Directly extends or validates a Tier 1-2 paper
4. **Venue quality:** Published in top venue (NeurIPS, ICML, SIGGRAPH, IEEE TCIAIG, ACM CHI/FDG)

Format in reviews:
```
**[Paper Name]** - X citations
Justification: [Recency/Gap/Extension] - [Specific reason]
Venue: [Conference/Journal name and quality indicator]
```

### Venue Quality Indicators

**Top-tier venues (strong justification alone may suffice):**
- AI/ML: NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, SIGGRAPH
- Games: IEEE TCIAIG, ACM FDG, AIIDE, IEEE CoG
- HCI: ACM CHI, UIST

**Mid-tier venues (need additional justification):**
- Workshops at top venues
- ACM TOMM, IEEE TG
- arXiv preprints (only if highly cited or very recent and impactful)

### Exception: Historical Significance

Some works transcend citation metrics due to exceptional historical or cultural impact:
- Pre-modern-era publications (before peer review was standard)
- Works with massive real-world adoption (e.g., algorithms used industry-wide)
- Foundational concepts cited by virtually all subsequent work in the field

Examples: Gardner's Game of Life (1970), Shannon's information theory papers

**Treatment:** Include with explicit "Historical Significance" justification.

### Red Flags - Papers to Exclude

- Low citations AND old (>5 years with <50 citations = field rejected it)
- Non-peer-reviewed without exceptional impact or historical significance
- Predatory journals
- Workshop papers without follow-up journal version (unless <3 years old)

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
