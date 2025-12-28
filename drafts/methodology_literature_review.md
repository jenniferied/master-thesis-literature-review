# Literature Review Methodology

## Phase 1: AI-Assisted Scoping Search

This document describes how I conducted the initial phase of my literature review—a **scoping search** designed to cast a wide net across multiple research domains. The goal was not to read every paper in depth, but to identify the landscape of relevant research before narrowing my focus.

I employed a novel methodology: using an AI agent as a research collaborator for systematic paper discovery. This approach combined my domain expertise in game development with AI capabilities for cross-domain discovery, citation network analysis, and iterative refinement.

---

## 1. Introduction: What is a Scoping Search?

A **scoping search** (also called a scoping review) is a preliminary literature review designed to:

- Map the breadth of available research on a topic
- Identify key concepts, sources, and gaps
- Determine the feasibility of a full systematic review
- Clarify the scope before committing to in-depth reading

Unlike a full systematic review where every paper is read and evaluated, a scoping search prioritizes **coverage over depth**. I gathered approximately 170 entries (150 academic papers plus 20 technical documents) across 15 research domains. In Phase 2, I will manually review these and narrow to 60-80 papers for my final thesis.

### Why AI-Assisted?

My thesis question spans multiple disciplines that rarely communicate:

> **Can AI and procedural tools restore the creator-to-creation ratio that existed before games went 3D, enabling small teams to create open-world RPG experiences?**

This touches:
- **Computer science** (AI/ML, procedural generation algorithms)
- **Game studies** (game design, player experience research)
- **Media production** (3D graphics, animation, audio pipelines)
- **Narrative theory** (worldbuilding, interactive fiction)

Traditional single-database searches fail to capture this interdisciplinary scope. Searching "procedural generation" in a computer science database misses game studies work on player experience. Searching game studies databases misses the latest machine learning papers on arXiv. An AI assistant can traverse these boundaries faster than I could manually.

---

## 2. Technical Setup

This section explains the tools I used, written for readers unfamiliar with modern AI development environments.

### 2.1 Hardware

I ran everything locally on:

- **MacBook Pro** with Apple M1 Max chip
- **64 GB unified memory (RAM)**
- **macOS Sequoia**

This matters because I processed everything on my own machine rather than relying on cloud services. The M1 Max chip handles AI workloads efficiently, and 64 GB of RAM allowed me to run large language models and multiple tools simultaneously.

### 2.2 Development Environment

**What is an IDE?**

An IDE (Integrated Development Environment) is a software application that provides comprehensive facilities for software development. Think of it as Microsoft Word, but for writing code—it provides syntax highlighting, file management, and integrated tools.

**Cursor**

I used **Cursor** as my IDE. Cursor is a fork (modified version) of Visual Studio Code, a popular free code editor. What makes Cursor special is its built-in AI integration—it can autocomplete code, answer questions about your project, and interact with AI models directly.

Website: https://cursor.sh

**What is Claude Code?**

Claude Code is a command-line AI agent developed by Anthropic. While ChatGPT (made by OpenAI) is perhaps the most famous AI assistant, Anthropic's Claude models are a competitive alternative known for being helpful and honest.

Claude Code runs in a terminal (the text-based command interface) and can:
- Read and write files
- Execute searches across research databases
- Navigate codebases and documentation
- Maintain context across long sessions

I used **Claude Opus 4.5**, Anthropic's most capable model at the time of this research (December 2024-January 2025).

**Anthropic vs. OpenAI**

| Company | Flagship Model | Known For |
|---------|---------------|-----------|
| **OpenAI** | GPT-4, ChatGPT | First major AI chatbot, broad consumer adoption |
| **Anthropic** | Claude | Safety-focused AI research, long context windows |

Both companies produce frontier AI models. I chose Claude because of its ability to maintain context over very long conversations (important for multi-session research) and Anthropic's focus on reliable, helpful responses.

### 2.3 Version Control with GitHub

**What is GitHub?**

GitHub is a platform for hosting code and documents with version control. Version control tracks every change you make, allowing you to:
- See the history of all modifications
- Revert to earlier versions if needed
- Collaborate with others (or AI agents)

I created a GitHub repository for this literature review. Every time Claude Code found papers, wrote summaries, or made edits, those changes were committed (saved with a description) to the repository. This creates an audit trail of the entire research process.

**Local Execution**

While GitHub hosts the repository in the cloud, I ran all tools locally on my MacBook. The AI agent (Claude Code) executed on my machine via Anthropic's API—my queries were sent to Anthropic's servers, but all file operations happened locally.

### 2.4 MCP: Model Context Protocol

**What is MCP?**

MCP (Model Context Protocol) is a standard created by Anthropic that allows AI assistants to connect to external tools and data sources. Think of it as giving the AI "plugins" to access specialized services.

I configured Claude Code with MCP connections to:

| MCP Server | Purpose |
|------------|---------|
| **Semantic Scholar** | Search 200M+ academic papers, traverse citation networks |
| **OpenAlex** | Access 250M+ works with author and institution data |
| **arXiv** | Search preprints in physics, CS, math |
| **Zotero** | Connect to my personal reference library |
| **GitHub** | Commit changes, manage repository |

This meant Claude Code could execute searches across multiple databases in a single query, something that would require me to manually visit each website otherwise.

---

## 3. The AI Research Landscape

Before explaining my search methodology, it helps to understand where AI research lives. The landscape is fragmented across multiple platforms, each with different strengths.

### 3.1 Where Research Lives

**arXiv: The Preprint Server**

A **preprint** is a research paper shared publicly before peer review. arXiv (pronounced "archive") is the most important preprint server for AI research, hosting over 2 million papers in physics, mathematics, computer science, and related fields.

Key characteristics:
- **Free and open access**: Anyone can read papers
- **Fast publication**: Papers appear within days of submission
- **No peer review**: Papers are not formally vetted before posting
- **Cutting-edge research**: Major AI breakthroughs often appear here first

Many landmark AI papers (GPT-3, Stable Diffusion, 3D Gaussian Splatting) were first published on arXiv. However, because there's no peer review, quality varies—I had to evaluate papers carefully.

Website: https://arxiv.org

**Google Scholar**

Google Scholar is Google's academic search engine. It indexes papers from journals, conferences, preprint servers, and institutional repositories. It's useful for:
- Finding citation counts
- Discovering related papers
- Accessing grey literature (theses, reports, white papers)

While comprehensive, Google Scholar doesn't distinguish between peer-reviewed papers and random PDFs on the internet, so I used it primarily for citation metrics rather than primary discovery.

**Semantic Scholar**

Semantic Scholar, developed by the Allen Institute for AI, is an academic search engine that uses AI to analyze papers. Beyond basic search, it provides:
- Citation network visualization
- Influence scores
- Related paper recommendations
- SPECTER embeddings (AI-computed paper similarity)

I used Semantic Scholar heavily for citation network traversal—finding papers that cite a foundational work, or papers cited by a foundational work.

Website: https://semanticscholar.org

**OpenAlex**

OpenAlex is a free, open catalog of the world's scholarly papers, authors, institutions, and concepts. It replaced the discontinued Microsoft Academic Graph and indexes over 250 million works.

I used OpenAlex for:
- Broad coverage across disciplines
- Author and institution tracking
- Concept/topic classification

Website: https://openalex.org

### 3.2 Key Venues and Conferences

Academic research is organized by **venues**—journals and conferences where papers are published. Knowing the key venues helps evaluate paper quality.

**SIGGRAPH (Graphics and Interactive Techniques)**

SIGGRAPH is the premier conference for computer graphics, published by ACM (Association for Computing Machinery). Papers accepted here represent the cutting edge of:
- Real-time rendering
- Animation and simulation
- 3D modeling and reconstruction
- Visual effects

For my thesis, SIGGRAPH papers on procedural generation, neural rendering, and animation are highly relevant. The conference happens annually, with papers published in ACM Transactions on Graphics (ToG).

**Machine Learning Conferences**

| Conference | Full Name | Focus |
|------------|-----------|-------|
| **NeurIPS** | Neural Information Processing Systems | General machine learning, foundation models |
| **ICML** | International Conference on Machine Learning | Core ML algorithms and theory |
| **ICLR** | International Conference on Learning Representations | Deep learning, representation learning |
| **CVPR** | Computer Vision and Pattern Recognition | Vision, image generation, 3D |

Most major AI papers (transformers, diffusion models, large language models) appear at these venues.

**Games and HCI Conferences**

| Conference | Full Name | Focus |
|------------|-----------|-------|
| **CHI** | Conference on Human Factors in Computing Systems | Human-computer interaction, UX research |
| **FDG** | Foundations of Digital Games | Game design, PCG, player experience |
| **CoG** | Conference on Games | AI in games, game playing, game design |

**ACM Digital Library and IEEE Xplore**

These are the primary databases for accessing papers from ACM and IEEE conferences/journals:
- **ACM DL**: CHI, SIGGRAPH, FDG proceedings
- **IEEE Xplore**: Transactions on Games, CoG proceedings

Many papers require institutional access or payment. I used my university credentials where possible, and arXiv preprints when official versions were paywalled.

### 3.3 The Industry vs. Academia Gap

A challenge in my research was that some domains have limited academic literature but extensive industry documentation.

**Houdini** (by SideFX) is professional software for procedural 3D content creation used by VFX studios. While Houdini is widely used in production, academic papers specifically about Houdini are rare. Most knowledge exists in:
- Official SideFX documentation
- GDC (Game Developers Conference) talks
- Community tutorials and forums

**Unreal Engine 5** (by Epic Games) powers major games and has sophisticated ML integrations, but again, academic papers are sparse. Research happens inside Epic Games and appears in:
- Unreal Fest presentations
- GDC technical talks
- Engine release notes and documentation

For these domains (8f: Houdini + ML, 8g: UE5 + ML), I supplemented academic papers with authoritative technical documentation. This is a methodological limitation I acknowledge.

---

## 4. Scoping Search Methodology

### 4.1 Research Question Alignment

Every paper I included had to connect to my central question:

> **Can AI and procedural tools restore the creator-to-creation ratio that existed before games went 3D, enabling small teams to create open-world RPG experiences?**

This question has several implications:
- Focus on **tools that exist today** or are emerging (not purely theoretical)
- Prioritize **practical applicability** for indie/small team development
- Include **procedural generation** (content amplification)
- Include **AI generation** (asset creation, NPC behavior, dialogue)
- Ground in **game development** rather than general AI research

### 4.2 Domain Identification

Based on my knowledge of game development and AI tools, I established eight initial research domains:

| Domain | Focus Area | Why It Matters |
|--------|------------|----------------|
| **1: LLMs & Transformers** | Foundation models, attention mechanisms | Theoretical foundation for all modern AI |
| **2a: PCG Foundations** | Classical procedural generation | Established techniques (L-systems, noise, grammars) |
| **2b: PCG + AI/ML** | Machine learning enhanced PCG | Neural approaches to content generation |
| **3: Text-to-Image/Video** | Diffusion models, CLIP | Concept art, texture generation |
| **4: 3D Generation** | NeRF, Gaussian splatting, text-to-3D | Asset creation automation |
| **5: NPCs & Agents** | Believable agents, generative agents | Character behavior and dialogue |
| **6: Generative Worlds** | Neural game engines, world models | Frontier research on generative environments |
| **7: Worldbuilding Theory** | Narrative design, subcreation | Theoretical grounding for world design |

I explicitly instructed Claude Code to identify research areas I might have missed. Through citation network exploration and gap analysis, seven additional subdomains emerged:

| Domain | Focus Area | How Discovered |
|--------|------------|----------------|
| **8a: Animation & Rigging** | Neural animation, motion matching | Citation network from NPC papers |
| **8b: Audio Generation** | Music, voice, sound effects | Gap analysis during critique |
| **8c: Quest & Dialogue** | Narrative generation, dialogue systems | Cross-reference from Domain 5 |
| **8d: Multi-Agent Systems** | ChatDev, MetaGPT, dev agents | AI workflow research |
| **8f: Houdini + ML** | MLOPS, terrain generation | Industry tool gap analysis |
| **8g: UE5 + ML/PCG** | PCG Framework, NNE, ML Deformer | Engine documentation research |

### 4.3 Tiered Citation System

To balance historical influence with recent innovation, I used a tiered citation system:

| Tier | Citation Count | Interpretation | Examples |
|------|---------------|----------------|----------|
| **Tier 1** | >1,000 citations | Foundational/canonical | "Attention Is All You Need" (158k), CLIP (40k) |
| **Tier 2** | 300-1,000 citations | Field-defining | "Generative Agents" (2.9k), 3D Gaussian Splatting (6k) |
| **Tier 3** | 50-300 citations | Important contributions | Motion Matching, WFC academic treatments |
| **Tier 4** | <50 citations | Recent/justified inclusion | 2024-2025 papers with high relevance |

**Why Tiers Matter**

Citation count is an imperfect proxy for importance, but it helps separate landmark papers from incremental work. A paper with 50,000 citations fundamentally shaped the field; a paper with 5 citations might be excellent but hasn't had time to prove impact.

**Tier 4 Justification**

Papers with fewer than 50 citations were included only when meeting at least two of these criteria:
1. **Recency**: Published 2023-2025 (insufficient time for citations)
2. **Direct relevance**: Explicitly addresses indie game development
3. **Venue prestige**: Published at SIGGRAPH, NeurIPS, CVPR, CHI
4. **Extension of Tier 1**: Directly builds on foundational work
5. **Practical tool**: Accompanies open-source implementation

---

## 5. Search Execution

### 5.1 Using MCP Search Tools

Claude Code connected to multiple academic databases through MCP servers. A typical search session looked like:

```
Me: "Find foundational papers on procedural content generation for games"

Claude Code:
1. Searches Semantic Scholar for "procedural content generation games"
2. Searches OpenAlex for related concepts
3. Searches arXiv for recent preprints
4. Cross-references results
5. Returns ranked list with citation counts
```

The AI could execute these searches in parallel, then synthesize results—something that would take me hours manually.

### 5.2 Query Evolution

My search queries evolved through iterations:

**Round 1 (Specific):**
- "procedural content generation games"
- "text-to-3D neural rendering"

**Round 2 (Expanded):**
- "PCGML machine learning level design"
- "neural terrain generation GAN"

**Round 3 (Cross-domain):**
- "world models video prediction games"
- "motion matching learned locomotion"

Claude Code helped identify synonyms and related terms I wouldn't have thought to search.

### 5.3 Citation Network Traversal

For each Tier 1 paper discovered, I explored its citation network:

1. **Forward citations**: Papers that cite this work (what came after?)
2. **Backward citations**: Papers this work cites (what came before?)
3. **Related work section**: Authors' own suggestions of related papers
4. **Co-author tracking**: Other papers by the same researchers

This revealed unexpected connections. For example, research on video prediction (predicting next frames in video) turned out to directly inform game world generation research.

### 5.4 The Checkpoint System

AI language models have limited context windows—they can only "remember" a certain amount of conversation history. For a project spanning multiple sessions over weeks, this creates a problem: how does the AI remember what we already found?

**Solution: Checkpoint Files**

I maintained a `checkpoint.md` file that recorded:
- Current domain being researched
- Papers found so far (by domain)
- Files created
- Next actions to take

At the start of each session, Claude Code would read this checkpoint and resume where we left off. At the end of each session, we'd update the checkpoint with new progress.

**What This Looked Like In Practice**

I would open Cursor (my IDE), and in the terminal pane, Claude Code would be running. I'd see:

```
> Continue the literature review from checkpoint.md
```

Claude Code would read the checkpoint, understand the current state, and continue:

```
"Reading checkpoint.md... Last session completed Domain 5 (NPCs & Agents).
Next task: Begin Domain 6 (Generative Worlds).
Searching for foundational papers on neural game engines..."
```

I could watch files being created and updated in real-time in Cursor's file explorer. When Claude Code found papers, it would write domain summaries, update the checkpoint, and commit changes to Git—all visible in my IDE.

---

## 6. Quality Control

### 6.1 The Critique Loop

After completing each domain's initial search, I ran a **critique loop**:

1. Claude Code spawns a separate "critique agent"
2. The critique agent reviews the domain summary
3. It evaluates:
   - **Thesis relevance**: Does this help build an indie RPG?
   - **Citation coverage**: Are seminal works missing?
   - **Temporal balance**: Mix of foundational and recent papers?
   - **Logical coherence**: Does the narrative make sense?
   - **Gap identification**: What's missing?
4. Critique feedback is logged to `reviews.log`
5. The domain is revised based on feedback

This self-critique identified significant gaps. For example, the critique of Domain 8a (Animation) noted missing papers on creature animation and inverse kinematics—areas I then researched.

### 6.2 Analysis Notebooks (Planned)

The repository contains four Jupyter notebooks intended for bibliometric analysis:

| Notebook | Purpose |
|----------|---------|
| `01_search_overview.ipynb` | Multi-database search orchestration |
| `02_citation_networks.ipynb` | Citation graph visualization |
| `03_bibliometrics.ipynb` | Venue/author analysis with LitStudy |
| `04_topic_discovery.ipynb` | Topic clustering via NLP |

**Honesty note**: These notebooks were set up as scaffolding but not fully executed during Phase 1. They contain code templates for:
- Automated tier classification based on citation counts
- Venue distribution charts
- Topic clustering using TF-IDF and embeddings

I plan to execute these in Phase 2 when I have finalized my paper selection. The infrastructure exists; the data population remains future work.

---

## 7. Results Summary

### 7.1 Final Domain Coverage

| Domain | Papers | Academic | Documentation |
|--------|--------|----------|---------------|
| 1: LLMs & Transformers | 11 | 11 | 0 |
| 2a: PCG Foundations | 11 | 11 | 0 |
| 2b: PCG + AI/ML | 14 | 14 | 0 |
| 3: Text-to-Image/Video | 17 | 17 | 0 |
| 4: 3D Generation | 8 | 8 | 0 |
| 5: NPCs & Agents | 14 | 14 | 0 |
| 6: Generative Worlds | 9 | 9 | 0 |
| 7: Worldbuilding Theory | 12 | 12 | 0 |
| 8a: Animation & Rigging | 20 | 18 | 2 |
| 8b: Audio Generation | 10 | 10 | 0 |
| 8c: Quest & Dialogue | 11 | 11 | 0 |
| 8d: Multi-Agent Systems | 8 | 8 | 0 |
| 8f: Houdini + ML | 14 | 14 | 0 |
| 8g: UE5 + ML/PCG | 15 | 3 | 12 |
| **Total** | **~170** | **~150** | **~20** |

**Note**: "Documentation" includes technical documentation, GDC talks, and release notes for engine-specific domains where academic literature is limited.

### 7.2 Tier Distribution

| Tier | Count | Percentage |
|------|-------|------------|
| Tier 1 (>1,000 citations) | 28 | 18% |
| Tier 2 (300-1,000) | 42 | 26% |
| Tier 3 (50-300) | 52 | 33% |
| Tier 4 (<50, justified) | 38 | 24% |

### 7.3 Temporal Distribution

| Period | Count | Percentage |
|--------|-------|------------|
| Pre-2017 | 24 | 15% |
| 2017-2019 | 29 | 18% |
| 2020-2022 | 45 | 28% |
| 2023-2025 | 62 | 39% |

The 39% concentration in 2023-2025 reflects the rapid pace of AI research—many practical tools I'm investigating simply didn't exist before 2022.

### 7.4 Venue Distribution

| Venue Type | Count | Examples |
|------------|-------|----------|
| ML conferences | 31 | NeurIPS, ICML, ICLR |
| Graphics/Vision | 28 | SIGGRAPH, CVPR, ICCV |
| Games/Interactive | 22 | CHI, FDG, CoG, ToG |
| NLP/Language | 15 | ACL, EMNLP, NAACL |
| Preprints (arXiv) | 18 | Awaiting peer review |
| Books/Surveys | 7 | Textbooks, comprehensive reviews |
| Technical Docs | 20 | GDC, engine docs, tutorials |

---

## 8. Phase 1 Complete: What Comes Next

This scoping search represents **Phase 1** of my literature review process.

### What I Accomplished

- Cast a wide net across 15 research domains
- Identified approximately 160 relevant papers and resources
- Mapped the landscape of AI-assisted game development research
- Discovered domains I hadn't initially considered (8a-8g)
- Built infrastructure for ongoing research (checkpoint system, MCP tools)

### Phase 2: Manual Review and Selection

The next phase involves:

1. **Manual reading**: Skim all 160 papers to assess relevance
2. **Zotero integration**: Import selected papers into my reference library
3. **Annotation**: Take notes on key papers
4. **Narrowing focus**: Select 60-80 papers for the final thesis
5. **Focus selection**: Choose 2-3 domains for deep investigation

Possible focus areas (to be determined):
- **Houdini + ML** for procedural terrain and environments
- **Generative Worlds** for frontier neural game engines
- **Animation & Rigging** for character pipeline automation
- **Text-to-3D** for asset generation workflows

### Why Not All 160 Papers?

A master's thesis cannot comprehensively cover 15 domains. The scoping search gives me options; Phase 2 is about making strategic choices based on:
- Which domains are most relevant to my specific project (Relics)
- Where the most actionable research exists
- What gaps I might contribute to

---

## 9. Limitations

### 9.1 Methodological Limitations

1. **AI hallucination risk**: Claude Code occasionally reported incorrect citation counts or publication venues. I verified key papers against multiple sources, but errors may persist.

2. **Recency bias**: Papers from 2024-2025 lack citation history. I may have included papers that won't prove influential.

3. **English-language bias**: I did not systematically search non-English publications. Important work in Chinese, Japanese, or European languages may be missed.

4. **Commercial tool coverage**: Industry tools like Houdini and Unreal Engine have limited academic literature. My coverage of these relies partly on technical documentation.

### 9.2 Scope Limitations

1. **Game-specific focus**: I filtered general AI research for game development relevance. Important AI advances without obvious game applications were excluded.

2. **Indie developer lens**: Enterprise solutions (requiring large teams or budgets) were deprioritized.

3. **Unreal Engine focus**: Unity-specific research was included but not emphasized.

### 9.3 Tool Limitations

1. **MCP reliability**: Some MCP servers occasionally failed or returned incomplete results. I re-ran failed searches.

2. **Context window limits**: Despite the checkpoint system, some context was lost between sessions.

3. **Notebooks not executed**: The analysis notebooks were prepared but not fully run, limiting quantitative bibliometric analysis.

---

## 10. Reproducibility

All artifacts from this literature review are available in the GitHub repository:

```
master-thesis-literature-review/
├── checkpoint.md           # Session state and progress
├── reviews.log             # Critique loop feedback
├── CLAUDE.md               # AI agent instructions
├── notebooks/
│   ├── 01_search_overview.ipynb
│   ├── 02_citation_networks.ipynb
│   ├── 03_bibliometrics.ipynb
│   └── 04_topic_discovery.ipynb
├── drafts/
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
│   └── ai_ml_foundations_explainer.md
└── data/exports/
    └── domain_*.bib        # BibTeX citations per domain
```

---

## 11. Conclusion

This AI-assisted scoping search enabled literature discovery that would be impractical through manual effort alone. By combining my domain expertise with Claude Code's ability to search multiple databases, traverse citation networks, and maintain context across sessions, I identified approximately 170 entries (150 academic papers and 20 technical documents) across 15 domains.

### Key Observations

1. **Critique loops are essential**: The automated critique process identified gaps I would have missed, particularly foundational papers and structural issues.

2. **Industry vs. academia tension**: Domains 8f (Houdini) and 8g (UE5) have limited academic papers but rich industry documentation. Academic methodology must adapt when researching commercial tools.

3. **Domain boundaries are fluid**: NPC research (Domain 5) overlaps with Quest/Dialogue (8c) and Multi-Agent Systems (8d). Clean categorization is sometimes impossible.

4. **Recent papers dominate tool-specific domains**: For UE5 and Houdini, most resources are 2023-2025 documentation rather than peer-reviewed papers.

5. **AI amplifies, doesn't replace**: Claude Code accelerated my search but required my judgment for relevance filtering, quality assessment, and strategic direction. The methodology is AI-*assisted*, not AI-*automated*.

### Value of This Approach

For other researchers considering AI-assisted literature reviews:

- **Best for**: Interdisciplinary topics, cross-domain discovery, comprehensive scoping
- **Requires**: Human oversight, verification of AI outputs, domain expertise for filtering
- **Produces**: Broad coverage quickly, but depth requires traditional reading

This scoping search gives me a map of the territory. Phase 2—the close reading—is where I'll chart my specific path through it.
