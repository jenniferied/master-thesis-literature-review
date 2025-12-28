# Master Thesis Literature Review

Automated literature review system for the master thesis: **"Worlds Within Reach: AI-Assisted Worldbuilding for Independent Development"**

## Purpose

This repository provides:

1. **Automated literature discovery** across multiple academic databases
2. **Bibliometric analysis** with visualization capabilities
3. **Progress tracking** for research domains
4. **Integration with Claude Code** via MCP tools

## Research Domains

| Domain | Focus | Status |
|--------|-------|--------|
| 1. Language Models | Transformers, GPT, LLMs | Pending |
| 2. Procedural Generation | PCG, WFC, PCGML | Pending |
| 3. Text-to-Image/Video | Diffusion, CLIP, Stable Diffusion | Pending |
| 4. 3D Generation | NeRF, Gaussian Splatting, DreamFusion | Pending |
| 5. NPCs & Agents | Believable agents, Generative Agents | Pending |
| 6. Generative Worlds | Genie, GameGAN, World Models | Pending |
| 7. Worldbuilding Theory | Subcreation, Transmedia | Pending |

## Repository Structure

```
master-thesis-literature-review/
├── CLAUDE.md              # Agent context for Claude Code
├── README.md              # This file
├── RESEARCH_STATUS.md     # Progress tracking
├── requirements.txt       # Python dependencies
│
├── context/               # Reference materials from main thesis
│   ├── research-strategy.md
│   └── ai-procedural-worldgen-research.md
│
├── notebooks/             # Jupyter analysis notebooks
│   ├── 01_search_overview.ipynb
│   ├── 02_citation_networks.ipynb
│   ├── 03_bibliometrics.ipynb
│   └── 04_topic_discovery.ipynb
│
├── data/
│   ├── searches/          # Raw search results (JSON/CSV)
│   ├── exports/           # BibTeX for Zotero import
│   └── visualizations/    # Generated figures
│
└── scripts/               # Automation scripts
```

## Setup

### Prerequisites

- Python 3.9+
- Zotero Desktop with Better BibTeX
- Claude Code with MCP servers configured:
  - Semantic Scholar
  - OpenAlex
  - Zotero
  - Paper Search

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/master-thesis-literature-review.git
cd master-thesis-literature-review

# Install Python dependencies
pip install -r requirements.txt

# Optional: Install Inciteful Zotero plugin
# Download from: https://github.com/inciteful-xyz/inciteful-zotero-plugin/releases
# Install via Zotero → Tools → Add-ons → Install from File
```

## Usage

### With Claude Code

Open this repository in Claude Code and use natural language queries:

```
"Search for the most cited papers on procedural content generation from 2015-2024"

"Find the citation network for Park et al. Generative Agents paper"

"Compare research trends in text-to-3D vs neural rendering from 2020-2025"
```

### With Jupyter Notebooks

```bash
jupyter notebook notebooks/
```

The notebooks provide:

1. **01_search_overview.ipynb** - Multi-database search templates
2. **02_citation_networks.ipynb** - Key paper discovery and network analysis
3. **03_bibliometrics.ipynb** - LitStudy visualizations (trends, authors, venues)
4. **04_topic_discovery.ipynb** - NLP topic clustering

## MCP Tools Available

| Tool | Database | Key Features |
|------|----------|--------------|
| `mcp__semantic-scholar__*` | Semantic Scholar | Full-text PDF, embeddings, citations |
| `mcp__openalex__*` | OpenAlex | Trends, institutions, geographic data |
| `mcp__zotero__*` | Zotero | Your curated library |
| `mcp__paper-search__*` | Multi | arXiv, PubMed, bioRxiv, Google Scholar |

## Related

- **Main thesis repository:** `~/Documents/GitHub/master-thesis/`
- **Thesis topic:** AI-assisted worldbuilding for independent game development

## License

MIT
