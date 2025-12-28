# Domain 1: LLMs & Transformers

## Overview

Large Language Models and the Transformer architecture represent the foundational technology enabling modern AI tools for content generation. This domain covers the evolution from attention mechanisms to modern instruction-following models.

**Thesis Relevance:** LLMs are the backbone of AI-assisted worldbuilding - from generating dialogue to creating lore, quest text, and NPC behaviors. Understanding this foundation is essential for applying these tools effectively.

---

## Paper Selection Methodology

Papers selected using tiered citation approach:
- **Tier 1 (>50,000 citations):** MUST include - Mega-foundational
- **Tier 2 (10,000-50,000 citations):** MUST include - Major foundational
- **Tier 3 (1,000-10,000 citations):** Include if venue is strong
- **Tier 4 (<1,000 citations):** Strong justification required

*Citation counts from Google Scholar (December 2025)*

---

## Tier 1: Mega-Foundational Papers (>50,000 citations)

### Vaswani, Shazeer, Parmar et al. (2017) - "Attention Is All You Need"
**209,837 citations** | NeurIPS 2017

The paper that introduced the Transformer architecture:
- **Self-attention mechanism:** Allows modeling dependencies regardless of distance
- **Multi-head attention:** Parallel attention computations for richer representations
- **Positional encoding:** Injects sequence order without recurrence
- **Encoder-decoder architecture:** Foundation for sequence-to-sequence tasks

*Thesis relevance:* THE foundational paper. Every modern AI tool (GPT, Stable Diffusion, etc.) builds on this architecture.

*Venue:* NeurIPS - Premier ML conference

---

### Devlin, Chang, Lee & Toutanova (2019) - "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
**152,304 citations** | NAACL 2019

Bidirectional pre-training that revolutionized NLP:
- **Masked language modeling (MLM):** Predict missing tokens from context
- **Next sentence prediction:** Learn inter-sentence relationships
- **Transfer learning:** Pre-train once, fine-tune for any task
- **Bidirectional context:** Uses both left and right context

*Thesis relevance:* Established the pre-train/fine-tune paradigm that enables adapting models to specific domains like fantasy worldbuilding.

*Venue:* NAACL - Top NLP venue

---

### Brown, Mann, Ryder et al. (2020) - "Language Models are Few-Shot Learners"
**61,197 citations** | NeurIPS 2020

GPT-3 and the emergence of in-context learning:
- **175 billion parameters:** Demonstrated scaling enables emergent capabilities
- **Few-shot learning:** Learn new tasks from just a few examples in the prompt
- **Zero-shot generalization:** Perform tasks with no examples
- **In-context learning:** Task specification through natural language

*Thesis relevance:* Demonstrated that LLMs can handle creative tasks (story generation, dialogue) with minimal fine-tuning - directly applicable to worldbuilding.

*Venue:* NeurIPS - Premier ML conference

---

## Tier 2: Major Foundational Papers (10,000-50,000 citations)

### Radford, Wu, Child, Luan, Amodei & Sutskever (2019) - "Language Models are Unsupervised Multitask Learners"
**20,123 citations** | OpenAI Blog

GPT-2 and the power of scale:
- **1.5 billion parameters:** Showed larger models learn more tasks
- **Zero-shot task transfer:** Single model performs diverse tasks
- **WebText dataset:** Large-scale web corpus for training
- **Autoregressive generation:** Predict next token approach

*Thesis relevance:* Demonstrated language models as general-purpose tools, not just translators or classifiers.

---

### Raffel, Shazeer, Roberts et al. (2020) - "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
**~20,000 citations** | JMLR 2020

T5 and the text-to-text paradigm:
- **Unified framework:** Every NLP task as text-to-text
- **Colossal Clean Crawled Corpus (C4):** Massive training dataset
- **Systematic study:** Compared pre-training objectives, architectures
- **Encoder-decoder transformer:** More flexible than decoder-only

*Thesis relevance:* The text-to-text paradigm simplifies prompt engineering for diverse worldbuilding tasks.

*Venue:* JMLR - Premier ML journal

---

### Touvron, Lavril, Izacard et al. (2023) - "LLaMA: Open and Efficient Foundation Language Models"
**~15,000 citations** | arXiv / Meta AI

Open-source foundation models:
- **7B to 65B parameters:** Range of model sizes
- **Trained on public data only:** No proprietary datasets
- **LLaMA-13B outperforms GPT-3:** Efficiency through better training
- **Open weights:** Enabled ecosystem of fine-tuned models

*Thesis relevance:* Critical for indie developers - open models that can run locally without API costs.

---

## Tier 3: Field-Defining Papers (1,000-10,000 citations)

### Ouyang, Wu, Jiang et al. (2022) - "Training Language Models to Follow Instructions with Human Feedback"
**~8,000 citations** | NeurIPS 2022

InstructGPT and RLHF:
- **Reinforcement Learning from Human Feedback (RLHF):** Align models with human preferences
- **Instruction following:** Models that do what users ask
- **Safety improvements:** Reduced harmful outputs
- **1.3B InstructGPT preferred over 175B GPT-3:** Alignment beats scale

*Thesis relevance:* Explains why ChatGPT/Claude are useful for creative tasks - they're trained to follow instructions, not just predict text.

*Venue:* NeurIPS - Premier ML conference

---

### Wei, Wang, Schuurmans et al. (2022) - "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
**~6,000 citations** | NeurIPS 2022

Prompting for complex reasoning:
- **Chain-of-thought (CoT):** Include reasoning steps in prompts
- **Emergent reasoning:** Only works at scale (>100B parameters)
- **Few-shot CoT:** Provide examples with reasoning traces
- **Zero-shot CoT:** "Let's think step by step"

*Thesis relevance:* Essential technique for complex worldbuilding tasks - designing consistent magic systems, historical timelines, faction relationships.

---

### Chen, Tworek, Jun et al. (2021) - "Evaluating Large Language Models Trained on Code"
**~4,000 citations** | arXiv

Codex and code generation:
- **12B parameter model fine-tuned on code:** GitHub training data
- **HumanEval benchmark:** Standardized code evaluation
- **70% pass@1 on simple tasks:** Substantial code generation capability
- **GitHub Copilot foundation:** Commercial application

*Thesis relevance:* Code generation enables AI-assisted game development - generating shaders, procedural generation scripts, tool code.

---

### Kaplan, McCandlish, Henighan et al. (2020) - "Scaling Laws for Neural Language Models"
**~3,000 citations** | arXiv

Predictable scaling behavior:
- **Power-law relationships:** Performance scales predictably with compute, data, parameters
- **Compute-optimal training:** Guidelines for resource allocation
- **Smooth improvement:** No phase transitions, gradual capability gain
- **Predictive framework:** Estimate performance before training

*Thesis relevance:* Explains why AI tools keep improving - foundation for understanding capability trajectory.

---

### Rozière, Gehring, Gloeckle et al. (2023) - "Code Llama: Open Foundation Models for Code"
**~2,000 citations** | arXiv / Meta AI

Open-source code generation:
- **Based on LLaMA 2:** Fine-tuned for code
- **7B to 70B parameters:** Range of sizes for different hardware
- **Infilling support:** Complete code in the middle
- **Python specialization:** Code Llama - Python variant

*Thesis relevance:* Open-source alternative to Copilot for indie developers - local code generation without API costs.

---

## Evolution of the Field

```
2017: Attention Is All You Need (Transformer)
   ↓
2018: GPT-1, BERT (Pre-training revolution)
   ↓
2019: GPT-2, T5 (Scale and unification)
   ↓
2020: GPT-3, Scaling Laws (Emergent capabilities)
   ↓
2021: Codex (Code generation)
   ↓
2022: InstructGPT, Chain-of-Thought (Alignment & reasoning)
   ↓
2023: LLaMA, Claude, GPT-4 (Open models & multimodality)
   ↓
2024+: Claude 3.5, LLaMA 3, Opus 4.5 (Refined instruction-following)
```

---

## Key Concepts for Thesis

| Concept | Paper | Application |
|---------|-------|-------------|
| **Transformer** | Vaswani 2017 | Architecture behind all modern AI |
| **Pre-training** | Devlin BERT | Train once, adapt to any task |
| **Few-shot learning** | Brown GPT-3 | Learn from examples in prompt |
| **Instruction-following** | Ouyang InstructGPT | Models that do what you ask |
| **Chain-of-thought** | Wei 2022 | Complex reasoning via prompting |
| **Code generation** | Chen Codex | AI-assisted programming |
| **Open models** | Touvron LLaMA | Local deployment without API costs |

---

## Practical Implications for Relics

| Task | Recommended Approach | Key Papers |
|------|---------------------|------------|
| **Lore generation** | Few-shot with examples | GPT-3, Chain-of-thought |
| **NPC dialogue** | Instruction-following models | InstructGPT |
| **Quest design** | Chain-of-thought prompting | Wei 2022 |
| **Procedural code** | Code Llama locally | Rozière 2023 |
| **Local deployment** | LLaMA-based models | Touvron 2023 |

---

## Summary: Papers by Tier

| Tier | Count | Papers |
|------|-------|--------|
| **Tier 1** | 3 | Transformer, BERT, GPT-3 |
| **Tier 2** | 3 | GPT-2, T5, LLaMA |
| **Tier 3** | 4 | InstructGPT, Chain-of-Thought, Codex, Scaling Laws, Code Llama |
| **Total** | 11 | |

---

## BibTeX

See `data/exports/domain_1.bib` for full citations.

## Sources

- [Attention Is All You Need - NeurIPS](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [BERT - ACL Anthology](https://aclanthology.org/N19-1423/)
- [GPT-3 - NeurIPS](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html)
- [LLaMA - arXiv](https://arxiv.org/abs/2302.13971)
