# A clean set for any application

The set is a template that any application team picks up and fills in. It holds the reference design (from `System Description.md`) and the rules, procedures and forms. It holds no record of anything that has happened: no assessment, test result, finding, risk entry, decision, incident, plan item, evidence received, interview answer, review or approval. Read `tools/CLEAN_GUIDE.md` too: everything it removes stays removed.

## IDs: which stay and which go

| Kind | Example | Keep or remove |
| --- | --- | --- |
| Settings, procedures, templates, policy rules, flows, keys, use cases | P-AC-10, PRO-AC-4, TPL-14, R11, A23, F7, K12, U6 | Keep: they are design |
| Tailoring proposals | TR-AC-02 | Keep the ID and what is tailored; drop any decision or approval state |
| Evidence requests | EV-IA-04 | Keep the ID and what is asked for; drop any state ("Not sent", "Received", "Not evidenced") |
| Decisions | D-AC-23, D-GEN-06, D-AC-P06 | Remove every reference. State the design plainly instead |
| Plan items and recommendations | PA-12, REC-11 | Remove every reference |
| Risks and non-compliances | R-AC-08, NC-21, NC-CM-15 | Remove every reference |
| Tests, drills and checks of a build | T33, I08, M12, D01, C04, A38, Test-Vulnerability.ps1 results | Remove every reference and result. A design rule that a script will check something may stay, without a result |
| Incidents | INC-2026-001 | Remove |

Where removing a reference leaves "(…)" empty, or leaves a sentence that only existed to point at it, remove the brackets or the sentence. Where a table column exists only to hold these references or results (for example "Today", "State now", "Evidence state", "Risk", "Plan item", "Decision"), remove the column and keep the cell counts consistent.

## Remove also

- Every note about the tested v1.0 build, "today", "as built", "how it stands today", and what a build did or did not do. Remove whole subsections that only describe the build today (for example "How it is built today"), and renumber nothing: if a removed subsection is not the last, replace its heading and body with nothing and leave the gap only if renumbering would break references; prefer removing the last-numbered ones. Report any subsection you removed.
- Summaries of results: "four of fourteen statements satisfied", "No control is missing from the design", counts of open items, "the two most serious gaps".
- In \<System Security Plan\> section 7 tables, the Status, Assessment and Decision cells become "\[Status\]", "\[Result\]" and "\[Decision\]". The How it is implemented, Who and Type cells stay, cleaned of the IDs above.

## Record documents become templates

A record document keeps its purpose, how to use it, its ID scheme, its section layout (one section per family where it has one) and its tables' column headers. Each table keeps its caption and header row and gets one placeholder row such as `| \[PA-nn\] | \[Weakness\] | ... |`. Methods, scales and rules for filling it in stay (for example the risk rating method and who may decide). Questions to ask stay; recorded answers go. Determination statements to assess stay; results and findings go.

## Rules

- Edit only the files you are given. Others edit other files at the same time. No git commands.
- Plain British English, no em dashes, no NIST (write CSS), no dates, no approvals.
- Keep section numbers and table numbers where you can. If you remove a table, renumber the remaining tables and their in-document references, and list the old-to-new numbers in your report so references from other documents can be fixed. Do not remove sections numbered before others unless they are wholly about results.
- Report: per file, what you removed, any section or table numbering changes, and anything you were unsure about.
