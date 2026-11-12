# Anti-Slop & Quality

**What “AI slop” actually is, what published research and working editors do about it, and how to wire it into the writers’ room.**

Prepared 2026-11-12 · Research note + operating model. Not a controlled test of your content.

Companion files: [WRITERS-ROOM.md](WRITERS-ROOM.md) · [AI-NAMING-AND-ORIGINALITY.md](AI-NAMING-AND-ORIGINALITY.md) · [templates/writers-room/QUALITY.md](templates/writers-room/QUALITY.md) · [tools/slop-audit.mjs](tools/slop-audit.mjs) · [data/slop-patterns.json](data/slop-patterns.json)

---

## The short answer

I had done **some** anti-slop research, mostly around names and the anti-slop sampler. That was not enough. The deeper research changes the model:

> **Anti-slop is not a word blacklist. It is a quality system.**
>
> The model is a draft engine. Quality comes from **brief, facts, voice, candidate selection, editing, fact-checking, reader testing and human sign-off** — not from telling the model to “avoid clichés.”

The best evidence-backed definition is multidimensional: slop is low **information utility**, low **information quality**, and/or poor **style quality** — not just the presence of “delve” or “tapestry.” Human-written text can be sloppy; AI text is not automatically slop. The label is about quality, not authorship ([Shaib et al., *Measuring AI “Slop” in Text*](https://arxiv.org/abs/2509.19163)).

The practical implication for the writers’ room:

- **Don’t** rely on a static banlist, an “anti-slop” prompt, a detector, or a single LLM judge.
- **Do** use a **quality ladder**: brief → facts → draft → slop profile → fact check → structure → voice → reader → human sign-off.
- **Do** use tools like the [Antislop Sampler / FTPO](https://arxiv.org/abs/2510.15061) only where you control the model; use **candidate generation + editorial selection** everywhere else.
- **Do** keep a human editor in the loop, exactly as a serious fiction magazine does: automated triage, human review, no algorithm final ([Neil Clarke, Clarkesworld](https://neil-clarke.com/how-ai-submissions-have-changed-our-submissions-process/)).

---

## 1. What “slop” actually is

The most rigorous public taxonomy comes from Shaib, Chakrabarty, Garcia-Olano and Wallace. They interviewed 19 experts across writing, journalism, linguistics, NLP and philosophy, then annotated 150 news articles and 100 QA passages at span level ([arXiv:2509.19163](https://arxiv.org/abs/2509.19163)).

Their taxonomy has three themes:

| Theme | Dimensions | What it catches |
| --- | --- | --- |
| **Information utility** | density, relevance | Padding, repetition, not answering the brief |
| **Information quality** | factuality, bias | Hallucination, false claims, misleading framing |
| **Style quality** | repetition, templatedness, coherence, fluency, verbosity, word complexity, tone | Formulaic structure, purple prose, incoherence, overwriting |

Two findings matter enormously for our operating model:

1. **Binary “slop” judgments are subjective.** Expert agreement on “is this slop?” was poor; agreement on *which spans* were problematic was moderate to high. Slop is better treated as a **profile** than a verdict.
2. **The strongest predictors were relevance, density and tone**, plus factual errors — not a single magic word. A text can avoid every cliché and still be slop because it is irrelevant, empty, inaccurate or tonally wrong.

The paper also found that **capable reasoning LLMs fail to reliably extract and identify slop**. Fully automated, scalable slop measurement remains an open problem. That is why CI should **flag**, not judge.

### A working definition for games

> Slop is text that costs the reader attention without returning enough **relevance, specificity, truth, voice or emotional/gameplay value**.

That definition lets us evaluate dialogue, quest text, item descriptions, UI copy and marketing — not just prose.

---

## 2. What the research and working editors actually do

### 2.1 The Antislop framework: suppress patterns at the model, not the prompt

Paech, Roush, Goldfeder and Shwartz-Ziv built **Antislop**: a detector, an inference-time sampler, and a fine-tuning method (FTPO) ([arXiv:2510.15061](https://arxiv.org/abs/2510.15061)).

Key numbers:

- Some slop patterns appear **over 1,000× more frequently** in LLM output than human text.
- The Antislop Sampler suppresses **8,000+ patterns** while maintaining quality.
- Token banning becomes unusable at just **2,000** patterns.
- **FTPO achieves ~90% slop reduction** while maintaining or improving GSM8K, MMLU and creative-writing performance.
- **DPO** achieved weaker suppression and significantly degraded writing quality and lexical diversity.
- The sampler’s cost is real: Thoughtworks reports **69–96% throughput degradation** from backtracking at 1k–8k patterns ([summary](https://research.thoughtworks.com/library/anti-slopping-an-innovation-for-rectifying-llm-writing-cliches)).

**What this means:** if you run an open model and control the logits, this is the strongest published anti-slop lever. If you use an API, you usually cannot use it. Do not pretend a prompt is the same thing.

### 2.2 The trope lists: useful, but not a theory

The `tropes.fyi` / `deslopify` list is a good field guide to the surface tells ([list](https://github.com/danicat/skills/blob/main/writing/deslopify/references/tropes.md)):

- **Lexical:** delve, tapestry, testament, landscape, navigate, leverage, robust, seamless, meticulous, intricate, pivotal, vibrant, bustling, nestled, breathtaking, palpable, cacophony, symphony, shimmer.
- **Structural:** “It’s not X — it’s Y”; “Not X. Not Y. Just Z.”; self-posed rhetorical questions; anaphora; tricolon abuse; “It’s worth noting”; superficial “-ing” analysis; false ranges; gerund fragment litany.
- **Paragraph:** short punchy fragments; “listicle in a trench coat.”
- **Tone:** “Here’s the kicker”; “Think of it as…”; “Imagine a world where…”; false vulnerability; “the truth is simple”; stakes inflation; vague attributions; invented concept labels.
- **Formatting:** em-dash addiction; bold-first bullets; unicode decoration.
- **Composition:** fractal summaries; dead metaphor; historical analogy stacking; one-point dilution; content duplication; signposted conclusion; “Despite its challenges…”.

This list is useful **as a diagnostic vocabulary**, not as law. One em dash is not a crime. The pattern is **clusters and frequency**, not a single instance. The list itself says: “any of these patterns used once might be fine.”

### 2.3 Clarkesworld: automated triage, human judgment

Neil Clarke’s account of the AI-submission flood is the best practical case study ([Clarkesworld](https://neil-clarke.com/how-ai-submissions-have-changed-our-submissions-process/)):

- After ChatGPT, the **signal-to-noise ratio** collapsed; human-written work risked becoming a minority.
- They added an **in-house automated check**, then a separate suspicious queue.
- **A human reviews every suspicious submission.** Slush readers do not see that queue.
- Bans are issued only when Clarke is certain; at 99% certainty he flags rather than bans.
- He accepts that false positives happen and personally checks them.
- The automated step is a **pressure valve**, not a judge.

**Lesson:** automate triage; reserve judgment for a human. This is exactly the model for our CI: `slop-audit` flags, an editor decides.

### 2.4 Self-Refine: revision helps, but it is not a substitute for taste

Self-Refine has the same model generate an initial output, critique it, and revise it. Across seven tasks, outputs were preferred over one-step generation by about **20% absolute** on average ([NeurIPS 2023](https://papers.nips.cc/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html)).

Use it as a **revision pass**:

1. Draft.
2. Score against the rubric.
3. Mark the weakest 10%.
4. Revise only those parts.
5. Re-score; human reads.

Do not let the model “self-approve.” Self-critique can be shallow, sycophantic or blind to its own patterns.

### 2.5 The reward-model trap: models prefer slop

A crucial finding summarized in the slop paper: reward models over-weight **five superficial cues** — **length, structure, jargon, sycophancy and vagueness** ([Shaib et al.](https://arxiv.org/abs/2509.19163), citing Bharadwaj et al. 2026).

That is a devastating insight for “best-of-N with an AI judge.” If you optimize for a model’s preference, you may select **longer, more structured, more jargon-heavy, more flattering, vaguer** text — the exact signature of slop.

And LLM judges have their own biases: position bias is measurable and not random across 15 judges, 22 tasks and 150,000+ evaluations ([Shi et al., IJCNLP-AACL 2025](https://aclanthology.org/2025.ijcnlp-long.18/)).

**Rule:** use model judges for **triage and comparison**, never as the final quality gate. Randomize order, use multiple judges, anchor with a rubric, and keep a human.

### 2.6 AI-text detectors are not quality detectors

Detection is a different task from quality. Detectors produce false positives and false negatives; human-written text can be labelled AI, and AI text can pass. Shaib et al. explicitly separate slop from AI-text detection.

**Rule:** never ban or accuse based on a detector. Use process evidence (provenance, drafts, editorial history), not a classifier.

---

## 3. Why LLMs produce slop

Five engines:

1. **Typicality bias in preference data.** Annotators prefer familiar text, so alignment compresses the distribution toward the safe and expected ([Verbalized Sampling](https://arxiv.org/abs/2510.01171)).
2. **Reward models reward the wrong things.** Length, structure, jargon, sycophancy and vagueness are easy cues; specificity and truth are harder ([Shaib et al.](https://arxiv.org/abs/2509.19163)).
3. **Templates are efficient.** The model has learned that “intro → three points → conclusion,” “not X but Y,” and “here’s the kicker” are high-probability shapes. They are cheap to generate and often read as “complete.”
4. **Low information density is safe.** Vague claims are harder to falsify than specific ones. “The city was vibrant” cannot be wrong; “the salt tax rose by a copper on the feast of St. Orra” can.
5. **No editorial pressure.** A first draft is optimized for plausibility, not for the reader’s time. Without a brief, a fact source, a voice and an editor, the model defaults to the average of its training.

The fix is therefore **structural**, not lexical.

---

## 4. What does not work

| Approach | Why it fails |
| --- | --- |
| **Static word blacklist** | Displaces patterns; damages legitimate prose; can halve attested real-name representation; “delve” can be the right word. |
| **“Avoid clichés / be original” prompt** | Too vague; no external reference for *your* definition of slop. |
| **One-shot generation** | No candidates, no comparison, no editorial pass. |
| **Higher temperature** | Changes surface, not the underlying template or relevance. |
| **AI-text detector as gate** | Different task; false positives; not a quality measure. |
| **Single LLM judge** | Position bias, verbosity bias, sycophancy; reward models prefer slop-like cues. |
| **“More detail”** | Often produces padding, not density. |
| **DPO on style** | The Antislop paper found DPO degraded writing quality and lexical diversity despite weaker suppression. |
| **Banning a phrase in the prompt** | Can backfire; the model may prioritise the forbidden concept; prompt lists are not enforcement. |

The common mistake is treating slop as a **lexical** problem. It is usually a **relevance, density, truth, structure and voice** problem wearing a lexical costume.

---

## 5. What works: the quality ladder

Adopt a nine-gate ladder for every substantial piece of content.

### Gate 0 — Brief

Before generation:

- **Audience:** who is reading/playing?
- **Purpose:** what should change in the reader/player?
- **Voice:** which room/voice bible?
- **Must include:** 3–7 facts, images or beats.
- **Must avoid:** project-specific tics, tropes, names, claims.
- **Sources:** registry, canon, interviews, primary texts.
- **Length:** a target, not a minimum.
- **Success test:** what would make you reject this?

### Gate 1 — Facts

- Every specific claim/name/place comes from the registry, a table draw, or a cited source.
- Unknowns are marked unknown; the model may not invent.
- Numbers, dates, titles and relationships are checked.

### Gate 2 — Draft

- Fixed facts in, prose out.
- The model may not rename canon or add core nouns.
- Draft **2–3 versions** (plain, lyrical, comic) if voice is uncertain; pick, don’t blend.

### Gate 3 — Slop profile

Run the heuristic audit and read the result:

```bash
node tools/slop-audit.mjs --file scene.md --top 15
node tools/slop-audit.mjs --root content/ --json
```

Then a human reads for:

- relevance to the brief;
- information density (what did I learn?);
- factual/canon errors;
- repetition and templatedness;
- tone/voice fit;
- verbosity and word complexity;
- coherence.

### Gate 4 — Fact check

- Source/registry check for every proper noun, number, title and claim.
- "Who says this? Where was it established? Does it still hold?"
- Cut or cite vague attributions (“experts agree”, “studies show”).

### Gate 5 — Structure

- Does the opening start **in the situation**, not in a definition?
- Is there one new idea/feeling/decision per beat?
- Cut 10% — then cut the first paragraph and last paragraph if they are throat-clearing/summary.
- Vary sentence and paragraph length deliberately.
- Remove rhetorical questions, tricolon clusters, “not X but Y,” and signposted conclusions.

### Gate 6 — Voice

- Read it aloud. Does it sound like the showrunner, or like a generic assistant?
- Blind test: can a reader identify the game from 200 words?
- Does each character sound like themselves with the name covered?
- Are the forbidden tics absent (or used deliberately once)?

### Gate 7 — Reader/player test

Ask 3–5 target readers/players:

1. What happened?
2. What did you learn?
3. What do you want to do next?
4. Which line felt generic?
5. Would you talk to this character again?

### Gate 8 — Sign-off and provenance

- Human editor/showrunner approves.
- Record model, prompt version, table seed, sources, edits.
- No AI-only publish.

### Gate 9 — Post-publish audit

- Sample published content monthly with the slop profile and name audit.
- Track top patterns and displaced patterns.
- Feed the findings back into the voice bible and tables.

---

## 6. Game-specific slop taxonomy

Use this to brief editors; do not turn it into a blanket ban.

| Layer | Common slop | Better question |
| --- | --- | --- |
| **Lexical** | delve, tapestry, testament, realm, palpable, shimmer, “ever-evolving landscape” | What is the concrete thing? |
| **Structural** | “not X but Y”; tricolon chains; rhetorical question + answer; em-dash pivots; signposted conclusion | What is the actual argument/scene? |
| **Narrative** | chosen one, prophecy, ancient evil, amnesia, hidden heir, “the real monster was grief,” twist that resets stakes | Whose want drives this, and what does it cost? |
| **Dialogue** | “You’re not from here”; “the old stories say”; “you have your mother’s eyes”; everyone quippy; exposition dump | What would this person say *now*, given what they want? |
| **Worldbuilding** | Ash/Thorn/Shadow + wood/haven/reach; faction monoculture; lore dump before need | Who pays for this place, and what do they call it? |
| **Quest text** | “collect 10 bear asses”; “the real treasure was the friends we made”; “embark on an epic journey” | What is the concrete task, complication and consequence? |
| **UI/marketing** | “unlock,” “elevate,” “seamless,” “revolutionary,” “the possibilities are endless” | What does it do, for whom, at what cost? |
| **Epistemic** | “experts agree,” “studies show,” “it is widely believed,” invented concept labels | Name the source or cut the claim. |

One use is fine. The signal is **clusters, frequency and low information density**.

---

## 7. The quality rubric

Score 1–5. A 1 in factuality, canon or voice is a **hard fail** regardless of average.

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| **Relevance** | Does not answer the brief | Mostly on brief | Every beat serves the brief |
| **Density** | Padding; says little | Some substance | Every paragraph earns its place |
| **Factuality/canon** | Contradicts or invents | Mostly consistent | Fully sourced/consistent |
| **Voice** | Generic assistant | Fits the room | Could only be this game |
| **Structure** | Templated/incoherent | Works but familiar | Deliberate, surprising, clear |
| **Specificity** | Abstractions | Some concrete detail | Concrete, sensory, situated |
| **Restraint** | Overwritten | Occasionally bloated | Precise; confident cuts |
| **Reader effect** | Forgettable | Competent | Memorable; makes you want more |
| **Gameplay value** | No choice/consequence | Functional | Clear choice, real cost, callback |

**Pass:** average ≥ 3.5, no hard fail. **Publish:** human sign-off.

Do not let a model “score” this alone. Use it as a human worksheet; a model can pre-fill for triage.

---

## 8. CI and tooling

`tools/slop-audit.mjs` is a **heuristic triage tool**:

- lexical/phrase patterns from `data/slop-patterns.json`;
- structural signals (sentence/paragraph variance, em-dash density, repetition, unique-word ratio);
- a 0–100 score and per-category profile;
- JSON output for dashboards.

Run it as a **warning**, not a hard gate at first:

```bash
node tools/slop-audit.mjs --root content/ --fail-over 55
```

On the included samples, a deliberately sloppy 190-word passage scored **100/100**; a clean 170-word scene scored **12/100**. That is the intended contrast — a smoke alarm, not a judge.

A smoke test on three existing Lantern Road story documents scored **18, 34 and 49**. Most of the hits were em dashes and bold-first bullets, not narrative slop. That is exactly why the threshold is a **warning** and a human decides.

Pair it with:

- `tools/name-audit.mjs` for name collisions;
- registry/schema validation for canon;
- a human "suspicious queue" for high scores (the Clarkesworld model);
- a monthly sample audit, not a one-time pass.

**CI policy:**

- Fail on schema/registry contradictions.
- Warn on slop score above a project threshold.
- Never auto-reject or auto-publish on a slop score.
- Route high scores to a human editor; record false positives; tune patterns.

---

## 9. How this changes the writers’ room

Add a `QUALITY.md` to each repo (template supplied) and make the quality ladder part of the room’s definition of done:

1. **Showrunner** owns the brief and final sign-off.
2. **Worldbuilder** supplies facts and the registry.
3. **Character lead** checks want/contradiction/voice.
4. **Dialogist** reads aloud and cuts.
5. **Continuity editor** runs the audits and fact check.
6. **Guest editor** (human or a different model) hunts slop and generic phrasing.

The room’s job is not to “make it sound human.” It is to make it **specific, true, voiced and worth the reader’s time**. Anti-slop is the floor; voice and insight are the ceiling.

### Prompt contract addition

Every generation prompt should include:

```
QUALITY CONTRACT
- Relevance: answer the brief, not a generic version of it.
- Density: every paragraph must add a fact, image, decision or feeling.
- Specificity: use the supplied facts; do not invent names/places/claims.
- Structure: no rhetorical question + answer; no "not X but Y" chains;
  no signposted conclusion; vary sentence length.
- Voice: follow the voice bible; if a line could be any fantasy game, rewrite it.
- Restraint: cut 10% after drafting; do not explain the theme.
- If a fact is unknown, say "unknown" rather than inventing.
```

And a revision pass:

```
Edit this draft against the quality rubric. Mark the weakest 10%.
Cut filler, replace abstractions with concrete details, remove
rhetorical scaffolding, and read it aloud. Do not add new canon.
```

---

## 10. Thirty-day implementation plan

### Week 1 — Baseline

- Run `slop-audit` on 20 samples across WILDY and Lantern Road.
- Have a human editor mark the worst spans and why.
- Define project-specific tics and a quality threshold (start at 55, tune).
- Fill `templates/writers-room/QUALITY.md`.

### Week 2 — Pilot

- Rewrite 3 WILDY scenes with the ladder: brief → facts → draft → slop profile → fact check → structure → voice → reader.
- Blind-test old vs new with 3–5 readers.
- Compare slop scores, reader preference and “would talk again.”

### Week 3 — CI and editorial routine

- Add `slop-audit` as a warning in CI.
- Create a “suspicious queue” for high scores; human review only.
- Add the quality contract to `PROMPTS.md`.
- Train the editor on the taxonomy; log false positives.

### Week 4 — Lantern Road

- Apply the ladder to 5 NPCs and 2 quests.
- Run name audit + slop audit + registry validation.
- Compare against the WILDY baseline.
- Decide thresholds and whether to roll to Repository Town.

---

## 11. Limits

- The slop taxonomy is validated on news and QA, not game dialogue; the dimensions transfer, the weights do not.
- Binary slop judgments are subjective; expert agreement is poor on the overall label. Treat scores as triage.
- The `tropes.fyi` list is a practitioner style guide, not a controlled study; some patterns are legitimate.
- The Antislop sampler/FTPO require logit access or fine-tuning; most APIs do not expose them.
- Self-Refine gains are task-dependent; self-critique can be shallow.
- LLM judges have position/verbosity/sycophancy biases; do not let them be the final gate.
- No playtest has validated this specific quality ladder yet; the 30-day plan is the test.

---

## Sources

- Shaib, C., Chakrabarty, T., Garcia-Olano, D. & Wallace, B. C. (2025/2026). *Measuring AI “Slop” in Text.* [arXiv:2509.19163](https://arxiv.org/abs/2509.19163) — taxonomy, expert annotation, dimensions, limits of automated/LLM measurement.
- Paech, S., Roush, A., Goldfeder, J. & Shwartz-Ziv, R. (2025). *Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models.* [arXiv:2510.15061](https://arxiv.org/abs/2510.15061) — 1,000× frequencies, 8,000+ patterns, 90% reduction, FTPO, DPO degradation.
- Roush, A. & Mahajani, P. (2026). *Anti-slopping: An innovation for rectifying LLM writing clichés.* Thoughtworks. [link](https://research.thoughtworks.com/library/anti-slopping-an-innovation-for-rectifying-llm-writing-cliches) — sampler throughput cost, 69–96%.
- Clarke, N. (2025). *How “AI” submissions have changed our submissions process.* Clarkesworld. [link](https://neil-clarke.com/how-ai-submissions-have-changed-our-submissions-process/) — automated triage, human review, false positives, no algorithm final.
- *AI Writing Tropes to Avoid* / `deslopify` / tropes.fyi. [list](https://github.com/danicat/skills/blob/main/writing/deslopify/references/tropes.md) — practical lexical/structural tells; practitioner source.
- Madaan, A. et al. (2023). *Self-Refine: Iterative Refinement with Self-Feedback.* NeurIPS 2023. [link](https://papers.nips.cc/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html) — ~20% absolute improvement from iterative self-feedback.
- Shi, L. et al. (2025). *Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge.* IJCNLP-AACL 2025. [link](https://aclanthology.org/2025.ijcnlp-long.18/) — judge position bias across 15 judges/150k evaluations.
- Zhang, J. et al. (2025/2026). *Verbalized Sampling.* [arXiv:2510.01171](https://arxiv.org/abs/2510.01171) — candidate diversity; use with a fit floor.
- Mozo Quesada, A. et al. (2026). *Character-Name Concentration in LLM Fiction.* [arXiv:2611.01284](https://arxiv.org/abs/2611.01284) — static banlists displace; registry/tracking works.
- Hamilton, S. & Mimno, D. (2026). *Elias in the Lighthouse, Again?* [arXiv:2605.26492](https://arxiv.org/abs/2605.26492) — alignment-data repetition.
