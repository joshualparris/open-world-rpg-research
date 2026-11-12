# Naming & Originality Playbook

A practical companion to [AI-NAMING-AND-ORIGINALITY.md](AI-NAMING-AND-ORIGINALITY.md). Use this when generating characters, places, factions or story premises with an LLM.

---

## The 30-minute name sprint

1. **Define the culture** (5 min). One page: sounds, stress, morphology, registers, taboos, history.
2. **Define the person** (5 min). Want, obstacle, contradiction, secret, role, class, age, origin.
3. **Generate 40–60 candidates** (5 min). Use scripts/lists and 3 LLM personas, not one answer.
4. **Score** (8 min). Fit, pronounceability, collision, memorability, role independence.
5. **Human pick** (5 min). Choose 1 core name + 1 variant/nickname; reject the model's first favorite.
6. **Record** (2 min). Registry, etymology, universe, approver, provenance.

If you only have one minute: **remove the model's first three names and the most familiar option; pick the fourth and check it for collisions.**

---

## Name culture worksheet

For each culture, fill this in before generating:

| Field | Your answer |
| --- | --- |
| Sound inventory | e.g. CV, CVC, no initial clusters |
| Stress | initial / penultimate / variable |
| Final sounds | -a, -e, -i / -k, -n, -th |
| Forbidden sounds | e.g. “th” is sacred, not spoken |
| Morphology | patronymic / clan / occupational / toponymic |
| Registers | ritual, common, nickname, insult, exonym |
| History | old form → modern form |
| Place grammar | “ford of X”, “X’s hill”, “new X” |
| Loanwords | which neighbouring culture, how adapted |
| Naming taboos | dead names, true names, slave names |

Then create **10 templates** and only afterwards names.

---

## Prompt pack

### 1. Surface the default

```
Before you generate, list the 15 character names, 10 place names, 8 professions
and 5 twists you would normally produce for this brief. Label them "defaults".
Do not use any of those defaults in the actual answer.
```

### 2. Phonology-first character names

```
Generate 10 phonotactic templates and 40 names for a culture with:
- CV and CVC syllables, initial stress, final vowels a/e/i;
- no initial consonant clusters;
- "th" is taboo in personal names;
- occupational suffixes -ward, -smith, -kell;
- two social registers: ritual and common.
Include 5 loanwords from a neighbouring culture and explain the adaptation.
Do not use any name in the attached registry. Mark the 10 most generic and replace them.
```

### 3. Candidate sets with scoring

```
Give 8 candidate name-sets for these roles: [roles].
Each set: 4 names, a 0-1 cultural fit score, a 0-1 "how likely is this the first
set you would produce" score, and one line of etymology.
Do not repeat a name across sets. Prefer names a reader can pronounce after one hearing.
```

### 4. Person before role

```
For each NPC: want, obstacle, contradiction, secret, nickname, how they
mispronounce a rival's name, and one thing they are wrong about.
Then name them after the person, not the role. Avoid role-name pairs
(Mira the healer, Kael the rogue, Rowan the mayor).
```

### 5. Place names with layers

```
Name 12 places from geography, economy and history:
a ford, a failed mill, a salt road, a border survey error, a saint's well,
a dispossessed village, a ferry crossing, a tannery, a plague pit, a new suburb,
a flooded mine, a market square.
For each: local name, official name, outsider name, and one lie locals tell
about how it got the name.
No Ash/Thorn/Shadow/Ember + wood/haven/reach/fall compounds.
```

### 6. Story constraint cards

```
Generate 12 premises, each anchored in a specific institution or economy:
water court, funeral debt, ferry schedule, guild audit, border survey,
salt tax, rent strike, inheritance dispute, plague quarantine, ship registry.
No chosen one, prophecy, ancient evil, amnesia, hidden heir, or "the real
monster was grief".
Then pick the 3 least similar premises and explain why.
```

### 7. Multiple naming historians

```
Generate names as six different local historians:
a tax clerk, a ferryman, a child, a priest, a smuggler, a foreign cartographer.
Each names the same five places differently; explain the layers and which
version is official.
```

### 8. Originality editor

```
Act as an editor who hates generic fantasy. Mark every name, place, profession,
title and twist that could appear in a generic LLM story. Replace each with a
specific, culturally grounded alternative. Keep a changelog of what changed and why.
```

### 9. Story from an object

```
Start with one concrete object (a debt ledger, a ferry token, a broken bell,
a survey stake) and build a situation around who needs it, who is hurt by it,
and what institution profits from it. No prophecy; no chosen one.
```

### 10. Anti-ensemble check

```
Review this cast as a set, not individually. Which names share a sound, ending,
origin, or role? Which pairs feel like an LLM default? Replace the two most
correlated names, keeping the cast pronounceable and culturally coherent.
```

---

## Selection rubric

Score 1–5:

| Criterion | Question |
| --- | --- |
| Cultural fit | Does it follow the culture’s phonology and naming convention? |
| Person fit | Does it fit age, class, region, profession and personality? |
| Pronounceability | Can a player say it after one hearing? |
| Memorability | Can they recall it after a session? |
| Distinctiveness | Is it distinguishable from the rest of the cast? |
| Role independence | Does it avoid a stock role-name pairing? |
| Collision | Is it already used in this universe or another? |
| Provenance | Can you explain where it came from? |

**Reject** if it is the model's first suggestion, a top-10 default, or a name+role clone from another project.

---

## Place-name grammar

Build places from:

1. **Landscape**: ford, escarpment, spring, harbour, pass, marsh, crag, heath.
2. **Economy**: mill, saltworks, tannery, market, ferry, quarry, brickworks, rail.
3. **History**: battle, plague, saint, treaty, survey error, dispossession, fire.
4. **People**: founder, landlord, rebel, saint, family, nickname.
5. **Layers**: local name / official name / outsider name / nickname / pronunciation.

Examples of the *method* (not a canon):

- “Gallowsfoot” — the ford where executions were held.
- “The Dew Line” — a border set by a surveyor’s error at dawn.
- “Ninebell” — a village that rang nine bells for a fire that never came.
- “Ostler’s Rest” — a coaching inn named after a horse, not a person.
- “The Sink” — a flooded mine that swallowed the market square.

Avoid: **Ashwood, Thornfield, Silverwood, Duskmere, Emberfall, Raven’s Reach** unless the name has a specific local cause and you can say what it means to the people who live there.

---

## Story constraints

Before writing, pick **three** constraints:

- a specific institution (court, guild, ferry, archive, tax office, temple);
- a specific economic pressure (rent, salt, harvest, debt, monopoly);
- a specific document or object (ledger, map, token, bell, key, deed);
- a specific point of view (clerk, child, outsider, rival, ghost, animal);
- a specific place with a history (a ford, a mill, a shrine);
- a specific failure mode (the plan works but costs the wrong person);
- a specific relationship (siblings, ex-lovers, mentor/student, rivals).

And **ban** the defaults for the first draft: prophecy, chosen one, ancient evil, amnesia, hidden heir, “the real monster was grief,” “the town with a secret.”

---

## Corpus metrics

Run:

```bash
node tools/name-audit.mjs --root /path/to/parent-of-repos
node tools/name-audit.mjs --root /path/to/game --json > name-audit.json
```

Track:

| Metric | Healthy direction |
| --- | --- |
| Collision probability | lower is better; target < 1% |
| Top-10 name share | target < 20% |
| Within-story duplicates | 0 |
| Cross-project core-name collisions | 0 unless shared canon |
| Role-name correlation | no repeated pairs across universes |
| Real-name attestation | appropriate to setting, not erased |
| Human blind distinctiveness | higher than baseline |
| Semantic similarity of premises | lower than baseline |

A useful A/B: generate 20 names with your normal prompt, then 20 with the phonology + candidate-set + registry approach. Blind-rate both for distinctiveness, memorability, fit and “could only be this world.”

---

## Portfolio rules

1. **One core name, one universe** unless the registry says “shared canon.”
2. **Reserve name+role pairs**, not just names.
3. **No fourth Mira.** Pick the canonical Mira; rename or link the others.
4. **Document shared settings** (Grey March: Rowan, Tessa, Elira).
5. **Watchlist, not blanket ban**: Elara, Elias, Mara, Aria, Seraphina.
6. **No static banlist alone**; track displacement and real-name representation.
7. **AI proposes; humans canonize.**
8. **Log provenance** for every core name: human, model, seed, approver.

See [data/name-commons.json](data/name-commons.json) for the current working registry.

---

## The 8-question final check

1. Could this name only belong to this culture/world?
2. Is it the model’s first, safest answer?
3. Does it repeat a name+role from another project?
4. Can a player pronounce and remember it?
5. Does it collide with the current cast?
6. Does it encode a place’s economy/history, or just “fantasy”?
7. Would a generic LLM write this premise? If yes, what specific institution/pressure makes it different?
8. Can you explain where it came from without saying “the AI suggested it”?
