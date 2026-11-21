#!/usr/bin/env python3
"""Remove document control, approval, change history, contents and section
links from every document in the set, then renumber sections and tables and
shift the cross-references that point at them.

Run once from the repository root: python3 tools/strip_control.py
Prints references it could not resolve (to a removed section or table).
"""
import glob
import re
import sys

SKIP = {"README.md"}
files = sorted(f for f in glob.glob("*.md") if f not in SKIP)
names = {f[:-3]: f for f in files}

texts = {f: open(f, encoding="utf-8").read() for f in files}

# Tables removed with section 1, per document.
k_tables = {}
for f, t in texts.items():
    m = re.search(r"^## 1 Document control$(.*?)^## 2 ", t, re.M | re.S)
    k_tables[f] = len({c for c in re.findall(r"\*\*Table (\d+)", m.group(1))}) if m else 0
has_dc = {f: k_tables[f] > 0 for f in files}

flags = []

DOC_RE = re.compile(r"\\<([^>\\]+)\\>|\[([^\]]+)\]\(([^)#]+?)\.md\)")


def target_doc(f, line, start):
    """The document a reference at line[start:] points to."""
    seg = line[:start]
    cut = max(seg.rfind("|"), seg.rfind(". "), seg.rfind("; "))
    seg = seg[cut + 1:]
    found = None
    for m in DOC_RE.finditer(seg):
        n = m.group(1) or m.group(2)
        n = n.replace("%20", " ")
        if n in names:
            found = names[n]
    return found or f


NUMLIST = r"\d+(?:\.\d+)*(?:(?:, | and | to | or )\d+(?:\.\d+)*)*"
SEC_RE = re.compile(r"\b([Ss]ections?) (" + NUMLIST + r")\b")
TAB_RE = re.compile(r"\b([Tt]ables?) (\d+[a-z]?(?:(?:, | and | to | or )\d+[a-z]?)*)\b")


def shift_line(f, line, lineno):
    def sec(m):
        after = line[m.end():m.end() + 12]
        before = line[max(0, m.start() - 14):m.start()]
        if after.startswith(" of the") or "800-63" in before or "Act 20" in before:
            return m.group(0)
        tgt = target_doc(f, line, m.start())
        if not has_dc.get(tgt):
            return m.group(0)

        def one(n):
            parts = n.group(0).split(".")
            v = int(parts[0]) - 1
            if v < 1:
                flags.append((f, lineno, "section " + n.group(0), line.strip()[:140]))
            parts[0] = str(v)
            return ".".join(parts)
        return m.group(1) + " " + re.sub(r"\d+(?:\.\d+)*", one, m.group(2))

    def tab(m):
        tgt = target_doc(f, line, m.start())
        k = k_tables.get(tgt, 0)
        if not k:
            return m.group(0)

        def one(n):
            v = int(n.group(1)) - k
            if v < 1:
                flags.append((f, lineno, "table " + n.group(0) + " -> " + tgt, line.strip()[:140]))
            return str(v) + n.group(2)
        return m.group(1) + " " + re.sub(r"(\d+)([a-z]?)", one, m.group(2))

    line = SEC_RE.sub(sec, line)
    line = TAB_RE.sub(tab, line)
    return line


for f in files:
    t = texts[f]
    # status line under the title
    t = re.sub(r"^\*\*\\<ref\\> \| Version [^\n]*\*\*\n\n", "", t, count=1, flags=re.M)
    # contents block
    t = re.sub(r"^\*\*Contents\*\*\n(?:\n|(?:\[[^\]]*\]\(#[^)]*\)(?: · )?)+\n)*", "", t, flags=re.M)
    # banners
    t = re.sub(r"^\| \*\*(?:SECTION|APPENDIX|CHAPTER|PART)[^*]*\*\* \|\n\| --- \|\n\n?", "", t, flags=re.M)
    # chapter navigation lines
    t = re.sub(r"^(?:\[[^\]]*\]\(#[^)]*\)(?: · )?)+\n\n?", "", t, flags=re.M)
    # section 1
    if has_dc[f]:
        m = re.search(r"^## 1 Document control$.*?(?=^## 2 )", t, re.M | re.S)
        keep = ""
        dp = re.search(r"^### 1\.\d+ Distribution and protection\n(.*?)(?=^##|\Z)", m.group(0), re.M | re.S)
        if dp:
            keep = dp.group(1).strip()
        t = t[:m.start()] + t[m.end():]
        if keep:
            # put it at the end of the new section 1 (old section 2)
            m3 = re.search(r"^## 3 ", t, re.M)
            subs = re.findall(r"^### 2\.(\d+) ", t[:m3.start()], re.M)
            n = max([int(s) for s in subs] or [0]) + 1
            keep = keep.replace(", with the change history", ", with a note of what changed")
            t = t[:m3.start()] + "### 2.%d Distribution and protection\n\n%s\n\n" % (n, keep) + t[m3.start():]
    # remaining in-document links become plain text
    t = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", t)
    # cross-document links lose their anchor
    t = re.sub(r"\]\(([^)#]+?\.md)#[^)]*\)", r"](\1)", t)

    out = []
    for i, line in enumerate(t.split("\n"), 1):
        if has_dc[f]:
            h = re.match(r"^(#{2,6}) (\d+)((?:\.\d+)*) ", line)
            if h:
                line = "%s %d%s " % (h.group(1), int(h.group(2)) - 1, h.group(3)) + line[h.end():]
                out.append(shift_line(f, line[:h.end()], i) if False else line)
                continue
        out.append(shift_line(f, line, i))
    t = "\n".join(out)
    t = re.sub(r"\n{3,}", "\n\n", t)
    texts[f] = t

for f, t in texts.items():
    open(f, "w", encoding="utf-8").write(t)

for fl in flags:
    print("%s:%d  %s  ||  %s" % fl)
print(len(flags), "unresolved", file=sys.stderr)
