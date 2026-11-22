# \<System Name\> Security Assessment Report

## 1 Purpose and scope

This report brings together the results of the assessment of all 19 control families, so that the authorising official can see in one place how far \<System Name\> meets the CSS Moderate baseline, what the remaining risk is, and what must happen before it can be authorised. It is the assessment report in the authorisation package (CSS, tasks A-4 and R-1), and it meets CA-2e and CA-2f. It covers the privacy controls as well, so it is also the privacy assessment report.

This section states what was assessed: the version of \<System Name\>, its components (UI application, Admin application, API and shared library, and the Microsoft SQL Server 2022 database) and the environment it runs in, two Windows Server 2025 VMs at \<Organisation\>. The detail for each family is in its assessment, which takes precedence over this summary. The figures in this report are taken from the assessments, \<Risk List\> and \<Plan of Action and Milestones\>, and are checked against them.

**Status of this version.** The figures in this version come from the desk self-assessment in \<Control Assessment Record\>, section 1.4, made on 22 November 2026 from the documents alone. It prepares for the assessments and is not the Level 2 report: no VM was built, no test was run, nobody was interviewed and none of \<Organisation\>'s evidence was seen. The authorisation rests on the independent Level 2 assessment (D-CA-01), whose results replace these. Each figure is counted from \<Control Assessment Record\>, and checked by the document set check (\<Documentation Map\>, section 4.11).

## 2 Executive summary

This section gives the authorising official the overall position in a few lines: whether \<System Name\> is ready to be authorised, and why.

- **Coverage:** The 316 entries of the CSS Moderate baseline with the privacy baseline, in 19 families, with 1,993 determination statements, using CSS catalog release 5.2.0. The 9 entries tailored out entirely (PT-4, SI-19 and the seven United States PT controls) have no statements in the record. The PM family is \<Organisation\>'s programme, inherited and not among the 316 (TR-PM-01)
- **Result:** 597 of 1,993 statements are satisfied, and 16 controls are fully satisfied. 22 entries are not applicable, subject to their tailoring decisions
- **Why the rest are not satisfied:** 642 await a decision, an approval or their first operation, and 710 await evidence, 660 of them from \<Organisation\> and 50 from the built VMs. None shows a gap in the system. 44 are not applicable or parameters not selected
- **Risk:** 51 risks are recorded in \<Risk List\>. None is rated High; 8 are Medium (R-AC-01, R-PT-03, R-RA-03, R-RA-04, R-RA-05, R-RA-06, R-RA-07, R-RA-08), each proposed for the authorising official's decision, and the rest Low. Behind them are 278 non-compliances: 3 rated Medium and 275 Low, most of them provisional until the evidence is seen
- **Remediation:** None. No weakness needs a fix: every non-compliance is proposed for approval, evidence or tailoring, and the Medium risks for acceptance with their measures already in the design. A gap found by the Level 1 or Level 2 assessment on the VMs becomes an item
- **Inherited controls:** 62 entries are wholly inherited from \<Organisation\>. None of the 80 requests in \<Evidence Requests\> has yet been answered

**Recommendation to the authorising official:** Not yet ready to authorise. The desk self-assessment finds the design complete, with no gap in the system, but nothing is yet approved, built, tested or evidenced. Authorisation should follow the Level 2 assessment once the conditions in section 8 are met, and should not rest on this version

## 3 Assessment approach

This section records who assessed \<System Name\>, how independent they are, when and how the assessment was carried out, and its limits.

**Table 1: Assessment approach**

| Item | Detail |
| --- | --- |
| Assessor | Level 2: an independent team led by \[Name\], which meets CA-2(1) once each member's TPL-19 is accepted by the authorising official. This report is for the Level 2 assessment; the Level 1 self-assessment by \[Name\], working for the system owner, is its starting point. An authorisation rests only on a Level 2 report. This version holds the desk self-assessment, prepared for the system owner from the documents before either assessor is appointed |
| Independence | The desk self-assessment and Level 1 are not independent: both work for the system owner. Level 2 is independent of the system owner, the developers and the administrators, and meets CA-2(1) (D-CA-01) |
| Dates | Desk self-assessment of all 19 families: 22 November 2026. Level 1 and Level 2: \[Dates\], set by the assessors once appointed |
| Procedures | CSS catalog release 5.2.0, with one finding for each of the 1,993 determination statements, by the rules in \<Control Assessment Record\>, section 1.4 |
| Methods | Examine only: the policy, procedures, plans, design documents and registers in the document set. No test was run and nobody was interviewed |
| Environment | None: the VMs are not built, and no data was used |
| Limits | Nothing was tested or seen in operation, none of \<Organisation\>'s evidence was examined, and the parameter values are proposed but not approved. A statement found satisfied means only that the design meets it |
| Plans | Section 4 of each family's chapter of \<Control Assessment Record\>, such as section AC.4. None is yet approved by the authorising official |

## 4 Results

### 4.1 Results by family

This section gives, for each family, the number of entries, the controls and statements satisfied, and why the other statements are not satisfied.

**Table 2: Results by family**

| Family | Entries | Controls satisfied | Statements satisfied | Awaiting a decision or operation | Gap in the system | Awaiting evidence | Not applicable | Assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AC Access Control | 39 | 2 | 33 of 189 | 55 | 0 | 81 | 20 | \<Control Assessment Record\>, AC chapter |
| AT Awareness and Training | 6 | 0 | 18 of 66 | 19 | 0 | 29 | 0 | \<Control Assessment Record\>, AT chapter |
| AU Audit and Accountability | 16 | 3 | 32 of 81 | 19 | 0 | 30 | 0 | \<Control Assessment Record\>, AU chapter |
| CA Assessment, Authorization, and Monitoring | 10 | 1 | 47 of 93 | 33 | 0 | 13 | 0 | \<Control Assessment Record\>, CA chapter |
| CM Configuration Management | 24 | 6 | 94 of 178 | 48 | 0 | 36 | 0 | \<Control Assessment Record\>, CM chapter |
| CP Contingency Planning | 23 | 3 | 28 of 124 | 58 | 0 | 38 | 0 | \<Control Assessment Record\>, CP chapter |
| IA Identification and Authentication | 24 | 0 | 22 of 92 | 15 | 0 | 42 | 13 | \<Control Assessment Record\>, IA chapter |
| IR Incident Response | 13 | 0 | 21 of 90 | 35 | 0 | 34 | 0 | \<Control Assessment Record\>, IR chapter |
| MA Maintenance | 9 | 1 | 20 of 64 | 21 | 0 | 23 | 0 | \<Control Assessment Record\>, MA chapter |
| MP Media Protection | 7 | 0 | 18 of 71 | 31 | 0 | 22 | 0 | \<Control Assessment Record\>, MP chapter |
| PE Physical and Environmental Protection | 18 | 0 | 18 of 121 | 33 | 0 | 70 | 0 | \<Control Assessment Record\>, PE chapter |
| PL Planning | 7 | 0 | 18 of 93 | 38 | 0 | 37 | 0 | \<Control Assessment Record\>, PL chapter |
| PS Personnel Security | 9 | 0 | 19 of 68 | 28 | 0 | 21 | 0 | \<Control Assessment Record\>, PS chapter |
| PT Personally Identifiable Information Processing and Transparency | 29, of which 9 have no statements | 0 | 33 of 103 | 45 | 0 | 25 | 0 | \<Control Assessment Record\>, PT chapter |
| RA Risk Assessment | 10 | 0 | 24 of 73 | 22 | 0 | 27 | 0 | \<Control Assessment Record\>, RA chapter |
| SA System and Services Acquisition | 17 | 0 | 52 of 160 | 47 | 0 | 60 | 1 | \<Control Assessment Record\>, SA chapter |
| SC System and Communications Protection | 25 | 0 | 28 of 107 | 22 | 0 | 54 | 3 | \<Control Assessment Record\>, SC chapter |
| SI System and Information Integrity | 18 | 0 | 34 of 139 | 45 | 0 | 53 | 7 | \<Control Assessment Record\>, SI chapter |
| SR Supply Chain Risk Management | 12 | 0 | 38 of 81 | 28 | 0 | 15 | 0 | \<Control Assessment Record\>, SR chapter |
| **Total** | **316** | **16** | **597 of 1,993** | **642** | **0** | **710** | **44** |  |

A control counts as satisfied only when every one of its statements is satisfied or does not apply. The PT chapter holds the privacy baseline controls of other families as well, and the 9 PT and SI entries tailored out entirely. Not applicable counts the statements tailored out and the AC parameters not selected (N/S).

### 4.2 Controls fully satisfied

This section lists, by family, the 16 controls whose every statement is satisfied or does not apply. Families with none are left out: each of their controls waits at least on its policy, a decision or evidence. The 22 entries tailored out are in \<Tailoring Register\>.

**Table 3: Controls fully satisfied**

| Family | Controls |
| --- | --- |
| AC | AC-2(4), AC-3 |
| AU | AU-3(1), AU-7, AU-7(1) |
| CA | CA-7(4) |
| CM | CM-2(2), CM-3(2), CM-3(4), CM-4, CM-4(2), CM-8(1) |
| CP | CP-2(8), CP-9(8), CP-10(2) |
| MA | MA-3(2) |

### 4.3 Why statements are other than satisfied

This section groups the statements that are other than satisfied by cause, and says what closes each group. The 44 statements that are not applicable or not selected rest on the tailoring decisions, and are not counted here.

**Table 4: Other than satisfied, by cause**

| Cause | Statements | What closes it |
| --- | --- | --- |
| Awaiting a decision, an approval or the first operation of a step (O-D) | 642 | The decisions and parameter approvals in \<Decision Register\>, with their sign-off sheets; then the steps' first operation once the VMs are built and the roles named |
| Awaiting \<Organisation\>'s evidence (O-E) | 660 | \<Organisation\>'s answers to \<Evidence Requests\>, examined by the assessor; each provisional rating in \<Risk List\> is then confirmed |
| Awaiting evidence from the built VMs (O-E) | 50 | Building the VMs and running the family tests, with their evidence and manifests |
| A gap in the system (O-G) | 0 | None found |
| **Total** | **1352** |  |

## 5 Risk position

This section lists the risks from \<Risk List\>, highest rating first, with their treatment and status, and gives the number of open non-compliances behind them by rating. The full register, with causes, consequences and decisions, is \<Risk List\>. Of the 278 open non-compliances behind them, none is rated High, 3 are rated Medium (NC-PT-02, NC-PT-05 and NC-PT-13) and 275 Low.

**Table 5: Risks**

| Risk | Rating | Treatment | Status |
| --- | --- | --- | --- |
| R-AC-01 A database administrator reads item content directly in SQL Server, outside the application's access checks | Medium | Reduce | Proposed (D-AC-11) |
| R-PT-03 Personal data is processed without a recorded lawful basis, condition or approved impact assessment | Medium | Approve | Open |
| R-RA-03 Someone on \<Organisation\>'s network exploits a known flaw in \<System Name\>'s applications, packages, browser libraries or servers to reach items | Medium | Reduce | Proposed (D-RA-02) |
| R-RA-04 A user with access to a schema reads, exports or shares its items beyond what their work needs, or sends an export to the wrong person | Medium | Reduce | Proposed (D-RA-02) |
| R-RA-05 A Windows server administrator, or someone who has taken over their account, misuses control of the application server | Medium | Reduce | Proposed (D-RA-02) |
| R-RA-06 A harmful or compromised package, browser library or build tool enters a release | Medium | Reduce | Proposed (D-RA-02) |
| R-RA-07 PingFederate or Active Directory is compromised or misconfigured, so that someone signs in as another person or is put into any group | Medium | Reduce | Proposed (D-RA-02) |
| R-RA-08 Ransomware, a destructive attack or an administrator's mistake destroys the database and its backups | Medium | Reduce | Proposed (D-RA-02) |
| R-AC-02 Access control values and tailoring are used before they are approved | Low | Approve | Open |
| R-AC-03 An access control that \<System Name\> inherits from \<Organisation\> is weaker than the design assumes | Low | Evidence | Open |
| R-AT-01 A standard user keeps access while their yearly awareness training and briefing are overdue | Low | Accept | Proposed (D-AT-01) |
| R-AT-02 Awareness and training values and the accepted risk are used before they are approved | Low | Approve | Open |
| R-AT-03 Training that \<System Name\> relies on from \<Organisation\> is weaker than the design assumes | Low | Evidence | Open |
| R-AU-01 Audit and accountability values and the accepted risk are used before they are approved | Low | Approve | Open |
| R-AU-02 Logging that \<System Name\> relies on from \<Organisation\> is weaker than the design assumes | Low | Evidence | Open |
| R-AU-03 A logging fault stops staff from using \<System Name\> | Low | Accept | Proposed (D-AU-01) |
| R-CA-01 Assessment, authorisation and monitoring rest on people, values and records nobody with authority has appointed or approved | Low | Approve | Open |
| R-CA-02 Inherited controls, exchanges or the monitoring strategy that \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-CM-01 Configuration management values, decisions and the plan are used before they are approved | Low | Approve | Open |
| R-CM-02 Configuration controls that \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-CP-01 Contingency values, decisions and the plan are used before they are approved | Low | Approve | Open |
| R-CP-02 The recovery services \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-IA-01 Identification and authentication values, levels and tailoring are used before they are approved | Low | Approve | Open |
| R-IA-02 Identification and authentication that \<System Name\> relies on from \<Organisation\> is weaker than the design assumes | Low | Evidence | Open |
| R-IR-01 Incident response values and the plan are used before they are approved, and before the people in it are named and exercised | Low | Approve | Open |
| R-IR-02 The incident help and records \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-MA-01 Maintenance values, decisions and lists are used before they are approved | Low | Approve | Open |
| R-MA-02 The maintenance, route and support \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-MP-01 Media protection values and decisions are used before they are approved | Low | Approve | Open |
| R-MP-02 The media handling \<System Name\> relies on from \<Organisation\> is weaker than the design assumes | Low | Evidence | Open |
| R-PE-01 Physical and environmental values and decisions are used before they are approved | Low | Approve | Open |
| R-PE-02 The physical and environmental protection \<System Name\> relies on from \<Organisation\> is weaker than the design assumes | Low | Evidence | Open |
| R-PL-01 Planning values, plan approvals and decisions are used before they are approved | Low | Approve | Open |
| R-PL-02 The enterprise architecture and hosting \<System Name\>'s plans rely on from \<Organisation\> differ from what the design assumes | Low | Evidence | Open |
| R-PM-01 The PM controls are relied on as \<Organisation\>'s without an approved decision | Low | Approve | Open |
| R-PM-02 The security and privacy programme \<System Name\> relies on from \<Organisation\> is weaker than the design assumes | Low | Evidence | Open |
| R-PS-01 Personnel security values, designations and decisions are used before they are approved | Low | Approve | Open |
| R-PS-02 The screening, leaver, HR and disciplinary processes \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-PT-01 Privacy values, tailoring and decisions are used before they are approved | Low | Approve | Open |
| R-PT-02 The privacy notices, record of processing, privacy programme or visitor records \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-RA-01 RA values, the categorisation and the threat risks are used before they are approved | Low | Approve | Open |
| R-RA-02 The security contact, scanning and risk strategy \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-RA-09 \<System Name\> is unavailable for longer than its maximum tolerable downtime | Low | Reduce | Proposed (D-RA-03) |
| R-SA-01 Acquisition and development values, tailoring and records are used before they are approved or made | Low | Approve | Open |
| R-SA-02 The development platform, contracts and services \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-SC-01 Communications protection values, tailoring and records are used before they are approved or made | Low | Approve | Open |
| R-SC-02 The network, VPN, proxy, name resolution, certificates and hosting \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-SI-01 Integrity values, decisions and records are used before they are approved or made | Low | Approve | Open |
| R-SI-02 The monitoring, advisories, and firmware updates and checks that \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |
| R-SR-01 Supply chain values, decisions, the plan and records are used before they are approved or made | Low | Approve | Open |
| R-SR-02 The supplier approval, notices, hardware inspection, repair control and disposal \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | Low | Evidence | Open |

## 6 Weaknesses fixed or closed during the assessment

This section lists the weaknesses that were fixed or closed while the assessment ran, with how each was closed and whether it awaits a repeat test.

**Table 6: Items fixed or closed**

| Item | Rating | Weakness | Outcome |
| --- | --- | --- | --- |
| None | Not applicable | No weakness has been raised: \<Plan of Action and Milestones\> holds no item | Not applicable |

## 7 Evidence

This section lists the test scripts run, the checks each covers, and their results. Each script can be run again, and each evidence folder holds a README and a manifest of SHA-256 hashes for its results. A gap in a result is a real weakness, recorded in \<Plan of Action and Milestones\>. It is not a script failure. Only Test-PlanConsistency.py, which runs on the documents, has been run. The other scripts need the built VMs, and the Checks column gives what each covers until its first run.

**Table 7: Test scripts and results**

| Script | Families | Checks | Number | Passed | Gaps | Latest results |
| --- | --- | --- | --- | --- | --- | --- |
| Test-AccessControl.ps1 | AC | Schema access, roles and anonymous endpoints | Not run | Not run | Not run | None: the VMs are not built |
| Test-AuditAndAuth.ps1 | AU, IA | Audit records, and sign-in | Not run | Not run | Not run | None: the VMs are not built |
| Test-Identification.ps1 | AU, IA | Identifiers and authenticators | Not run | Not run | Not run | None: the VMs are not built |
| Test-ConfigurationManagement.ps1 | CM | The baseline and settings | Not run | Not run | Not run | None: the VMs are not built |
| Test-Protection.ps1 | SC | Encryption in transit, security headers and cookies, keys and secrets, and request limits | Not run | Not run | Not run | None: the VMs are not built |
| Test-IncidentReadiness.ps1 | IR | Ending access, clocks, and the logs an incident needs | Not run | Not run | Not run | None: the VMs are not built |
| Test-BackupRestore.ps1 | CP | Backup and restore | Not run | Not run | Not run | None: the VMs are not built |
| Test-Maintenance.ps1 | MA | Maintenance pages and tools | Not run | Not run | Not run | None: the VMs are not built |
| Test-MediaProtection.ps1 | MP | Exports and marking | Not run | Not run | Not run | None: the VMs are not built |
| Test-PersonalData.ps1 | PT | How personal data is held, logged and kept | Not run | Not run | Not run | None: the VMs are not built |
| Test-Integrity.ps1 | SI | Upload checks, error handling, checksums, the audit chain and alerts | Not run | Not run | Not run | None: the VMs are not built |
| Test-Vulnerability.ps1 | RA | Packages, browser libraries, code and the risk records | Not run | Not run | Not run | None: the VMs are not built |
| Test-SupplyChain.ps1 | SR | Package sources, lock files, signatures, the browser library manifest, the bill of materials, the release's SHA-256 values and suppliers | Not run | Not run | Not run | None: the VMs are not built |
| Test-Development.ps1 | SA | Repositories, the build and component support | Not run | Not run | Not run | None: the VMs are not built |
| Test-PlanConsistency.py | PL | The consistency of the document set: checks L1 to L24 | 24 | 24 | 0 | Run on the document set on 22 November 2026, before this version was issued; the result is kept in the change record (\<Documentation Map\>, section 4.11) |
| **Total** |  |  | **24** | **24** | **0** |  |

## 8 Conditions before authorisation

This section lists the conditions the assessor recommends are met before \<System Name\> is authorised, each linked to the items, risks or evidence that close it.

1. The decisions in \<Plan of Action and Milestones\>, REC-1 to REC-10, are made and signed on TPL-24: above all the Head of Cyber's approval of \<Policy\>, the authorising official's decisions on the tailoring, the plans and the Medium risks (D-AC-11 for R-AC-01, D-RA-02 for R-RA-03 to R-RA-08), and the system owner's parameter approvals.
2. The legal adviser has set the lawful bases and conditions and completed the impact assessment, and it is approved, before real data is held (REC-8, REC-15; D-PT-03, D-PT-04, D-PT-05), so that NC-PT-02, NC-PT-05, NC-PT-13 and R-PT-03 can be decided.
3. \<Organisation\>'s evidence for the 62 inherited controls and the other requests in \<Evidence Requests\> is received and examined, and each provisional rating in \<Risk List\> confirmed (REC-11 to REC-14).
4. The steps required before real data is held are complete: the first access list, the first scan and reviews, and screening, training and signed rules for each person before access (REC-16 to REC-18).
5. The VMs are built, each family's test is run with its evidence, the restore test, tabletop exercise and penetration test are held, and any gap found is rated in \<Risk List\> and, unless accepted, planned in \<Plan of Action and Milestones\> (REC-19 to REC-24).
6. The independent Level 2 assessment re-determines every statement, and its report replaces the desk figures in this version (REC-25, REC-26; D-CA-01).

## 9 Authorisation package

This report is one part of the authorisation package. The package is listed once, in \<Assessment, Authorization, and Monitoring Management\>, Table 4, and the authorising official records the decision on TPL-18.
