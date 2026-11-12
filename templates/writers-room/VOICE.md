# <GAME> Writers’ Room

> One page. If it takes more than a page, it is a setting bible, not a voice guide.

## Showrunner

**Name / role:** <human owner>  
**North star:** <one sentence: what this game is really about>  
**Tone in three words:** <e.g. wry, haunted, humane>  
**What it is not:** <e.g. not grimdark, not whimsical, not a power fantasy>  
**Reference lenses (not imitations):** <e.g. Fallen London’s content discipline; Fable’s warmth; Skyrim’s lived-in towns>

## The room

| Role | Owns | Must ask |
| --- | --- | --- |
| **Showrunner** | Canon, tone, final call | “Does this feel like *us*?” |
| **Worldbuilder** | Geography, institutions, history, names, places | “Why does this place exist, and who pays for it?” |
| **Character lead** | Wants, contradictions, relationships, arcs | “What does this person want when the plot isn’t looking?” |
| **Dialogist** | Diction, rhythm, subtext, silence | “Would this character say it *this* way?” |
| **Continuity editor** | Registry, contradictions, CI, callbacks | “Where was this established, and does it still hold?” |
| **Guest voice** (per arc) | One deliberate outside perspective | “What would an outsider notice?” |

Keep the room small. Three to five voices is enough; a ten-person committee produces consensus prose.

## Voice rules

- **POV / tense:** <first / second / third; past / present>
- **Sentence rhythm:** <e.g. short declaratives; one long sentence per beat>
- **Dialogue ratio:** <e.g. 50% scene, 50% talk>
- **Humour:** <e.g. dry, never quippy; one joke per scene maximum>
- **Violence / horror:** <e.g. consequence over gore; the aftermath is the scene>
- **Exposition:** <e.g. never explain the world before a character needs it>
- **Swearing / register:** <e.g. plain, no pseudo-archaic “thee”>
- **Forbidden tics:** <e.g. “little did they know”, “a testament to”, “shimmering”>

## Naming cultures

For each culture:

| Field | Answer |
| --- | --- |
| Sound inventory | |
| Stress | |
| Final sounds | |
| Morphology | |
| Registers | |
| Taboos | |
| Place grammar | |
| Loanwords | |
| Historical layers | |

**Reserved names:** <link to registry>  
**Name+role pairs never to repeat:** <e.g. Mira the keeper, Rowan the mayor>

## Tables

- Names: `tables/names.<culture>.json`
- Places: `tables/places.<culture>.json`
- Trades: `tables/trades.json`
- Quirks: `tables/quirks.json`
- Premise axes: `tables/premise.json`
- Draw: `node tools/table-draw.mjs --seed <arc-id> --table names --count 3`

Tables are canon. The model receives the drawn values as fixed facts.

## Prompt contract

The model may write **prose, dialogue and description**. It may not:

- invent or rename a core character, place, faction or trade;
- change a fixed fact;
- add a new core NPC without a table draw and human approval;
- resolve a premise by contradicting the registry.

## Quality gate

See `QUALITY.md` for the nine-gate ladder, rubric and slop audit. A high slop score is a **triage flag**, not a verdict; a human editor decides.

## Evaluation

- Voice adherence: blind A/B against the previous prose.
- Name/place collisions: `tools/name-audit.mjs`.
- Contradictions: registry validator.
- Reader test: “Which game is this from?” — if they can’t tell, the voice is not distinct enough.
