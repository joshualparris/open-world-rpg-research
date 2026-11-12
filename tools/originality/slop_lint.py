#!/usr/bin/env python3
"""Find "AI slop" in prose: stock words, stock phrases, stock structures, and repetition.

  python slop_lint.py story.md chapters/              # report
  python slop_lint.py content/ --json                  # machine-readable
  python slop_lint.py content/ --max-score 12          # exit 1 if any file scores above 12 (CI gate)
  python slop_lint.py content/ --voice voice.json      # also read a per-repo "banned" list from the voice file
  python slop_lint.py client/src/game --code-strings    # game content lives in code: lint long string literals in .ts/.tsx/.js/.json
  python slop_lint.py content/ --patterns my.json      # extend/override the built-in patterns

HOW TO USE THE RESULT
  * It is a QUALITY CHECK for your own output, not a detector. Do not use it to accuse anyone of using AI:
    detectors of this kind misfire (they flagged most non-native English essays in one study).
  * The score is a heuristic. The thresholds (below 5 fine, 5-15 watch, above 15 revise) are NOT validated;
    tune them on text you consider good.
  * Feed the findings to an editor pass as EXTERNAL feedback ("these 7 spots; rewrite them concretely").
    Models correct themselves poorly without outside feedback.
  * Sentence-length variation is reported as advisory only: studies disagree on whether it separates machine
    from human prose, so it is not scored.

Categories and the sources they come from are listed in ANTISLOP.md. Stdlib only.
"""
import argparse, collections, json, os, re, sys

# ------------------------------------------------------------------ built-in patterns (edit freely)
WORDS = [  # stock "AI" vocabulary: over-represented in LLM output vs earlier human text (Kobak 2024, Antislop 2025, practitioner lists)
    "delve", "delves", "delving", "tapestry", "testament", "underscore", "underscores", "underscoring", "showcase", "showcases",
    "showcasing", "pivotal", "crucial", "intricate", "nuanced", "multifaceted", "realm", "beacon", "symphony", "kaleidoscope",
    "labyrinth", "myriad", "bustling", "vibrant", "ethereal", "palpable", "shimmering", "dappled", "ozone", "petrichor",
    "embark", "foster", "fostering", "leverage", "navigate", "navigating", "interplay", "resonate", "resonates", "unwavering",
    "relentless", "tantalizing", "visceral", "ineffable", "whispers", "echoes",
]
PHRASES = {  # phrase / construction -> regex (case-insensitive)
    "a testament to": r"\ba testament to\b",
    "couldn't help but": r"\bcouldn'?t help but\b",
    "a mix/mixture of X and Y": r"\ba (?:mix|mixture|blend) of \w+ and \w+\b",
    "sense of": r"\ba (?:sense|wave|surge|flicker|pang) of \w+",
    "something shifted/changed": r"\bsomething (?:shifted|changed|stirred|flickered) (?:in|behind|within)\b",
    "let out a breath": r"\b(?:let out|released|exhaled) a breath (?:he|she|they|I) (?:didn'?t|hadn'?t) (?:know|realize)",
    "eyes sparkle/twinkle": r"\beyes (?:sparkled|twinkled|glinted|gleamed|danced)\b",
    "heart hammered/raced": r"\b(?:heart|pulse) (?:hammered|pounded|raced|thundered|skipped)\b",
    "shiver down spine": r"\bshiver(?:ed)? (?:ran |went )?down (?:his|her|their|my) spine\b",
    "knuckles white": r"\bknuckles (?:white|whitened|turned white)\b",
    "silence stretched/hung": r"\bsilence (?:stretched|hung|settled|pressed)\b",
    "air thick/heavy with": r"\bair (?:was )?(?:thick|heavy|charged) with\b",
    "dance of": r"\b(?:a|the) (?:delicate |intricate |complex )?dance of\b",
    "whispers of": r"\bwhispers? of\b",
    "in the end / in conclusion": r"\b(?:in conclusion|in summary|ultimately,|in the end,)\b",
    "it's important to note": r"\b(?:it'?s|it is) (?:important|worth) (?:to note|noting)\b",
}
STRUCTURES = {  # structural tells; each is (regex, description, hint)
    "negative_parallelism": (
        r"\b(?:it|this|that|she|he|they|[A-Z]\w+)(?:'s| is| was| are| were)?(?: not|n['’]t) (?:just |only |merely |simply )?[^.!?;:\n]{1,70}?(?:,|;| -|—)\s*(?:but |it'?s |it is |it was |he'?s |she'?s |they'?re |rather |more )"
        r"|\bnot (?:just|only|merely|simply) [^.!?\n]{1,70}?,? but (?:also )?\b"
        r"|\b(?:it|this|that|she|he|they)(?:'s| is| was| are| were)?(?: not|n['’]t) (?:\w+ ){1,5}but (?:a|an|the|rather)\b"
        r"|\bnot (?:just|only|merely|simply) [^.!?\n]{1,70}?,\s*(?:it|this|that|he|she|they)\b"
        r"|\b(?:isn['’]t|wasn['’]t|aren['’]t|weren['’]t) [^.!?\n]{1,60}[.!?]\s+(?:It|This|That|He|She|They)(?:'s| is| was| are)\b",
        "'not X, but Y' framing", "State the thing directly; keep one clause."),
    "participial_significance": (
        r",\s*(?:highlighting|underscoring|showcasing|reflecting|symbolizing|emphasizing|demonstrating|illustrating|reinforcing)\b",
        "tacked-on significance clause", "Cut it, or show the consequence in a later action."),
    "rule_of_three": (
        r"\b\w+, \w+,? and \w+\b",
        "habitual triplet", "Use two, or four, or one exact item."),
    "paragraph_aphorism": (
        r"(?m)(?:^|[.!?]\s)(?:And so|In the end|Perhaps|Maybe|Somewhere|Always|Together|After all)[^.!?\n]{0,90}[.!?]\s*$",
        "tidy closing aphorism", "End on a concrete image or an action, not a moral."),
}
WEIGHTS = {"words": 1.0, "phrases": 3.0, "negative_parallelism": 4.0, "participial_significance": 3.0,
           "rule_of_three": 0.5, "paragraph_aphorism": 3.0, "em_dash_excess": 1.0, "repeated_openers": 2.0, "repeated_trigrams": 1.5}
EM_DASH_OK_PER_1000 = 3.0   # more than this many per 1000 words counts toward the score
FIX_HINTS = {
    "words": "Replace with the plain, specific word a person in this world would say.",
    "phrases": "Describe what the character actually does or perceives instead of the stock beat.",
}

def clean(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)       # front matter
    text = re.sub(r"```.*?```", " ", text, flags=re.S)             # code
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)            # links
    text = re.sub(r"(?m)^\s*#+ .*$", "", text)                      # headings are labels, not prose
    text = re.sub(r"(?m)^\s*\|.*\|\s*$", "", text)                   # table rows
    text = re.sub(r"(?m)^\s*(?:>|[-*+]|\d+\.)\s+", "", text)       # list / quote markers
    text = re.sub(r"\*\*[^*\n]{1,40}:\*\*", "", text)                  # **Label:** fragments
    text = re.sub(r"(?m)^\s*[A-Z][A-Za-z/ ]{1,24}: ", "", text)          # leading "Label: " (metadata or speaker tags)
    return text

def load_patterns(path, voice):
    words, phrases, structures, weights = list(WORDS), dict(PHRASES), dict(STRUCTURES), dict(WEIGHTS)
    if path:
        extra = json.load(open(path, encoding="utf8"))
        words += extra.get("words", [])
        phrases.update(extra.get("phrases", {}))
        weights.update(extra.get("weights", {}))
    if voice:
        v = json.load(open(voice, encoding="utf8"))
        words += v.get("banned_words", [])
        phrases.update({p: re.escape(p) for p in v.get("banned_phrases", [])})
    return sorted(set(w.lower() for w in words)), phrases, structures, weights

def lint_text(text, patterns):
    words, phrases, structures, weights = patterns
    body = clean(text)
    toks = re.findall(r"[A-Za-z']+", body)
    n = max(len(toks), 1)
    per = 1000.0 / n
    findings = []   # (category, label, line, snippet)
    lines = body.split("\n")
    def add(cat, label, m):
        line = body.count("\n", 0, m.start()) + 1
        findings.append((cat, label, line, body[max(0, m.start() - 25): m.end() + 25].replace("\n", " ")))
    wordre = re.compile(r"\b(" + "|".join(re.escape(w) for w in words) + r")\b", re.I) if words else None
    counts = collections.Counter()
    if wordre:
        for m in wordre.finditer(body):
            counts["words"] += 1; add("words", m.group(1).lower(), m)
    for label, rx in phrases.items():
        for m in re.finditer(rx, body, re.I):
            counts["phrases"] += 1; add("phrases", label, m)
    for cat, (rx, desc, hint) in structures.items():
        for m in re.finditer(rx, body, re.I if cat != "negative_parallelism" else re.I):
            counts[cat] += 1; add(cat, desc, m)
    em = body.count("—") + len(re.findall(r" -- ", body))
    em_rate = em * per
    counts["em_dash_excess"] = max(0.0, em_rate - EM_DASH_OK_PER_1000) / per if per else 0
    # repeated sentence openers (3+ in a row starting with the same word)
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()]
    firsts = [re.match(r"[\"'“]?(\w+)", s).group(1).lower() if re.match(r"[\"'“]?(\w+)", s) else "" for s in sents]
    run = 1; rep = 0
    for i in range(1, len(firsts)):
        run = run + 1 if firsts[i] and firsts[i] == firsts[i - 1] else 1
        if run == 3: rep += 1
    counts["repeated_openers"] = rep
    # repeated trigrams (4+ occurrences)
    low = [t.lower() for t in toks]
    tri = collections.Counter(zip(low, low[1:], low[2:]))
    stop = {("i", "don't", "know"), ("one", "of", "the"), ("a", "lot", "of")}
    rep_list = [(t, c) for t, c in tri.items() if c >= 4 and t not in stop]
    counts["repeated_trigrams"] = len(rep_list)
    for t, c in sorted(rep_list, key=lambda x: -x[1])[:5]:
        findings.append(("repeated_trigrams", f"\"{' '.join(t)}\" x{c}", 0, "phrase repeats; vary the wording or cut"))
    # advisory only
    lens = [len(re.findall(r"[A-Za-z']+", s)) for s in sents if s]
    mean = sum(lens) / len(lens) if lens else 0
    cv = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5 / mean if mean else 0
    window = 200
    mattr = None
    if len(low) >= window:
        vals = [len(set(low[i:i + window])) / window for i in range(0, len(low) - window + 1, 20)]
        mattr = sum(vals) / len(vals)
    score = 0.0
    for k, c in counts.items():
        score += weights.get(k, 1.0) * c * per
    return dict(words=len(toks), score=round(score, 2), counts={k: round(v, 2) if isinstance(v, float) else v for k, v in counts.items()},
                em_dash_per_1000=round(em_rate, 1), sentence_len_cv=round(cv, 2), lexical_diversity_mattr200=round(mattr, 3) if mattr else None,
                findings=findings)

STRING_RE = re.compile(r'"((?:[^"\\\n]|\\.){30,})"|\'((?:[^\'\\\n]|\\.){30,})\'|`((?:[^`\\]|\\.){30,})`')
def code_strings(text):
    """Pull long string literals out of source code so dialogue and descriptions can be linted as prose."""
    out = []
    for m in STRING_RE.finditer(text):
        t = next(g for g in m.groups() if g)
        if re.search(r"[A-Za-z]{3,} [A-Za-z]{3,}", t) and "://" not in t and "className" not in t:
            out.append(t.replace("\\n", "\n").replace("\\'", "'").replace('\\"', '"'))
    return "\n\n".join(out)

def iter_files(paths, code=False):
    for p in paths:
        if os.path.isdir(p):
            for d, dirs, fs in os.walk(p):
                dirs[:] = [x for x in dirs if x not in {"node_modules", ".git", "dist", "build"}]
                for f in sorted(fs):
                    ext = os.path.splitext(f)[1].lower()
                    if ext in {".md", ".txt"} or (code and ext in {".ts", ".tsx", ".js", ".json"} and not f.endswith("lock.json") and not f.endswith(".d.ts")):
                        yield os.path.join(d, f)
        else:
            yield p

def verdict(score, warn=5.0, bad=15.0):
    return "revise" if score > bad else "watch" if score > warn else "ok"

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--patterns"); ap.add_argument("--voice")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--top", type=int, default=6, help="findings to show per file")
    ap.add_argument("--code-strings", action="store_true", help="also lint long string literals in .ts/.tsx/.js/.json files")
    ap.add_argument("--min-words", type=int, default=120, help="skip very short files (scores are noisy)")
    ap.add_argument("--max-score", type=float, default=None, help="exit 1 if any file scores above this")
    a = ap.parse_args()
    pats = load_patterns(a.patterns, a.voice)
    results = []; worst = 0.0
    for f in iter_files(a.paths, a.code_strings):
        try: text = open(f, encoding="utf8", errors="ignore").read()
        except OSError: continue
        if os.path.splitext(f)[1].lower() in {".ts", ".tsx", ".js", ".json"}: text = code_strings(text)
        r = lint_text(text, pats)
        if r["words"] < a.min_words: continue
        r["file"] = f; r["verdict"] = verdict(r["score"]); results.append(r); worst = max(worst, r["score"])
    results.sort(key=lambda r: -r["score"])
    if a.json:
        print(json.dumps([{k: v for k, v in r.items() if k != "findings"} | {"findings": [list(x) for x in r["findings"][:40]]} for r in results], indent=2))
    else:
        for r in results:
            print(f"{r['score']:>6.1f}  {r['verdict']:<6} {r['words']:>6}w  {r['file']}")
            c = {k: v for k, v in r["counts"].items() if v}
            if c: print("        " + ", ".join(f"{k}={v}" for k, v in c.items()) + f" | em-dash/1k={r['em_dash_per_1000']} | sentence-length CV={r['sentence_len_cv']} (advisory)")
            for cat, label, line, snip in r["findings"][: a.top]:
                print(f"        L{line:<4} [{cat}] {label}: ...{snip}...")
        if results:
            avg = sum(r["score"] for r in results) / len(results)
            print(f"\n{len(results)} files, mean score {avg:.1f}, worst {worst:.1f}  (ok<=5, watch<=15, revise>15; heuristic thresholds)")
    if a.max_score is not None and worst > a.max_score: sys.exit(1)

if __name__ == "__main__":
    main()
