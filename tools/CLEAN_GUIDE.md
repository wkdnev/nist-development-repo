# Making the set clean and unapproved

The set is a clean template for any application. Nothing in it has been reviewed, approved, agreed, confirmed, signed, accepted or decided by anyone, and nothing has happened on a date.

## Remove

- **Dates** of any kind: "on 9 November 2026", "(November 2026)", "by 20 November 2026", "accepted to 6 November 2027", "as at ...", years attached to events. Rewrite the sentence so it still reads well without the date. Keep durations and periods ("every 12 months", "within 1 hour", "72-hour recovery time objective").
- **Statements that something has been approved, agreed, confirmed, reviewed, signed, accepted or decided**, by anyone: "approved by the system owner", "confirmed by the Head of Cyber", "the legal adviser reviewed it", "Not yet approved", "Approved", "agreed with", "signed off", "stated by the system owner", "pending confirmation". State the design or rule plainly instead. Where a table column exists only to record approval state (for example a "Status" or "Approved" column of a settings table), empty it to a placeholder such as "\[To be approved\]" only if the column must stay; otherwise remove the column, keeping cell counts consistent.
- **Review notes and history**: "this was changed after review", "previously", "was renamed", "the earlier version said", "since corrected", notes about what an earlier draft said.
- **Named real events**: specific incidents, drills or meetings that happened (for example INC-2026-001). Describe the design or procedure instead.

## Keep

- **Design processes that involve approval**: "the line manager approves the request", "changes are approved by the change board", "the ServiceNow approval workflow", "PRO-xx steps", templates with blank "Approved by" fields. These describe how the system will work, not something that happened.
- Decision IDs (D-xx-nn), PA-, R-, NC-, TR-, EV-, T-numbered test IDs and findings, and "the tested v1.0 build" notes. They are handled separately. Do not remove or reword them in this pass, except to drop a date or an approval phrase attached to them ("D-RA-09, approved on 11 November 2026" becomes "D-RA-09").
- Section and table numbers, placeholders (\<System Name\>, \<Organisation\>, \[Name\]).

## Rules

- Edit only the files you are given. Others are editing other files at the same time. No git commands.
- Plain British English, no em dashes, no NIST (write CSS). Keep table cell counts consistent.
- Report: per file, the number of changes, and anything you were unsure about.
