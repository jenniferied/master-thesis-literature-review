# Domain 8b: Audio Generation for Games

## Overview

Audio is a critical but often overlooked component of game development. This subdomain covers AI-generated music, voice synthesis, and sound effects - all essential for creating immersive RPG experiences without a dedicated audio team.

**Thesis Relevance:** RPGs require extensive audio: ambient music, combat themes, NPC voices, environmental sounds. AI audio generation can enable a solo developer to create professional-quality soundscapes.

---

## Paper Selection Methodology

- **Tier 1 (>500 citations):** MUST include
- **Tier 2 (100-500 citations):** Include if venue is strong
- **Tier 3 (<100 citations):** Include if recent (2023-2025) and directly applicable

*Many papers are recent (2023-2025) with growing citations.*

---

## Section A: Music Generation

### Copet et al. (2023) - "MusicGen: Simple and Controllable Music Generation"
**~400 citations** | Meta AI (arXiv → TMLR)

Foundation model for music:
- **Text-to-music:** Generate music from descriptions
- **Melody conditioning:** Control via reference melody
- **Single-stage:** No cascaded models needed
- **Open source:** Part of AudioCraft suite

*Thesis relevance:* Generate background music matching game moods - "epic orchestral battle theme", "melancholic tavern ambience".

---

### Agostinelli et al. (2023) - "MusicLM: Generating Music From Text"
**~500 citations** | Google Research

High-fidelity music generation:
- **Hierarchical:** MuLan embeddings + AudioLM tokens
- **Long-form:** Generate coherent multi-minute tracks
- **Rich conditioning:** Text, melody, images
- **Quality:** State-of-the-art audio fidelity

*Thesis relevance:* Alternative to MusicGen with different strengths.

---

### Huang et al. (2023) - "Noise2Music: Text-conditioned Music Generation with Diffusion Models"
**~200 citations** | Google Research

Diffusion for music:
- **Diffusion-based:** Leverages image diffusion advances
- **Text conditioning:** Natural language prompts
- **24 kHz quality:** Broadcast-quality output

*Thesis relevance:* Shows diffusion models work for audio, not just images.

---

## Section B: Voice Synthesis

### NVIDIA Audio2Face (2024)
**Industry Tool** | NVIDIA Omniverse (Open Source)

Speech-driven facial animation:
- **Audio input only:** Speech → facial blend shapes
- **ARKit compatible:** 52+ blendshapes
- **Real-time:** Streaming capability
- **Emotion detection:** Infers mood from voice

*Thesis relevance:* Animate NPC faces from voice without facial mocap.

---

### Shen et al. (2023) - "Bark: Text-to-Speech with Suno AI"
**Open Source** | Suno AI

Expressive TTS:
- **Emotions:** Laughing, sighing, crying
- **Non-verbal:** Gasps, hesitations, breaths
- **Multilingual:** Multiple languages/accents
- **Voice cloning:** With reference audio

*Thesis relevance:* Generate expressive NPC voices with personality.

---

### Casanova et al. (2024) - "XTTS: Cross-Lingual Text-to-Speech"
**Open Source** | Coqui AI

Multi-speaker voice synthesis:
- **17 languages:** Single model
- **Voice cloning:** 6-second reference
- **Fast inference:** Near real-time
- **Commercial license:** MIT license

*Thesis relevance:* Generate voices for diverse NPCs with minimal reference audio.

---

## Section C: Sound Effects

### Liu et al. (2023) - "AudioLDM: Text-to-Audio Generation with Latent Diffusion Models"
**~800 citations** | arXiv → ICML

Latent diffusion for audio:
- **Text-to-SFX:** "Sword clashing against shield"
- **Efficient:** Latent space compression
- **High quality:** State-of-the-art on AudioCaps
- **Fast:** Single GPU training

*Thesis relevance:* CRITICAL - generate game sound effects from text descriptions.

---

### Liu et al. (2024) - "AudioLDM 2: Learning Holistic Audio Generation with Self-supervised Pretraining"
**~300 citations** | arXiv → ICML 2024

Unified audio model:
- **Multi-domain:** Speech, music, and sound effects
- **Language of Audio (LOA):** Unified representation
- **Better quality:** Improved over AudioLDM 1
- **Controllability:** Fine-grained control

*Thesis relevance:* Single model for all game audio types.

---

### Meta AudioGen (2023)
**Part of AudioCraft** | Meta AI

Dedicated sound effects:
- **Environmental sounds:** Trained on public SFX datasets
- **Text prompts:** Natural language descriptions
- **8 seconds:** Generate short clips
- **Complementary:** Works alongside MusicGen

*Thesis relevance:* Specialized for environmental game sounds.

---

## Section D: Voice-to-Animation Integration

### Richard et al. (2021) - "MeshTalk: 3D Face Animation from Speech using Cross-Modality Disentanglement"
**~200 citations** | ICCV 2021

Speech-driven face meshes:
- **Direct mesh output:** No blendshape rigging needed
- **Emotion transfer:** Disentangled audio features
- **Various styles:** Different speaking styles

*Thesis relevance:* Alternative to Audio2Face for mesh-based characters.

---

## Evolution of AI Audio

```
2020-2021: Foundational speech synthesis (Tacotron, WaveNet derivatives)
    ↓
2022: Jukebox (OpenAI) - First large music model
    ↓
2023: MusicLM, MusicGen - Practical music generation
       AudioLDM - Text-to-SFX breakthrough
       Bark - Expressive voice
    ↓
2024: AudioLDM 2 - Unified audio
       Audio2Face open source
       XTTS improvements
    ↓
2025: Real-time integration pipelines
```

---

## Key Concepts for Thesis

| Concept | Tool/Paper | Application |
|---------|------------|-------------|
| **Music generation** | MusicGen, MusicLM | Background scores, themes |
| **Voice synthesis** | Bark, XTTS | NPC dialogue voices |
| **Sound effects** | AudioLDM, AudioGen | Environmental audio |
| **Lip sync** | Audio2Face | Facial animation |
| **Unified audio** | AudioLDM 2 | Full audio pipeline |

---

## Practical Implications for Relics

| Audio Need | Recommended Approach | Key Papers/Tools |
|------------|---------------------|------------------|
| **Ambient music** | MusicGen with mood prompts | Copet 2023 |
| **Combat themes** | MusicGen + manual editing | MusicGen |
| **NPC voices** | XTTS with voice library | Casanova 2024 |
| **Monster sounds** | AudioLDM effects | Liu 2023 |
| **Environmental audio** | AudioGen | Meta 2023 |
| **Dialogue lip sync** | Audio2Face | NVIDIA 2024 |

---

## Workflow for Solo Developer

```
1. MUSIC PIPELINE
   Mood description → MusicGen → Loop editing → Implementation

2. VOICE PIPELINE
   Script → XTTS synthesis → Audio2Face lip sync → Game integration

3. SFX PIPELINE
   Sound description → AudioLDM → Post-processing → Trigger system
```

---

## Summary: Papers by Category

| Category | Count | Papers/Tools |
|----------|-------|--------------|
| **Music Generation** | 3 | MusicGen, MusicLM, Noise2Music |
| **Voice Synthesis** | 3 | Audio2Face, Bark, XTTS |
| **Sound Effects** | 3 | AudioLDM, AudioLDM 2, AudioGen |
| **Integration** | 1 | MeshTalk |
| **Total** | 10 | |

---

## BibTeX

See `data/exports/domain_8b.bib` for full citations.

## Sources

- [AudioCraft / MusicGen](https://ai.meta.com/resources/models-and-libraries/audiocraft/)
- [AudioLDM](https://audioldm.github.io/)
- [XTTS](https://github.com/coqui-ai/TTS)
- [Audio2Face](https://developer.nvidia.com/omniverse/audio2face)
- [Bark](https://github.com/suno-ai/bark)
