# \<System Name\> Security Assessment Report

## 1 Purpose and scope

This report brings together the results of the Level 1 self-assessment of all 19 control families, so that the authorising official can see in one place how far \<System Name\> meets the NIST SP 800-53 Rev 5 Moderate baseline, what the remaining risk is, and what must happen before it can be authorised. It is the assessment report in the authorisation package (NIST SP 800-37 Rev 2, tasks A-4 and R-1), and it meets CA-2e and CA-2f. It covers the privacy controls as well, so it is also the privacy assessment report.

It covers \<System Name\> v1.0: UI application, Admin application, API and the \<System Name\> database, on the two planned Windows Server 2025 VMs at \<Organisation\>. The detail for each family is in its assessment, which takes precedence over this summary. The figures in this report are generated from the assessments, the risk list and the POA&M, and Test-PlanConsistency.ps1 checks that they agree.

## 2 Executive summary

**\<System Name\> is not ready to be authorised, and it holds no production documents.** That is the expected position for a system that is not yet built on its VMs: most of what is outstanding is a decision not yet carried out, evidence not yet available, or a code fix waiting for the development phase.

- **Coverage:** all 316 entries in the Moderate baseline, and the privacy baseline outside PM, were assessed against 1,998 NIST SP 800-53A determination statements. The coverage and the statement counts were checked against NIST's catalogue, release 5.2.0, on 12 November 2026.
- **Result:** 1,083 statements (54%) are satisfied, and 19 controls are fully satisfied. Every other statement is recorded with a reason, and every non-compliance is rated in \<Risk List\>.
- **Why the rest are not satisfied:** 157 statements (8%) are gaps in the system itself; 306 (15%) await evidence from \<Organisation\> or the VMs; 390 (20%) await a decision, or the start of operation; and 62 do not apply. Section 4.3 breaks these down.
- **Risk:** 24 risks are recorded. 5 are rated High: a user interferes with another user's session or abuses internal functions (R-AC-02); someone gains full database control (R-AC-04); credentials or documents are intercepted (R-AC-05); a stolen password gives full access (R-AC-10); a known flaw or malicious upload compromises the system (R-SI-01).
- **Remediation:** \<Plan of Action and Milestones\> holds 131 items: 13 High, 55 Medium and 63 Low. 6 are fixed and waiting for a repeat test on the VMs, 2 are closed and 123 are open, 10 of them High.
- **Inherited controls:** 65 entries depend wholly on \<Organisation\> (\<Assessment, Authorization, and Monitoring Management\>, section 3.6). None of the 74 evidence requests in \<Evidence Requests\> has yet been sent.

**Recommendation to the authorising official:** do not authorise yet. Authorisation should wait for, at least, the conditions in section 8.

## 3 Assessment approach

**Table 1: Assessment approach**

| Item | Detail |
| --- | --- |
| Assessor | Level 1: Claude, an AI assistant, working for the system owner. Level 2: an independent team led by \[Name\], which meets CA-2(1) once each member has completed TPL-19 |
| Independence | Level 1 is a self-assessment. The same assistant drafted the documents and assessed them, for the system owner, so it is not independent. Level 2 provides the independence |
| Dates | 5 to 12 November 2026. Each family was assessed on 5 or 6 November, and reassessed after its pack review between 8 and 12 November |
| Procedures | NIST SP 800-53A Rev 5, catalog release 5.2.0, one finding for every determination statement |
| Methods | Examine (documents, code and configuration), Test (15 test scripts, with results and hash manifests in the evidence store; section 7) and Interview (the system owner's written answers only) |
| Environment | A throwaway Docker stack on one PC with sample data, built from the code tagged v1.0 |
| Limits | The VMs, PostgreSQL on Windows and \<Organisation\>'s services were not examined, and the role holders were not interviewed. Nothing has been seen in operation, because \<System Name\> is not in use. Level 2 must repeat the tests on the VMs |
| Plans | Each family's assessment plan is in its chapter of \<Control Assessment Record\>, and all 19 were approved by the authorising official (D-GEN-18) |

## 4 Results

### 4.1 Results by family

**Table 2: Results by family**

| Family | Entries | Controls satisfied | Statements satisfied | Awaiting a decision or operation | Gap in the system | Awaiting evidence | Not applicable | Assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AC Access Control | 39 | 0 | 74 of 189 | 22 | 39 | 21 | 33 | \<Control Assessment Record\>, AC chapter |
| AT Awareness and Training | 6 | 0 | 34 of 66 | 17 | 0 | 15 | 0 | \<Control Assessment Record\>, AT chapter |
| AU Audit and Accountability | 16 | 1 | 48 of 81 | 8 | 15 | 10 | 0 | \<Control Assessment Record\>, AU chapter |
| CA Assessment, Authorization, and Monitoring | 10 | 0 | 64 of 93 | 27 | 0 | 2 | 0 | \<Control Assessment Record\>, CA chapter |
| CM Configuration Management | 24 | 2 | 90 of 178 | 41 | 16 | 31 | 0 | \<Control Assessment Record\>, CM chapter |
| CP Contingency Planning | 23 | 2 | 65 of 124 | 28 | 12 | 19 | 0 | \<Control Assessment Record\>, CP chapter |
| IA Identification and Authentication | 24 | 0 | 41 of 92 | 7 | 15 | 15 | 14 | \<Control Assessment Record\>, IA chapter |
| IR Incident Response | 13 | 0 | 49 of 90 | 38 | 3 | 0 | 0 | \<Control Assessment Record\>, IR chapter |
| MA Maintenance | 9 | 0 | 32 of 64 | 23 | 4 | 5 | 0 | \<Control Assessment Record\>, MA chapter |
| MP Media Protection | 7 | 0 | 46 of 71 | 7 | 3 | 14 | 1 | \<Control Assessment Record\>, MP chapter |
| PE Physical and Environmental Protection | 18 | 0 | 54 of 121 | 6 | 0 | 61 | 0 | \<Control Assessment Record\>, PE chapter |
| PL Planning | 7 | 3 | 74 of 93 | 17 | 0 | 2 | 0 | \<Control Assessment Record\>, PL chapter |
| PS Personnel Security | 9 | 0 | 38 of 68 | 17 | 0 | 13 | 0 | \<Control Assessment Record\>, PS chapter |
| PT Personally Identifiable Information Processing and Transparency | 29 | 1 | 58 of 109 | 31 | 9 | 7 | 4 | \<Control Assessment Record\>, PT chapter |
| RA Risk Assessment | 10 | 2 | 49 of 73 | 13 | 9 | 2 | 0 | \<Control Assessment Record\>, RA chapter |
| SA System and Services Acquisition | 17 | 5 | 88 of 159 | 46 | 5 | 20 | 0 | \<Control Assessment Record\>, SA chapter |
| SC System and Communications Protection | 25 | 1 | 49 of 107 | 4 | 10 | 41 | 3 | \<Control Assessment Record\>, SC chapter |
| SI System and Information Integrity | 18 | 2 | 74 of 139 | 22 | 13 | 23 | 7 | \<Control Assessment Record\>, SI chapter |
| SR Supply Chain Risk Management | 12 | 0 | 56 of 81 | 16 | 4 | 5 | 0 | \<Control Assessment Record\>, SR chapter |
| **Total** | **316** | **19** | **1,083 of 1,998** | **390** | **157** | **306** | **62** |  |

A control counts as satisfied only when every one of its statements is satisfied or does not apply.

### 4.2 Controls fully satisfied

**Table 3: Controls fully satisfied**

| Family | Controls |
| --- | --- |
| AU | AU-3(1) |
| CM | CM-2(7), CM-3(4) |
| CP | CP-2(3), CP-2(8) |
| PL | PL-4(1), PL-10, PL-11 |
| PT | IR-8(1) |
| RA | RA-2, RA-9 |
| SA | SA-4(1), SA-4(2), SA-4(9), SA-15(3), SA-22 |
| SC | SC-2 |
| SI | SI-7(7), SI-10 |

### 4.3 Why statements are other than satisfied

**Table 4: Other than satisfied, by cause**

| Cause | Statements | What closes it |
| --- | --- | --- |
| Evidence from \<Organisation\>, or from the VMs once built | 306 | The answers to \<Evidence Requests\>, and the tests repeated on the VMs |
| Approved, but not yet operating; or a decision or approval is outstanding | 288 | Go-live: training, signatures, reviews, tests and exercises begin. The Head of Cyber's pending approvals |
| A gap in the system | 157 | The fixes in \<Plan of Action and Milestones\>, in the development phase |
| A first scheduled review that is not yet due | 57 | Time: the first yearly reviews fall due in November 2027. These are scored cautiously as other than satisfied |
| The policy or procedures have not yet been shared | 45 | The system owner shares them with their recipients, and records it |
| **Total** | **853** |  |

## 5 Risk position

**Table 5: Risks**

| Risk | Rating | Treatment | Status |
| --- | --- | --- | --- |
| R-AC-02 A user interferes with another user's session or abuses internal functions | High | Fix | Open; treatment in progress |
| R-AC-04 Someone gains full database control | High | Fix | Open; treatment in progress |
| R-AC-05 Credentials or documents are intercepted | High before production; low while only on localhost | Fix | Open; treatment in progress |
| R-AC-10 A stolen password gives full access | High | Accepted to 6 May 2027 (D-GEN-13); end state decided by the authorising official: multi-factor for administrators before production documents, and for all users by 6 May 2027 (D-IA-07) | Accepted to 6 May 2027; remediation planned |
| R-SI-01 A known flaw or malicious upload compromises the system | High | Fix | Open; treatment in progress |
| R-AC-01 A user reads documents outside their projects | Medium | Fix | Open; treatment in progress |
| R-AC-03 An outsider degrades the service without signing in | Medium | Fix | Open; treatment in progress |
| R-AC-06 People keep access they no longer need | Medium | Fix | Open; treatment in progress |
| R-AC-07 Administrator misuse goes unnoticed | Medium | Fix | Open; treatment in progress |
| R-AC-08 An unattended session is used by someone else | Medium | Fix | Open; treatment in progress |
| R-AC-11 The system cannot be authorised | Medium | Fix | Open; treatment in progress |
| R-AT-01 Someone makes a mistake, or is deceived, because they were not trained | Medium | Fix: no access without the briefing, and no privileged role without its modules (\<Awareness and Training Management\>) | Open; proposed on 12 November 2026, and the rating awaits the authorising official (D-RA-10) |
| R-AU-01 Audit records are changed or removed without detection | Medium | Fix (authorising official, D-AU-06) | Open; treatment in progress |
| R-AU-02 Personal data and live session IDs are exposed through the application log | Medium | Fix (authorising official, D-AU-06). Until then the application log is treated as audit information (\<Audit and Accountability Management\>) | Open; treatment in progress |
| R-CM-01 \<System Name\> runs software or settings that differ from the approved baseline, and nobody notices | Medium | Fix (authorising official, D-CM-10) | Open; treatment in progress |
| R-CP-01 Documents cannot be recovered after a failure | Medium | Fix | Open; treatment in progress |
| R-IR-01 An incident is not contained or reported in time | Medium | Fix: train, exercise and set up tracking before go-live | Open; proposed on 12 November 2026, and the rating awaits the authorising official (D-RA-10) |
| R-PT-01 Personal data is misused, kept too long, or relied on when wrong | Medium | Fix | Open; treatment in progress |
| R-SA-01 A flaw or unapproved change reaches production | Medium | Fix | Open; treatment in progress |
| R-SC-01 Stored documents or keys are read from a disk, backup or export copy | Medium | Fix | Open; proposed on 12 November 2026, and the rating awaits the authorising official (D-RA-10) |
| R-SR-01 A compromised or counterfeit component reaches the build | Medium | Fix (PA-94 proposed by the system owner; awaits the authorising official) | Open; proposed on 12 November 2026, and the rating awaits the authorising official (D-RA-10) |
| R-AC-09 Monitoring or legal action is challenged | Low | Fix | Open; treatment in progress |
| R-PE-01 Someone reaches the VMs or disks physically, or the site fails | Low | Obtain evidence | Open; treatment in progress |
| R-PS-01 Someone unsuitable holds access, or keeps it after moving or leaving | Low | Obtain evidence | Open; treatment in progress |

The 301 non-compliances behind these risks are rated 17 High, 56 Medium and 228 Low. The full register, with causes, consequences and decisions, is \<Risk List\>.

## 6 Weaknesses fixed or closed during the assessment

**Table 6: Items fixed or closed**

| Item | Rating | Weakness | Outcome |
| --- | --- | --- | --- |
| PA-01 | High | Any signed-in user can fetch any document page by number, with no project check. Page numbers restart in each project, so a request can also return the wrong project's page | Fixed on 5 November 2026 (T20, T21, T56 to T59); awaiting a repeat test on the VMs |
| PA-04 | High | Export job status, download and cancel do not check that the job belongs to the caller | Fixed on 5 November 2026 (T62); awaiting a repeat test on the VMs |
| PA-05 | Medium | Bad file reports have no project check. The list also fails for everyone with a database error | Fixed on 5 November 2026 (T23, T60, T61); awaiting a repeat test on the VMs |
| PA-08 | Low | The API document endpoint refuses access with a server error, not 403 | Fixed on 5 November 2026 (T14); awaiting a repeat test on the VMs |
| PA-09 | Medium | Document content is sent as publicly cacheable for an hour, so it can stay in shared caches and after sign-out | Fixed on 5 November 2026 (T22); awaiting a repeat test on the VMs |
| PA-27 | High | Export and upload checked access to the project named in a request but used a separately named schema, so an editor of one project could reach another | Fixed on 5 November 2026 (T63); awaiting a repeat test on the VMs |
| PA-24 | Low | The evidence describes uncommitted code on a local branch | Closed on 6 November 2026: committed and tagged v1.0 locally on 6 November 2026. Hashes are in \<System Security Plan\>, section 2 |
| PA-33 | Low | The 8-hour session limit check gave 200 in one full test run, then passed every other time. The cause was not found, so a real intermittent fault cannot yet be ruled out | Closed on 9 November 2026: the full run was repeated and passed five times in a row (I11). T45 now records its set-up result |

## 7 Evidence

Each script can be run again, and each evidence folder holds a README and a manifest of SHA-256 hashes for its results. A gap in a result is a real weakness, recorded in \<Plan of Action and Milestones\>. It is not a script failure.

**Table 7: Test scripts and results**

| Script | Families | Checks | Number | Passed | Gaps | Latest results |
| --- | --- | --- | --- | --- | --- | --- |
| Test-AccessControl.ps1 | AC | T01 to T55 | 75 | 52 | 23 | ac-test-results-2026-11-08-v1.0.csv, in the AC evidence |
| Test-AuditAndAuth.ps1 | AU, IA | A01 to A32 | 38 | 23 | 15 | au-ia-test-results-2026-11-08-v1.0.csv, in the AU and IA evidence |
| Test-Identification.ps1 | IA | I01 to I11 | 11 | 9 | 2 | ia-test-results-2026-11-09-v1.0.csv, in the AU and IA evidence |
| Test-ConfigurationManagement.ps1 | CM | C01 to C11 | 11 | 6 | 5 | cm-test-results-2026-11-08-v1.0.csv, in the SC and CM evidence |
| Test-BackupRestore.ps1 | CP | R01 to R09 | 9 | 7 | 2 | cp-test-results-2026-11-09-v1.0.csv, in the CP evidence |
| Test-IncidentReadiness.ps1 | IR | D01 to D08 | 8 | 5 | 3 | ir-test-results-2026-11-10-v1.0.csv, in the IR evidence |
| Test-Maintenance.ps1 | MA | M01 to M12 | 12 | 6 | 6 | ma-test-results-2026-11-10-v1.0.csv, in the MA evidence |
| Test-MediaProtection.ps1 | MP | P01 to P09 | 9 | 2 | 7 | mp-test-results-2026-11-10-v1.0.csv, in the MP evidence |
| Test-PersonalData.ps1 | PT | Q01 to Q10 | 10 | 3 | 7 | pt-test-results-2026-11-11-v1.0.csv, in the PT evidence |
| Test-Vulnerability.ps1 | RA, SI | V01 to V09 | 9 | 6 | 3 | ra-test-results-2026-11-11-after.csv, in the RA evidence |
| Test-Development.ps1 | SA | S01 to S10 | 10 | 2 | 8 | sa-test-results-2026-11-11-after.csv, in the SA evidence |
| Test-Protection.ps1 | SC | N01 to N12 | 12 | 1 | 11 | sc-test-results-2026-11-12-before.csv, in the SC evidence |
| Test-Integrity.ps1 | SI | H01 to H12 | 12 | 7 | 5 | si-test-results-2026-11-12-v1.0.csv, in the SI evidence |
| Test-SupplyChain.ps1 | SR | U01 to U10 | 10 | 3 | 7 | sr-test-results-2026-11-12-after.csv, in the SR evidence |
| Test-PlanConsistency.ps1 | All | L01 onward | Reported in the PL evidence | All | None | The PL evidence |
| **Total, apart from the consistency checks** |  |  | **236** | **132** | **104** |  |

## 8 Conditions before authorisation

1. TLS and secure cookies on every connection, and secrets removed from source (PA-18, PA-19), as the authorising official decided.
2. Sign-in through AD FS, with multi-factor authentication, shown working for every user before any production documents are held (D-AC-23, PA-95; D-IA-07).
3. Every other POA&M item whose latest completion is before go-live closed, including the packages with High advisories (PA-56) and backups (PA-64).
4. The VMs built, and the tests repeated on them.
5. \<Organisation\>'s evidence for the inherited controls received, and those controls accepted (\<Assessment, Authorization, and Monitoring Management\>, section 3.6).
6. The independent Level 2 assessment held, and this report replaced by its report.
7. The authorisation decision recorded on TPL-18, with its terms, conditions and end date.

## 9 Authorisation package

The authorising official receives: this report, whose section 2 is the executive summary; \<System Security Plan\>, the system security plan; \<Privacy Plan\>, the privacy plan; \<Control Assessment Record\>, the assessment record, with a chapter for each of the 19 families; \<Plan of Action and Milestones\>, the plan of action; \<Risk List\>, the risks; \<Decision Register\>, the decisions; and the evidence folders with their hash manifests. \<Assessment, Authorization, and Monitoring Management\>, section 3.5, lists the package and records the decision.
