# Creative Voice, Original Play and NPC Distinctiveness — Portfolio Research Addendum

**Research date:** 12 November 2026 · **Status:** source-grounded design research + repository desk audit; **not** a claim of implementation or completed player testing.  
**Purpose:** extend, not repeat, the existing [REPORT](REPORT.md), [GAME-REPOS-AUDIT](GAME-REPOS-AUDIT.md), [AI-NAMING-AND-ORIGINALITY](AI-NAMING-AND-ORIGINALITY.md), [NAMING-PLAYBOOK](NAMING-PLAYBOOK.md) and [WRITERS-ROOM](WRITERS-ROOM.md). The latter remains the **single authoritative showrunner/seeded-table/registry/production-rollout plan**; this file adds *player-facing fun, NPC behaviour, empirical speech-style evidence and tests* only.

## Executive finding

**The highest-leverage missing discipline is not another common NPC engine. It is a different *creative contract* for each game, tested against actual player behaviour.**

The portfolio already understands actor IDs, memory, authored dialogue, systemic consequences, quest branching, dialogue validation, curiosity, and naming collisions. Repeating those recommendations would add paperwork. This addendum contributes **six new design disciplines**:

1. **Fun signatures:** each game makes a different promise about *what the player does, feels and learns*, not merely a different art style.
2. **Character speech and social style:** distinct voices come from topic selection, pragmatics, sentence construction, professional vocabulary, evasions and values—not accents or name changes.
3. **Combinatorial social situations:** reusable norms, obligations, resources and conflicting intentions create original scenes rather than more static quest text.
4. **Quality-diversity selection:** generate divergent *playable situations*, then compare their merit within different kinds of fun rather than selecting the first plausible LLM idea.
5. **Distinctive failure and recovery:** identify what failure feels like in each world and why a player wants to retry, negotiate or return.
6. **Blind attribution and observable playtesting:** test whether people can recognise a game/character without its name and whether interactions are enjoyable in practice.

This is an **authoring and evaluation layer**, not a second Actor & Dialogue Core, writers' room, voice bible, seeded generator, rollout plan, or NPC naming registry. **Follow [WRITERS-ROOM.md](WRITERS-ROOM.md) for the creative governance, project voice bible templates and current phased implementation roadmap.** Use this addendum to ask whether their outputs are *playably fun, socially distinctive and recognisable by strangers*.

## 1. Deduplication map: reuse these; do not rewrite them

| Already canonical | Existing source | What this addendum adds only |
| --- | --- | --- |
| NPC counts versus genuine presence, routine, memory, state authority | [NPC realism audit](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/NPC_REALISM_AUDIT_2026-10-19.md), [REPORT](REPORT.md) | Social *friction*, relationship triangles and conversational conduct as the content of play |
| Typed dialogue effects and conditions; authority boundaries | [RTD-009](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/RTD_009_DIALOGUE_SCHEMA_V1.md) | The author-facing **voice fingerprint** that sits above the validated dialogue contract |
| 93-step dialogue implementation roadmap | [Skyrim NPC plan](https://github.com/joshualparris/JoshMemory/blob/main/repository-town/docs/SKYRIM_NPC_DIALOGUE_IMPLEMENTATION_TODO.md) | No new infrastructure roadmap; add a separate creative acceptance gate |
| NPC callbacks, quest consequences and scene packs | [Lantern Road authored material](https://github.com/joshualparris/JoshMemory/tree/main/repository-town/games/lantern-road/story) | Voice diversity, story situations in conflict, and actual playtest discrimination |
| Names, phonology, originality audit, collision registry and showrunner-led seeded tables | [AI-NAMING-AND-ORIGINALITY](AI-NAMING-AND-ORIGINALITY.md), [WRITERS-ROOM](WRITERS-ROOM.md), [data/name-commons.json](data/name-commons.json) | Diversity of **actions, moral dilemmas, speech acts and player activities**, *not* more name lists or another writing pipeline |
| World-shape, density, player autonomy, MDA and Flow | [REPORT](REPORT.md), [CHECKLIST](CHECKLIST.md) | A per-project **fun signature**, expectation calibration and distinctive failure modes |
| Repo scorecards and shared technical core | [GAME-REPOS-AUDIT](GAME-REPOS-AUDIT.md) | New creative direction for projects not covered there, plus deliberately contrasting identities for closely related games |

**Evidence distinction:** citations below to a game's README/source show **what it says or contains**, not that people enjoyed it. Every creative seed is a proposed original design and must be implemented and playtested before being described as a feature.

## 2. New research findings — evidence, practical consequence and limits

### F1. Character voice is a behaviour system, not a decorative writing style

**Evidence:** Mairesse & Walker's *PERSONAGE* (ACL 2007) formalises variation in personality-directed surface generation; Lopez Latouche, Marcotte & Swanson's *Generating Video Game Scripts with Style* (NLP4ConvAI 2023) uses character-specific prior utterances and adaptive style retrieval to make dialogue resemble its speaker. Ubisoft's accompanying practitioner write-up notes both promising improvements and the remaining gap to human-authored scripts. [R1–R3]

**New contribution to this portfolio:** build **voice fingerprints** alongside actor records:
- **Attention:** what this person notices before other people do (prices, injuries, weather, promises, craftsmanship).
- **Conversational goal:** what they want the exchange to accomplish, independently of the quest.
- **Speech act:** do they report, bargain, accuse, reassure, qualify, deflect, confess, joke or redirect?
- **Syntax:** short imperatives; nested qualifications; anecdotes; questions; careful lists; unfinished thoughts.
- **Lexicon:** 6–12 job/place/family words that occur *naturally*, plus banned stock phrases.
- **Disclosure:** what they volunteer, conceal, misremember or refuse; what makes that change.
- **Nonverbal signature:** where they look and what their hands do *while* speaking.
- **Relationship change:** how the same fact is conveyed to a stranger, friend and opponent.
- **Contradiction:** an enduring value that collides with an immediate want.

An NPC saying “Hello, traveller” in five synonyms is not five personalities. An accountant who first asks for a receipt, a boatman who asks about the current, and a sibling who asks whom you told have *different minds on the same event*.

**Boundary:** a style guide must never override world-state truth, safety, accessibility or player clarity. OCEAN trait labels alone are too coarse to produce a distinctive voice.

### F2. Social history matters most when it changes what a person is willing to do

**Evidence:** *Comme il Faut* (McCoy et al., AIIDE 2011) represents reusable social norms and interactions; *Prom Week* demonstrates social goals with multiple solutions and characters whose relationship histories matter. Its contribution is not free chat but **social state as gameplay**. [R4–R5]

**Practical translation:** create *small, recombinable social exchanges*:
- ask a favour while already owing one;
- correct someone in front of a person they wish to impress;
- ask for a resource owned by one NPC but promised to another;
- reveal a truth that helps a friend and embarrasses a colleague;
- apologise sincerely versus strategically;
- make a public promise that a bystander remembers.

Give each exchange: two or three actors, who knows what, a norm, an intent, a reason to accept/refuse, an observable outcome, and one later callback. Do **not** simulate a hidden soap opera that players cannot perceive or influence.

**Design distinction:** this is richer than one actor's +1 relationship score. A late repair bill, a witnessed lie and a neighbour's embarrassment can affect three people differently.

### F3. Distinct creative plans require a *portfolio* of good alternatives, not one “best” pitch

**Evidence:** quality-diversity research (Pugh, Soros & Stanley, 2016) seeks high-performing solutions across different behavioural niches instead of converging on one optimum; the 2024 game-scenario diversity survey and the 2025 PCG Benchmark distinguish *diversity* from *quality*, *controllability* and *playability*. [R6–R8]

**Practical translation (analogy, not a claim that MAP-Elites is already installed):** make an **idea archive** with bins such as:
- player verb: investigate / negotiate / repair / defend / travel / build / survive / care;
- emotional colour: warmth / awe / dread / pride / comedy / remorse;
- social structure: stranger / pair / triangle / institution / crowd;
- constraint: time / scarce resource / unreliable witness / conflicting rules / environmental change;
- consequence: physical / relational / economic / epistemic.

Write or generate **12 candidate situations across at least four distinct bins**, select **three different promising niches**, prototype the cheapest, and only then scale. Do not let an LLM select all the winners by resemblance to its own drafts. A human editor and gameplay tests make the call.

**Limit:** high novelty is not automatically fun. Unclear, unsolvable or inconsistent ideas are rejected regardless of novelty.

### F4. Fun is calibrated progress, not unlimited surprise

**Evidence:** a 2025 *Scientific Reports* analysis spanning puzzle, platformer and racing game datasets found preferences for intermediate difficulty, with player expectations and success also contributing to enjoyment. This is broad evidence about difficulty and fun, **not** a universal percentage or a guarantee for narrative RPGs. Curiosity research also identifies several different social, strategic and informational drivers. [R9–R10]

**Practical translation:** each game's 10-minute pilot should include:
1. an **invitation**: a visible question or affordance;
2. an **experiment**: a small reversible player action;
3. **legible feedback**: the player understands what changed;
4. a **surprise with cause**: the result is unexpected *but explainable*;
5. a **new capability or relationship**: a concrete reason to keep playing.

Measure not just “time in game” but whether players correctly anticipated the rules, recovered after failure, voluntarily tried a second strategy, and chose to revisit a character. Don't use addictive compulsion loops as a substitute for an interesting game.

### F5. Natural conversation includes manners, interruptions, context and refusal

**Evidence:** Rennick & Roberts' 2021 Game Studies paper applies conversation analysis and politeness theory to familiar game dialogue tropes. A character who delivers exposition on demand, regardless of setting or relationship, violates social expectations even if every line is beautifully written. [R11]

**Practical translation:** author NPCs who say “not here”, finish the job they're doing, redirect an invasive question, misunderstand a phrase for a character-specific reason, keep a confidence, or ask the player to come back—**provided the player is given a useful alternative path**. Important clue: different NPCs should have *different conditions for saying no*.

**Accessibility rule:** refusal must never hide an essential progression route behind arbitrary time-wasting. Respectful refusal plus actionable alternative is stronger than an invisible dialogue gate.

### F6. Planning and structured state beat unconstrained prose for coherence

**Evidence:** *SWAG: Storytelling With Action Guidance* (EMNLP 2024) explores separating narrative generation from action-level steering; the 2023 *Personalized Quest and Dialogue Generation* and 2026 *Game Knowledge Management System* research highlight grounded quest/narrative evaluation, with the latter expressly warning that LLM-as-judge is not independent player evidence. Ubisoft's 2024 NEO NPC and 2025 Teammates prototypes similarly use writer-authored personalities and scenario constraints; they remain experimental evidence, not proof that freeform NPCs are production-ready. [R12–R15]

**Practical translation:** keep **three separate layers**:
- **World designer**: assigns the immutable world rules and current authoritative state (already covered in RTD-009; reuse).
- **Scenario planner**: proposes *goals, conflicting constraints and feasible player verbs*.
- **Voice editor**: writes the actual line within the project's and NPC's fingerprint.

The editor is not permitted to invent a solved quest, an owned item or a witnessed event. The planner should propose at least two causally valid routes and an interesting non-ideal outcome before prose is written.

## 3. Project identity cards — proposed original creative direction

**These are design recommendations, not statements that the described features currently exist.** Project evidence is linked to the actual source repository; related projects deliberately share *plumbing* without sharing *tone*.

| Project and grounded starting point | Unique fun promise (what you *do*) | Distinct voice and mood | Original pilot (not yet implemented) | What to avoid |
| --- | --- | --- | --- | --- |
| **[Repository Town](https://github.com/joshualparris/JoshMemory/tree/main/repository-town)** — Narromine-grounded 3D town, people and daily work | **Notice → help → observe the town change**. Familiar streets acquire meaning through small obligations and systems | Grounded Central West Australian everyday speech for the real Narromine layer; warm and observant, occasionally dry. Fictional Repository Town may carry the writers’ room's civic-magical-realism angle, but never pass fictional incidents or invented locals off as real | **The refrigeration morning:** a delivery is delayed by a failed cold room. A shop worker, driver and repairer disagree over whose next job matters. Player can carry a part, lend transport or negotiate another delivery window; the next morning is visibly different | Fantasy “chosen one” plots, invented real-person biographies, generic friendship bars, quest spam |
| **[Lantern Road](https://github.com/Parris-Tech-Services/lantern-road)** — hex travel and four-person party | **Journey → promise → costly loyalty**. Companions read the same hardship differently | Spare frontier folktale, weather and material objects; warmth under uncertainty, never uniformly grim | **The ferryman's lamp:** an overdue crossing pits a sick traveller against a family who needs the last fuel; companions propose incompatible but reasonable solutions, and one remembers how you decided | A stat-only faction shift, anonymous quest givers, always choosing between obvious good and evil |
| **[The Undercity](https://github.com/joshualparris/theUndercity)** — original memory-trading city and dense storylets | **Interpret → bargain → exploit a civic contradiction**. Bureaucracy becomes a social puzzle | Crowded, wickedly funny institutional Gothic; official certainty paired with everyday absurdity | **The person officially absent:** an applicant has been erased from an index but keeps receiving bills. A clerk, an ally and a creditor each need different evidence; records and reputations change | More interchangeable cryptic nouns, random supernatural twists without institutional causes |
| **[Neathbound](https://github.com/joshualparris/JoshMemory/tree/main/repository-town/games/neathbound)** — compact route-based dark narrative | **Listen → infer → choose what to disclose**. Intimacy and absence create dread | Quiet, personal and restrained; the unsaid matters more than ornate descriptions | **Two punches in a one-way ticket:** three witnesses agree on the trip but disagree on who returned. The player chooses what truth to tell a family | Cloning Undercity's bureaucratic satire, multiplying storylets without returning people |
| **[Astra / AI dungeon projects](https://github.com/parristechservices-prog/AIDungeonMaster)** — freeform AI GM ambition | **Propose → test the world → improvise within rules**. Player invention produces coherent responses | Mythic-frontier oracle with a ledger; agile table-GM clarity, sensory hooks, quick causal adjudication, strong “yes, and/yes, but/no, because” | **The stranded rope bridge:** scout, negotiate for materials, or improvise a risky crossing; the same world model resolves all three, and NPCs remember the choice | AI manufacturing unearned inventory, new NPC identities each turn or fake omniscience |
| **[Whirring Wilderness](https://github.com/Parris-Tech-Services/WhirringWilderness)** — text-first wildlands RPG | **Listen → track → decide whether to disturb**. Reading the environment is a skill | Oral wilderness tall tale, anchored by real naturalist observations of bird, soil and weather; storytelling without indiscriminate mystical adjectives | **The wrong birdsong:** a ranger and hermit interpret the silence differently; following signs reveals a mundane danger before a supernatural one is considered | Generic prophecy, “ancient” every second sentence, borrowing Lantern Road's frontier speech |
| **[Grey March / Marsh](https://github.com/Parris-Tech-Services/Marsh)** — hex map → ASCII town → tactical battle | **Change scale → solve the same human problem three ways** | Clear, tactile, legible; visual/musical motifs bridge each zoom level | **The blocked causeway:** see flood on the map, trace its impact on residents in town, and solve a timed defence/repair scene tactically; same promise survives all three scales | Three unrelated minigames glued together; copied Lantern Road questlines |
| **[WILDY](https://github.com/joshualparris/RunescapeFedoraCrashDoctor)** — exploration and three-minute Rift | **Discover → prepare → survive**. Every exploration choice has a readable combat pay-off | Campfire folk horror with brief warmth and wit, a practical field journal and crisp three-minute combat barks | **A temporary blessing with a price:** one camp NPC offers speed at the cost of a defensive rune; test whether players understand and choose the trade-off | Long character monologues during short sessions, scope growth into a second MMO |
| **[Buckland Blocks](https://github.com/Parris-Tech-Services/BucklandBlocks)** — procedural voxel terrain/building | **Tinker → build → see emergent consequences**. Structures and neighbours make experimentation funny | Practical workshop banter and material specificity; curious, not grandiose | **The wall that sends water next door:** a clever build solves one problem and creates another; both neighbours act on real flood/pathfinding state | Copy-pasted Minecraft NPC chores, scripted “simulation” that ignores built geometry |
| **[Energy Quest](https://github.com/Parris-Tech-Services/energyquest)** — early Unity energy-collection prototype | **Collect → convert → sacrifice an opportunity → improve the world** | Hopeful field-science notebook: measurements, experiments and ethical disagreements, not space-opera jargon | **The final charge:** power either a greenhouse, a lift or a mining drill; observe resulting changes before adding biomes | Claiming nonexistent gameplay is already implemented; endless pickups without a trade-off |
| **[JoshRS](https://github.com/Parris-Tech-Services/JoshRS)** — real private 377 world plus separate original Woodlands demo | **Learn a local problem → cooperate → complete a short quest**. Family-scale discovery, dependable state and genuine NPC presence | Light, mischievous, workaday humour in *original expansions*; preserve existing historical game content faithfully without blending eras | **A bridge with an unreliable bell:** two family players coordinate on opposite banks using a repairer, ferryman and timed mechanism; one complete short original quest, verified in the actual 377 engine separately from Woodlands | Misrepresenting an HTML demo as the live 377 world; duplicating licensed quests/assets; auto-importing other revisions without parity tests |
| **[Sigil Delve](https://github.com/Parris-Tech-Services/delve)** — four-hero tactical dungeon slice | **Read a threat → coordinate → outsmart it**. Tactical decisions express relationships | Crisp, urgent, affectionate squad banter; role-specific sightlines and tactical instincts | **A lever no one can safely reach:** a risk-taking hero proposes a dash, a careful hero proposes cover, and the room itself enables a third answer | A giant open map; dialogue scenes that interrupt turns without improving decisions |
| **[ASHFALLER](https://github.com/joshualparris/AshFallen)** — sci-fantasy extraction beneath fictionalised Dubbo | **Assess risk → carry a cost → decide when to leave** | Sparse, tense expedition notes; tactile machinery, distance and dwindling light | **The second relic:** carrying it dims the lantern; returning early saves equipment, pressing onward helps a missing expedition. Both endings remain playable | Another generic apocalypse codex, infinite loot inflation, using real residents as fictional NPCs |
| **[Forbidden Quests](https://github.com/Parris-Tech-Services/ForbiddenQuests)** — standalone branching browser text RPG | **Test a strange rule → exploit it → accept consequences** | Quick, mischievous, precise verbal logic and visible dice/stats | **The invitation-only door:** permission is an actual mechanic; convince a witness, find an old invitation, or break in and acquire a lasting reputation | Expanding into a vast engine before persistence and core test loops work |
| **[SwordCoast / dndgame](https://github.com/Parris-Tech-Services/SwordCoast)** — browser D&D-like RPG | **Role-play a particular hero → exploit class strengths → see fair consequences** | Heroic, companion-forward and legible, with humour as release | **The disputed ford:** wizard, fighter and scout each propose a different rule-consistent solution and get different relationship reactions | Rote imitation of copyrighted campaigns or generic “roll for Persuasion” as the only social action |

**Fan/canon boundary:** StarHaven, KKC Adventure, Wild2 and historical RuneScape projects have source-IP and fidelity constraints. They can serve as *internal learning/reference material*, but original publishable worlds should not duplicate copyrighted character voices, signature plots or proprietary assets. Do not automatically rewrite preserved canonical content in a “uniqueness” sweep.

**Crucial contrasts:**
- **Undercity vs Neathbound:** public satire and society **versus** private ambiguity and loss.
- **Lantern Road vs Marsh:** travel and moral loyalty **versus** the same cause-and-effect across three playable spatial scales.
- **Repository Town vs Buckland Blocks:** a grounded community of human obligations **versus** the creative physical consequences of building.
- **JoshRS vs WILDY:** persistent long-lived historical world and cooperative quest **versus** a short exploration-to-combat ritual.
- **Whirring vs Energy Quest:** ecological observation and restraint **versus** experiments and explicit resource trade-offs.
- **Sigil Delve vs Astra:** authored tactical constraints **versus** freeform proposals bound by the same rules.

## 4. NPC-specific behavioural fingerprint (supplement to the existing voice bible)

**Do not create another project-level voice template.** The canonical showrunner's project tone, fixed facts, naming tables, seed, continuity registry and sign-off are already in [WRITERS-ROOM.md](WRITERS-ROOM.md) and [templates/writers-room/](templates/writers-room/). This is a *small NPC-level extension* to that approved bible: what the person notices, wants, conceals and actually does under pressure. Keep the filled card in the game's existing character authoring system, not as a divergent game-state source.

~~~text
NPC ID:                  | JOB / RELATIONSHIP TO COMMUNITY:
THE FIRST THING NOTICED: | THREE FAVOURED WORDS (NOT CATCHPHRASES):
SENTENCE RHYTHM:         | DOESN'T WANT TO TALK ABOUT:
WANTS FROM THE PLAYER:   | WANTS FROM A DIFFERENT NPC:
PRIVATE CONTRADICTION:   | PUBLIC BEHAVIOUR:
KNOWS NOW (FACTS):       | WILL LEARN ONLY IF (EVENT):
TRUE AFTER FAILURE:      | FIRST RETURN LINE CONDITION:
SAMPLE A: stranger       | SAMPLE B: trusted person
SAMPLE C: under pressure | SAMPLE D: after being wrong
~~~

**Voice is not accent cosplay.** A person's job, age, trust, losses, context and education shape their choices, not a fixed collection of catchphrases. Use real local language with care and never assume a protected characteristic from style.

### One factual situation, four distinct voices (original sample dialogue)

Prompt: *“The mill has closed.”* The **fact is identical**; no line asserts a new state.

- **Repository Town — practical:** “Sign was up when I went past. Flour delivery's still booked for Thursday, though.”
- **Lantern Road — human consequence:** “Then the road will have hungry travellers by nightfall. Someone had better tell the ferryman.”
- **Undercity — institutional comedy:** “Closed? Certainly not. Its operations have merely been classified as theoretical.”
- **Neathbound — intimate uncertainty:** “It was still turning when she left. That's the part he won't explain.”

Blind-read these without labels. If a reader cannot assign them to the correct world, rewrite **who notices what** before swapping adjectives.

## 5. Original scenario design: combine causes, not tropes

Use a five-card deck:

1. **World-specific material constraint** — a cold room, a ferry lamp, a missing registry entry, a weak battery, a sealed bridge.
2. **Two legitimate wants** — both sympathetic but incompatible in the next ten minutes.
3. **A social rule** — who has authority, whose word counts, who owes whom.
4. **At least three player verbs** — not three differently worded “agree” buttons.
5. **Two visible outcomes + a return** — change to object, person, place or group, with a plausible callback.

Then add a *single contradiction*: the reliable mechanic is afraid to admit a mistake; the rule-abiding clerk hides an unofficial kindness; the brave companion worries about being left alone.

**Negative filters:** reject “retrieve 10 items”, a mysterious hooded stranger, generic prophecy, villain who only desires power, identical faction speeches, a bargain that offers no actual sacrifice, and a choice whose branches reconverge without acknowledged consequences. These may be valid in an *intentional* parody, but not as default writing.

### Example three-way situation — same mechanics, different story

Every game can share the engine state **scarce resource; two claimants; delayed consequence**, while retaining a different plot:

- **Repository Town:** limited replacement part; three neighbours; repair priority, loan and council notice.
- **Lantern Road:** lamp oil; ferryman, traveller, companion; a promise or a safe passage.
- **Undercity:** a registrable unit of memory; debtor, clerk, erased resident; competing documentary proof.
- **Energy Quest:** finite charge; greenhouse, industrial lift, drill; physical energy conservation.

**Do not paste a single scenario across games with nouns changed.** The player's *verbs*, the social meaning of the choice, the sensory texture and the way failure lands must also differ.

## 6. Gameplay experiment checks for the established writers' room

**Not a second writing room or implementation roadmap.** Keep the curated table draw, project voice decision and provenance in [WRITERS-ROOM.md](WRITERS-ROOM.md). Apply the following *playability and distinction checks* to its approved candidate situations, above the technical tasks in the existing repo.

**Pass 0 — Search first.** Read the project's actual README, vision, mechanics, NPC/quest lists, present backlog and source-of-truth documents. Identify the exact feature already implemented. Record whether the evidence is source, CI, browser, or live gameplay. Never invent a missing project feature.

**Pass 1 — Apply the existing identity.** Read the project's approved writers' room voice bible and inherited shared canon; add one fun verb, one social rule and one failure grammar *only as diagnostic annotations*, not competing tone canon.

**Pass 2 — Test idea-space coverage.** Take 12 *already drawn or approved* situation candidates from the established seeded-tables/room process and check coverage across ≥4 player verbs and ≥3 emotions. Have the room generate additional candidates in missing bins if needed. Keep the existing registry authoritative and store a **rejection reason** for near-duplicates.

**Pass 3 — Causal test.** For three finalists write: initial facts, two competing goals, affordances, preconditions, 3 actions, likely direct effects, second-order social effects, a failed attempt and first-return callback. Reject any scene that demands imaginary inventory, inaccessible locations or inconsistent time.

**Pass 4 — Make it a game.** Create an actual playable 5–10-minute slice. One interaction should affect a visible object or relationship. No lengthy world lore until the slice is fun.

**Pass 5 — Voice edit.** For 3–5 crucial lines per NPC, remove names and evaluate who could plausibly say them. Reject non-specific monologues, identical refusal styles, exposition dumping and dialogue that talks past the player's action. An LLM can propose *variants*, while the editor approves and owns the lines.

**Pass 6 — Blind and replay tests.** Ask a person to attribute the unlabelled lines to the correct project/NPC; test a stranger, friend and enemy state; try the alternative route; return after a quest; reload a save; verify that all 3 paths remain authoritative. Record confusion and evidence.

**Pass 7 — Ship, measure, retain or cut.** Merge only the slice that works. Keep an **idea archive**, not an ever-growing canon; every rejected idea does not need a quest file.

**Prompt for a creative planning agent (copyable):**

~~~text
Read this project's source-of-truth README, narrative files, backlog and
WRITERS-ROOM.md creative governance/seeded-table rules. First report EXISTING
features, locked names/premise facts and evidence grade. Do not duplicate previous quests,
characters, names, systems, research or plans. Do not alter the engine or import other
game IP. Define a distinct project voice using: player verb, emotional curve,
material world, social rules, linguistic cadence, humour, refusal style and failure.
Review 12 approved or seeded situation candidates covering at least four
kinds of play; reject close
matches to this repo and other games in the portfolio. For the three strongest,
show two conflicting legitimate wants, three CAUSALLY different player actions,
a non-ideal outcome, immediate physical/social change, a return callback and
the exact engine state fields needed. Write short contrasting sample lines,
then critically edit them against the project's fingerprint. Mark every item
PROPOSED, IMPLEMENTED, CI-VERIFIED or PLAYTEST-VERIFIED. No fake success claims.
Prefer a single playable 10-minute test over 100 more NPC or storylet records.
~~~

## 7. An evaluation that can actually reject generic NPC content

The following are **proposed pilot thresholds, not research-proven universal targets**. Test with 3–5 people initially; record sample size and provenance, then revise thresholds rather than gaming them.

| Question | Measure | Initial gate / action |
| --- | --- | --- |
| Are the projects distinguishable? | Blind project attribution for 4 projects × 4 comparable lines with names/place titles removed | Better than 25% chance; aim ≥75%, investigate every confusion |
| Are core NPCs distinguishable *within* a project? | 4 speakers × 3 short lines, no names, topic controlled | Aim ≥70% attribution; revise attention/syntax/refusal, not just names |
| Did fun happen before lore? | In a 10-minute test, number of purposeful actions, comprehension of next goal, spontaneous second attempt | Player must be able to attempt two real verbs; report observed, not assumed |
| Was the choice real? | Replay different branches from same save and compare observable state | Two branches produce materially different tracked results or acknowledged perspectives |
| Do relationships matter? | After event + reload, revisit actor A and actor B | Both have different justified reactions; no invented memory |
| Is failure recoverable? | Deliberately choose non-ideal outcome, attempt continuing | At least one meaningful next action, no unexplained dead end |
| Are NPCs socially convincing? | Player rates refusal/interruptions appropriate and useful | Identify unfair gates and repeated exposition |
| Is the voice original? | Human scan for generic text + independent similarity/collision check against the portfolio | No unregistered shared canon; no copied copyrighted dialogue |
| Is content truthful? | Engine tests: actors, location, items, money, time, quest flags; unknown-state denial | **Zero fabricated factual claims in tested dialogue** |
| Is it accessible? | Mobile, keyboard, text size, subtitles, skip and readable fallback | No necessary clue hidden in voice-only audio or tiny interaction target |

**Report:** a table of scenario ID, repo+commit, sample sizes, player quote (with consent), chosen path, confusion, bugs, fixes and the actual passing test link. No percentage denominators of zero; unknown ≠ pass.

### Adversarial playtest cases

- The player is silent, skips dialogue, or repeatedly asks “why?”.
- The NPC is on duty, away, angry, exhausted or currently speaking to someone else.
- One actor heard a rumour; another watched the event; neither is omniscient.
- The player lies or apologises; it affects *more than one* actor in different ways.
- A critical item was sold, a door is blocked, or a route is locked.
- Two equally valid solutions are attempted in either order.
- The save is reloaded mid-quest; social memory and world state still agree.
- An AI suggests an unregistered new item, name or quest; the engine rejects it safely.
- On the first minute of play, the player knows what can be attempted *without* a tutorial lecture.

## 8. Candidate playability experiments (not another project rollout)

**Do not reorder or duplicate the existing [WRITERS-ROOM.md](WRITERS-ROOM.md) phased rollout.** These are experiments to attach to each project *when that project's phase/agent is ready*. P0/P1/P2 indicate the *research value of the experiment*, not permission to open competing tasks or skip an approved phase. The writers' room remains the governing implementation sequence.

| Research value | Project | Proposed deliverable, deliberately scoped | Verification |
| --- | --- | --- | --- |
| P0 | **Repository Town** | One three-person, one-morning repair/delivery dispute backed by *existing* actor/job/shop/world state; 3 solutions, at least one witnessed consequence | Real in-browser movement, social reactions and save/reload; no invented town facts |
| P0 | **Lantern Road** | One companion disagreement in a travel/ferry scene with two valid outcomes and separate companion follow-up lines | Existing quest/content validator + actual browser play of both branches |
| P0 | **Undercity** | One original storylet cluster attached to three reusable named social roles; satirical paperwork puzzle and delayed consequence | Storylet conditions/qualities validated; two states and a return visit |
| P1 | **JoshRS** | One **original**, short family quest separate from upstream 377 canon; compare exact current 377 engine capabilities before authoring | Full in-game NPC interaction and persistence on two private accounts; isolated from Woodlands demo |
| P1 | **Sigil Delve** | One tactical room whose 3 solutions arise from different hero abilities and banter | Deterministic seed replay, combat log, save/load |
| P1 | **Energy Quest** | One energy-conversion fork plus visible beneficiary reaction | Unity scene actually runnable; before/after resource ledger and replay |
| P1 | **Buckland Blocks** | One build causes a neighbour-level environmental change and a response | Real collision/flow/path state + browser test, not merely scripted dialogue |
| P1 | **Whirring Wilderness** | One clue read two ways; one quiet NPC conversation with a clear alternate path | Quest progress, restore and mobile controls verified |
| P2 | **Neathbound, WILDY, Marsh, Astra, ASHFALLER, Forbidden Quests** | One tailored pilot each, using the identity cards above, *after* current owners' pending work is inspected | Source-specific contract + two alternative paths + observable consequence |

**Do not open sixteen duplicate roadmaps across game repos.** Maintain this cross-project experimental research here and obey the existing writers' room sequence; project-specific implementation tasks belong in their existing issue/queue systems. This addendum **does not claim those work orders have begun**.

## 9. Source and evidence ledger — new material only

Existing foundational NPC/open-world/naming references remain in [SOURCES.md](SOURCES.md). These sources add independent material on **linguistic style, social game mechanics, diversity search, fun calibration, conversation etiquette and creative planning**.

| ID | Source | Evidence and limit | Relevance |
| --- | --- | --- | --- |
| **R1** | [Mairesse & Walker (2007), PERSONAGE](https://aclanthology.org/P07-1063/) | Peer-reviewed dialogue generation; not a modern game NPC playtest | Controllable linguistic style |
| **R2** | [Lopez Latouche, Marcotte & Swanson (2023), Generating Video Game Scripts with Style](https://aclanthology.org/2023.nlp4convai-1.11/) | Peer-reviewed research on 23-game script corpus; human authors still outperform systems | Author-character utterance references |
| **R3** | [Ubisoft La Forge (2023), practitioner write-up](https://www.ubisoft.com/en-us/studio/laforge/news/7CCHPeIseXSW1P49L4XZ7l/generating-video-game-scripts-with-style) | Industry research interpretation, not an independent game trial | Word choice, style retrieval, editing |
| **R4** | [McCoy et al. (2011), Comme il Faut](https://ojs.aaai.org/index.php/AIIDE/article/view/12454) | Peer-reviewed social-simulation architecture | Social norms, retargetable interactions |
| **R5** | [Prom Week game](https://promweek.soe.ucsc.edu/about/) and [AIIDE paper (2013)](https://ojs.aaai.org/index.php/AIIDE/article/view/12662) | Working reference game + academic description | Relationships as a playable system |
| **R6** | [Pugh, Soros & Stanley (2016), Quality Diversity](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2016.00040/full) | Review/theory, not evidence that our game is fun | Diverse high-quality alternatives |
| **R7** | [Li et al. (2024), Measuring Diversity of Game Scenarios](https://arxiv.org/abs/2404.15192) | Research survey | Diversity dimensions and measures |
| **R8** | [Khalifa et al. (2025), PCG Benchmark](https://arxiv.org/abs/2503.21474) | Benchmark across multiple procedural game tasks | Separate quality/diversity/controllability |
| **R9** | [Leveling up fun (2025), Scientific Reports](https://www.nature.com/articles/s41598-025-14628-2) | Large game-data observational analysis plus controlled experiments; not specifically dialogue RPGs | Challenge, expectation and success |
| **R10** | [Exploring Curiosity in Games (2024)](https://www.tandfonline.com/doi/full/10.1080/10447318.2024.2325171) | Participant survey; generalises cautiously | Social/strategic/information curiosity |
| **R11** | [Rennick & Roberts (2021), Trope-Informed Conversation Design](https://gamestudies.org/2103/articles/rennick_roberts) | Design/theory study; not a shipped NPC system | Politeness, conversation context, refusals |
| **R12** | [Pei et al. (2024), SWAG](https://aclanthology.org/2024.findings-emnlp.824/) | LLM-assisted story planning study; not game deployment | Separate action selection from prose |
| **R13** | [Personalized Quest and Dialogue Generation (CHI 2023)](https://doi.org/10.1145/3544548.3581441) | User-study and evaluation of player-initiated quest/dialogue ideas | Player initiative, quest relevance |
| **R14** | [Ubisoft NEO NPC (2024)](https://news.ubisoft.com/en-us/article/5qXdxhshJBXoanFZApdG3L/how-ubisofts-new-generative-ai-prototype-changes-the-nature-of-npcs); [Teammates (2025)](https://news.ubisoft.com/en-gb/article/3mWlITIuWuu0MoVuR6o8ps/ubisoft-reveals-teammates-an-ai-experiment-to-change-the-game) | Industry prototypes, selected playtest reporting, not independent general proof | Writer-created personality and bounded improvisation |
| **R15** | [Game Knowledge Management System (2026)](https://www.mdpi.com/2079-8954/14/2/175) | Pilot, small human study; automatically judged scores are auxiliary, not ground truth | Schema-valid quests, actual human checks |

### Additional caution: recent LLM NPC evidence

A [2026 systematic mapping study](https://assets.ptidej.net/Publications/Documents/ToG26a.doc.pdf) reports 42 analysed studies from 377 records, with variable long-term-memory adoption and substantial response latency. It is **a recent research report, not proof of commercial success**. Treat real-time LLM chat as an optional, controlled addition rather than a prerequisite for a fun NPC.

## 10. Final recommendation

**One shared technical truth; many intentionally different artistic truths.** Reuse the portfolio's existing actor/state validators, save/load tests, originality registry and research sources. Differentiate each game by its **player verbs, emotional rhythm, social rules, speech behaviour, material world, conflict types, failure outcomes and visible changes**.

The first real success is not “100 new NPCs” or “20 new quests”. It is **one independently playable scene per project** that another person finds memorable *and can recognise without the game's title*.

*Prepared as an addition to the existing research. No gameplay implementation, player study, or external rights clearance is implied.*
