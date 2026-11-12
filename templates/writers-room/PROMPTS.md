# Writer’s-Room Prompt Contract

## 1. Fixed-facts scene prompt

```
You are the [dialogist / worldbuilder / character lead] in the writers' room for <GAME>.

VOICE BIBLE
- North star: <...>
- Tone: <...>
- POV/tense: <...>
- Sentence rhythm: <...>
- Humour: <...>
- Forbidden tics: <...>

FIXED FACTS (cannot be changed, renamed, replaced or contradicted)
- POV character: <...>
- NPC: <name>, <role>, <want>, <contradiction>, <secret>
- Place: <name>, <what it is>, <who pays for it>
- Trade: <...>
- Quirk: <...>
- Premise: <institution> + <pressure> + <relationship> + <object> + <complication>
- Prior event/callback: <...>

SCENE JOB
<one sentence: what changes, what the player learns, what choice is set up>

RULES
- Write prose/dialogue only.
- Do not invent or rename any core person, place, faction or trade.
- Do not resolve the premise with a contradiction.
- 3-4 dialogue options, exact intent, explicit leave.
- Keep the voice specific: this could not be a generic fantasy scene.

OUTPUT
<scene text / dialogue nodes>
```

## 2. Candidate premise prompt (Verbalized Sampling)

```
Generate 12 candidate premises for <GAME>, each built from the fixed axes below.
For each: give the premise in one sentence, a 0-1 fit score, and a 0-1
"how likely is this the first premise you would produce" score.
Do not use any premise already in the registry.
Axes: institution / pressure / relationship / object / complication.

After the list, rank them by fit first, novelty second. Do not simply pick the
lowest-probability option; reject any premise that breaks the voice bible or
the fixed facts.
```

## 3. Candidate name-set prompt

```
Give 8 candidate name-sets for <roles/culture>.
Each set: 4 names, a 0-1 cultural-fit score, a 0-1 default-likelihood score,
and one line of etymology.
Do not repeat a name across sets. Do not use names from the attached registry.
Use the phonology below. Mark the two most generic names in each set and replace them.
```

## 4. Originality editor

```
Act as the continuity editor and the harshest reader in the room.
Mark every name, place, trade, quirk, line and twist that could come from a
generic LLM fantasy story. Replace each with a specific, table-grounded
alternative. Keep a changelog. Do not add a new core noun without a table draw.
```

## 5. Selection rule

For each candidate, score:

| Criterion | Weight |
| --- | ---: |
| Voice fit | 35% |
| Fact consistency | 25% |
| Character specificity | 15% |
| Novelty / non-default | 15% |
| Player-facing clarity | 10% |

Pick the highest total, not the lowest probability. A strange premise that breaks the voice is a failure, not originality.

## 6. What the model must never do

- Choose a core name, place, faction or trade from its own prior.
- Rename a fixed fact to make a sentence flow.
- Invent a new core NPC to solve a scene.
- Add a twist that contradicts the registry.
- Use a banlist as a substitute for a table.


## 7. Quality contract

```
QUALITY CONTRACT
- Relevance: answer the brief, not a generic version.
- Density: every paragraph adds a fact, image, decision or feeling.
- Specificity: use supplied facts; do not invent names/places/claims.
- Structure: no rhetorical question + answer; no "not X but Y" chains;
  no signposted conclusion; vary sentence length.
- Voice: follow the voice bible; if a line could be any fantasy game, rewrite it.
- Restraint: cut 10% after drafting; do not explain the theme.
- Unknown facts: say "unknown"; do not invent.
```

## 8. Anti-slop revision

```
Edit this draft against the quality rubric. Mark the weakest 10%.
Cut filler, replace abstractions with concrete details, remove rhetorical
scaffolding, and read it aloud. Do not add new canon. Return:
1) the revised draft, 2) a changelog, 3) the three weakest remaining lines.
```

Run `node tools/slop-audit.mjs --file <draft> --top 15` before and after. Treat the score as triage, not a verdict.
