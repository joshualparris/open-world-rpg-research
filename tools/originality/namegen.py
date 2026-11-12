#!/usr/bin/env python3
"""Pick names in code, not in the model.

LLMs collapse to a few "safe" names (Elara, Elias, Mira ...). The model should not choose names at all:
draw them here with a seeded RNG, reject anything on the banlist or too close to one, keep a per-world
registry so nothing repeats, then hand the chosen names to the model as fixed facts.

  python namegen.py person --style river --n 12 --seed 7
  python namegen.py place --n 8 --seed 7 --registry world.json
  python namegen.py npc --n 5 --seed 7            # name + trade + quirk + want

Stdlib only. Deterministic for a given seed and registry.
"""
import argparse, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))

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

# Syllable styles: onset + vowel (+ coda on the last syllable). Always 2-3 syllables so names look like names,
# and pronounceability is enforced below. Deliberately varied; none are tuned to resemble usual LLM output.
STYLES = {
    "river": dict(on=["b","d","g","h","j","k","m","n","p","r","s","t","v","z","br","dr","gr","tr","sh"],
                  v=["a","e","i","o","u","ai","ei"], co=["","n","r","l","s","k","m"]),
    "stone": dict(on=["b","d","f","g","h","l","m","n","r","s","t","w","br","gl","th"],
                  v=["a","e","i","o","u"], co=["","d","g","k","n","rd","rn","st","t"]),
    "salt":  dict(on=["k","l","m","n","p","s","t","w","y","ts"],
                  v=["a","e","i","o","u","ia","ao"], co=["","n","k","t","m"]),
    "ash":   dict(on=["c","d","f","j","l","m","n","r","s","v","ch","dh","sl","sn"],
                  v=["a","e","i","o","u","oi","ua"], co=["","m","n","l","d","x","c"]),
}
BAD = ("aaa","eee","iii","ooo","uuu","aoa","oao")
COMMON_WORDS = {"dust","mist","wand","rain","tree","moon","star","fire","sand","dark","rust","bell","salt","ash"}

def pronounceable(n):
    low = n.lower()
    if low in COMMON_WORDS: return False
    vowels = "aeiouy"
    run = 0
    for ch in low:
        run = run + 1 if ch in vowels else 0
        if run >= 3: return False
    run = 0
    for ch in low:
        run = run + 1 if ch not in vowels else 0
        if run >= 4: return False
    return not any(b in low for b in BAD)

SURNAME_BITS = ["marsh","crake","dun","fell","holt","wick","combe","garth","ley","thwaite","moor","scar","stead","bourne","wald","hurst"]
SURNAME_HEADS = ["Ald","Bram","Cor","Dray","Esk","Fenn","Gorm","Hask","Ing","Jut","Kell","Lorn","Marl","Nev","Orm","Pell","Quill","Rask","Sedge","Tarn","Ull","Wend","Yarr"]
PLACE_HEADS = ["Crake","Dunn","Esk","Fenn","Garr","Hob","Ink","Jarl","Kest","Lorn","Marl","Nett","Orme","Pell","Quarn","Rudd","Sark","Tarr","Ulm","Wend","Yarrow","Brack","Cull","Dray","Fallow","Gorse","Hale","Ing","Kilm","Lund"]
PLACE_TAILS = ["ham","ton","by","wick","ford","combe","mere","thwaite","stead","moor","scar","holme","burn","gate","hithe","shaw","stow","wold","ness","pool"]
PLACE_KINDS = ["a tidal salt-works","a tannery town","a quarry village","a canal junction","a market on stilts","a ferry crossing","a mining camp","a monastery orchard","a toll bridge","a beekeepers' hamlet","a brickworks","a drovers' halt"]
TRADES = ["ferrier","eel-trapper","net-mender","salt-boiler","bell-founder","chimney sweep","glassblower","beekeeper","tanner","ropewalker","cooper","apothecary's runner","drover","potter","tide-table keeper","lamp-trimmer","cartwright","thatcher","brewer","stonemason's mate"]
QUIRKS = ["counts everything twice","never answers a question the first time it is asked","collects bent nails","hums only when lying","keeps a tally of favours owed","refuses to cross water at dusk","speaks to animals before people","writes with the wrong hand on purpose","will not be photographed or sketched","trades only in odd numbers"]
WANTS = ["to pay off a debt without anyone learning it exists","to be asked for advice just once","to see a sibling's grave","to keep the shop open one more winter","to be believed about something small","to leave and be talked out of leaving","to finish a job someone else started","to be proven right about a boundary stone"]

def syllable_name(style, rng, banned):
    s = STYLES[style]
    for _ in range(400):
        n = rng.choice([2, 2, 3])
        name = ""
        for k in range(n):
            name += rng.choice(s["on"]) + rng.choice(s["v"])
            if k == n - 1: name += rng.choice(s["co"])
        name = name.capitalize()
        if 4 <= len(name) <= 9 and pronounceable(name) and not too_close(name, banned):
            return name
    raise RuntimeError("could not generate a clean name")

def too_close(name, banned):
    low = name.lower()
    return any(edit1(low, b) or low.startswith(b) or b.startswith(low) for b in banned if " " not in b)

def load_registry(path):
    if path and os.path.exists(path):
        return set(json.load(open(path, encoding="utf8")))
    return set()

def save_registry(path, used):
    if path:
        json.dump(sorted(used), open(path, "w", encoding="utf8"), indent=2)

def make_person(rng, banned, used, style):
    for _ in range(200):
        first = syllable_name(style, rng, banned)
        last = rng.choice(SURNAME_HEADS) + rng.choice(SURNAME_BITS)
        full = f"{first} {last.capitalize() if last[0].islower() else last}"
        if first.lower() in used or too_close(last, banned): continue
        used.add(first.lower()); return full
    raise RuntimeError("registry exhausted")

def make_place(rng, banned, used):
    for _ in range(200):
        name = rng.choice(PLACE_HEADS) + rng.choice(PLACE_TAILS)
        if name.lower() in used or too_close(name, banned): continue
        used.add(name.lower()); return name, rng.choice(PLACE_KINDS)
    raise RuntimeError("registry exhausted")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", choices=["person", "place", "npc"])
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--style", choices=sorted(STYLES), default=None, help="default: a different style per name")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--registry", help="JSON file of names already used in this world; updated in place")
    ap.add_argument("--banlist")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    banned = load_banlist(a.banlist)
    used = load_registry(a.registry)
    for _ in range(a.n):
        if a.kind == "place":
            nm, kind = make_place(rng, banned, used); print(f"{nm}\t{kind}")
        else:
            style = a.style or rng.choice(sorted(STYLES))
            nm = make_person(rng, banned, used, style)
            if a.kind == "person": print(nm)
            else: print(f"{nm}\t{rng.choice(TRADES)}\t{rng.choice(QUIRKS)}\twants {rng.choice(WANTS)}")
    save_registry(a.registry, used)

if __name__ == "__main__":
    main()
