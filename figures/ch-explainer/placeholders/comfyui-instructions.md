# ComfyUI Workflow Screenshots - Instructions

This document provides instructions for creating ComfyUI workflow screenshots for the AI/ML Foundations Explainer chapter.

## Required Screenshots

### Variation 1: Text-to-Image Workflow (Basic)

**Purpose:** Demonstrate the fundamental node-based workflow for generating images from text prompts.

**What to capture:**

1. Open ComfyUI with a basic txt2img workflow
2. Show these essential nodes connected:
   - **Load Checkpoint** (loading a Stable Diffusion model)
   - **CLIP Text Encode** (positive prompt)
   - **CLIP Text Encode** (negative prompt)
   - **Empty Latent Image** (resolution settings)
   - **KSampler** (the denoising process)
   - **VAE Decode** (converting latent to image)
   - **Preview Image** or **Save Image**

**Suggested prompt:** "a cozy medieval tavern interior, warm lighting, detailed"

**Screenshot tips:**

- Zoom to ~80% so all nodes are visible
- Use the default dark theme for readability
- Include the generated image preview in frame
- Resolution: at least 1920x1080

---

### Variation 2: ControlNet Workflow (Intermediate)

**Purpose:** Show how structural guidance (poses, edges, depth) controls image generation.

**What to capture:**

1. Load a ControlNet workflow (pose or depth)
2. Show these nodes:
   - **Load Image** (the control input - pose/depth/edge)
   - **ControlNet Loader**
   - **Apply ControlNet** node
   - Standard txt2img nodes from Variation 1
   - Both the control input AND output visible

**Suggested setup:**

- Use a pose skeleton image as input
- Prompt: "professional dancer on stage, dramatic lighting"
- Show how the output follows the pose

**Key elements to highlight:**

- The control image input
- How ControlNet connects to the main pipeline
- The output matching the control structure

---

### Variation 3: LoRA/Style Workflow (Advanced)

**Purpose:** Demonstrate customization through LoRA models for consistent style or character.

**What to capture:**

1. Workflow with LoRA model integration
2. Show these nodes:
   - **Load LoRA** node
   - Connection to the main model pipeline
   - Before/after comparison if possible (with and without LoRA)

**Alternative:** If you have trained a custom LoRA, show:

- The same prompt with different LoRA weights
- How the style changes based on LoRA influence

---

## Technical Requirements

| Requirement | Specification |
|-------------|---------------|
| Resolution | Minimum 1920x1080 |
| Format | PNG (lossless) or PDF |
| Color depth | 24-bit RGB |
| File naming | `comfyui-workflow-{variation}.png` |

## File Naming Convention

```
figures/ch-explainer/
├── comfyui-workflow-txt2img.png     (Variation 1)
├── comfyui-workflow-controlnet.png  (Variation 2)
├── comfyui-workflow-lora.png        (Variation 3)
└── placeholders/
    └── comfyui-instructions.md      (this file)
```

## Caption Templates

Use these captions in the thesis:

**Variation 1:**
> Figure X: A basic text-to-image workflow in ComfyUI showing the node-based approach to image generation. The workflow loads a Stable Diffusion checkpoint, encodes text prompts, and progressively denoises a latent image.

**Variation 2:**
> Figure X: A ControlNet workflow in ComfyUI demonstrating how structural guidance (in this case, a pose skeleton) constrains the image generation to match a specific composition while the text prompt controls the visual style.

**Variation 3:**
> Figure X: A LoRA-enhanced workflow showing how lightweight fine-tuned adapters can modify model behavior to produce consistent styles or characters without retraining the full model.

## Optional: Same Seed Comparison

If time permits, create a side-by-side comparison showing:

1. Same random seed (e.g., 42)
2. Same settings (steps, CFG, sampler)
3. Different prompts: "cat astronaut" vs "dog astronaut"
4. Result: structurally similar but semantically different images

This demonstrates how the random seed determines image composition while the prompt guides content.

---

## Notes for Thesis Integration

When you have created these screenshots:

1. Place the PNG files in `figures/ch-explainer/`
2. Update `figures/README.md` with the new entries
3. Replace the `[PLACEHOLDER: ComfyUI workflow...]` text in `ai_ml_foundations_explainer.md` with proper figure references
4. Add to List of Figures in thesis YAML frontmatter
