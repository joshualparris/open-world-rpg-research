# Why the AI keeps naming everyone Mira, and how to stop it

**Prepared 2026-11-12 · Evidence review plus measurements on your own repos · Tools in [`tools/originality/`](tools/originality/)**

You noticed that names like **Mira** keep coming back. This note covers why that happens, what researchers have already measured, the same pattern in places, professions and plots, and what actually works to get more original names, places and stories.

---

## 1. The short answer

1. **It is real and measured.** A 2026 Cornell study of 20,000 stories from four current models found that **11 words appear in 88.3% of them**, including the names **Elias, Mara and Elara**, the setting **lighthouse**, and professions like **clockmaker** and **librarian**. Mira is the same sound family (short, soft, two syllables, ends in -a), though I could not see the full list of 11, so I cannot say whether Mira itself is on it.
2. **It is mostly caused by training, not by chance.** The leading explanations: alignment training (RLHF and preference tuning) reduces output diversity, and human raters prefer *typical, familiar* text, so the model learns that the safe answer is the common one. A name is a low-stakes choice where the most typical option wins almost every time.
3. **Asking for "original" or turning up the temperature mostly does not fix it.** What works is **taking the choice away from the model**: draw names, places and story seeds from outside the model (code, tables, random seeds), then give them to the model as fixed facts. Banlists, "give me 20 and sample", and some decoding tricks help as a second layer.

---

## 2. What your own repos show

Measured with [`name_audit.py`](tools/originality/name_audit.py) (capitalised whole-word match, `aria-label` and ordinary words excluded):

| Where | Result |
| --- | --- |
| **Across ~120 clones** | **"Mira" appears in about 20 separate repos**, in very different roles: a wandering NPC (Aetheria), a mercenary companion (an older RPG prototype), a bar contact (a chat-roleplay test), a mother (a D&D prototype), a tech operator (a sci-fi prototype), the greeted test NPC in AIDungeonMaster's smoke test, plus a Lantern Road companion. |
| **A hard-coded name list** in a D&D prototype | `["Elyra", "Thorne", "Kael", "Mira", "Rowan", "Nyx", "Alaric", "Vera"]`, which is close to a textbook sample of LLM fantasy names. |
| **JoshMemory (all games)** | 2,491 hits on 23 banlisted names. Mira 979 (72 files), Oren 672, Mara 290, Rowan 197, Wren 103. |
| **Lantern Road** | Mira 501 hits in 63 files; Oren 371 in 54 files. |
| **AIDungeonMaster** | Mira 41 (21 files), Rowan 24, Kaelen 16, Elara 8. |
| **Aetheria** | Elara 13, Theron 6, Mira 3, Aldric 3. |

**Places and objects** (repos where the word appears, excluding the mirror repo): *lantern* 26, *ledger* 25, *forgotten* 25, *Whispering* 21, *whispers* 19, *Hollow* 18, *echoes* 14, *ember* 13, *ozone* 9, *lighthouse* 8, *Misty* 8, *librarian* 6.

**Two honest caveats.**
- These counts overstate independence. Several repos are mirrors or share a lineage, and **once a name is in your own documents it gets copied forward** (a model that reads "Mira" in your prompt or lore will keep using her). Lantern Road's 501 mentions are partly that. So the 20 repos are evidence of a *tendency*, not 20 independent coin flips.
- "Lantern" and "ledger" are also themes you chose on purpose (Lantern Road, "The Missing Ledger"), so those two are not clean evidence.

---

## 3. What the research says

Evidence grade: **A** peer-reviewed or conference paper with data · **B** preprint or secondary report · **C** practitioner report or blog. I could not open some pages from this session (they are outside its allowed network), so several entries rely on search summaries; those are marked.

| Finding | Source | Grade |
| --- | --- | --- |
| **88.3% of 20,000 LLM stories contain one of 11 words** (names Elias, Mara, Elara; lighthouse in half of all stories; clockmaker, librarian), little difference between models. The tokens are **rare in books and pre-training data but present in preference data.** Authors' framing: these stories are "so safe". | Hamilton and Mimno, ["Elias in the Lighthouse, Again?"](https://arxiv.org/abs/2605.26492), EMNLP 2026; [Cornell news](https://news.cornell.edu/node/333804) | A |
| Press coverage names the **WildChat** dataset as a likely original source and cites "166 conversations"; I could not confirm that number in the paper. | [404 Media](https://www.404media.co/elias-thorne-chatbots-llms-chatgpt-lighthouse-keeper-story/), [AI Weekly](https://aiweekly.co/alerts/cornell-links-ais-elias-thorne-pattern-to-wildchat-data) | C (unverified detail) |
| **RLHF improves generalisation but reduces output diversity**, including across different inputs (more similar text regardless of prompt). | Kirk et al., [ICLR 2024](https://arxiv.org/abs/2310.06452) | A |
| Co-writing with the feedback-tuned model made essays **more alike**; the base model did not. The loss came from model-written text. | Padmakumar and He, [ICLR 2024](https://arxiv.org/abs/2309.05196) | A |
| AI story ideas made **individual** stories better rated but **stories collectively more similar** (293 writers). | Doshi and Hauser, [*Science Advances* 2024](https://arxiv.org/abs/2312.00506) | A |
| **"Artificial Hivemind":** across 70+ models, a single model repeats itself and **different models give strikingly similar answers**; reward models and LLM judges are poorly calibrated to idiosyncratic human taste. | Jiang et al., [NeurIPS 2025](https://arxiv.org/abs/2510.22954) | A |
| Preference data has a **typicality bias** (raters favour familiar text), a data-level cause of mode collapse. A training-free prompt, **Verbalized Sampling** (ask for several answers with probabilities), is reported to raise creative-writing diversity about 1.6-2.1x. | Zhang et al., [arXiv 2510.01171](https://arxiv.org/abs/2510.01171) | B (self-reported gains) |
| "Elara" appeared **85,513x more often** than in human text in one model's creative output; a ban-list sampler (**Antislop**) suppressed 8,000+ patterns while keeping quality; the authors advise building **your own** list. | [Antislop](https://arxiv.org/abs/2510.15061), [code](https://github.com/sam-paech/antislop-sampler) | B |
| Across 10 LLMs vs human stories, a "mean generic narrative" emerges, and **negative prompting and temperature scaling fail to fix it**. | ["Do LLMs Always Tell The Same Stories?"](https://arxiv.org/abs/2606.17350) | B (read via an aggregator summary) |
| LLM stories show lower **plot uniqueness** than human ones, with abrupt drops after surprise events. | "Echoes in AI" (Sui Generis score), via a search summary | B (secondary) |
| **Min-p sampling** keeps coherence at higher temperature, improving quality and diversity in the authors' tests. | [Min-p, ICLR 2025](https://arxiv.org/abs/2407.01082) | B |
| Practitioners report the same names across tools: Gemini giving **Elara/Lyra ~90%** of the time; AI Dungeon users getting **Marcus, Lyra, Elara**; a blog test of Claude repeating **Kira Voss, Kira Vance, Kael Voss** for a spaceship pilot. | [Gemini forum](https://discuss.ai.google.dev/t/gemini-cannot-come-up-with-unique-name-for-characters/94830), [AI names blog](https://www.seehuhn.de/blog/ai-names/) | C |

**What is not established.** Why *these specific names* won is a hypothesis: the mechanism (preference data favouring safe options) is supported, but the exact origin (for example WildChat or copyright-related filtering) is not. One report floated copyright filters pushing fiction toward out-of-copyright material; that is speculation, not a finding.

---

## 4. Why it happens (the working model)

1. **Pre-training** gives a broad distribution of names.
2. **Post-training sharpens it.** Preference tuning rewards the answers raters find "good", and raters pick the familiar and safe (typicality bias). Diversity falls (Kirk, Padmakumar, Zhang).
3. **Names are the perfect place for it to show.** A name is a one-word, low-stakes, no-wrong-answer decision. Nothing pushes the model off its single most probable choice, so it picks it nearly every time.
4. **The effect is shared across models**, probably through overlapping data and tuning practice (Hivemind). Different tools therefore converge on the same names. *(Why they overlap is a hypothesis.)*
5. **Short prompts give no signal**, so the model falls back to the mode. A longer prompt does not help unless it contains *specific, unusual constraints* (see below).
6. **In-context copying locks it in.** Once a name is in your lore, tests or examples, the model repeats it. This is the likely reason Mira is *so* frequent in your repos.

---

## 5. The same pattern beyond names

| Layer | Overused defaults (evidence) |
| --- | --- |
| **First names** | Elara, Elias, Mara, Lyra, Kael, Seraphina, Aria, Marcus (Cornell; Gemini and AI Dungeon reports; your repos) |
| **Surnames** | Voss, Vance, Thorne, Chen, Blackwood (blog tests; practitioner skill notes on "the Chen proliferation") |
| **Settings** | lighthouse (half of 20,000 stories), "Whispering Woods", "Misty ...", "... Hollow" (Cornell; your repos) |
| **Professions** | clockmaker, librarian, keeper-of-something (Cornell) |
| **Objects and motifs** | ledger, locket, amulet, lantern, echoes, whispers, ember, ozone, tapestry (your repos; Antislop-style frequency lists) |
| **Plot** | A "mean generic narrative"; low plot uniqueness; surprise events followed by a fall back to the stock arc (2026 and 2025 story studies) |
| **Prose** | "Slop" phrases that appear over 1,000x more than in human text (Antislop) |

For your games the plot layer matters most: a world full of different names that all run the same quest shape is still generic.

---

## 6. What does *not* work well

- **"Be original / creative / avoid clichés."** The model's idea of original is its own mode ("Elara" feels fantasy-original). The 2026 story study reports negative prompting did not fix homogeneity.
- **Temperature alone.** Higher temperature adds randomness but costs coherence, and does not target the specific collapsed choices. Min-p and similar samplers help, but only where you control decoding.
- **"Pick a random name."** Models are not random. One documented practitioner test (reported secondhand) asked for a random pick from a list; the model chose the same entry every time, even reordering the list to do it. **Randomness must come from code.**
- **Fixing it only in the prompt.** One instruction competes with the whole alignment training.

---

## 7. What works (ranked by evidence and effort)

### 1. Take the choice away from the model *(strongest, cheapest)*
Generate names, places, trades, quirks and story seeds **in code** from a seeded RNG, check them against a banlist and a per-world registry, then give them to the model as facts: "The innkeeper is **Tiakam Drayscar**, a net-mender who counts everything twice." Practitioners and game developers arrive at the same rule independently ("use random tables for name generation instead of having it run full LLM"). It also matches your own engine-owns-truth principle: **a name is state**, and state belongs to the engine ([MORE-FROM-YOUR-REPOS.md](MORE-FROM-YOUR-REPOS.md) N2).

→ [`namegen.py`](tools/originality/namegen.py): people, places, and whole NPC seeds.

### 2. Inject outside randomness into the *story*, not just the name
Draw a premise from tables: **situation × obstacle × relationship × constraint**, plus an unusual trade and a want. A related line of work ("Addressing LLM Diversity by Infusing Random Concepts", known to me only from a [review summary](https://www.themoonlight.io/review/addressing-llm-diversity-by-infusing-random-concepts)) finds that prepending a random word or sentence to the prompt reduces repetition. The point is to give the model *specific, unusual constraints* so the mode is not the only option.

### 3. Ask for breadth, then choose from the tail
Don't ask for one; ask for 10-20 with rough probabilities (**Verbalized Sampling**) and pick the lowest-probability usable one, or pick by code. Cheap and works through any chat API (gains are self-reported, so test it on your own prompts).

### 4. Keep a banlist and a "used so far" ledger
Include in the prompt: "Do not use these names" plus the registry of names already in this world. Treat the list as a *starting* list; Antislop's authors recommend building your own, which is what [`banlist.txt`](tools/originality/banlist.txt) and the audit do for you. Enforce it in validation: reject any NPC whose name collides with the registry or banlist, the same way RTD-009 rejects unknown state.

### 5. Use decoding tools where you control the model
Min-p, DRY-style repetition penalties and Antislop-style backtracking exist for local models. Hosted APIs usually expose only temperature and top-p, so for those lean on 1-4.

### 6. Validate after generation
Run [`name_audit.py`](tools/originality/name_audit.py) in CI with a threshold (`--max N`); reject and regenerate when output contains a banlisted default or too many near-duplicates of existing names.

### 7. Keep a human in the naming loop
Doshi and Hauser found AI ideas help *individual* writers but narrow the *collective* range. Use the model for scaffolding (descriptions, dialogue, structure) and let a person (or your tables) own the names and the premise. Rename after, not before.

### 8. Measure it
Over N generations, track: **distinct first names / N**, banlist hit rate, repeated n-grams, and embedding self-similarity. A simple target: generate 50 NPCs and expect near-50 distinct names with zero banlist hits (the included generator gives 2,000 distinct of 2,000 in a test).

---

## 8. A drop-in prompt pack

**System prompt addition (any game or DM prompt):**

```text
Names are facts supplied by the game, never your choice.
- Use only names from the NAMES list in the context. If you need a new one, ask for it; do not invent one.
- Never use these overused defaults unless they appear in the NAMES list: Elara, Elias, Mara, Mira, Lyra, Kael, Thorne, Voss, Seraphina, Aria, Eldoria.
- Places, trades, objects and quirks also come from the context. Do not default to lighthouses, clockmakers, librarians, ledgers, lockets or whispering/misty/hollow place names.
- If a scene needs something that is not in the context, make it specific and a little odd (a concrete job, an unglamorous want), not mythic.
```

**Per-NPC seed (filled in by code, then handed to the model):**

```text
NPC: {name}, {trade}. Quirk: {quirk}. Wants: {want}.
Lives in {place} ({place_kind}).
Write 3 lines of dialogue in this person's voice. Do not change the name, trade or place.
```

**Verbalized Sampling, when you must let the model propose:**

```text
Give 10 candidate {names/premises} for {context}, each with a probability (how likely you would
pick it by default). Include at least 5 you would normally rank below 0.1. Output a table only.
```
Then choose from the low-probability rows in code, not by asking the model to pick.

**Story seed (code draws one from each list):**

```text
Premise: {situation} while {obstacle}. The two people involved are {relationship}. Constraint: {constraint}.
Avoid the genre's stock opening. Start in the middle of an ordinary task.
```

---

## 9. What to do in your repos

1. **Stop letting the model choose NPC names.** In AIDungeonMaster's prompt and any NPC-generation call, pass names from an engine-owned registry (it already plans a canon log and persistent NPC records, so this is a small step).
2. **Replace hard-coded fantasy name arrays** (the D&D prototype's `["Elyra", "Thorne", "Kael", "Mira", ...]`) with `namegen.py` output or a curated list.
3. **Add the audit to CI:** `python tools/originality/name_audit.py . --max 0` on new content, or a threshold for old content.
4. **Decide about Mira and Oren in Lantern Road.** They are central (501 and 371 mentions across 63 and 54 files). You may reasonably treat them as chosen canon now. Renaming would be a large migration touching quest and dialogue text, and any stable actor keys, so I did **not** change them; the decision is yours. A cheaper rule: keep existing canon, and apply the registry to *new* characters only.
5. **Add stakes to places.** Use the generator's "place kind" (a tidal salt-works, a toll bridge) so a place has an economic reason to exist; that does more against generic worlds than a fresh name.
6. **Plot layer:** draw each quest's premise from tables (point 2 in section 7) before the model writes it. This is the only fix aimed at generic *stories* rather than names.

---

## 10. Limits of this note

- **Evidence is uneven.** The core Cornell result, the RLHF-diversity papers and the co-writing experiments are solid; Verbalized Sampling and Antislop gains are the authors' own and not independently replicated; several practitioner items are anecdotes.
- **Search-summary sources.** I could not open some pages from this session, so the "Do LLMs Always Tell The Same Stories?", "Echoes in AI", and practitioner entries rely on search summaries. Check them before citing.
- **Your counts are suggestive, not clean.** Lineage and copy-forward inflate them (section 2).
- **Mira is a perfectly good real name.** The issue is concentration, not the name. Treat the banlist as "avoid unless chosen on purpose".
- **The included generator is a starting point.** Its syllable names are varied but still sound "made up"; for more realistic worlds, replace the syllable styles with curated real-world name pools and keep the same registry logic.
- **No testing with players.** Whether a more varied cast is more *fun* is the open question from the main report; this note only shows how to make it more varied.

---

*See [README.md](README.md) for the overall research, [MORE-FROM-YOUR-REPOS.md](MORE-FROM-YOUR-REPOS.md) for the NPC and dialogue findings this builds on, and [`tools/originality/`](tools/originality/) for the generator, banlist and audit script.*
