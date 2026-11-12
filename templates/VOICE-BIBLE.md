# Voice Bible: <repo / game / world name>

> Copy this file into the repo (for example `docs/VOICE-BIBLE.md`). Keep it short enough to load in full as a **static prefix** in every writing prompt (about 1,500-2,500 tokens). Details live in the linked files, not here.
> Companion machine-readable file: `voice.json` (naming grammar, trades, quirks, wants, reserved canon). See `voice.example.json`.

## 0. Meta
- **Showrunner (final say):** <you>
- **Room size:** 1 / 3 / 6 / 10  (see section 2)
- **Status:** draft / reviewed / adopted · **Last reviewed:** <date>
- **Canon boundary:** <what is fixed and may not be invented or renamed; what is open>
- **Audience and rating:** <who it is for; content limits>

## 1. Premise and pillars (3-5 lines)
One sentence premise. Three pillars, each as a *rule a writer can break* (for example: "debts outlast people").

## 2. The room
| Writer | Owns | Does not touch | How it works |
| --- | --- | --- | --- |
| **Showrunner** | canon, premise, final approval | | human |
| **Worldsmith** | names, places, trades, quirks | prose | **code**: `namegen.py --voice voice.json` |
| **Voice writer(s)** | narration and dialogue in the house style | names, facts | LLM, with sections 3-6 as the prefix |
| **Quest/plot writer** | premise, beats, consequences | names | LLM, premise drawn from tables first |
| **Continuity editor** | checks against canon and the registry | | **code** + LLM check |
| **Contrarian** | cuts clichés and stock beats | | LLM pass with the banlist |
Add or remove rows to fit the room size. Each writer is **original and fictional** (a role with house rules), never "write like <living author>".

## 3. House style
- **POV / tense / register:**
- **Sentence rhythm:** (for example short, concrete, ends on the noun)
- **Humour level and kind:**
- **Violence, romance, grief: how handled:**
- **What a scene does at its start and end:** (habit, not rule)
- **Reading level / audience adjustments:**

## 4. Naming grammar  *(the Tolkien lesson: sounds first, names follow)*
- **Source flavours (pick 2-3):** (for example English dialect words, Welsh-like consonants, Norse compounds). Real languages as *seeds*, not copied names.
- **Given names:** sounds, length, endings. Example: 1-2 syllables, soft vowels, ends in -a/-en/-k.
- **Surnames:** pattern (landscape/craft words, patronymics, compounds). **One family = one surname**; no surname reused by unrelated people.
- **Places:** compound pattern (head + tail), what the tails mean, and a *reason each place exists* (trade, crossing, works).
- **Factions / objects / titles:** pattern.
- **Sound change over distance or time:** how a name differs across regions (optional but powerful).
- **Name taboos:** names never used; defaults that are banned (see `tools/originality/banlist.txt`).
- **Registry:** every name lives in `registry.json`; the model is never asked to choose a name.

## 5. Lexicon
- **Preferred words and images (10-20):**
- **Banned words and phrases:** stock fantasy/sci-fi words and "slop" you do not want (for example *whisper(s), echo(es), tapestry, ozone, ledger, locket*, unless chosen).
- **Idioms this world uses (and invents):**

## 6. How the cast speaks  *(voice lives in examples)*
| Tier | Speech pattern | Tic / habit | Never says |
| --- | --- | --- | --- |
| Protagonist / companions | | | |
| Recurring NPCs | | | |
| Crowd | | | |
Give **2 sample lines per tier**, written or approved by a human. Three characters should be distinguishable with their names hidden.

## 7. Structural habits
- **Quest shape:** (offer / complication / decision / aftermath / non-ideal branch, or your own)
- **Endings:** what they leave unresolved.
- **A quota of wrongness:** how often the world should surprise the genre (for example one odd, specific, un-mythic detail per scene).

## 8. Obsessions and taboos
Two or three themes the world keeps returning to, and two things it never does.

## 9. Samples (3-5, up to 120 words each)
Human-written or human-approved passages that sound like the world. These are the few-shot examples the writers see.

## 10. Canon change process
Who may add a name, place or rule; how it enters `registry.json`; how a rename is migrated (including stable actor keys and saves).

## 11. QA gates (every batch)
- [ ] `name_audit.py` has zero hits from the banlist unless chosen on purpose.
- [ ] No name outside `registry.json`; no repeated surnames outside families.
- [ ] `voice_lint` (banned lexicon) passes.
- [ ] Blind test: three speakers are told apart without names.
- [ ] Showrunner approves each batch.

## 12. Metrics and review
Distinct-name ratio, banlist rate, surname repeats, speaker-distinction score, human preference vs baseline. Review quarterly; update the banlist from real output.

## 13. Provenance and rights
What came from existing canon (inferred, not invented); what is original; any real-world inspirations used as *mechanics* only; no imitation of a living author's prose or distinctive names.
