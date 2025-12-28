# Literature Review Checkpoint

Last Updated: 2025-12-28T22:30:00

## THESIS INTENTION (North Star)

**Title:** "Worlds Within Reach: AI-Assisted Worldbuilding for Independent Development"

**The Dream:** Create **Relics** - a Skyrim-scale open-world dark fantasy action RPG set in the Shadow Realm - as a solo developer using AI and procedural tools.

**Central Question:** Can AI and procedural tools restore the creator-to-creation ratio that existed before games went 3D, enabling small teams to create open-world RPG experiences?

**Key Focus:**
- Worldbuilding for **games** (not literature), specifically **RPGs**
- **Medieval fantasy** settings (Shadow Realm, vampires, werewolves, Schattenfieber)
- **Unreal Engine 5.6+** pipeline (Nanite, Lumen, PCG framework)
- **Houdini** and procedural terrain/environment generation
- **Procedural animation** (motion matching, learned locomotion)
- **3D asset generation** and **texture generation**
- Tools that exist TODAY or are emerging - practical focus

**The Tension:** AI can exploit (corporations cutting jobs) or empower (indie devs realizing visions). This thesis explores empowerment.

---

## Session Status
- **Phase:** Domains 2a & 2b COMPLETE, continuing to Domain 5
- **Next Action:** Complete Domain 5 (NPCs & Believable Agents)

## Domain Priority Order
1. **2a: PCG Foundations** - COMPLETE (11 papers, tiered methodology applied)
2. **2b: PCG + AI/ML** - COMPLETE (14 papers, tiered methodology applied)
3. **5: NPCs & Believable Agents** - Pending
4. **7: Worldbuilding Theory** - Pending
5. **1: LLMs & Transformers** - Pending (Foundation, not skipped!)
6. **3: Text-to-Image** - Pending
7. **4: 3D Generation** - Pending
8. **6: Generative Worlds** - Pending
9. **8: Exploratory** - Pending (Animation, Houdini, unexplored)

## Completed Domains
- [ ] Domain 1: LLMs & Transformers
- [x] Domain 2a: PCG Foundations (11 papers, tiered methodology applied)
- [x] Domain 2b: PCG + AI/ML (14 papers, tiered methodology applied)
- [ ] Domain 3: Text-to-Image
- [ ] Domain 4: 3D Generation
- [ ] Domain 5: NPCs & Believable Agents
- [ ] Domain 6: Generative Worlds
- [ ] Domain 7: Worldbuilding Theory
- [ ] Domain 8: Exploratory

## Infrastructure Completed
- [x] Zotero MCP configured (API key + User ID: 13820503)
- [x] GitHub MCP configured
- [x] GitHub CLI authenticated (jenniferied)
- [x] Science MCP configured (arXiv + OpenAlex) - NO API KEY NEEDED
- [x] Papers MCP configured (arXiv, PubMed, bioRxiv, Web of Science) - NO API KEY NEEDED
- [x] Thesis context: context/thesis-vision.md
- [x] CLAUDE.md updated with autonomous behavior rules + Domain 8
- [x] gemini-tips.md deleted (merged into CLAUDE.md)
- [x] Initial infrastructure commit made

## User Info
- **Email:** m.jennifer@outlook.com (for CrossRef/Unpaywall APIs if needed)
- **Zotero User ID:** 13820503

## Domain 2a Papers Found (10 total, tiered)

### Tier 1 (>1,000 citations) - 4 papers
1. Perlin (1985) - "An Image Synthesizer" - ~5,000 citations | SIGGRAPH
2. Prusinkiewicz & Lindenmayer (1990) - L-systems - ~1,600 citations | Springer
3. Togelius et al. (2011) - Search-Based PCG - 1,088 citations | IEEE TCIAIG
4. Shaker et al. (2016) - PCG Textbook - 992 citations | Springer

### Tier 2 (300-1,000 citations) - 1 paper
5. Hendrikx et al. (2013) - PCG Survey - 926 citations | ACM TOMM

### Tier 3 (50-300 citations) - 3 papers
6. Smith & Whitehead (2010) - Expressive Range - 128 citations | ACM Workshop
7. Freiknecht & Effelsberg (2017) - Virtual Worlds Survey - 136 citations | MDPI
8. Dormans (2010) - Graph Grammar Dungeons - 81 citations | ACM Workshop

### Tier 4 (<50 citations, justified) - 2 papers
9. Liapis et al. (2016) - Mixed-Initiative - 31 citations | Book chapter (extends Tier 1)
10. Karth & Smith (2017) - WFC Academic - ~150 citations | ACM FDG

### Excluded
- Stammer (2015) Spelunky - 10 citations, too old
- Gardner (1970) Game of Life - Not peer-reviewed

## Files Created
- `context/thesis-vision.md` - Thesis abstract and Relics project
- `drafts/domain_2a_pcg_foundations.md` - Draft summary (needs revision)
- `data/searches/domain_2a_2025-12-28.json` - Paper metadata
- `data/exports/domain_2a.bib` - BibTeX for Zotero
- `reviews.log` - Critique feedback

## MCPs Available After Restart
```
github  - Git operations
zotero  - Add papers to Zotero collections
science - OpenAlex + arXiv search (FREE)
papers  - arXiv, PubMed, bioRxiv, Web of Science (FREE)
```

## Critique Feedback for Domain 2a
- Add thesis relevance section (how PCG enables small teams)
- Better chronological structure
- Missing: BSP, Voronoi, Diamond-Square algorithms
- Add mixed-initiative PCG discussion (directly relevant to thesis!)
- Include industry examples (Spelunky, Dwarf Fortress, Minecraft)

## Next Session Instructions
When you start a new session, say:
> "Continue the literature review from checkpoint.md"

I will:
1. Read this checkpoint
2. Use MCP tools (science, papers, zotero) for paper discovery
3. Revise Domain 2a with better structure
4. Add papers directly to Zotero collections
5. Continue through all 8 domains
6. Rank papers by: citations, venue prestige, thesis relevance

## Zotero Collection Structure (to create)
```
Thesis/
├── 01-LLMs
├── 02a-PCG-Foundations
├── 02b-PCG-AI-ML
├── 03-Text-to-Image
├── 04-3D-Generation
├── 05-NPCs-Agents
├── 06-Generative-Worlds
├── 07-Worldbuilding
└── 08-Exploratory
```
