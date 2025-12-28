# Domain 5: NPCs & Believable Agents

## Overview

Believable agents are autonomous characters that exhibit consistent, emotionally rich behavior that creates the illusion of life. This domain spans from foundational work on emotion in agents (1990s) to modern LLM-powered generative agents (2023+).

**Thesis Relevance:** NPCs are fundamental to RPG immersion. This domain addresses how to create characters that feel alive in the Shadow Realm - from townsfolk to quest-givers to enemies with apparent goals and emotions.

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

### Park, O'Brien, Cai, Morris, Liang & Bernstein (2023) - "Generative Agents: Interactive Simulacra of Human Behavior"
**3,753 citations** | ACM UIST (Best Paper)

Revolutionary work demonstrating LLM-powered agents with:
- **Memory stream:** Complete record of agent experiences
- **Reflection:** Higher-level abstractions from memories
- **Planning:** Action sequences based on character and context
- 25 agents in "Smallville" sandbox demonstrating emergent social behaviors

*Thesis relevance:* Directly applicable to NPC behavior in RPGs. Memory + reflection + planning architecture could enable dynamic, contextual NPC responses.

*Venue:* ACM UIST - Top HCI venue, Best Paper award

---

### Bates (1994) - "The Role of Emotion in Believable Agents"
**2,182 citations** | Communications of the ACM

Foundational paper establishing emotion as central to believability:
- Drew from Disney animation principles (12 principles)
- Defined "believable" as creating "the illusion of life"
- Introduced the Oz Project framework at CMU
- Argued agents need emotions, not just rational planning

*Thesis relevance:* Theoretical foundation for all NPC work. Establishes WHY emotional modeling matters for game characters.

*Venue:* Communications of the ACM - Premier CS publication

---

## Tier 2: Major Foundational Papers (300-1,000 citations)

### Mateas & Stern (2003) - "Façade: An Experiment in Building a Fully-Realized Interactive Drama"
**877 citations** | Game Developers Conference

First fully-realized interactive drama with believable characters:
- Two AI characters (Trip and Grace) with emotional models
- Natural language understanding for player input
- Drama manager for narrative arc control
- Demonstrated feasibility of reactive, emotional NPCs

*Thesis relevance:* Proof that emotionally complex NPCs are achievable. Architecture lessons for dialogue-heavy RPG scenarios.

---

### Reilly (1996) - "Believable Social and Emotional Agents"
**531 citations** | CMU PhD Thesis

Extended Bates' work with computational emotion model:
- Em architecture for emotion generation
- Social relationships between agents
- Personality traits affecting behavior
- Goal-driven behavior modulated by emotion

*Thesis relevance:* Practical architecture for implementing emotional NPCs.

---

### Dias & Paiva (2005) - "Feeling and Reasoning: A Computational Model for Emotional Characters"
**411 citations** | Portuguese Conference on AI (Springer)

Integration of emotion with cognitive reasoning:
- OCC emotion model implementation
- Emotion influencing decision-making
- Appraisal theory in agent architecture

*Thesis relevance:* Shows how to connect emotion models to actual behavior selection.

---

### Loyall (1997) - "Believable Agents: Building Interactive Personalities"
**394 citations** | CMU PhD Thesis

Comprehensive framework for believable agent architecture:
- Hap behavior language
- Layered personality systems
- Natural language integration
- Real-time performance requirements

*Thesis relevance:* Implementation-focused companion to Bates' theoretical work.

---

### Mateas & Stern (2005) - "Structuring Content in the Façade Interactive Drama Architecture"
**385 citations** | AAAI Conference on AI and Interactive Digital Entertainment (AIIDE)

Technical deep-dive into Façade's architecture:
- Joint Dialog Behaviors as atomic units
- Drama manager beat sequencing
- Character consistency mechanisms

*Thesis relevance:* Detailed implementation guide for dialogue-driven NPCs.

*Venue:* AIIDE - Top venue for game AI

---

### Mateas & Stern (2002) - "A Behavior Language for Story-Based Believable Agents"
**339 citations** | IEEE Intelligent Systems

ABL (A Behavior Language) for agent authoring:
- Reactive planning for real-time behavior
- Joint behaviors for character coordination
- Designed specifically for interactive drama

*Thesis relevance:* Practical authoring approach for NPC behaviors.

*Venue:* IEEE Intelligent Systems - High-quality venue

---

## Tier 3: Field-Defining Papers (50-300 citations)

### Park, Zou, Shaw, Hill, Cai et al. (2024) - "Generative Agent Simulations of 1,000 People"
**285 citations** | arXiv

Scaled up generative agents to population level:
- 1,000 agents based on real interview data
- 85% accuracy replicating human survey responses
- Validated against General Social Survey data

*Thesis relevance:* Shows generative agents scale to RPG population sizes.

---

### Mateas & Stern (2003) - "Integrating Plot, Character and Natural Language Processing in Façade"
**274 citations** | Technologies for Interactive Digital Storytelling (TIDSE)

Integration architecture for narrative + NPC + NLU:
- Plot as constraint on character behavior
- Character autonomy within narrative bounds
- NLP for player intent recognition

*Thesis relevance:* How to balance quest-driven plot with NPC autonomy.

---

### Loyall & Bates (1997) - "Personality-Rich Believable Agents That Use Language"
**205 citations** | ACM International Conference on Autonomous Agents

Language generation reflecting personality:
- Verbal tics and speech patterns
- Emotion expressed through language choices
- Real-time generation constraints

*Thesis relevance:* NPC dialogue that reflects character personality.

---

### Elliott & Brzezinski (1998) - "Autonomous Agents as Synthetic Characters"
**179 citations** | AI Magazine

Survey of the field connecting robotics to character AI:
- Bridged academic AI and entertainment applications
- Discussed emotional modeling approaches
- Contextualized CMU work within broader AI

*Thesis relevance:* Good survey of pre-2000 approaches.

*Venue:* AI Magazine - AAAI flagship publication

---

### Demeure, Niewiadomski & Pelachaud (2011) - "How is Believability of a Virtual Agent Related to Warmth, Competence, Personification, and Embodiment?"
**151 citations** | Presence: Teleoperators and Virtual Environments

Empirical study of believability factors:
- Measured user perception of agent believability
- Connected to social psychology (warmth/competence)
- Embodiment effects on perception

*Thesis relevance:* User study methodology for evaluating NPC believability.

---

### Bates, Loyall & Reilly (1991) - "Broad Agents"
**145 citations** | ACM SIGART Bulletin

Early vision paper for the Oz Project:
- Outlined goals for believable agents
- Introduced key terminology
- Set research agenda for the decade

*Thesis relevance:* Historical context for believable agents research.

---

### Uludağlı & Oğuz (2023) - "Non-Player Character Decision-Making in Computer Games"
**57 citations** | Artificial Intelligence Review (Springer)

Recent comprehensive survey of NPC AI:
- FSM, behavior trees, GOAP, utility AI
- ML approaches to NPC behavior
- Comparison of traditional vs. modern methods

*Thesis relevance:* Current state-of-the-art survey directly applicable to implementation decisions.

---

### Kaiya, Naim, Kondic et al. (2023) - "Lyfe Agents: Generative Agents for Low-Cost Real-Time Social Interactions"
**56 citations** | arXiv

Cost-optimized generative agents:
- 10-100x cost reduction vs. Park et al.
- Real-time interaction capable
- Maintained believability at lower cost

*Thesis relevance:* Critical for indie dev context - affordable generative NPCs.

---

## Techniques Summary

| Technique | Era | Best For | Key Papers |
|-----------|-----|----------|------------|
| **Emotional Models (OCC)** | 1990s-2000s | Character reactions | Bates 1994, Reilly 1996 |
| **Behavior Languages** | 2000s | Authored NPC scripts | Mateas ABL 2002, Loyall Hap |
| **FSM/Behavior Trees** | 2000s-present | Game industry standard | Uludağlı survey 2023 |
| **Drama Management** | 2000s | Narrative-driven games | Mateas Façade 2003-2005 |
| **LLM Generative Agents** | 2023+ | Dynamic, emergent NPCs | Park 2023, Lyfe Agents |

---

## Evolution of the Field

```
1990s: Emotion is Central (Bates, Oz Project)
   ↓
2000s: Interactive Drama (Façade, ABL)
   ↓
2010s: Industry Standardization (Behavior Trees, GOAP)
   ↓
2023+: LLM Revolution (Generative Agents)
```

---

## Key Takeaways for Thesis

1. **Emotion is Foundational** - Bates (1994) established that believability requires emotional modeling, not just rational behavior

2. **Façade Proved Feasibility** - Interactive drama with complex NPCs was achievable in 2005 with careful architecture

3. **Generative Agents are Game-Changing** - Park (2023) demonstrates LLMs can create emergent, believable social behavior without manual scripting

4. **Cost is Solvable** - Lyfe Agents shows 10-100x cost reduction while maintaining believability

5. **Memory + Reflection + Planning** - The Park architecture provides a template for RPG NPCs

6. **Traditional Methods Still Valid** - FSM/behavior trees remain industry standard and are well-documented

---

## Implementation Recommendations for Relics

| NPC Type | Recommended Approach | Papers |
|----------|---------------------|--------|
| **Major Characters** | Generative agents with memory | Park 2023 |
| **Quest Givers** | Hybrid: scripted core + LLM dialogue | Mateas ABL + Park |
| **Townspeople** | Cost-optimized generative | Lyfe Agents |
| **Enemies** | Traditional behavior trees | Uludağlı survey |
| **Companions** | Full generative with emotional model | Park + Reilly |

---

## Summary: Papers by Tier

| Tier | Count | Papers |
|------|-------|--------|
| **Tier 1** | 2 | Park Generative Agents, Bates Emotion |
| **Tier 2** | 6 | Façade (3), Reilly, Dias, Loyall thesis |
| **Tier 3** | 6 | Park 1000, Loyall language, Elliott, Demeure, Bates Broad, Uludağlı, Lyfe |
| **Total** | 14 | |

---

## BibTeX

See `data/exports/domain_5.bib` for full citations.

## Sources

- [Generative Agents - ACM DL](https://dl.acm.org/doi/10.1145/3586183.3606763)
- [Bates 1994 - Communications of ACM](https://dl.acm.org/doi/10.1145/176789.176803)
- [Façade Project](https://www.interactivestory.net/)
