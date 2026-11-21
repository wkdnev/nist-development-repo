#!/usr/bin/env python3
"""Replace every reference to a NIST standard with CSS (Cyber Security Standards)."""
import glob, re
REV = r"(?:,? (?:Rev(?:ision)?\.? ?\d+|Part \d+|Volume I+|Vol\. ?\d+))*"
STD = re.compile(
    r"\bNIST(?:'s)? (?:Special Publication |SP |IR |NISTIR )?800-\d+[A-Z]?" + REV +
    r"|\b(?:SP |NISTIR |Special Publication )?800-\d+[A-Z]?" + REV +
    r"|\bFIPS(?: PUB)? \d+(?:-\d)?" +
    r"|\bNIST(?:'s)? (?:SSDF|CSF|Cybersecurity Framework|Privacy Framework|Secure Software Development Framework)" +
    r"|\bSSDF\b")
for f in sorted(glob.glob("*.md")) + ["tools/ALIGNMENT_GUIDE.md"]:
    t = open(f, encoding="utf-8").read(); o = t
    t = re.sub(r"\[([^\]]*)\]\(https?://[^)]*nist\.gov[^)]*\)", r"\1", t)
    t = STD.sub("CSS", t)
    t = re.sub(r"(^|\| |[.:!?] |\n- |\(|\*\*)NIST's ", lambda m: m.group(1) + "The CSS ", t, flags=re.M)
    t = t.replace("NIST's ", "the CSS ")
    t = re.sub(r"\bNIST\b", "CSS", t)
    for _ in range(3):
        t = re.sub(r"\bCSS(?:,| and| or|/| \+)? CSS\b", "CSS", t)
        t = re.sub(r"\bCSS \(CSS\)", "CSS", t)
    t = t.replace("the the CSS", "the CSS").replace("The the CSS", "The CSS")
    if t != o:
        open(f, "w", encoding="utf-8").write(t); print(f)
