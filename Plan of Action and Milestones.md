# \<System Name\> Plan of Action and Milestones

## 1 Purpose and summary

This plan is used by every control family. It holds every weakness that needs a fix, in one register (section 3), with closed items in section 4 and the road to authorisation in section 5. Items are numbered PA-nn.

An item is worked on once its risk decision in \<Risk List\> is to remediate. The plan holds remediation only: evidence still to come is tracked in \<Evidence Requests\>, and an accepted risk in \<Risk List\>, section 3. If an item's risk is later accepted instead of fixed, the item moves to section 4 with the acceptance as the way it closed.

In the Source column, a letter and number is a check in the evidence store. "Code review" means found by the assessor's review of the application and not tested. The finding is stated in full here, so no reader needs the code. "Assessment" and "Review" mean found while assessing or reviewing a family. Section 5 gives the recommended order of decisions and work, with the facts still to be supplied.

## 2 How items are scheduled

### 2.1 Milestones

Each item has a milestone, which says when its fix is planned. The system owner sets the dates when the development phase is scheduled.

**Table 1: Milestones**

| Milestone | What it is | Date |
| --- | --- | --- |
| M1 | Approvals and decisions, before development starts | \[Date\] |
| M2 | The development phase | \[Date\] |
| M3 | The VM build | \[Date\] |
| M4 | Before authorisation | \[Date\] |
| Go-live | Real data is first held | \[Date\] |

### 2.2 Latest completion

Each item also has a latest completion, after which it is overdue. Until the go-live date is set, it is stated as a rule.

**Table 2: Latest completion by rating**

| Item | Latest completion | Decided by |
| --- | --- | --- |
| High items | \[Latest completion\] | Authorising official |
| Medium items | Within 180 days of go-live, or of the date the item is raised if later | \<Policy\> (CA) |
| Low items | Within 365 days of go-live, or of the date the item is raised if later | \<Policy\> (CA) |
| Known vulnerabilities | 3 days if exploited, 14 days for Critical and High, 30 days for Medium and 90 days for Low, from the fix's release or its detection if later (\<System Description\>, P-11) | \<Risk Assessment Management\>, section 3.6 |
| Items the fix or the decision says must be done first | Before go-live | The item's own decision |

Overdue items go to the authorising official each quarter. An item closes only when its fix is tested and recorded (\<Procedures\>, PRO-CA-3). Effort is an estimate for the system owner to confirm: small is up to a day, medium is up to a week, and large is more than a week.

## 3 Register of open and fixed items

**Table 3: Register of open and fixed items**

| ID | Rating | Control | Weakness | Source | Identified | Fix | Risk | Non-compliance and decision | Owner | Resources and effort | Milestone | Latest completion | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[PA-nn\] | \[Rating\] | \[Control\] | \[Weakness\] | \[Source\] | \[Date\] | \[Fix\] | \[Risk\] | \[Non-compliance and decision\] | \[Owner\] | \[Resources; effort\] | \[Milestone\] | \[Latest completion\] | \[Status\] |

## 4 Closed items

**Table 4: Closed items**

| ID | Rating | Control | Weakness | Source | Identified | How it was closed | Closed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \[PA-nn\] | \[Rating\] | \[Control\] | \[Weakness\] | \[Source\] | \[Date\] | \[How it was closed\] | \[Date\] |

## 5 Road to authorisation

This section sets out, in a suggested order, the decisions and actions that lead to an authorisation decision. The organisation takes a risk-based approach, so not every step needs to be carried out: each non-compliance is first decided in \<Risk List\>, section 5, and a fix follows only where the risk is not accepted. The steps are recommendations.

### 5.1 Decide first

The decisions to be made before work starts, so that results can be approved and fixes scheduled.

### 5.2 Get from \<Organisation\>

The facts, evidence and services to be obtained from \<Organisation\>, such as inherited controls and their scope.

### 5.3 Fix before \<System Name\> holds real data

The fixes needed before real data is held, with the quickest risk reductions first.

### 5.4 Fix before going live

The further fixes needed before \<System Name\> goes live.

### 5.5 Assurance and next steps

The assurance work and next steps that support the authorisation decision.

### 5.6 Steps by family

The steps that arise from each family's assessment, in CSS order.

### 5.7 Facts still to be supplied

Square brackets in the document set mark a fact that has not yet been supplied, or a register entry that is completed when its event happens; they are grouped by who is expected to supply them, so that each person can be asked once.
