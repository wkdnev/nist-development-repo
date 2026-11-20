# \<System Name\> Interview Guide

## 1 Purpose

CSS uses three assessment methods: examine, test and interview. These questions cover that method. The system owner's answers so far are in section 22.1. For this Level 1 assessment, the system owner answers them. The Level 2 assessor, \[Name\], may repeat them with the role holders named in \<Roles and Responsibilities\>. Ask each person how the control works in practice and to show a record. An answer alone is not evidence that a control operates.

After each interview, record it in section 2 and update the matching statements in \<Control Assessment Record\>, section AC.5, or the equivalent for the family.

Questions are numbered INT-XX-nn, where XX is the family code, and each names the statements it supports. The people to interview come from the Interview objects in CSS.

**Table 1: Family coverage**

| Family | Section | State |
| --- | --- | --- |
| AC Access Control | 4 | All answered by the system owner at Level 1; role holders not interviewed |
| AT Awareness and Training | 5 | Answered by the system owner at Level 1 |
| AU Audit and Accountability | 6 | Answered by the system owner at Level 1 |
| CA Assessment, Authorization and Monitoring | 7 | Answered by the system owner at Level 1 |
| CM Configuration Management | 8 | Answered by the system owner at Level 1 |
| CP Contingency Planning | 9 | Answered by the system owner at Level 1 |
| IA Identification and Authentication | 10 | Answered by the system owner at Level 1 |
| IR Incident Response | 11 | Answered by the system owner at Level 1 |
| MA Maintenance | 12 | Answered by the system owner at Level 1 |
| MP Media Protection | 13 | Answered by the system owner at Level 1 |
| PE Physical and Environmental Protection | 14 | Answered by the system owner at Level 1 |
| PL Planning | 15 | Answered by the system owner at Level 1 |
| PS Personnel Security | 16 | Answered by the system owner at Level 1 |
| PT Personally Identifiable Information | 17 | Answered by the system owner at Level 1 |
| RA Risk Assessment | 18 | Answered by the system owner at Level 1 |
| SA System and Services Acquisition | 19 | Answered by the system owner at Level 1 |
| SC System and Communications Protection | 20 | Answered by the system owner at Level 1 |
| SI System and Information Integrity | 21 | Answered by the system owner at Level 1 |
| SR Supply Chain Risk Management | 22 | Answered by the system owner at Level 1 |

## 2 Interview log

**Table 2: Interview log**

| Date | Family | Person and role | Interviewer | Questions covered | Records seen | Notes reference |
| --- | --- | --- | --- | --- | --- | --- |
| 5 November 2026 | AC | \[Name\], system owner | Written questions, Level 1 | INT-AC-01 to 06 | None | Section 22.1, Table 29 |
| 5 November 2026 | AC | \[Name\], answering for the global administrator | Written questions, Level 1 | INT-AC-07 to 12 | None | Section 22.1, Table 29 |
| 5 November 2026 | AC | \[Name\], answering for the project access approver | Proposed answers, Level 1 | INT-AC-13 to 15 | None | Section 22.1, Table 29 |
| 5 November 2026 | AC | \[Name\], answering for the auditor, security officer, administrators and developers | Proposed answers, Level 1 | INT-AC-16 to 26 | None | Section 22.1, Table 29 |
| 5 November 2026 | AC | \[Name\], answering for \<Organisation\>'s security contact and sample users | Proposed answers, Level 1 | INT-AC-27 to 34 | None | Section 22.1, Table 29 |
| 6 November 2026 | AU, IA | \[Name\], answering for each role | Proposed answers, Level 1 | INT-AU-01 to 06, INT-IA-01 to 06 | None | Section 22.2, Table 30 |
| 6 November 2026 | AC, AU, IA | \[Name\], \[Name\], \[Name\], \[Name\], \[Name\], \[Name\], \[Name\], \[Name\], \[Name\], \[Name\], \[Name\] and \[Name\] | Meeting, reported by the system owner | Confirmed their roles and the answers given for them | None | Sections 22.1 and 22.2; \<Evidence Requests\>, section 23 |
| 6 November 2026 | SC, CM | \[Name\], answering for each role | Proposed answers, Level 1 | INT-SC-01 to 06, INT-CM-01 to 08 | None | Section 22.3, Table 31 |
| 6 November 2026 | SI, RA, CA | \[Name\], answering for each role | Proposed answers, Level 1 | INT-SI-01 to 06, INT-RA-01 to 05, INT-CA-01 to 05 | None | Section 22.4, Table 32 |
| 6 November 2026 | IR, CP, AT | \[Name\], answering for each role | Proposed answers, Level 1 | INT-IR-01 to 04, INT-CP-01 to 04, INT-AT-01 to 04 | None | Section 22.5, Table 33 |
| 6 November 2026 | MA, MP, PE | \[Name\], answering for each role | Proposed answers, Level 1 | INT-MA-01 to 05, INT-MP-01 to 03, INT-PE-01 to 04 | None | Section 22.6, Table 34 |
| 6 November 2026 | PL, PS | \[Name\], answering for each role | Proposed answers, Level 1 | INT-PL-01 to 04, INT-PM-01, INT-PS-01 to 05 | None | Section 22.7, Table 35 |
| 6 November 2026 | PT, SA, SR | \[Name\], answering for each role | Proposed answers, Level 1 | INT-PT-01 to 05, INT-SA-01 to 05, INT-SR-01 to 04 | None | Section 22.8, Table 36 |

## 3 Access Control (AC)

### 3.1 System owner

**Table 3: Questions for the system owner**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-01 | Who approved the policy and procedures, and how were they shared? | AC-01a, AC-01b | Approval and distribution record |
| INT-AC-02 | When were they last reviewed, and what would trigger another review? | AC-01c | Review record, change record |
| INT-AC-03 | How do you decide who holds privileged roles? | AC-02e, AC-06(05) | Approved access list, TPL-2 records |
| INT-AC-04 | How are duties separated, and where does staffing prevent it? | AC-05a, AC-05b | Roles document, risk acceptance |
| INT-AC-05 | How do you decide whether a non-compliance is accepted or remediated? | All; PRO-AC-17 | Decision register, TPL-1 records |
| INT-AC-06 | What is allowed on external systems and portable storage? | AC-20, AC-20(02) | P-AC-22, any approvals |

### 3.2 Global administrators (account managers)

**Table 4: Questions for global administrators**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-07 | Take me through creating an account. What do you need before you start? | AC-02c, AC-02e, AC-02f | A recent TPL-2 record and its audit entry |
| INT-AC-08 | How do you learn that someone has left or moved, and how quickly? | AC-02h, AC-02l, AC-02(03) | Recent notice and the change it caused |
| INT-AC-09 | What would you do if told someone is a high risk, right now? | AC-02(13) | PRO-AC-4, last walk-through |
| INT-AC-10 | How do you find inactive accounts? | AC-02(03)(d) | PRO-AC-8 records |
| INT-AC-11 | Do you use your administrator account for everyday document work? | AC-06(02) | Your two accounts |
| INT-AC-12 | Who checks your own actions? | AC-05b, AC-06(09) | Auditor's review record |

### 3.3 Project access approvers

**Table 5: Questions for project access approvers**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-13 | How do you decide who may read or edit your project? | AC-02i, AC-03 | TPL-2 records |
| INT-AC-14 | When did you last review who has access, and what changed? | AC-02j, AC-06(07) | TPL-3 record |
| INT-AC-15 | How do you decide whether a document can be shared outside the project? | AC-21a, AC-21b | PRO-AC-16 record |

### 3.4 Auditors and security officers

**Table 6: Questions for auditors and security officers**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-16 | How do you monitor account use, and how often? | AC-02g | Weekly review record |
| INT-AC-17 | Which privileged actions do you look for, and what would you do on finding a problem? | AC-06(09) | Review record, escalation |
| INT-AC-18 | Are there actions you cannot see in the log? | AC-02(04), AC-06(09) | Known gaps; PA-14 |

### 3.5 Windows server and database administrators

**Table 7: Questions for Windows server and database administrators**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-19 | Who has administrator rights on each VM and in PostgreSQL? | AC-06(01), AC-06(05) | Group and role listings |
| INT-AC-20 | What rights do the application service accounts have? | AC-06 | Service account and database role settings |
| INT-AC-21 | From where, and how, do you administer the VMs? | AC-17, AC-17(04) | Administration route; firewall rules |
| INT-AC-22 | What are the logon lockout, banner and screen lock settings? | AC-07, AC-08, AC-11 | Policy export |
| INT-AC-23 | How are your privileged actions logged? | AC-06(09) | Sample log |

### 3.6 Developers

**Table 8: Questions for developers**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-24 | How do you make sure a new page or endpoint needs the right access? | AC-03, AC-06(10) | Code review practice, test checks |
| INT-AC-25 | Do you have any access to production? | AC-05a, AC-06 | Approved access list |
| INT-AC-26 | How are diagnostic pages kept out of production? | AC-06(10), AC-14 | Build settings; PA-07 |

### 3.7 \<Organisation\> security contact

**Table 9: Questions for \<Organisation\>'s security contact**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-27 | Does the Cyber Essentials Plus scope include these VMs and their hosting? | Inherited controls | EV-GEN-02 |
| INT-AC-28 | Who controls firewalls, and how are rule changes approved? | AC-04 | EV-AC-03 |
| INT-AC-29 | How do people reach internal systems remotely, and how is that monitored? | AC-17, AC-17(01) to (03) | EV-AC-08 to EV-AC-11 |
| INT-AC-30 | How are wireless, mobile devices and USB storage controlled? | AC-18, AC-19, AC-20(02) | EV-AC-13 to EV-AC-17 |
| INT-AC-31 | How do leavers and movers reach the system owner? | AC-02h, AC-02l | EV-AC-01 |

### 3.8 Sample users

**Table 10: Questions for sample users**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-32 | Have you read the SyOPS, and did you sign it? | AC-01a, AC-02c | Signed acknowledgement |
| INT-AC-33 | What do you do if you can see a document you should not? | AC-03 | None |
| INT-AC-34 | Do you use \<System Name\> from a phone, or a personal device, or copy documents to USB? | AC-19, AC-20 | None |

## 4 Awareness and Training (AT)

These questions have not been asked yet.

**Table 11: AT questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-AT-01 | System owner | How do you know each user completed training before getting access? | AT-02, AT-04 | TPL-9 records |
| INT-AT-02 | Security officer | What role training has been given, and how is its content kept up to date? | AT-03, AT-04 | \<Awareness and Training Management\> (role curriculum and training matrix), module content and TPL-9 records |
| INT-AT-03 | A sample of users | How would you recognise and report social engineering or an insider threat? | AT-02(02), AT-02(03) | The \<System Name\> briefing scenarios (\<Awareness and Training Management\>, section 3.3) |
| INT-AT-04 | Security officer | How do you know the training works, and what changed after the last incident or review? | AT-01, AT-02, AT-03 | Training measures on TPL-8 (\<Awareness and Training Management\>, section 3.9) |

## 5 Audit and Accountability (AU)

**Table 12: AU questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-AU-01 | System owner | How do you decide which events are logged, and why are they enough? | AU-02d, AU-12b | \<Audit and Accountability Management\>, review record |
| INT-AU-02 | Auditor | Show me your last weekly review. What did you find, and whom did you tell? | AU-06a, AU-06b | Review record |
| INT-AU-03 | Auditor | How do you know the records have not been changed? | AU-09a, AU-09b | Chain check result |
| INT-AU-04 | Windows server administrator | What happens when logging fails? Who is told, and how quickly? | AU-05 | An alert and its response |
| INT-AU-05 | Database administrator | How long are records kept, and how is capacity checked? | AU-04, AU-11 | Capacity record, backup |
| INT-AU-06 | \<Organisation\>'s security contact | Is there central monitoring, and which time source do the VMs use? | AU-06(01), AU-06(03), AU-08 | EV-AU-01, EV-AU-02 |

## 6 Assessment, Authorization and Monitoring (CA)

Role holders have not been interviewed. Answers are in section 22.4.

**Table 13: CA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-CA-01 | Security assessor | Have you had any part in building or running \<System Name\>? | CA-02(01), CA-07(01) | TPL-19 independence statement |
| INT-CA-02 | Authorising official | What did you rely on to authorise \<System Name\>, and which risks did you accept? | CA-06c | TPL-18 authorisation decision, and \<Security Assessment Report\> |
| INT-CA-03 | System owner | How is the plan kept up to date, and when did it last change? | CA-05b | \<Plan of Action and Milestones\> history |
| INT-CA-04 | Security officer | Show me the last monitoring report on TPL-8, and any measure past its threshold. Who received it? | CA-07 | Monitoring report |
| INT-CA-05 | System owner | Which systems connect to \<System Name\>, and who approved them? | CA-03, CA-09 | Interface record |

## 7 Configuration Management (CM)

Role holders have not been interviewed. Answers are in section 22.3.

**Table 14: CM questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-CM-01 | System owner | How is a change approved, who reviews it, and how are records kept? | CM-03, CM-04 | A ServiceNow change record |
| INT-CM-02 | Developers | How is a release tested and verified before it goes live? | CM-03(02), CM-04(02) | A release test record |
| INT-CM-03 | Windows server administrator | What is the baseline for each VM, and which secure settings are applied? | CM-02, CM-06 | Baseline, CIS Benchmark result |
| INT-CM-04 | Windows server administrator | Who can make changes to the VMs, and how is that restricted? | CM-05 | Access list, EV-CM-01 |
| INT-CM-05 | Developers | Which functions have been removed or turned off, and when was that last reviewed? | CM-07, CM-07(01) | Functions review record |
| INT-CM-06 | Windows server administrator | How is software approved and installed, and how is the list kept up to date? | CM-07(02), CM-07(05), CM-11 | Approved software list, an approval |
| INT-CM-07 | Windows server administrator | How is the inventory kept accurate? | CM-08, CM-08(01) | Inventory |
| INT-CM-08 | \<Organisation\>'s security contact | How are unauthorised components found, and how are licences tracked? | CM-08(03), CM-10, CM-12(01) | EV-CM-02, EV-CM-03 |

## 8 Contingency Planning (CP)

These questions have not been asked yet.

**Table 15: CP questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-CP-01 | System owner | When would you invoke the plan, and who would you tell? | CP-02 | \<Contingency Planning Management\> |
| INT-CP-02 | Database administrator | How are backups taken and protected, and when was the last restore test? | CP-09, CP-09(01), CP-09(08) | Backup log and restore record |
| INT-CP-03 | Windows server administrator | How would you rebuild the VMs, and how long would it take? | CP-07, CP-10 | Test record |
| INT-CP-04 | \<Organisation\>'s IT service desk | Where is the second site, and what connects it? | CP-06, CP-07, CP-08 | EV-CP-01, EV-CP-02 |

## 9 Identification and Authentication (IA)

**Table 16: IA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-IA-01 | \<Organisation\>'s IT service desk | How do you check who someone is before resetting their password or second factor? | IA-05a, IA-05d | PRO-IA-2 record |
| INT-IA-02 | \<Organisation\>'s IT service desk | What happens to an Active Directory account name when someone leaves? Is it ever given to another person? | IA-04d | \<Organisation\>'s record (EV-AC-01) |
| INT-IA-03 | Sample user | What would you do if you thought your password was known? | IA-05f, IA-05h | None |
| INT-IA-04 | Windows server administrator | When were the signing key and service secrets last changed? | IA-05f, IA-05(06) | Rotation record |
| INT-IA-05 | \<Organisation\>'s security contact | How are devices identified on the network? | IA-03 | EV-IA-01 |
| INT-IA-06 | \<Organisation\>'s HR | What identity evidence do you check, and how are people told? | IA-12, IA-12(02), IA-12(03), IA-12(05) | EV-IA-02 |
| INT-IA-07 | Developers, with \<Organisation\>'s security contact | Show me a sign-in through PingFederate from start to finish. What does \<System Name\> check in the OpenID Connect response, and what happens if I present the same response twice? | IA-02, IA-02(01), IA-02(08) | The trust settings (\<Identification and Authentication Management\>, section 3.3); a test record |

## 10 Incident Response (IR)

These questions have not been asked yet.

**Table 17: IR questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-IR-01 | Security officer | Talk me through what happens when someone reports an incident | IR-04, IR-05, IR-08 | \<Incident Response Management\>, and an incident ticket |
| INT-IR-02 | Security officer | When was the last exercise, and what changed as a result? | IR-03, IR-03(02), IR-04c | Exercise record |
| INT-IR-03 | Legal adviser | How do you decide whether to tell the ICO, and how quickly can you? | IR-06 | Reporting record |
| INT-IR-04 | \<Organisation\>'s security contact | How do reports reach you, and what help do you give? | IR-06, IR-07 | EV-IR-01 |

## 11 Maintenance (MA)

These questions have not been asked yet.

**Table 18: MA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-MA-01 | Windows server administrator | Show me the record for the last maintenance. Who approved it, and who checked the controls afterwards? | MA-02 | Change record and TPL-12 |
| INT-MA-02 | Windows server administrator | Which tools are approved, and how are they checked? | MA-03, MA-03(01), MA-03(02) | Tool list |
| INT-MA-03 | System owner | How does remote maintenance get approved, watched and ended? | MA-04 | Change record and session logs |
| INT-MA-04 | System owner | Who may maintain \<System Name\>, and how is anyone else supervised? | MA-05 | Approved list |
| INT-MA-05 | \<Organisation\>'s IT service desk | How quickly can support and parts arrive, and how is equipment sanitised before it leaves? | MA-02d, MA-06 | EV-MA-01 |
| INT-MA-06 | Security officer | How do you review the maintenance records and the remote session logs, and what happens when a job has no change record? | MA-02a, MA-04a | TPL-12 reviews; session logs |
| INT-MA-07 | Global administrator | When did you last use a built-in maintenance page? Who approved it, who was present, and where is it recorded? | MA-03a | Change record and TPL-12 |

## 12 Media Protection (MP)

These questions have not been asked yet.

**Table 19: MP questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-MP-01 | A sample of users | What do you do with a printed Restricted document? | MP-02, MP-03, MP-04, MP-06 | Locked storage and shredder |
| INT-MP-02 | Database administrator | Where do backup media go, and who can reach them? | MP-02, MP-04, MP-05 | EV-MP-01 |
| INT-MP-03 | \<Organisation\>'s IT service desk | How are disks and backup media sanitised, and how is USB blocked? | MP-06, MP-07 | EV-MP-02, EV-MP-03 |
| INT-MP-04 | Windows server administrator | Show me the export folder on the application VM and your last check. What do you do with a copy older than 24 hours? | MP-04, MP-06 | TPL-8 (C49) |
| INT-MP-05 | System owner | When did you last review the media inventory, and check a sample of sanitising certificates against the media records? | MP-02, MP-06 | Inventory review; TPL-13 |

## 13 Physical and Environmental Protection (PE)

These questions have not been asked yet.

**Table 20: PE questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PE-01 | \<Organisation\>'s security contact | Who can enter the data centre and the second site, how are they monitored, are both covered by your ISO/IEC 27001 certificate (Annex A.7) or SOC 2 report, and how would \<System Name\>'s security officer hear about an incident? | PE-02, PE-03, PE-06, PE-08 | EV-PE-01 |
| INT-PE-02 | \<Organisation\>'s security contact | What happens to the data centre in a power failure, fire or flood? | PE-09 to PE-15 | EV-PE-02, EV-PE-03 |
| INT-PE-03 | Security officer | How are home working controls assessed each year with TPL-4, is anyone printing at home, and how do people raise concerns? | PE-17 | Assessment record |
| INT-PE-04 | \<Organisation\>'s facilities contact | Which managed printers with secure release can \<System Name\> users print to, and where are they? | PE-05 | EV-PE-05 |
| INT-PE-05 | A sample of people who work from home | Where do you work when at home? What would you do if you needed to print, or if your laptop was lost? | PE-05, PE-17 | Home working checklist (TPL-4) |

## 14 Planning (PL)

These questions have not been asked yet.

**Table 21: PL questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PL-01 | System owner | When was the plan last reviewed, and who received it? | PL-02b, PL-02c | Change record, and distribution record |
| INT-PL-02 | A sample of users | Which rules did you sign, and when? | PL-04 | Signed acknowledgement |
| INT-PL-03 | System owner | How do you decide whether a control can be tailored? | PL-11 | \<Tailoring Register\> |
| INT-PL-04 | A sample of users and an administrator | Which version of the rules did you sign, and when? Can you name two rules that apply to you? Have you been asked to sign again after a change? | PL-4b, PL-4d, PL-4(1) | TPL-21 and the register of signatures in \<Planning Management\>, section 3.5 |
| INT-PL-05 | Head of Cyber | Have you seen the System Security Plan, and do you concur with it? How are you told when it changes? | PL-02a.15, PL-02b | The plan's approval in \<Decision Register\> and the plan review record |
| INT-PM-01 | Head of Cyber | Where is \<Organisation\>'s security programme written down, what is its risk appetite, is \<System Name\> in the system inventory, and who is the data protection officer? Do \<System Name\>'s risk thresholds fit the appetite? | PM-1, PM-2, PM-5, PM-9, PM-19 (inherited; \<Program Management\>, section 3.3) | EV-PM-01, EV-PM-02, EV-PM-04 |
| INT-PM-02 | Legal adviser | Is there a privacy programme plan, and who leads it? Where is \<System Name\>'s HR data in the record of processing? How do complaints and breaches reach the people who must be told? | PM-5(1), PM-18, PM-19, PM-26, PM-27 (inherited; \<Program Management\>, section 3.3) | EV-PM-02, EV-PM-04 |

## 15 Personnel Security (PS)

These questions have not been asked yet.

**Table 22: PS questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PS-01 | \<Organisation\>'s HR | What screening is done before someone starts, and when is it repeated? | PS-02b, PS-03 | EV-PS-01 |
| INT-PS-02 | Global administrator | Show me the last leaver and the last mover. When were you told, and when were the Active Directory account disabled, the group memberships changed and the PingFederate sign-in ended? | PS-04, PS-05 | TPL-14 and audit records |
| INT-PS-03 | System owner | Show me the signed agreement for a sample of people | PS-06 | Signed agreements |
| INT-PS-04 | \<Organisation\>'s HR | How are exit interviews and disciplinary action handled, and do job descriptions state security duties? | PS-04c, PS-08, PS-09 | EV-PS-02 |
| INT-PS-05 | System owner | How do you check that external people meet their contract terms? | PS-07 | EV-PS-03 |
| INT-PS-06 | A line manager | When one of your people changes role or leaves, whom do you tell, how, and how quickly? | PS-04, PS-05 | TPL-14 |

## 16 Personally Identifiable Information (PT)

These questions have not been asked yet.

**Table 23: PT questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PT-01 | Legal adviser | What is the lawful basis, and is consent ever relied on? | PT-02, PT-04 | The written position |
| INT-PT-02 | Legal adviser | Where is the impact assessment, and what does it say about special category data? | RA-08, PT-07 | The assessment |
| INT-PT-03 | Legal adviser | Show me a request from an individual. How was it handled? | AC-03(14), SI-18(04) | A request record |
| INT-PT-04 | Business owner | What personal data do projects hold, for how long, and who checks it is correct? | PT-03, SI-12(01), SI-18 | Retention periods and the last check |
| INT-PT-05 | Developers | What personal data is in audit records and test data? | AU-03(03), SI-12(02) | A sample of each |
| INT-PT-06 | Legal adviser | Show me a data protection complaint. Was it acknowledged within 30 days, and how was it resolved? | PT-01, PM-26 | A complaint record (TPL-22) |
| INT-PT-07 | Administrator who would handle a request | Show me how you would find every document about one person, and how you would record a correction or deletion | AC-03(14), SI-18(04) | TPL-15; audit records |
| INT-PT-08 | Data protection officer | What advice did you give on the impact assessment, and what changed as a result? | RA-08, PT-02 | The impact assessment |

## 17 Risk Assessment (RA)

Role holders have not been interviewed. Answers are in section 22.4.

**Table 24: RA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-RA-01 | System owner | How is risk reviewed, and who sees the result? | RA-03d, RA-03e | Review record |
| INT-RA-02 | Authorising official | How did you reach the Moderate categorisation? | RA-02 | \<System Security Plan\>, section 3.3 |
| INT-RA-03 | Windows server administrator | Show me the last scan. How quickly were findings fixed? | RA-05, RA-05(05) | Scan report |
| INT-RA-04 | Security officer | How would someone report a vulnerability, and what happens next? | RA-05(11) | Route, a sample report |
| INT-RA-05 | Developers | How do you judge the risk of a new package? | RA-03(01) | Supply chain review |
| INT-RA-06 | Security officer | A flaw in a component \<System Name\> uses was added to CISA's exploited list today. Walk me through the next 3 days | RA-05d, SI-02 | A TPL-7 record and the emergency change |
| INT-RA-07 | System owner | Show me the critical components and how they were chosen. What changed when sign-in moved to PingFederate? | RA-09 | \<Risk Assessment Management\>, section 3.9; TPL-23 |
| INT-RA-08 | Authorising official | How do you decide whether to accept a risk, and how do you know the decision fits \<Organisation\>'s risk appetite? | RA-07, RA-03b | \<Risk List\>, sections 3 and 4.2; \<Decision Register\> |

## 18 System and Services Acquisition (SA)

These questions have not been asked yet.

**Table 25: SA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-SA-01 | Developers | Walk me through a recent change, from plan to release | SA-03, SA-10, SA-15 | The ServiceNow record and pull request |
| INT-SA-02 | Developers | What tests run at a release, and where are the results? | SA-11 | The latest results |
| INT-SA-03 | System owner | How are security and privacy costs raised and funded? | SA-02 | The budget request |
| INT-SA-04 | System owner | How do you check that providers keep to their contracts? | SA-04, SA-09 | The last review |
| INT-SA-05 | Developers | How do you know a component is nearing the end of its support? | SA-22 | The monthly check |
| INT-SA-06 | Developers | Show me how the default branch is protected, and the review on the last change merged to it | SA-10, CM-3 | The GitHub branch settings and the latest Test-Development.ps1 results |
| INT-SA-07 | \<Organisation\>'s contract owner | Show me the security and privacy terms in the agreement for \<System Name\>'s hosting and services, and how \<Organisation\> shows it keeps to them | SA-04, SA-09 | The agreement; service level reports |
| INT-SA-08 | Security officer | Which designs have you checked against the engineering principles, and what changed as a result? | SA-03d, SA-08 | TPL-6 records of design checks |

## 19 System and Communications Protection (SC)

Role holders have not been interviewed. Answers are in section 22.3.

**Table 26: SC questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-SC-01 | Developers | Which traffic is encrypted, and how are certificates renewed? | SC-08, SC-08(01), SC-23 | VM configuration, certificate record |
| INT-SC-02 | Developers | Where are keys held, who can reach them, and how are they rotated? | SC-12 | Key record |
| INT-SC-03 | Developers | Which scripts can pages load, and how would you notice an unapproved one? | SC-18 | Page policy, PA-51 |
| INT-SC-04 | Windows server administrator | Is disk encryption on, and how are recovery keys protected? | SC-28, SC-28(01) | BitLocker status on both VMs |
| INT-SC-05 | \<Organisation\>'s security contact | What protects the boundary, and how are exceptions approved? | SC-07, SC-07(03), SC-07(04), SC-07(05) | EV-SC-02 |
| INT-SC-06 | \<Organisation\>'s security contact | What protects against denial of service, and how is DNS protected? | SC-05, SC-20, SC-21, SC-22 | EV-SC-01, EV-SC-05 |
| INT-SC-07 | Windows server administrator | Show me where each key in the register is kept, when it was last changed, and how the data protection key rings are protected | SC-12, SC-13 | \<System and Communications Protection Management\>, section 3.4, and the TPL-6 records of key changes |
| INT-SC-08 | Windows server administrator | Show me each server's host firewall rules, and how they match the allow-lists | SC-07, SC-07(05) | The host firewall rules; \<System and Communications Protection Management\>, section 3.2 |

## 20 System and Information Integrity (SI)

Role holders have not been interviewed. Answers are in section 22.4.

**Table 27: SI questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-SI-01 | Developers | How do you find out a package has a flaw, and how quickly is it fixed? | SI-02a, SI-02c | Package check, change record |
| INT-SI-02 | Windows server administrator | How are updates tested, and is Defender running on both VMs? | SI-02b, SI-03 | Update and Defender records |
| INT-SI-03 | Security officer | Show me your last log review. Which detection use case would raise an alert, who is told, and what did you do about the last one? | SI-04d, SI-04(05) | TPL-8 review record, an alert and its PRO-SI-4 response |
| INT-SI-04 | Security officer | Which advisories do you receive, and what did you do about the last one? | SI-05 | Advisory record |
| INT-SI-05 | Developers | How are inputs checked, and what does a user see when something fails? | SI-10, SI-11 | Test results |
| INT-SI-06 | \<Organisation\>'s security contact | What monitors traffic, and how are firmware updates handled? | SI-04(04), SI-02c | EV-SI-01, EV-SI-02 |
| INT-SI-07 | Security officer | Show me the integrity baseline for the running release. How would you know a release package, a document or an audit record had been changed? | SI-07a, SI-07(01), SI-07(07) | \<System and Information Integrity Management\>, section 3.5; the Test-Integrity.ps1 baseline; a TPL-8 integrity check |
| INT-SI-08 | Developers | Upload the EICAR test file and show me what happens, and where it is recorded | SI-03 | The refused upload; the audit record; the alert |

## 21 Supply Chain Risk Management (SR)

These questions have not been asked yet.

**Table 28: SR questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-SR-01 | System owner | Who is on the supply chain team, and when did it last meet? | SR-02, SR-02(01) | Minutes |
| INT-SR-02 | Developers | Where does each package come from, and how do you know the restore got exactly what the lock file records? | SR-03, SR-05 | A recent example |
| INT-SR-03 | Security officer | What happens when a supplier reports a compromise? | SR-08 | EV-SR-01 |
| INT-SR-04 | \<Organisation\>'s IT service desk | How is hardware inspected, repaired and disposed of? | SR-10, SR-11(02), SR-12 | EV-SR-02 |
| INT-SR-05 | Developers | Show me the bill of materials for the release I am looking at, and how you checked that release against it before installation | SR-03b, SR-10 | The bill of materials; Test-SupplyChain.ps1 results |
| INT-SR-06 | System owner | Show me the last review of \<Organisation\> as a supplier, and what changed as a result | SR-06, SR-02(01) | TPL-16 |

## 22 Answers given at Level 1

The answers are kept in the order they were given, so that each batch stays with its date. The interview log in section 2 points to each batch.

### 22.1 AC answers

The system owner gave these answers in writing on 5 November 2026, including those for the global administrator (INT-AC-07 to 12) and for the other roles (INT-AC-13 to 34). Later answers were proposed from the documents and agreed or changed by the system owner, and the Level 2 assessor should treat them as such. No records were seen, so they do not change any finding in \<Control Assessment Record\>, section AC.5.

**Table 29: System owner's answers**

| ID | Answer as given | Clarified by the system owner | Position |
| --- | --- | --- | --- |
| INT-AC-01 | Policy and procedures approved by Head of Cyber \[Name\] | \[Name\] approved only the policy, as the Head of Cyber approves all policies. The system owner approved the procedures | No record exists yet, so \[Name\] is to confirm it in \<Decision Register\>. How they were shared was not stated, and they are recorded as not yet shared |
| INT-AC-02 | 6 months (reviewed annually) | Issued on 5 November 2026 and reviewed annually | Consistent with P-AC-02 and P-AC-03. First review not yet due |
| INT-AC-03 | System owner decides | None needed | Consistent with P-AC-05. Record to be seen |
| INT-AC-04 | No person has multiple roles | \[Name\] is not a developer | Consistent with \<Roles and Responsibilities\>. Test T75 still shows a global administrator holds all rights in the system |
| INT-AC-05 | Default is non-compliance | Confirmed: a control counts as non-compliant until shown otherwise. Accept or remediate is decided under \<Risk List\>, section 4 | Consistent |
| INT-AC-06 | Nothing | Keep the approved rule: not allowed without the system owner's approval | Consistent with P-AC-22. No approvals given |
| INT-AC-07 | Full workflow approval using ServiceNow | Planned for go-live, using ServiceNow electronic approval workflows | PRO-AC-1, 2, 5 and 6 rewritten in version \<ver\>, now approved. ServiceNow is owned by \<Organisation\>'s IT service desk. Not yet set up, so no record exists. Movers use a ServiceNow change request |
| INT-AC-08 | Prompt from Starters/Leavers system | Planned. The global administrator is prompted and acts within a week. The corporate network account is disabled immediately, so the person could not get access | P-AC-06 changed to 5 working days for leavers, once \<Organisation\> evidences the immediate disable (EV-AC-01), and 1 working day for movers |
| INT-AC-09 | Disable access | None needed | Consistent with PRO-AC-4 and P-AC-13. Walk-through to be seen |
| INT-AC-10 | Check last login data | None needed | Consistent with PRO-AC-8, a monthly manual check. PRO-AC-8 records to be seen. Test T43 shows the system does not disable inactive accounts itself |
| INT-AC-11 | No | None needed | Consistent with P-AC-18. The two accounts are to be seen; PA-17 records them as not yet issued |
| INT-AC-12 | \[Name\] | An extra check, alongside the auditor and system owner | Consistent with \<Access Control Management\>. \[Name\]'s check is every 3 months, recorded on TPL-3 (proposed answer, agreed by the system owner). No record yet |
| INT-AC-13 | The line manager confirms the need in ServiceNow, and the approver approves only if the person needs that level of access for their work | Proposed answer, agreed by the system owner | Consistent with PRO-AC-5. Planned; no record yet |
| INT-AC-14 | None yet, because \<System Name\> is not live. The first is at go-live, then every 12 months, or every 3 months for privileged groups | Proposed answer, agreed by the system owner | Consistent with P-AC-07. No review exists (PA-16) |
| INT-AC-15 | The approver checks the recipient and the document's restrictions, decides under PRO-AC-16 and records it. Nothing leaves without approval | Proposed answer, agreed by the system owner | Consistent with PRO-AC-16. Restrictions are not recorded on documents (PA-22) |
| INT-AC-16 | A weekly review of the audit logs in the admin portal, starting at go-live. Not yet started | Proposed answer, agreed by the system owner | Consistent with \<Security Operating Procedures\>. No record yet |
| INT-AC-17 | Repeated failed sign-ins, lockouts, refused access, unusual sign-in times, account and privilege changes, password resets, large exports, and records under unknown names or "System". Anything unexplained is raised as a security incident | Proposed answer, agreed by the system owner | Consistent with \<Security Operating Procedures\>. No record yet |
| INT-AC-18 | Yes. Many privileged actions are not logged, and ordinary users can add records | Proposed answer, agreed by the system owner | Consistent with PA-14 and PA-29 |
| INT-AC-19 | \[Name\] on the VMs and \[Name\] in PostgreSQL, once the VMs are built | Proposed answer, agreed by the system owner | Consistent with \<Roles and Responsibilities\>. Listings to be seen on the VMs |
| INT-AC-20 | Today the applications share a database superuser role in Docker. Least-privilege accounts are planned for the VMs | Proposed answer, agreed by the system owner | Consistent with T55 and PA-10 |
| INT-AC-21 | Only from inside \<Organisation\>'s network, once built | Proposed answer, agreed by the system owner | Consistent with D-AC-08 and TR-AC-05, which await the authorising official. Evidence is EV-AC-12 |
| INT-AC-22 | Not set yet. They will match the approved values: 5 attempts, a 15-minute lock, the approved notice, and a lock after 25 minutes | Proposed answer, agreed by the system owner | Consistent with D-AC-P14 to P16. Policy export to be seen on the VMs |
| INT-AC-23 | Windows and PostgreSQL logs, checked weekly. To be confirmed with \<Organisation\>, which may monitor them centrally | Proposed answer, agreed by the system owner | Consistent with \<Security Operating Procedures\>. Sample log to be seen |
| INT-AC-24 | Each page and endpoint declares its access rule, and the access control test script checks it. Known gaps remain open | Proposed answer, agreed by the system owner | Gaps are PA-03, PA-06 and PA-29. PA-02 is closed, as the design has no session functions |
| INT-AC-25 | None | Proposed answer, agreed by the system owner | Consistent with \<Access Control Management\>. Approved access list not yet built (D-AC-14) |
| INT-AC-26 | Not yet kept out of production | Proposed answer, agreed by the system owner | Consistent with PA-07 |
| INT-AC-27 | \<Organisation\> holds Cyber Essentials Plus. Whether it covers the two VMs and their hosting is not yet confirmed | Proposed answer, agreed by the system owner | Not from \<Organisation\>. Evidence is EV-GEN-02 |
| INT-AC-28 | \<Organisation\>'s network team controls firewalls, and rule changes go through its change process | Proposed as a best guess, agreed by the system owner | Not from \<Organisation\>. Evidence is EV-AC-03 |
| INT-AC-29 | Through \<Organisation\>'s managed remote access service, monitored by \<Organisation\>. Details are to come from \<Organisation\> | Proposed as a best guess, agreed by the system owner | Not from \<Organisation\>. Evidence is EV-AC-08 to 11 |
| INT-AC-30 | \<Organisation\> controls these. Phones and tablets are not allowed with \<System Name\>, and external systems and USB storage need the system owner's approval | Proposed answer, agreed by the system owner | Consistent with D-AC-09 and D-AC-10. Not from \<Organisation\>. Evidence is EV-AC-13 to 17 |
| INT-AC-31 | Planned. Leavers come through the Starters/Leavers prompt, and movers through a ServiceNow change request | Proposed answer, agreed by the system owner | Consistent with PRO-AC-2 and PRO-AC-3. Evidence is EV-AC-01 |
| INT-AC-32 | Not yet. Each user signs it before getting access | Proposed answer, agreed by the system owner | No real users exist yet. Consistent with PRO-AC-1 |
| INT-AC-33 | Close it, do not share it, and report it straight away to the security officer | Proposed as a best guess, agreed by the system owner | No real users exist yet, so this states the expected answer |
| INT-AC-34 | No, none of these are allowed | Proposed answer, agreed by the system owner | No real users exist yet, so this states the rule. External use with approval is allowed by P-AC-22 |

### 22.2 AU and IA answers given at Level 1

The system owner agreed these proposed answers in writing on 6 November 2026, answering for each role. No records were seen, so they change no finding. Answers marked as a best guess or suggestion were not confirmed by \<Organisation\>, and the Level 2 assessor should treat them as such. The answers to INT-IA-01 to INT-IA-03 were given before sign-in moved to PingFederate (D-AC-23), and are overtaken: \<Organisation\>'s IT service desk, not a global administrator, resets passwords, and no temporary password is used.

**Table 30: AU and IA answers**

| ID | Answer agreed | Position |
| --- | --- | --- |
| INT-AU-01 | The system owner decides, based on what is needed to trace who did what, and reviews the list every 12 months | Consistent with \<Audit and Accountability Management\> |
| INT-AU-02 | No review yet, as \<System Name\> is not live. It starts at go-live | PA-40 |
| INT-AU-03 | It cannot be shown yet. The chain check exists but nothing runs it, and the database account can change records | PA-36, PA-37; the chain itself cannot yet detect tampering (PA-73, PA-74) |
| INT-AU-04 | Today it reaches only the application log. An alert within 1 hour is planned | PA-38 |
| INT-AU-05 | 12 months, with a monthly capacity check once the VMs are built | PA-42 |
| INT-AU-06 | Not yet confirmed; with the evidence request to \<Organisation\> | Best guess. EV-AU-01, EV-AU-02 |
| INT-IA-01 | In person, or through a known contact route, with the temporary password sent separately | Suggestion, added to PRO-IA-2 |
| INT-IA-02 | The account stays disabled, and the name is never reused | Consistent with PRO-AC-3. Deletion is still possible (PA-47) |
| INT-IA-03 | Tell a global administrator and the security officer straight away, and the administrator resets it | Consistent with PRO-IA-3 |
| INT-IA-04 | Not yet, as they are committed in source. New ones will be set on the VMs, then changed every 12 months | PA-19 |
| INT-IA-05 | By \<Organisation\>'s network controls, with details to come through the evidence request | Best guess. EV-IA-01 |
| INT-IA-06 | Photo ID and right-to-work checks before hiring, and people are told it has been done | Best guess. EV-IA-02 |
| INT-IA-07 | Not yet asked: added on 16 November 2026, after sign-in moved to PingFederate | Open (PA-95, PA-117) |

### 22.3 SC and CM answers

The system owner agreed these on 6 November 2026, at Level 1. They state the intended position. An answer doesn't change a finding, which still needs the record shown in Tables 14 and 26.

**Table 31: SC and CM answers**

| ID | Answer agreed | Position |
| --- | --- | --- |
| INT-SC-01 | Nothing is encrypted in the Docker stack today. On the VMs, TLS will protect web and database traffic, with certificates from \<Organisation\>, renewed before expiry | Agreed; gap until PA-18 |
| INT-SC-02 | Keys are committed in source today. They will move to a protected store outside source code, and change every 12 months | Agreed; gap until PA-19 |
| INT-SC-03 | Today UI application and Admin application send no page policy at all, and pages load scripts from cdn.jsdelivr.net (N04, N10). Scripts will be served locally, the page policy tightened, and changes reviewed at release | Agreed; gap until PA-34 and PA-51 |
| INT-SC-04 | BitLocker (XTS-AES 256 with the TPM) will be on both VMs, with the recovery keys tested every 12 months (SyOps C53), with recovery keys held by the Windows server administrator in \<Organisation\>'s protected store | Agreed; to confirm on the VMs (PA-52) |
| INT-SC-05 | \<Organisation\>'s security contact answers, with evidence | Not answerable by the system owner (EV-SC-02) |
| INT-SC-06 | \<Organisation\>'s security contact answers, with evidence | Not answerable by the system owner (EV-SC-01, EV-SC-05) |
| INT-SC-07 | The register lists every key, but the signing key and passwords are in source and the key rings are unencrypted | Agreed; not started (PA-19, PA-93) |
| INT-CM-01 | Through a ServiceNow approval by the change control element, which meets monthly and when an urgent or security change arises. Records are kept for 3 years | Agreed; workflow not yet set up (PA-53). The board is chartered in \<Configuration Management\>, section 3.8, with impact analysis criteria in \<Configuration Management\>, section 3.9 |
| INT-CM-02 | Each release is tested on a separate stack before go-live, then verified after it | Agreed; no release gate yet (PA-53) |
| INT-CM-03 | The baseline is the tagged release with the VM build record, and CIS Benchmarks apply to Windows Server 2025 and PostgreSQL, with exceptions recorded | Agreed; to confirm on the VMs (PA-54). The baseline and secure settings are in \<Configuration Management\>, sections 3.4 and 3.6 |
| INT-CM-04 | Only the named Windows server and database administrators can change the VMs, using Windows user rights, after a ServiceNow approval | Agreed; to confirm on the VMs (EV-CM-01) |
| INT-CM-05 | Diagnostic, test and maintenance pages will be removed from production builds, and functions are reviewed every 12 months | Agreed; gap until PA-07 and PA-31 |
| INT-CM-06 | Software is approved through ServiceNow and recorded on the approved list, reviewed every 12 months. The list isn't technically enforced, by decision | Agreed; decision D-CM-06 (PA-55) |
| INT-CM-07 | The Windows server administrator updates it at each change, recording name, type, version, location and owner | Agreed; to complete on the VMs (PA-54). The software components are listed in \<Configuration Management\>, section 3.5, from the scripted inventory |
| INT-CM-08 | \<Organisation\>'s security contact answers, with evidence | Not answerable by the system owner for the VMs and hosting (EV-CM-02, EV-CM-03). \<System Name\>'s own component licences are recorded in \<Configuration Management\>, section 3.5, and reviewed under PRO-CM-9 |

### 22.4 SI, RA and CA answers

The system owner agreed these on 6 November 2026, at Level 1. They state the intended position. An answer doesn't change a finding, which still needs the record shown in Tables 13, 24 and 27.

**Table 32: SI, RA and CA answers**

| ID | Answer agreed | Position |
| --- | --- | --- |
| INT-SI-01 | Developers run Test-Vulnerability.ps1 each month and at each release. Fixes follow \<Risk Assessment Management\>, section 3.6: exploited flaws within 3 days, Critical and High within 14 | Agreed; 7 advisories open (PA-56); run by hand, not yet scheduled (PA-57) |
| INT-SI-02 | Updates are tested on a separate stack first. Defender will run on both VMs, and each upload will be scanned through AMSI before it is stored | Agreed; no scanner call in the upload path yet (H08); Defender to confirm on the VMs (PA-58) |
| INT-SI-03 | The security officer reviews logs weekly. Use cases U1 to U8 in \<System and Information Integrity Management\>, section 3.4, such as repeated failed sign-ins, an audit chain break or a Defender detection, will alert them, and PRO-SI-4 sets the response | Agreed; failed sign-ins are recorded (H11), but nothing raises an alert yet (H12; PA-59) |
| INT-SI-04 | NCSC (including Early Warning), CISA's exploited list, Microsoft, .NET, GitHub and PostgreSQL advisories go to the security officer, who records those that apply on TPL-7 and passes them on (PRO-SI-5) | Agreed; not started; Early Warning to confirm with \<Organisation\> (EV-SI-03) |
| INT-SI-05 | API models are validated, and uploads are checked for type, file signature, size and name. Users will see a general message, and detail goes to the log | Agreed; input checks tested on 12 November 2026 (H02 to H07); about 29 responses still return exception detail (H01; PA-60) |
| INT-SI-06 | \<Organisation\>'s security contact answers, with evidence | Not answerable by the system owner (EV-SI-01, EV-SI-02) |
| INT-SI-07 | The v1.0 images and assemblies were recorded with SHA-256 on 12 November 2026. Scheduled checks, SHA-256 document checksums and a verifiable audit chain are planned; a mismatch goes to incident response (PRO-SI-6) | Agreed; baseline recorded; checks not built (PA-61); audit chain does not verify (H10; PA-74) |
| INT-RA-01 | The system owner reviews \<Risk List\> every 12 months and after a significant change, and shares it with the authorising official and Head of Cyber | Agreed; first review not yet due |
| INT-RA-02 | Moderate: confidentiality Moderate, integrity Moderate, availability Low, as HR documents hold personal data | Agreed; approved by \[Name\] (D-GEN-06) |
| INT-RA-03 | Monthly and at each release, credentialed, to the timetable in \<Risk Assessment Management\>, section 3.6: Critical and High within 14 days of the fix's release, Medium 30, Low 90 | Agreed; no scanner yet (PA-62) |
| INT-RA-04 | Through \<Organisation\>'s security contact, who passes it to the security officer | Agreed; to confirm with \<Organisation\> (EV-RA-01) |
| INT-RA-05 | Developers check its origin, support and known problems, as part of the 12-month supply chain review | Agreed; first review held on 11 November 2026 (D-RA-09) |
| INT-RA-06 | Checked weekly (SyOps C50); recorded on TPL-7 the same day, and fixed or mitigated within 3 days as an emergency change (PRO-RA-4) | Agreed (D-RA-P02); not yet in use |
| INT-CA-01 | \[Name\] answers, in writing | Not answerable by the system owner |
| INT-CA-02 | \[Name\] will rely on the SSP, assessments, risk list and plan, and accept the remaining risk by name. The package is now set in \<Assessment, Authorization, and Monitoring Management\>, section 3.5 | Agreed; not authorised |
| INT-CA-03 | The system owner updates it monthly from assessments, monitoring and audits | Agreed; monthly updates not started |
| INT-CA-04 | The security officer reports monthly to the system owner, who reports quarterly to \[Name\] | Agreed; not started |
| INT-CA-05 | ServiceNow, the Starters/Leavers system and the link between the VMs. The system owner approves each one when built | Agreed; not built (PA-63). \<Assessment, Authorization, and Monitoring Management\>, section 3.7, now lists six exchanges, adding \<Organisation\>'s central logging, time service and backup site |

### 22.5 IR, CP and AT answers

The system owner agreed these on 6 November 2026, at Level 1. They state the intended position. An answer doesn't change a finding, which still needs the record shown in Tables 11, 15 and 17.

**Table 33: IR, CP and AT answers**

| ID | Answer agreed | Position |
| --- | --- | --- |
| INT-IR-01 | Report to the security officer within 1 hour, who raises a ticket and leads the steps in \<Incident Response Management\> | Agreed; plan version \<ver\> written with severity targets and playbooks (\<Incident Response Management\>, sections 3.6 and 3.9), awaiting the Head of Cyber; ServiceNow ticket not yet in place (PA-65) |
| INT-IR-02 | A tabletop exercise is held every 12 months, with the contingency plan, and the plan is updated afterwards | Agreed; none held yet |
| INT-IR-03 | \[Name\] answers. The target is to tell the ICO within 72 hours of becoming aware of a reportable personal data breach, to tell the people affected when the risk to them is high, and to record every breach (\<Incident Response Management\>, section 3.8) | Not answerable by the system owner |
| INT-IR-04 | \<Organisation\>'s security contact answers, with evidence | Not answerable by the system owner (EV-IR-01) |
| INT-CP-01 | When a failure stops the essential functions, or threatens to stop them for longer than 72 hours. The system owner tells the people in \<Contingency Planning Management\> | Agreed; plan approved, not yet in use. \<Contingency Planning Management\> version \<ver\> now invokes the plan after 24 hours, so that recovery and checks finish within 72 hours (\<Contingency Planning Management\>, section 3.5.1) |
| INT-CP-02 | Database and documents daily, encrypted, at the second site, and a restore test every 6 months | Agreed; no backups yet (PA-64). The restore procedure was shown in Docker on 9 November 2026 (R01 to R09) |
| INT-CP-03 | From the tagged release and CIS Benchmarks, at the second site if the main one is lost, within 72 hours | Agreed; not tested |
| INT-CP-04 | \<Organisation\>'s IT service desk answers, with evidence | Not answerable by the system owner (EV-CP-01, EV-CP-02) |
| INT-AT-01 | The system owner checks the training record and the signed Security Operating Procedures before the person is added to a group | Agreed; not started |
| INT-AT-02 | Role modules M1 to M9 (\<Awareness and Training Management\>, section 3.4) come before access and every 12 months, each with a check passed at 80%. The security officer writes and updates the content after significant incidents and changes | Agreed; content not written |
| INT-AT-03 | Each user answers for themselves | Not answerable by the system owner |
| INT-AT-04 | Five measures, reported monthly on TPL-8: trained before access, first-attempt pass rate, overdue refreshers, suspicious messages reported and content reviewed | Agreed; no measures yet, as \<System Name\> is not in use |

### 22.6 MA, MP and PE answers

The system owner agreed these on 6 November 2026, at Level 1. They state the intended position. An answer doesn't change a finding, which still needs the record shown in Tables 18 to 20.

**Table 34: MA, MP and PE answers**

| ID | Answer agreed | Position |
| --- | --- | --- |
| INT-MA-01 | Each piece of maintenance has a change record, approved first. The administrator runs the checklist afterwards, the security officer signs it, and records are reviewed monthly (C48) | Agreed; no maintenance yet |
| INT-MA-02 | Only those on the approved list, inspected first and scanned by Defender | Agreed; provisional list in \<Maintenance Management\>, section 3.5, including the built-in maintenance pages (PA-31); Defender not yet in place (PA-58) |
| INT-MA-03 | The system owner approves it, an administrator watches it, it uses \<Organisation\>'s route, and it ends when finished | Agreed; routes R1 to R5 in \<Maintenance Management\>, section 3.4; \<Organisation\>'s route not evidenced (EV-MA-02), and the admin portal is open to every network (PA-83) |
| INT-MA-04 | Those on the approved list, screened and signed up to Part B. Suppliers get temporary accounts. Anyone else is escorted, with no access to \<System Name\>'s data | Agreed; provisional list in \<Maintenance Management\>, section 3.6 (PA-67) |
| INT-MA-05 | \<Organisation\>'s IT service desk answers, with evidence | Not answerable by the system owner (EV-MA-01) |
| INT-MP-01 | Each user answers for themselves. The rule is to mark it RESTRICTED, keep it on site, lock it away and shred it to DIN 66399 level P-4 | Not answerable by the system owner |
| INT-MP-02 | \<Organisation\>'s data centres, reached by its hosting staff, the database administrator and the Windows server administrator; copied to the second site encrypted (PA-64) | Agreed; no backups yet (PA-64), and not evidenced (EV-MP-01) |
| INT-MP-03 | \<Organisation\>'s IT service desk answers, with evidence | Not answerable by the system owner (EV-MP-02, EV-MP-03) |
| INT-MP-04 | Copies older than 24 hours are deleted each working day and recorded on TPL-8 (weekly until 17 November 2026; D-MP-10), until \<System Name\> removes them itself (PA-86) | Agreed; not yet in use, and copies were left on the server in Docker (P02 to P06) |
| INT-PE-01 | \<Organisation\>'s security contact answers, with evidence | Not answerable by the system owner (EV-PE-01) |
| INT-PE-02 | \<Organisation\>'s security contact answers, with evidence | Not answerable by the system owner (EV-PE-02, EV-PE-03) |
| INT-PE-03 | The security officer assesses them every 12 months, and people report concerns to the security officer | Agreed; not yet assessed |

### 22.7 PL and PS answers

The system owner agreed these on 6 November 2026, at Level 1. They state the intended position. An answer doesn't change a finding, which still needs the record shown in Tables 21 and 22.

**Table 35: PL and PS answers**

| ID | Answer agreed | Position |
| --- | --- | --- |
| INT-PL-01 | Reviewed after each assessment and every 12 months, and shared with the Head of Cyber, administrators and \<Organisation\>'s security contact | Agreed; not yet shared |
| INT-PL-02 | Each user answers for themselves | Not answerable by the system owner |
| INT-PL-03 | Only through \<Tailoring Register\>, with a rationale and a condition that must hold | Agreed; in use |
| INT-PS-01 | \<Organisation\>'s HR answers, with evidence | Not answerable by the system owner (EV-PS-01) |
| INT-PS-02 | A leaver within 5 working days, or 1 hour if higher risk, and a mover within 1 working day, recorded in TPL-14 | Agreed; route not built (PA-32) |
| INT-PS-03 | Everyone signs before access and every 12 months | Agreed; none signed yet |
| INT-PS-04 | \<Organisation\>'s HR answers, with evidence | Not answerable by the system owner (EV-PS-02) |
| INT-PS-05 | The system owner checks every 12 months | Agreed; not started |

### 22.8 PT, SA and SR answers

The system owner agreed these on 7 November 2026, at Level 1. They state the intended position. An answer doesn't change a finding, which still needs the record shown in Tables 23, 25 and 28.

**Table 36: PT, SA and SR answers**

| ID | Answer agreed | Position |
| --- | --- | --- |
| INT-PT-01 | The legal adviser answers. Proposed: UK GDPR, and consent isn't relied on | Not answerable by the system owner |
| INT-PT-02 | The legal adviser answers. A draft, \<Data Protection Impact Assessment\> \<ver\>, awaits completion before production | Not answerable by the system owner (PA-72) |
| INT-PT-03 | The legal adviser answers. None received yet | Not answerable by the system owner |
| INT-PT-04 | The business owner answers. Periods are drafted in \<PII Processing Management\>, section 3.7, awaiting the business owner (D-PT-21), and project access approvers check every 12 months | Not answerable by the system owner (PA-70) |
| INT-PT-05 | Audit records hold the named fields; free text holds no extra personal data (Q04), but the application log repeats usernames and IP addresses (Q05, PA-75). Test stacks use sample data | Agreed (PA-71) |
| INT-SA-01 | Planned, reviewed by another developer before merge, and recorded in ServiceNow once the workflow is set up. Today GitHub doesn't enforce the review (PA-91) | Agreed; workflow not set up (PA-53) |
| INT-SA-02 | The scripts in the developer test plan (\<System and Services Acquisition Management\>, section 3.9), which lists 15, run by hand on a separate test stack until a pipeline exists; no unit tests yet (PA-92) | Agreed (PA-68) |
| INT-SA-03 | The system owner raises them in yearly budgeting | Agreed; not yet raised |
| INT-SA-04 | The system owner reviews every 12 months | Agreed; not started |
| INT-SA-05 | The monthly package check | Agreed; not started |
| INT-SA-06 | Not yet protected: no repository requires a review before merge (S01) | Agreed; not started (PA-91) |
| INT-SR-01 | The system owner, security officer, a developer and \<Organisation\>'s IT service desk. It hasn't met yet | Agreed; not started |
| INT-SR-02 | A developer checks origin, publisher, support and known problems first (PRO-SR-1). Today only the OfflineModules packages come from the offline feed; the rest come from nuget.org, with no lock file | Agreed; gap until PA-94 (U01, U02) |
| INT-SR-03 | The security officer follows \<Procedures\> (IR) | Agreed; not used yet |
| INT-SR-04 | \<Organisation\> answers, with evidence | Not answerable by the system owner (EV-SR-02) |
| INT-SR-05 | A CycloneDX bill of materials is made for each release, and Test-SupplyChain.ps1 compares the release with the recorded SHA-256 values (PRO-SR-3) | Agreed; images match the baseline (U08); no bill of materials yet (PA-78) |
