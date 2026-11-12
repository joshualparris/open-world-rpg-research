# Self-prompt: Aetheria originality, depth and fun program

> Written by me, for me, 2026-11-12. This is the working contract for the Aetheria pilot (roadmap item 12). It is deliberately shorter than the DeepSeek prompt because I already hold the research, tools and rules. It records the **real starting state** I found, so nothing later is claimed without a baseline.

## 0. Mission
Take **Aetheria** (`Parris-Tech-Services/Aetheria`, public; React + TypeScript + zustand client, Express server) from a thin prototype to a game that is **playable, honest, original and deeper**, in small verified steps. Keep going until the Definition of Done is met or a stop condition fires. I never claim "fun": Josh is the judge. I hand over a build, evidence and a plain report.

## 1. What I found at the start (baseline, verified by reading the code)
1. **Most authored content is dead.** `npc-data.ts` (7 NPCs with dialogue trees), `quest-data.ts` and `lore-data.ts` are **imported by nothing**. The live game uses only `GameData.npcDialogue` in `data.ts`: **3 NPCs, 2 options each**.
2. **Choosing a dialogue option shows nothing.** `Play.tsx` calls `closeDialogue()` in `onSelectOption`; the NPC's `response` is never displayed. That violates "player actions must give visible feedback".
3. **The player cannot leave the first map.** The village layout has no `>` exit tile, and `movePlayer` blocks stepping onto `>` before the exit logic can run, so map transitions can never fire. The tavern, barrow, Ashfields and boss chamber are unreachable.
4. **Entities with no behaviour:** a chest (`T`) opens a dialogue lookup that returns nothing (silent); a guard (`G`) is defined but never placed; combat says "Gained 50 XP" but XP is never applied.
5. **Names are LLM defaults:** Elara Mossbind, Guard Captain Theron, Mira the Wanderer, Brother Aldric (the audit: Elara 13, Theron 6, Mira 3, Aldric 3). Fenwick, Dunna and the Hollow King fit the world's own register and stay.
6. **No tests and no CI.** `tsc` reports pre-existing errors in `server/storage.ts` (not mine; I will not widen scope to fix them, only avoid adding any).

## 2. Voice (draft, derived from existing canon)
- **World:** a woodland-edge village under the shadow of the Hollow King's curse; Spring Spirits, the Rotted Barrow, the Ashfields, the Deepkin. Tone: weathered, practical, quietly eerie; people talk about work, weather and debt, not destiny.
- **Naming grammar:** short Old-English-flavoured given names; surnames are plant/craft/landscape words or compounds (*Mossbind*, *Fenwick*); places are compounds (*Tipped Flagon*, *Rotted Barrow*). Keep canon names; reserve them; new names come from `namegen.py --voice`.
- **Rules for every NPC:** a want that is not "save the world", a limit, something they will not discuss, and a reason their line changes after the player acts.

## 3. Definition of Done for this program (scoped to what a session can prove)
- [ ] **Playable loop:** a new player can leave the village, reach the barrow and tavern, talk to every NPC, accept and progress a quest, and return; verified in a **real browser** on a recorded commit.
- [ ] **Honest feedback:** every interaction (dialogue option, chest, exit, quest change) produces visible output; no silent buttons.
- [ ] **Live content = authored content:** the dialogue trees, quests and lore are wired into the engine (or explicitly removed); none is dead.
- [ ] **NPC depth:** each NPC has want, limit, knowledge boundaries (public/private/unknown), a tone-change trigger, and at least three states (first meeting, return, after the player acts).
- [ ] **Originality:** names from the generator/grammar; `name_audit` 0 hits on player-facing text except approved canon; one family one surname.
- [ ] **No slop:** `slop_lint` on player-facing text: median at most 5, none above 15; flagged text went through the tool-fed Editor pass.
- [ ] **Guard rails:** a content-integrity test (dialogue graph, quests, names) and a browser smoke test that fail on the old behaviour; `tsc` errors in `client/` not increased.
- [ ] **Handover:** before/after numbers, evidence, gaps, decisions for Josh.

## 4. Rules for this session
- Work on branch `claude/new-session-yrqsqk` in each repo. **Do not push to `main`. Do not open PRs** unless Josh asks.
- Small, reviewable commits; one concern per commit; commit messages carry the session trailer.
- Never weaken a test, threshold or banlist to pass. Never fabricate evidence; say "I did not run it" when true.
- Public repo hygiene: no secrets, no private repo names, no copyrighted text or imitation of a living author.
- Keep canon names stable (ids never change, so saves keep working); display names only.
- Stop and report on: three iterations with no measurable improvement; anything that needs Josh (canon rename beyond the four default names, rating/tone change, deleting content, real-device checks).

## 5. The loop I will run
1. **Baseline:** name audit, slop lint (on strings in code), type-check, build, and a real-browser first-five-minutes run.
2. **Fix the biggest blocker first** (priority: can't progress > silent actions > dead content > names/voice > depth > polish).
3. **Wire, don't add:** connect what exists before writing more.
4. **Write with the room:** names and premises from code; Voice Bible as the prefix; positive style rules; slop check then a findings-fed edit; continuity check; me as showrunner reviewing every line.
5. **Verify in a browser;** add a test that fails on the old behaviour.
6. **Measure, log, repeat** in `docs/ORIGINALITY-PROGRAM.md`.

## 6. Order of work for this session
1. Tooling: let `slop_lint` read strings in code (content lives in `.ts` files).
2. Baseline measurements + real-browser run (record the blockers above as evidence).
3. Make the map transitions and exits work; add exits and a tavern door.
4. Wire dialogue trees (flags, requires, effects, reputation) with visible responses; chest and unknown-entity feedback.
5. Wire quests and a visible quest log; apply XP; connect lore discoveries.
6. Voice Bible, `voice.json`, registry; rename the four default-name NPCs (display names only).
7. Rewrite the NPC content to the depth standard; slop pass; continuity pass.
8. Tests (content integrity + browser smoke); final measurements; handover report.

If I run out of runway, I stop after a step that leaves the game **better and working**, and I say which steps remain.
