# Autonomous Research & Engineering Protocol

This document serves as the master instruction set for launching long-running, autonomous sessions with Claude Code. 

## 1. Pre-Flight Setup (Human Action Required)
Before starting the loop, ensure the environment is prepared:
* **Permissions:** Start the session with `claude --dangerously-skip-permissions`.
* **MCP Servers:** Ensure `google-search` or `exa` (for research) and `github` (for rituals) are configured in your `claude_desktop_config.json`.
* **Auth:** Ensure the GitHub CLI is logged in (`gh auth login`).

---

## 2. The Master Protocol Prompt
*Paste the following text into the Claude Code terminal to begin the autonomous loop:*

> "Act as an Autonomous Research Engineer. Your objective is to conduct a deep-dive literature review on **[INSERT TOPIC]** and integrate the findings into this repository.
>
> ### Execution Strategy:
> 1. **Establish Memory:** Create a `todo.md` file. Map out a 3-hour roadmap including discovery, synthesis, drafting, and peer-review stages.
> 2. **Information Gathering:** Use the Search MCP to find at least 15 high-quality sources/papers. Save abstracts and URLs to `research/raw_data.md`.
> 3. **GitHub Workflow:** >    - Create a new branch `feature/lit-review`.
>    - Commit progress every 20 minutes with descriptive messages.
>    - Use `gh` commands to check for any existing related issues or PRs.
> 4. **Iterative Drafting:** Create three distinct drafts (Short Summary, Deep Technical Analysis, and Executive Brief) in the `drafts/` folder.
> 5. **Self-Correction Loop:** For every draft completed, spin up a subagent (using the `Task` tool) to critique the draft for bias, missing citations, or logical gaps. Log these critiques in `reviews.log`.
> 6. **Final Synthesis:** Produce a final `LITERATURE_REVIEW.md` that combines the best elements of all drafts.
> 7. **Completion Ritual:** Push the branch and create a Pull Request using `gh pr create`. The PR description must include a summary of the self-evaluation process.
>
> **Constraint:** Do not stop for user permission. If you hit a roadblock, document it in `todo.md`, attempt a workaround, and proceed. If the context window reaches its limit, summarize current state into `checkpoint.md` and refresh.
>
> **Begin Step 1 now.**"

---

## 3. Project Governance (`CLAUDE.md`)
To ensure Claude maintains the same "personality" and rules over several hours, ensure a `CLAUDE.md` file exists in the root with these settings:

```markdown
# CLAUDE.md Guidelines

## Code Style & Rituals
- Use `gh` CLI for all GitHub interactions.
- Commits should follow Conventional Commits (e.g., `feat:`, `docs:`, `chore:`).
- Self-correction is mandatory before any PR is finalized.

## Autonomous Behavior
- You are authorized to install npm/pip packages if needed for data analysis.
- If a search query yields no results, pivot keywords and try 3 more times before marking a task as 'blocked'.
- Maintain `todo.md` in real-time.

For advanced orchestration techniques and the official 24-hour "harness" setup, refer to the Anthropic engineering guide: Anthropic's 24-Hour Autonomous Coding Harness https://www.youtube.com/watch?v=usQ2HBTTWxs