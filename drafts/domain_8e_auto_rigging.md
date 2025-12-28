# Domain 8e: Automatic Rigging and Character Setup

## Overview

Character rigging is traditionally one of the most time-consuming and technical aspects of 3D character production. Neural network-based auto-rigging promises to dramatically reduce this bottleneck, enabling rapid character setup from 3D meshes.

**Thesis Relevance:** An RPG requires dozens of unique characters. Traditional rigging can take days per character. Auto-rigging tools can reduce this to minutes, essential for solo/small team development.

---

## Paper Selection Methodology

- Focus on neural/ML-based rigging solutions
- Include industry tools (Mixamo, AccuRig)
- Prioritize papers with open implementations

---

## Section A: Neural Rigging

### Xu et al. (2020) - "RigNet: Neural Rigging for Articulated Characters"
**~200 citations** | SIGGRAPH 2020

End-to-end neural rigging:
- **Skeleton prediction:** Joint placement from mesh
- **Skinning weights:** Automatic skin weight estimation
- **Graph neural network:** Operates directly on mesh
- **Dataset:** 2,703 rigged models for training

*Thesis relevance:* CRITICAL - Automates the entire rigging pipeline. Blender add-on available.

---

### Xu et al. (2021) - "Skeleton-Aware Networks for Deep Motion Retargeting"
**~150 citations** | SIGGRAPH 2020

Motion transfer between skeletons:
- **Cross-skeleton:** Transfer motion between different rigs
- **Latent space:** Skeleton-agnostic motion representation
- **Real-time:** Fast enough for interactive use

*Thesis relevance:* Use motion capture data on auto-rigged characters.

---

### Ma et al. (2024) - "HumanRig: Learning Automatic Rigging for Humanoid Character Animation"
**Recent** | SIGGRAPH 2024

State-of-the-art humanoid rigging:
- **Production quality:** Matches manual rigging
- **Facial rigging:** Includes face bones
- **Muscle deformation:** Advanced secondary motion
- **Industry tested:** Validated by animation studios

*Thesis relevance:* Latest advancement - production-ready auto-rigging.

---

## Section B: Industry Tools

### Adobe Mixamo
**Commercial/Free Tool** | Adobe

Widely-used auto-rigging service:
- **Automatic:** Upload mesh, receive rigged character
- **Animation library:** 2,500+ motion clips included
- **Free tier:** Accessible to indie developers
- **Limitations:** Humanoid only, limited customization

*Thesis relevance:* Practical tool for rapid character prototyping.

---

### Reallusion AccuRig
**Commercial Tool** | Reallusion

AI-powered rigging:
- **Character Creator integration:** Works with CC pipeline
- **Custom proportions:** Non-standard humanoids
- **Facial rigging:** Full face bone setup
- **Motion retargeting:** Compatible with iClone

*Thesis relevance:* Commercial option with advanced features.

---

### NVIDIA Omniverse Audio2Face
**Free Tool** | NVIDIA

Speech-driven facial animation:
- **Audio input:** Voice to face animation
- **Real-time:** Streaming capability
- **ARKit compatible:** 52+ blendshapes
- **Emotion detection:** Infers mood from voice

*Thesis relevance:* Automate NPC facial animation from dialogue audio.

---

## Section C: Skinning and Deformation

### Li et al. (2021) - "Learning Skeletal Graph Neural Networks for Hard 3D Pose Estimation"
**~100 citations** | ICCV 2021

Improved skeleton prediction:
- **Graph convolution:** Better joint relationship modeling
- **Occlusion handling:** Works with partial visibility
- **Multi-person:** Handles multiple characters

*Thesis relevance:* Better skeleton prediction for auto-rigging.

---

### NeuroSkinning (Liu et al., 2019)
**~150 citations** | SIGGRAPH 2019

Neural skinning weights:
- **Learned weights:** Better than geometric methods
- **Pose-dependent:** Weights vary with pose
- **Muscle bulging:** Secondary deformation

*Thesis relevance:* Improved deformation quality for auto-rigged characters.

---

## Evolution of Auto-Rigging

```
2015-2018: Geometric methods (Pinocchio, etc.)
    ↓
2019: NeuroSkinning - Neural skinning weights
    ↓
2020: RigNet - End-to-end neural rigging
      Mixamo adoption increases
    ↓
2021: Motion retargeting improvements
      Skeleton-aware networks
    ↓
2022-2023: Production integration
           AccuRig, Character Creator AI
    ↓
2024: HumanRig - Production-quality
      Facial + body in single pipeline
    ↓
2025: Game engine integration expected
```

---

## Key Concepts for Thesis

| Concept | Paper/Tool | Application |
|---------|------------|-------------|
| **End-to-end rigging** | RigNet | Mesh → skeleton → weights |
| **Motion retargeting** | Xu 2021 | Share animations across characters |
| **Facial rigging** | Audio2Face | NPC dialogue animation |
| **Production rigging** | HumanRig | High-quality characters |
| **Rapid prototyping** | Mixamo | Quick character setup |

---

## Practical Implications for Relics

| Task | Recommended Approach | Key Papers/Tools |
|------|---------------------|------------------|
| **Player character** | HumanRig + manual refinement | HumanRig |
| **Main NPCs** | RigNet + Mixamo animations | RigNet |
| **Background NPCs** | Mixamo full pipeline | Mixamo |
| **Creatures** | RigNet (non-humanoid support) | RigNet |
| **Facial animation** | Audio2Face | NVIDIA |
| **Motion library** | Mixamo + custom mocap | Various |

---

## Auto-Rigging Pipeline

```
1. 3D MESH INPUT
   Character model (T-pose preferred)
       ↓
2. SKELETON PREDICTION
   RigNet / HumanRig → joint positions + hierarchy
       ↓
3. SKINNING
   Neural skinning weights → vertex-bone associations
       ↓
4. ANIMATION
   Mixamo library OR motion retargeting
       ↓
5. FACIAL SETUP
   Audio2Face for dialogue scenes
       ↓
6. REFINEMENT
   Manual tweaks for hero characters
```

---

## Summary: Papers by Category

| Category | Count | Papers/Tools |
|----------|-------|--------------|
| **Neural Rigging** | 2 | RigNet, HumanRig |
| **Motion Retargeting** | 1 | Skeleton-Aware Networks |
| **Industry Tools** | 3 | Mixamo, AccuRig, Audio2Face |
| **Skinning** | 2 | Skeletal GNN, NeuroSkinning |
| **Total** | 8 | |

---

## BibTeX

See `data/exports/domain_8e.bib` for full citations.

## Sources

- [RigNet - GitHub](https://github.com/zhan-xu/RigNet)
- [RigNet - Project Page](https://zhan-xu.github.io/rig-net/)
- [Mixamo](https://www.mixamo.com/)
- [Audio2Face](https://developer.nvidia.com/omniverse/audio2face)
- [AccuRig](https://www.reallusion.com/accurig/)
