# Research Strategy & Thesis Planning

## Project Summary

**Working Title (EN):** *Worlds Within Reach: AI-Assisted Worldbuilding for Independent Development*

**Working Title (DE):** *Welten denken, Welten erschaffen: KI im kreativen Workflow*

**Central Question:** Can AI and procedural tools restore the creator-to-creation ratio that existed before games went 3D?

**Focus:** Investigating how AI and procedural generation can enable small teams (or solo developers) to create open-world RPG experiences that previously required large studios and massive budgets.

**Lens:** Role-playing games as the example—because they demand the full stack: world, characters, systems, narrative, interactivity.

**Deliverable:**

- Playable world prototype (single biome/region)
- Worldbuilding Bible
- Concept art and environment documentation
- Thesis documenting the process and reflecting on feasibility

**Format:** APA 7, practice-based Master's thesis (40-70 pages)

---

## The Core Tension

```text
Pen & Paper Era        →    3D Game Era              →    AI Era (?)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1 person creates       →    100+ people needed       →    Small team again?
entire world                 for same scope

Writing + sketches     →    3D modeling, texturing,  →    AI handles the
= complete game              rigging, animation...        "slave work"?

Creative work: 100%    →    Creative work: ~10%      →    Creative work: ↑↑?
```

---

## The Ethical Dimension

| AI for Extraction | vs. | AI for Creation |
|-------------------|-----|-----------------|
| Cut costs, fire artists | | Empower small teams |
| Generate slop at scale | | Enable visions that couldn't exist |
| Shareholders happy | | Creators happy |
| Less soul, more volume | | More soul, feasible scope |

**Side Question:** How is AI being used for exploitation in games, and how can it be used for genuine creative empowerment instead?

---

## Your Approach vs. The Frontier

| Approach | What It Means | Maturity |
|----------|---------------|----------|
| **Your approach** | AI assists at each stage (concept art, textures, dialogue), human directs | Production-ready now |
| **Genie-style** | AI generates entire playable world from prompt | Research only, not production-ready |

Your thesis acknowledges the frontier while arguing for the practical middle ground: **enhanced traditional workflows**.

---

## Foundational Literature: The Complete AI Pipeline

Organized from simple to complex, building upon each layer.

### Level 1: Language Models & Transformers (Text Foundation)

The base layer—everything else builds on this.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Vaswani et al., "Attention Is All You Need"** | 158,585 | 2017 | THE transformer paper. Everything builds on this. |
| **Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers"** | 106,985 | 2019 | Bidirectional understanding, changed NLP |
| **Brown et al., "GPT-3: Language Models are Few-Shot Learners"** | 51,425 | 2020 | Proved scale works, few-shot learning |
| Wei et al., "FLAN: Finetuned Language Models Are Zero-Shot Learners" | 4,529 | 2021 | Instruction tuning |

**Read:** Vaswani (skim for concepts), Brown (understand capabilities)

---

### Level 2: Vision-Language Bridge

Connects text understanding to visual understanding.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Radford et al., "CLIP: Learning Transferable Visual Models from Natural Language Supervision"** | 40,232 | 2021 | Connects text and images. Enables everything below. |

**Read:** Radford (essential for understanding text-to-image)

---

### Level 3: Text-to-Image

From words to pictures.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Goodfellow et al., "Generative Adversarial Networks"** | 30,299 | 2014 | Original GAN paper, historical context |
| **Rombach et al., "High-Resolution Image Synthesis with Latent Diffusion Models"** | 20,577 | 2021 | THE Stable Diffusion paper. Made diffusion practical. |
| Podell et al., "SDXL: Improving Latent Diffusion Models" | 3,674 | 2023 | Current state-of-the-art open model |

**Read:** Rombach (essential), Goodfellow (skim for historical context)

---

### Level 4: Text-to-Video

Adding temporal dimension.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Blattmann et al., "Align Your Latents: Video LDM"** | 1,398 | 2023 | Extended Stable Diffusion to video |
| Zheng et al., "Open-Sora: Democratizing Efficient Video Production" | 452 | 2024 | Open-source Sora alternative |
| Karaarslan & Aydin, "Review of OpenAI Sora, Stable Diffusion, Lumiere" | 17 | 2024 | Survey of text-to-video models |

**Read:** Blattmann (understand the approach)

---

### Level 5: 3D Representations

How to represent 3D scenes for neural rendering.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields"** | ~10,000+ | 2020 | Revolutionary neural scene representation |
| Barron et al., "Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields" | 2,177 | 2021 | Extended NeRF to unbounded scenes |
| **Kerbl et al., "3D Gaussian Splatting for Real-Time Radiance Field Rendering"** | 6,261 | 2023 | Real-time rendering, current SOTA |
| Pumarola et al., "D-NeRF: Neural Radiance Fields for Dynamic Scenes" | 1,743 | 2020 | Dynamic/animated scenes |

**Read:** Mildenhall (foundational), Kerbl (current state-of-art)

---

### Level 6: Text/Image to 3D

Generating 3D assets from prompts.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Poole et al., "DreamFusion: Text-to-3D using 2D Diffusion"** | 3,094 | 2022 | THE text-to-3D paper |
| **Lin et al., "Magic3D: High-Resolution Text-to-3D Content Creation"** | 1,411 | 2022 | Faster/better than DreamFusion |
| Raj et al., "DreamBooth3D: Subject-Driven Text-to-3D Generation" | 267 | 2023 | Personalized 3D generation |

**Read:** Poole (foundational), Lin (improvements)

---

### Level 7: Procedural Content Generation

Traditional and AI-enhanced procedural methods.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Togelius et al., "Search-Based PCG: A Taxonomy and Survey"** | 751 | 2011 | THE PCG survey, established the field |
| **Summerville et al., "Procedural Content Generation via Machine Learning (PCGML)"** | 425 | 2017 | Bridges classic PCG and ML |
| Shaker, Togelius, Nelson, *Procedural Content Generation in Games* (textbook) | 147 | 2016 | Comprehensive textbook, free online |

**Read:** Togelius (survey), Summerville (ML approach), Shaker textbook (chapters 1-4, terrain)

---

### Level 8: NPCs & Believable Agents

Making characters feel real.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Bates, "The Role of Emotion in Believable Agents"** | 1,413 | 1994 | THE classic on making NPCs feel real |
| Loyall, "Believable Agents: Building Interactive Personalities" | 280 | 1997 | Practical implementation of Bates' ideas |
| Loyall & Bates, "Personality-rich Believable Agents That Use Language" | 172 | 1997 | Language and personality |
| **Park et al., "Generative Agents: Interactive Simulacra of Human Behavior"** | 2,875 | 2023 | LLM-powered NPCs. The modern foundation. |

**Read:** Bates (foundational), Park (essential modern work)

---

### Level 9: Code Generation

AI-assisted programming.

| Paper | Citations | Year | Why Foundational |
|-------|-----------|------|------------------|
| **Chen et al., "Codex: Evaluating Large Language Models Trained on Code"** | 7,526 | 2021 | Powers GitHub Copilot |

**Read:** Chen (understand capabilities and limitations)

---

### Level 10: Generative Interactive Worlds (The Frontier)

Where the field is heading—not production-ready, but important context.

| Paper | Citations | Year | Why Important |
|-------|-----------|------|---------------|
| **Bruce et al., "Genie: Generative Interactive Environments"** | 341 | 2024 | Google DeepMind. Generates playable worlds from images/text. |
| Kazemi et al., "Learning Generative Interactive Environments by Trained Agent Exploration" | 3 | 2024 | GenieRedux implementation |

**Read:** Bruce (understand the frontier, good for reflection section)

---

### Worldbuilding & RPG Theory

The domain-specific literature.

| Paper/Book | Citations | Year | Why Foundational |
|------------|-----------|------|------------------|
| **Wolf, *Building Imaginary Worlds: The Theory and History of Subcreation*** | 298 | 2012 | THE academic text on worldbuilding |
| **Jenkins, *Convergence Culture*** | 3,514 | 2006 | Transmedia storytelling, world across media |

**Read:** Wolf (essential for worldbuilding theory), Jenkins (transmedia context)

---

## Thesis Outline

### 1. Introduction (4-6 pages)

- The Skyrim problem: open-world RPGs need 100+ people and $100M+
- The risk: AI as cost-cutting tool → soulless content
- The opportunity: AI as creative leverage → accessible creation
- Research question and scope
- What this thesis will and won't cover

---

### 2. Background: From Pen & Paper to Digital Worlds (10-14 pages)

**2.1 The Tabletop Foundation**

- Worldbuilding in pen & paper RPGs
- One person could create an entire game world
- The creative process: writing, sketching, rules, lore
- What makes tabletop RPGs work (character creation, choice, roleplay)

**2.2 The 3D Revolution and Its Costs**

- Evolution from tabletop to digital RPGs
- What Skyrim/open-world RPGs require
- Why the team size exploded
- The current state of AAA development (cost, time, team size)

**2.3 What Makes an Open-World RPG**

- Core elements: open world, character creation, choice, roleplay
- Skyrim vs. Witcher example (character creation as key differentiator)
- The "big world" dream and what it requires

**Key Sources:**

- Wolf, *Building Imaginary Worlds* (298 citations)
- Jenkins, *Convergence Culture* (3,514 citations)
- Game development post-mortems
- AAA development cost studies

---

### 3. The AI-Assisted Creation Pipeline: A Tool Survey (18-25 pages)

Theory section organized as a progression from simple to complex, building upon each layer.

---

#### 3.1 Foundation: Language Models & Transformers

**What They Enable:**

- Text generation (lore, dialogue, descriptions)
- Research and synthesis
- Reasoning and planning

**Foundational Papers:**

| Paper | Citations | Year |
|-------|-----------|------|
| Vaswani et al., "Attention Is All You Need" | 158,585 | 2017 |
| Brown et al., "GPT-3" | 51,425 | 2020 |

**Tools:** ChatGPT, Claude, local LLMs (Llama, Mistral)

---

#### 3.2 From Text to Images: Visual Generation

**What It Enables:**

- Concept art generation
- Character design exploration
- Environment concepts
- Mood boards and style guides

**Foundational Papers:**

| Paper | Citations | Year |
|-------|-----------|------|
| Radford et al., "CLIP" | 40,232 | 2021 |
| Rombach et al., "Latent Diffusion Models" | 20,577 | 2021 |
| Goodfellow et al., "GANs" | 30,299 | 2014 |

**Tools:** Midjourney, Stable Diffusion, DALL-E, Leonardo AI

---

#### 3.3 From Images to Video: Temporal Generation

**What It Enables:**

- Animated concept visualization
- Cinematic previsualization
- Motion reference generation

**Foundational Papers:**

| Paper | Citations | Year |
|-------|-----------|------|
| Blattmann et al., "Video LDM" | 1,398 | 2023 |
| Open-Sora | 452 | 2024 |

**Tools:** Runway Gen-2, Pika, Sora, Kling

---

#### 3.4 From 2D to 3D: Spatial Representations

**What It Enables:**

- 3D asset generation from images
- Neural scene capture
- Real-time rendering of generated content

**Foundational Papers:**

| Paper | Citations | Year |
|-------|-----------|------|
| Mildenhall et al., "NeRF" | ~10,000+ | 2020 |
| Kerbl et al., "3D Gaussian Splatting" | 6,261 | 2023 |
| Poole et al., "DreamFusion" | 3,094 | 2022 |
| Lin et al., "Magic3D" | 1,411 | 2022 |

**Tools:** Luma AI, Meshy, Tripo3D, CSM, Rodin

---

#### 3.5 Procedural World Generation

**What It Enables:**

- Terrain generation at scale
- Vegetation and prop distribution
- Road networks and infrastructure
- Biome systems

**Foundational Papers:**

| Paper | Citations | Year |
|-------|-----------|------|
| Togelius et al., "Search-Based PCG" | 751 | 2011 |
| Summerville et al., "PCGML" | 425 | 2017 |
| Shaker et al., PCG Textbook | 147 | 2016 |

**Tools:** Houdini, Unreal PCG Framework, World Machine, Gaea

---

#### 3.6 NPCs and Runtime Behavior

**What It Enables:**

- Dynamic dialogue generation
- Believable character behavior
- Player-responsive interactions
- Emergent narrative

**Foundational Papers:**

| Paper | Citations | Year |
|-------|-----------|------|
| Bates, "Role of Emotion in Believable Agents" | 1,413 | 1994 |
| Park et al., "Generative Agents" | 2,875 | 2023 |

**Tools:** Inworld AI, Convai, NVIDIA ACE, custom LLM integration

---

#### 3.7 Code and Automation

**What It Enables:**

- Script generation
- Shader code
- Pipeline automation
- Debugging assistance

**Foundational Papers:**

| Paper | Citations | Year |
|-------|-----------|------|
| Chen et al., "Codex" | 7,526 | 2021 |

**Tools:** GitHub Copilot, Claude, Cursor, local code LLMs

---

#### 3.8 The Frontier: Generative Interactive Worlds

**What It Promises:**

- Generate entire playable environments from prompts
- Learn physics and interactions from video
- Create games without traditional game engines

**Why It's Not Ready:**

- Research-stage only
- Requires massive compute
- No fine-grained control
- Can't match production quality

**Foundational Papers:**

| Paper | Citations | Year |
|-------|-----------|------|
| Bruce et al., "Genie" | 341 | 2024 |

**Why You Chose Enhanced Traditional Workflows:**

- Production-ready now
- Human remains in creative control
- Predictable, iteratable results
- Works with existing tools (Houdini, Unreal)

---

### 4. The Worldbuilding Bible: Bridging Written and Digital (6-8 pages)

- What a worldbuilding bible contains
- How it connects to game design documents
- Using AI to generate and maintain consistency
- From written world to 3D realization
- The bible as source of truth for procedural systems

---

### 5. Practical Project: My Process (20-28 pages)

**5.1 Project Scope & Goals**

- What I'm trying to create (single biome/region prototype)
- Why these specific tools were chosen
- Success criteria

**5.2 Written Foundation**

- Worldbuilding bible development
- AI-assisted lore and character creation
- Documentation of the process

**5.3 Visual Development**

- Concept art generation
- Style guide development
- Iteration and refinement process

**5.4 Procedural Environment**

- Houdini terrain and scatter systems
- Houdini → Unreal pipeline
- What worked, what didn't

**5.5 Engine Implementation**

- Unreal integration
- Materials, lighting, atmosphere
- Performance considerations

**5.6 NPC Exploration (if scope allows)**

- Testing LLM-powered dialogue
- Integration challenges
- Observations on believability

**5.7 Production Timeline & Effort**

- Actual time spent per phase
- Comparison to traditional methods (estimated)
- Where AI saved time, where it cost time

---

### 6. Reflection & Implications (10-14 pages)

**6.1 What's Actually Feasible Now**

- Honest assessment of current tools
- Where the hype exceeds reality
- What genuinely works

**6.2 The Remaining Walls**

- What still requires human expertise
- Quality and consistency challenges
- Technical limitations

**6.3 AI for Exploitation vs. Empowerment**

- How corporations use AI to cut corners
- The "slop" problem
- How small teams can use AI differently
- Ethical considerations for the industry

**6.4 Implications for Different Audiences**

- Solo developers and tiny teams
- Small studios
- Larger studios seeking efficiency
- The future of game development labor

**6.5 What This Means for Digital World Creation**

- Beyond games: virtual production, VR, metaverse
- The transferable pipeline
- Where this is heading

---

### 7. Conclusion (3-5 pages)

- Summary of findings
- Answer to the central question
- Limitations of this study
- Future research directions
- Personal reflection

---

## Reading Order

### Phase 1: Absolute Foundations (Week 1-2)

**Must read first—everything else builds on these:**

1. **Vaswani et al., "Attention Is All You Need"** (158,585 citations)
   - Skim for core concepts: attention mechanism, transformer architecture

2. **Brown et al., "GPT-3"** (51,425 citations)
   - Understand what LLMs can do, few-shot learning

3. **Radford et al., "CLIP"** (40,232 citations)
   - How text and vision connect

4. **Rombach et al., "Latent Diffusion Models"** (20,577 citations)
   - How Stable Diffusion works

---

### Phase 2: Domain Foundations (Week 3-4)

**The specific fields you're working in:**

1. **Wolf, *Building Imaginary Worlds*** (298 citations)
   - Worldbuilding theory, chapters 1-3 + relevant sections

2. **Togelius et al., "Search-Based PCG"** (751 citations)
   - PCG fundamentals

3. **Shaker et al., PCG Textbook** (147 citations)
   - Chapters 1-4, terrain chapter
   - Free online: [pcgbook.com](http://pcgbook.com/)

4. **Bates, "Role of Emotion in Believable Agents"** (1,413 citations)
   - Classic NPC theory

---

### Phase 3: Modern Applications (Week 5-6)

**Current state-of-the-art:**

1. **Park et al., "Generative Agents"** (2,875 citations)
   - LLM NPCs, essential modern paper

2. **Poole et al., "DreamFusion"** (3,094 citations)
    - Text-to-3D concepts

3. **Kerbl et al., "3D Gaussian Splatting"** (6,261 citations)
    - Current 3D rendering SOTA

4. **Chen et al., "Codex"** (7,526 citations)
    - AI code generation

---

### Phase 4: Frontier & Context (Week 7-8)

**Where things are heading:**

1. **Bruce et al., "Genie"** (341 citations)
    - Generative worlds, the frontier

2. **Summerville et al., "PCGML"** (425 citations)
    - ML + PCG intersection

3. **Jenkins, *Convergence Culture*** (3,514 citations)
    - Transmedia context (skim relevant chapters)

---

## Key Databases & Sources

| Type | Sources |
|------|---------|
| Academic | Google Scholar, IEEE Xplore, ACM Digital Library, DiGRA |
| Conferences | GDC Vault, AIIDE, FDG, CHI Play, SIGGRAPH |
| Industry | Game Developer (Gamasutra), 80 Level, technical blogs |
| Preprints | arXiv (cs.AI, cs.GR, cs.HC) |
| Tools | Official docs (SideFX, Epic, Inworld), YouTube tutorials |
| Books | Wolf (worldbuilding), Shaker et al. (PCG), Short & Adams (procedural) |

---

## Research Phases

### Phase 1: Foundation (Weeks 1-4)

- Read essential texts (see reading order above)
- Build initial source library for each pipeline stage
- Refine worldbuilding bible concept

### Phase 2: Tool Survey Deep Dive (Weeks 5-8)

- Research each pipeline stage systematically
- Test tools hands-on
- Document capabilities and limitations

### Phase 3: Practical Exploration (Weeks 9-14)

- Begin prototype development
- Document process as you go
- Note what works, what doesn't

### Phase 4: Writing & Reflection (Weeks 15-18)

- Draft thesis chapters
- Complete reflection section
- Revise and finalize

---

## Broader Applications

The pipeline and findings apply beyond games:

| Domain | Application |
|--------|-------------|
| Games | Open-world RPGs, indie development |
| Virtual Production | Film/TV digital environments |
| VR/AR | Immersive world experiences |
| Metaverse | Persistent digital worlds |
| Education | Interactive learning environments |
| Architecture | Visualization and walkthroughs |

RPGs are the lens because they demand everything—but the tools transfer.

---

## Page Distribution Guidelines

- **Introduction + Background:** ~20% (14-20 pages)
- **Tool Survey (Theory):** ~25% (18-25 pages)
- **Practical Project:** ~35% (20-28 pages)
- **Reflection + Conclusion:** ~20% (13-19 pages)

**Appendices (not counted):**

- Full Worldbuilding Bible
- Technical breakdowns and node graphs
- Extended asset documentation
- Code snippets and configurations

---

## Citation Summary

### Tier 1: Mega-Foundational (>50,000 citations)

- Vaswani "Attention" — 158,585
- Devlin "BERT" — 106,985
- Brown "GPT-3" — 51,425

### Tier 2: Major Foundational (10,000-50,000 citations)

- Radford "CLIP" — 40,232
- Goodfellow "GANs" — 30,299
- Rombach "Latent Diffusion" — 20,577

### Tier 3: Field-Defining (1,000-10,000 citations)

- Chen "Codex" — 7,526
- Kerbl "Gaussian Splatting" — 6,261
- Wei "FLAN" — 4,529
- SDXL — 3,674
- Jenkins "Convergence Culture" — 3,514
- DreamFusion — 3,094
- Park "Generative Agents" — 2,875
- Mip-NeRF 360 — 2,177
- D-NeRF — 1,743
- Magic3D — 1,411
- Bates "Believable Agents" — 1,413
- Video LDM — 1,398

### Tier 4: Important Modern Work (100-1,000 citations)

- Togelius "Search-Based PCG" — 751
- Open-Sora — 452
- Summerville "PCGML" — 425
- Genie — 341
- Wolf "Building Imaginary Worlds" — 298
- Loyall "Believable Agents" — 280
- DreamBooth3D — 267
- Shaker PCG Textbook — 147

---

## Notes

- A single biome/region prototype is sufficient. Don't promise an entire world.
- The tool survey is meant to be useful to others—think "encyclopedia" not "exhaustive list"
- Honest reflection matters more than proving AI is amazing
- Document failures as much as successes
- Your approach (enhanced traditional) is a valid choice vs. fully generative (Genie-style)

---

## Appendix A: Title Options

### Main Titles

**English:** Worlds Within Reach, Dreams of Scale, Worldbuilding at Scale, Scaling Imagination, Building Digital Worlds, Reclaiming Scale

**Deutsch:** Welten erschaffen, Vom Traum zur Welt, Grenzenlose Welten, Weltenbau neu gedacht, Kreativität entfesseln, Welten denken Welten bauen, Die Kunst des Weltenbaus

### Subtitles

**English:** AI-Assisted Worldbuilding for Open-World Games, AI-Assisted Worldbuilding for Independent Development, Tools Methods and Practice for Worldbuilding

**Deutsch:** Weltenbau mit KI-Unterstützung, KI als Werkzeug für Weltenbauer, Wie KI das Weltenschaffen verändert, Neue Werkzeuge für alte Träume

---

## Appendix B: Vision Inputs (Original Voice)

*Raw thoughts and motivations captured from planning conversations.*

### Core Motivation

> "What drives me the most is making a game like Skyrim myself. Like, no one knows how to do it using those tools."

> "The awesome thing about the game is that you can run around some big world and pick a character. This is what I especially like about Skyrim vs The Witcher. I mean, though The Witcher is objectively the better game, you can create your character in the beginning, which is a huge part."

> "I kinda wanna do all this to see how I can make this world, a world like that. Faster, more procedurally, make it fun and not just hard manual labor that I cannot do alone."

### The Industry Problem

> "That's very expensive because the current gaming industry is shit because it's just driven by people that don't have a passion and they just wanna make money. It's too hard for small studios to make these really big games but maybe we got opportunities to do so now with AI."

> "The big risk is that these corporations are going to use AI to make just slop and bad things."

### Scope & Audience

> "I don't know if I'm confident enough to say solo dev, but I mean back in the day, one person could create an entire pen and paper game and still can, so yeah."

> "Maybe this is just in a sense a survey and toolkit for small teams."

### Worldbuilding Philosophy

> "I kinda wanna talk about world-building basics, especially like role-play. The example of a role-playing game which requires a world and setting."

> "With tabletop role-playing games, it was made on paper, but now it has to be made digitally and ideally in 3D. Big worlds and stuff like that."

### The AI Toolkit Vision

> "You can generate text with it, research with it. Create characters, worlds like in a written form. But also to start to create concept images and concept art basically."

> "I could generate concept images, concept 3D things, environments, textures, video, like text code, and yeah, also NPCs on runtime."

### Key Themes

1. **Democratization** — Making big-world game creation accessible to small teams/solo devs
2. **The Pen & Paper Parallel** — One person could create entire RPG worlds on paper; can AI restore that?
3. **Creative vs. Slave Work** — AI should handle tedious labor, humans should stay creative
4. **Ethical Stakes** — AI for slop vs. AI for genuine creative empowerment
5. **Full Pipeline** — From writing to concept art to 3D to engine to runtime NPCs
6. **Skyrim as North Star** — Open world, character creation, choice, roleplay, big world

---

*Last updated: 2025-12-25*
