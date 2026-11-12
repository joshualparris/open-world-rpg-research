# Applying the Framework Across the Game Portfolio

**What this is:** a repo-by-repo audit of the game projects that currently have NPCs, dialogue, factions or narrative state, scored against the framework in [README.md](README.md) and [REPORT.md](REPORT.md), with concrete changes for making each one more fun, more open, and deeper in character.

**Date:** 2026-11-12.  
**Status:** desk audit of public docs/code; no playtests. Scores are directional, not benchmarks.  
**Scope:** public game repos and public source in `JoshMemory`; private repositories are summarised generically where relevant and not linked.

---

## 1. Coverage

### Audited in depth

| Project | Where it lives | What it is |
| --- | --- | --- |
| **Repository Town** | [`JoshMemory/repository-town`](https://github.com/joshualparris/JoshMemory/tree/main/repository-town) + public mirror/desktop/playtest ports | 3D town RPG/simulation with 32 named characters, 38 simulated villagers, 188 house slots, shops, quests and AI chat |
| **Lantern Road** | [`Parris-Tech-Services/lantern-road`](https://github.com/Parris-Tech-Services/lantern-road) | Hex-map party RPG with 15 NPCs, four companions, factions, quests, rumours and callbacks |
| **The Undercity** | [`joshualparris/theUndercity`](https://github.com/joshualparris/theUndercity) | Storylet RPG with 352 stories, 854 choices, 34 professions, factions, ambitions and a content studio |
| **Neathbound** | [`Parris-Tech-Services/NeathBound`](https://github.com/Parris-Tech-Services/NeathBound) | Storylet RPG with 9 locations, QBN studio, ambitions, multiple endings |
| **Whirring Wilderness** | [`Parris-Tech-Services/WhirringWilderness`](https://github.com/Parris-Tech-Services/WhirringWilderness) | Text-first wildlands RPG with branching quests, tactical encounters, autosave |
| **KKC Adventure** | [`kkc-adventure`](https://github.com/Parris-Tech-Services/kkc-adventure) + [`rothfuss-kkc-adventure`](https://github.com/Parris-Tech-Services/rothfuss-kkc-adventure) | Kingkiller text RPG: 18 locations, 5 canonical NPCs, time-of-day, relationships, skill dialogue |
| **Astra** | [`joshualparris/AstraDndGame`](https://github.com/joshualparris/AstraDndGame) | AI-driven open-world D&D solo campaign with server-authoritative state and signed saves |
| **Grey March / Marsh** | [`joshualparris/Marsh`](https://github.com/joshualparris/Marsh) | Hex + ASCII town + tactical prototype with 13 NPCs, factions, quests and shared memory |
| **dndgame / SwordCoast** | [`dndgame`](https://github.com/Parris-Tech-Services/dndgame) / [`SwordCoast`](https://github.com/joshualparris/SwordCoast) | Compact D&D browser RPG with locations, factions and 9 NPCs |
| **Whispering-Wilds** | [`joshualparris/Whispering-Wilds`](https://github.com/joshualparris/Whispering-Wilds) + browser port | Single-file text adventure with rooms, items, three NPCs, dialogue and quests |
| **WILDY** | [`joshualparris/RunescapeFedoraCrashDoctor`](https://github.com/joshualparris/RunescapeFedoraCrashDoctor) | Implemented small exploration + survivor game: 7 NPCs, 3 waystones, boons, journal |

### Adjacent or excluded

- **AshFallen** — a strong choice/exploration game, but no NPC cast; it is a candidate for adding one, not an NPC system to improve.
- **ForbiddenQuests** — private D&D text RPG; story nodes and wraith/lich encounters, but no persistent NPC layer. Generic recommendations apply.
- **Campaign Copilot / CanonRPG** — table tools, not games. They can reuse the NPC schema but are not scored.
- **Schism** — a world bible/campaign manager, not a game loop. It is a consistency asset.
- **Lore atlases / Fable Atlas / repository dashboards** — not game loops; excluded.
- **Puzzle/card/dice/chess games** (JoshCards, NebulaDice, Chess, etc.) — no NPC cast.
- **Empty or unreadable repos** (several tiny prototypes with no default branch) — not scored.

---

## 2. The five portfolio moves

1. **Build one Actor & Dialogue Core** — stable actor IDs, schedule/current activity, event-backed memory, relationships, typed effects, graph validation, 3–4 clear choices, mobile dialogue UI. Use RTD-009 as the starting contract.
2. **Ship one vertical slice in Lantern Road** — it already has the complete loop (travel → town → rumour → quest → choice → faction → combat → return) and a content validator. Add current activity, 3-node conversations and first-return callbacks for five NPCs; measure before scaling.
3. **Retrofit the storylet giants** — give The Undercity and Neathbound a recurring cast and witness/memory ledger. Their content density is an asset; the missing layer is people the player can revisit.
4. **Give Astra a structured NPC ledger** — the AI should voice a persistent cast, not invent faces every turn. Add `npcs[]`, location, goals, promises, memory and a known-faces journal.
5. **Deepen the small games, don’t grow them** — WILDY, Whirring, Marsh and dndgame need a few memorable people with callbacks, not more map or more slots.

**Do not start with the biggest map.** Start with the contract and one loop that can prove it.

---

## 3. Portfolio scorecard

Scale: **0 absent · 1 placeholder · 2 functional · 3 solid · 4 strong · 5 reference-grade**.  
“Truth” = state authority, dialogue/action alignment, tests, AI boundary. “Scale” = content volume/production maturity.

| Project | World shape | NPC presence | Dialogue | Quests | Player identity | Truth | Scale | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| **Repository Town** | 4 | 3 | 3 | 3 | 3 | 4 | 5 | Strongest simulation; consolidate and deepen the cast |
| **Lantern Road** | 4 | 4 | 3 | 4 | 4 | 4 | 4 | Strongest complete narrative loop; make dialogue sing |
| **The Undercity** | 3 | 2 | 3 | 4 | 4 | 3 | 5 | Storylet giant; needs recurring people |
| **Neathbound** | 3 | 2 | 3 | 3 | 3 | 3 | 4 | Storylet system; needs a cast and return visits |
| **Whirring Wilderness** | 3 | 1 | 1 | 2 | 2 | 3 | 2 | Good engine; almost no people |
| **KKC Adventure** | 2 | 4 | 4 | 2 | 3 | 3 | 2 | Best character voice; needs world and consequences |
| **Astra** | 4 | 1 | 2 | 2 | 3 | 4 | 2 | Best open-world AI bones; no persistent cast |
| **Grey March / Marsh** | 4 | 3 | 2 | 3 | 3 | 2 | 2 | Best small-scale hybrid; deepen conversation |
| **dndgame / SwordCoast** | 3 | 2 | 2 | 2 | 3 | 2 | 2 | Functional; NPCs are quest hooks |
| **Whispering-Wilds** | 1 | 1 | 2 | 2 | 1 | 2 | 1 | Teaching prototype; not the priority |
| **WILDY** | 2 | 3 | 3 | 2 | 2 | 4 | 2 | Best micro-model; add callbacks, not size |
| **AshFallen** | 2 | 0 | 2 | 2 | 2 | 3 | 1 | Adjacent; add a cast if NPCs are wanted |

**Reading the table:** a 5 in “Scale” does not mean “best.” The Undercity has enormous content density but weak NPC presence; KKC has superb character voice but little world. The portfolio’s best future is cross-pollination, not picking one winner.

---

## 4. What the portfolio already does well

1. **Narrative density** — Undercity and Neathbound prove you can author and validate hundreds of storylets and choices.
2. **World simulation** — Repository Town has schedules, shops, travel, interiors and a living-town simulation; Lantern Road has hex travel, factions and party memory.
3. **Character voice** — KKC’s NPC profiles (temperament, speech style, known/taboo topics, greeting pools) are better than most commercial NPC bibles.
4. **Truth architecture** — Astra already separates AI narration from server-authoritative state; Repository Town/RTD-009 have the strongest dialogue contract.
5. **Small complete loops** — WILDY and Marsh prove you can ship an explore/talk/fight loop without a giant team.
6. **Content tooling** — QBN Studio, content trackers, validators, save migrations and privacy gates are real production assets.

---

## 5. The gaps that repeat everywhere

| Gap | Where it shows up | Consequence |
| --- | --- | --- |
| **NPCs are functions, not people** | dndgame (greeting + quest hook), Repository Town (some cast), Whispering-Wilds | Talk once, never return |
| **NPCs are prose roles, not agents** | Undercity, Neathbound | 352 stories, but no one to revisit |
| **No persistent memory/callback** | KKC (mostly), Astra, dndgame, Whirring | The world forgets the player |
| **No current activity/schedule** | Lantern Road, Marsh, KKC (partial) | NPCs feel like static kiosks |
| **Dialogue is a menu, not a character** | dndgame, Marsh, Whispering | Information exchange, not relationship |
| **World shape is nodes, not landmarks** | most projects | “Open” means a list of destinations |
| **Consequences are local or invisible** | many | Choices do not echo |
| **AI invents people/facts** | Astra (free-form), Repository Town (optional chat) | One contradiction destroys trust |
| **Content scale outruns identity** | Undercity, Repository Town | Hundreds of units, few remembered people |
| **No shared actor/dialogue layer** | every project | Each game rebuilds the same plumbing |

---

## 6. Repo-by-repo prescriptions

### 5.1 Repository Town — the simulation flagship

**What it has:** 32 named characters, 38 simulated villagers, 188 generated house slots, schedules, shops, interiors, quests, AI chat, location grounding, audit backlog, 93-task dialogue roadmap.

**What is working**

- The cast/simulation scale is unique in the portfolio.
- The NPC realism audit is the best design document in the repos.
- RTD-009 gives a real contract for conditions/effects.
- The 3D town and interiors make “place” tangible.

**What is holding it back**

- 258 slots ≠ 258 people; repeated names and shallow generated residents.
- Dialogue and physics do not always share state (the Arlo bug).
- Named cast and villagers use different simulation tiers.
- Culling stops simulation, not just rendering.
- AI chat can outrun verified facts.
- Canonical source/mirror/desktop/playtest drift.

**Top moves**

1. **Freeze the canonical cast.** Pick 20–24 names that matter; give each a unique role, home, workplace, schedule and one relationship. Let the rest be explicitly ambient.
2. **Make one actor-state API.** Location, activity, inventory, money, quest stage, relationship, memory flags. Every dialogue/chat/shop reads it; no channel guesses.
3. **Ship 8–12 authored “core” arcs.** Each core NPC gets a 3-scene arc with a promise, a complication and a callback. This is what makes the 32 cast feel like people.
4. **Add NPC-to-NPC scenes.** Two named characters talking in the market; the player can overhear, interrupt or ask about it later. This is Skyrim’s best trick and Disco’s best texture.
5. **Audit the truth boundary in CI.** Contradiction tests: location vs dialogue, shop vs stock, quest vs reward, caption vs clip.
6. **Consolidate the mirrors.** One canonical source; generated copies clearly marked; no hand edits.

**North star:** Skyrim’s lived-in town + Disco Elysium’s conversational intimacy.

---

### 5.2 Lantern Road — the complete loop flagship

**What it has:** hex map, towns, 15 NPCs, four companions with personal arcs/memories, factions, rumours, six questlines, quest callbacks, trust, settlement consequences, content validator, save state.

**What is working**

- The loop is complete: travel → town → rumour → quest → choice → faction shift → combat → return.
- The world is deliberately small so choices echo.
- Companion memory/trust is real state, not a bar.
- The NPC/quest/faction cross-references are validated.
- The quest callbacks are excellent consequence writing.

**What is holding it back**

- NPC dialogue is data-driven but still closer to “services + rumours” than a conversation with a person.
- NPCs are mostly static per settlement; no current activity/routine.
- Faction/quest consequences are often abstract numbers; the player may not see them.
- Companion banter and NPC-to-NPC life are thin.
- The UI can feel like a dashboard rather than a place.

**Top moves**

1. **Add a “current self” to each NPC.** A one-line activity (“Tessa is counting clipped coins”), a time-of-day position, and a reaction to the last local event. This is cheap and transforms presence.
2. **Turn rumours into observable scenes.** A rumour should point to a place/person/time; the player can witness it, not just read it.
3. **Give every NPC a first-return and repeat line.** Use the Lantern Road callback rule you already wrote.
4. **Make faction consequences visible in town.** A patrol changes, a shop closes, a shrine gets busier, a rumour changes.
5. **Companion banter.** Two companions disagree at a camp; the player can side, mediate or ignore; Trust shifts.
6. **Fable pass.** Add warmth, humour and small human beats; the Grey March is rich but can feel uniformly grave.

**North star:** Fallen London’s content discipline + Fable’s warmth + Skyrim’s travel rhythm.

---

### 5.3 The Undercity — the content giant

**What it has:** 352 storylets, 854 choices, 34 professions, 16 districts, 4 ambitions, factions, quirks, exceptional stories, content tracker, QBN studio, witness/secret ledger.

**What is working**

- Enormous authored density and real content operations.
- Identity is strong: origin, faction, profession, quirks, ambition.
- Choices use stats, faction requirements, resources and consequences.
- The “witness” and “secret” material is a natural foundation for NPC memory.

**What is holding it back**

- NPCs are **roles in prose** (clockmaker, archivist, lamplighter), not persistent agents with IDs, schedules, relationships or callbacks.
- The README explicitly says character-specific dialogue and NPC consequences are still needed.
- Storylets are the unit of content; the player may not form relationships with people.
- Locations are a map of districts, not a lived-in place.
- No NPC-to-NPC life; the city is a narrator, not a society.

**Top moves**

1. **Promote 12–16 prose roles into a named cast.** The clockmaker, the archivist, the lamplighter, the baker, the inspector, the ferryman. Give each a stable ID, home district, schedule and two relationship states.
2. **Attach storylets to people, not only districts.** Every ambition chapter should have one recurring NPC who remembers the previous chapter.
3. **Build a witness ledger.** The existing witness material should become an NPC memory: who saw what, what they will repeat, what they will deny.
4. **Add return visits.** After each ambition milestone, the NPC has a new first-return line and a changed activity.
5. **Make professions social.** A promotion should change how NPCs address you, not only pay/equipment.
6. **Keep the density; cut the anonymity.** The content volume is an asset; the missing layer is identity.

**North star:** Fallen London’s quality-based narrative and recurring cast + Disco Elysium’s voices and failure.

---

### 5.4 Neathbound — the moody storylet RPG

**What it has:** 9 locations, storylets, QBN Studio, ambitions, multiple permanent endings, classes/quirks, a strong “city beneath the world” premise.

**What is working**

- Strong atmosphere and premise.
- Multiple outcomes and permanent consequences.
- Good content pipeline and validation.
- Exploration is route-based and readable.

**What is holding it back**

- NPCs are functions/roles in prose (archivists, merchants, librarians), not recurring people.
- No cast with schedules, relationships, memory or callbacks.
- Locations are visited for a storylet, not for a person.
- “Your Journey” guidance can flatten discovery if it becomes a checklist.
- The world can feel like a sequence of rooms rather than a society.

**Top moves**

1. **Create a recurring cast of 8–12.** The archivist, the ferryman, the librarian, the merchant, the clerk, the gardener. Stable IDs, home locations, one want, one secret.
2. **Make locations returnable.** A location should change after a storylet: a person moves, a sign changes, a route opens.
3. **Use NPC memory for the “witness” mechanic.** The game already cares about who remembers; give that to people.
4. **Add one social hub.** A tavern/market where 3–4 NPCs coexist and comment on recent events.
5. **Keep the QBN discipline.** Add “NPC” and “relationship” fields to the storylet schema; validate that callbacks reference real events.

**North star:** Fallen London’s city-as-character + Disco Elysium’s interiority.

---

### 5.5 Whirring Wilderness / Whispering Wilds — engine, no people

**What it has:** text-first wildlands RPG, branching quests, tactical encounters, autosave/backup, content tests.

**What is holding it back**

- Only **three NPCs** (Caretaker, Hermit, Ranger), each with intro lines and little else.
- No dialogue trees, schedules, memory, relationships, factions or callbacks.
- The world is a set of locations/quests; the “wilderness” has no social texture.
- NPC presence score is effectively 1.

**Top moves**

1. **Write 8–10 NPCs**, not 100: a camp keeper, a trapper, a deserter, a pedlar, a shrine keeper, a rival adventurer, a child, a healer, a ferryman, a hermit.
2. **Give each a schedule and a want.** The trapper is out at dawn, in the tavern at night; the pedlar moves between camps.
3. **Add a dialogue tree per NPC** using the 3–4 option rule, one hub topic, one personal topic, one rumour, one callback.
4. **Tie quests to people.** The current quests should change how an NPC acts afterward, not only the quest log.
5. **Add one social hub.** A campfire where 3 NPCs comment on the last quest.

**North star:** a small Skyrim camp, not a big empty map.

---

### 5.6 KKC Adventure — the character-voice benchmark

**What it has:** 18 locations, 5 canonical NPCs, time-of-day movement, 0–100 relationships, skill-based dialogue (Wit/Empathy/Authority/Scholarship), a richer TS implementation with NPC profiles (temperament, speech style, known/taboo topics, greeting pools, topic responses).

**What is working**

- The NPC voices are specific: Simmon is warm, Wilem is terse, Ambrose is cruel, Kilvin is grave.
- Taboo topics and topic matching create a sense of personhood.
- Time and relationship state give the world a rhythm.
- Skill checks make conversations a build expression.

**What is holding it back**

- World is a set of rooms/commands; little landmark/traversal design.
- Quests are thin; the academic loop is stronger than the story loop.
- Memory is limited: greeting variation and topic responses, but few long-term callbacks.
- The two implementations risk divergence.
- The property is fan fiction; original NPCs should be the long-term IP.

**Top moves**

1. **Add a memory ledger.** “You asked about his family and he deflected”; next visit, he acknowledges it.
2. **Give each NPC one arc.** Simmon’s money, Wilem’s homesickness, Ambrose’s cruelty, Kilvin’s ethics, Elodin’s danger. Three scenes each.
3. **Use Disco-style internal voices.** Wit/Empathy/Authority/Scholarship can comment on the conversation, not just unlock options.
4. **Make failure interesting.** A failed check should reveal character, not just close a door.
5. **Add a social location.** The Eolian or Ankers at night, with 3 NPCs and overheard talk.
6. **Unify the two implementations.** One canonical NPC/dialogue data source; the other consumes it.

**North star:** Disco Elysium’s voice/failure + Fallen London’s social memory.

---

### 5.7 Astra — the open-world AI bones

**What it has:** AI GM, server-authoritative state, signed saves, travel, locations, quests, factions, facts, journal, combat, D&D rules; `npcs: []` in the state schema.

**What is working**

- The architecture is right: AI narrates, server owns truth, idempotent actions, signed saves.
- Open-world intent is explicit: “the player may attempt ANY fictional action.”
- The opening already has an NPC (the woman), but she is not a structured person.
- The review document identifies the right next step: structured NPCs/promises/quests with stable identities.

**What is holding it back**

- There is **no persistent NPC ledger**. The AI can invent a name, a face, a promise, a quest; the next turn may forget or contradict.
- NPCs have no location, schedule, relationship, memory or consequences.
- The player can’t return to a person and see recognition.
- The world is broad but thin; “open” is a prompt, not a designed landscape.
- AI free-form dialogue can outrun the state.

**Top moves**

1. **Add `npcs[]` to the state schema**: stable ID, name, role, location, goal, appearance, relationship, knowledge, promises, last seen, alive/dead.
2. **Author 8–12 recurring NPCs** with goals and secrets; let the AI voice them but only within their facts.
3. **Add an NPC memory/event log**: witnessed, promised, lied to, helped, threatened. Feed it to the model as structured context; never let the model rewrite it.
4. **Make locations returnable.** The woman, the innkeeper, the gate guard should be in specific places at specific times.
5. **Add a “known faces” journal** so the player can see who they met and what they owe.
6. **Add a campaign clock.** Travel time, NPC schedules, quest deadlines; open-world freedom needs time pressure somewhere.

**North star:** Skyrim’s world + Disco’s character voice, with AI as a GM that cannot invent facts.

---

### 5.8 Grey March / Marsh — the hybrid prototype

**What it has:** hex overland, ASCII towns, tactical combat, 4 settlements, 4 wilderness sites, 5 questlines, 3 factions, 13 NPCs, shared NPC memory, save/load.

**What is working**

- The three-zoom loop is excellent: world → town → combat.
- 13 NPCs with state-dependent dialogue, quest hooks and faction roles.
- Persistent memory (`met`, `talks`, `lastTopic`) and quest state.
- The small scope makes consequence visible.

**What is holding it back**

- Conversation is mostly a single modal screen with a couple of choices; no real branching/hub.
- NPCs are static; no schedules/current activity beyond `lastTopic`.
- Faction consequences are numbers; the town does not visibly change.
- UI/typography is prototype-grade.
- Content is small (5 questlines).

**Top moves**

1. **Give each NPC a 3-node conversation**: greeting/current activity → topic hub → personal callback; 3–4 options.
2. **Add time-of-day.** NPCs move between home/work/tavern; the town feels different at night.
3. **Make faction standing visible.** Patrols, prices, rumors, a closed stall.
4. **Add two signature NPCs with arcs.** The best 2 of 13 should get 3 scenes each; leave the rest as texture.
5. **Use the Lantern Road callback structure** for the five questlines.

**North star:** a compact Fallout/Fable town, not a giant map.

---

### 5.9 dndgame / SwordCoast — the functional RPG

**What it has:** locations, travel, factions, 9 NPCs with location, faction, greeting, shop/heal/rumour/quest hooks, character creation, quests, combat.

**What is holding it back**

- NPC dialogue is a greeting + hook; no topics, relationships, memory or branching.
- NPCs are vending machines for services/quests.
- No schedules or world-state reactions.
- Quest consequences are thin.

**Top moves**

1. **Replace `greeting` + `questHook` with a `DialogueTree`**: 3–4 options, one personal topic, one faction topic, one quest topic.
2. **Add `met`, `lastTopic`, `trust`, `promises` per NPC.**
3. **Make the 9 NPCs returnable**: after the main quest, each has a new line and a changed service/attitude.
4. **Use the 3 factions as social lenses**: the same NPC talks differently at different standing.
5. **Add two companion NPCs** with opinions and banter.

**North star:** a compact Baldur’s Gate/Fable cast, not a bigger map.

---

### 5.10 Whispering-Wilds — the teaching prototype

**What it has:** rooms, items, gear, NPCs, a caretaker dialogue tree, quests, save/load, tests.

**What is holding it back**

- Four static NPCs (Caretaker, Ranger, Hermit, Trader); only the Caretaker has a real dialogue tree.
- No schedules, factions, relationships or world state beyond quest flags.
- Tiny map; not open-world.
- The browser port and Python CLI may diverge.

**Top moves**

1. **Keep it as a teaching/testbed**; don’t try to make it Skyrim.
2. Add one faction and one 3-scene NPC arc to demonstrate the pattern.
3. Share the dialogue/actor schema with the bigger games.
4. Use it for parser/NPC experiments (free text, topic matching).

---

### 5.11 WILDY — the micro-model

**What it has:** 7 NPCs, branching dialogue, boons, 3 waystones, 3 caches, journal, 2400×1800 map, minimap reveal, Rift; authored truth, no AI.

**What is working**

- Small but complete: explore → talk → earn → carry consequence into combat.
- 3–4 choices, explicit leave, boons/flags, journal.
- The calm/combat contrast is excellent.
- The “beeliner” path (Warden/Rift) exists.

**What is holding it back**

- NPCs are static; no schedules/current activity.
- Limited memory/callbacks; after a run, the camp mostly resets.
- No NPC-to-NPC life.
- Only seven people; the world can feel like a diorama.
- Lore is thin relative to the systems.

**Top moves**

1. **Post-run callbacks.** After a win/death, Mira, Bran, Pip and Sable each have a new line referencing what happened.
2. **NPC-to-NPC scenes.** Pip and Mira argue about the pebble; Bran and Sable trade barbs.
3. **One personal quest per NPC**, using the Lantern Road offer/complication/decision/aftermath structure.
4. **Add a day/night or “after N runs” state** so the camp changes without a huge simulation.
5. **Stop at 10 NPCs.** Depth, not count.

**North star:** a tiny Fable camp with Disco-ish voices.

---

### 5.12 AshFallen — adjacent, not an NPC game

Choice/scene survival with strong pressure, items, flags and outcomes; no NPC cast. If NPCs are added, use 3–4 survivors with memory and conflicting goals; otherwise keep it as a solo choice game and don’t force dialogue.

---

## 7. Shared platform: the highest-leverage move

Every project is rebuilding the same layer. The portfolio should have one **Actor & Dialogue Core**:

### 6.1 Actor record

```json
{
  "actorKey": "named:mira",
  "displayName": "Mira",
  "role": "Keeper of Ember Camp",
  "faction": "camp",
  "home": "ember_camp",
  "schedule": [{ "from": 0, "to": 360, "place": "ember_camp", "activity": "mending" }],
  "relationships": { "player": 2, "pip": 1 },
  "knowledge": ["demon", "waystones"],
  "memory": [],
  "tags": ["core", "vendor"]
}
```

### 6.2 Event log

Every NPC memory is an event, not an LLM summary:

```json
{ "type": "promise", "actor": "named:mira", "about": "return_with_charm", "turn": 12 }
{ "type": "witnessed", "actor": "named:bran", "event": "rift_won", "turn": 45 }
{ "type": "trade", "actor": "named:tessa", "item": "ration", "qty": 2 }
```

### 6.3 Dialogue contract

Generalise RTD-009:

- actor key + node id;
- topic (introduction, news, directions, work, relationship, quest, trade, help, story, explore, farewell);
- conditions (flag, quest stage, item, money, location, time, relationship, on-duty, nearby actor);
- 3–4 choices, exact intent, leave;
- response (text or verified clip);
- effects (typed, allowlisted, idempotent);
- callback fields (`witnessed`, `promised`, `lied`, `quest-outcome`).

### 6.4 Director + validator

- graph reachability/cycles/missing links;
- condition evaluation with **unknown = deny**;
- effect authority + idempotency;
- contradiction tests (location vs dialogue, stock vs speech, captions vs clips);
- save migration for new fields.

### 6.5 Authoring template

Every NPC arc:

1. **Meet** — voice, want, place, activity.
2. **Complicate** — a choice with stakes.
3. **Resolve / fail forward** — non-ideal branch.
4. **Callback** — first return, short repeat, optional follow-up.

### 6.6 UI kit

- dialogue card with portrait, name, title, exact line;
- 3–4 choices, leave, history;
- journal with known people/places/promises;
- minimap with known/rumoured/discovered;
- mobile typography and hit targets.

### 6.7 AI adapter

- AI may propose narration and free chat;
- it receives structured state but cannot mutate it;
- it may not invent names, quests, items, locations or memories;
- if state is unknown, say “I don’t know”;
- offline authored fallback.

---

## 8. Priority sequence

### Phase 1 — contract and one vertical slice (2–4 weeks)

1. Write the Actor & Dialogue Core schema + validator.
2. Pick **Lantern Road** as the vertical slice (strongest complete loop).
3. Add current activity, 3-node conversations, first-return callbacks for 5 NPCs.
4. Measure: NPC recall, callback recognition, repetition, “would talk again.”

### Phase 2 — cast retrofit (4–6 weeks)

1. **Repository Town**: 20–24 core cast, actor state API, core arcs, NPC-to-NPC scenes.
2. **Undercity**: 12–16 named recurring roles, witness ledger, ambition callbacks.
3. **Neathbound**: 8–12 recurring cast, social hub, returnable locations.

### Phase 3 — open-world depth (4–6 weeks)

1. **Astra**: `npcs[]`, authored 8–12 cast, memory ledger, known-faces journal, campaign clock.
2. **KKC**: memory/callback layer, internal voices, one arc per NPC, unify implementations.
3. **Marsh**: time-of-day, branch conversations, visible faction consequences.

### Phase 4 — small games

1. **WILDY**: post-run callbacks, NPC-to-NPC scenes, one personal quest per NPC.
2. **Whirring**: 8–10 NPCs, schedules, dialogue trees, social hub.
3. **dndgame**: dialogue trees/memory for the 9 NPCs.
4. **Whispering-Wilds**: teaching testbed; share schema.

### Phase 5 — production

- content tracker + validators across all projects;
- telemetry/playtest protocol;
- shared package distribution (TypeScript reference, Python adapter, JSON schema).

---

## 9. Metrics that matter

| Metric | Target | Why |
| --- | --- | --- |
| NPC recall | 3/3 named NPCs described by role/activity | Presence, not count |
| Contradiction rate | 0 claims contradicted by state | Trust |
| Callback recognition | ≥ 60% of players notice a prior choice | Consequence visibility |
| Repeat-line rate | < 20% after three visits | Memory/repeat-safe writing |
| Time to first meaningful choice | < 5 minutes | Pacing |
| Traversal dead time | < 45 seconds between beats | Density |
| Optional-content uptake | 30–60% (varies by genre) | Exploration pull |
| “Would talk again?” | ≥ 70% for core NPCs | Relationship pull |
| Intent clarity | ≥ 90% predict choice effect | Dialogue UI |
| Beeliner path viability | Main path works without side content | Respect time |

---

## 10. What to steal from the reference games

| Reference | Steal | Do not copy |
| --- | --- | --- |
| **Disco Elysium** | Internal voices, failure as content, build-gated dialogue, personal-first lore | Walls of text; no safety rails; every conversation a novel |
| **Fallen London** | Quality-based narrative, recurring cast, menace clocks, exceptional stories, content discipline | Energy/grind gating; opaque quality maths |
| **Skyrim** | Schedules, radiant systems, moddability, “one more cave,” sandbox presence | Generic radiant filler; quest-marker soup; shallow faction consequences |
| **Fable** | Warmth, humour, NPC reactivity, accessible morality, cinematic framing | Binary morality; over-simplified choices; empty promises |

**Portfolio blend:** Fallen London’s content economy + Skyrim’s presence + Disco’s voice + Fable’s warmth.

---

## 11. Bottom line

The portfolio does not need “more open worlds.” It needs **one shared layer that makes people persistent**, then a deliberate pass through each game:

- **Storylet games** (Undercity, Neathbound) need a **cast**, not more storylets.
- **Simulation games** (Repository Town, Lantern Road, Marsh) need **authored intimacy**, not more systems.
- **AI games** (Astra) need a **structured NPC ledger**, not a better prompt.
- **Character games** (KKC) need **world and consequence**, not more voices.
- **Small games** (WILDY, Whirring, dndgame) need **depth per NPC**, not scale.
- **Prototypes** (Whispering-Wilds) should become **schema testbeds**, not content mountains.

The single highest-leverage change is not a new game. It is the **Actor & Dialogue Core** plus one flagship implementation. Once that exists, every repo can share the same truth, memory and conversation quality — and each game can spend its uniqueness on world, tone and story instead of rebuilding NPC plumbing.
