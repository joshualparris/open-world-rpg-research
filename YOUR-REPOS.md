# Audit: What Your Repositories Already Know

**Scope:** a GitHub-wide code search across `joshualparris` and `Parris-Tech-Services`, a check of a private Dewey-style research catalogue, and a close read of 15+ public design/engineering documents. This is an inventory of **existing research and design notes**, not a claim that every proposal is implemented.

---

## 1. What was searched

Search terms included:

`open world`, `open-world`, `NPC`, `NPC dialogue`, `dialogue`, `dialogue tree`, `quest`, `quest design`, `player agency`, `world bible`, `narrative RPG`, `Disco Elysium`, `immersion`, `environmental storytelling`.

Repositories with relevant material:

- **`JoshMemory`** — by far the largest body of work: Repository Town, Lantern Road, The Undercity, Neathbound, Schism, Sigil Delve, Whirring Wilderness, and related design/audit documents.
- **`Whispering-Wilds`** — Josh's explicit RPG preferences and the AI Table DM product brief.
- **`RunescapeFedoraCrashDoctor` (WILDY)** — an implemented small-scale exploration/arena game with its own research notes.
- **A private Dewey-style research catalogue** — indexes research repositories and Drive documents; it is a catalogue, not a source collection. Only title-level metadata was available for one narrative-RPG blueprint; no private content is reproduced here.
- **A private catalogue frontend** — not a separate research source for this topic.
- **A private interactive-fiction architecture repo** — Fallen London/Sunless Sea notes; adjacent rather than directly about open-world NPC design, so not used as primary evidence.
- **`ElodinDeepLore`**, **`NeathBound`**, **`Aetheria`**, **`SwordChronicles`** — lore/world content and game prototypes; useful context but not dedicated research on this question.

---

## 2. Inventory

| Source | What it is | What it contributes | Status / caution |
| --- | --- | --- | --- |
| [NPC realism audit](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/NPC_REALISM_AUDIT_2026-10-19.md) | Source-level audit of Repository Town's 258 NPC “slots” | Identity, place, routine, memory, shops, AI truthfulness, culling, privacy; P0/P1 backlog | Audit of a snapshot; not a player study; some fixes on an audit branch |
| [RTD-009 dialogue schema](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/RTD_009_DIALOGUE_SCHEMA_V1.md) | Versioned data/test contract | Actor keys, topics, conditions, priorities, typed effects, unknown-state deny, idempotency | Schema only; director/runtime not implemented |
| [Skyrim-inspired dialogue roadmap](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/SKYRIM_NPC_DIALOGUE_IMPLEMENTATION_TODO.md) | 93 numbered RTD tasks in 8 phases | Actor-specific branches, priorities, conditions, quest stages, memory, voice integrity, AI boundary | Research/plan; most tasks open |
| [32-NPC expansion](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/NPC_EXPANSION_2026-10-19.md) | Implementation notes for 20 new residents | 32 total named cast; themed prompts; 3-choice mini-quests; offline badges | Deploy was blocked at time of writing; not proof of live build |
| [Location grounding](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/NPC_LOCATION_GROUNDING_2026-10-19.md) | Bug/fix note (Arlo at Market Garden vs Arcade Avenue) | Authoritative current location vs home/workplace; prompt grounding | Integration note; live/canonical drift called out |
| [Lantern Road NPC callbacks](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/lantern-road/story/npcs/README.md) | Authored dialogue pack for 15 NPCs | Social memory; first-return/repeat/follow-up; voice rule; declarative triggers | Authored blueprint; runtime integration later |
| [Lantern Road dialogue framework](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/lantern-road/story/dialogue/README.md) | Player-Leader and consequential dialogue design | “Who am I in this conversation?”; 8 criteria; companion autonomy; Trust/faction memory | Authoring only |
| [Lantern Road quest scenes](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/lantern-road/story/quests/README.md) | Six core quest scene packs | Offer → complication → decision → aftermath → non-ideal branch | Authoring only; integration later |
| [Quest callbacks](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/lantern-road/story/endings/QUEST-CALLBACKS.md) | Epilogue blocks for each outcome | Delayed consequences; partial/unresolved states; visible world change | Authored prose; not a runtime system |
| [The Undercity](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/the-undercity/README.md) | Implemented/storylet RPG | 352 storylets, 854 branches, 34 professions, 4 ambitions; content tracker + QBN studio | Production-scale content density |
| [Neathbound](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/neathbound/README.md) | Text-led RPG prototype | 9 locations, optional encounters, multiple outcomes, route guidance | Strong small-scale exploration example |
| [Schism world bible](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/games/schism/seed/world-bible-v1.md) | Worldbuilding bible | Factions, technology rules, daily life, personal protagonist stake | Consistency/production artefact |
| [Whispering-Wilds RPG preferences](https://github.com/joshualparris/Whispering-Wilds/blob/main/docs/chatgpt-conversations/2026-09-25-dnd-rpg-preferences-and-codex-prompts.md) | Archived design conversation | Josh's explicit taste: rich, choice-heavy, lore-dense, 5e, believable NPCs, multiple approaches, exploration rewards | Personal preference, not market research |
| [AI Table DM concept](https://github.com/joshualparris/Whispering-Wilds/blob/main/docs/conversations/2026-09-25-ai-table-dm-app-concept.md) | Product/architecture brief | AI narrator + deterministic rules engine + structured state; AI must not own rules | Concept, not implementation |
| [WILDY DESIGN](https://github.com/joshualparris/RunescapeFedoraCrashDoctor/blob/main/DESIGN.md) | Implemented game's design notes | Exploration/Rift split; 7 NPCs, 3 waystones, boons, journal; flow/juice | Small-scale, implemented and tested |

---

## 3. The strongest material, and why

### 3.1 The NPC realism audit is the crown jewel

It is unusually honest for a game-design document. It distinguishes **role systems** from **people**, and refuses to call 258 slots a cast of 258 characters:

> “Counts are distinct role systems, not a verified census of persistent independent people.”

It then produces a design backlog that maps almost one-to-one onto the external research:

- identity (stable IDs, unique names);
- place awareness (current location vs home/workplace);
- daily routine (shifts, routes, meals, shopping, sleep);
- navigation (paths, doors, collisions, off-screen simulation);
- world-state actions (quests change objects);
- social relationships (witnessed events vs seeded backstory);
- memory (per-actor, privacy-controlled);
- shops (speech and stock agree);
- AI truthfulness (grounded answers, no invented facts);
- expression (gesture, posture, voice).

The most important sentence for any open-world RPG is the finding that **dialogue and physical actions diverge** when they do not share state. That is the difference between a living world and a theme park of talking mannequins.

### 3.2 The dialogue schema is a rare, testable contract

RTD-009 is not a vibe; it is a schema with negative tests. It defines:

- stable actor keys (`named:`, `worker:`, `resident:`);
- topics (introduction, news, directions, work, relationship, quest, trade, help, story, explore, farewell);
- conditions (flags, quest stage, inventory, money, visited location, time window, relationship, on-duty, shop-open, nearby actor);
- priorities and repeatability;
- recorded/text responses with verified captions;
- allowlisted effects with typed fields;
- **unknown state denies**;
- effects are requests, not execution.

This is exactly the infrastructure an open-world RPG needs to keep hundreds of conversations truthful. The gap is that the schema is a contract, not a runtime: the director, condition evaluator, effect executor and graph validator are still future work.

### 3.3 The Skyrim roadmap is the implementation plan

The 93-task roadmap translates “Skyrim-inspired” into concrete work:

- stable actor identity across 319 slots;
- deterministic DialogueDirector;
- graph integrity (missing nodes, cycles, reachability);
- topic categories and conditional greetings;
- predicates and priority/cooldowns;
- nested choices/back/change subject;
- authoritative quest/repair/trade effects;
- negative branches for closed shops, insufficient funds, missing items;
- event-backed memory and save migration;
- exact voice/caption integrity;
- responsive UI and input handling;
- AI grounded in live state, forbidden from mutating the game;
- release evidence.

It is strong because it treats **dialogue as a system with a truth boundary**, not a writing feature bolted onto a game.

### 3.4 Lantern Road is the content-design answer

Where the audit/schema are engineering, Lantern Road is authoring craft:

- 15 named NPCs with distinct voices and motives.
- At least two materially different callback states per NPC.
- Social memory around the existing quests, not a second plot.
- Voice rule: “Your Warden standing is high, so I trust you” is bad; a character-specific gesture/line is good.
- Repetition rule: first return, shorter repeat, optional follow-up.
- Player-Leader framework: the player is an in-world social role, not a cursor.
- The eight-point conversation test; if none apply, the choice probably should not exist.
- Quest scenes with offer/complication/decision/aftermath/non-ideal branch.
- Epilogue callbacks that make consequences visible, including partial and unresolved outcomes.

This is the best material in the repos for “lots of NPCs to talk to” because it treats conversations as **relationships over time**, not one-off trees.

### 3.5 Undercity/Neathbound show content scale and route shape

- **Undercity**: 352 storylets, 854 authored choice branches, 34 professions, 4 ambitions, multiple origins/factions/escape routes, and a content tracker/CMS. This is what “dense” looks like in production.
- **Neathbound**: nine locations, optional encounters, multiple permanent outcomes, a “Your Journey” guide, and a clear main mystery. This is a useful small-scale model for an open-ish RPG without a giant map.
- **Schism**: a world bible with factions, technology rules, daily life and a personal protagonist stake — consistency plus a reason to care.

### 3.6 Whispering-Wilds is the taste brief

Josh's own list is the cleanest statement of the target experience:

> “A rich, choice-heavy, lore-dense, properly 5e, immersive RPG with depth, consequence, mystery, and lots to explore.”

And the anti-goals:

- thin lore;
- railroading;
- generic choices;
- shallow worlds;
- sloppy presentation;
- “fake D&D”;
- short, flat, undercooked adventures.

The AI DM brief adds the architectural principle: **AI narrator + deterministic rules engine + structured game state + human override**. “Let the AI be creative where creativity is safe, and let code be strict where correctness matters.”

### 3.7 WILDY is the implemented micro-example

WILDY's explore mode is a small, working expression of the same ideas:

- seven authored NPCs with branching dialogue and boons;
- three waystones and a gated Rift;
- a journal, minimap that reveals stones after a hint, and camp blessings that carry into combat;
- a clear “beeliner” path via the Warden;
- no AI, no fabricated state.

It is not an open-world RPG, but it demonstrates the loop: **explore → talk → earn → carry consequence into a different mode**.

---

## 4. Cross-cutting strengths

Across the repos, five things are unusually strong:

1. **Truthfulness as a design value.** The audit and schema both insist that NPC claims match state; AI must not invent.
2. **Identity hygiene.** Namespaced actor keys, stable IDs, no display-name-as-ID.
3. **Memory as a first-class system.** Promises, favours, witnessed events, lies, relationships.
4. **Event-backed consequences.** Quest callbacks, world outcomes, aftermath states.
5. **Production realism.** Content trackers, graph tests, save migrations, privacy gates, release evidence.

These are exactly the areas where most open-world RPG design documents are vague. Your repos are ahead.

---

## 5. Gaps and duplication

### 5.1 The missing world-shape research

The repos are strong on **NPC truth** and **dialogue plumbing**, but thin on:

- landmark hierarchy and visual navigation;
- traversal cost and fast travel;
- density/pacing metrics;
- exploration anxiety and analysis paralysis;
- map reveal and icon budgets;
- “beeliners” vs explorers;
- how optional content is signposted;
- how open-world shape changes quest design.

This repo fills that gap with external research and connects it to the internal material.

### 5.2 Research vs implementation

Many documents are explicitly **authoring-only** or **plan-only**:

- Lantern Road NPC/quest docs are blueprints; runtime integration belongs to later tasks.
- The Skyrim roadmap is mostly unchecked; only RTD-001–009 are verified.
- The dialogue schema is a contract, not a director.
- The 32-NPC expansion deploy was blocked at the time; do not claim it as live.
- The audit is a snapshot, not a player study.

Treat these as **design evidence and engineering intent**, not proof of player experience.

### 5.3 Duplication and naming

There are parallel concepts:

- `Repository Town` appears in `JoshMemory` and `Parris-Tech-Services/Repository-town` (generated mirror).
- `Whispering-Wilds` exists as a Python CLI and a browser game.
- `Neathbound`/`The Undercity`/`Lantern Road` share storylet/QBN patterns.
- The private catalogue and its frontend are catalogue/frontend, not source research.

Consolidation should preserve canonical sources and link, not fork, the evidence.

### 5.4 The “counts” trap

The audit's numbers are useful, but they can be misread as a cast size. The repo should consistently say:

- 32 named characters;
- 38 simulated villagers;
- 188 generated house slots;
- 258 role-system slots;
- **not** 258 independent people.

The same applies to “352 storylets” or “854 branches”: these are content units, not evidence of player-perceived depth.

---

## 6. What should be canonical where

A practical structure:

- **Source evidence** stays authoritative in the original repo (JoshMemory, Whispering-Wilds, WILDY).
- **This repo** is the synthesis: the question, findings, evidence grades, checklist, and links.
- **A private Dewey-style catalogue** can index this repo by subject (700 Arts & Recreation / game design) with a short abstract and link; it should not duplicate the report.
- **Its frontend** can display the same metadata if it is kept in sync.

This avoids the common failure mode where five documents each contain a slightly different version of the same claim.

---

## 7. Bottom line from the audit

Your repositories already contain the **hard, unglamorous half** of a great open-world RPG: actor identity, dialogue contracts, memory, consequences, and a refusal to let AI invent facts.

They do not yet contain the **world-shape half**: landmarks, density, traversal, exploration anxiety, map reveal and the economics of player time. That is the gap this repo addresses.

The combined thesis:

> **A dense cast is only as good as the world that makes talking to them worth the walk — and a world is only as good as the people who make it feel inhabited.**

---

*See [README.md](README.md) for the summary, [REPORT.md](REPORT.md) for the full argument, and [SOURCES.md](SOURCES.md) for evidence quality.*
