# Writers’ Room Audit

## Automated checks

- [ ] `node tools/slop-audit.mjs --root <content> --top 15` — no unexplained high-slop cluster; score routed to human.
- [ ] `node tools/slop-audit.mjs --root <content> --fail-over 55` — warning threshold (tune per project; do not auto-reject on it).
- [ ] `QUALITY.md` rubric completed; no 1 in factuality/canon/voice.
- [ ] `node tools/name-audit.mjs --root <game>` — no new cross-project core-name collisions.
- [ ] `node tools/table-draw.mjs --seed <arc-id> --table names --count 3` — reproducible; no excluded names.
- [ ] Registry JSON validates; every core name has `source`, `seed`, `status`, `universe`.
- [ ] No duplicate name+role pair across universes.
- [ ] No core name marked `watchlist` is used without a written justification.
- [ ] No model-invented core name/place/faction in the diff.
- [ ] No banned voice tics (project-specific list in `VOICE.md`).
- [ ] Save/load includes all new registry fields.

## Human gate

- [ ] Read aloud; cut 10%; no rhetorical question/answer, no "not X but Y" chains, no signposted conclusion.
- [ ] Blind reader can identify the game from 200 words.
- [ ] Every specific name/place/number/claim is sourced or registry-backed.
- [ ] High slop scores are reviewed by a human, not auto-rejected.
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
