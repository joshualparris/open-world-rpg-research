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

`ResearchLibrary` (private) was checked for related work. It is a **catalogue**, not a source repository. A title-level pointer to a narrative-RPG design document exists, but the underlying document was not accessible without authentication, and no private content is reproduced or linked here. `ResearchAtlas` is a catalogue frontend, not an additional evidence source.

---

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
