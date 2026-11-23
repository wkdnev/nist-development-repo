#!/usr/bin/env python3
"""Test-PlanConsistency: the automatic check on the document set.

Reads every Markdown document in the set and confirms that the documents agree
with each other: the totals in the plan, the assessment record and the report,
the identifiers each document cites, the links and section references between
documents, and the count of facts still to be supplied
(<Documentation Map>, section 4.11; <Planning Management>, section 3.4).

It runs on the documents only and changes nothing. A gap it reports is a real
inconsistency, to be corrected in the documents.

Usage:
    python tools/Test-PlanConsistency.py [--root PATH] [--census] [--verbose]

Exit code 0 when every check passes, 1 otherwise. --census prints the count of
placeholders by who is expected to supply them, as used in
<Plan of Action and Milestones>, section 5.7.
"""
import argparse
import collections
import os
import re
import sys

FAMILIES = "AC AT AU CA CM CP IA IR MA MP PE PL PS PT RA SA SC SI SR".split()
EXPECTED_DOCUMENTS = 42
EXPECTED_CONTROLS = 316
EXPECTED_INHERITED = 62
# Angle-bracket names that are placeholders, not documents
NON_DOCUMENTS = {"System Name", "Organisation", "Code", "Classification", "evidence",
                 "ver", "Name", "Date", "Document Name", "ref"}


# ----------------------------------------------------------------- reading
class DocSet:
    def __init__(self, root):
        self.root = root
        self.docs = {}
        for name in sorted(os.listdir(root)):
            if name.endswith(".md") and name != "README.md":
                with open(os.path.join(root, name), encoding="utf-8") as fh:
                    self.docs[name[:-3]] = fh.read()

    def text(self, name):
        return self.docs[name]

    def lines(self, name):
        return self.docs[name].split("\n")

    def headings(self, name):
        out = set()
        for line in self.lines(name):
            m = re.match(r"^#{2,4} ((?:[A-Z]{2}\.)?\d+(?:\.\d+)*) ", line)
            if m:
                out.add(m.group(1))
        return out

    def tables(self, name):
        return set(re.findall(r"^\*\*Table ([A-Z]{0,2}-?\d+[a-z]?):", self.docs[name], re.M))


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def norm_control(text):
    text = text.replace("\\", "").strip().rstrip(",")
    m = re.match(r"([A-Z]{2})-(\d+)(?:\((\d+)\))?", text)
    if not m:
        return None
    fam, num, enh = m.groups()
    return f"{fam}-{int(num)}" + (f"({int(enh)})" if enh else "")


def rows_starting(lines, pattern, ncells=None):
    out = []
    for line in lines:
        if re.match(pattern, line):
            c = cells(line)
            if ncells is None or len(c) == ncells:
                out.append(c)
    return out


def fmt(n):
    return f"{n:,}"


# ------------------------------------------------------------- the models
def ssp_controls(ds):
    """Control lines of <System Security Plan>, section 7."""
    out = collections.OrderedDict()
    text = ds.text("System Security Plan")
    sec7 = text.split("## 7 Control implementation", 1)[1].split("## 8 ", 1)[0]
    for line in sec7.split("\n"):
        if not re.match(r"^\| [A-Z]{2}-\d", line):
            continue
        c = cells(line)
        if len(c) != 6:
            continue
        ids = re.findall(r"[A-Z]{2}-\d+(?:\(\d+\))?", c[0].split(" ")[0] if not c[0].startswith("PT-5(2)") else c[0])
        if c[0].startswith("PT-5(2)"):
            ids = re.findall(r"PT-\d+(?:\(\d+\))?", c[0])
        for cid in ids:
            out[norm_control(cid)] = dict(type=c[3], status=c[4], gap=c[5])
    return out


def nc_register(ds):
    out = collections.OrderedDict()
    for c in rows_starting(ds.lines("Risk List"), r"^\| NC-[A-Z]{2}-\d", 10):
        out[c[0]] = dict(family=c[1], control=norm_control(c[2]), text=c[3],
                         cause={x.strip() for x in c[4].split(",")}, risks=c[5],
                         rating=c[6], poam=c[9])
    return out


def risk_register(ds):
    out = collections.OrderedDict()
    for c in rows_starting(ds.lines("Risk List"), r"^\| R-[A-Z]{2}-\d", 13):
        out[c[0]] = dict(rating=c[6], treatment=c[7], poam=c[10], status=c[11])
    return out


def car_model(ds):
    """Findings per chapter of <Control Assessment Record>."""
    lines = ds.lines("Control Assessment Record")
    chapters = collections.OrderedDict()
    x1 = []
    fam = None
    for i, line in enumerate(lines):
        m = re.match(r"^## ([A-Z]{2}) ", line)
        if m:
            fam = m.group(1)
            chapters[fam] = dict(statements=[], controls=collections.OrderedDict(), lines=[])
        if line.startswith("| XX-01"):
            x1.append(cells(line))
        if fam:
            chapters[fam]["lines"].append(line)
            m = re.match(r"^\| ([A-Z]{2}-\d[^|]*?) \| [^|]* \| ([A-Z/-]+|\\\[Finding\\\]) \| (.*) \|$", line)
            if m:
                chapters[fam]["statements"].append((m.group(1), m.group(2), m.group(3)))
            m = re.match(r"^\| ([A-Z]{2}-\d+(?:\(\d+\))?) \| (Satisfied|Not applicable|Other than satisfied|\\\[Result\\\]) \| (\S+) of (\S+) \|", line)
            if m:
                chapters[fam]["controls"][m.group(1)] = (m.group(2), m.group(3), m.group(4))
    return chapters, x1


def car_counts(chapters, x1):
    counts = collections.OrderedDict()
    for i, fam in enumerate(FAMILIES):
        c = collections.Counter(s[1] for s in chapters[fam]["statements"])
        for row in x1:
            c[row[2 + i]] += 1
        counts[fam] = c
    return counts


# ------------------------------------------------------------ placeholders
PLACEHOLDER = re.compile(r"\\\[(.*?)\\\]")


def placeholders(ds):
    """Every square-bracket placeholder that marks a fact to be supplied.

    Statement identifiers such as \\[01\\] and the empty finding cells \\[ \\]
    are not facts and are left out."""
    out = []
    for doc, text in ds.docs.items():
        for lineno, line in enumerate(text.split("\n"), 1):
            for m in PLACEHOLDER.finditer(line):
                inner = m.group(1)
                if re.fullmatch(r"\d+|\s*|[a-z]", inner):
                    continue
                out.append((doc, lineno, inner, line))
    return out


SUPPLIERS = [
    ("Decision makers", "The decision, name and date of each approval and decision, and the sign-off sheets"),
    ("Legal adviser", "The lawful bases, special category and criminal offence conditions, retention periods with the business owner, and the impact assessment's scores, advice and sign-off"),
    ("Business owner", "The information types and their ratings, hours of service, numbers of users and items, and each schema's Data Owner"),
    ("System owner", "The people in each role, their deputies and contacts, the milestone dates, and the business values the system owner sets"),
    ("\\<Organisation\\>", "The values, services, names and evidence \\<Organisation\\> provides"),
    ("Developers and administrators at build", "Names, versions, counts, hashes, suppliers and settings recorded when the VMs are built and the components chosen"),
    ("Assessors and the authorising official", "The assessors' names, the assessment dates and sites, and the conditions of authorisation"),
    ("Registers, as events happen", "The template rows of the registers and the review dates, completed when each event happens"),
]


def supplier_of(doc, inner, line):
    """Who is expected to supply a placeholder: the first rule that fits."""
    s = inner
    low = s.lower()
    if doc == "Decision Register":
        return "Decision makers"
    if doc in ("Data Protection Impact Assessment", "PII Processing Management", "Privacy Plan") \
            or "legal adviser" in low or "legitimate interests" in low or s == "Period":
        if "business owner" in low and "legal" not in low:
            return "Business owner"
        return "Legal adviser"
    if re.search(r"\\\[(PA-nn|R-XX-nn|NC-XX-nn|EV-XX-nn|XX|D-XX-P?nn)\\\]", line):
        return "Registers, as events happen"
    if doc in ("Control Assessment Record", "Security Assessment Report"):
        return "Assessors and the authorising official"
    if "business owner" in low or "information type" in low or "names, one for each schema" in low \
            or s == "CSS types" or (doc in ("System Description", "System Security Plan") and s == "Rating") \
            or "application profile" in low or low.startswith("number of"):
        return "Business owner"
    if "organisation" in low or "EV-" in s or s == "service" or "address range" in low \
            or "facilities contact" in low:
        return "\\<Organisation\\>"
    if re.search(r"build|sha-256|version|supplier|licence|^number$|to be set|measured|as microsoft|"
                 r"advisory source|remote desktop|time-outs|^function$|^problem$|^what to do$|library|"
                 r"managed printers|approved locations|^schema$|ports|commits|interval", low):
        return "Developers and administrators at build"
    if line.startswith("| \\[") or (doc == "Risk List" and s == "Date") \
            or (doc in ("Awareness and Training Management", "Maintenance Management") and low in ("date", "dates", "name", "names")):
        return "Registers, as events happen"
    return "System owner"


def census(ds):
    c = collections.Counter()
    for doc, lineno, inner, line in placeholders(ds):
        c[supplier_of(doc, inner, line)] += 1
    return c


# --------------------------------------------------------------- the checks
class Checker:
    def __init__(self, ds, verbose=False):
        self.ds = ds
        self.verbose = verbose
        self.results = []

    def check(self, cid, title):
        def deco(fn):
            problems = []
            try:
                fn(problems)
            except Exception as exc:  # a check that cannot run is a failure
                problems.append(f"check could not run: {exc!r}")
            self.results.append((cid, title, problems))
            return fn
        return deco

    def run(self):
        ds = self.ds
        docs = set(ds.docs)
        ssp = ssp_controls(ds)
        ncs = nc_register(ds)
        risks = risk_register(ds)
        chapters, x1 = car_model(ds)
        counts = car_counts(chapters, x1)
        dr_text = ds.text("Decision Register")
        decisions = re.findall(r"^\| (D-[A-Z]{2,3}-P?\d+) \|", dr_text, re.M)
        ev_defined = re.findall(r"^\| (EV-[A-Z]{2,3}-\d+) \|", ds.text("Evidence Requests"), re.M)
        tr_defined = {c[0]: c for c in rows_starting(ds.lines("Tailoring Register"), r"^\| TR-")}
        all_text = "\n".join(ds.docs.values())

        @self.check("L1", "Every document listed in <Documentation Map>, Table 1, exists, and every document is listed")
        def _(p):
            listed = re.findall(r"^\| \\<([^\\]+)\\> \| (?:Plans|Rules|Assessment|Guides)", ds.text("Documentation Map"), re.M)
            for d in listed:
                if d not in docs:
                    p.append(f"listed but missing: {d}")
            for d in docs:
                if d not in listed:
                    p.append(f"not listed in Table 1: {d}")
            if len(listed) != EXPECTED_DOCUMENTS:
                p.append(f"Table 1 lists {len(listed)} documents, not {EXPECTED_DOCUMENTS}")
            for m in re.finditer(r"(\d+) documents", all_text):
                if int(m.group(1)) not in (EXPECTED_DOCUMENTS,) and int(m.group(1)) > 30:
                    p.append(f"a total of {m.group(1)} documents is stated")

        @self.check("L2", "Every document cited by name in angle brackets is in the set")
        def _(p):
            for doc, text in ds.docs.items():
                for name in set(re.findall(r"\\<([^\\>]+)\\>", text)):
                    if name not in docs and name not in NON_DOCUMENTS and not name.startswith("Code"):
                        p.append(f"{doc}: cites \\<{name}\\>, which is not a document")

        @self.check("L3", "Every link and figure resolves to a file")
        def _(p):
            for doc, text in ds.docs.items():
                for target in re.findall(r"\]\(([^)#]+?)(?:#[^)]*)?\)", text):
                    if re.match(r"https?:", target):
                        continue
                    path = os.path.join(ds.root, target.replace("%20", " "))
                    if not os.path.exists(path):
                        p.append(f"{doc}: link to {target} does not resolve")

        @self.check("L4", "Every section cited in another document exists there")
        def _(p):
            pat = re.compile(r"\\<([^\\>]+)\\>(?: \([A-Z]{2}\))?, sections? ((?:[A-Z]{2}\.)?\d+(?:\.\d+)*)"
                             r"(?:(?:, | and | to )((?:[A-Z]{2}\.)?\d+(?:\.\d+)*))*")
            for doc, text in ds.docs.items():
                for m in pat.finditer(text):
                    target = m.group(1)
                    if target not in docs:
                        continue
                    heads = ds.headings(target)
                    full = m.group(0)
                    for num in re.findall(r"(?:[A-Z]{2}\.)?\d+(?:\.\d+)*", full.split(",", 1)[1]):
                        if num not in heads and not re.fullmatch(r"\d+", num) and num not in heads:
                            p.append(f"{doc}: \\<{target}\\>, section {num} does not exist")
                        elif re.fullmatch(r"\d+", num) and num not in heads:
                            p.append(f"{doc}: \\<{target}\\>, section {num} does not exist")

        @self.check("L5", "Every table cited in another document exists there")
        def _(p):
            pat = re.compile(r"\\<([^\\>]+)\\>(?: \([A-Z]{2}\))?, Tables? ([A-Z]{0,2}-?\d+[a-z]?)(?:(?:, | and | to )([A-Z]{0,2}-?\d+[a-z]?))*")
            for doc, text in ds.docs.items():
                for m in pat.finditer(text):
                    target = m.group(1)
                    if target not in docs:
                        continue
                    tabs = ds.tables(target)
                    for num in re.findall(r"(?<![\w.])[A-Z]{0,2}-?\d+[a-z]?(?![\w.])", m.group(0).split(",", 1)[1]):
                        if num not in tabs:
                            p.append(f"{doc}: \\<{target}\\>, Table {num} does not exist")

        @self.check("L6", f"<System Security Plan>, section 7, has one line for each of the {EXPECTED_CONTROLS} controls, and every stated total agrees")
        def _(p):
            if len(ssp) != EXPECTED_CONTROLS:
                p.append(f"section 7 has {len(ssp)} controls")
            for doc, text in ds.docs.items():
                for m in re.finditer(r"\b(3\d\d) controls\b", text):
                    if m.group(1) != str(EXPECTED_CONTROLS):
                        p.append(f"{doc}: states {m.group(1)} controls")

        @self.check("L7", f"{EXPECTED_INHERITED} controls are inherited, in section 7 and wherever the total is stated")
        def _(p):
            n = sum(1 for v in ssp.values() if v["type"] == "Inherited")
            if n != EXPECTED_INHERITED:
                p.append(f"section 7 has {n} inherited controls")
            for doc, text in ds.docs.items():
                for m in re.finditer(r"\b(\d+) (?:are |entries are |controls are )?(?:wholly )?inherited\b(?! PM)", text, re.I):
                    if int(m.group(1)) != EXPECTED_INHERITED and int(m.group(1)) > 20:
                        p.append(f"{doc}: states {m.group(1)} inherited")

        @self.check("L8", "Each control's gap entry in the security plan and its entry in <Risk List> name each other")
        def _(p):
            by_control = {v["control"]: k for k, v in ncs.items()}
            for cid, v in ssp.items():
                gap = v["gap"]
                if gap.startswith("NC-"):
                    nid = gap.split(",")[0].split(" ")[0]
                    if nid not in ncs:
                        p.append(f"{cid}: gap entry {nid} is not in \\<Risk List\\>")
                    elif ncs[nid]["control"] != cid:
                        p.append(f"{cid}: gap entry {nid} is for {ncs[nid]['control']}")
                elif cid in by_control:
                    p.append(f"{cid}: has {by_control[cid]} in \\<Risk List\\>, but the plan says {gap}")
            for nid, v in ncs.items():
                if v["control"] not in ssp:
                    p.append(f"{nid}: control {v['control']} is not in the plan")
                if nid[3:5] != v["family"]:
                    p.append(f"{nid}: family column says {v['family']}")

        @self.check("L9", "Every control treated as not applicable has a tailoring entry, and every entry exists")
        def _(p):
            for cid, v in ssp.items():
                if v["status"] == "Not applicable":
                    if not v["gap"].startswith("TR-") or v["gap"] not in tr_defined:
                        p.append(f"{cid}: not applicable with gap entry {v['gap']}")
            withdrawn = set()
            for line in ds.lines("Tailoring Register"):
                if "withdrawn" in line:
                    withdrawn |= set(re.findall(r"TR-[A-Z]{2}-\d+", line))
            for tid in set(re.findall(r"TR-[A-Z]{2}-\d+", all_text)):
                if tid not in tr_defined and tid not in withdrawn:
                    p.append(f"{tid} is cited but not in \\<Tailoring Register\\>")
            for tid in tr_defined:
                if not re.search(r"Approve " + re.escape(tid) + r"\b", dr_text):
                    p.append(f"{tid} has no decision row in \\<Decision Register\\>")

        @self.check("L10", "Every risk and non-compliance names risks and POA&M items that exist")
        def _(p):
            poam_items = set(re.findall(r"^\| (PA-\d+) \|", ds.text("Plan of Action and Milestones"), re.M))
            for nid, v in ncs.items():
                for rid in re.findall(r"R-[A-Z]{2}-\d+", v["risks"]):
                    if rid not in risks:
                        p.append(f"{nid}: risk {rid} does not exist")
                if v["poam"] != "None" and v["poam"] not in poam_items:
                    p.append(f"{nid}: POA&M {v['poam']} does not exist")
            for rid, v in risks.items():
                if v["poam"] != "None" and v["poam"] not in poam_items:
                    p.append(f"{rid}: POA&M {v['poam']} does not exist")
            for rid in set(re.findall(r"\bR-[A-Z]{2}-\d+\b", all_text)):
                if rid not in risks:
                    p.append(f"{rid} is cited but not in the risk register")
            for nid in set(re.findall(r"\bNC-[A-Z]{2}-\d+\b", all_text)):
                if nid not in ncs:
                    p.append(f"{nid} is cited but not in the non-compliance register")

        @self.check("L11", "Every decision cited exists once in <Decision Register>, and no document cites a value by a parameter code such as P-02")
        def _(p):
            dup = [d for d, n in collections.Counter(decisions).items() if n > 1]
            if dup:
                p.append("defined more than once: " + ", ".join(dup))
            dset = set(decisions)
            for doc, text in ds.docs.items():
                for d in set(re.findall(r"\bD-[A-Z]{2,3}-P?\d+\b", text)):
                    if d not in dset:
                        p.append(f"{doc}: cites {d}, which is not in \\<Decision Register\\>")
            # Values are written out in words wherever they are used; parameter codes (P-01 to P-76)
            # are no longer used. DIN 66399 level P-4, CSS task P-5 and ECDSA P-256 are not parameter codes.
            for doc, text in ds.docs.items():
                for prm in sorted(set(re.findall(r"(?<![A-Z]-)(?<![\w-])(?<!level )(?<!task )(?<!66399 )(?<!ECDSA )P-(\d+)\b(?!-)", text))):
                    p.append(f"{doc}: cites P-{prm}; write the value out instead")

        @self.check("L12", "Every evidence request cited exists once in <Evidence Requests>")
        def _(p):
            dup = [d for d, n in collections.Counter(ev_defined).items() if n > 1]
            if dup:
                p.append("defined more than once: " + ", ".join(dup))
            for doc, text in ds.docs.items():
                for e in set(re.findall(r"\bEV-[A-Z]{2,3}-\d+\b", text)):
                    if e not in ev_defined:
                        p.append(f"{doc}: cites {e}, which is not in \\<Evidence Requests\\>")

        @self.check("L13", "Every procedure, record template and interview question cited is defined")
        def _(p):
            pro = set(re.findall(r"^\| (PRO-[A-Z]{2}-\d+)\b", ds.text("Procedures"), re.M)) | \
                set(re.findall(r"^#{2,4} (PRO-[A-Z]{2}-\d+)\b", ds.text("Procedures"), re.M))
            tpl = set(re.findall(r"\b(TPL-\d+)\b", "\n".join(l for l in ds.lines("Record Templates") if l.startswith("#") or l.startswith("| TPL"))))
            intq = set(re.findall(r"^\| (INT-[A-Z]{2,3}-\d+) \|", ds.text("Interview Guide"), re.M))
            for doc, text in ds.docs.items():
                for x in set(re.findall(r"\bPRO-[A-Z]{2}-\d+\b", text)):
                    if x not in pro:
                        p.append(f"{doc}: cites {x}, which is not in \\<Procedures\\>")
                for x in set(re.findall(r"\bTPL-\d+\b", text)):
                    if x not in tpl:
                        p.append(f"{doc}: cites {x}, which is not in \\<Record Templates\\>")
                for x in set(re.findall(r"\bINT-[A-Z]{2,3}-\d+\b", text)):
                    if x not in intq:
                        p.append(f"{doc}: cites {x}, which is not in \\<Interview Guide\\>")

        def roles_of(doc, table_titles):
            out = []
            for line in ds.lines(doc):
                pass
            text = ds.text(doc)
            for title in table_titles:
                block = text.split(f"**{title}**", 1)[1].split("\n\n", 2)[1]
                for line in block.split("\n")[2:]:
                    if line.startswith("|"):
                        out.append(cells(line)[0])
            return out

        def same_role(a, b):
            a = a.lower().rstrip("s"); b = b.lower().rstrip("s")
            return a == b or a.startswith(b) or b.startswith(a)

        @self.check("L14", "Every security role in <Roles and Responsibilities> has its training defined in the matrix, or is named as relying on other training")
        def _(p):
            roles = roles_of("Roles and Responsibilities", ["Table 1: Governance roles", "Table 2: Operating roles"])
            matrix = roles_of("Awareness and Training Management", ["Table 4: Training matrix"])
            atm = ds.text("Awareness and Training Management")
            rely = atm.split("**Roles without access.**", 1)[1].split("\n", 1)[0] if "**Roles without access.**" in atm else ""
            for r in roles:
                if any(same_role(r, m) for m in matrix):
                    continue
                if r.replace("\\", "").replace("'s", "").lower() in rely.replace("\\", "").replace("'s", "").lower():
                    continue
                p.append(f"{r}: no row in the training matrix, and not named as relying on other training")

        @self.check("L15", "The non-compliance decision rows cover every entry once, with the right decider for the rating")
        def _(p):
            covered = collections.Counter()
            for c in rows_starting(ds.lines("Decision Register"), r"^\| NC-[A-Z]{2}-\d+ to NC-", 7):
                m = re.match(r"NC-([A-Z]{2})-(\d+) to NC-\1-(\d+)", c[0])
                fam, a, b = m.group(1), int(m.group(2)), int(m.group(3))
                ids = [f"NC-{fam}-{i:02d}" for i in range(a, b + 1)]
                fam_ids = [k for k in ncs if k[3:5] == fam]
                if ids != fam_ids:
                    p.append(f"{c[0]}: the family has {fam_ids[0]} to {fam_ids[-1]}")
                for k in ids:
                    covered[k] += 1
                meds = [k for k in fam_ids if ncs[k]["rating"].startswith(("Medium", "High"))]
                for k in meds:
                    if k not in c[2] or "authorising official" not in c[2]:
                        p.append(f"{k} is rated {ncs[k]['rating']}, but {c[0]} does not give it to the authorising official")
                if not meds and "every" not in c[2]:
                    p.append(f"{c[0]}: decider text does not match its ratings")
            for k in ncs:
                if covered[k] != 1:
                    p.append(f"{k} is covered {covered[k]} times")

        @self.check("L16", "<Control Assessment Record>: every statement has a finding, and each chapter's summary tables and totals agree with its findings")
        def _(p):
            valid = {"S", "O-D", "O-E", "O-G", "N/A", "N/S"}
            for i, fam in enumerate(FAMILIES):
                ch = chapters[fam]
                for sid, code, basis in ch["statements"]:
                    if code not in valid:
                        p.append(f"{fam}: {sid} has no finding")
                    elif "\\[Basis\\]" in basis:
                        p.append(f"{fam}: {sid} has no basis")
                for row in x1:
                    if row[2 + i] not in valid:
                        p.append(f"{fam}: {row[0]} has no finding in section 1.3")
                c = counts[fam]
                n = sum(c.values())
                text = "\n".join(ch["lines"])
                scope = re.search(r"with (\d+) determination statements", text)
                if not scope or int(scope.group(1)) != n:
                    p.append(f"{fam}: plan scope states {scope.group(1) if scope else 'no'} statements, the chapter has {n}")
                m = re.search(r"Of the CSS (\d+) statements, (\d+) are satisfied, (\d+) are not applicable, (\d+) await a decision or approval, (\d+) show a gap in the system,? (?:and )?(\d+) await evidence", text)
                if not m:
                    p.append(f"{fam}: summary sentence not filled")
                else:
                    got = list(map(int, m.groups()))
                    want = [n, c["S"], c["N/A"], c["O-D"], c["O-G"], c["O-E"]]
                    if got != want:
                        p.append(f"{fam}: summary sentence says {got}, findings give {want}")
                # control table
                stm_by_ctl = collections.defaultdict(list)
                for sid, code, _ in ch["statements"]:
                    stm_by_ctl[norm_control(sid)].append(code)
                stm_by_ctl[f"{fam}-1"] = [row[2 + i] for row in x1]
                for cid, (res, sat, tot) in ch["controls"].items():
                    codes = stm_by_ctl.get(cid, [])
                    if not codes:
                        p.append(f"{fam}: {cid} has no statements")
                        continue
                    exp = "Not applicable" if all(x in ("N/A", "N/S") for x in codes) else \
                        "Satisfied" if all(x in ("S", "N/A", "N/S") for x in codes) else "Other than satisfied"
                    if res != exp or sat != str(codes.count("S")) or tot != str(len(codes)):
                        p.append(f"{fam}: {cid} says {res}, {sat} of {tot}; findings give {exp}, {codes.count('S')} of {len(codes)}")
                for cid in stm_by_ctl:
                    if cid not in ch["controls"]:
                        p.append(f"{fam}: {cid} has statements but no result row")
                groups = collections.Counter(v[0] for v in ch["controls"].values())
                for label, key in (("Satisfied", "Satisfied"), ("Not applicable, subject", "Not applicable"),
                                   ("Other than satisfied, needing only", "Other than satisfied")):
                    m = re.search(r"^\| " + re.escape(label) + r"[^|]*\| (\d+) \|", text, re.M)
                    if not m or int(m.group(1)) != groups[key]:
                        p.append(f"{fam}: results-by-control row '{label}' does not give {groups[key]}")

        @self.check("L17", "Every role in <Roles and Responsibilities> has a risk designation")
        def _(p):
            roles = roles_of("Roles and Responsibilities", ["Table 1: Governance roles", "Table 2: Operating roles", "Table 3: Other roles"])
            designated = roles_of("Personnel Security Management", ["Table 1: Risk designations"])
            for r in roles:
                if not any(same_role(r, d) for d in designated):
                    p.append(f"{r}: no risk designation")

        @self.check("L18", "Each control's findings agree with <Risk List> and <Tailoring Register>")
        def _(p):
            codes_by_ctl = collections.defaultdict(list)
            for fam in FAMILIES:
                for sid, code, _ in chapters[fam]["statements"]:
                    codes_by_ctl[norm_control(sid)].append(code)
                codes_by_ctl[f"{fam}-1"] = [row[2 + FAMILIES.index(fam)] for row in x1]
            by_control = {v["control"]: (k, v) for k, v in ncs.items()}
            for cid, v in ssp.items():
                codes = codes_by_ctl.get(cid)
                if v["status"] == "Not applicable":
                    if codes and any(c != "N/A" for c in codes):
                        p.append(f"{cid}: tailored out but has findings other than N/A")
                    continue
                if not codes:
                    p.append(f"{cid}: no findings")
                    continue
                if cid in by_control:
                    nid, nc = by_control[cid]
                    found = {c[2:] for c in codes if c.startswith("O-")}
                    if not found:
                        p.append(f"{cid}: has {nid} but every statement is satisfied")
                    if found - nc["cause"]:
                        p.append(f"{cid}: findings {sorted(found)} go beyond {nid}'s causes {sorted(nc['cause'])}")
                    if len(codes) >= len(nc["cause"]) and nc["cause"] - found:
                        p.append(f"{cid}: {nid}'s causes {sorted(nc['cause'])} not all found")
                elif any(c.startswith("O-") for c in codes):
                    p.append(f"{cid}: other than satisfied, but no non-compliance entry")

        @self.check("L19", "<Security Assessment Report> gives the figures in <Control Assessment Record>")
        def _(p):
            sar = ds.text("Security Assessment Report")
            tot = collections.Counter()
            for fam in FAMILIES:
                c = counts[fam]
                tot.update(c)
                n = sum(c.values())
                ents = len(chapters[fam]["controls"])
                sat = sum(1 for v in chapters[fam]["controls"].values() if v[0] == "Satisfied")
                m = re.search(r"^\| " + fam + r" [^|]+\| (\d+)[^|]*\| (\d+) \| (\d+) of (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", sar, re.M)
                if not m:
                    p.append(f"Table 2 has no figures for {fam}")
                    continue
                got = list(map(int, m.groups()))
                want = [ents + (9 if fam == "PT" else 0), sat, c["S"], n, c["O-D"], c["O-G"], c["O-E"], c["N/A"] + c["N/S"]]
                if got != want:
                    p.append(f"Table 2, {fam}: says {got}, the record gives {want}")
            n = sum(tot.values())
            m = re.search(r"^\| \*\*Total\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*([\d,]+) of ([\d,]+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\*", sar, re.M)
            if not m:
                p.append("Table 2 has no total row")
            else:
                got = [int(x.replace(",", "")) for x in m.groups()]
                sat = sum(1 for f in FAMILIES for v in chapters[f]["controls"].values() if v[0] == "Satisfied")
                want = [EXPECTED_CONTROLS, sat, tot["S"], n, tot["O-D"], tot["O-G"], tot["O-E"], tot["N/A"] + tot["N/S"]]
                if got != want:
                    p.append(f"Table 2 total says {got}, the record gives {want}")
            if f"with {fmt(n)} determination statements" not in sar:
                p.append(f"the executive summary does not give {fmt(n)} statements")
            if f"{fmt(tot['S'])} of {fmt(n)} statements are satisfied" not in sar:
                p.append("the executive summary's satisfied figure differs")
            m = re.search(r"^\| \*\*Total\*\* \| \*\*(\d+)\*\* \|  \|$", sar, re.M)
            if not m or int(m.group(1)) != tot["O-D"] + tot["O-E"] + tot["O-G"]:
                p.append("Table 4's total differs from the other than satisfied statements")
            dm = ds.text("Documentation Map")
            if f"the {fmt(n)} determination statements" not in dm:
                p.append(f"\\<Documentation Map\\>, Table 1, does not give {fmt(n)} statements")

        @self.check("L20", "<Security Assessment Report>, Table 5, lists every risk with its rating and status")
        def _(p):
            sar = ds.text("Security Assessment Report")
            sec = sar.split("**Table 5: Risks**", 1)[1].split("## 6", 1)[0]
            rows = {c[0].split(" ")[0]: c for c in rows_starting(sec.split("\n"), r"^\| R-")}
            for rid, v in risks.items():
                if rid not in rows:
                    p.append(f"{rid} is missing")
                elif rows[rid][1] != v["rating"] or rows[rid][3] != v["status"]:
                    p.append(f"{rid}: report says {rows[rid][1]}, {rows[rid][3]}; \\<Risk List\\> says {v['rating']}, {v['status']}")
            for rid in rows:
                if rid not in risks:
                    p.append(f"{rid} is in the report but not in \\<Risk List\\>")

        @self.check("L21", "<Plan of Action and Milestones> holds every item the registers name, and the report gives its count")
        def _(p):
            poam = ds.text("Plan of Action and Milestones")
            items = re.findall(r"^\| (PA-\d+) \|", poam, re.M)
            named = {v["poam"] for v in list(ncs.values()) + list(risks.values())} - {"None"}
            for x in named:
                if x not in items:
                    p.append(f"{x} is named in \\<Risk List\\> but not in the plan")
            sar = ds.text("Security Assessment Report")
            m = re.search(r"\*\*Remediation:\*\* ([^\n]+)", sar)
            if not m:
                p.append("the report gives no remediation figure")
            elif not items and not m.group(1).startswith("None"):
                p.append("the plan has no items, but the report gives some")
            elif items and str(len(items)) not in m.group(1):
                p.append(f"the plan has {len(items)} items; the report does not say so")
            if "\\[PA-nn\\]" in "\n".join(l for l in ds.text("Risk List").split("\n") if l.startswith("| R-")):
                p.append("a risk still names \\[PA-nn\\]")

        @self.check("L22", "Each control's status in the security plan agrees with its assessment result")
        def _(p):
            res = {}
            for fam in FAMILIES:
                res.update({k: v[0] for k, v in chapters[fam]["controls"].items()})
            for cid, v in ssp.items():
                r = res.get(cid)
                if r is None:
                    if v["status"] != "Not applicable":
                        p.append(f"{cid}: no result in \\<Control Assessment Record\\>")
                    continue
                if (v["status"] == "Not applicable") != (r == "Not applicable"):
                    p.append(f"{cid}: plan says {v['status']}, assessment says {r}")
                if v["status"] == "Not implemented" and r == "Satisfied":
                    p.append(f"{cid}: not implemented but satisfied")

        @self.check("L23", "The count of facts still to be supplied in <Plan of Action and Milestones>, section 5.7, matches the set")
        def _(p):
            poam = ds.text("Plan of Action and Milestones")
            sec = poam.split("### 5.7", 1)[1] if "### 5.7" in poam else ""
            c = census(ds)
            total = sum(c.values())
            for who, _ in SUPPLIERS:
                m = re.search(r"^\| " + re.escape(who) + r" \|.*\| (\d[\d,]*) \|$", sec, re.M)
                if not m:
                    p.append(f"section 5.7 has no row for {who}")
                elif int(m.group(1).replace(",", "")) != c[who]:
                    p.append(f"section 5.7 gives {m.group(1)} for {who}; the set has {c[who]}")
            m = re.search(r"^\| \*\*Total\*\* \|.*\| \*\*([\d,]+)\*\* \|$", sec, re.M)
            if not m or int(m.group(1).replace(",", "")) != total:
                p.append(f"section 5.7's total is not {total}")

        @self.check("L24", "Every figure has its source, and every figure file is used")
        def _(p):
            figdir = os.path.join(ds.root, "figures")
            pngs = {f for f in os.listdir(figdir) if f.endswith(".png")}
            srcs = {f[:-5] for f in os.listdir(os.path.join(figdir, "src")) if f.endswith(".html")}
            used = set(re.findall(r"figures/([\w-]+\.png)", all_text))
            for f in pngs:
                if f[:-4] not in srcs:
                    p.append(f"{f} has no source in figures/src")
                if f not in used:
                    p.append(f"{f} is not used by any document")
            for f in used:
                if f not in pngs:
                    p.append(f"{f} is used but missing")
            for s in srcs:
                if s + ".png" not in pngs:
                    p.append(f"figures/src/{s}.html has no image")

        return self.results


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--census", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    ds = DocSet(args.root)
    if args.census:
        c = census(ds)
        for who, what in SUPPLIERS:
            print(f"{c[who]:5}  {who}")
        print(f"{sum(c.values()):5}  Total")
        return 0
    results = Checker(ds, args.verbose).run()
    failed = 0
    for cid, title, problems in results:
        status = "PASS" if not problems else "GAP"
        print(f"{cid:4} {status:4} {title}")
        if problems:
            failed += 1
            shown = problems if args.verbose else problems[:15]
            for x in shown:
                print(f"           - {x}")
            if len(problems) > len(shown):
                print(f"           ... and {len(problems) - len(shown)} more (use --verbose)")
    print(f"\n{len(results)} checks: {len(results) - failed} passed, {failed} with gaps")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
