#!/usr/bin/env python3
"""Find overused LLM-default names in your own content.

  python name_audit.py path/to/repo            # human-readable report
  python name_audit.py path/to/repo --json     # machine-readable
  python name_audit.py path/to/repo --max 0    # exit 1 if any hit (use in CI)

Counts whole-word, capitalised hits (so "aria-label" and "sage" the herb are ignored) from banlist.txt in text files (md, txt, json, js, ts, tsx, py, gd, yml).
Skips node_modules, build output and lock files. Stdlib only.
"""
import argparse, collections, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EXT = {".md", ".txt", ".json", ".js", ".ts", ".tsx", ".py", ".gd", ".yml", ".yaml", ".html"}
SKIP = {"node_modules", ".git", "dist", "build", ".next", "public", "web-dist", "__pycache__"}

def banlist(path):
    return [l.strip() for l in open(path, encoding="utf8") if l.strip() and not l.startswith("#")]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("--banlist", default=os.path.join(HERE, "banlist.txt"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--max", type=int, default=None, help="fail (exit 1) if total hits exceed this")
    a = ap.parse_args()
    words = banlist(a.banlist)
    # Capitalised, whole-word, not part of a hyphenated token (so "aria-label" is not "Aria").
    caps = [" ".join(p.capitalize() for p in w.split()) for w in words]
    pat = re.compile(r"(?<![\w-])(" + "|".join(re.escape(w) for w in sorted(caps, key=len, reverse=True)) + r")(?![\w-])")
    total = collections.Counter(); files = collections.defaultdict(set)
    for d, dirs, fs in os.walk(a.root):
        dirs[:] = [x for x in dirs if x not in SKIP]
        for f in fs:
            if os.path.splitext(f)[1].lower() not in EXT or f.endswith("lock.json"): continue
            p = os.path.join(d, f)
            try: txt = open(p, encoding="utf8", errors="ignore").read()
            except OSError: continue
            for m in pat.finditer(txt):
                total[m.group(1)] += 1; files[m.group(1)].add(os.path.relpath(p, a.root))
    hits = sum(total.values())
    if a.json:
        print(json.dumps({"hits": hits, "names": {k: {"count": v, "files": len(files[k])} for k, v in total.most_common()}}, indent=2))
    else:
        print(f"{hits} hits across {len(total)} banlisted names")
        for k, v in total.most_common(25): print(f"  {k:<14} {v:>5} in {len(files[k]):>3} files")
    if a.max is not None and hits > a.max: sys.exit(1)

if __name__ == "__main__":
    main()
