# Sources and Evidence Quality

**Accessed:** 2026-11-12.  
**Purpose:** annotated bibliography for [README.md](README.md) and [REPORT.md](REPORT.md).  
**Caution:** links can rot, and a source being linked does not make every claim in it true. The grade reflects what the source is, not whether you should agree with it.

---

## Evidence grades

| Grade | Meaning | Examples |
| --- | --- | --- |
| **A** | Primary design talk, developer interview, source-level audit, formal schema, implemented/tested design | GDC write-ups quoting the developers; Repository Town audit; RTD-009; WILDY design/tests |
| **B** | Practitioner analysis, reference definition, reputable journalism, design essay | *Game Developer* dialogue essays; Wikipedia definitions; RPS interview; 80.lv summary |
| **C** | This synthesis, inference, or a claim that needs playtesting | “Density beats size”; “20–40 deep NPCs”; design recommendations |

A source can be grade A for *what the developer said* and still be weak evidence for *what players enjoy*. Treat practitioner claims as design hypotheses with strong prior plausibility, not controlled findings.

---

## External sources

### Theory and player motivation

1. **MDA framework** — Hunicke, LeBlanc & Zubek.  
   Overview: [Wikipedia](https://en.wikipedia.org/wiki/MDA_framework) · Paper: [PDF](http://www.cs.northwestern.edu/~hunicke/pubs/MDA.pdf)  
   Used for: mechanics → dynamics → aesthetics; discovery, fantasy, narrative, challenge, expression. **Grade B/A.**

2. **Self-determination theory** — autonomy, competence, relatedness.  
   Overview: [Wikipedia](https://en.wikipedia.org/wiki/Self-determination_theory)  
   Ryan & Deci (2000), *Self-determination theory and the facilitation of intrinsic motivation…*: [doi](https://doi.org/10.1037/0003-066X.55.1.68)  
   Ryan, Rigby & Przybylski (2006), *The motivational pull of video games*: [doi](https://doi.org/10.1007/s11031-006-9051-8)  
   Used for: why autonomy/competence/relatedness are the needs beneath the design. **Grade B/A.**

3. **Flow** — challenge–skill balance, clear goals, immediate feedback.  
   Overview: [Wikipedia](https://en.wikipedia.org/wiki/Flow_%28psychology%29)  
   Sweetser & Wyeth (2005), *GameFlow*: [doi](https://doi.org/10.1145/1077246.1077253)  
   Used for: pacing and feedback; why a linear difficulty curve fails in an open world. **Grade B.**

4. **Information-gap curiosity** — Loewenstein (1994), *The psychology of curiosity*.  
   [doi](https://doi.org/10.1037/0033-2909.116.1.75)  
   Used for: curiosity as a specific gap, not “see everything”; why withholding information works. **Grade A for theory, C for application.**

5. **A Theory of Fun for Game Design** — Raph Koster.  
   Book; no stable open link.  
   Used for: fun as pattern recognition/learning; why novelty and mastery sustain interest. **Grade B (design theory).**

### Open-world design

6. **Open world** — definition and design tensions.  
   [Wikipedia](https://en.wikipedia.org/wiki/Open_world)  
   Used for: autonomy as the main draw; nonlinear approach; freedom vs narrative; “Ubisoft towers” critique. **Grade B.**

7. **5 design lessons from *Breath of the Wild*** — Holly Green, *Game Developer*, 2023, summarising GDC 2017/CEDEC 2017 material.  
   [Article](https://www.gamedeveloper.com/design/5-design-lessons-learned-from-i-the-legend-of-zelda-breath-of-the-wild-i-) · [GDC 2017 talk](https://www.youtube.com/watch?v=QyMsF31NdNc)  
   Used for: player-paced travel, triangle design, multiplicative gameplay, variety/scarcity. **Grade A/B.**

8. **10 key quest-design takeaways from *The Witcher 3* and *Cyberpunk 2077*** — Holly Green, *Game Developer*, 2023, summarising Paweł Sasko's GDC 2023 talk.  
   [Article](https://www.gamedeveloper.com/marketing/10-key-takeaways-from-the-quest-design-of-cyberpunk-2077-and-the-witcher-3)  
   Used for: withholding information, emotional impact, human moments, succinctness, signal/noise, dilemmas, delayed/visible consequences, overdesign, MAYA. **Grade A/B.**

9. **“Players don't explore”: exploration anxiety and open-world fatigue** — 80.lv, 2025, summarising Cameron Williams's GDC panel.  
   [Article](https://80.lv/articles/former-gta-6-dev-on-exploration-anxiety-in-open-world-games)  
   Used for: “how far? what's my gain?”, exploration anxiety, analysis paralysis, beeliners, too-large possibility space. **Grade B.**

10. **Environmental storytelling** — definition.  
    [Glossary entry](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms#Environmental_storytelling)  
    Henry Jenkins, *Game Design as Narrative Architecture*, in *First Person: New Media as Story, Performance, and Game* (MIT Press, 2004). Book chapter; no stable open link.  
    Used for: spaces as narrative, player as archaeologist, inference over exposition. **Grade B/A.**

### NPCs and dialogue

11. **Radiant AI / Radiant Story** — goals, schedules, dynamic quests.  
    [Wikipedia](https://en.wikipedia.org/wiki/Radiant_A.I.)  
    Used for: NPC goals and emergent routine; dynamic quest placement; the “organic feel” claim. **Grade B.**

12. **Rockstar on *Red Dead Redemption 2* NPCs** — Wccftech, 2018, quoting Rob Nelson.  
    [Article](https://wccftech.com/rockstar-talks-about-rdr2-evolved-npcs/)  
    Used for: camp conversation → mission/backstory; nuanced choices; detailed interiors; organic discovery. **Grade B.**

13. **Defining Dialogue Systems** — Brent Ellison, *Game Developer*, 2008.  
    [Article](https://www.gamedeveloper.com/design/defining-dialogue-systems)  
    Used for: non-branching/branching/hub-and-spoke/waterfall/systemic/parser; the vending-machine risk; time scheduling; 3–4 options; literal vs paraphrase. **Grade A/B.**

14. **Branching Conversation Systems and the Working Writer, Part 2** — Alexander Freed, *Game Developer*, 2014.  
    [Article](https://www.gamedeveloper.com/design/branching-conversation-systems-and-the-working-writer-part-2-design-considerations)  
    Used for: voiceover trade-offs, hubs vs waterfalls, selection interface, 3–4 options, forced lines, mechanics in dialogue, exact intent. **Grade A/B.**

15. **Dialogue tree / dialogue wheel** — definitions and critique.  
    [Wikipedia](https://en.wikipedia.org/wiki/Dialogue_tree)  
    Used for: authored branches; hub cycles; skills/charisma gates; dialogue-wheel speed vs ambiguity; criticism of paraphrases and mood categories. **Grade B.**

16. **Disco Elysium interview** — Robert Kurvitz with Rock Paper Shotgun, 2018.  
    [Article](https://www.rockpapershotgun.com/disco-elysium-rpg-details)  
    Used for: skills as voices, failure as content, own quests, anti-quest-giver design, personal-first worldbuilding, tenacity. **Grade A/B.**

---

## Internal sources

These are public repos unless noted. They are evidence of **design intent and engineering analysis**, not proof of player experience.

| Source | Role | Grade |
| --- | --- | --- |
| [NPC realism audit](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/NPC_REALISM_AUDIT_2026-10-19.md) | Audit of 258 role slots; identity, place, routine, memory, shops, AI truth, culling, privacy | A (source-level audit, not playtest) |
| [RTD-009 dialogue schema](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/RTD_009_DIALOGUE_SCHEMA_V1.md) | Formal schema and test contract | A |
| [Skyrim-inspired roadmap](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/SKYRIM_NPC_DIALOGUE_IMPLEMENTATION_TODO.md) | 93-task implementation plan | A for plan; most tasks open |
| [32-NPC expansion](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/NPC_EXPANSION_2026-10-19.md) | Cast/content implementation notes | B (blocked deploy at time) |
| [Location grounding](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/NPC_LOCATION_GROUNDING_2026-10-19.md) | Location-authority bug/fix | A (bug note) |
| [Lantern Road NPC callbacks](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/lantern-road/story/npcs/README.md) | Authored social memory; 3-tier repetition; voice rule | A (authoring) |
| [Lantern Road dialogue framework](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/lantern-road/story/dialogue/README.md) | Player role; 8-point conversation test; companion autonomy | A (authoring) |
| [Lantern Road quest scenes](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/lantern-road/story/quests/README.md) | Offer/complication/decision/aftermath/non-ideal | A (authoring) |
| [Quest callbacks](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/lantern-road/story/endings/QUEST-CALLBACKS.md) | Delayed/visible consequences | A (authoring) |
| [The Undercity](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/the-undercity/README.md) | 352 storylets / 854 branches / 34 professions | B (project claims; mostly implemented) |
| [Neathbound](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/neathbound/README.md) | 9 locations, optional routes, multiple outcomes | B |
| [Schism world bible](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/schism/seed/world-bible-v1.md) | World consistency; factions; personal stakes | A (world bible) |
| [Whispering-Wilds preferences](https://github.com/joshualparris/Whispering-Wilds/blob/main/docs/chatgpt-conversations/2026-09-25-dnd-rpg-preferences-and-codex-prompts.md) | Josh's explicit taste and anti-goals | A (primary preference record) |
| [AI Table DM concept](https://github.com/joshualparris/Whispering-Wilds/blob/main/docs/conversations/2026-09-25-ai-table-dm-app-concept.md) | AI narrator + deterministic rules + state | A (architecture brief) |
| [WILDY DESIGN](https://github.com/joshualparris/RunescapeFedoraCrashDoctor/blob/main/DESIGN.md) | Implemented small-scale exploration/arena design | A (implemented/tested) |
| WILDY README / tests | Live game and 22 tests | A |

### Private catalogue

A private Dewey-style research catalogue was checked for related work. It is a **catalogue**, not a source repository. A title-level pointer to a narrative-RPG design document exists, but the underlying document was not accessible without authentication, and no private content is reproduced or linked here. A related private catalogue frontend was not an additional evidence source.

---

## AI naming, diversity and homogenization

1. **Hamilton, S. & Mimno, D. (2026). *Elias in the Lighthouse, Again? Diagnosing Low Diversity in LLM Stories.***  
   [arXiv:2605.26492](https://arxiv.org/abs/2605.26492)  
   Used for: 20,000 stories, 11 words in 88.3%, Elias/Mara/Elara/lighthouse/keeper/clockmaker/librarian; preference data rather than pre-training frequency. **Grade A** (large empirical study), with the caveat that it studies English short fiction.

2. **Mozo Quesada, A., Gálvez Rojas, S. & López Valverde, F. (2026). *Character-Name Concentration in LLM Fiction: Measuring Displacement and Mitigating Repetition.***  
   [arXiv:2611.01284](https://arxiv.org/abs/2611.01284)  
   Used for: 44,782 stories / 88,919 names; Slop Ratio; static banlists displace concentration and reduce real-name representation; speculative naming / SlopTracker reduces collision 7.3%→0.4%, within-story 4.3%→0.2%, naturalness 42–69%. **Grade A.**

3. **Brzozowski, M. & Chung, N. C. (2026). *The Ghost Couple: Correlated LLM Name Priors and Their Haunting of the Web and Academic Publishing.***  
   [arXiv:2606.02184](https://arxiv.org/abs/2606.02184)  
   Used for: correlated ensembles/pairs/trios (Elena Vasquez + Marcus Chen + Amara Okafor; Aris Thorne + Lena Petrova; Elara Voss), model/version-specific priors. **Grade A for the phenomenon; the web-pollution findings are outside game design.**

4. **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond).** NeurIPS 2025.  
   [paper](https://papers.nips.cc/paper_files/paper/2025/file/754d5a526a5ee5a47220664a0eb92751-Paper-Datasets_and_Benchmarks_Track.pdf)  
   Used for: semantic convergence even under high-temperature sampling; pairwise similarity ~0.80–0.90. **Grade A/B.**

5. **Fu, T. et al. (2026). *Beyond the Hivemind: Escaping LLM Homogeneity via Meta-Persona Anchoring and Sequential Temperature Scaling.***  
   [arXiv:2608.02618](https://arxiv.org/abs/2608.02618)  
   Used for: meta-persona + filtered temperature scaling; similarity ~0.85→0.65. **Grade B/A** (preprint; ~20B open models).

6. **Doshi, A. R. & Hauser, O. P. (2024). *Generative AI enhances individual creativity but reduces the collective diversity of novel content.*** Science Advances 10(28), eadn5290.  
   [doi](https://doi.org/10.1126/sciadv.adn5290) · [UCL record](https://discovery.ucl.ac.uk/id/eprint/10195027/)  
   Used for: individual creativity up, collective similarity up. **Grade A** (controlled experiment).

7. **Shumailov, I. et al. (2024). *AI models collapse when trained on recursively generated data.*** Nature.  
   [doi](https://doi.org/10.1038/s41586-024-07566-y)  
   Used for: model collapse risk from recursive synthetic data; do not train on unfiltered AI output. **Grade A.**

8. **Jwynia, *Character Naming: Breaking the Chen Proliferation.***  
   [skill](https://github.com/jwynia/agent-skills/blob/main/skills/creative/fiction/character/character-naming/SKILL.md)  
   Used for: external entropy, cast collision, cultural coherence, median-hopping; practical checklist. **Grade C** (practitioner heuristic, not a study), but useful and explicitly MIT-licensed.

9. **Gizmodo, *Why Do Chatbots Keep Telling Stories About Someone Named ‘Elias Thorne’?***  
   [article](https://gizmodo.com/why-do-chatbots-keep-telling-stories-about-someone-named-elias-thorne-2000770629)  
   Used for: accessible summary of Hamilton & Mimno; journalistic framing. **Grade C** (secondary).

## Writers’ room, voice and generation methods

1. **Showrunner.** Wikipedia. [link](https://en.wikipedia.org/wiki/Showrunner)  
   Used for: showrunner as top creative authority/head writer, tone and final cut. **Grade B** (reference overview).

2. **Writers’ room.** Wikipedia. [link](https://en.wikipedia.org/wiki/Writers%27_room)  
   Used for: room sizes 2–30, no single formula, UK single-writer/voice-driven tradition, criticisms. **Grade B.**

3. **Bible (screenwriting).** Wikipedia. [link](https://en.wikipedia.org/wiki/Bible_%28screenwriting%29)  
   Used for: story bible, continuity, “walking bibles.” **Grade B.**

4. **Languages constructed by Tolkien.** Wikipedia. [link](https://en.wikipedia.org/wiki/Languages_constructed_by_Tolkien)  
   Used for: glossopoeia, language families, Tolkien’s “a name comes first and the story follows.” **Grade B** (reference; primary quote).

5. **George R. R. Martin / Star Wars / Steven Moffat.** Wikipedia overviews. [Martin](https://en.wikipedia.org/wiki/George_R._R._Martin) · [Star Wars](https://en.wikipedia.org/wiki/Star_Wars) · [Moffat](https://en.wikipedia.org/wiki/Steven_Moffat)  
   Used for: background; the voice/naming analysis is interpretive craft reading, not a controlled study. **Grade C** for style claims.

6. **Zhang, J. et al. (2025/2026). *Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity.*** [arXiv:2510.01171](https://arxiv.org/abs/2510.01171)  
   Used for: 1.6–2.1× diversity in creative writing; probability-verbalized candidate sets. **Grade A.**

7. **Zhao, M., Du, Y. & Wang, M. (2026). *Large Language Models Are Bad Dice Players.*** ACL 2026. [link](https://aclanthology.org/2026.acl-long.1051/)  
   Used for: LLMs lack a functional internal sampler; 7% median pass rate in batch, 10/11 models pass no distribution in independent requests; external RNG needed. **Grade A.**

8. **Nguyen, M. et al. (2025). *Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs.*** ICLR 2025. [link](https://proceedings.iclr.cc/paper_files/paper/2025/hash/afa5f124e36bed5cc2125067005d43f5-Abstract-Conference.html)  
   Used for: min-p; caveat: contested by later critical analysis. **Grade B/A.**

9. **Roush, A. & Mahajani, P. (2026). *Anti-slopping: An innovation for rectifying LLM writing clichés.*** Thoughtworks. [link](https://research.thoughtworks.com/library/anti-slopping-an-innovation-for-rectifying-llm-writing-cliches)  
   Used for: anti-slop sampler, 69–96% throughput cost at 1k–8k patterns, logit access required. **Grade B** (practitioner/research lab).

## Claim-to-source map

| Claim | Sources |
| --- | --- |
| Open world's main draw is autonomy, not size | Open world (Wikipedia); 80.lv (fatigue); BotW |
| Curiosity is an information gap | Loewenstein; BotW triangle design; Witcher quest design |
| Too many markers cause analysis paralysis | 80.lv; Open world (Ubisoft towers) |
| Great quests withhold, humanise and delay consequences | Sasko/Game Developer; Lantern Road; Quest Callbacks |
| NPCs need identity, place, routine, memory, consequence | Repository Town audit; Radiant AI; RDR2; Lantern Road |
| NPC count is not depth | Repository Town audit; 32-NPC expansion; cast architecture |
| Dialogue hubs can become vending machines | Defining Dialogue Systems; Branching Conversation Systems |
| 3–4 options is a practical default | Freed/Game Developer; Defining Dialogue Systems |
| Dialogue wheels speed flow but can obscure intent | Dialogue tree (Wikipedia); Freed |
| Failure should be authored content | Disco Elysium/RPS; Lantern Road non-ideal branches |
| AI must not own facts | AI Table DM brief; RTD-009; NPC audit |
| Density beats distance | Sasko; Undercity; Neathbound; 80.lv (counter-pressure) |
| Environmental storytelling rewards inference | Jenkins; environmental storytelling glossary; Disco/RPS |
| Player role/identity matters | Lantern Road dialogue framework; SDT; Disco |
| LLM names concentrate (Elias/Mara/Elara) | Hamilton & Mimno; Mozo Quesada et al. |
| Banlists displace rather than solve | Mozo Quesada et al. |
| Correlated name ensembles | Brzozowski & Chung |
| Temperature alone does not create diversity | Artificial Hivemind; Beyond the Hivemind |
| Collective diversity falls even as individual quality rises | Doshi & Hauser |
| External entropy + tracking beats prompts | Mozo Quesada et al.; Jwynia |
| Voice/style per repo beats pure random | Showrunner/writers’ room sources; author analysis (interpretive) |
| A small showrunner-led room beats a large committee | Writers’ room; Showrunner |
| LLMs cannot reliably sample from distributions | Zhao et al. |
| Verbalized Sampling increases diversity 1.6–2.1× | Zhang et al. |
| Min-p/anti-slop need logits and have costs | Nguyen et al.; Roush & Mahajani |
| Seeded tables + fixed facts are the right division of labour | Synthesis; Zhao et al.; Mozo Quesada et al. |

---

## Limitations

- **No player study.** None of the recommendations were tested with players for this report.
- **Survivorship bias.** The games discussed are mostly successful; failed open worlds are less documented.
- **Practitioner claims.** GDC talks describe what worked for one team, not universal laws.
- **Source summary chain.** Some articles summarise talks; details may be compressed or lost. Where possible, the GDC talk itself is linked.
- **Snapshot counts.** Repository Town's 258/32/38/188 figures are from an audit snapshot; the project has changed since.
- **Private material.** No private correspondence, credentials or Drive contents were used. Private catalogue metadata is not reproduced.
- **Quotes.** Short quotes are attributed for criticism/commentary; full texts remain with their owners.

---

*If you reuse this material, cite the original sources first and this synthesis second.*
