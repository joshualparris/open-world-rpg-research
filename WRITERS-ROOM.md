# The Writers’ Room Model

**Voice, not randomness — but voice plus randomness, tables and a registry.**

A research and implementation plan for giving every game repo a distinctive showrunner-led voice, while taking names, places, trades, quirks and premise facts away from the model.

Prepared 2026-11-12 · Desk research + architecture proposal. Not a playtest.

Companion files: [AI-NAMING-AND-ORIGINALITY.md](AI-NAMING-AND-ORIGINALITY.md) · [NAMING-PLAYBOOK.md](NAMING-PLAYBOOK.md) · [templates/writers-room/](templates/writers-room/) · [tools/table-draw.mjs](tools/table-draw.mjs) · [tools/name-audit.mjs](tools/name-audit.mjs)

---

## The verdict

Your instinct is right, but the framing should be:

> **A writers’ room is the governance model. Seeded tables are the entropy. The registry is the memory. The human showrunner is the taste.**

Not “writers instead of random,” and not “random instead of writers.”

- **Voice alone** produces pastiche: the model imitates a famous writer’s surface and still reaches for the same names.
- **Random alone** produces incoherence: surprising facts with no taste, no throughline and no believability.
- **Voice + curated tables + seeded draws + fit-filtered selection + registry + human approval** produces a world that feels authored *and* is not the model’s default.

This is also how real rooms work: a showrunner owns tone and final cut; a small room breaks stories; a story bible and continuity editor keep canon; individual writers bring distinct voices inside that frame. The room is not a democracy of style. It is a **controlled collision of voices under one sensibility**.

The strongest version for your repos is **an auteur-led mini-room**:

| Role | Responsibility |
| --- | --- |
| **Showrunner** (you) | North star, tone, final canon, naming/premise approval |
| **Worldbuilder** | Geography, institutions, history, names, places, trades |
| **Character lead** | Wants, contradictions, relationships, arcs |
| **Dialogist** | Diction, rhythm, subtext, silence |
| **Continuity editor** | Registry, callbacks, contradictions, CI |
| **Guest voice** (per arc) | One deliberate outside perspective |

Three to five voices is enough. A ten-person room tends toward consensus prose; the distinctiveness comes from the showrunner’s frame and the guest’s friction.

---

## 1. What research says about the room

- A **showrunner** is the top creative authority, usually the head writer, responsible for tone, story, hiring and the final cut. In scripted TV, the showrunner and head writer often set the season’s tone and structure before production ([Showrunner](https://en.wikipedia.org/wiki/Showrunner)).
- A **writers’ room** is a collaborative writing space, but there is no single formula; room sizes range from two to thirty, and each room has its own rules ([Writers’ room](https://en.wikipedia.org/wiki/Writers%27_room)).
- A **story bible** exists to keep characters, settings, continuity and timeline consistent; it is updated as the show establishes new facts. Some shows rely on writers’ assistants/script coordinators as “walking bibles” ([Bible (screenwriting)](https://en.wikipedia.org/wiki/Bible_%28screenwriting%29)).
- The UK tradition is often **single-writer or per-episode freelance**, and some executives argue those scripts are more “voice-driven” precisely because they are not room-written ([Writers’ room](https://en.wikipedia.org/wiki/Writers%27_room)).

The lesson for a solo AI-assisted studio: **do not simulate a ten-person committee.** Simulate a **showrunner with a small room and a strong bible**. The room’s job is to generate and stress-test; the showrunner’s job is to say “that is not us.”

---

## 2. What distinctive voices actually consist of

A writer’s voice is not a vibe word. It is a stable set of choices:

1. **What they notice** (sensory and moral attention).
2. **What they refuse to explain** (mystery, subtext, withheld lore).
3. **How power works** (who gets away with what).
4. **How people talk** (rhythm, register, profanity, silence).
5. **What a happy/sad ending costs** (thematic price).
6. **What names and places sound like** (phonology, class, history).
7. **What they find funny** (and what they never joke about).

The four examples you named are useful because each has a **recognisable selection filter**, not just a prose style.

### 2.1 Tolkien — the philologist

**Voice:** mythic, archaic, earnest; landscape and language carry the weight; high contrast between light and shadow, but mercy and pity complicate it; songs, genealogies and ruins imply a history much larger than the story.

**Naming convention:** language first. Tolkien wrote that the invention of languages was the foundation and “a name comes first and the story follows” ([Languages constructed by Tolkien](https://en.wikipedia.org/wiki/Languages_constructed_by_Tolkien)). Names belong to language families (Quenya, Sindarin, Khuzdul, Westron), with etymologies, sound changes and cultural ownership. Places are philological: the name has a history, a translation and often a tension between what insiders and outsiders call it.

**Quirk:** the narrator can stop for a poem, a genealogy or a footnote; the world is “all of a piece” because the languages and the legendarium share a root.

**What to steal:** name cultures with real phonology and history; places whose names encode landscape/language; the sense that the story is a window into a much older world.

**What not to copy:** pseudo-Elvish apostrophes, fake archaism, or a legendarium that exists only as a wiki.

### 2.2 George R. R. Martin — the political realist

**Voice:** grey morality, viewpoint intimacy, mundane texture (food, clothes, heraldry, weather), consequences that outlive the scene; the fantastic is real but expensive. The famous formulation is about “the human heart in conflict with itself,” and the books earn it by putting people in institutions that reward the worst in them.

**Naming convention:** regional families. The North sounds different from the Iron Islands, Dorne, the Reach or the Free Cities; names repeat within houses; house words and heraldry do narrative work. Places are concrete and possessive: Winterfell, Riverrun, Casterly Rock. Names are not random fantasy syllables; they signal region, class and allegiance.

**Quirk:** nobody is safe; feasts, tourneys and weddings are set pieces where the social contract can break; the mundane detail makes the violence land.

**What to steal:** regional naming families; house/faction words; the idea that a name is an address, a class and a loyalty at once; consequence that follows the character home.

**What not to copy:** grimdark as a substitute for theme; killing characters to prove you are serious; faux-medieval food porn.

### 2.3 George Lucas — the mythic pulp serial

**Voice:** archetypal adventure; the hero’s journey, the western, the samurai film, the Saturday serial and the war movie in one; moral clarity at the surface, with a “used future” texture that makes the world feel lived-in rather than pristine. The world is a playground of factions, ships, criminals and mystics.

**Naming convention:** simple, evocative, pronounceable, often echoing a function or a mythic role: Luke Skywalker, Darth Vader, Tatooine, Coruscant. Names are built for a child to repeat and a toy to sell; they are not philologically deep, but they are **legible**.

**Quirk:** rhyming/echoing names and motifs; the same story beats recur across trilogies; the world is expanded by glimpses (a cantina, a junk planet, a hologram) rather than explained.

**What to steal:** legibility; archetype as a doorway, not a cage; the “used future” detail that implies a working economy; naming for the ear.

**What not to copy:** the monomyth checklist; special-edition retcons; names that are only brandable.

### 2.4 Steven Moffat — the puzzle-box romantic

**Voice:** high-concept puzzle, time as an emotional weapon, banter as flirtation and defence, fairy-tale horror at a domestic scale, and a belief that the most important thing in the universe is a person. The structure is often a trap that turns into a love letter.

**Naming convention:** allusive, lyrical, often paired or image-led: River Song, Amy Pond, Clara Oswald, Weeping Angels. The names are **images** first and plot devices second; they promise a mystery and an emotion at the same time.

**Quirk:** “timey-wimey” causality, recurring catchphrases, the reveal that recontextualises an earlier line; the monster is often a metaphor for grief, memory or fear.

**What to steal:** names that are images; the emotional payoff of a structural reveal; horror that is intimate rather than gory; wit as character.

**What not to copy:** convoluted timelines that require a wiki; cleverness that replaces character; catchphrases as a substitute for voice.

### 2.5 The pattern across all four

They do not “have a style.” They have a **selection filter**:

| Writer | What gets selected | What gets cut |
| --- | --- | --- |
| Tolkien | Language, myth, landscape, mercy | Modern irony, casual register |
| Martin | Political consequence, mundane texture, grey motive | Pure heroism, plot armour |
| Lucas | Mythic image, legible archetype, used-future detail | Ambiguity that blocks a child’s grasp |
| Moffat | Puzzle, banter, intimate horror, emotional reveal | Naturalism, loose ends |

Your repos need the same: not “write like Martin,” but **“this game selects X and cuts Y.”**

---

## 3. Does your proposed stack hold up?

| Your claim | Verdict | Refinement |
| --- | --- | --- |
| **1. A particular voice/style per repo beats random.** | **Yes — with a caveat.** | Voice gives coherence; randomness gives variety. Use voice as the frame and randomness as the entropy inside it. A strong voice without fresh facts becomes pastiche; fresh facts without voice become noise. |
| **2. Take names/places/trades/quirks away from the model; draw from seeded code.** | **Correct.** | LLMs are poor samplers: in a 2026 ACL audit, batch generation had a **7% median pass rate** across distributions, and independent requests failed almost entirely; 10 of 11 models passed none of the distributions ([LLMs Are Bad Dice Players](https://aclanthology.org/2026.acl-long.1051/)). Use a real PRNG in code. |
| **3. Draw the story premise from tables, not just the name.** | **Correct.** | Use **axes with dependencies**, not a random sentence: institution × pressure × relationship × object × complication. The axes are curated; the draw is seeded. |
| **4. Ask for 10–20 options with probabilities and pick from the unlikely end.** | **Partly.** | This is close to **Verbalized Sampling**, which reports **1.6–2.1× diversity** in creative writing ([arXiv:2510.01171](https://arxiv.org/abs/2510.01171)). But the method samples across the verbalized distribution; picking the absolute lowest-probability option selects incoherent outliers. Use a **fit floor**: generate 10–20, discard anything that breaks voice/facts, then choose from the **lower-probability but still coherent** band. |
| **5. Keep a banlist and a “used so far” registry in the prompt and validation.** | **Yes, but validation is authoritative.** | Prompt banlists are weak and can backfire. Static name bans displace concentration to new names and can halve attested real-name representation ([name-concentration study](https://arxiv.org/abs/2611.01284)). Keep the registry in code/CI; use the prompt copy only as a reminder. |
| **6. Use decoding tricks (min-p, anti-slop sampler) only where you control the model.** | **Correct.** | Min-p needs token probabilities; anti-slop backtracks on logits and costs **69–96% throughput** at 1k–8k patterns ([Thoughtworks](https://research.thoughtworks.com/library/anti-slopping-an-innovation-for-rectifying-llm-writing-cliches)). Most APIs do not expose what these need. Use candidate generation + selection there. Also note min-p’s evidence is contested by later analysis; don’t treat it as a silver bullet. |
| **7. Audit output in CI; a person owns names and premises.** | **Correct.** | Automate collisions, schema, banned patterns and cross-project reuse; keep a human showrunner for taste, canon and the final call. |

**Bottom line:** your architecture is sound. The missing piece is **voice as a selection filter**, and the correction is **fit-filtered sampling**, not “pick the weirdest option.”

---

## 4. The operating system for a repo

Create a `writers-room/` directory in each game:

```text
writers-room/
  VOICE.md              # one page: showrunner, room, rules, naming
  TABLES/
    names.<culture>.json
    places.<culture>.json
    trades.json
    quirks.json
    premise.json
  REGISTRY.json         # used names, places, role pairs, provenance
  PROMPTS.md            # fixed-facts contract
  QUALITY.md            # nine-gate quality ladder, rubric, revision
  AUDIT.md              # CI checks + human gate
```

Templates are in [templates/writers-room/](templates/writers-room/). The key files:

- **VOICE.md** — one page. If it takes fifty pages, it is a setting bible, not a voice guide.
- **TABLES** — curated facts with weights, tags and dependencies. The model never chooses from its own prior.
- **REGISTRY** — the used-so-far memory and the cross-project collision check.
- **PROMPTS** — the contract: fixed facts in, prose out; no renaming, no new core nouns.
- **QUALITY** — the nine-gate quality ladder, rubric, revision pass and slop triage.
- **AUDIT** — deterministic checks plus a human sign-off.

### 4.1 The draw ceremony

For each arc/quest/scene:

1. **Choose the seed** — the arc ID, not the timestamp. `--seed lantern-road/q03`.
2. **Draw the facts** — 1–3 names, 1 place, 1 trade, 1 quirk, 1 premise bundle.
3. **Freeze them** in a JSON fact sheet.
4. **Human showrunner approves** or redraws.
5. **Give the model the facts as fixed canon** and ask only for prose/dialogue.
6. **Validate** the output against the registry; log provenance.

The same seed must always produce the same facts. If you want a different draw, change the seed deliberately — never let the model “choose again” until it gives something you like.

### 4.2 Table design

Each table row should have:

```json
{
  "id": "gallows",
  "value": "Gallowsfoot",
  "weight": 1,
  "tags": { "culture": "grey-march", "kind": "ford", "class": "common" },
  "requires": ["river"],
  "forbids": ["landlocked"],
  "note": "The ford where executions were held."
}
```

- **Tags** let you filter by culture, class, region, genre, tone.
- **Weights** encode “common / uncommon / rare” without making the rare option impossible.
- **Requires/forbids** prevent incoherent combinations (a ferryman in a landlocked town).
- **Notes** carry the etymology or story; the model can use it, not invent it.

Use **curated tables**, not generic fantasy lists. A random draw from a generic table is still generic. The quality of the draw is the quality of the table.

### 4.3 Premise axes

Do not draw a whole premise sentence. Draw one value from each axis, then let the room find the story:

| Axis | Example values |
| --- | --- |
| **Institution** | water court, ferry schedule, funeral debt, guild audit, border survey, salt tax |
| **Pressure** | rent due, wells failing, strike, quarantine, contested inheritance |
| **Relationship** | siblings, rivals, ex-lovers, mentor/student |
| **Object** | ledger with a missing page, ferry token, cracked bell, deed with two names |
| **Complication** | the obvious culprit is protecting someone; the fair solution ruins the petitioner; the only witness benefits; the law is on the wrong side |

The draw gives you a **situation**, not a plot. The room supplies the character who wants something inside it.

### 4.4 The model’s job

The model writes:

- prose, description, dialogue, interiority;
- variations and alternatives;
- critique against the voice bible;
- candidate names **only as suggestions**, never as canon.

The model does **not**:

- choose a core name, place, faction or trade;
- rename a fixed fact for sentence flow;
- invent a new core NPC to solve a scene;
- add a twist that contradicts the registry;
- decide the premise.

This is the division of labour that makes the room work.

### 4.5 Anti-slop quality gates

Anti-slop is not a word blacklist. The research treats slop as low **information utility** (density, relevance), low **information quality** (factuality, bias) and poor **style quality** (repetition, templatedness, coherence, fluency, verbosity, tone) — and finds that binary “is this slop?” judgments are subjective and that LLM judges are unreliable at it ([Shaib et al.](https://arxiv.org/abs/2509.19163)).

That means the room needs a **quality ladder**, not a longer banlist:

1. **Brief** — audience, purpose, voice, must-include, must-avoid, sources, length.
2. **Facts** — registry/table/source; no invented specifics.
3. **Draft** — fixed facts + voice bible; 2–3 versions if uncertain.
4. **Slop profile** — automated triage + human read for relevance, density, repetition, templatedness, tone.
5. **Fact/canon** — every proper noun/number/claim checked.
6. **Structure** — start in the situation; cut 10%; remove rhetorical scaffolding.
7. **Voice** — read aloud; blind identify the game; name-covered character test.
8. **Reader/player test** — what happened, what did you learn, what next, what felt generic?
9. **Human sign-off + provenance.**

A practical CI policy:

- **Fail** on schema/registry contradictions.
- **Warn** on `slop-audit` score above a project threshold.
- **Route** high scores to a human “suspicious queue” — the Clarkesworld model: automated triage, human review, no algorithm final ([Neil Clarke](https://neil-clarke.com/how-ai-submissions-have-changed-our-submissions-process/)).
- **Never** auto-publish or auto-reject on a slop score.

The strongest open-model lever is the **Antislop Sampler/FTPO** (8,000+ patterns, ~90% reduction), but it needs logits/fine-tuning and costs 69–96% throughput; most APIs cannot use it ([Paech et al.](https://arxiv.org/abs/2510.15061), [Thoughtworks](https://research.thoughtworks.com/library/anti-slopping-an-innovation-for-rectifying-llm-writing-cliches)). For APIs, use candidate generation, a rubric, Self-Refine and human editing.

---

## 5. Per-repo voice seeds

These are starting points, not final bibles. Each one is a **selection filter** and a **room**.

| Repo | Showrunner voice | Room | Naming field | First move |
| --- | --- | --- | --- | --- |
| **WILDY** | Campfire folk horror / cozy doom: the fire is small, the dark is patient, the kettle is always on. | Keeper, imp, woodsman, scavenger, echo | Short, spoken, worn-down; place names from camp chores and road marks | Rename the Keeper if Mira is reserved for Lantern Road; give each NPC a trade/quirk table |
| **Lantern Road** | Frontier elegy: small lives on a road that eats empires; every campfire is a eulogy waiting to happen. | War correspondent, ballad singer, quartermaster, priest | Grey March: Anglo/Germanic/folk, regional by settlement; no generic -a fantasy | Freeze the Grey March voice; reserve Rowan/Tessa/Elira; draw 10 new names for the next arc |
| **Repository Town** | Civic magical realism: everyone knows the ledger, and the ledger knows back. | Town clerk, gossip, folklorist, comic | Occupational/regional; names that sound like they belong to a street, not a fantasy novel | Define 20–24 core cast; one actor-state API; 8–12 arcs |
| **The Undercity** | Bureaucratic surrealism: Kafka by gaslight; the city is a filing cabinet that dreams. | Clerk, archivist, dissident, ghost | Institutional/Byzantine; district names from functions, not Ash/Thorn compounds | Promote 12–16 prose roles into a cast with IDs and memory |
| **Neathbound** | Subterranean gothic: the city beneath remembers what the city above deleted. | Archivist, ferryman, child, heretic | Clipped, mineral, archival; place names from strata and records | 8–12 recurring cast; one social hub; returnable locations |
| **KKC Adventure** | Academic picaresque: wit is currency, tuition is a wound, every mentor is a locked door. | Student, master, rival, gossip | Canon language families; new NPCs must fit the phonology, not the fantasy default | Add memory/callbacks and one arc per NPC; unify the two implementations |
| **Astra** | Mythic frontier: the DM is an oracle with a ledger; every legend has a receipt. | Oracle, drifter, magistrate, skeptic | Hollow Marches: regional, plain-spoken, moral weight | Add `npcs[]` and an 8–12 person persistent cast; AI narrates, never invents facts |
| **Grey March / Marsh** | Shared **Grey March chronicle** with Lantern Road. | Reeve, smuggler, priest, soldier | Same Grey March tables; shared registry | Reuse Lantern Road voice; deepen 13 NPCs; do not duplicate names |
| **dndgame / SwordCoast** | Pulp heroic: tavern, torch, terrible decision; the world is a serial. | Bard, veteran, trickster, quartermaster | Simple, legible, regional; avoid Kael clones | Replace greeting+hook with 3-node conversations; one code family |
| **Whirring Wilderness** | Wilderness tall tale: the woods are bigger than the map, and the map knows it. | Trapper, cartographer, campfire liar, hermit | Place names from rivers, traps, portages, failed surveys | 8–10 NPCs, schedules, one social hub |
| **Whispering-Wilds** | Storybook parser: a small fire in a large forest; every room is a sentence. | Caretaker, hermit, trader, ranger | Small, oral, folkloric | Use as the schema testbed; one faction and one 3-scene arc |

The point is not to make every game “literary.” It is to make each game **identifiable in 200 words**. If a reader cannot tell which game a scene belongs to, the voice is not distinct enough.

---

## 6. The numbered roadmap

**One repo at a time.** Each phase has a stop/go gate. Do not start the next repo until the current gate passes.

### Phase 1 — Build the room kit (1 week, once)

1. **Write the operating principles.** Voice is the frame; tables are entropy; registry is memory; the human showrunner owns canon. Put this in `writers-room/README.md`.
2. **Create the templates.** Use [templates/writers-room/](templates/writers-room/): `VOICE.md`, `QUALITY.md`, tables, registry, prompts, audit.
3. **Install the tools.** `node tools/table-draw.mjs` for deterministic facts; `node tools/name-audit.mjs` for collisions; `node tools/slop-audit.mjs` for quality triage; a CI schema check.
4. **Define the gates.** Voice bible approved; 30+ curated facts per culture; 3 reproducible draws; 3 scenes written; blind reader identifies the game; slop profile reviewed by a human; zero new cross-project core collisions.

**Gate:** a one-page voice bible and a seeded draw that a second person can reproduce exactly.

### Phase 2 — Pilot: WILDY (1–2 weeks)

5. **Write WILDY’s one-page voice bible.** “Campfire folk horror / cozy doom.” Three room voices, forbidden tics, naming field, what it is not.
6. **Build the WILDY tables.** 30 names (camp/road cultures), 12 places, 12 trades, 12 quirks, 6 premise axes. Mark Mira as reserved for Lantern Road; draw a replacement if needed.
7. **Draw and rewrite three NPCs.** Give each a fixed name, trade, quirk, want, contradiction and one callback. No model-chosen names.
8. **Blind test.** Show 200 words from the old and new versions to 3–5 readers; ask “which game is this?” and “would you talk to this person again?”
9. **CI.** Name audit, registry, forbidden phrases, cross-project collisions, slop-audit warning, human review queue.

**Gate:** 3/5 readers identify WILDY from a 200-word sample; no new cross-project core names; the showrunner prefers the new voice to the old.

### Phase 3 — Lantern Road (2–3 weeks)

10. **Freeze the Grey March voice.** Shared with Marsh; reserve Rowan/Tessa/Elira; write the naming field by settlement and class.
11. **Build shared Grey March tables.** Names, places, trades, quirks, premise axes; one registry for Lantern + Marsh.
12. **Rewrite five NPCs** with fixed facts, 3-node conversations and first-return callbacks. Add one NPC-to-NPC scene.
13. **Audit.** No duplicate name+role pairs; faction consequences visible; blind voice test; slop profile and human quality pass.

**Gate:** Lantern Road and Marsh share a registry with zero accidental collisions; a reader can distinguish Grey March from WILDY and Repository Town.

### Phase 4 — Repository Town (3–4 weeks)

14. **Define the showrunner voice.** Civic magical realism; the town as a character; the ledger as a motif.
15. **Pick 20–24 core cast**, each with a fixed name, trade, home, schedule, want, contradiction and one relationship. The rest are explicitly ambient.
16. **Draw the next 8–12 arcs** from tables; human approves; actor-state API supplies facts to dialogue.
17. **Add NPC-to-NPC scenes** and callback validation.

**Gate:** 20 core NPCs pass the presence test (identity + place + routine + memory + consequence + expression); no channel contradicts another.

### Phase 5 — The Undercity (2–3 weeks)

18. **Write the voice bible.** Bureaucratic surrealism; the city as a filing cabinet that dreams.
19. **Promote 12–16 prose roles into a cast.** Stable IDs, home district, schedule, relationship, witness memory.
20. **Attach every ambition chapter to a recurring NPC**; add first-return and aftermath lines.
21. **Build district/trade tables** from institutions, not fantasy compounds.

**Gate:** 12 recurring NPCs are recognisable across at least two storylets each; the witness ledger is real state.

### Phase 6 — Neathbound (2 weeks)

22. **Voice bible:** subterranean gothic; archival horror; the city beneath remembers.
23. **8–12 recurring cast**, one social hub, returnable locations.
24. **Add NPC/relationship fields to the storylet schema**; validate callbacks.

**Gate:** a player can name three Neathbound NPCs and what they want after one session.

### Phase 7 — KKC Adventure (2 weeks)

25. **Voice bible:** academic picaresque; wit as currency; mentorship as locked door.
26. **Canon phonology:** original NPC names fit the language families; no generic fantasy defaults.
27. **Memory ledger and internal voices:** Wit/Empathy/Authority/Scholarship comment on conversations; failure reveals character.
28. **One arc per NPC**; unify the two implementations.

**Gate:** Simmon/Wilem/Kilvin/Ambrose/Elodin each have a distinct voice and a callback; no canon collisions.

### Phase 8 — Astra (3 weeks)

29. **Voice bible:** mythic frontier; the DM as oracle with a ledger.
30. **Add `npcs[]` to the state schema**: ID, name, role, location, goal, relationship, knowledge, promises, last seen, alive/dead.
31. **Author 8–12 recurring NPCs**; AI voices them within fixed facts; no invented names/places.
32. **Known-faces journal, campaign clock, callbacks.**

**Gate:** a named NPC, promise and quest survive a long campaign + export/restore; zero AI-invented canon contradictions in a 20-turn test.

### Phase 9 — Grey March / Marsh (1–2 weeks)

33. **Reuse the Lantern Road voice bible and registry.** Deepen 13 NPCs; add schedules, 3-node conversations, visible faction consequences.
34. **Do not create a second Grey March naming field.**

**Gate:** Lantern + Marsh feel like one world, not two parallel drafts.

### Phase 10 — dndgame / SwordCoast (1–2 weeks)

35. **Voice bible:** pulp heroic; the world as a serial.
36. **Replace greeting + quest hook with a 3-node conversation**; add memory, trust and promises.
37. **One code family; one registry.**

**Gate:** 9 NPCs return after the main quest with changed lines; no Kael clones.

### Phase 11 — Whirring Wilderness (2 weeks)

38. **Voice bible:** wilderness tall tale.
39. **8–10 NPCs**, schedules, one social hub, one faction.
40. **Tables for trapper/cartographer/portage names**; 3-node conversations.

**Gate:** the camp feels populated; three NPCs are recognisable by voice alone.

### Phase 12 — Whispering-Wilds (1 week)

41. **Use it as the schema/testbed**, not a content mountain.
42. **One faction, one 3-scene arc, one naming culture** to prove the kit on a tiny codebase.

**Gate:** the same `VOICE.md`/tables/registry schema works without modification.

### Phase 13 — Quarterly room retreat (ongoing)

43. **Refresh tables** after every content drop; retire overused names; add one guest voice per quarter.
44. **Audit the portfolio**: cross-project names, role-pair collisions, top-10 share, semantic similarity of premises.
45. **Ask the hard question:** which game’s voice is becoming indistinguishable from another? Fix that before adding content.

---

## 7. What to measure

| Metric | Target | Why |
| --- | --- | --- |
| Blind voice identification | ≥ 4/5 readers identify the game from 200 words | Distinctiveness |
| Core-name recall | ≥ 3 NPCs named + one want each after a session | Presence |
| Cross-project core-name collisions | 0 unless shared canon | Coherence |
| Role+name repeats | 0 across universes | Prevents “Mira the keeper” |
| Top-10 name share | < 20% | Corpus diversity |
| Seeded draw reproducibility | 100% | Trust in the table |
| Contradiction rate | 0 against registry | Canon truth |
| Premise similarity | lower than baseline | Story variety |
| Showrunner approval | 100% of core names/premises | Ownership |
| Reader “would talk again” | ≥ 70% for core NPCs | Relationship pull |

---

## 8. Risks and how to avoid them

| Risk | Symptom | Fix |
| --- | --- | --- |
| **Pastiche** | “This is just Martin with the serial numbers filed off.” | Use the writer as a **selection filter**, not a voice to imitate; write an original synthesis; ban signature phrases/names. |
| **Committee blandness** | Every game sounds like the same pleasant fantasy. | One showrunner, 3–5 voices, guest friction; voice test across games. |
| **Generic tables** | Random draws still produce Ashwood, Kael and Mira. | Curate tables from cultures/institutions/history; audit top-10 share; retire defaults. |
| **Random incoherence** | A ferryman in a landlocked town; a court intrigue in a survival camp. | Tags, requires/forbids, fit floor, human approval. |
| **Over-constraint** | Every scene is a table lookup; no surprise. | Allow 10–20% “guest” facts; let the room improvise inside the frame. |
| **Model renames facts** | The prose “fixes” a name or place for flow. | Fixed-facts contract; validator; reject/regenerate. |
| **Registry drift** | Two games quietly reuse the same core name. | CI audit; one shared registry across universes; status field. |
| **Cultural flattening** | “Diverse” names drawn from a generic list. | Culture-specific tables, consultation, pronunciation/etymology; do not use real names as decoration. |
| **AI automation bias** | The showrunner rubber-stamps whatever the model proposes. | Human approval gate; blind tests; keep a “reject” log. |

---

## 9. The one-page implementation rule

If you remember nothing else:

1. **One showrunner per repo.**
2. **One-page voice bible.**
3. **Curated tables, not model memory.**
4. **Seeded code draw, fixed facts.**
5. **10–20 candidates, fit-filtered, not absolute-lowest.**
6. **Registry in code/CI, not just the prompt.**
7. **Decoding tricks only on models you control.**
8. **Human owns names and premises.**

That is the difference between “AI wrote a fantasy game” and “this studio has a voice.”

---

## Sources

- *Showrunner.* Wikipedia. [link](https://en.wikipedia.org/wiki/Showrunner) — role, tone, head writer, final authority.
- *Writers’ room.* Wikipedia. [link](https://en.wikipedia.org/wiki/Writers%27_room) — room sizes 2–30, no single formula, UK single-writer/voice-driven tradition, criticisms.
- *Bible (screenwriting).* Wikipedia. [link](https://en.wikipedia.org/wiki/Bible_%28screenwriting%29) — story bible, continuity, “walking bibles.”
- *Languages constructed by Tolkien.* Wikipedia. [link](https://en.wikipedia.org/wiki/Languages_constructed_by_Tolkien) — glossopoeia, language families, “a name comes first and the story follows.”
- *George R. R. Martin.* Wikipedia. [link](https://en.wikipedia.org/wiki/George_R._R._Martin) — background; the voice/naming analysis is interpretive, grounded in the primary works.
- *Star Wars.* Wikipedia. [link](https://en.wikipedia.org/wiki/Star_Wars) — franchise background; the mythic/pulp analysis is interpretive.
- *Steven Moffat.* Wikipedia. [link](https://en.wikipedia.org/wiki/Steven_Moffat) — showrunner/head writer background; the voice analysis is interpretive.
- Zhang, J. et al. (2025/2026). *Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity.* [arXiv:2510.01171](https://arxiv.org/abs/2510.01171) — 1.6–2.1× diversity; probability-verbalized candidate sets.
- Zhao, M., Du, Y. & Wang, M. (2026). *Large Language Models Are Bad Dice Players.* ACL 2026. [link](https://aclanthology.org/2026.acl-long.1051/) — LLMs lack a functional internal sampler; external RNG needed.
- Nguyen, M. et al. (2025). *Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs.* ICLR 2025. [link](https://proceedings.iclr.cc/paper_files/paper/2025/hash/afa5f124e36bed5cc2125067005d43f5-Abstract-Conference.html) — min-p; caveat: contested by later critical analysis ([NeurIPS 2026](https://neurips.cc/virtual/2026/loc/sydney/166291)).
- Roush, A. & Mahajani, P. (2026). *Anti-slopping: An innovation for rectifying LLM writing clichés.* Thoughtworks. [link](https://research.thoughtworks.com/library/anti-slopping-an-innovation-for-rectifying-llm-writing-cliches) — anti-slop sampler, 69–96% throughput cost, logit access.
- Mozo Quesada, A. et al. (2026). *Character-Name Concentration in LLM Fiction.* [arXiv:2611.01284](https://arxiv.org/abs/2611.01284) — static banlists displace; dynamic tracking works.
- Hamilton, S. & Mimno, D. (2026). *Elias in the Lighthouse, Again?* [arXiv:2605.26492](https://arxiv.org/abs/2605.26492) — 11 words in 88.3% of stories; alignment data.
- Brzozowski, M. & Chung, N. C. (2026). *The Ghost Couple.* [arXiv:2606.02184](https://arxiv.org/abs/2606.02184) — correlated name ensembles.
- Doshi, A. R. & Hauser, O. P. (2024). *Generative AI enhances individual creativity but reduces the collective diversity of novel content.* [doi](https://doi.org/10.1126/sciadv.adn5290).
- Shumailov, I. et al. (2024). *AI models collapse when trained on recursively generated data.* [doi](https://doi.org/10.1038/s41586-024-07566-y).
- Shaib, C., Chakrabarty, T., Garcia-Olano, D. & Wallace, B. C. (2025/2026). *Measuring AI “Slop” in Text.* [arXiv:2509.19163](https://arxiv.org/abs/2509.19163) — slop taxonomy, subjectivity, automated limits.
- Paech, S., Roush, A., Goldfeder, J. & Shwartz-Ziv, R. (2025). *Antislop.* [arXiv:2510.15061](https://arxiv.org/abs/2510.15061) — 8,000+ patterns, 90% reduction, FTPO, DPO degradation.
- Clarke, N. (2025). *How “AI” submissions have changed our submissions process.* [Clarkesworld](https://neil-clarke.com/how-ai-submissions-have-changed-our-submissions-process/) — automated triage, human review, false positives.
- Madaan, A. et al. (2023). *Self-Refine.* [NeurIPS 2023](https://papers.nips.cc/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html) — iterative revision gains.
- Shi, L. et al. (2025). *Judging the Judges.* [IJCNLP-AACL 2025](https://aclanthology.org/2025.ijcnlp-long.18/) — position bias in LLM judges.
- *AI Writing Tropes to Avoid* / `deslopify`. [list](https://github.com/danicat/skills/blob/main/writing/deslopify/references/tropes.md) — practitioner trope list.

**Limits:** the author analyses are interpretive craft readings, not controlled studies; the TV-room sources describe a production model, not a guaranteed quality mechanism; the sampling research is mostly on English creative writing, not game dialogue; no playtest has validated this specific pipeline yet.
