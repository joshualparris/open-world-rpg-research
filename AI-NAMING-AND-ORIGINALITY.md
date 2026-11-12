# Why AI Keeps Naming People Mira — and How to Make It Original

**A research note on name concentration, correlated character priors, generic places and stories — and a practical originality system for the game portfolio.**

Prepared 2026-11-12 · Desk research + a local name audit. Not a controlled experiment on your games.

Companion files: [NAMING-PLAYBOOK.md](NAMING-PLAYBOOK.md) · [tools/name-audit.mjs](tools/name-audit.mjs) · [data/name-commons.json](data/name-commons.json) · [SOURCES.md](SOURCES.md)

---

## The short answer

“Mira” is not a random glitch. It is the visible tip of three overlapping loops:

1. **Model prior** — LLMs concentrate on a small pool of short, familiar, easy-to-pronounce names. In current English short fiction the measurable core is **Elias, Mara and Elara**; “Mira” belongs to the same soft, two-syllable, open-vowel family.
2. **Alignment/typicality** — preference tuning makes models prefer “safe, familiar, broadly acceptable” outputs. A small amount of preference data can have a disproportionate effect; the “Elias the lighthouse keeper” pattern is the clearest published example.
3. **Your own name commons** — in this workspace, **Mira is already canonical in Lantern Road, WILDY and Astra’s opening**, Kael recurs across dndgame/SwordCoast/StarHaven, and Rowan/Tessa/Elira are shared across the Grey March projects. When new content is generated with those repos in context, the model learns “this is what a character here is called.”

So the fix is not just “ask for more original names.” It is a **system**: external entropy, naming cultures, candidate generation, corpus-level tracking, a canonical registry, and human selection.

---

## 1. What is actually happening

### 1.1 The published pattern: eleven words in 88% of stories

Hamilton and Mimno sampled **20,000 stories from four current models** and found that **11 words occur in 88.3% of generated stories**, with little difference between model families ([arXiv:2605.26492](https://arxiv.org/abs/2605.26492)).

The core tokens were:

- names: **Elias, Mara, Elara**
- settings: **lighthouse**
- professions: **keeper, baker, mayor, clockmaker, fisherman, librarian, conductor**

Rates were extreme: lighthouse appeared in **51.2%** of stories, keeper in **48.1%**, Elias in **26.5%**, Mara in **16.7%**, Elara in **13.1%**; **66.6%** contained the full “Elias the lighthouse keeper” combination.

Crucially, the authors found these tokens **do not occur with unusual frequency in published literature or pre-training data**. They trace them to **preference/alignment data** — including a small set of post-training stories (3,053 of 78,958, about **3.8%**) that were enough to reshape the output distribution. Their conclusion: small datasets plus powerful alignment algorithms can have a disproportionate effect ([arXiv:2605.26492](https://arxiv.org/abs/2605.26492); [Gizmodo summary](https://gizmodo.com/why-do-chatbots-keep-telling-stories-about-someone-named-elias-thorne-2000770629)).

This is the mechanism behind the “Elias Thorne” phenomenon: a name that no one can trace to a real person, repeated across models because it lives in the post-training consensus.

### 1.2 Name concentration is measurable — and banlists do not fix it

A 2026 study generated **44,782 stories from 20 LLMs in four languages**, producing **88,919 named characters**. It measured a **Slop Ratio** — a list-free collision metric — and tested eight mitigation strategies ([arXiv:2611.01284](https://arxiv.org/abs/2611.01284)).

Key findings:

- **Static banlists do not remove slop.** They displace it to **emergent names**, and more than **halve the share of attested real names** (a representation cost).
- The sampling scaffold alone cut Slop Ratio by **89%** on average.
- Adding a dynamic **SlopTracker** (per-model fingerprint + runtime counter) brought the total reduction to **95%**.
- Mean collision probability fell from **7.3% to 0.4%**; known-name collisions held at **zero**; within-story collisions fell from **4.3% to 0.2%**.
- Naturalness stayed close to baseline: **42–69%** attested real names by language.
- The ranking held across languages and model families.
- **Anti-slop prompts** were weak; **reasoning mode** did not reduce name slop.
- **Vision input** lowered slop in 4 of 5 model families — a useful reminder that changing the conditioning channel changes the prior.

The practical lesson: **don’t just ban names; track the distribution and sample against it.**

### 1.3 Models produce correlated ensembles, not independent names

The “Ghost Couple” paper shows that LLMs do not merely default to high-probability individual names — they generate **correlated character ensembles** at rates far above chance ([arXiv:2606.02184](https://arxiv.org/abs/2606.02184)):

- Claude-family: **Elena Vasquez + Marcus Chen + Amara Okafor**
- Gemini-family: **Aris Thorne + Lena Petrova**
- GPT-family: **Elara Voss** (with no fixed partner)

These priors are **model-family-specific and version-specific**, and can be suppressed at release boundaries — leaving dateable fingerprints. The paper also documents downstream pollution: 1,655 ghost-authored Zenodo records with real DataCite DOIs, fabricated journals and backdated timestamps.

For game design, the important point is: **a cast is not a bag of independent names**. Models produce *pairs and trios* that feel like a house style. If you accept a whole set at once, you inherit the correlation.

### 1.4 “Artificial Hivemind”: semantic collapse survives high temperature

The Artificial Hivemind work documents open-ended homogeneity: models converge on a narrow consensus even for questions with many valid answers, with **pairwise semantic similarity around 0.80–0.90 even under high-temperature sampling** ([NeurIPS 2025 paper](https://papers.nips.cc/paper_files/paper/2025/file/754d5a526a5ee5a47220664a0eb92751-Paper-Datasets_and_Benchmarks_Track.pdf)).

“Beyond the Hivemind” tests a mitigation: **meta-persona anchoring** (model self-selects an idiosyncratic persona before answering) plus **filtered temperature scaling** (top-p first, then extreme temperature on the surviving candidates). Average pairwise cosine similarity dropped from **≈0.85 to ≈0.65** ([arXiv:2608.02618](https://arxiv.org/abs/2608.02618)).

Temperature alone is not a diversity knob. Temperature changes the shape of a distribution that is already collapsed.

### 1.5 Individual creativity up, collective diversity down

Doshi and Hauser's controlled study found that writers given LLM story ideas produced stories judged **more creative, better written and more enjoyable** — especially less-creative writers — but the AI-assisted stories were **more similar to each other** than stories written without AI. Individual creativity rose; **collective novelty fell** ([Science Advances, doi](https://doi.org/10.1126/sciadv.adn5290); [UCL record](https://discovery.ucl.ac.uk/id/eprint/10195027/)).

This is the social dilemma of AI-assisted worldbuilding: the first draft gets better, the corpus gets narrower.

### 1.6 Model collapse: don’t train on unfiltered AI output

Recursive training on model-generated data can degrade diversity and quality over generations — “model collapse” ([Shumailov et al., Nature 2024, doi](https://doi.org/10.1038/s41586-024-07566-y)). For a game studio, the practical rule is: **do not let generated content become canon or training data without human filtering and provenance.**

---

## 2. Why “Mira”, specifically

There are two layers.

### 2.1 The model-level family

“Mira” has the features models reach for:

- **Two syllables**, easy stress, no consonant clusters.
- **Open final vowel** (-a), like Elara, Mara, Lyra, Aria, Seraphina.
- A **real given name in several language traditions** (Slavic, Indic, Romance and others), so it is familiar without being tied to one obvious culture.
- Soft sonority: m + vowel + r + vowel; easy for English speakers to pronounce and remember.
- It fits the **“mysterious but warm”** role cluster: keeper, healer, guide, innkeeper, scout.

The published top-name lists do not name Mira specifically; the point is that Mira belongs to the same **high-probability, “safe-familiar” family** as Elara/Elias/Mara. It is the kind of name a model produces when it is optimizing for “plausible fantasy name that won’t offend anyone.”

### 2.2 The local loop

In this workspace, Mira is not only a model prior; it is **canon**:

| Project | Mira’s role | Evidence |
| --- | --- | --- |
| **Lantern Road** | Mira Quickstep, scout companion with a personal arc | `story/companions/MIRA.md`, content data |
| **WILDY** | Mira, Keeper of Ember Camp | `src/npcs.js` |
| **Astra** | “Mira’s daughter” in the opening state/prompt | `server/world.cjs` |

That is three different universes using the same core name. Once Mira is in the repos/prose/context, new generation sees it as **house style**, not as a random draw. The model is doing what models do: continuing the distribution it is given.

This is the critical distinction:

- **Model bias** explains why *this family* of names is likely.
- **Local canon** explains why *this specific name* keeps reappearing in your work.
- **Process** explains why it survives: no registry, no collision check, no corpus-level diversity metric.

### 2.3 Other local patterns

A quick GitHub search and a scan of the local clones found:

- **Kael** — dndgame, SwordCoast, StarHaven (probably shared code/data).
- **Rowan** — Repository Town, Lantern Road, Grey March/Marsh; in Lantern and Marsh he is **Mayor of Hearthwick**.
- **Tessa** — Lantern Road and Marsh; both **innkeepers** (Tessa Reed).
- **Elira** — Lantern Road and Marsh; both **Road Priest** (Sister Elira).
- **Lyra** — Repository Town voice roster.
- **Thorne** — Schism.
- **Elara** — one hit in dndgame pasted text; also a top model-default name.

Some of this is **deliberate shared canon** (Lantern Road and Grey March/Marsh share the Grey March setting; Rowan/Tessa/Elira are the same people). Some is **code reuse** (dndgame/SwordCoast/StarHaven). Some is **cross-universe drift** (Mira in Lantern, WILDY and Astra). The audit should classify before renaming; do not “fix” intentional canon.

---

## 3. Other patterns to audit

The research gives hard numbers for names and professions; the rest are craft observations to test in your corpus, not universal laws.

### 3.1 Names and ensembles

- Soft feminine names ending in **-a**: Elara, Mara, Lyra, Aria, Seraphina, Mira.
- Short masculine names with **K/Th/R**: Kael, Kaelen, Thorne, Cassian, Rowan.
- **Role-coupled names**: Mira the keeper/healer, Kael the rogue, Rowan the mayor/leader, Lyra the musician, Thorne the villain.
- **Correlated pairs/trios**: the Ghost Couple pattern; a cast that “sounds right” because the model has produced the set before.

### 3.2 Places

- Compound **adjective/noun + settlement suffix**: Ashwood, Thornfield, Silverwood, Duskmere, Emberfall, Oakhaven, Raven’s Reach.
- **Lighthouse/village/archive/clocktower** as default settings.
- **Place names with no economy, history or pronunciation layer** — they are labels, not places.
- Every place has a “dark secret” rather than a **specific function** (ferry crossing, salt tax, failed mill, border survey).

### 3.3 Professions and roles

The Elias study’s core professions are a useful watchlist: **keeper, baker, mayor, clockmaker, fisherman, librarian, conductor**. Add the game-specific cluster: **innkeeper, blacksmith, healer, archivist, ferryman, guard captain, scavenger, merchant**.

Ask: is this NPC’s role a **job with a life**, or a **quest dispenser with a costume**?

### 3.4 Story shapes

Common defaults in AI fantasy:

- the chosen one / hidden heir / prophecy;
- the ancient evil returning;
- amnesia / the protagonist who forgot;
- the dying mentor’s last request;
- the town with a secret;
- the price of magic;
- “the real monster was grief”;
- a letter/knock at the door that starts the plot;
- the heist/ritual/festival that goes wrong.

These are not forbidden — they are **defaults**. If you use one, give it a specific institutional, economic or cultural cause that could only belong to this world.

### 3.5 Titles and dialogue

- “The Last ___”, “The ___ of ___”, “A ___ of ___”.
- “You’re not from around here.”
- “The old stories say…”
- “I haven’t seen you before.”
- “You have your mother’s eyes.”
- “There’s something you should know.”

Audit your scripts for these; replace with a line that could only come from this character, in this place, with this history.

---

## 4. What does *not* work

| Approach | Why it fails |
| --- | --- |
| “Be original” / “avoid clichés” | Too vague; the model has no external reference for what you consider generic. |
| Static banlist of names | Displaces concentration to new names; can halve attested real-name representation ([name-concentration study](https://arxiv.org/abs/2611.01284)). |
| Raise temperature | Collapse is semantic, not just lexical; high temperature alone leaves the model in the same basin ([Artificial Hivemind](https://papers.nips.cc/paper_files/paper/2025/file/754d5a526a5ee5a47220664a0eb92751-Paper-Datasets_and_Benchmarks_Track.pdf)). |
| Persona prompt only | Fine-grained persona prompting alone did not raise lexical diversity in the name-concentration study; it needs external entropy/selection. |
| Reasoning mode | Did not reduce name slop in the same study. |
| One-shot generation | No candidates, no comparison, no corpus counter. |
| Human “feels fresh” | Familiarity is a feature to the reader; without a blind panel/registry, the same names win. |
| Asking the model to invent a language from scratch | Often produces aesthetic pastiche; needs phonology, constraints and curation. |

The deeper problem: **static controls treat symptoms**. You need a **pipeline** that generates many candidates, scores them against a corpus, and selects for fit + novelty.

---

## 5. What works

### 5.1 External entropy, not model memory

The practical naming skill from jwynia puts it bluntly: *“LLMs default to statistical medians. External entropy is the only cure.”* Its symptoms — Chen proliferation, median-hopping, cultural incoherence, cast collision, character mismatch — are exactly the patterns above ([character-naming skill](https://github.com/jwynia/agent-skills/blob/main/skills/creative/fiction/character/character-naming/SKILL.md)).

Use the model for **evaluation and variation**, not as the source of the name pool. Draw from:

- curated real-name lists (with cultural context and licensing);
- phoneme/syllable generators;
- historical/occupational/place-name corpora;
- random seeds chosen outside the model.

### 5.2 Speculative naming (the strongest published method)

The name-concentration paper's method is fine-tuning-free and works at corpus level:

1. Scaffold the story with **name placeholders**.
2. Ask the model for **candidate name-sets** with verbalized probabilities (not one name).
3. Score each candidate against a **SlopTracker**: a per-model baseline fingerprint + a runtime counter of names already used.
4. Select with a **temperature-controlled rule** (or a strict “HARD” rule) that favors fit and freshness.
5. Substitute the chosen names and update the tracker.

Reported results: **95% Slop Ratio reduction**, collision **7.3% → 0.4%**, known-name collisions zero, within-story **4.3% → 0.2%**, naturalness 42–69% attested.

You do not need the exact paper implementation to use the idea. The minimum viable version:

- generate **8–12 candidate sets**, not one;
- score each candidate for **fit**, **phonotactic legitimacy**, **collision with registry**, and **“how likely is this the model's first answer?”**;
- select the best set that is **not** the model's most typical;
- update a project-level count.

### 5.3 Phonology-first naming cultures

Define a naming culture before names:

- syllable inventory (CV, CVC, CCV…);
- stress pattern;
- allowed/forbidden clusters;
- word-final sounds;
- morphology (patronymic, clan, occupational, toponymic);
- social registers (formal, common, nickname, insult, exonym);
- taboo sounds/names;
- historical layers (older form → modern form).

Then generate **templates** and **candidates**, and let the model evaluate which fit. This prevents “Kael, Zephyrine and Bob in the same kingdom” ([character-naming skill](https://github.com/jwynia/agent-skills/blob/main/skills/creative/fiction/character/character-naming/SKILL.md)).

### 5.4 Toponymy, not adjective+noun

Name places from:

- geography (ford, escarpment, spring, harbour, pass);
- economy (mill, saltworks, tannery, market, ferry);
- history (battle, plague, saint, treaty, survey error, dispossession);
- layers (local name, official name, outsider name, nickname);
- pronunciation change over time.

A place name should encode **why someone stopped there**. “Ashwood” encodes nothing; “Gallowsfoot” encodes a story; “The Dew Line” encodes a surveyor’s mistake.

### 5.5 Story constraints and institutional specificity

Instead of “write a fantasy story,” constrain:

- a specific institution (water court, ferry schedule, guild audit, funeral debt, border survey);
- a specific economic pressure (salt tax, failed harvest, rent, monopoly);
- a specific social role (clerk, ferryman, archivist, tax collector);
- a specific point of view (a child, an outsider, a document, a rival);
- a ban on the defaults (prophecy, chosen one, ancient evil, amnesia, hidden heir).

Then generate **many premises**, cluster them, and choose the outliers. “Specific” beats “original” as an instruction.

### 5.6 Meta-persona anchoring + filtered temperature

For semantic diversity, the Beyond the Hivemind method is useful:

- ask the model to **self-select an idiosyncratic persona** (a specific local historian, a hostile witness, a bureaucratic clerk);
- use top-p to keep coherence, then **high-temperature variation** over the surviving candidates;
- generate several perspectives and compare.

The paper reports pairwise similarity **0.85 → 0.65**. This is a semantic-diversity lever, not a name-specific one; combine it with the naming pipeline.

### 5.7 A registry and a name council

Keep a canonical registry:

- name, pronunciation, culture, meaning/etymology;
- project/universe, role, first use;
- status: owned / shared canon / retired / watchlist;
- variants, nicknames, exonyms;
- collision notes.

A human “name council” (even one person) approves core names. The model proposes; the registry decides.

### 5.8 Corpus-level metrics

Track:

- **collision probability** and top-10 share;
- **within-story duplicate rate**;
- **cross-project reuse** (core names);
- **role-name correlation** (are all healers Mira?);
- **attested real-name share** (is the culture represented?);
- **semantic similarity** of premises/stories;
- **human blind ratings** for distinctiveness, memorability, fit.

See [tools/name-audit.mjs](tools/name-audit.mjs) for a starter.

---

## 6. A naming system for the portfolio

### Step 0 — Audit before renaming

1. Export the cast/place lists from each game.
2. Run the name audit at the parent directory of the repos.
3. Classify each collision:
   - **Intentional shared canon** (Grey March: Rowan, Tessa, Elira).
   - **Code family** (dndgame/SwordCoast/StarHaven: Kael).
   - **Accidental cross-universe** (Mira in Lantern/WILDY/Astra).
   - **Model watchlist** (Elara, Elias, Mara, Aria, Seraphina).
4. Do not rename shared canon just because it repeats.

### Step 1 — Assign name ownership

Use [data/name-commons.json](data/name-commons.json). Suggested decisions:

- **Mira** — reserve for Lantern Road; rename WILDY’s Keeper and Astra’s opening NPC, or make the shared-universe link explicit. Do not add a fourth Mira.
- **Rowan/Tessa/Elira** — keep as Grey March shared canon; document the shared setting.
- **Kael** — one code family; rename if StarHaven is a separate universe.
- **Lyra/Thorne** — reserve the name+role; avoid a new bard/villain with those names.
- **Elara/Elias/Mara/Aria/Seraphina** — watchlist; only use with a specific cultural/phonological reason, not because they sound fantasy.

### Step 2 — Define 2–4 naming cultures per game

For each culture, write a one-page phonology and naming convention. Example fields:

| Field | Example |
| --- | --- |
| Sound | CV/CVC; initial stress; final -a/-e; no “th” |
| Morphology | occupational suffix + clan prefix |
| Registers | ritual name / common name / nickname |
| Taboo | names of the dead not spoken for a year |
| History | old form → modern form |
| Place grammar | “ford of X”, “X’s hill”, “new X” |

### Step 3 — Generate with external entropy

- scripts: phoneme/syllable generators, name lists, toponymy lists;
- model: candidate sets, not single names;
- random seeds chosen outside the model;
- multiple personas: a tax clerk, a ferryman, a child, a foreign cartographer, a priest.

### Step 4 — Score and select

Score each candidate:

- **Fit** (culture, class, era, role).
- **Phonotactic legitimacy** (can you pronounce it? does it break the rules for a reason?).
- **Collision** (registry, current cast, cross-project).
- **Memorability** (can a player repeat it after one hearing?).
- **Distinctiveness** (does it avoid the model's first answer?).
- **Role independence** (does it avoid “Mira the healer”).
- **Cultural care** (is it a real name used with respect/context?).

### Step 5 — Human approval and provenance

Record:

- who proposed/approved;
- model and prompt version (if used);
- seed/entropy source;
- edits;
- universe ownership.

### Step 6 — Measure

Run the audit after each content drop. Set project thresholds, e.g.:

- top-10 name share < 20%;
- collision probability < 1%;
- within-story duplicates = 0;
- cross-project core-name collisions = 0 (unless registered shared canon);
- no role-name pair repeated across universes.

---

## 7. Prompt patterns that help

Full prompt pack: [NAMING-PLAYBOOK.md](NAMING-PLAYBOOK.md).

### 7.1 Surface the prior, then avoid it

```
Before generating, list the 15 character names, 10 place names, 8 professions and 5 twists
you would normally produce for this brief. Label them "default".
Do not use any of those defaults in the actual answer.
```

### 7.2 Phonology-first

```
Generate 10 phonotactic templates and then 40 names for a culture with:
- CV and CVC syllables, initial stress, final vowels a/e/i;
- no initial consonant clusters;
- taboo sound "th";
- occupational suffixes -ward, -smith, -kell.
Give 5 names that are loanwords from a neighbouring culture and explain the adaptation.
Avoid the attached registry names.
```

### 7.3 Candidate sets with scoring

```
Give 8 candidate name-sets for [roles]. Each set: 4 names, a 0-1 fit score,
a 0-1 "how likely is this the first set you would produce" score, and one line
of etymology. Do not repeat a name across sets.
```

### 7.4 Place layers

```
Name 12 places from geography, economy and history:
a ford, a failed mill, a salt road, a border survey error, a saint's well,
a dispossessed village.
For each: local name, official name, outsider name, and one lie locals tell
about how it got the name. No Ash/Thorn/Shadow/Ember + wood/haven/reach compounds.
```

### 7.5 Story constraint cards

```
Generate 12 premises, each anchored in a specific institution or economy
(water court, funeral debt, ferry schedule, guild audit, border survey).
No chosen one, prophecy, ancient evil, amnesia or hidden heir.
Then pick the 3 least similar and explain why.
```

### 7.6 Person before role

```
For each NPC: want, obstacle, contradiction, secret, nickname, how they
mispronounce a rival's name, and one thing they are wrong about.
Name them after the person, not the role.
```

### 7.7 Originality editor

```
Act as an editor who hates generic fantasy. Mark every name, place, profession
and twist that could appear in a generic LLM story. Replace each with a
specific, culturally grounded alternative. Keep a changelog.
```

---

## 8. Why this matters for the games

The same principles apply beyond names:

- **Undercity**: name the institutions and districts from their functions and history, not “Ash” + “fall.” The clockmaker should have a name from a specific district culture.
- **Lantern Road**: the Grey March already has a naming field; extend it by class/region, not by adding more -a fantasy names. Reserve Mira.
- **WILDY**: seven names should feel like seven different people, not seven variants of the same soft fantasy pool. Rename Mira if it is a different universe.
- **Astra**: an AI open world will default to Elias/Elara/Mara and correlated pairs; give it a **name registry** and structured NPC facts, not just a prompt.
- **Neathbound/Undercity**: place names should encode the city’s institutions (Bureau of Hours, Registry of Names) rather than generic fantasy compounds.
- **KKC**: canon names are fixed; original NPCs need a phonology that fits the world’s cultures and does not collide with canon.

---

## 9. Limits

- The published name studies focus on **English short fiction**, not games or dialogue; the mechanisms transfer, but the rates will differ.
- The “Mira” diagnosis is partly inferential: it is not one of the 11 core tokens in the Elias study. The local audit is the stronger evidence for *your* corpus.
- Static counts are not meaning; a name can repeat deliberately (shared universe). Classify before renaming.
- Cultural naming needs care: real-world names carry history and ownership. “Diverse” is not a one-of-each checklist.
- The audit tool is heuristic; it counts known names, not every character. Use it to find drift, not to declare a canon.
- No playtest was run to see whether players actually notice or care; the recommendations are design hypotheses with strong research support.

---

## 10. The one-paragraph version

Models concentrate on a small pool of familiar names and correlated ensembles because of training and preference tuning; your repos then reinforce a local pool. Banlists only move the problem. Generate many candidates with external entropy and explicit phonologies, score them against a project registry and a corpus-level collision metric, let humans approve a small canon, and reserve names per universe. The goal is not “weird names.” It is **names that could only belong to this place, this culture, and this person** — and a process that notices when the model is about to give you Mira again.

---

## Sources

- Hamilton, S. & Mimno, D. (2026). *Elias in the Lighthouse, Again? Diagnosing Low Diversity in LLM Stories.* [arXiv:2605.26492](https://arxiv.org/abs/2605.26492)
- Mozo Quesada, A., Gálvez Rojas, S. & López Valverde, F. (2026). *Character-Name Concentration in LLM Fiction: Measuring Displacement and Mitigating Repetition.* [arXiv:2611.01284](https://arxiv.org/abs/2611.01284)
- Brzozowski, M. & Chung, N. C. (2026). *The Ghost Couple: Correlated LLM Name Priors and Their Haunting of the Web and Academic Publishing.* [arXiv:2606.02184](https://arxiv.org/abs/2606.02184)
- *Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond).* NeurIPS 2025. [paper](https://papers.nips.cc/paper_files/paper/2025/file/754d5a526a5ee5a47220664a0eb92751-Paper-Datasets_and_Benchmarks_Track.pdf)
- Fu, T. et al. (2026). *Beyond the Hivemind: Escaping LLM Homogeneity via Meta-Persona Anchoring and Sequential Temperature Scaling.* [arXiv:2608.02618](https://arxiv.org/abs/2608.02618)
- Doshi, A. R. & Hauser, O. P. (2024). *Generative AI enhances individual creativity but reduces the collective diversity of novel content.* Science Advances 10(28), eadn5290. [doi](https://doi.org/10.1126/sciadv.adn5290)
- Shumailov, I. et al. (2024). *AI models collapse when trained on recursively generated data.* Nature. [doi](https://doi.org/10.1038/s41586-024-07566-y)
- Jwynia, *Character Naming: Breaking the Chen Proliferation.* [skill](https://github.com/jwynia/agent-skills/blob/main/skills/creative/fiction/character/character-naming/SKILL.md) (practical checklist; MIT)
- Gizmodo, *Why Do Chatbots Keep Telling Stories About Someone Named ‘Elias Thorne’?* [article](https://gizmodo.com/why-do-chatbots-keep-telling-stories-about-someone-named-elias-thorne-2000770629) (journalistic summary of Hamilton & Mimno)
