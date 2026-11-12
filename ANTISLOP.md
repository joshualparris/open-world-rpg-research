# Anti-Slop: What People Do to Get High-Quality Prose Out of LLMs, and Our Operating Model

**Prepared 2026-11-12 · Builds on [ORIGINALITY.md](ORIGINALITY.md) and [WRITERS-ROOM.md](WRITERS-ROOM.md) · Tool: [`tools/originality/slop_lint.py`](tools/originality/slop_lint.py)**

"Slop" is the stock vocabulary, phrasing, structure and repetition that make LLM text feel generic. Names like Mira are one kind of slop (covered in [ORIGINALITY.md](ORIGINALITY.md)). This note covers the rest: what it is, what people actually do about it, what does not work, and how we have built it into the way we produce content.

---

## 1. The short answer

- **Earlier I covered only part of this** (the Antislop sampler and a name banlist). This is the wider pass.
- **What people do is a layered stack**, not one trick: positive style rules and examples in the prompt; written rule sets of stock words and structures; decoding-time suppression and training-time fixes *if you control the model*; and, for everyone else, **detect → revise with outside feedback → re-check → human edit**.
- **What matters most for us** (hosted models, no training): a rule set of patterns we enforce with a **linter**, an **editor pass that is fed the linter's findings**, a **human showrunner**, and **measurement**. All four are now in place (section 6).
- **Three traps to avoid:** using "AI detectors" to judge people, treating one statistic (like em dashes or sentence-length variation) as proof, and letting the model grade and fix itself with no outside feedback.

---

## 2. What slop actually is (and how it was measured)

| Kind | Evidence | In our linter? |
| --- | --- | --- |
| **Stock vocabulary** | Across 14M PubMed abstracts, words like *delves*, *showcasing*, *underscores* rose far above pre-LLM trends (excess-frequency ratios of about 28, 10 and 11); by 2024 at least ~10% of abstracts were LLM-assisted. A later revision notes that some of those words then *fell* while others (*significant*) rose, so **lists age**. Kobak et al., [arXiv 2406.07016](https://arxiv.org/abs/2406.07016) | Yes (`words`) |
| **Stock phrases and clichés** | Sets of overused phrases appear over **1,000x** more often than in human text in some models ([Antislop, ICLR 2026](https://arxiv.org/abs/2510.15061)). Fiction clichés (*shiver down her spine*, *heart hammered*, *a breath she didn't know she was holding*) are the practitioner staples. | Yes (`phrases`) |
| **Stock structures** | The Wikipedia editors' field guide ([Signs of AI writing](https://cavac.at/cavacopedia/Wikipedia%3ASigns_of_AI_writing), read via a mirror) lists "not X, but Y" negative parallelism, habitual triplets (rule of three), vague "significance" clauses, and tidy summary endings, and says plainly that these are **signs, not proof**. | Yes (`negative_parallelism`, `rule_of_three`, `participial_significance`, `paragraph_aphorism`) |
| **Repetition and low lexical variety** | The open [slop-score](https://github.com/sam-paech/slop-score) tool combines slop-word and trigram matches, n-gram repetition, "not X but Y" patterns and lexical diversity (MATTR-500). EQ-Bench publishes slop and repetition beside its leaderboard rather than inside the ranking. | Yes (`repeated_trigrams`, `repeated_openers`; MATTR reported) |
| **Names, settings, professions** | Cornell: 11 words in 88.3% of 20,000 stories; "Elara" 85,513x over human text in one model. | Yes, via [`name_audit.py`](tools/originality/name_audit.py) and the generator |
| **Em dashes** | The Wikipedia guide notes they are more frequent in LLM text than typical non-professional writing but treats the sign as useful *only alongside others*; it is "not a ban on punctuation". | Scored only above a high rate |
| **Uniform sentence length ("burstiness")** | **Disputed.** One vendor test (about 5,900 pairs) found it near chance (AUROC 0.521), and a NeurIPS 2026 submission argues it is confounded with length. Not peer-reviewed. | Reported as **advisory only**, not scored |

**Why models do it (leading hypotheses, not settled):** human raters in feedback training prefer certain words (a COLING 2025 study found mixed evidence; a follow-up, [arXiv 2508.01930](https://arxiv.org/abs/2508.01930), found participants systematically preferred variants containing some of the words), and preference tuning narrows diversity in general (see [ORIGINALITY.md](ORIGINALITY.md)). Because these patterns come from *training*, rewriting a prompt rarely removes them entirely.

---

## 3. What people do: the stack, from cheapest to most powerful

| Layer | What people do | Do we use it? |
| --- | --- | --- |
| **1. Prompt** | Positive style rules ("write concrete nouns", "end on an action"), specifics supplied up front, and **examples instead of adjectives** (voice lives in samples). | **Yes** (Voice Bible; section 7 prompt) |
| **2. Written rule sets** | Reusable lists of stock phrases and structures to avoid, e.g. the open-source [stop-slop](https://github.com/hardikpandya/stop-slop) skill (banned phrases, structural patterns such as binary contrasts and rule-of-three, a 5-dimension score where under 35/50 means revise; it says it should *not* dumb the writing down) and a 200+ rule fork that adjusts by register. | **Yes**, as our own independent list in `slop_lint.py` (I did not copy theirs) |
| **3. Decoding** (if you control the model) | The [Antislop sampler](https://github.com/sam-paech/antislop-sampler) backtracks when a banned string appears; **min-p** keeps quality at higher temperature. | Not on hosted APIs; noted for local models |
| **4. Training** (if you train) | **FTPO** (final-token preference optimisation) reports about 90% slop reduction with little quality loss and works with lists of ~8,000 patterns, where plain token banning fails past ~2,000 (secondary summaries); **DivPO** reports about 45.6% more diverse persona attributes and 74.6% more story diversity. | No (we do not train) |
| **5. Post-process loop** | **Detect, then revise using the findings, then re-check.** | **Yes** (section 6) |
| **6. Human edit** | A person owns taste, canon and names. | **Yes** (the showrunner) |
| **7. Measurement** | Slop score, n-gram repetition, lexical diversity, an LLM judge, and human preference. | **Yes** (linter plus the A/B test in [WRITERS-ROOM.md](WRITERS-ROOM.md)) |

**On "never say X" prompts.** There is a named "pink elephant" effect: naming a forbidden thing can *increase* it. The one academic study I found is about **image** generators ([Hwang et al., arXiv 2404.15154](https://arxiv.org/abs/2404.15154)); for text models the evidence is anecdotal and I found no controlled test. The practical hedge is cheap: **say what to do** in the prompt, and keep the long banlists in the **validators and the editor pass**, not in the generation prompt. (I have corrected the prompt pack in [ORIGINALITY.md](ORIGINALITY.md) accordingly.)

---

## 4. What not to do

1. **Do not use detectors to judge people.** In a study of seven AI-text detectors, the average false-positive rate on non-native English essays was **61.3%**, with one detector flagging over 97% ([Liang et al.](https://arxiv.org/abs/2304.02819)); simple self-edit prompts also drove detection of real AI text as low as 13%. Our linter is a **quality check on our own output**, not an accusation tool.
2. **Do not treat one statistic as proof.** Em dashes and sentence-length variation are weak, contested signals. The score is a heuristic; the thresholds (5 and 15) are **not validated**; tune them on text you consider good.
3. **Do not let the model fix itself unaided.** A 2024 study found self-refinement **amplifies self-bias** (the model "corrects" things that were fine) and that **external feedback with accurate assessment** reduces it ([arXiv 2402.11436](https://arxiv.org/abs/2402.11436)). So our editor pass is fed the **linter's concrete findings**, not "make this better".
4. **Do not over-clean.** Stripping everything distinctive produces flat text, and removing one pattern can let another appear (whack-a-mole; Antislop reports its method limits new patterns emerging, but prompt-level lists do not). Keep the voice, cap the rounds, and refresh the lists.
5. **Do not rely on static lists.** Vocabulary shifts over time. Refresh from your own approved vs rejected text.

---

## 5. Where this fits in the writers' room

The room in [WRITERS-ROOM.md](WRITERS-ROOM.md) already has a *Contrarian*. It becomes a **tool-fed Editor**: it never edits blind. The linter finds the problems; the Editor rewrites exactly those spots.

---

## 6. Our operating model (implemented)

```
brief
  → code draws names, places, premise            (namegen.py --voice; seed logged)
  → Voice writer drafts                          (positive style rules + samples; Voice Bible prefix)
  → slop_lint.py                                 (score, findings with line numbers)
       ok (<= 5)      → continue
       watch / revise → Editor pass fed the findings  (max 2 rounds), then re-lint
  → name_audit.py + registry check               (no banlisted or unregistered names)
  → human approves                               (showrunner)
  → registry updated; lists refreshed from approved/rejected text (monthly)
```

**Gates (per batch):** median score at most 5, no file above 15, zero unintended hits from the `words` list, names pass the audit, a blind speaker-ID check on dialogue, human approval.

**What exists now:**

| Piece | File |
| --- | --- |
| Slop linter (words, phrases, 4 structures, repeated openers and trigrams, em-dash rate, advisory sentence-length and MATTR) | [`tools/originality/slop_lint.py`](tools/originality/slop_lint.py) |
| Name audit | [`tools/originality/name_audit.py`](tools/originality/name_audit.py) |
| Voice-aware generator | [`tools/originality/namegen.py`](tools/originality/namegen.py) |
| Per-repo extension of the lists | `--patterns my.json` or `banned_words` / `banned_phrases` in `voice.json` |
| CI gate | `slop_lint.py content/ --max-score 15` (exit code 1 on failure) |

**How the linter was checked.** On a deliberately sloppy paragraph it scores about 435; on a clean paragraph written for the test it scores 0. Along the way I fixed three false alarms it produced on your files: contraction matching inside words ("Important"), em dashes inside headings, and repeated labels in structured metadata.

### Baseline: Lantern Road story files (public repo)

54 files, **mean 5.7**; 34 ok, 16 watch, 4 revise. The categories that fired most: **rule-of-three (54), repeated trigrams (37), repeated sentence openers (24)**; stock words (15), stock phrases (1) and "not X, but Y" (3) were **rare**.

**Reading it correctly:** the lexical slop is low, which is good. The habits to watch are triplets and repeated phrasing. Most of the high-scoring files are authoring or design documents and rumour tables, not finished player-facing prose, so this is a **rough baseline, not a quality verdict**. Re-run it on actual in-game text once the pilot produces some.

---

## 7. Prompt pack

**A. Style rules for the generation prompt (positive, short):**

```text
Write the way a specific person in this world would speak or notice things.
- Name the exact object, task, price or place instead of the type of feeling.
- Make each sentence carry one new fact; vary length by content, not by formula.
- Put the character's want in an action or a refusal, not a summary of feelings.
- End scenes on a concrete image or a decision, never a moral.
- Use the NAMES, PLACES and PREMISE supplied in the context exactly as given.
```

**B. Editor pass, fed by the linter (this is the part that must be external feedback):**

```text
Here is a draft and a list of specific problems found by a checker (line, category, snippet).
Rewrite ONLY those passages. Keep the meaning, the facts, the names and the voice.
For each problem, replace it with the concrete detail a person in this world would give.
Do not add new metaphors. Do not change anything that was not listed.
Return the full text, then a one-line note per change.
PROBLEMS:
{findings}
DRAFT:
{draft}
```

Then **re-run the linter**. Stop after two rounds; send what remains to the human.

**C. List refresh (monthly, by a person or script):** collect rejected drafts, run the linter, and add repeating words and phrases to `banned_words` / `banned_phrases` in the repo's `voice.json`; remove entries that no longer appear.

---

## 8. Limits of this note

- **Source quality varies.** The Wikipedia guide was read through a mirror and secondary coverage; the FTPO/DPO comparisons come from summaries; the pink-elephant evidence for text is anecdotal; the burstiness evidence is non-peer-reviewed. I flagged each.
- **The linter is heuristic.** It will miss slop it does not know and flag some good prose. Its score is relative; calibrate on text you like.
- **The word lists are mine.** They follow the categories in the sources but are not copied from any of them.
- **No test with readers yet.** Whether lower slop scores make content *better to read* is exactly what the A/B test in [WRITERS-ROOM.md](WRITERS-ROOM.md) measures.

---

*See [WRITERS-ROOM.md](WRITERS-ROOM.md) for the roadmap this plugs into and [`tools/originality/`](tools/originality/) for the tools.*
