# Merging section 4 into section 3 in a family document

The worked example is `Access Control Management.md`. Read its sections 1 to 3 before starting.

## The rule behind it

**No duplication.** A design element is written in one place only, so that a change to the design is made once. A family document holds only the design and implementation settings for its family. Anything held in another document is pointed to, never repeated:

| Information | Where it lives |
| --- | --- |
| Status, who provides, who is responsible, assessment result | \<System Security Plan\>, section 7.n (the family's table) |
| What CSS requires, part by part; tests and results; records an assessor asks for | \<Control Assessment Record\> (XX) |
| Risk for a control | \<Risk List\> |
| Open items and fixes | \<Plan of Action and Milestones\> |
| Policy rules; procedure steps | \<Policy\> (XX); \<Procedures\> (XX) |
| Organisation-defined parameter values | Set at corporate level by \<Organisation\> |

## Steps for one document

1. **Section 4** ("Each control and enhancement") has, for each control, a design table (Part, CSS requires, Design, Today) and a responsibility and evidence table. For every Design cell and every "Enforced by" row, check whether section 3 already states that design. If not, move the missing design detail (a rule, setting, value, mechanism, who does what, a time limit) into the most fitting section 3 subsection, in the document's plain-English style. Where nothing fits, add a subsection at the end of section 3, grouped by topic, never by control. Keep P-, PRO-, D-, TPL-, TR- references.
2. Do not carry over the CSS requires text, Today, Provided by, Responsible, Rules and procedures, Tests, Records, Status, Risk decision or Open items.
3. **Delete section 4 entirely.** If appendices follow, they keep their letters.
4. **Tag section 3.** Directly under each section 3 subsection heading (### and ####), add a blank line and then one line: `Controls met here: XX-1, XX-2(3).` listing, in catalogue order, every control whose parts that subsection meets. Every control of the family (as listed in the old section 4) must appear in at least one tag. Subsections that meet no control get no tag.
5. **Rewrite section 1 Purpose** on the Access Control model: one sentence on what the document covers; "Section 3 is the design: ..." with a short topic list and the sentence "Each subsection names the controls it helps to meet, and the settings table in section 3.x names the control each setting serves." (only if the document has a settings table; give its number); the paragraph "Other documents hold the rest. ..." naming the right family code, the plan's section 7.n and Table number (see the pointer already at the top of section 2); one sentence that values CSS asks the organisation to define are set at corporate level by \<Organisation\>, and that any settings in section 3 should match them, and are changed in this document where they do not; and, only if section 3 still has "today" notes, one sentence saying they describe the tested v1.0 build. Remove sentences that describe section 4 or the old appendices. Remove any claim that this is the only place something is held.
6. **Renumber** table captions (`**Table N: ...**`) from 1 in order of appearance, and every in-document "Table N" reference. Fix in-document "section 4.x" references to point at the section 3 subsection that now holds the design.
7. **Check:** every in-document "Table N" resolves; every "section 3.x" resolves; tables have consistent cell counts; no em dashes; British spelling; no new dates, approvals or review statements.

## References from other documents

Do not edit any file other than your own family documents. Other agents are working in parallel. Instead, grep the other `*.md` files for references into your document that your change breaks ("\<Your Document\>, section 4.n", "\<Your Document\>, Table N", a renumbered section 3 subsection) and write each needed change to `/tmp/claude-0/-home-user/76f25fd2-8795-5139-89a6-2782c059f998/scratchpad/xrefs/<Your Document>.tsv`, one per line: `file<TAB>line number<TAB>exact old text<TAB>exact new text`. The exact old text must be a substring of that line, short but unique within the line.
