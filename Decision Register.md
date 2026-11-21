## 1 Purpose

This register records the approvals and decisions for the set. Each row states what needs deciding, the recommendation and who decides, with space for the decision, name and date. Nothing is decided until a named person completes a row. The recommendations are proposals.

After a decision, the document it affects is updated to match: \<System Description\>, section 4, and the family design document for values, \<Risk List\> for risk treatments and \<Tailoring Register\> for tailoring.

A departure from the reference design (\<System Description\>, section 3.6) is decided by the system owner and recorded here as a D-GEN entry; a departure from a Secure by Design principle (\<System Description\>, section 8) is decided by the authorising official.

Decisions are numbered D-XX-nn, parameter approvals D-XX-Pnn and non-compliance entries NC-XX-nn, where XX is the family code. Cross-family decisions use GEN as the code. Each table has one row for each entry, with a Family column, so that adding an entry never renumbers another.

## 2 Decisions

Documents, policy decisions and cross-family decisions (GEN). The legal adviser confirms the legal positions in PT decisions.

**Table 1: Decisions**

| ID | Family | Decision needed | Recommendation | Who decides | Decision | Name | Date | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[D-XX-nn\] | \[XX\] | \[Decision needed\] | \[Recommendation\] | \[Who decides\] | \[Decision\] | \[Name\] | \[Date\] | \[Sheet\] |

## 3 Parameter approvals

The reference values are the parameters in \<System Description\>, section 4, which match \<Organisation\>'s corporate values. Each row records the approval of one control's parameters, with the main values proposed.

**Table 2: Parameter approvals**

| ID | Family | Control | Parameters | Main values | Who decides | Decision | Name | Date | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[D-XX-Pnn\] | \[XX\] | \[Control\] | \[Number of parameters\] | \[Main values\] | \[Who decides\] | \[Decision\] | \[Name\] | \[Date\] | \[Sheet\] |

## 4 Non-compliance treatment decisions

The control, rating, reason and treatment of each entry are in \<Risk List\>, section 5. This table records who decided, when, and the sheet that proves it, with one row for each batch of decisions. The system owner decides Low risks and the authorising official decides Medium and High risks. A provisional rating is confirmed when the evidence is seen.

**Table 3: Non-compliance treatment decisions**

| Entries | Family | Who decides | Decision | Name | Date | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| \[NC-XX-nn\] | \[XX\] | \[Who decides\] | \[Decision\] | \[Name\] | \[Date\] | \[Sheet\] |

## 5 Proof of approval

Every decision in this register names the person who made it. Where the system owner records another person's decision, that person signs for it on their own sheet.

The Evidence column of each table names the sign-off sheet that proves the decision. A sheet is form TPL-24 in \<Record Templates\>. It lists the decisions by number, and the approver signs it, or confirms it by email or in a minuted meeting. One sheet covers every decision a person has made up to its date, and a new sheet is started for later decisions. "None yet" marks a decision that is still pending. A row that covers several entries counts once for each entry.

Until a sheet is filed, the decisions it covers rest on the system owner's record alone. The system owner files each sheet in the Restricted store and enters its reference and date below. Nobody signs for anyone else.

**Table 4: Sign-off sheets**

| Sheet | Approver | Role | Covers | Decisions | Filed |
| --- | --- | --- | --- | --- | --- |
| \[Sheet\] | \[Name\] | \[Role\] | \[Decisions covered\] | \[Number of decisions\] | \[Reference and date\] |
