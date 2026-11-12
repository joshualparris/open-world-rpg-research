# Writers’ Room Kit

Copy this directory into a game repo as `writers-room/`.

## Operating principles

1. **One showrunner.** A human owns tone, canon and the final call.
2. **One-page voice bible.** If it takes fifty pages, it is a setting bible, not a voice guide.
3. **Curated tables.** The model does not choose core names, places, trades or premise facts from its prior.
4. **Seeded draws.** Same seed + same tables = same facts. The seed is the arc/quest ID, not the clock.
5. **Fixed facts in, prose out.** The model may write dialogue and description; it may not rename canon.
6. **Registry in code/CI.** The prompt copy is a reminder; validation is authoritative.
7. **Fit before novelty.** Generate 10–20 candidates, reject voice/fact breaks, then choose from the coherent lower-probability band.
8. **Human approval.** A person signs off every core name and premise.

## Files

- `VOICE.md` — the one-page room bible.
- `TABLES.example.json` — schema + sample rows; replace with curated tables.
- `REGISTRY.example.json` — used names/places/role pairs and provenance.
- `PROMPTS.md` — the fixed-facts contract and candidate prompts.
- `AUDIT.md` — deterministic checks and the human gate.

## Quick start

```bash
cp -r templates/writers-room <game>/writers-room
node tools/table-draw.mjs --seed <arc-id> --table names --count 3 --filter culture=<culture>
node tools/table-draw.mjs --seed <arc-id> --table premise --count 3
node tools/name-audit.mjs --root <game>
```

Then fill `VOICE.md`, replace the example tables, and write the first scene from fixed facts.
