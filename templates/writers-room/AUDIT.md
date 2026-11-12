# Writers’ Room Audit

## Automated checks

- [ ] `node tools/name-audit.mjs --root <game>` — no new cross-project core-name collisions.
- [ ] `node tools/table-draw.mjs --seed <arc-id> --table names --count 3` — reproducible; no excluded names.
- [ ] Registry JSON validates; every core name has `source`, `seed`, `status`, `universe`.
- [ ] No duplicate name+role pair across universes.
- [ ] No core name marked `watchlist` is used without a written justification.
- [ ] No model-invented core name/place/faction in the diff.
- [ ] No banned voice tics (project-specific list in `VOICE.md`).
- [ ] Save/load includes all new registry fields.

## Human gate

- [ ] Showrunner approves every core name and premise.
- [ ] Blind voice test: 4/5 readers identify the game from 200 words.
- [ ] Three core NPCs pass the presence test: identity + place + routine + memory + consequence + expression.
- [ ] A first-return line exists for each new core NPC.
- [ ] At least one NPC-to-NPC or overheard scene exists per location cluster.
- [ ] The new content does not contradict the voice bible’s “what it is not.”

## Sign-off

| Role | Name | Date | Notes |
| --- | --- | --- | --- |
| Showrunner | | | |
| Continuity editor | | | |
| Guest voice | | | |
