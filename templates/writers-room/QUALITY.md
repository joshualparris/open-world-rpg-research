# Quality & Anti-Slop Gate

> Anti-slop is a quality system, not a word blacklist. Score the profile; don’t ban single words.

## The quality ladder

| Gate | Owner | Check | Fail action |
| --- | --- | --- | --- |
| 0. Brief | Showrunner | Audience, purpose, voice, must-include, must-avoid, sources, length | Rewrite brief |
| 1. Facts | Worldbuilder | Names/places/claims come from registry, table or source | Cut/replace |
| 2. Draft | Writer/model | Fixed facts + voice bible; 2–3 versions if uncertain | Redraft |
| 3. Slop profile | Editor | `slop-audit` + human read for relevance, density, repetition, templatedness, tone | Edit |
| 4. Fact/canon | Continuity | Every proper noun/number/claim checked; no invented specifics | Cut/cite |
| 5. Structure | Dialogist/editor | Starts in situation; one beat per paragraph; cut 10%; no rhetorical scaffolding | Restructure |
| 6. Voice | Showrunner | Read aloud; blind identify the game; name-covered character test | Rewrite voice |
| 7. Reader test | 3–5 readers | What happened? What did you learn? What next? What felt generic? | Revise |
| 8. Sign-off | Showrunner | Human approval; provenance recorded | Hold |
| 9. Post-audit | Continuity | Monthly sample; track patterns and displacement | Tune |

## Rubric (1–5)

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Relevance | Off-brief | Mostly on brief | Every beat serves |
| Density | Padding | Some substance | Every paragraph earns its place |
| Factuality/canon | Contradicts/invents | Mostly consistent | Fully sourced/consistent |
| Voice | Generic | Fits | Only this game |
| Structure | Templated/incoherent | Works but familiar | Deliberate, clear, surprising |
| Specificity | Abstractions | Some concrete detail | Concrete, situated |
| Restraint | Overwritten | Occasional bloat | Precise, confident cuts |
| Reader effect | Forgettable | Competent | Memorable, pulls forward |
| Gameplay value | No choice | Functional | Clear choice, real cost, callback |

**Pass:** average ≥ 3.5, no 1 in factuality/canon/voice. **Publish:** human sign-off.

## Slop audit

```bash
node tools/slop-audit.mjs --file scene.md --top 15
node tools/slop-audit.mjs --root content/ --json
node tools/slop-audit.mjs --root content/ --fail-over 55
```

- Score is a **triage signal**, not a verdict.
- A high score goes to a human “suspicious queue.”
- Never auto-reject or auto-publish on score alone.
- Track false positives; tune patterns per project/genre.

## Prompt contract (append to every generation)

```
QUALITY CONTRACT
- Relevance: answer the brief, not a generic version.
- Density: every paragraph adds a fact, image, decision or feeling.
- Specificity: use supplied facts; do not invent names/places/claims.
- Structure: no rhetorical question + answer, no "not X but Y" chains,
  no signposted conclusion; vary sentence length.
- Voice: follow the voice bible; if a line could be any fantasy game, rewrite it.
- Restraint: cut 10% after drafting; do not explain the theme.
- Unknown facts: say "unknown"; do not invent.
```

## Revision prompt

```
Edit this draft against the quality rubric. Mark the weakest 10%.
Cut filler, replace abstractions with concrete details, remove rhetorical
scaffolding, and read it aloud. Do not add new canon. Return:
1) the revised draft, 2) a changelog, 3) the three weakest remaining lines.
```
