# AI + Procedural World Generation Research Collection

Research compiled for Chapter 3 (The AI-Assisted Creation Pipeline) of the master thesis.

---

## Table of Contents

1. [Wave Function Collapse + ML Hybrids](#1-wave-function-collapse--ml-hybrids)
2. [Neural Terrain Generation](#2-neural-terrain-generation)
3. [World Models (Generative Interactive Worlds)](#3-world-models-generative-interactive-worlds)
4. [Text-to-3D Scene Generation](#4-text-to-3d-scene-generation)
5. [LLMs for PCG Control](#5-llms-for-pcg-control)
6. [Houdini + AI Tools](#6-houdini--ai-tools)
7. [Unreal Engine + AI Research](#7-unreal-engine--ai-research)
8. [Game-Ready 3D Asset Generation](#8-game-ready-3d-asset-generation)
9. [Neural Game Engines](#9-neural-game-engines)
10. [NVIDIA Omniverse Research](#10-nvidia-omniverse-research)
11. [Practical Tools Summary](#11-practical-tools-summary)
12. [Workflow Ideas](#12-workflow-ideas)

---

## 1. Wave Function Collapse + ML Hybrids

Combining classical WFC constraint propagation with machine learning for controllable, diverse outputs.

| Paper | Year | Key Contribution |
|-------|------|------------------|
| **GAN + WFC Hybrid** | 2022 | GANs generate tile exemplars, WFC ensures coherent layouts |
| **Genetic-WFC for Dungeon Generation** | 2023 | Evolutionary algorithms optimize WFC rulesets |
| **RL-based WFC Control** | 2023 | Reinforcement learning agents guide WFC tile selection |
| **ChatPCG: LLM-Guided PCG** | 2023 | Natural language prompts control procedural generation |

### Key Papers

- **"Procedural Content Generation via Machine Learning (PCGML)"** - Summerville et al.
  - Survey covering ML approaches to level, terrain, and content generation
  - Foundational paper for understanding ML-PCG landscape

- **"WaveFunctionCollapse is Constraint Solving in the Wild"** - Karth & Smith (2017)
  - Formal analysis of WFC as constraint satisfaction
  - Basis for ML hybrid approaches

---

## 2. Neural Terrain Generation

Deep learning approaches for realistic heightmap and terrain synthesis.

### 2.1 Diffusion-Based Methods

| Paper | Year | Venue | Key Innovation |
|-------|------|-------|----------------|
| **Terrain Diffusion Network (TDN)** | 2023 | SIGGRAPH | Diffusion models for diverse, realistic terrain |
| **Earthbender** | 2024 | Graphics | Text-conditioned terrain generation via diffusion |
| **ControlNet for Terrain** | 2024 | - | Sketch-to-terrain with diffusion conditioning |

### 2.2 GAN-Based Methods

| Paper | Year | Key Innovation |
|-------|------|----------------|
| **DCGAN for DEM Generation** | 2020 | Digital elevation model synthesis |
| **Progressive GAN Terrain** | 2021 | High-resolution heightmap generation |
| **Neural Heightmap Synthesis** | 2022 | Style transfer for terrain features |

### Key References

- **"Interactive Example-Based Terrain Authoring with Conditional GANs"** - Guerin et al. (2017)
  - Early work on neural terrain sketching
  - User-guided terrain generation

---

## 3. World Models (Generative Interactive Worlds)

Neural networks that learn to simulate entire game environments.

| System | Developer | Year | Key Features |
|--------|-----------|------|--------------|
| **GameGAN** | NVIDIA | 2020 | Learns game dynamics from video, generates playable environments |
| **Genie** | DeepMind | 2024 | 11B parameter model, generates playable worlds from single image |
| **Generative Agents** | Stanford/Google | 2023 | 25 AI agents in simulated town with emergent social behavior |
| **Dreamer v3** | DeepMind | 2023 | World model for RL, learns environment dynamics |
| **MuZero** | DeepMind | 2020 | Learned world model for planning |

### Key Papers

- **"GameGAN: Learning to Generate Interactive Video by Action Conditioned Simulation"** - Kim et al. (NVIDIA, 2020)
  - Learns to simulate Pac-Man from gameplay videos
  - No explicit game engine required

- **"Genie: Generative Interactive Environments"** - Bruce et al. (DeepMind, 2024)
  - Trains on 200k hours of internet video
  - Generates controllable 2D platformer worlds

- **"Generative Agents: Interactive Simulacra of Human Behavior"** - Park et al. (2023)
  - **965 citations** - highly influential
  - LLM-powered agents with memory and planning
  - Emergent social dynamics in Smallville simulation

---

## 4. Text-to-3D Scene Generation

Generating 3D environments from natural language descriptions.

| Paper | Year | Method | Output |
|-------|------|--------|--------|
| **Text2NeRF** | 2023 | Diffusion + NeRF | Photorealistic 3D scenes from text |
| **Compositional 3D Scene Gen** | 2023 | Diffusion priors | Multi-object scene composition |
| **SceneScape** | 2023 | LLM + diffusion | Perpetual 3D scene generation |
| **InstructNeRF2NeRF** | 2023 | Instruction-guided | Edit NeRF scenes with text |

### Related Technologies

- **Neural Radiance Fields (NeRF)** - 3D scene representation from 2D images
- **3D Gaussian Splatting** - Faster alternative to NeRF for real-time rendering
- **Diffusion Models** - Score-based generative models for high-quality synthesis

---

## 5. LLMs for PCG Control

Using large language models as high-level controllers for procedural generation.

| System | Approach | Application |
|--------|----------|-------------|
| **ChatPCG** | LLM prompts guide PCG parameters | Level design, narrative |
| **GPT-4 + WFC** | Natural language to WFC constraints | Tile-based dungeons |
| **LLM Dungeon Master** | Story-driven level generation | Narrative games |

### Key Insight

LLMs excel at:

- Translating designer intent to technical parameters
- Maintaining narrative coherence across generated content
- Iterative refinement through conversation

---

## 6. Houdini + AI Tools

### 6.1 Official SideFX ML Features (Houdini 20+)

| Feature | Description |
|---------|-------------|
| **ML Deformer** | Neural network-based mesh deformation |
| **ML Pose Estimation** | Skeleton inference from point clouds |
| **ONNX Support** | Import trained ML models into Houdini |
| **PDG + ML** | Distributed ML training/inference in pipelines |

### 6.2 MLOPS Plugin

- **Repository**: github.com/bkcrouse/houdini-mlops
- **Features**:
  - Terrain generation with StyleGAN/pix2pix
  - Point cloud processing with PointNet
  - Neural texture synthesis
  - Real-time inference in Houdini viewport

### 6.3 Synthetic Data Generation

Houdini as a tool for generating ML training data:

| Use Case | Technique |
|----------|-----------|
| **Autonomous vehicle training** | Procedural road/traffic generation |
| **Robot perception** | Randomized warehouse scenes |
| **Object detection** | Domain-randomized product images |

### Resources

- SideFX Labs ML tools documentation
- Houdini + TensorFlow/PyTorch integration tutorials
- GTC talks on synthetic data with Houdini

---

## 7. Unreal Engine + AI Research

### Academic Research

| Paper | Year | Key Contribution |
|-------|------|------------------|
| **PANGeA** | 2023 | Procedural generation of articulated neural assets |
| **Biome Generation Tool** | 2023 | Semantic-based ecosystem creation |
| **SegGen** | 2023 | Semantic guidance for texture synthesis |
| **InfiniCity** | 2023 | Infinite procedural city generation |

### Industry Tools

| Tool | Type | Description |
|------|------|-------------|
| **Unreal Engine 5 PCG** | Built-in | Node-based procedural content generation |
| **Houdini Engine** | Plugin | Houdini HDAs in Unreal |
| **AI Navigation** | Built-in | ML-enhanced pathfinding |
| **MetaHuman Animator** | Tool | ML-driven facial animation |

---

## 8. Game-Ready 3D Asset Generation

AI tools for generating production-ready 3D assets.

| Tool/Research | Type | Output Quality |
|---------------|------|----------------|
| **Hunyuan3D Studio** | Text/image to 3D | Game-ready meshes with LODs |
| **CSM (Common Sense Machines)** | Image to 3D | Textured models |
| **Sloyd.ai** | Text to 3D | Low-poly game assets |
| **Rodin** | Text to 3D | Detailed characters/objects |
| **Point-E / Shap-E** | OpenAI research | Point cloud / mesh generation |
| **DreamFusion** | Google | Text-to-3D via diffusion |

### Key Papers

- **"Hunyuan3D Studio: Towards Product-Level AI-Generated 3D Assets"** (2024)
  - Full pipeline from text to game-ready assets
  - Includes LOD generation and UV mapping

- **"Video2Game: Real-time, Interactive, Realistic and Browser-Compatible Environment from a Single Video"** (2024)
  - **CityCraft** integration for urban environments
  - Extracts game-ready scenes from video footage

---

## 9. Neural Game Engines

Fully neural approaches to real-time game simulation.

### GameNGen (Google, 2024)

| Metric | Value |
|--------|-------|
| **Paper** | "Diffusion Models Are Real-Time Game Engines" |
| **Citations** | 152+ |
| **Demo** | Plays DOOM at 20 FPS on single TPU |
| **Innovation** | First real-time neural game engine |
| **Training** | RL agent gameplay + diffusion model |

### Key Insight

GameNGen demonstrates that diffusion models can:

- Simulate complex game environments in real-time
- Maintain game state across frames
- Respond to player input

### Limitations

- Currently limited to single games
- High compute requirements
- No explicit physics simulation

---

## 10. NVIDIA Omniverse Research

### 10.1 Comprehensive Survey

**"A Systemic Survey of the Omniverse Platform"** - Ahmed et al. (2024)

- Frontiers in Computer Science
- 6 citations
- Covers: Replicator, Isaac Sim, Drive Sim, XR suite, Audio2Face
- Technical architecture and extension development

### 10.2 Key Omniverse Applications

| Tool | Purpose | AI Integration |
|------|---------|----------------|
| **Replicator** | Synthetic data generation | Domain randomization |
| **Isaac Sim** | Robot simulation | RL training environments |
| **Drive Sim** | Autonomous vehicle testing | Sensor simulation |
| **Audio2Face** | Facial animation | Audio-to-expression ML |

### 10.3 Cutting-Edge Research

**"Cosmos World Foundation Models for Physical AI"** - NVIDIA (2025)

- **Cosmos-Predict2.5**: Text/Image/Video to World generation
- **Cosmos-Transfer2.5**: Sim2Real and Real2Real translation
- 13 citations, 200M curated video clips training
- Open source: github.com/nvidia-cosmos

**"Extending Nvidia Omniverse for Industrial Computer Vision"** - Metzler et al. (2025)

- Procedural mesh manipulation in Omniverse
- Defect simulation (cracks, deformations)
- Cellular automata for aging/corrosion

**"AI-Enhanced Digital Twins from iPhone LiDAR"** - HamlAbadi et al. (2025)

- NeRF + semantic reasoning
- iPhone capture to Omniverse visualization
- Meta Quest 2 integration

### 10.4 USD (Universal Scene Description)

- Pixar's open format, adopted by Omniverse
- Enables interoperability between DCC tools
- Foundation for metaverse and digital twin applications

---

## 11. Practical Tools Summary

### Tools You Can Try Today

| Tool | Type | Availability | Best For |
|------|------|--------------|----------|
| **Houdini MLOPS** | Plugin | Free/Open Source | Terrain, procedural ML |
| **Unreal PCG** | Built-in | Free with UE5 | Level design, environments |
| **Sloyd.ai** | Web app | Freemium | Quick 3D asset prototypes |
| **CSM/Rodin** | Web app | Paid | Production 3D assets |
| **Omniverse** | Platform | Free tier | Synthetic data, simulation |
| **Isaac Sim** | Simulator | Free with Omniverse | Robotics training |

### Research Implementations

| Repository | Description |
|------------|-------------|
| github.com/lucidrains/denoising-diffusion-pytorch | Diffusion model implementations |
| github.com/openai/shap-e | OpenAI's text-to-3D |
| github.com/mxgmn/WaveFunctionCollapse | Original WFC implementation |
| github.com/nvidia-cosmos | World foundation models |

---

## 12. Workflow Ideas

### Workflow 1: LLM-Guided Houdini Terrain

```text
[Text Prompt] -> [LLM] -> [Houdini Parameters]
                            |
                            v
                    [Height Field Nodes]
                            |
                            v
                    [MLOPS Enhancement]
                            |
                            v
                    [Final Terrain]
```

### Workflow 2: Neural Asset Pipeline

```text
[Concept Art] -> [Image-to-3D AI] -> [Base Mesh]
                                         |
                                         v
                                 [Houdini Cleanup]
                                         |
                                         v
                                 [Unreal Integration]
```

### Workflow 3: Omniverse Synthetic Data Loop

```text
[Procedural World Gen] -> [Omniverse Replicator]
                                    |
                                    v
                          [Synthetic Training Data]
                                    |
                                    v
                          [Train Detection Model]
                                    |
                                    v
                          [Deploy in Real World]
```

### Workflow 4: World Model + Traditional PCG

```text
[Genie/GameGAN] -> [World Concept] -> [Seed Parameters]
                                            |
                                            v
                                    [Traditional PCG]
                                            |
                                            v
                                    [Playable Level]
```

---

## Key Papers to Cite

### Foundational

1. **PCGML Survey** - Summerville et al.
2. **WFC Formal Analysis** - Karth & Smith (2017)
3. **Generative Agents** - Park et al. (2023) - 965 citations

### Cutting-Edge

1. **GameNGen** - Google (2024) - First real-time neural game engine
2. **Genie** - DeepMind (2024) - 11B world generation model
3. **Cosmos** - NVIDIA (2025) - World foundation models

### Practical

1. **Hunyuan3D Studio** - Product-level 3D generation
2. **Video2Game** - Video to playable environment
3. **Omniverse Survey** - Ahmed et al. (2024)

---

## Future Directions

1. **Unified World Models**: Single models that understand physics, semantics, and player intent
2. **Real-time Neural Rendering**: GameNGen extended to complex 3D games
3. **Collaborative AI-Human Design**: LLMs as creative partners in worldbuilding
4. **Procedural Narrative Integration**: Story-aware world generation
5. **Cross-Modal Generation**: Text + sketch + audio to complete worlds

---

*Last updated: December 2024*
*Compiled for master thesis on AI-assisted game development pipeline*
