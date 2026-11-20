# \<System Name\> Tailoring Register

**\<ref\> | Version \<ver\> | Approved by the system owner, live document**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose](#2-purpose)

[3 Access Control (AC)](#3-access-control-ac)

[4 Identification and Authentication (IA)](#4-identification-and-authentication-ia)

[5 Program Management (PM)](#5-program-management-pm)

[6 PT and SA](#6-pt-and-sa)

[7 System and Communications Protection (SC)](#7-system-and-communications-protection-sc)

[8 System and Information Integrity (SI)](#8-system-and-information-integrity-si)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<System Name\> Tailoring Register |
| Version | \<ver\> |
| Status | Approved by the system owner (D-PL-09); acceptance by the authorising official as a record pending. A live document, updated through \<Decision Register\> |
| Date | 5 November 2026 |
| Owner | System owner |
| Applies to | All control families; AC, AU, IA, SC, CM, SI, RA, CA, IR, CP, AT, MA, MP, PE, PL, PS, PT, SA and SR assessed in this version |
| Classification | Restricted |
| Next review | Every 12 months, when a family is added, and when a condition changes |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

Each entry is decided and recorded in \<Decision Register\>, under the decision rules in \<Risk List\>. The register as a whole was approved by the system owner as version \<ver\> on 11 November 2026 (D-PL-09), and goes to the authorising official, \[Name\], to accept as a record, as the SSP was. Later entries follow \<Procedures\>, PRO-PL-4.

### 1.3 Change history

**Table 2: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 18 November 2026 | No code references: page addresses, setting names, folder paths and file paths are described in plain words, and names of groups, scripts and releases are shown as plain text. No value, finding or decision is changed |
| \<ver\> | 17 November 2026 | The list of Program Management controls that \<System Name\> inherits moved to \<Program Management\>, as the system owner asked (D-PM-05). The decision TR-PM-01 stays here, unchanged |
| \<ver\> | 17 November 2026 | PM-27 cites the breach register by its present section |
| \<ver\> | 17 November 2026 | References to the incident response design follow the new section numbers of \<Incident Response Management\> (D-IR-10) |
| \<ver\> | 12 November 2026 | References to the assessment, authorisation and monitoring design point to \<Assessment, Authorization, and Monitoring Management\>, where it is now held (D-CA-11) |
| \<ver\> | 12 November 2026 | The condition of TR-AC-02 follows D-AC-23 |
| \<ver\> | 12 November 2026 | TR-IA-02 reworded for D-AC-23 |
| \<ver\> | 12 November 2026 | Version numbers are shown as a placeholder, as the system owner asked (D-GEN-28). No other change |
| \<ver\> | 12 November 2026 | The document number is replaced by a placeholder on the line under the title and in the details table, as the system owner asked (D-GEN-27). No other change |
| \<ver\> | 12 November 2026 | The name of the system is shown as a placeholder, as the system owner asked (D-GEN-26). No other change |
| \<ver\> | 12 November 2026 | The earlier rows of the change history are folded into one row, as the system owner decided (D-GEN-25). No other change |
| \<ver\> | 12 November 2026 | The steps for adding a control family are removed, as all 19 families are now in the document; the numbering rule they held is kept in section 2 |
| \<ver\> | 12 November 2026 | References to the register, the policy and the assessment record follow their new section and table numbers (D-GEN-24) |
| \<ver\> | 12 November 2026 | Documents are cited by name in angle brackets, in place of their numbers, as the system owner asked (D-GEN-23). No other change |
| \<ver\> | 12 November 2026 | The AC procedures are cited as PRO-AC-1 to PRO-AC-16 (WS-D11). Whole-set review (WS-D8): family sections are in NIST order, and Table 3 has a row for each of the 20 families; sections and tables renumbered. No entry changed. The combined documents are cited by their new numbers and chapters (D-GEN-21). The document standard is cited as \<Documentation Map\>, section 5. The contents list is rebuilt so that its links work in Markdown |
| \<ver\> to \<ver\> | 5 to 11 November 2026 | The earlier versions. Their history is kept in the change record (\<Documentation Map\>, section 5.1) |

| **SECTION 2** |
| --- |

## 2 Purpose

NIST SP 800-37 Rev 2 (task S-2) allows a baseline to be tailored to the system, and expects each decision to have a rationale and an approval. This register holds the case for every control, part or parameter proposed as not applicable. Tailoring is not a way to avoid a control that is merely difficult. Every entry states the condition that makes it valid, and it ends if that condition stops being true. All entries are proposals.

Entries are numbered TR-XX-nn, where XX is the family code. Each has a matching decision in \<Decision Register\>.

**Table 3: Family coverage**

| Family | Section | State |
| --- | --- | --- |
| AC Access Control | 3 | Decided |
| AT Awareness and Training | None | Assessed; nothing tailored |
| AU Audit and Accountability | None | Assessed; nothing tailored |
| CA Assessment, Authorization, and Monitoring | None | Assessed; nothing tailored |
| CM Configuration Management | None | Assessed; nothing tailored |
| CP Contingency Planning | None | Assessed; nothing tailored |
| IA Identification and Authentication | 4 | Agreed by the system owner |
| IR Incident Response | None | Assessed; nothing tailored |
| MA Maintenance | None | Assessed; nothing tailored |
| MP Media Protection | None | Assessed; nothing tailored |
| PE Physical and Environmental Protection | None | Assessed; nothing tailored |
| PL Planning | None | Assessed; nothing tailored |
| PM Program Management | 5 | Agreed by the system owner; outside the baseline |
| PS Personnel Security | None | Assessed; nothing tailored |
| PT Personally Identifiable Information Processing and Transparency | 6 | Agreed by the system owner; 7 US-only entries |
| RA Risk Assessment | None | Assessed; nothing tailored |
| SA System and Services Acquisition | 6 | Agreed by the system owner; SA-4(10) |
| SC System and Communications Protection | 7 | Agreed by the system owner |
| SI System and Information Integrity | 8 | Agreed by the system owner |
| SR Supply Chain Risk Management | None | Assessed; nothing tailored |

| **SECTION 3** |
| --- |

## 3 Access Control (AC)

### 3.1 Tailoring decisions

**Table 4: AC tailoring decisions**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| TR-AC-01 | AC-2(2) | Not applicable | Temporary and emergency accounts are prohibited (P-AC-09), and the system cannot expire accounts | Each access review confirms that no such account exists | The system must first be able to disable them automatically | Approved, \[Name\], 5 November 2026 |
| TR-AC-02 | AC-2k | Not applicable | Shared and group accounts are prohibited (P-AC-04) | \<System Name\> holds no accounts of its own: every account is a person's own Active Directory account (D-AC-23). The admin account is seeded sample data in the Docker environment only (D-AC-13) | A process for changing shared authenticators is needed | Approved, \[Name\], 5 November 2026 |
| TR-AC-03 | AC-8a.01 | Replace the statement with one naming \<Organisation\> | \<System Name\> is not a U.S. Government system, so the statement would be untrue | The notice names \<Organisation\>, and a legal adviser agrees the wording | Applies again if \<System Name\> serves a U.S. Government customer | Approved, \[Name\], 5 November 2026. Legal review to follow |
| TR-AC-04 | AC-8c | Not applicable | \<System Name\> is not publicly accessible | Documents and functions need sign-in, except the list in P-AC-25 | AC-8c applies in full | Approved, \[Name\], 5 November 2026 |
| TR-AC-05 | AC-17(4) | Not applicable | NIST defines remote access as access through external networks. Administration is to take place only from inside \<Organisation\>'s network | \<Organisation\> confirms this route, and external routes to the VMs' administration ports are blocked (EV-AC-12) | AC-17(4) applies, with defined needs and logging | Approved, \[Name\], 6 November 2026. Condition still to be evidenced |
| TR-AC-06 | AC-19, AC-19(5) | Not applicable | Phones and tablets are not to be used with \<System Name\> in the first release | \<Organisation\>'s device controls prevent or govern this. \<System Name\> cannot identify a device, so a rule alone is weak evidence (EV-AC-15) | Both apply, with \<Organisation\>'s mobile controls as evidence | Approved, \[Name\], 5 November 2026. Condition still to be evidenced |
| TR-AC-07 | AC-20(1) | Not applicable | P-AC-22 does not allow external systems to reach or hold \<System Name\> data without the system owner's approval, and none is proposed | No such approval has been given | Verification of controls and retained agreements are needed for each approval | Approved, \[Name\], 5 November 2026 |
| TR-AC-08 | AC-22 | Not applicable | \<System Name\> holds no public content (P-AC-24) | Documents need sign-in (T02, T03), and the open endpoints in NC-24 are dealt with | AC-22 applies in full | Approved, \[Name\], 5 November 2026 |
| TR-AC-09 | AC-07\_ODP\[05\], \[06\] | Not selected | The account lock is the chosen action, so no delay algorithm or other action is needed | The lock remains in place | Define the value that is then selected | Approved, \[Name\], 5 November 2026 |
| TR-AC-10 | AC-20\_ODP\[03\] | Not selected | Terms and conditions are used, not asserted controls | P-AC-22 remains the rule | Define the asserted controls | Approved, \[Name\], 5 November 2026 |

### 3.2 Considered and not proposed

These controls may look unnecessary but are not proposed for tailoring, so that their risk stays visible.

**Table 5: AC controls considered and kept**

| Control | Reason it stays |
| --- | --- |
| AC-18, AC-18(1) | \<System Name\> provides no wireless access, but users may reach it over \<Organisation\>'s wireless network, so the control is inherited and needs evidence |
| AC-18(3) | It needs confirming on the built VMs and workstation builds |
| AC-17, AC-17(1) to (3) | Approved users may work remotely through \<Organisation\>'s service |
| AC-20, AC-20(2) | Downloads can reach any device the user has, so the rule and its enforcement remain relevant |

| **SECTION 4** |
| --- |

## 4 Identification and Authentication (IA)

No AU control is tailored. The system owner agreed these on 5 November 2026 (D-IA-05). IA-5i is covered by TR-AC-02.

**Table 6: IA tailoring decisions**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| TR-IA-01 | IA-2(12) | Not applicable | PIV credentials are a US federal scheme, and \<Organisation\> is a UK company | \<Organisation\> does not serve a US federal customer through \<System Name\> | IA-2(12) applies | Agreed, \[Name\], 5 November 2026 |
| TR-IA-02 | IA-5(2) | Not applicable | \<System Name\> does not use public key sign-in | Users do not sign in to \<System Name\> with a public key: AD FS decides the factors | IA-5(2) applies. A public key second factor would bring it back | Agreed, \[Name\], 5 November 2026 |
| TR-IA-03 | IA-8 | Not applicable | Only \<Organisation\>'s staff and contractors hold accounts | Each access review confirms no outside user holds an account | IA-8 applies | Agreed, \[Name\], 5 November 2026 |
| TR-IA-04 | IA-8(1) | Not applicable | As TR-IA-01 and TR-IA-03 | As TR-IA-03 | IA-8(1) applies | Agreed, \[Name\], 5 November 2026 |
| TR-IA-05 | IA-8(2) | Not applicable | No external authenticators are accepted | As TR-IA-03 | IA-8(2) applies | Agreed, \[Name\], 5 November 2026 |
| TR-IA-06 | IA-8(4) | Not applicable | No external identity profiles are used | As TR-IA-03 | IA-8(4) applies | Agreed, \[Name\], 5 November 2026 |

| **SECTION 5** |
| --- |

## 5 Program Management (PM)

The system owner agreed this on 6 November 2026 (D-PM-01). It isn't tailoring in the strict sense, as PM has no controls in the Moderate baseline. It is recorded here so that all 20 families are accounted for. PT also has no controls in that baseline, and is assessed against the privacy baseline instead (D-PT-01).

**Table 7: PM decision**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| TR-PM-01 | The whole PM family | Outside the baseline; not assessed for \<System Name\> | PM controls cover an organisation's whole security programme, not one system, and NIST does not allocate them to a baseline. \<System Name\> still inherits them as common controls (NIST SP 800-37, task P-5), as listed in \<Program Management\>, section 4.3 | The organisation's programme stays with \<Organisation\> and the Head of Cyber, and \<System Name\>'s owner or authorising official doesn't ask for it to be assessed | Assess the PM controls | Agreed, \[Name\], 6 November 2026 |

### 5.1 PM controls \<System Name\> inherits

The list of PM controls that \<System Name\> inherits, with the provider and the evidence for each, is held in \<Program Management\>, section 4.3. It is not repeated here.

| **SECTION 6** |
| --- |

## 6 PT and SA

The system owner agreed these on 6 November 2026 (D-PT-08, D-SA-06). The PT controls are in NIST's privacy baseline, not Moderate, and were assessed against it (D-PT-01, D-PT-07).

**Table 8: PT and SA decisions**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| TR-PT-01 | PT-5(2), PT-6, PT-6(1), PT-6(2), PT-7(1), PT-7(2), PT-8 | Not applicable | These rest on US law and federal bodies: the Privacy Act, Federal Register notices, Social Security numbers, the First Amendment and computer matching. \<Organisation\> operates in the UK | \<System Name\> processes no data under those US laws. The legal adviser confirms this | Assess those controls | Agreed by the system owner, 6 November 2026 |
| TR-SA-01 | SA-4(10) | Not applicable | It requires US government PIV identity products, which \<System Name\> doesn't use | \<System Name\> doesn't use PIV cards | Assess SA-4(10) | Agreed by the system owner, 6 November 2026 |

| **SECTION 7** |
| --- |

## 7 System and Communications Protection (SC)

The system owner agreed this on 6 November 2026 (D-SC-05). No CM control is tailored, and CM-2(7) stays in scope by decision (D-CM-05).

**Table 9: SC tailoring decisions**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| TR-SC-01 | SC-15 | Not applicable | \<System Name\> has no collaborative computing devices or applications | None is added to the system | SC-15 applies | Agreed, \[Name\], 6 November 2026 |

| **SECTION 8** |
| --- |

## 8 System and Information Integrity (SI)

The system owner agreed this on 6 November 2026 (D-SI-05). No RA or CA control is tailored.

**Table 10: SI tailoring decisions**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| TR-SI-01 | SI-8, SI-8(2) | Not applicable | \<System Name\> sends and receives no email, so it has no entry or exit point for spam | \<System Name\> does not add email | SI-8 and SI-8(2) apply | Agreed, \[Name\], 6 November 2026 |
