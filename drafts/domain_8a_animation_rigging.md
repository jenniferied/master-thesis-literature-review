# Domain 8a: AI Animation & Automatic Rigging

## Overview

Character animation and rigging represent two of the most time-intensive aspects of game development. AI-driven approaches are transforming both fields, from neural motion synthesis that generates animations from text descriptions to automatic rigging that can produce production-ready character setups in minutes rather than days.

**Thesis Relevance:** An open-world RPG requires hundreds of unique animations and dozens of rigged characters. For a solo developer, AI animation and auto-rigging tools are essential force multipliers that can reduce months of work to hours.

---

## Paper Selection Methodology

This domain covers both foundational research (establishing the field) and recent advances (2023-2025 state-of-the-art):

- **Tier 1 (>300 citations):** Field-defining neural animation papers
- **Tier 2 (100-300 citations):** Major advances in motion synthesis
- **Tier 3 (50-100 citations):** Important specialized contributions
- **Tier 4 (<50 citations):** Recent 2023-2025 papers with high relevance

---

## Section A: Foundational Neural Animation

### Tier 1: Foundational (>300 citations)

#### Holden, Saito & Komura (2016) - "A Deep Learning Framework for Character Motion Synthesis and Editing"
**~600+ citations** | ACM TOG (SIGGRAPH 2016)

The paper that launched neural animation:
- **Convolutional autoencoder:** First to apply deep learning to motion synthesis
- **Motion manifold:** Learned continuous space of human motion
- **Editing operations:** Style transfer, motion blending, constraint satisfaction
- **Real-time:** Fast enough for interactive applications

*Thesis relevance:* FOUNDATIONAL - Established that neural networks can learn motion representations. All subsequent work builds on this.

*Venue:* SIGGRAPH - Premier graphics venue

---

#### Holden, Komura & Saito (2017) - "Phase-Functioned Neural Networks for Character Control" (PFNN)
**~443 citations** | ACM TOG (SIGGRAPH 2017)

Neural network animation control:
- **Phase-based weights:** Cyclic function controls network parameters through gait cycle
- **Real-time:** Runs at 60+ fps on consumer hardware
- **End-to-end:** User input → character pose with terrain adaptation
- **Compact:** Single network replaces complex state machines

*Thesis relevance:* CRITICAL - Enables solo dev to create responsive character animation without hand-authoring state machines. Directly applicable to Relics character locomotion.

*Venue:* SIGGRAPH - Premier graphics venue

---

#### Peng, Abbeel, Levine & van de Panne (2018) - "DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills"
**~800+ citations** | ACM TOG (SIGGRAPH 2018)

Physics-based imitation learning:
- **Motion capture → physics:** Learn robust controllers from mocap reference
- **Multiple characters:** Works for humanoids, dinosaurs, dragons, any skeletal structure
- **Diverse skills:** Walking, running, acrobatics, martial arts, dancing
- **Robust:** Recovers from perturbations, handles uneven terrain

*Thesis relevance:* Enables physics-based animation from reference clips. For Relics: robust combat and traversal animation that responds naturally to world physics.

*Venue:* SIGGRAPH - Premier graphics venue

---

### Tier 2: Major Advances (100-300 citations)

#### Holden, Kanoun, Perepichka & Popa (2020) - "Learned Motion Matching"
**~200+ citations** | ACM TOG (SIGGRAPH 2020)

Neural replacement for motion matching:
- **70x memory reduction:** 590MB → 8.5MB for large motion databases
- **Preserves quality:** Matches original motion matching output
- **Scalable:** Works with massive datasets (hours of motion capture)
- **Fast iteration:** Quick retraining when adding new motions

*Thesis relevance:* Makes motion matching practical for indie devs. Massive animation databases in small memory footprint - essential for open-world games with limited resources.

*Venue:* SIGGRAPH - Premier graphics venue

---

#### Peng, Ma, Abbeel, Levine & Kanazawa (2021) - "AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control"
**~300+ citations** | ACM TOG (SIGGRAPH 2021)

Adversarial learning for animation:
- **Style-aware:** Learns motion style from small clip collections
- **No reward engineering:** Discriminator provides natural motion reward
- **Emergent composition:** Blends skills automatically
- **Task completion:** Achieves goals while maintaining natural motion style

*Thesis relevance:* Enables stylized character animation (zombie shamble, heroic stride, wounded limp) without manual reward design. Critical for varied NPC behaviors in Relics.

*Venue:* SIGGRAPH - Premier graphics venue

---

#### Clavet (2016) - "Motion Matching: The Future of Games Animation"
**Industry Standard** | GDC, Ubisoft

The industry technique that changed game animation:
- **Data-driven:** Search mocap database at runtime for best matching pose
- **Responsive:** Frame-level control without blend tree delays
- **Natural transitions:** No state machine artifacts or pop
- **Widely adopted:** For Honor, Far Cry, The Last of Us, Ghost of Tsushima

*Justification:* Industry standard cited by all subsequent academic work. Understanding motion matching is essential for any game animation discussion.

*Thesis relevance:* The baseline technique that learned methods improve upon. UE5.4+ has native motion matching support.

---

## Section B: Text-to-Motion & Recent Advances

### Tier 2-3: State-of-the-Art (2022-2024)

#### Tevet, Raab, Gordon, Shafir, Cohen-Or & Bermano (2022) - "Human Motion Diffusion Model (MDM)"
**~400+ citations** | ICLR 2023

Text-to-motion diffusion:
- **Text prompts:** "A person walks forward, then jumps and waves"
- **Classifier-free guidance:** No external classifier needed
- **Geometric losses:** Foot contact, joint positions, physics constraints
- **State-of-the-art:** HumanML3D benchmark leader (at time of publication)

*Thesis relevance:* Generate prototype animations from text descriptions. Revolutionary for rapid iteration during pre-production.

*Venue:* ICLR - Premier ML conference

---

#### Guo, Mu, Javed, Wang & Cheng (2023) - "MoMask: Generative Masked Modeling of 3D Human Motions"
**~150+ citations** | CVPR 2024

Current state-of-the-art text-to-motion:
- **Masked transformer:** Bidirectional generation with iterative refinement
- **Hierarchical VQ:** Multi-layer discrete motion tokens for high fidelity
- **Best FID:** 0.045 on HumanML3D (vs 0.141 for T2M-GPT)
- **Temporal inpainting:** Edit specific parts of motion sequences

*Thesis relevance:* Best current method for generating animations from text. Practical for prototyping NPC behaviors and player actions.

*Venue:* CVPR - Premier vision conference

---

#### Jiang et al. (2023) - "MotionGPT: Human Motion as a Foreign Language"
**~200+ citations** | NeurIPS 2023

LLM-based motion generation:
- **Unified vocabulary:** Motion tokens + text tokens in single LLM
- **Multi-task:** Text-to-motion, motion captioning, motion prediction, in-between
- **Pre-training:** Large-scale motion-language pre-training
- **Prompt-based:** Question-and-answer format for motion tasks

*Thesis relevance:* Demonstrates that LLMs can understand and generate motion. Opens possibility of conversational animation design.

*Venue:* NeurIPS - Premier ML conference

---

#### Zhang et al. (2023) - "MotionGPT: Finetuned LLMs Are General-Purpose Motion Generators"
**~100+ citations** | AAAI 2024

Alternative LLM approach:
- **Multimodal control:** Text AND single-frame poses for conditioning
- **Efficient fine-tuning:** Only 0.4% of LLM parameters tuned
- **Multimodal prompts:** Unified instruction format

*Thesis relevance:* Efficient approach to motion generation with pose control. Useful for guided animation generation.

---

#### Wu et al. (2024) - "Motion-Agent: A Conversational Framework for Human Motion Generation with LLMs"
**Recent** | arXiv 2024

Conversational motion generation:
- **Multi-turn dialogue:** Complex motion sequences through conversation
- **GPT-4 integration:** Combines MotionLLM with GPT-4 reasoning
- **Editing support:** Modify motions through natural language
- **Versatile tasks:** Generation, editing, understanding in one system

*Thesis relevance:* Enables iterative refinement of animations through conversation. Practical workflow for solo developers.

---

## Section C: Automatic Rigging

### Tier 2: Neural Rigging

#### Xu, Zhou, Kalogerakis, Landreth & Singh (2020) - "RigNet: Neural Rigging for Articulated Characters"
**~200 citations** | SIGGRAPH 2020

End-to-end neural rigging:
- **Skeleton prediction:** Joint placement from mesh using graph neural network
- **Skinning weights:** Automatic skin weight estimation
- **Mesh-agnostic:** Works on diverse character types without assumptions
- **Dataset:** 2,703 rigged models for training

*Thesis relevance:* CRITICAL - Automates entire rigging pipeline. Open-source Blender add-on available. Dramatically reduces character setup time.

*Venue:* SIGGRAPH - Premier graphics venue

---

#### Xu, Zhou, Kalogerakis & Singh (2021) - "Skeleton-Aware Networks for Deep Motion Retargeting"
**~150 citations** | SIGGRAPH 2020

Motion transfer between skeletons:
- **Cross-skeleton:** Transfer motion between different rigs
- **Latent space:** Skeleton-agnostic motion representation
- **Real-time:** Fast enough for interactive use
- **Topology-invariant:** Works across different skeleton structures

*Thesis relevance:* Use motion capture data on auto-rigged characters. Essential for leveraging existing animation libraries.

---

#### Chu et al. (2024) - "HumanRig: Learning Automatic Rigging for Humanoid Character in a Large Scale Dataset"
**Recent** | SIGGRAPH 2024

State-of-the-art humanoid rigging:
- **Large dataset:** 11,434 T-posed meshes with uniform skeleton topology
- **Prior-Guided Skeleton Estimator:** Uses 2D skeleton for initial estimate
- **Production quality:** Matches manual rigging quality
- **Handles AI meshes:** Works with AI-generated 3D characters

*Thesis relevance:* Latest advancement - production-ready auto-rigging that works with AI-generated character models. Critical for AI-driven asset pipeline.

*Venue:* SIGGRAPH - Premier graphics venue

---

### Industry Tools

#### Adobe Mixamo
**Commercial/Free Tool** | Adobe

Widely-used auto-rigging service:
- **Automatic:** Upload mesh, receive rigged character in minutes
- **Animation library:** 2,500+ motion clips included free
- **Free tier:** Accessible to indie developers
- **Limitations:** Humanoid only, limited customization

*Thesis relevance:* Practical tool for rapid character prototyping. First stop for indie dev character setup.

---

#### Reallusion AccuRig
**Commercial Tool** | Reallusion

AI-powered rigging:
- **Character Creator integration:** Works with CC pipeline
- **Custom proportions:** Non-standard humanoids supported
- **Facial rigging:** Full face bone setup
- **Motion retargeting:** Compatible with iClone

*Thesis relevance:* Commercial option with advanced features for production characters.

---

#### NVIDIA Audio2Face
**Free Tool** | NVIDIA Omniverse

Speech-driven facial animation:
- **Audio input:** Voice recording to face animation
- **Real-time:** Streaming capability for dialogue
- **ARKit compatible:** 52+ blendshapes
- **Emotion detection:** Infers mood from voice tone

*Thesis relevance:* Automate NPC facial animation from dialogue audio. Essential for narrative RPG with voiced characters.

---

## Section D: Physics-Based & Specialized Animation

### Motion Datasets

#### Lin et al. (2023) - "Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset"
**~100+ citations** | NeurIPS 2023

Massive motion dataset:
- **15.6M poses:** SMPL-X whole-body annotations
- **81.1K sequences:** From diverse scenes
- **Whole-body:** Face, hands, body in unified format
- **Text annotations:** Frame-level and sequence-level descriptions

*Thesis relevance:* Training data for motion generation models. Enables fine-tuning on specific motion styles.

---

### Surveys

#### Xue et al. (2025) - "Human Motion Video Generation: A Survey"
**Recent** | IEEE TPAMI 2025

Comprehensive survey:
- **200+ papers:** Covers entire field
- **5 phases:** Input → Motion Planning → Generation → Refinement → Output
- **3 modalities:** Vision, text, audio conditioning
- **LLM integration:** First survey to discuss LLMs for motion

*Thesis relevance:* Reference for understanding current landscape and choosing appropriate methods.

---

## Evolution of AI Animation

```
2016: Holden - Deep Learning Motion Synthesis
   ↓
2016: Motion Matching - Industry adoption (Ubisoft)
   ↓
2017: PFNN - Phase-based neural control
   ↓
2018: DeepMimic - Physics-based imitation
   ↓
2020: RigNet - End-to-end neural rigging
      Learned Motion Matching - Scalable data-driven
   ↓
2021: AMP - Adversarial motion priors
      Skeleton-Aware Networks - Motion retargeting
   ↓
2022: MDM - Diffusion for motion
   ↓
2023: MoMask - State-of-the-art text-to-motion
      MotionGPT - LLM-based motion
      Motion-X - Large-scale dataset
   ↓
2024: HumanRig - Production auto-rigging
      Motion-Agent - Conversational generation
      UE5.4 Motion Matching - Engine integration
   ↓
2025: Multi-modal agents, real-time generation
```

---

## Animation + Rigging Pipeline for Relics

```
┌─────────────────────────────────────────────────────────────┐
│                    CHARACTER CREATION                        │
│  AI 3D Generation (Domain 4) → T-posed mesh                 │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    AUTOMATIC RIGGING                         │
│  RigNet / HumanRig → Skeleton + Skinning weights            │
│  (Or Mixamo for rapid prototyping)                          │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    MOTION ACQUISITION                        │
│  Option A: MoMask/MotionGPT → Generate from text            │
│  Option B: Mixamo library → Pre-made animations             │
│  Option C: Motion capture → High-quality reference          │
│  Option D: Physics (DeepMimic/AMP) → Reactive motion        │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    MOTION RETARGETING                        │
│  Skeleton-Aware Networks → Apply to auto-rigged character   │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    RUNTIME CONTROL                           │
│  UE5 Motion Matching → Data-driven character control        │
│  PFNN-style → Terrain-adaptive locomotion                   │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    FACIAL ANIMATION                          │
│  Audio2Face → Dialogue-driven facial motion                 │
│  (Integrated with NPC dialogue system - Domain 5)           │
└─────────────────────────────────────────────────────────────┘
```

---

## Practical Implications for Relics

| Task | Recommended Approach | Key Papers/Tools |
|------|---------------------|------------------|
| **Player locomotion** | UE5 Motion Matching + mocap library | Learned MM, UE5.4+ |
| **Combat animation** | AMP + motion capture reference | Peng 2021 |
| **NPC walking** | Text-to-motion prototyping | MoMask, MotionGPT |
| **Character rigging** | RigNet (open-source) / Mixamo (free) | RigNet, HumanRig |
| **Creature rigging** | RigNet (non-humanoid support) | RigNet |
| **Facial dialogue** | Audio2Face | NVIDIA |
| **Motion library** | Mixamo + custom mocap | Mixamo |
| **Style transfer** | AMP for stylized NPCs | Peng 2021 |

---

## Summary: Papers by Category

| Category | Count | Papers/Tools |
|----------|-------|--------------|
| **Foundational Animation** | 3 | Holden 2016, PFNN, DeepMimic |
| **Motion Matching** | 2 | Clavet, Learned MM |
| **Physics-Based** | 2 | DeepMimic, AMP |
| **Text-to-Motion** | 4 | MDM, MoMask, MotionGPT (x2) |
| **Conversational** | 1 | Motion-Agent |
| **Neural Rigging** | 3 | RigNet, Skeleton-Aware, HumanRig |
| **Industry Tools** | 3 | Mixamo, AccuRig, Audio2Face |
| **Datasets/Surveys** | 2 | Motion-X, Survey |
| **Total** | 20 | |

---

## BibTeX

See `data/exports/domain_8a.bib` for full citations.

## Sources

- [PFNN Project Page](http://theorangeduck.com/page/phase-functioned-neural-networks-character-control)
- [DeepMimic](https://xbpeng.github.io/projects/DeepMimic/)
- [AMP](https://xbpeng.github.io/projects/AMP/)
- [MDM](https://guytevet.github.io/mdm-page/)
- [MoMask](https://ericguo5513.github.io/momask/)
- [MotionGPT](https://motion-gpt.github.io/)
- [RigNet](https://zhan-xu.github.io/rig-net/)
- [HumanRig](https://arxiv.org/abs/2412.02317)
- [Audio2Face](https://developer.nvidia.com/omniverse/audio2face)
- [Mixamo](https://www.mixamo.com/)
- [GDC Motion Matching](https://www.gdcvault.com/play/1023280/)
