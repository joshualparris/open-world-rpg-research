# Design & Playtest Checklist

A practical checklist for an open-world RPG with a dense NPC cast. Use it as a design review, a content budget, or a playtest script.

---

## 1. World shape

- [ ] The main draw is **autonomy**, not map size: the player can approach major goals in more than one order and more than one way.
- [ ] Every major region has a readable silhouette/landmark from a distance.
- [ ] Landmarks form a hierarchy: regional (draws the eye), local (a promise of a kind of experience), micro (rhythm/decoration).
- [ ] 60–90 seconds of travel between meaningful beats, or a deliberate longer stretch with a view/decision.
- [ ] Negative space is intentional: quiet roads, long views, weather, room to think.
- [ ] Traversal offers decisions (shortcut, mount, climb, risk, fast travel, toll).
- [ ] Fast travel exists for time-poor players, without erasing the first journey.
- [ ] Optional content is clustered and its reward type is visually legible.
- [ ] The map reveals progressively; not every activity is an icon at hour one.
- [ ] “Known / rumoured / discovered” states are distinct.
- [ ] Some secrets are deliberately off-map.

**Red flags**

- long empty traversal with no decision or view;
- an icon for every collectible;
- a map that shows everything before the player has a reason to care;
- a “beeliner” path that is boring, or an explorer path that is punished.

---

## 2. Density and pacing

- [ ] Meaningful beats per minute is a tracked metric, not a vibe.
- [ ] Main-path beats and optional beats have different densities.
- [ ] Repeated exposition is cut; the player is not told the same thing by three NPCs.
- [ ] Important information is delivered in focused scenes; less important information can happen while moving/doing.
- [ ] The player is not forced to complete busywork to reach the main story.
- [ ] Each region has a mood/pace change (safe camp, dangerous road, quiet ruin).
- [ ] The game respects the player's time budget: save/quit, resume, short sessions, clear goals.

**Red flags**

- “wide as an ocean, deep as a puddle”;
- a checklist of chores disguised as content;
- every quest at the same intensity;
- long stretches where nothing changes.

---

## 3. NPC cast architecture

- [ ] The cast is tiered: core, recurring, ambient, faction/antagonist.
- [ ] Core NPCs have authored identity, routine, memory, multiple scenes and at least one arc.
- [ ] Recurring NPCs have a job/home, a handful of topics, one or two callbacks.
- [ ] Ambient NPCs have short reactive lines and do not claim deep history.
- [ ] Every NPC has a stable ID, not just a display name.
- [ ] Names are unique within a role tier; repeated names are deliberate (family, alias) and explained.
- [ ] The content budget per tier is written down (topics, scenes, callbacks, voice lines).
- [ ] The UI can show a large cast without turning into a spreadsheet.

**Red flags**

- 200 “residents” generated from 26 names;
- every NPC has the same three topics;
- named characters who never do their job;
- ambient NPCs who claim to remember events they never witnessed.

---

## 4. NPC presence

For each core/recurring NPC:

- [ ] **Identity:** name, role, faction, voice, relationships, pronouns, secrets.
- [ ] **Place:** current location resolved from simulation; home/workplace distinct; no guessed location.
- [ ] **Routine:** work/rest/social/meal/travel; off-screen simulation continues.
- [ ] **Memory:** met, last topic, promise, favour, lie, quest outcome, relationship change.
- [ ] **Consequence:** dialogue/actions change shop stock, quest state, world objects or relationships.
- [ ] **Expression:** posture, gesture, timing, silence, voice; not only text.
- [ ] **Truthfulness:** every claim in dialogue is true, deliberately false, or explicitly framed as rumour/hearsay.
- [ ] **Repeat-safe:** first-return line, short repeat line, optional follow-up.
- [ ] **Culling:** rendering stops off-screen; simulation does not.
- [ ] **Privacy:** memory is local, inspectable, resettable; AI chat is optional and separate.

**Test:** ask the NPC where they are, what they are doing, and what they remember about the player. Cross-check all three against the simulation.

**Red flags**

- dialogue and physical actions disagree;
- NPCs describe objects not present;
- seeded backstory presented as witnessed history;
- a shopkeeper who cannot see their own stock;
- an NPC frozen because the player walked away.

---

## 5. Dialogue

- [ ] 3–4 options per choice (more only for rare set-pieces).
- [ ] Each option has a distinct intent (kind, stern, curious, deceptive, etc.).
- [ ] Full literal line shown when the choice has consequences; paraphrase only for flavour.
- [ ] A “leave” option always exists.
- [ ] No lore dump: personal first, world later.
- [ ] Hubs are limited (topics per visit, already-asked hidden, NPC can interrupt/refuse).
- [ ] Waterfall used for dramatic spine; hub used for optional investigation.
- [ ] Skills/background/faction/reputation gate real options, not cosmetic ones.
- [ ] Failure is authored (new situation, not reload).
- [ ] The Lantern Road test: learn, reveal, react, remember, obligate, risk, acknowledge — at least one.
- [ ] The NPC has a goal in the conversation, not just answers.
- [ ] Recorded lines/captions match; no invented subtitle for generated speech.
- [ ] Mobile: readable at 360–430 px; hit targets ≥ 44 px; keyboard/controller support.

**Red flags**

- paraphrase that makes the player say something they did not intend;
- a hub that turns the NPC into a database;
- choices that converge with no acknowledgment;
- “Tell me about the war” → 800-word history lecture;
- a “romance” option that is just a disposition bar.

---

## 6. Quests

- [ ] Origin is a person/place/situation, not a floating task.
- [ ] Offer: why this person, why now.
- [ ] Complication/investigation: the player's understanding changes.
- [ ] Decision/resolution: a real trade-off.
- [ ] Aftermath: a human/world response.
- [ ] Non-ideal branch: refusal, delay, failure, partial success.
- [ ] At least two viable approaches (combat, stealth, persuasion, investigation, creativity).
- [ ] Consequence appears soon and again later.
- [ ] Consequence is visible enough to recognise.
- [ ] No busywork; if the quest disappeared, the character/place would lose something.
- [ ] Rewards are legible and fit the fantasy (loot, knowledge, access, relationship, expression).

**Red flags**

- “collect 10 wolf pelts” with no character/place stake;
- one solution dressed up as three;
- a “choice” where one option is obviously correct;
- a consequence that never returns;
- a quest that exists only to fill a map icon.

---

## 7. Player identity

- [ ] The player knows who they are in the world and in a conversation.
- [ ] Background/class/race/faction change dialogue options, risks and reactions.
- [ ] Build choices matter outside combat (investigation, crafting, social).
- [ ] Companions have goals that can conflict with the player's.
- [ ] Companions remember promises, lies and faction choices.
- [ ] Reputation/faction standing changes access and tone, not just numbers.
- [ ] The player can be wrong, fail, or refuse without the game ending.

**Test:** “Who am I in this conversation?” If the answer is “a cursor selecting options,” the role is underdesigned.

---

## 8. Worldbuilding and lore

- [ ] A world bible defines the authorial truth: geography, history, factions, technology, daily life.
- [ ] NPCs can be wrong, lying or biased; the bible still knows the truth.
- [ ] Secrets are planted across places, objects, rumours and people.
- [ ] The player can infer facts from the environment before being told.
- [ ] The journal records what the player learned, not everything the designer knows.
- [ ] Fact / rumour / theory are distinguished in the UI.
- [ ] The main story starts with a personal stake, not a history lecture.
- [ ] The world exists beyond the player: factions act, schedules advance, ruins predate you.

**Red flags**

- opening with a cosmology lecture;
- contradictory lore because no bible exists;
- mystery presented as randomness;
- every secret explained in a codex entry.

---

## 9. Systems, AI and truth

- [ ] The simulation owns facts: location, time, inventory, money, quests, relationships, world objects.
- [ ] Dialogue effects are typed, allowlisted, authoritative and idempotent.
- [ ] Unknown state denies the option; it never enables a guess.
- [ ] Failed transactions cannot trigger success dialogue or success audio.
- [ ] AI is narration/free-chat only; it cannot mutate state.
- [ ] AI answers are grounded in live state or explicitly say “I don't know.”
- [ ] Authored dialogue works offline.
- [ ] Recorded audio/captions are verified against the actual clip.
- [ ] Graph validation catches missing nodes, cycles, unreachable nodes, duplicate IDs.
- [ ] Save migration preserves flags, quests and relationships.

**Red flags**

- an AI NPC inventing a quest reward;
- a shopkeeper quoting stock they do not have;
- a success line after a failed check;
- a dialogue flag that resets on reload;
- an LLM “memory” the player never experienced.

---

## 10. Content operations

- [ ] Content-as-data with stable IDs.
- [ ] A catalogue/index of actors, places, quests, topics, flags and effects.
- [ ] Graph validators and link checkers in CI.
- [ ] Content tracker for branches/scenes/voice coverage.
- [ ] Authoring workflow (CMS/spreadsheet/JSON) with review.
- [ ] Privacy/redaction gate for logs, memories and exports.
- [ ] Migration plan for IDs and save flags.
- [ ] Performance budget for NPCs, dialogue UI and audio on mobile.

---

## 11. Playtest measures

### Exploration

- [ ] Time to first meaningful choice.
- [ ] Time between meaningful beats.
- [ ] Landmark recall (draw the map from memory).
- [ ] Traversal dead time.
- [ ] Fast-travel use vs first-journey enjoyment.
- [ ] Map-staring time / analysis paralysis.
- [ ] Optional-content uptake; beeliner path viability.

### NPCs

- [ ] Name/role recall for 3 NPCs.
- [ ] Location truth check.
- [ ] Memory/callback recognition.
- [ ] Repetition count across three visits.
- [ ] Fabricated-claim count.
- [ ] Off-screen routine advancement.
- [ ] Shop/action alignment.
- [ ] “Would you talk to them again?” reasons.

### Dialogue

- [ ] Intent clarity (“what will this choice do?”).
- [ ] “I didn't mean to say that” rate.
- [ ] Skip rate (boredom vs reading speed).
- [ ] Hub exhaustion behaviour.
- [ ] Leave-comfort (“did you feel free to exit?”).
- [ ] Consequence recognition.

### Quests

- [ ] Approaches found and perceived viability.
- [ ] Non-ideal branch uptake and interest.
- [ ] Aftermath recall.
- [ ] Busywork rating.
- [ ] Would they replay for another path?

### Emotion / story

- [ ] Favourite NPC/place and why.
- [ ] Hardest choice and why.
- [ ] “What happened in your playthrough?” — story vs checklist.
- [ ] Return intention.

---

## 12. Quick audit: 20 questions

1. Can the player describe two viable plans for the next 20 minutes?
2. Is there a landmark visible from the last landmark?
3. How long is the walk with no decision or view?
4. Does the map show the player a question, or an answer?
5. Can the player name three NPCs by what they *do*?
6. Does every named NPC have a place, routine and memory?
7. Does any NPC claim a location/object/event the simulation does not support?
8. Does a shopkeeper's dialogue agree with their stock?
9. Is there a repeat-safe line for the second and third visit?
10. Do 3–4 dialogue options have distinct, legible intents?
11. Can the player leave any conversation immediately?
12. Does any hub feel like an information vending machine?
13. Does failure create a new situation rather than a reload?
14. Does a choice return later in a visible way?
15. Does a quest start with a person/place rather than a task?
16. Is there a non-ideal branch that is interesting?
17. Does background/build/faction change a conversation?
18. Do companions have goals that can conflict with the player?
19. Does the AI ever invent state? (It must not.)
20. Would a player tell a story about this session, or list what they collected?

---

*If most answers are “yes,” the world and cast are probably doing the hard work. If not, start with presence and density before adding more map or more NPCs.*
