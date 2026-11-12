#!/usr/bin/env python3
"""Pick names in code, not in the model, inside a world's own naming grammar.

LLMs collapse to a few "safe" names (Elara, Elias, Mira ...). The model should not choose names at all.
Draw them here with a seeded RNG, reject anything on the banlist or too close to one, keep a per-world
registry so nothing repeats, then hand the chosen names to the model as fixed facts.

Without --voice it uses four generic syllable styles. With --voice it uses the repo's own *naming grammar*
(see ../../templates/voice.example.json), the way Tolkien built names out of a language:
the voice file defines the sounds, the compounds, the trades and the quirks of one world.

  python namegen.py person --style river --n 12 --seed 7
  python namegen.py place  --n 8 --seed 7 --registry world.json
  python namegen.py npc    --n 5 --seed 7 --voice ../../templates/voice.example.json --registry world.json

Stdlib only. Deterministic for a given seed, voice file and registry.
"""
import argparse, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- banlist and similarity
def load_banlist(path=None):
    path = path or os.path.join(HERE, "banlist.txt")
    out = set()
    for line in open(path, encoding="utf8"):
        line = line.strip()
        if line and not line.startswith("#"):
            out.add(line.lower())
    return out

def edit1(a, b):
    """True if the two strings are within one edit (insert, delete or substitute)."""
    if abs(len(a) - len(b)) > 1: return False
    if a == b: return True
    i = j = diff = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]: i += 1; j += 1; continue
        diff += 1
        if diff > 1: return False
        if len(a) == len(b): i += 1; j += 1
        elif len(a) > len(b): i += 1
        else: j += 1
    return diff + (len(a) - i) + (len(b) - j) <= 1

def too_close(name, banned):
    low = name.lower()
    return any(edit1(low, b) or low.startswith(b) or b.startswith(low) for b in banned if " " not in b)

# ---------------------------------------------------------------- defaults (used when there is no voice file)
DEFAULT_STYLES = {
    "river": dict(on=["b","d","g","h","j","k","m","n","p","r","s","t","v","z","br","dr","gr","tr","sh"],
                  v=["a","e","i","o","u","ai","ei"], co=["","n","r","l","s","k","m"]),
    "stone": dict(on=["b","d","f","g","h","l","m","n","r","s","t","w","br","gl","th"],
                  v=["a","e","i","o","u"], co=["","d","g","k","n","rd","rn","st","t"]),
    "salt":  dict(on=["k","l","m","n","p","s","t","w","y","ts"],
                  v=["a","e","i","o","u","ia","ao"], co=["","n","k","t","m"]),
    "ash":   dict(on=["c","d","f","j","l","m","n","r","s","v","ch","dh","sl","sn"],
                  v=["a","e","i","o","u","oi","ua"], co=["","m","n","l","d","x","c"]),
}
DEFAULT = dict(
    surname=dict(mode="compound",
                 heads=["Ald","Bram","Cor","Dray","Esk","Fenn","Gorm","Hask","Ing","Jut","Kell","Lorn","Marl","Nev","Orm","Pell","Quill","Rask","Sedge","Tarn","Ull","Wend","Yarr"],
                 tails=["marsh","crake","dun","fell","holt","wick","combe","garth","ley","thwaite","moor","scar","stead","bourne","wald","hurst"]),
    place=dict(heads=["Crake","Dunn","Esk","Fenn","Garr","Hob","Ink","Jarl","Kest","Lorn","Marl","Nett","Orme","Pell","Quarn","Rudd","Sark","Tarr","Ulm","Wend","Yarrow","Brack","Cull","Dray","Fallow","Gorse","Hale","Ing","Kilm","Lund"],
               tails=["ham","ton","by","wick","ford","combe","mere","thwaite","stead","moor","scar","holme","burn","gate","hithe","shaw","stow","wold","ness","pool"],
               kinds=["a tidal salt-works","a tannery town","a quarry village","a canal junction","a market on stilts","a ferry crossing","a mining camp","a monastery orchard","a toll bridge","a beekeepers' hamlet","a brickworks","a drovers' halt"]),
    trades=["ferrier","eel-trapper","net-mender","salt-boiler","bell-founder","chimney sweep","glassblower","beekeeper","tanner","ropewalker","cooper","apothecary's runner","drover","potter","tide-table keeper","lamp-trimmer","cartwright","thatcher","brewer","stonemason's mate"],
    quirks=["counts everything twice","never answers a question the first time it is asked","collects bent nails","hums only when lying","keeps a tally of favours owed","refuses to cross water at dusk","speaks to animals before people","writes with the wrong hand on purpose","will not be photographed or sketched","trades only in odd numbers"],
    wants=["to pay off a debt without anyone learning it exists","to be asked for advice just once","to see a sibling's grave","to keep the shop open one more winter","to be believed about something small","to leave and be talked out of leaving","to finish a job someone else started","to be proven right about a boundary stone"],
)
BAD = ("aaa","eee","iii","ooo","uuu","aoa","oao")
COMMON_WORDS = {"dust","mist","wand","rain","tree","moon","star","fire","sand","dark","rust","bell","salt","ash"}

def pronounceable(n):
    low = n.lower()
    if low in COMMON_WORDS: return False
    v = "aeiouy"; run = 0
    for ch in low:
        run = run + 1 if ch in v else 0
        if run >= 3: return False
    run = 0
    for ch in low:
        run = run + 1 if ch not in v else 0
        if run >= 4: return False
    return not any(b in low for b in BAD)

# ---------------------------------------------------------------- voice file
def load_voice(path):
    """Merge a voice file over the defaults. Missing keys fall back to the defaults."""
    cfg = json.loads(json.dumps(DEFAULT))
    cfg["given"] = None
    cfg["reserved"] = []
    cfg["avoid"] = []
    cfg["max_surname_repeats"] = 1
    if path:
        v = json.load(open(path, encoding="utf8"))
        for k in ("trades", "quirks", "wants", "reserved", "avoid"):
            if k in v: cfg[k] = v[k]
        if "max_surname_repeats" in v: cfg["max_surname_repeats"] = int(v["max_surname_repeats"])
        for k in ("surname", "place"):
            if k in v: cfg[k].update(v[k])
        if "given" in v: cfg["given"] = v["given"]
        cfg["name"] = v.get("name", os.path.basename(path))
    return cfg

def syllable_name(phon, rng, banned):
    syl = phon.get("syllables", [2, 2, 3])
    lo, hi = phon.get("length", [4, 9])
    for _ in range(600):
        n = rng.choice(syl)
        name = ""
        for k in range(n):
            name += rng.choice(phon["on"]) + rng.choice(phon["v"])
            if k == n - 1: name += rng.choice(phon["co"])
        name = name.capitalize()
        if lo <= len(name) <= hi and pronounceable(name) and not too_close(name, banned):
            return name
    raise RuntimeError("could not generate a clean name; loosen the voice file's phonology")

def make_surname(rng, banned, used, cfg):
    s = cfg["surname"]
    for _ in range(400):
        if s.get("mode") == "word":
            w = rng.choice(s["words"]).capitalize()
        else:
            w = rng.choice(s["heads"]).capitalize() + rng.choice(s["tails"])
            w = w[0] + w[1:]
        key = "surname:" + w.lower()
        if too_close(w, banned) or w.lower() in {a.lower() for a in cfg["avoid"]}: continue
        if used_count(used, key) >= cfg["max_surname_repeats"]: continue
        return w, key
    raise RuntimeError("surnames exhausted; raise max_surname_repeats or add more")

# The registry is a list of strings. "given:x", "surname:x" and "place:x" are counted entries.
def used_count(used, key): return sum(1 for u in used if u == key)
def load_registry(path):
    if path and os.path.exists(path):
        return list(json.load(open(path, encoding="utf8")))
    return []
def save_registry(path, used):
    if path:
        json.dump(sorted(used), open(path, "w", encoding="utf8"), indent=2)

def register_reserved(cfg, used):
    """Existing canon goes into the registry first so new names never collide with it.
    "Edda Briar" reserves given 'edda' and surname 'briar'; "place:Greyfen" reserves a place."""
    for r in cfg.get("reserved", []):
        if r.lower().startswith("place:"):
            k = "place:" + r.split(":", 1)[1].strip().lower()
            if k not in used: used.append(k)
            continue
        for part in r.split():
            for kind in ("given", "surname"):
                k = f"{kind}:{part.lower()}"
                if k not in used: used.append(k)

def make_person(rng, banned, used, cfg, style):
    phon = cfg["given"] if cfg.get("given") else dict(DEFAULT_STYLES[style])
    for _ in range(400):
        given = syllable_name(phon, rng, banned)
        gk = "given:" + given.lower()
        if gk in used or given.lower() in {x.lower() for x in cfg["avoid"]}: continue
        last, sk = make_surname(rng, banned, used, cfg)
        used.append(gk); used.append(sk)
        return f"{given} {last}"
    raise RuntimeError("registry exhausted")

def make_place(rng, banned, used, cfg):
    p = cfg["place"]
    for _ in range(400):
        name = rng.choice(p["heads"]).capitalize() + rng.choice(p["tails"])
        k = "place:" + name.lower()
        if k in used or too_close(name, banned): continue
        used.append(k)
        return name, rng.choice(p["kinds"])
    raise RuntimeError("registry exhausted")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", choices=["person", "place", "npc"])
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--style", choices=sorted(DEFAULT_STYLES), default=None, help="generic style (ignored when the voice file defines 'given')")
    ap.add_argument("--voice", help="per-repo voice file (JSON); see templates/voice.example.json")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--registry", help="JSON file of names already used in this world; updated in place")
    ap.add_argument("--banlist")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    banned = load_banlist(a.banlist)
    cfg = load_voice(a.voice)
    used = load_registry(a.registry)
    register_reserved(cfg, used)
    for _ in range(a.n):
      try:
        if a.kind == "place":
            nm, kind = make_place(rng, banned, used, cfg); print(f"{nm}\t{kind}")
        else:
            style = a.style or rng.choice(sorted(DEFAULT_STYLES))
            nm = make_person(rng, banned, used, cfg, style)
            if a.kind == "person": print(nm)
            else: print(f"{nm}\t{rng.choice(cfg['trades'])}\t{rng.choice(cfg['quirks'])}\twants {rng.choice(cfg['wants'])}")
      except RuntimeError as e:
        print(f"stopped early: {e}", file=sys.stderr); save_registry(a.registry, used); sys.exit(2)
    save_registry(a.registry, used)

if __name__ == "__main__":
    main()
