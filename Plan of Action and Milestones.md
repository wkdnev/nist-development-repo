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
| Known vulnerabilities | 3 days if exploited, 14 days for Critical and High, 30 days for Medium and 90 days for Low, from the fix's release or its detection if later | \<Risk Assessment Management\>, section 3.6 |
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

Each step has a fixed number, REC-n (\<Documentation Map\>, Table 9). The road follows the desk self-assessment in \<Control Assessment Record\>, section 1.4, which found no gap in the system: every control is designed, and what remains is decisions, \<Organisation\>'s evidence, the build and the first operation of each step, and assurance. So no step below is a fix, and Table 3 holds no item. A gap found when the VMs are built and tested becomes an item in Table 3, and its fix is added to section 5.3 or 5.4.

### 5.1 Decide first

The decisions to be made before work starts, so that results can be approved and fixes scheduled. Each is a row in \<Decision Register\>, with its recommendation; nothing is decided until its row is completed by the person named.

**Table 5: Decisions to make first**

| Step | Who | What | Closes |
| --- | --- | --- | --- |
| REC-1 | \<Organisation\>; system owner | Appoint the authorising official, and name the person in every role and every deputy in \<Roles and Responsibilities\>, with their contact details | NC-CA-06 in part; the names in every plan and appendix |
| REC-2 | Authorising official | Decide what an authorisation rests on (D-CA-01, recommended: the independent Level 2 assessment), select the baseline (D-PL-03) and approve the categorisation (D-RA-01) | NC-CA-02 in part, NC-PL-06, NC-RA-02 |
| REC-3 | Head of Cyber; system owner | Approve the 19 chapters of \<Policy\> (Head of Cyber), and the 19 chapters of \<Procedures\> and the family design documents (system owner); the Head of Cyber also approves the incident response plan (D-IR-01) | NC-AC-01 to NC-SR-01, the XX-1 statements |
| REC-4 | Authorising official | Decide the tailoring: D-AC-01 to D-AC-04, D-AC-07 to D-AC-10, D-IA-02 to D-IA-07, D-PM-01, D-PT-01, D-PT-06, D-PT-07, D-SA-01, D-SC-01 and D-SI-01 | NC-PL-07, and the statements found not applicable |
| REC-5 | Authorising official | Decide the plans and the control types: D-CA-01, D-CA-03, D-IA-01, D-MP-03, D-PL-01, D-PL-03, D-PS-02, D-PT-02, D-RA-01 and D-SR-01; and, with the system owner, the contingency plan (D-CP-02) | The O-D statements that rest on them |
| REC-6 | Authorising official, on the system owner's advice | Decide the Medium risks: R-AC-01 (D-AC-11) and R-RA-03 to R-RA-08 (D-RA-02), each recommended for acceptance as its measures are already in the design; then NC-PT-02, NC-PT-05 and NC-PT-13 once REC-8 is done | The Medium entries in \<Risk List\> |
| REC-7 | System owner | Make the system owner's decisions (D-AC-12, D-AT-01, D-AU-01, D-CA-02, D-CA-04, D-CM-01, D-CM-02, D-CP-01, D-MA-01 to D-MA-03, D-MP-01, D-MP-02, D-PE-01, D-PL-04, D-PS-01, D-RA-03, D-RA-04, D-SC-02, D-SI-02 and D-SR-02, D-SR-03), approve the 68 parameter approvals in \<Decision Register\>, Table 2, with the legal adviser where its row says so, and decide the Low non-compliance batches in Table 3 | Most O-D statements |
| REC-8 | Legal adviser | Set the lawful basis for each kind of personal data, the special category and criminal offence conditions and whether an appropriate policy document is needed (D-PT-03); confirm the laws that apply (D-PT-P31) and the notice wording (D-AC-03); complete \<Data Protection Impact Assessment\> with its scores and the data protection officer's advice, and sign it off (D-PT-04, then the authorising official for its residual risks); approve \<Privacy Plan\> with the authorising official (D-PL-02); and set the retention periods with the business owner (D-PT-05) | NC-PT-02, NC-PT-05, NC-PT-13 to NC-PT-16, NC-PT-18, R-PT-03 |
| REC-9 | System owner, with the business owner | Set the two SI alert values (D-SI-P27): the bulk export threshold for U5, proposed at more than 200 items by one user in a day, and the out-of-hours window for administrator sign-ins (U6), proposed as outside 07:00 to 19:00 UK time, Monday to Friday except public holidays. Both are proposed reference values only. Supply the hours of service, the numbers of users, schemas and items, the information types, and the Data Owner of each schema | NC-SI-05 in part; \<System and Information Integrity Management\>, Table 3 |
| REC-10 | Each person who decides | Sign a sign-off sheet (TPL-24) for the decisions made, and have the system owner file it (\<Decision Register\>, section 5) | The Evidence column of every decision |

### 5.2 Get from \<Organisation\>

The facts, evidence and services to be obtained from \<Organisation\>, such as inherited controls and their scope.

**Table 6: What to get from \<Organisation\>**

| Step | What | Closes |
| --- | --- | --- |
| REC-11 | Send the covering request in \<Evidence Requests\>, section 1.2, for all 80 requests, and examine each answer. The 62 inherited controls rest wholly on them, and each provisional rating in \<Risk List\>, Table 3d, is confirmed or changed when its evidence is seen | Every O-E statement that names an EV request |
| REC-12 | Confirm that the Cyber Essentials Plus scope includes the two VMs, and obtain \<Organisation\>'s policies that apply (EV-GEN-04) | NC-AC-01 to NC-SR-01 in part |
| REC-13 | Obtain the name of \<Organisation\>'s common control official, the authorisation of its common controls (EV-CA-01), and the evidence for the 35 inherited PM controls (EV-PM-01 to EV-PM-04) | NC-CA-06 in part, R-PM-02 |
| REC-14 | Obtain the values only \<Organisation\> can give: its time source, address ranges and ports, its central logging service, the approved locations for copies, the managed printers, the remote maintenance route and tool, and its contacts, as listed in section 5.7 | The placeholders marked for \<Organisation\> |

### 5.3 Fix before \<System Name\> holds real data

The fixes needed before real data is held, with the quickest risk reductions first. No fix is needed: the desk self-assessment found no gap in the system. These steps are what the documents require before real data is held.

**Table 7: Before real data is held**

| Step | What | Where it is required |
| --- | --- | --- |
| REC-15 | Complete REC-8: the lawful bases and conditions, and the impact assessment completed and approved | \<Data Protection Impact Assessment\>; \<Risk List\>, R-PT-03 |
| REC-16 | Approve the first access list (TPL-5) | \<Procedures\>, PRO-CM-2; NC-CM-17 |
| REC-17 | Choose the scanner, and record the first scan, risk review and supply chain review | \<Risk List\>, R-RA-01; NC-RA-04, NC-RA-05 |
| REC-18 | Before each person's access: screening confirmed, the briefing and role modules given, and the rules of behaviour and access agreements signed | NC-PS-03, NC-PS-06, NC-PL-03, NC-PT-07, NC-PT-09 |

### 5.4 Fix before going live

The further fixes needed before \<System Name\> goes live. As in section 5.3, none is a fix of a known gap; these are the steps the documents require before go-live.

**Table 8: Before going live**

| Step | What | Where it is required |
| --- | --- | --- |
| REC-19 | Build the two VMs; record the baseline's commits, checksums and CIS results, the inventory, the key store and the tool list; enforce App Control for Business after its audit period (D-CM-01) | NC-CM-02, NC-CM-12, NC-IA-11, NC-MA-03, NC-SC-14 |
| REC-20 | Run each family's test script on the built VMs, keep the results with their manifests, and raise any gap as an item in Table 3 | Every O-E statement awaiting evidence from the VMs; \<Security Assessment Report\>, section 7 |
| REC-21 | Hold the first restore test and the tabletop exercise within 30 days of the build | NC-CP-06, NC-CP-20, NC-IR-03 |
| REC-22 | Walk each procedure through once on TPL-4 | \<Procedures\>, section 1 |
| REC-23 | Commission the penetration test by a tester independent of the build, and rate each finding in \<Risk List\> | \<Tailoring Register\>, CA-8 |
| REC-24 | Set the milestone dates in Table 1 | Section 2.1 |

### 5.5 Assurance and next steps

The assurance work and next steps that support the authorisation decision.

**Table 9: Assurance**

| Step | What | Closes |
| --- | --- | --- |
| REC-25 | Appoint the Level 1 assessor, have the authorising official approve each chapter's assessment plan, and re-determine on the built VMs every finding of the desk self-assessment | NC-CA-02 |
| REC-26 | Appoint the independent Level 2 team, with each member's TPL-19 accepted by the authorising official; it re-determines every statement and its report replaces the desk figures in \<Security Assessment Report\> | CA-2(1); D-CA-01 |
| REC-27 | Assemble the authorisation package (\<Assessment, Authorization, and Monitoring Management\>, Table 4); the authorising official decides on TPL-18, accepting the 62 inherited controls and reliance on \<Organisation\>'s programme | NC-CA-06 |
| REC-28 | Start continuous monitoring at go-live, and re-authorise every year on a new Level 2 assessment | NC-CA-07 |

### 5.6 Steps by family

The steps that arise from each family's assessment, in CSS order. For each family: its non-compliance entries, the decisions they await, the evidence they await from \<Organisation\>, and the entries that also await a first operation or evidence from the VMs. Each family's decisions are made in REC-3 to REC-10, its evidence obtained in REC-11 to REC-14, and its first operation follows REC-16 to REC-22.

**Table 10: Steps by family**

| Family | Entries | Decisions awaited | Evidence awaited from \<Organisation\> | Also awaiting a first operation or evidence from the VMs |
| --- | --- | --- | --- | --- |
| AC | 34 | \<Policy\> (AC) and \<Procedures\> (AC); D-AC-02 to D-AC-04, D-AC-09, D-AC-10, D-AC-P02 to D-AC-P06, D-AC-P36 to D-AC-P38, D-AC-P41 to D-AC-P49 and D-AC-P51 to D-AC-P55 | EV-AC-01 to EV-AC-17, EV-IA-04 and EV-GEN-04 | None |
| AT | 6 | \<Policy\> (AT) and \<Procedures\> (AT); D-AT-01, D-AT-P24 and D-AT-P56 to D-AT-P60 | EV-AT-01, EV-AT-02 and EV-GEN-04 | None |
| AU | 13 | \<Policy\> (AU) and \<Procedures\> (AU); D-AU-01, D-AU-P07 to D-AU-P09 and D-AU-P61, D-AU-P62 | EV-AU-01 to EV-AU-05 and EV-GEN-04 | None |
| CA | 9 | \<Policy\> (CA) and \<Procedures\> (CA); D-AC-11, D-CA-01 to D-CA-04 and D-CA-P25 | EV-CA-01, EV-CA-02, EV-PM-03 and EV-GEN-04 | NC-CA-02, NC-CA-05, NC-CA-06, NC-CA-07 |
| CM | 18 | \<Policy\> (CM) and \<Procedures\> (CM); D-CM-01, D-CM-02, D-CM-P29 and D-CM-P63 to D-CM-P66 | EV-AC-03, EV-AC-05, EV-AC-07, EV-CM-01 to EV-CM-05 and EV-GEN-04 | NC-CM-02, NC-CM-12, NC-CM-15, NC-CM-17 |
| CP | 20 | \<Policy\> (CP) and \<Procedures\> (CP); D-AT-P24, D-CP-01, D-CP-02 and D-CP-P12 to D-CP-P16 | EV-CP-01, EV-CP-02 and EV-GEN-04 | NC-CP-02, NC-CP-05, NC-CP-06, NC-CP-18, NC-CP-20 |
| IA | 18 | \<Policy\> (IA) and \<Procedures\> (IA); D-AC-P02 and D-IA-01 | EV-AC-01, EV-IA-01 to EV-IA-04 and EV-GEN-04 | NC-IA-09, NC-IA-11 |
| IR | 13 | \<Policy\> (IR) and \<Procedures\> (IR); D-AT-P24, D-AT-P56, D-AT-P58, D-IR-01 and D-IR-P21 | EV-CP-01, EV-IR-01, EV-IR-02, EV-SR-01, EV-GEN-01 and EV-GEN-04 | NC-IR-02, NC-IR-03, NC-IR-06, NC-IR-10, NC-IR-11, NC-IR-13 |
| MA | 8 | \<Policy\> (MA) and \<Procedures\> (MA); D-AC-P54, D-CM-01, D-MA-01 to D-MA-03 and D-MA-P67, D-MA-P68 | EV-MA-01, EV-MA-02 and EV-GEN-04 | NC-MA-03, NC-MA-04, NC-MA-06, NC-MA-07 |
| MP | 7 | \<Policy\> (MP) and \<Procedures\> (MP); D-AC-P48, D-MP-01 to D-MP-03, D-MP-P20 and D-MP-P69 | EV-AC-17, EV-AU-03, EV-CP-01, EV-MP-01 to EV-MP-03 and EV-GEN-04 | NC-MP-02, NC-MP-03, NC-MP-04 |
| PE | 18 | \<Policy\> (PE) and \<Procedures\> (PE); D-MA-03, D-MP-01, D-PE-01 and D-PE-P70 | EV-MA-01, EV-PE-01 to EV-PE-05 and EV-GEN-04 | NC-PE-03, NC-PE-05, NC-PE-18 |
| PL | 7 | \<Policy\> (PL) and \<Procedures\> (PL); D-AC-01 to D-AC-04, D-AC-07 to D-AC-10, D-IA-02 to D-IA-07, D-PL-01 to D-PL-04, D-PL-P71, D-PM-01, D-PT-01, D-PT-06, D-PT-07, D-SA-01, D-SC-01 and D-SI-01 | EV-PL-01 and EV-GEN-04 | NC-PL-02, NC-PL-03, NC-PL-05 |
| PS | 9 | \<Policy\> (PS) and \<Procedures\> (PS); D-AC-P06, D-AC-P41, D-PL-04, D-PS-01, D-PS-02 and D-PS-P72 | EV-AC-01, EV-PS-01 to EV-PS-03 and EV-GEN-04 | NC-PS-02, NC-PS-03, NC-PS-06, NC-PS-07 |
| PT | 20 | \<Policy\> (PT) and \<Procedures\> (PT); D-AT-P24, D-AT-P59, D-IR-01, D-PT-02 to D-PT-05, D-PT-P22, D-PT-P31 and D-PT-P73 | EV-PM-02, EV-PT-01, EV-PT-02 and EV-GEN-04 | NC-PT-04, NC-PT-06, NC-PT-07, NC-PT-09, NC-PT-12, NC-PT-15, NC-PT-17, NC-PT-19, NC-PT-20 |
| RA | 10 | \<Policy\> (RA) and \<Procedures\> (RA); D-PT-04, D-RA-01 to D-RA-04, D-RA-P11, D-RA-P30 and D-RA-P74 | EV-PM-01, EV-RA-01, EV-SR-01, EV-SR-02 and EV-GEN-04 | NC-RA-05, NC-RA-06, NC-RA-07 |
| SA | 16 | \<Policy\> (SA) and \<Procedures\> (SA); D-CA-02, D-CA-04, D-MA-P68, D-PL-01, D-RA-04, D-RA-P74, D-SA-P28 and D-SA-P75 | EV-CA-02, EV-MA-01, EV-SA-01 to EV-SA-04 and EV-GEN-04 | NC-SA-02, NC-SA-03, NC-SA-07, NC-SA-08, NC-SA-09, NC-SA-10, NC-SA-13, NC-SA-14, NC-SA-16 |
| SC | 24 | \<Policy\> (SC) and \<Procedures\> (SC); D-AC-P02, D-IA-01, D-SC-02, D-SC-P10 and D-SC-P26 | EV-AC-03, EV-AU-01, EV-IA-04, EV-SC-01 to EV-SC-05 and EV-GEN-03, EV-GEN-04 | NC-SC-02, NC-SC-14, NC-SC-17, NC-SC-22, NC-SC-24 |
| SI | 16 | \<Policy\> (SI) and \<Procedures\> (SI); D-AU-P07, D-CM-P29, D-CP-P15, D-MP-P20, D-MP-P69, D-PT-05, D-RA-P11, D-SI-02, D-SI-P17 and D-SI-P27 | EV-SI-01 to EV-SI-03 and EV-GEN-04 | NC-SI-02, NC-SI-03, NC-SI-04, NC-SI-09, NC-SI-10, NC-SI-12, NC-SI-16 |
| SR | 12 | \<Policy\> (SR) and \<Procedures\> (SR); D-SR-01 to D-SR-03 and D-SR-P76 | EV-MA-01, EV-SA-01, EV-SA-04, EV-SR-01, EV-SR-02 and EV-GEN-04 | NC-SR-02, NC-SR-03, NC-SR-04, NC-SR-05, NC-SR-06, NC-SR-08, NC-SR-09 |

### 5.7 Facts still to be supplied

Square brackets in the document set mark a fact that has not yet been supplied, or a register entry that is completed when its event happens; they are grouped by who is expected to supply them, so that each person can be asked once. Test-PlanConsistency.py (\<Documentation Map\>, section 4.11) counts them with the same rules, and check L23 confirms this table. Nothing in this table may be filled in by anyone other than the person named.

**Table 11: Facts still to be supplied**

| Who | Facts | Placeholders |
| --- | --- | --- |
| Decision makers | The decision, name and date of each approval and decision, and the sign-off sheets | 477 |
| Legal adviser | The lawful bases, special category and criminal offence conditions, retention periods with the business owner, and the impact assessment's scores, advice and sign-off | 112 |
| Business owner | The information types and their ratings, hours of service, numbers of users and items, and each schema's Data Owner | 33 |
| System owner | The people in each role, their deputies and contacts, the milestone dates, and the business values the system owner sets | 247 |
| \<Organisation\> | The values, services, names and evidence \<Organisation\> provides | 46 |
| Developers and administrators at build | Names, versions, counts, hashes, suppliers and settings recorded when the VMs are built and the components chosen | 75 |
| Assessors and the authorising official | The assessors' names, the assessment dates and sites, and the conditions of authorisation | 62 |
| Registers, as events happen | The template rows of the registers and the review dates, completed when each event happens | 239 |
| **Total** |  | **1,291** |
