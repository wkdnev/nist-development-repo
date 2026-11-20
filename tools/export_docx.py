#!/usr/bin/env python3
"""Export the document set to Word, with tables that behave in Word.

Copying from a Markdown viewer carries the viewer's own HTML and styling into
Word, which treats it inconsistently. This builds each .docx directly instead:

- pandoc converts the Markdown (GitHub flavour), with figures embedded;
- every table then gets the same style: thin grey borders, a shaded header row
  that repeats on each page, rows that do not split across pages, full text
  width, column widths in proportion to their content, and 9 pt text (8 pt for
  tables with seven or more columns);
- table captions are kept with their table, and figure captions with their
  figure; pages are A4 with 2 cm margins.

Usage: python3 tools/export_docx.py OUTPUT_DIR [Document.md ...]
"""
import glob
import math
import os
import re
import subprocess
import sys

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BORDER = "A6A6A6"
HEADER_FILL = "D9E1EC"


def el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), str(v))
    return e


def replace_child(parent, tag, new):
    for old in parent.findall(qn(tag)):
        parent.remove(old)
    parent.append(new)


def style_table(table, text_width_twips):
    tbl = table._tbl
    tblPr = tbl.tblPr
    replace_child(tblPr, "w:tblW", el("w:tblW", w=5000, type="pct"))
    replace_child(tblPr, "w:tblLayout", el("w:tblLayout", type="fixed"))
    borders = el("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        borders.append(el("w:" + side, val="single", sz=4, space=0, color=BORDER))
    replace_child(tblPr, "w:tblBorders", borders)
    mar = el("w:tblCellMar")
    for side, w in (("top", 40), ("left", 80), ("bottom", 40), ("right", 80)):
        mar.append(el("w:" + side, w=w, type="dxa"))
    replace_child(tblPr, "w:tblCellMar", mar)
    look = tblPr.find(qn("w:tblLook"))
    if look is not None:
        tblPr.remove(look)

    rows = table.rows
    ncols = max(len(r.cells) for r in rows)
    size = Pt(8) if ncols >= 7 else Pt(9)

    # column widths: each column at least as wide as its longest word, and
    # the rest shared in proportion to how much text the column holds
    char = 104 if ncols >= 7 else 114         # twips per character at 8 or 9 pt
    longest, amount = [0] * ncols, [0] * ncols
    for r in rows:
        for i, c in enumerate(r.cells[:ncols]):
            words = c.text.split()
            longest[i] = max([longest[i]] + [min(len(w), 22) for w in words])
            amount[i] = max(amount[i], min(len(c.text), 300))
    floor = [l * char + 200 for l in longest]
    if sum(floor) > text_width_twips:
        widths = [int(text_width_twips * fl / sum(floor)) for fl in floor]
    else:
        spare = text_width_twips - sum(floor)
        weights = [math.sqrt(max(a - l, 0)) for a, l in zip(amount, longest)]
        tw = sum(weights) or 1
        widths = [int(fl + spare * w / tw) for fl, w in zip(floor, weights)]
    grid = tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn("w:gridCol"))):
        if i < ncols:
            gc.set(qn("w:w"), str(widths[i]))

    for ri, r in enumerate(rows):
        trPr = r._tr.get_or_add_trPr()
        replace_child(trPr, "w:cantSplit", el("w:cantSplit"))
        if ri == 0:
            replace_child(trPr, "w:tblHeader", el("w:tblHeader"))
        for ci, c in enumerate(r.cells):
            tcPr = c._tc.get_or_add_tcPr()
            if ci < ncols:
                replace_child(tcPr, "w:tcW", el("w:tcW", w=widths[ci], type="dxa"))
            if ri == 0:
                replace_child(tcPr, "w:shd", el("w:shd", val="clear", color="auto", fill=HEADER_FILL))
            for p in c.paragraphs:
                pf = p.paragraph_format
                pf.space_before = Pt(0)
                pf.space_after = Pt(0)
                for run in p.runs:
                    run.font.size = size
                    if ri == 0:
                        run.font.bold = True


LANDSCAPE_FROM = 8   # tables this wide get a landscape page of their own


def section_break(orient):
    """A paragraph that ends a section with the given orientation."""
    p = OxmlElement("w:p")
    pPr = OxmlElement("w:pPr")
    sect = OxmlElement("w:sectPr")
    w, h = (16838, 11906) if orient == "landscape" else (11906, 16838)
    pg = el("w:pgSz", w=w, h=h)
    if orient == "landscape":
        pg.set(qn("w:orient"), "landscape")
    sect.append(pg)
    sect.append(el("w:pgMar", top=1134, right=1134, bottom=1134, left=1134,
                   header=708, footer=708, gutter=0))
    pPr.append(sect)
    p.append(pPr)
    return p


def landscape(doc, table):
    tbl = table._tbl
    start = tbl
    prev = tbl.getprevious()
    if prev is not None and prev.tag == qn("w:p") and CAPTION.match("".join(prev.itertext()).strip()):
        start = prev
    before = start.getprevious()
    # merge with a landscape section that ends just before this one
    if before is not None and before.find(qn("w:pPr") + "/" + qn("w:sectPr")) is not None:
        before.getparent().remove(before)
    else:
        start.addprevious(section_break("portrait"))
    tbl.addnext(section_break("landscape"))


CAPTION = re.compile(r"^(Table|Figure) [A-Z0-9-]+[a-z]?:")


def postprocess(path):
    d = Document(path)
    for s in d.sections:
        s.orientation = WD_ORIENT.PORTRAIT
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.left_margin = s.right_margin = Cm(2)
        s.top_margin = s.bottom_margin = Cm(2)
    text_width = int((21 - 4) / 2.54 * 1440)
    for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
        if name in [st.name for st in d.styles]:
            d.styles[name].font.name = "Calibri"
            d.styles[name].font.size = Pt(10.5)
    land_width = int((29.7 - 4) / 2.54 * 1440)
    for t in d.tables:
        ncols = max(len(r.cells) for r in t.rows)
        if ncols >= LANDSCAPE_FROM:
            style_table(t, land_width)
            landscape(d, t)
        else:
            style_table(t, text_width)
    # keep table captions with the table that follows, and figures with their captions
    paras = d.paragraphs
    for i, p in enumerate(paras):
        if CAPTION.match(p.text.strip()):
            if p.text.startswith("Table"):
                p.paragraph_format.keep_with_next = True
            elif i > 0:
                paras[i - 1].paragraph_format.keep_with_next = True
        if p.style.name.startswith("Heading"):
            p.paragraph_format.keep_with_next = True
            for run in p.runs:
                run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
    d.save(path)


def main():
    out = sys.argv[1]
    files = sys.argv[2:] or sorted(f for f in glob.glob(os.path.join(ROOT, "*.md"))
                                   if os.path.basename(f) != "README.md")
    os.makedirs(out, exist_ok=True)
    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        dest = os.path.join(out, name + ".docx")
        subprocess.run(["pandoc", "-f", "gfm", "-t", "docx", f, "--resource-path", ROOT,
                        "-o", dest], check=True, cwd=ROOT)
        postprocess(dest)
        print("wrote", dest)


if __name__ == "__main__":
    main()
