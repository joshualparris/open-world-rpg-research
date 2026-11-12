# More From Your Repositories: Second-Pass Findings

**Prepared 2026-11-12 · Addendum to [YOUR-REPOS.md](YOUR-REPOS.md) · Desk research, not a player study.**

The first audit ([YOUR-REPOS.md](YOUR-REPOS.md)) read about six repositories closely: JoshMemory (Repository Town, Lantern Road, Undercity, Neathbound, Schism), Whispering-Wilds and WILDY. This second pass searched **about 120 local clones** of your repositories (a few are duplicates or mirrors) for anything about **fun, NPCs, dialogue, quests and game design**, and read the documents that turned up. It adds **13 findings** and **1 correction**. Nothing in the original files was removed; where this pass disagrees with them, the disagreement is flagged.

**How to read this:** each finding has *what the repo says*, *why it matters for a big open world with many NPCs*, an **evidence grade** (see §0.3) and a *design test* you can run. Quotes are short and attributed; every source has a link.

---

## 0. Scope, method and limits

### 0.1 What was searched

- All repos in your session that were cloned locally (about 120, counting a few duplicates), by ripgrep over `*.md`, `*.txt`, `*.mdx` and the extracted text of three `.docx` planning files, using: `NPC`, `non-player`, `dialogue tree`, `player agency`, `game feel`, `flow state`, `game design`, `immersion`, `fun`, plus a filename sweep (`research`, `design`, `playtest`, `quest`, `lore`, `audit`, `roadmap`, `principle`).
- Skipped on purpose: `node_modules`, build output, bundled `public/games/**`, changelogs, and generated "BEAUTIFUL_CODE_STANDARD_AUDIT" boilerplate.
- **Hit counts for the public repos that mattered** (files matching the keyword sweep): repository-town-playtest 684 (a snapshot of ~60 games), joshrs 170, joshmemory 142, kkc-adventure 107, repository-town 58, lantern-road 46, AIDungeonMaster 28, campaign-copilot 18, WhirringWilderness 10, CanonRPG 10, and a long tail of 1-8 across other repos.

### 0.2 What this pass could not see

- **PDFs and Drive documents.** `3layers` and `kkc-adventure` hold PDFs (character sheets, handovers, planning PDFs) that were not text-extracted. The `.docx` planning files *were* read.
- **Private or inaccessible repos.** Only repos attached to the session were searched.
- **The source of the child-learning research.** The child-app design research note is referenced in two repos but the file itself is not in any of them; only excerpts and a roadmap built from it are. Treat those excerpts as secondary.
- **Players.** No document anywhere contains observed-player data on a *dense-NPC open world*. The closest are the Repository Town playtests, which are automated plus developer-driven, and the child-app QA notes. See §4.

### 0.3 Evidence grades used here

| Grade | Meaning |
| --- | --- |
| **A** | Observed behaviour with a reproducible record (a regression test that failed before and passes after, or a dated playtest log with named bugs). |
| **B** | Source-level audit or a design contract by someone who read the code, but no player in the loop. |
| **C** | Design intent: planning documents, roadmaps, briefs, prompts. Shows what you *decided*, not what worked. |
| **D** | Wishlist or pasted brainstorm. Useful as a taste signal only. |

---

## 1. Correction to the first audit

**The "38 simulated villagers" figure is out of date.**

The first audit and the main report quote the 19 Oct NPC realism audit's **258 slots = 32 named + 38 simulated villagers + 188 house slots**. A later inventory, [RTD-003 (24 Oct 2026)](https://github.com/joshualparris/joshmemory/blob/main/repository-town/docs/RTD_003_NPC_CAST_INVENTORY_2026-10-24.md), recounts the same town as:

| Type | Count | Stable key | Really simulated? |
| ---: | ---: | --- | --- |
| Named street characters | **32** | `named:<id>` | Street roaming and dialogue only; not the full work/day planner |
| Simulated workers / residents | **99** | `worker:<numeric-id>` | **Yes**: jobs, shifts, homes, money, needs, social events |
| House resident **slots** | **188** | `resident:<coord>` | **No**: deterministic dialogue identity per house, not 188 more people |
| Grid positions with no project house | **20** | none | No |

So the town now has **319 namespaced identity slots**, not 258. The first 38 worker IDs are kept as-is for save compatibility; the roster grew to 99 by adding later job entries (23), relief shifts for understaffed facilities (30) and security/HQ/locksmith staff (8). RTD-003 repeats the warning the first audit made: **do not sum the counts into "319 independent people"**; 99 of the 188 houses are also homes of simulated workers, leaving 89 houses with a dialogue identity only.

The rest of this research repo still quotes 258/32/38/188 with the "snapshot" caveat. The *argument* (count is not depth) is unchanged and, if anything, stronger: even the "99 simulated" number mixes people with very different amounts of life.

---

## 2. New findings

### A. Scope, proof and honesty

#### N1. Prove fun in 30 minutes, then build the epic

Five of your repos, written months apart for different games, land on the same discipline:

| Repo | What it says | Grade |
| --- | --- | --- |
| [AIDungeonMaster](https://github.com/parristechservices-prog/AIDungeonMaster/blob/main/docs/ai-dm-app-gaps-and-next-steps.md) | The V0 is "a single-player, text-only, web-based 30-minute D&D one-shot... just enough to prove the hybrid engine-plus-LLM model is fun." Closing line: "If the 30-minute proof is fun, the epic is worth building. If it isn't, nothing else matters." | C |
| [kkc-adventure plan v1.1](https://github.com/Parris-Tech-Services/kkc-adventure/blob/master/RothfussGameDocs/KINGKILLER%20CHRONICLE%20TEXT%20ADVENTURE%20v1.1%20planning%20Doc.docx) | Pillar 12 "Small Enough to Finish": "Each phase must end in something playable." (The companion `_Improvements` note phrases it as "a playable artifact, not just more planning".) MVP cut to one protagonist, one era, 8-12 locations, 3 fully modelled NPCs. | C |
| [Aetheria Improvements](https://github.com/Parris-Tech-Services/Aetheria/blob/main/Improvements.md) | "Do NOT work on multiplayer, 3D, guilds, leaderboards... focus only on the highest-value upgrades for this current game"; warns against "feature bloat". | C/D |
| [Whirring Wilderness roadmap](https://github.com/Parris-Tech-Services/WhirringWilderness/blob/main/docs/AAA_INDIE_ROADMAP.md) | "A polished, focused game is better than a feature-bloated one." | C |
| [Delve README](https://github.com/joshualparris/joshmemory/blob/main/repository-town/games/delve/README.md) / [Bramblewick README](https://github.com/Parris-Tech-Services/bramblewick/blob/main/README.md) | Both call themselves a "tight vertical slice"; Bramblewick's loop is one village, one quest, one boss. | B |

**Why it matters here:** a dense-NPC open world is where scope runs away fastest. The fix your own documents keep arriving at is a *slice that is already fun*, with a few NPCs done properly.

**Design test:** can a stranger play 30 minutes, with three fully modelled NPCs, and want the next 30?

#### N2. Engine owns truth, narrator owns prose (five independent confirmations)

The first report already argued this (§6.8) from RTD-009 and the AI Table DM brief. The second pass shows it is a **house rule you reinvented in at least five repos**:

- **AIDungeonMaster:** "the engine owns mechanics; the AI only narrates/suggests" ([competitor-gap-roadmap](https://github.com/parristechservices-prog/AIDungeonMaster/blob/main/docs/competitor-gap-roadmap.md)). Its grounded-QA report lists adversarial inputs the validator must refuse: *invented NPCs*, impossible movement, unsupported spells, "missing NPCs ... fail safely" ([qa-grounded-dm-report](https://github.com/parristechservices-prog/AIDungeonMaster/blob/main/docs/qa-grounded-dm-report.md)). Its prompt forbids new "locations, NPCs, or plot points without good reason" ([dm-prompt-design](https://github.com/parristechservices-prog/AIDungeonMaster/blob/main/docs/dm-prompt-design.md)). Its gaps doc adds the **canon log**: an append-only list of facts the DM has stated, fed back into every prompt ([gaps](https://github.com/parristechservices-prog/AIDungeonMaster/blob/main/docs/ai-dm-app-gaps-and-next-steps.md)).
- **kkc-adventure:** pillar 11 "Engine Owns Truth"; every prompt repeats "narration must never mutate PlayerState" and "the engine remains the source of truth" ([prompt 42](https://github.com/Parris-Tech-Services/kkc-adventure/blob/master/RothfussGameDocs/PromptGenerator1-20/generated_prompts/prompt_42_npc_trust_reaction_layer.md)).
- **Bramblewick:** "QuestManager ... LISTENS to monster_killed / item_gained / dialogue_event (combat and dialogue never edit quests directly)" ([ARCHITECTURE](https://github.com/Parris-Tech-Services/bramblewick/blob/main/ARCHITECTURE.md)).
- **RTD-009** and **Whispering-Wilds** (first audit).

**Grade:** B/C (architecture intent plus tests; no player evidence). **Why it matters:** with many NPCs, one wrong hallucinated fact is multiplied by every conversation. The convergence is a reason to make it a rule, not a preference.

**Design test:** if you delete the model, does every quest, price, location and relationship still resolve?

#### N3. Evidence honesty is part of the product

Your best documents refuse to overclaim, and that habit is itself a design asset:

- The Repository Town verification note: "CPU geometry tests: 188 houses, 843 rooms, 2627 interactive exhibits ... **This is NOT a graphical playtest.**" and "57 packed games in source does not mean 57 games published." ([PLAYTEST_2026-10-19](https://github.com/joshualparris/joshmemory/blob/main/repository-town/PLAYTEST_2026-10-19.md))
- The Occupations doc ends with "**Still requires human/device acceptance** ... Automated geometry, physics, state and audio-graph checks do not substitute for these checks." ([OCCUPATIONS_PLAYTEST](https://github.com/joshualparris/joshmemory/blob/main/repository-town/docs/OCCUPATIONS_PLAYTEST.md))
- JoshRS keeps a generated [quest matrix](https://github.com/Parris-Tech-Services/joshrs/blob/main/docs/QUEST_MATRIX.md) ("one honest state per quest", "do not hand-edit; regenerate"). Its completeness audit found that in one open-source server, "15 journal classes ≠ 15 playable quests": the journal screen existed but the end-state logic lived elsewhere, so the status stays **UNKNOWN** ([audit](https://github.com/Parris-Tech-Services/joshrs/blob/main/docs/377_OPEN_SOURCE_GAMEPLAY_COMPLETENESS_AUDIT_2026-10-31.md)).
- `3layers` tags every campaign fact with provenance: `source-canon`, `table-canon`, `player-choice`, `inferred`, `unresolved`, `retconned`, `DM-private`, and requires key facts to be retrievable "in under 10 seconds during play" ([GDD](https://github.com/Parris-Tech-Services/3layers/blob/main/Epic-Quest-Saga/docs/01-product/game-design-document.md), [pillars](https://github.com/Parris-Tech-Services/3layers/blob/main/Epic-Quest-Saga/docs/01-product/vision-and-pillars.md)).

**Why it matters for NPCs:** "content present" is not "content playable". A shopkeeper who exists, a quest with a journal entry, or an NPC with 40 lines is not evidence of fun until someone completes the loop. The practical form is a generated status matrix for NPCs and quests, and a provenance tag on facts NPCs assert.

**Grade:** A for the honesty practice (it is visible in dated documents); the *benefit* is untested.

**Design test:** can you list every NPC and quest with one of {authored, wired, playable, verified-by-a-human} and regenerate that list from the repo?

---

### B. NPCs: what they are, what they know, what they can do

#### N4. A major-NPC template, and the fields most designs skip

The Kingkiller v1.1 plan lists what every *major* NPC requires: identity; era presence; speech style; daily routine; social status; core motives; key fears; capabilities **and limitations**; public knowledge; private knowledge; **unknown-in-canon boundaries**; stance toward the player; **taboo topics**; **conversation exit conditions**; **what they notice first**; **what makes their tone change**. Three NPCs are "fully modelled", two "partially modelled", and one cameo-pressure NPC, deliberately *not* two ([plan v1.1](https://github.com/Parris-Tech-Services/kkc-adventure/blob/master/RothfussGameDocs/KINGKILLER%20CHRONICLE%20TEXT%20ADVENTURE%20v1.1%20planning%20Doc.docx)).

Compared with the presence model in the main report (§6.4: identity, place, routine, memory, consequence), the new, genuinely useful fields are:

1. **Knowledge boundaries** (public / private / unknown), so an NPC cannot answer what they cannot know.
2. **Exit conditions and tone-change triggers**, so a conversation ends or turns for a reason.
3. **"What they notice first"**, a cheap way to give each NPC a distinct *attention*.
4. **Limitations**, which stop a character becoming a quest dispenser.

The same document also writes a **negative scope rule** that is quotable: "generic filler NPCs as the main content" is on its *Should Not Have* list.

**Grade:** C. **Design test:** pick any NPC; can you state what they would *not* talk about, and why?

#### N5. Difficult NPCs need voice rules, an arc and a decoder

The Elodin hooks note ([ELODIN_GAME_HOOKS](https://github.com/joshualparris/joshmemory/blob/main/repository-town/games/elodin-deep-lore/ELODIN_GAME_HOOKS.md)) is a compact craft guide for a character who knows more than they can say:

- **Voice principles (their own list):** never explain directly; every "nonsense" line has a decodable meaning; warm but not comforting; never deceived by the player.
- **A five-act NPC arc:** obstacle → teacher → warning → ally (with limits) → *measure of who the player has become*. A relationship that changes *role* over the game, not just its number.
- **A question economy:** a limited number of questions with this NPC; "burning a question badly ... closes off a branch; saving questions for the right moment opens new possibilities."
- **The "pinecone" pattern:** quests from this NPC are tests of something other than the stated task; players who rush the stated task miss the lesson.

The Kingkiller plan adds a guard: very delicate characters get **bespoke rule packs** and are "not implemented deeply until later" rather than run through the generic system.

*Caution:* this material derives from published fiction. Keep it as private design reference, not shipped text. The plan itself puts a "Rights/Release" gate first and says so ([_Improvements](https://github.com/Parris-Tech-Services/kkc-adventure/blob/master/RothfussGameDocs/_Improvements.docx), §2.2).

**Grade:** C. **Design test:** does your most important NPC change *role* across the game, or only get friendlier?

#### N6. The affordance gap: a staffed building with nothing to do

Your 29 Oct Repository Town playtest is the best-evidenced NPC finding in the collection because it was **played, then fixed, with a regression test that failed before**:

- "**The Corner Grocer had a cashier but sold nothing.**" Fixed by giving it stock, restocking trucks and Buy buttons, and a rule: "no sale without a cashier at the till."
- "**Residents cooked dinner in the wrong room in 11 homes.**" A themed exhibit room with a coffee machine outranked the real kitchen, so a resident "spent dinner milling about the hallway". Fixed by ranking rooms stove > fridge/pantry > coffee machine (`tests/resident-kitchen.mjs`, all 188 homes).
- Left open on purpose: "pharmacy, library, dentist, gym and ~14 more still have staff but nothing to do" (RTBUILD-001...019, "interior detail pending").

([PLAYTEST_2026-10-29](https://github.com/joshualparris/joshmemory/blob/main/repository-town/PLAYTEST_2026-10-29.md))

**Why it matters:** an NPC is only as convincing as the *affordance* behind their job and the *world rule* that makes it true. A visible role with no verb is worse than no NPC, because it teaches the player to stop trying.

**Grade:** A (regression tests failed on the old commit and pass on the fix) for these three bugs; B for the broader claim.

**Design test:** for every visible NPC role, name the verb the player can perform with them, and the world rule that makes the role causally real.

#### N7. One dialogue controller, one identity policy, and a gossip pipeline

The RTD-004 source audit found **three separate dialogue UIs** for one town ([RTD-004](https://github.com/joshualparris/joshmemory/blob/main/repository-town/docs/RTD_004_DIALOGUE_SYSTEM_AUDIT_2026-10-24.md)):

1. 32 named street characters (recorded branches, optional quizzes, freeform chat);
2. house residents and walking workers (a different UI, its own chat history, grounded scene answers);
3. NPC-to-NPC "yarns" (deterministic four-line exchanges chosen from templates by participants, place, event and time).

It concludes: "Named characters, simulation villagers and generated house residents do not yet share a single dialogue state/controller or identity policy", and warns **not** to remove the villagers' detailed grounded answers while introducing a shared director.

Two further observations from the same audit are worth pulling out:

- The shared recorded graph (`start, topics, advice, explore, stories, goodbye`) is "shown to all eligible voiced actors". That is the **"same tree for everyone"** failure the main report describes in §7.4, found in your own code.
- NPC-to-NPC yarns are called "an excellent factual feed for unlocking later player dialogue". That is a **gossip pipeline**: what NPCs say to each other becomes what they can tell you. It is the missing link between simulation and conversation.
- **A voice-honesty rule** worth copying: "Never describe arbitrary AI text as genuine ElevenLabs audio"; device speech must be visibly labelled.

**Grade:** B. **Design test:** if an NPC witnessed an event in the simulation, can the player hear about it from that NPC, or from someone they told?

#### N8. Presence is also *seen*: identity at phone scale, and bodies that don't overlap

The RTN tracker ([RTN triage](https://github.com/joshualparris/joshmemory/blob/main/repository-town/docs/RTN_NPC_CROWD_FALLBACK_TRIAGE_2026-10-25.md)) treats visual identity as a P0 NPC problem:

- A deterministic wardrobe keyed to **persistent identity**, so the same worker has the same outfit on the street and behind a counter.
- Separate entrance positions, reserved counter spots and queues, moving-obstacle steering, and **swept-body collision** so customers do not tunnel through furniture corners.
- "Never erase an actual simulation actor to make a crowd look clear."
- Compare silhouettes "at actual phone scale".

**Why it matters:** with a big cast the player recognises people by silhouette and place long before they read a name. Duplicate-looking NPCs and bodies sharing a tile break "these are people" faster than thin dialogue does.

**Grade:** B (source-level work with regression tests, hosted and mobile sign-off still open at the time of writing). **Design test:** at the screen size the player actually uses, can you tell three NPCs apart without reading their names?

---

### C. Conversation grammar and scarcity

#### N9. Two independent grammars for "a move in a conversation"

You wrote two conversation models without referencing each other:

| Kingkiller v1.1 (structured intent) | Lantern Road (choice intents) |
| --- | --- |
| **act:** ask, tell, request, flatter, provoke, deflect, lie, remain silent, leave | **intents:** ASK, PROBE, REASSURE, CHALLENGE, SUPPORT, JOKE, PROMISE, LIE, EVADE, REFUSE, DEFER |
| **topic:** person, place, event, rumour, favour, object | Each intent carries *Purpose* and *Possible consequence* |
| **tone:** careful, warm, casual, bold, manipulative, angry, joking | Intent changes trust differently by character ("PROBE may increase respect with direct characters; reduce Trust with guarded characters") |
| **knowledge limit:** the player cannot discuss what they do not know | Repeat rule: ASK "should not disappear after use"; on repeat it becomes a follow-up, not the same question |
| Response depends on relationship, mood, setting, memory, time pressure, and *what the NPC knows about the player* | Test: a choice is worthwhile only if changing it would change information, relationship, commitment, future availability, remembered tone, immediate action, or interpretation |

([Kingkiller plan §8.3](https://github.com/Parris-Tech-Services/kkc-adventure/blob/master/RothfussGameDocs/KINGKILLER%20CHRONICLE%20TEXT%20ADVENTURE%20v1.1%20planning%20Doc.docx) · [Lantern Road DIALOGUE-CHOICE-GRAMMAR](https://github.com/joshualparris/joshmemory/blob/main/repository-town/games/lantern-road/story/dialogue/DIALOGUE-CHOICE-GRAMMAR.md))

**Why it matters:** both reject a rigid tree *and* uncontrolled free text. Combined, they give a small closed set of **moves** (intent × topic × tone) that the engine can evaluate against NPC state, and a model can only *phrase*. That is the safest way to put an LLM inside a dense cast. The Lantern Road "replay test" ("if three choices all produce the same paragraph and same consequences, they are not three choices") is the cheapest quality check you can run on any dialogue file.

**Grade:** C (both are authoring/design documents). **Design test:** take any conversation node; which of the seven things would change if you picked a different option?

#### N10. Scarcity makes conversations matter: question tokens, attention, and "persuadable, not programmable"

- **Question economy** (Elodin hooks, above): limited questions per NPC.
- **Companion autonomy:** Lantern Road's companions are "**persuadable, not programmable**": they can accept, accept reluctantly, counter-offer, refuse, volunteer, warn, interject. The spec lists what it must *not* create: "random obstruction; hidden personality rolls; ... constant permission prompts for ordinary combat actions; 'high Trust = obedience'." The Leader keeps final authority over irreversible party-level choices ([COMPANION-WILLINGNESS-AUTONOMY-SPEC](https://github.com/joshualparris/joshmemory/blob/main/repository-town/games/lantern-road/systems/companions/COMPANION-WILLINGNESS-AUTONOMY-SPEC.md)).
- **Persistent NPC state:** the AIDungeonMaster roadmap targets "NPC relationship state, schedules, promises and unresolved obligations" and "durable important-fact retention across 100-300+ turns" as its fifth milestone ([open-threads](https://github.com/parristechservices-prog/AIDungeonMaster/blob/main/docs/open-threads.md)).

**Why it matters:** unlimited, free conversation is cheap and therefore weightless. Limits (questions, attention, authority, time) are what give a line its cost.

**Grade:** C. **Design test:** what does the player *spend* to talk to this NPC, and what do they lose if they spend it badly?

---

### D. Fun for specific audiences

#### N11. A child is a different audience: the fun rules change

`SylviePhonetics` and `Sleepy` hold the most concrete "what makes this fun and safe for a small player" guidance in your repos ([QA-Recommendations](https://github.com/joshualparris/joshmemory/blob/main/repository-town/games/sylvie-phonetics/QA-Recommendations.md), [ResearchImplementationRoadmap](https://github.com/joshualparris/joshmemory/blob/main/repository-town/games/sylvie-phonetics/docs/ResearchImplementationRoadmap.md), [Sleepy QA](https://github.com/joshualparris/joshmemory/blob/main/repository-town/games/sleepy/QA-Recommendations.md)). They are built from a research note for a preschool-age child and a QA audit. The transferable rules:

| Rule | Source wording / detail |
| --- | --- |
| **Short sessions with a closing ritual** | Target 8-10 minutes, soft stop at 12, hard transition at 15; "multiple short sessions outperform one long session". Closing copy sends the child to a real-world task. |
| **Scaffolded feedback, never a bare "no"** | Ladder: hint → model → retry → gentle close ("We will come back to that sound."). Avoid red X states, "wrong" as the main feedback, and generic "good job". |
| **Informational praise; no variable-ratio rewards** | "Avoid variable-ratio reward schedules, choose narrative completion over points, and never shame mistakes." |
| **Audio-first, then symbols** | Sound before letters; sequence matters; one learning stage per mini-game. |
| **Anchor on the child's own name** | Used as a warm start, not a repeated quiz. |
| **Co-play is built into the game** | A caregiver prompt on every screen ("Say the sound first, then let [the child] copy"); movement/breathing breaks every 5-7 minutes; "Find one thing in the room that starts with your favorite sound." |
| **Sleep-safe design** (Sleepy) | Lights-out mode that fades to audio; no autoplay or external video; a parent gate; a timer and a prompt to go and read a real book. |
| **Private family play** (JoshRS) | "No internet, no accounts on external services, no strangers, no public chat" for the family LAN world ([family LAN guide](https://github.com/Parris-Tech-Services/joshrs/blob/main/docs/PLAY_WITH_SYLVIE.md)). |

**Why it matters for an open-world RPG:** if family co-play is a real audience, then **session shape** (where does a session end?), **failure tone** (what does the world say when you miss?) and **reward type** (completion vs a slot-machine drip) matter more than system depth. They also line up with the main report's finding that failure should be authored content.

**Caveats:** the underlying research file is not in any repo, so treat these as *your* working rules, not cited science; the roadmap itself says app practice must "support, not replace" therapist or educator guidance. Don't generalise preschool-age limits to adults; generalise the *principles* (closing ritual, informative feedback, no manipulative reward loops).

**Grade:** B- (QA audit plus a roadmap, secondary source). **Design test:** does a session end, on purpose, in a way you would be comfortable with a four-year-old (or a tired adult) seeing?

#### N12. Fun at a *table*: the Keeper's craft in your own mystery

[`The Last Laugh of Briarwick`](https://github.com/Parris-Tech-Services/campaign-copilot/blob/main/docs/adventures/MOTW_THE_LAST_LAUGH_OF_BRIARWICK_KEEPER.md) (an original Monster-of-the-Week scenario for three hunters and a first-time Keeper) is a worked example of fun-making technique, with design choices stated inline:

- **Don't gate truth behind a single roll:** the true story is supported by an inscription, testimony, a playbill, a diary *and* the monster's own speech. The weakness has two independent methods (silence the organ; tell the true story aloud to three or more witnesses).
- **Ask each player questions, then reuse the answers:** three opening questions (why did you come, who do you trust, what is your first reaction to the supernatural?); "Record their answers and reuse one later."
- **Equal spotlight** among the three; time-boxed (3 hours achievable inside a 5-hour window) with a six-stage countdown.
- **Tonal contrast:** an absurd opening ("a goose in a tiny judicial wig" as magistrate) against genuine dread.
- **"Keep play moving":** state a disturbing image, ask "What do you do?", answer with honest Keeper moves.
- **Safety as setup:** agree lines and veils first; anyone can skip or soften content.

AIDungeonMaster's gaps list adds the **missing-DM problems** an app must replace: dead-air nudges ("a soft 'What do you do?' after silence"), an **appeal button** ("wait, can we revisit that?") so one bad ruling doesn't end the session, **party-split** handling, **persona continuity** so "*their* DM is back", a cold-start first-five-minutes mode, and **"fun proxy" metrics**: "session length, drop-off points ... player utterance frequency ... return rate to next session" ([gaps](https://github.com/parristechservices-prog/AIDungeonMaster/blob/main/docs/ai-dm-app-gaps-and-next-steps.md)).

**Grade:** C (design intent; the scenario has not been run at a table in any recorded form). **Why it matters:** these are the techniques a good human game master uses to make a *cast* worth talking to; most carry straight into NPC and quest design (redundant clues, reused player answers, reversible mistakes).

**Design test:** if a player misses the key clue or roll, does the story still have a route forward?

---

### E. Work, competence and tension in your own taste

#### N13a. Competence loops that forgive error, with social progression

The Repository Town [Occupations doc](https://github.com/joshualparris/joshmemory/blob/main/repository-town/docs/OCCUPATIONS_PLAYTEST.md) describes jobs built from **physical stations and real items** (mop with a warning sign; weigh 2000 game grams; proof for 40 town minutes; take real queued villagers' tickets). Design choices worth keeping:

- "**Incorrect choices invite rework without deductions from earned wages.**" A full shift earns its agreed wage even if some duties need rework.
- Progression is **recognition**: three supervised shifts earn a town certificate and a 10% higher offer; six earn experienced-worker status and 25%; certificates unlock fixed-scope contracts with employer **escrow**.
- Fairness rules that prevent exploits: a duty recorded early is retained and credited; repeated collection "cannot pay twice"; saves reload to the same state (`tests/work-save.mjs`).

JoshRS adds the same instinct for MMO-style loops: balancing checks such as "no infinite money from starter shops, no duplicate XP from clicks", and a quest acceptance suite covering "completion, failure, wrong-order actions, repeated rewards and safe recovery after disconnect" (checklist items SKILL-10 and QUEST-08, [FULL_CLASSIC_MMO_CHECKLIST](https://github.com/Parris-Tech-Services/joshrs/blob/main/docs/FULL_CLASSIC_MMO_CHECKLIST.md)).

**Why it matters:** jobs and chores are how a dense cast becomes *useful*, but only if mistakes are recoverable and progress is recognised by people, not just numbers.

**Grade:** B (design plus automated tests; no human acceptance yet, as the doc itself says).

#### N13b. Tension register: where your own documents disagree

A second pass should surface contradictions, not hide them.

| Topic | Document A | Document B | How to resolve |
| --- | --- | --- | --- |
| **How many NPCs?** | Roadmaps scale the cast up: the Whirring Wilderness roadmap targets "10-15 NPCs" with schedules, relationships and dynamic dialogue | The NPC audit and Kingkiller plan: "Depth outranks breadth ... a few richly modelled places are better than a wide, thin map" | Start at the 3-5 fully modelled NPC slice; let counts grow only as each new NPC passes the N4 template. |
| **Quest markers** | The main report discusses icon budgets and legible rewards | The Kingkiller plan lists "quest markers" under *Should Not Have* and "slow play rewarded" as a pillar | Genre decides: for a mystery-first simulation use journal, rumours and landmarks instead of markers; for a content-rich sandbox use a small, honest marker budget. |
| **Free chat with NPCs** | Repository Town offers freeform AI chat with offline fallback | AIDungeonMaster / RTD-009: the AI must not own facts; unknown state denies | Free text is fine as *phrasing* over a closed set of moves; never as a source of world facts. |
| **Count vs census** | Earlier audit: 258 slots | RTD-003: 319 slots, 99 simulated | See §1. |

---

## 3. Convergence map: which of your repos back which principle

| Principle | Repos that independently say it |
| --- | --- |
| Small vertical slice first | AIDungeonMaster, kkc-adventure, Aetheria, WhirringWilderness, Delve, Bramblewick |
| Engine/state owns truth; narrator only phrases | AIDungeonMaster, kkc-adventure, Bramblewick, RTD-009, Whispering-Wilds |
| Typed events/effects; dialogue and combat do not edit quests directly | Bramblewick, RTD-009, AIDungeonMaster |
| Persistent NPC identity keys, not names | RTD-003 / RTD-009, Bramblewick (`id`), kkc-adventure (NPC template) |
| NPC state includes schedule, relationship, memory | Bramblewick (`schedule` field), kkc-adventure, AIDungeonMaster milestone 5, Repository Town |
| Depth over count | NPC audit, kkc-adventure; scaled up only by roadmap targets (C grade) |
| Honest status / provenance | JoshRS quest matrix, 3layers canon tags, Repository Town test notes |
| Forgiving failure, informative feedback | Occupations (rework without deductions), SylviePhonetics (feedback ladder), Lantern Road (non-ideal branch) |
| Session shape and a deliberate ending | SylviePhonetics, Sleepy, Briarwick (time-boxed, countdown), AIDungeonMaster (pacing, dead air) |

---

## 4. What is still missing (and a small protocol to fill it)

1. **No observed-player evidence on a dense-NPC world.** The Repository Town playtests are developer-driven and automated, and say so. The closest to real play is the child-app QA. The first report already warned "no player study"; that remains true.
2. **No recall test for NPCs.** Nothing measures whether a player can name and describe the cast after play.
3. **Fun proxies are proposed, not collected.** AIDungeonMaster lists them; no repo records them.

A 20-minute protocol that reuses your own measures:

| Measure | From | How |
| --- | --- | --- |
| Utterance / action frequency | AIDungeonMaster "fun proxy" | Count player inputs per minute; note long silences |
| Return intent | AIDungeonMaster; main report §11 | Ask "would you start another session?" and watch whether they do |
| NPC recall | Repository Town audit ("describe three NPCs by what they do") | After play, ask for three NPCs and what they did, not sold |
| First-5-minutes clarity | AIDungeonMaster cold-start | Note the first moment the player hesitates |
| Dead ends | Briarwick "don't gate truth behind a single roll" | Count times the player is stuck with no route forward |
| Closing | SylviePhonetics | Does the session end well, or just stop? |

---

## 5. Recommended next actions (from this pass only)

In order of leverage, each tied to a finding:

1. **Make one dialogue controller** over the three UIs, keyed by `named:` / `worker:` / `resident:` (N7, RTD-003/004). Keep the villagers' grounded answers.
2. **Write the 3-NPC slice with the full template** (N4) and the five-act arc for the most important one (N5), before adding NPC #4.
3. **Close the affordance gap** (N6): give every staffed building one verb, or hide the staff until the interior exists.
4. **Adopt a closed move grammar** (N9): intent × topic × tone, evaluated by the engine, phrased by the model.
5. **Generate an NPC/quest status matrix** (N3): authored / wired / playable / human-verified.
6. **Pipe NPC-to-NPC yarns into player-facing rumours** (N7) so the simulation becomes conversation.
7. **Decide the session shape on purpose** (N11): where a session ends, what the failure tone is, whether rewards are completion-based.
8. **Run the §4 protocol** once with two or three real players.

---

## Appendix A. Repo-by-repo ledger

| Repo | Relevant? | What it contributed (this pass) |
| --- | --- | --- |
| [AIDungeonMaster](https://github.com/parristechservices-prog/AIDungeonMaster) | **Yes** | Hybrid engine+LLM rule; 16-point gaps list; fun proxies; NPC-persistence milestone; grounded-DM adversarial tests |
| [kkc-adventure](https://github.com/Parris-Tech-Services/kkc-adventure) | **Yes** | Major-NPC template; conversation moves; pillars; scope discipline; NPC reaction layer (engine-owned reputation bands) |
| [campaign-copilot](https://github.com/Parris-Tech-Services/campaign-copilot) | **Yes** | Original Keeper-edition mystery with explicit fun technique; session-brain concept |
| [joshmemory](https://github.com/joshualparris/joshmemory) (Repository Town) | **Yes (more than first pass)** | Cast inventory (RTD-003), dialogue audit (RTD-004), crowd/identity (RTN), playtests (19/29 Oct), occupations, Lantern Road choice grammar and companion autonomy, Elodin hooks, SylviePhonetics and Sleepy |
| [joshrs](https://github.com/Parris-Tech-Services/joshrs) | **Yes** | Quest matrix; "journal ≠ playable"; MMO checklist items; family-LAN play |
| [3layers](https://github.com/Parris-Tech-Services/3layers) | **Yes** | Fact provenance tags; three-layer separation; retrieval-under-10-seconds target |
| [bramblewick](https://github.com/Parris-Tech-Services/bramblewick) | **Yes** | Event-driven quest rule; NPC schema with `schedule`; vertical slice |
| [Aetheria](https://github.com/Parris-Tech-Services/Aetheria) | Partly | Prioritisation advice; "handcrafted, not generic AI filler" |
| [WhirringWilderness](https://github.com/Parris-Tech-Services/WhirringWilderness) | Partly | NPC-depth roadmap; "polished and focused" principle |
| [CanonRPG](https://github.com/Parris-Tech-Services/CanonRPG) | Slightly | DM-prep tooling roadmap; canon-audit scoring (Canon Health Score) |
| [repository-town-playtest](https://github.com/Parris-Tech-Services/repository-town-playtest) | Duplicate | Snapshot of ~60 games; the canonical copies live in JoshMemory, which this pass linked instead |

**Searched, nothing relevant to fun or NPCs:** about 100 other repositories, mostly apps, tooling, dashboards and early prototypes (plus WILDY, which the first audit already covered). Private repositories are deliberately not named or cited in this public repo.

## Appendix B. New source files, by path

- AIDungeonMaster: `docs/ai-dm-app-gaps-and-next-steps.md`, `docs/open-threads.md`, `docs/competitor-gap-roadmap.md`, `docs/qa-grounded-dm-report.md`, `docs/dm-prompt-design.md`
- kkc-adventure: `RothfussGameDocs/KINGKILLER CHRONICLE TEXT ADVENTURE v1.1 planning Doc.docx`, `RothfussGameDocs/_Improvements.docx`, `RothfussGameDocs/PromptGenerator1-20/generated_prompts/prompt_42_npc_trust_reaction_layer.md` (default branch `master`)
- campaign-copilot: `docs/adventures/MOTW_THE_LAST_LAUGH_OF_BRIARWICK_KEEPER.md`
- JoshMemory (`repository-town/`): `PLAYTEST_2026-10-19.md`, `PLAYTEST_2026-10-29.md`, `docs/OCCUPATIONS_PLAYTEST.md`, `docs/RTD_003_NPC_CAST_INVENTORY_2026-10-24.md`, `docs/RTD_004_DIALOGUE_SYSTEM_AUDIT_2026-10-24.md`, `docs/RTN_NPC_CROWD_FALLBACK_TRIAGE_2026-10-25.md`, `games/lantern-road/story/dialogue/DIALOGUE-CHOICE-GRAMMAR.md`, `games/lantern-road/systems/companions/COMPANION-WILLINGNESS-AUTONOMY-SPEC.md`, `games/elodin-deep-lore/ELODIN_GAME_HOOKS.md`, `games/sylvie-phonetics/QA-Recommendations.md`, `games/sylvie-phonetics/docs/ResearchImplementationRoadmap.md`, `games/sleepy/QA-Recommendations.md`
- joshrs: `docs/QUEST_MATRIX.md`, `docs/377_OPEN_SOURCE_GAMEPLAY_COMPLETENESS_AUDIT_2026-10-31.md`, `docs/FULL_CLASSIC_MMO_CHECKLIST.md`, `docs/` family LAN guide
- 3layers: `Epic-Quest-Saga/docs/01-product/game-design-document.md`, `vision-and-pillars.md`
- Bramblewick: `ARCHITECTURE.md`, `DEVELOPMENT_ROADMAP.md`
- Aetheria: `Improvements.md` · WhirringWilderness: `docs/AAA_INDIE_ROADMAP.md`

---

*See [README.md](README.md) for the summary, [REPORT.md](REPORT.md) for the full external argument, [YOUR-REPOS.md](YOUR-REPOS.md) for the first audit, [CHECKLIST.md](CHECKLIST.md) §13 for the new audit questions and [SOURCES.md](SOURCES.md) for evidence quality.*
