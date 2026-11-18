# \<DocuView\> Security Policy

**\<ref\> | Version \<ver\> | The layout introduced in version \<ver\> awaits the system owner's approval; the content of every chapter is unchanged**

**Contents**

[1 Document control](#1-document-control)

[2 How to use this document](#2-how-to-use-this-document)

[AC Access Control](#ac-access-control)

[AT Awareness and Training](#at-awareness-and-training)

[AU Audit and Accountability](#au-audit-and-accountability)

[CA Assessment, Authorization, and Monitoring](#ca-assessment-authorization-and-monitoring)

[CM Configuration Management](#cm-configuration-management)

[CP Contingency Planning](#cp-contingency-planning)

[IA Identification and Authentication](#ia-identification-and-authentication)

[IR Incident Response](#ir-incident-response)

[MA Maintenance](#ma-maintenance)

[MP Media Protection](#mp-media-protection)

[PE Physical and Environmental Protection](#pe-physical-and-environmental-protection)

[PL Planning](#pl-planning)

[PS Personnel Security](#ps-personnel-security)

[PT Personally Identifiable Information Processing and Transparency](#pt-personally-identifiable-information-processing-and-transparency)

[RA Risk Assessment](#ra-risk-assessment)

[SA System and Services Acquisition](#sa-system-and-services-acquisition)

[SC System and Communications Protection](#sc-system-and-communications-protection)

[SI System and Information Integrity](#si-system-and-information-integrity)

[SR Supply Chain Risk Management](#sr-supply-chain-risk-management)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<DocuView\> Security Policy |
| Version | \<ver\> |
| Status | Version \<ver\> has one status, approval and change history for the whole document, as the system owner asked on 12 November 2026 (D-GEN-24), and that layout awaits the system owner's approval. No rule, value, finding or decision changed, so each chapter stands as it was approved (Table 4) |
| Date | 12 November 2026 |
| Owner | System owner |
| Applies to | The 19 control families listed in Table 4 |
| Classification | Restricted |
| Next review | Every 12 months, and after a significant change |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| System owner | Neil Ramsbottom | The layout introduced in version \<ver\> awaits approval. The approval of each chapter's content is in Table 4 | Pending |

### 1.3 Change history

From version \<ver\> the document has one version, one approval and one change history. A change to any chapter raises the document's version, and the row below names the chapter that changed.

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 18 November 2026 | Whole-set review: sections 2 and 2.1 point to each family's design document, as the register now holds none |
| \<ver\> | 18 November 2026 | Chapter SR: the offline feed is defined without naming its folder. For the Head of Cyber with the later version (D-SR-12) |
| \<ver\> | 18 November 2026 | Chapter SC: rules R5 and R10 and the database administrator's responsibility describe the settings in plain words, not by their configuration names. No requirement is changed. For the Head of Cyber with the later version (D-SC-06) |
| \<ver\> | 18 November 2026 | References to the communications protection design point to \<System and Communications Protection Management\>, where it is now held (D-SC-09). References to the integrity design point to \<System and Information Integrity Management\>, where it is now held (D-SI-10) |
| \<ver\> | 18 November 2026 | References to the acquisition design point to \<System and Services Acquisition Management\>, where it is now held (D-SA-19) |
| \<ver\> | 18 November 2026 | Chapter RA: rule R6 covers \<DocuView\>'s own applications, and rule R9 requires the reporting route to be published with terms that authorise research in good faith, from the RA cross-check. For the Head of Cyber with the later version (D-RA-06) |
| \<ver\> | 18 November 2026 | Chapter PT: rule R11 added, requiring personal data to be kept accurate and checked every 12 months (SI-18), as the system owner decided (D-PT-24). For the Head of Cyber with the later version (D-PT-18) |
| \<ver\> | 18 November 2026 | References to the risk assessment design point to \<Risk Assessment Management\>, where it is now held (D-RA-11) |
| \<ver\> | 18 November 2026 | References to the personal data design point to \<PII Processing Management\>, where it is now held (D-PT-22). Chapter PT: the scope and rule R8 follow sign-in through AD FS, as \<DocuView\> holds no accounts and has no sign-in page of its own (D-AC-23). For the Head of Cyber with the later version (D-PT-18) |
| \<ver\> | 17 November 2026 | Chapter PS: the definition of an external person includes an independent assessor. For the Head of Cyber with the later version (D-PS-08) |
| \<ver\> | 17 November 2026 | References to the personnel security design point to \<Personnel Security Management\>, where it is now held (D-PS-10). Chapter PS: rule R2 and the global administrator's responsibility follow sign-in through AD FS, as \<DocuView\> holds no accounts (D-AC-23). For the Head of Cyber with the later version (D-PS-08) |
| \<ver\> | 17 November 2026 | References to the planning design point to \<Planning Management\>, where it is now held (D-PL-12) |
| \<ver\> | 17 November 2026 | Chapter PE, rule R5: the inspection covers both data centres, as rule R4 already holds the second site to the same requirements |
| \<ver\> | 17 November 2026 | References to the physical and environmental protection design point to \<Physical and Environmental Protection Management\>, where it is now held (D-PE-11) |
| \<ver\> | 17 November 2026 | Chapter MP, scope: the list of media names every kind in the media inventory. No rule is changed |
| \<ver\> | 17 November 2026 | Chapter MP, rule R5: the export folder is checked each working day in place of weekly, as the system owner decided (D-MP-10). For the Head of Cyber with the later version (D-MP-07) |
| \<ver\> | 17 November 2026 | References to the media protection design point to \<Media Protection Management\>, where it is now held (D-MP-09) |
| \<ver\> | 17 November 2026 | References to the maintenance design point to \<Maintenance Management\>, where it is now held (D-MA-09) |
| \<ver\> | 17 November 2026 | Chapter IR, rule R10: Report Fraud is named in place of Action Fraud, which it replaced in December 2025. No change to the rule |
| \<ver\> | 17 November 2026 | References to the incident response design follow the new section numbers of \<Incident Response Management\> (D-IR-10) |
| \<ver\> | 15 November 2026 | References to the identification and authentication design point to \<Identification and Authentication Management\>, where it is now held (D-IA-11) |
| \<ver\> | 13 November 2026 | References to the configuration management design follow the new section numbers of \<Configuration Management\> (D-CM-13) |
| \<ver\> | 12 November 2026 | References to the assessment, authorisation and monitoring design point to \<Assessment, Authorization, and Monitoring Management\>, where it is now held (D-CA-11) |
| \<ver\> | 12 November 2026 | References to the audit design point to \<Audit and Accountability Management\>, where it is now held (D-AU-10) |
| \<ver\> | 12 November 2026 | Principle 1 of chapter AT says "no access", as no account is created in the system (D-AC-23) |
| \<ver\> | 12 November 2026 | References to the training design point to \<Awareness and Training Management\>, where it is now held (D-AT-09). Rule R1 of chapter AT says "before getting access", as no account is created in the system (D-AC-23) |
| \<ver\> | 12 November 2026 | The identification and authentication policy follows D-AC-23: sign-in through AD FS with multi-factor authentication, Active Directory accounts as identifiers, and no passwords held by the system. Requirements R1 to R4, R6, R7, R10 and R11 of chapter IA change, so the chapter awaits the Head of Cyber |
| \<ver\> | 12 November 2026 | Version numbers are shown as a placeholder, as the system owner asked (D-GEN-28). No other change |
| \<ver\> | 12 November 2026 | The document number is replaced by a placeholder on the line under the title and in the details table, as the system owner asked (D-GEN-27). No other change |
| \<ver\> | 12 November 2026 | The name of the system is shown as a placeholder, as the system owner asked (D-GEN-26). No other change |
| \<ver\> | 12 November 2026 | References to the access control design point to \<Access Control Management\>, where it is now held |
| \<ver\> | 12 November 2026 | References to documents that no longer exist now name where their content is, as the system owner asked. No other change |
| \<ver\> | 12 November 2026 | The rules common to every policy are stated once, in section 2.1, and removed from the chapters, each of which keeps what is particular to it (D-GEN-25). No rule is changed, so the change is editorial |
| \<ver\> | 12 November 2026 | One status, approval and change history for the whole document, as the system owner asked (D-GEN-24). The status, approval and change history of each chapter are removed, and Table 4 records what each chapter was approved as. Sections and tables in each chapter renumbered. No rule, value, finding or decision changed |
| \<ver\> | 12 November 2026 | Documents are cited by name in angle brackets, in place of their numbers, as the system owner asked (D-GEN-23). No other change |
| \<ver\> | 12 November 2026 | The system owner confirmed the combined form of this document (D-GEN-21). The status and approval now say so. No chapter changed |
| \<ver\> | 12 November 2026 | First issue. The 19 family policies, brought into one document as chapters in NIST order (whole-set review, WS-D13, D-GEN-21). No content changed. Each chapter keeps its version, approval and change history |

### 1.4 What each chapter was approved as

Until version \<ver\> each chapter carried its own version, approval and change history. Table 4 records where each stood. The earlier change histories are kept in the change record (\<Documentation Map\>, section 5.1).

**Table 4: Chapters**

| Chapter | Family | Last chapter version | Status at that version |
| --- | --- | --- | --- |
| AC | Access Control | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> approved on 8 November 2026 (D-AC-16); legally reviewed on 12 November 2026; version \<ver\> makes editorial changes only, issued by the system owner under D-GEN-19 |
| AT | Awareness and Training | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-AT-07); legally reviewed on 12 November 2026 |
| AU | Audit and Accountability | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> approved on 8 November 2026 (D-AU-08); legally reviewed on 12 November 2026; version \<ver\> makes editorial changes only, issued by the system owner under D-GEN-19 |
| CA | Assessment, Authorization, and Monitoring | \<ver\> | Approved by the Head of Cyber; legally reviewed on 12 November 2026; version \<ver\> makes editorial changes only, issued by the system owner under D-GEN-19 |
| CM | Configuration Management | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> approved on 8 November 2026 (D-CM-11); legally reviewed on 12 November 2026; version \<ver\> makes editorial changes only, issued by the system owner under D-GEN-19 |
| CP | Contingency Planning | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> approved on 9 November 2026 (D-CP-12); legal review completed on 9 November 2026 |
| IA | Identification and Authentication | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> approved on 9 November 2026 (D-IA-09); legal review completed on 9 November 2026 |
| IR | Incident Response | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-IR-07); legal review completed on 10 November 2026 |
| MA | Maintenance | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-MA-07); legal review completed on 10 November 2026 |
| MP | Media Protection | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-MP-07); legal review completed on 10 November 2026 |
| PE | Physical and Environmental Protection | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-PE-09); legally reviewed on 10 November 2026 |
| PL | Planning | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-PL-07); legally reviewed on 11 November 2026 |
| PS | Personnel Security | \<ver\> | Version \<ver\> approved by the Head of Cyber and legally reviewed on 12 November 2026; version \<ver\> awaiting re-approval and legal review (D-PS-08) |
| PT | Personally Identifiable Information Processing and Transparency | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-PT-18); legally reviewed on 11 November 2026 |
| RA | Risk Assessment | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-RA-06); legally reviewed on 11 November 2026 |
| SA | System and Services Acquisition | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-SA-16); legally reviewed on 11 November 2026 |
| SC | System and Communications Protection | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-SC-06); legally reviewed on 12 November 2026 |
| SI | System and Information Integrity | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-SI-06); legally reviewed on 12 November 2026 |
| SR | Supply Chain Risk Management | \<ver\> | Version \<ver\> approved by the Head of Cyber; version \<ver\> awaiting re-approval (D-SR-12); legally reviewed on 12 November 2026 |

| **SECTION 2** |
| --- |

## 2 How to use this document

This document is the security and privacy policy for \<DocuView\>. It holds one policy for each of the 19 NIST SP 800-53 Rev 5 control families that apply, as chapters in NIST order. A policy says what must be true and who is accountable for it. How each rule is carried out is in \<Procedures\>, and the design, values and decisions are in each family's design document (\<Documentation Map\>, section 3.2).

The Head of Cyber approves each policy, and the legal adviser reviews it. Table 4 shows where each chapter stands. Where a chapter awaits the Head of Cyber, the decision is listed in \<Decision Register\>.

- **Chapters.** Each chapter is named by its family code. Its sections carry the code, so PS.3 is section 3 of the Personnel Security chapter, and its tables are numbered Table PS-1, Table PS-2 and so on.
- **Citing.** Cite a chapter as \<Policy\> (PS), a section as \<Policy\>, section PS.3, and a table as \<Policy\>, Table PS-1.
- **Versions.** The document has one version. A change to any chapter is a new version of the document.

### 2.1 Rules common to every policy

These rules apply to every chapter. They are stated once here. A chapter repeats one only where its rule differs or adds to it.

1. **Ownership:** the system owner manages each policy and its procedures.
2. **Approval:** the Head of Cyber approves each policy, as all policies, and the system owner approves the procedures and the family's design document.
3. **Policy review:** every 12 months, and after a significant incident, audit finding or system change.
4. **Procedures review:** every 12 months, and after a change to the steps.
5. **Compliance and management commitment:** the system owner reviews compliance at each review and records the result.
6. **Non-compliance:** a control counts as non-compliant until shown otherwise. Each non-compliance is recorded and rated in \<Risk List\>, and a named person decides its treatment: the system owner for Low risks, and the authorising official for Medium and High risks. A fix is made only through \<Plan of Action and Milestones\>. Section AC.7 sets out the approach in full.

| **CHAPTER AC** |
| --- |

## AC Access Control

[AC.1 Purpose and scope](#ac1-purpose-and-scope) · [AC.2 The organisation's position](#ac2-the-organisations-position) · [AC.3 Control principles](#ac3-control-principles) · [AC.4 Mandatory requirements](#ac4-mandatory-requirements) · [AC.5 Responsibilities](#ac5-responsibilities) · [AC.6 Governance requirements](#ac6-governance-requirements) · [AC.7 Non-compliance and risk acceptance](#ac7-non-compliance-and-risk-acceptance) · [AC.8 Definitions](#ac8-definitions) · [AC.9 References](#ac9-references)

### AC.1 Purpose and scope

This policy sets the organisation's rules and principles for access to \<DocuView\>: what is mandatory, and who answers for it. The Head of Cyber, who approves all policies, has approved it. The legal adviser reviewed it on 12 November 2026. It has not yet been shared. The approved decisions and settings that carry it out are in \<Access Control Management\>, and the steps people follow are in \<Procedures\> (AC).

This policy sets who may access \<DocuView\>, what they may do, and how that access is controlled, in line with the NIST SP 800-53 Rev 5 AC family (AC-1).

It applies to everyone who uses or administers DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database and the two Windows Server 2025 VMs they run on at ABC Technologies, and to any service account they use.

### AC.2 The organisation's position

Documents in \<DocuView\> are available only to people with an approved need. Convenience never overrides that. The organisation accepts that some access controls depend on ABC Technologies, and it stays accountable for making sure they are in place and evidenced. The Head of Cyber, for ABC Technologies' management, is committed to this policy: to providing the people, time and tools it needs, to reviewing how well it works, and to acting on breaches of it.

### AC.3 Control principles

1. Access is denied unless a role or group grants it.
2. Each person has one named account. Shared accounts are not allowed.
3. People get the least access their job needs, and it is removed when the need ends.
4. Duties that could be misused together are held by different people where staffing allows.
5. Privileged actions are recorded and reviewed.
6. Access routes and information flows are approved in advance.
7. Access is reviewed regularly and corrected when it no longer matches a person's need.

### AC.4 Mandatory requirements

**Table AC-1: Mandatory requirements**

| No. | Requirement | Controls |
| --- | --- | --- |
| R1 | Only named accounts of an allowed type may be used. Shared, guest and anonymous accounts are not allowed | AC-2 |
| R2 | Every account, group membership and privilege must have a recorded approval before it is granted | AC-2, AC-6(5) |
| R3 | Access must change promptly when people join, move or leave. Accounts that are unused, unneeded or a risk must be disabled. Account management must use automated support where the system provides it | AC-2, AC-2(1), AC-2(3), AC-2(13) |
| R4 | Temporary and emergency accounts may be used only if they end automatically | AC-2(2) |
| R5 | The system must enforce approved access and deny everything else. Only approved actions may work without signing in | AC-3, AC-14 |
| R6 | People and processes must have only the access their tasks need. Only authorised people may use security functions or see security-relevant information | AC-6, AC-6(1), AC-6(5), AC-6(10) |
| R7 | People with privileged access must use a non-privileged account for everyday work | AC-6(2) |
| R8 | Duties that could be misused together must be separated | AC-5 |
| R9 | Account changes and privileged actions must be recorded against the person who made them | AC-2(4), AC-6(9) |
| R10 | Access and privileges must be reviewed at set intervals | AC-2, AC-6(7) |
| R11 | Repeated failed sign-ins must lock the account. Idle sessions must lock and end, and every session must have a time limit. A system use notice must be shown before sign-in | AC-2(5), AC-7, AC-8, AC-11, AC-11(1), AC-12 |
| R12 | Information must flow only along approved routes. Remote access must use an approved, managed and encrypted route | AC-4, AC-17 family |
| R13 | Wireless access, mobile devices, external systems and portable storage must follow approved rules | AC-18, AC-19 and AC-20 families |
| R14 | Information may be shared outside a project only after a decision by its approver. \<DocuView\> does not hold public content | AC-21, AC-22 |

### AC.5 Responsibilities

**Table AC-2: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves all policies, including this one |
| System owner | Owns this policy, approves privileged access, approves exceptions and accepts risk within their authority |
| Authorising official | Accepts residual risk and authorises operation |
| Global administrator | Carries out approved changes to users, groups, projects and sessions |
| Project access approver | Decides who may read or edit a project, and whether its information may be shared |
| Auditor | Reviews audit records and privileged activity |
| Security officer | Monitors security information |
| Windows server and database administrators | Keep to these requirements on the VMs and in PostgreSQL |
| ABC Technologies security contact | Provides evidence for the controls \<DocuView\> inherits |
| Every user | Follows the Security Operating Procedures (\<Security Operating Procedures\>) |

The people holding each role are named in \<Roles and Responsibilities\>.

### AC.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Ownership (P-AC-01):** the system owner manages this policy and the procedures.
2. **Communication:** this policy and the procedures must be shared with everyone who uses or administers \<DocuView\>, and whenever they change.
3. **Policy review (P-AC-02):** every 12 months, and after a significant incident, audit finding or system change.
4. **Procedures review (P-AC-03):** every 12 months, and after a change to the steps.
5. **Compliance and management commitment:** the system owner reviews compliance at each review and records the result. Breaches may lead to loss of access and to disciplinary action. They may also be offences under the Computer Misuse Act 1990 or the Data Protection Act 2018, as \<Security Operating Procedures\>, rule A4, explains.
6. **Coordination:** the system owner agrees with ABC Technologies' security contact how inherited controls, leavers and incidents are handled, and records it.
7. **Laws and standards:** this policy must be consistent with applicable law, ABC Technologies' policies and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 12 November 2026.
8. **Exceptions:** an exception needs written approval from the system owner, a stated end date and an entry in \<Risk List\>. \<Access Control Management\> sets the rules, and PRO-AC-15 sets the steps.

### AC.7 Non-compliance and risk acceptance

The organisation takes a risk-based approach to these requirements. No system meets every control, and a non-compliance is acceptable when its risk is understood and has been accepted by the right person.

1. Every non-compliance must be identified, documented and recorded in \<Risk List\>.
2. Its risk must be rated by the method in \<Risk List\>, section 5.
3. A named person must decide its treatment: accept, remediate, approve a value, obtain evidence or tailor the control. The system owner decides Low risks and the authorising official decides Medium and High risks.
4. A risk that is too high to accept requires a remediation plan in \<Plan of Action and Milestones\>. A High risk may be accepted only for a limited period while that plan runs.
5. A remediation is carried out through that plan and its milestones, and does not begin simply because a non-compliance was found.
6. Every acceptance is recorded with the name, date, reason and review date, and is reviewed at the interval in \<Risk List\>. PRO-AC-17 sets out the steps.

### AC.8 Definitions

**Table AC-3: Definitions**

| Term | Meaning |
| --- | --- |
| Access | The ability to use \<DocuView\> or its information, including reading, editing, exporting and administering |
| Account | A named identity in \<DocuView\>, Windows or PostgreSQL that a person or service uses to sign in |
| Approver | The person who must agree an access change before it is made: the system owner, or the project access approver for project groups (P-AC-05) |
| Exception | Written permission to depart from a requirement for a set period, recorded in \<Risk List\> |
| Least privilege | Giving each person or process only the access its tasks need |
| Privileged access | Access that can change accounts, settings, security functions, servers or the database, or read audit records |
| Project | A set of documents in \<DocuView\> with its own read and edit groups |
| Separation of duties | Splitting duties so that no one person can misuse them together unnoticed |
| Service account | An account used by a program rather than a person |

### AC.9 References

**Table AC-4: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, Access Control (AC) family | The controls this policy meets |
| NIST SP 800-53B, Moderate baseline | The controls selected |
| \<Procedures\> (AC), Access Control Procedures | The steps people follow |
| \<Access Control Management\>, Access Control Management | The approved settings and parameter values |
| \<Security Operating Procedures\>, Security Operating Procedures | The rules every user signs |
| \<Risk List\>, Risk List | Non-compliances, ratings and decisions |
| \<Roles and Responsibilities\>, Roles and Responsibilities | The people holding each role |
| UK GDPR, Data Protection Act 2018, Computer Misuse Act 1990 | The laws this policy must be consistent with |

| **CHAPTER AT** |
| --- |

## AT Awareness and Training

[AT.1 Purpose and scope](#at1-purpose-and-scope) · [AT.2 The organisation's position](#at2-the-organisations-position) · [AT.3 Control principles](#at3-control-principles) · [AT.4 Mandatory requirements](#at4-mandatory-requirements) · [AT.5 Responsibilities](#at5-responsibilities) · [AT.6 Governance requirements](#at6-governance-requirements) · [AT.7 Non-compliance and risk acceptance](#at7-non-compliance-and-risk-acceptance) · [AT.8 Definitions](#at8-definitions) · [AT.9 References](#at9-references)

### AT.1 Purpose and scope

This policy sets the organisation's rules for security and privacy awareness and training for \<DocuView\>, in line with the NIST SP 800-53 Rev 5 AT family (AT-1). It stands alone, as each family has its own policy. The curriculum, briefing, training matrix, measures and register are in \<Awareness and Training Management\>, and the steps people follow are in \<Procedures\> (AT).

It applies to everyone who uses, administers or develops \<DocuView\>, including ABC Technologies' staff who hold a \<DocuView\> role. It covers the training other families require: incident response (IR-2), contingency (CP-3), privacy (AT-3(5)) and the rules of behaviour (PL-4).

### AT.2 The organisation's position

\<DocuView\> holds Restricted HR documents, so the people who use and run it are part of its protection. ABC Technologies' general course gives everyone the basics; \<DocuView\> adds what is specific to it, and trains each role in the duties it actually performs. Training that cannot be shown, or that people did not understand, does not count.

### AT.3 Control principles

1. **Train before access:** no access without awareness training, and no privileged role without role training.
2. **Train for the job:** role training follows the \<DocuView\> procedures the role runs.
3. **Check understanding:** each module ends with a short check.
4. **Make reporting safe:** people are thanked, not blamed, for reporting a mistake or a suspicious message.
5. **Keep records:** training that cannot be shown did not happen.

### AT.4 Mandatory requirements

1. **R1 Awareness:** all users must complete ABC Technologies' security and privacy awareness course and the \<DocuView\> briefing before getting access, and every 12 months.
2. **R2 Briefing content:** the \<DocuView\> briefing must cover Restricted HR documents and export rules, insider threat and social engineering scenarios specific to \<DocuView\>, and how to report.
3. **R3 Rules of behaviour:** all users must sign \<Security Operating Procedures\> Part A, and privileged users Part B, before access.
4. **R4 Role training:** each role in the training matrix must complete its modules before privileged access, and every 12 months. Incident response and contingency training must be completed within 30 days of taking the role.
5. **R5 Privacy training:** everyone who handles HR documents, and all administrators, must complete privacy training before access and every 12 months.
6. **R6 Updates:** content must be reviewed every 12 months, and after a significant incident, exercise or change, with the lessons added.
7. **R7 Checks and measures:** each module must end with a check, with a pass mark of 80%. Completion before access, the pass rate and the number of suspicious messages reported must be reported monthly.
8. **R8 Phishing simulations:** none may be run without the agreement of HR and the legal adviser. If run, no one is penalised for clicking, and the measure is reports, not clicks.
9. **R9 Records:** every completion must be recorded on TPL-9 and in the training register, and kept for 3 years.
10. **R10 Checking:** Test-PlanConsistency.ps1 (check L14) must show that every security role has its training defined, at each review.

### AT.5 Responsibilities

**Table AT-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies; trains the security officer and auditor |
| Authorising official | Decides Medium and High risks |
| System owner | Owns this policy, the curriculum and the matrix; gives the \<DocuView\> briefing; checks the register before granting a role |
| Security officer | Writes and updates role training content, keeps the register and reports the measures |
| Legal adviser | Reviews privacy training content and agrees any phishing simulation |
| Line managers | Make sure their staff complete training on time |
| Everyone | Completes training, and reports anything suspicious |
| ABC Technologies | Provides the general course and its records, and evidences its administrators' role training |

### AT.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses, administers or develops \<DocuView\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews the measures monthly and compliance at each review, and records the result.
3. **Coordination:** the system owner agrees with ABC Technologies how its course and its administrators' training are evidenced, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, ABC Technologies' policies and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 12 November 2026.

### AT.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### AT.8 Definitions

**Table AT-2: Definitions**

| Term | Meaning |
| --- | --- |
| Awareness | Messages and briefings that keep security in people's minds |
| Role training | Training in the security duties a person performs in their \<DocuView\> role |
| Training matrix | The table of roles, modules, deadlines and frequencies in \<Awareness and Training Management\> |
| Social engineering | Manipulating people into giving access or information, including by email, phone or in person |
| Insider threat | Harm, deliberate or accidental, by someone with authorised access |

### AT.9 References

**Table AT-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, AT family | The controls this policy meets |
| NIST SP 800-50 Rev 1 (September 2024) | Running the learning programme |
| NIST SP 800-181 Rev 1, the NICE Framework | Describing role training |
| NCSC 10 Steps: engagement and training; NCSC phishing guidance | Needs-led training and blame-free reporting |
| ICO data protection audit framework: training and awareness | Privacy training and evidence of understanding |
| \<Awareness and Training Management\>, \<Procedures\> (AT), \<Security Operating Procedures\> and \<PII Processing Management\> | The curriculum, procedures, rules and privacy training |

| **CHAPTER AU** |
| --- |

## AU Audit and Accountability

[AU.1 Purpose and scope](#au1-purpose-and-scope) · [AU.2 The organisation's position](#au2-the-organisations-position) · [AU.3 Control principles](#au3-control-principles) · [AU.4 Mandatory requirements](#au4-mandatory-requirements) · [AU.5 Responsibilities](#au5-responsibilities) · [AU.6 Governance requirements](#au6-governance-requirements) · [AU.7 Non-compliance and risk acceptance](#au7-non-compliance-and-risk-acceptance) · [AU.8 Definitions](#au8-definitions) · [AU.9 References](#au9-references)

### AU.1 Purpose and scope

This policy sets the organisation's rules for recording and reviewing activity in \<DocuView\>, so that actions can be traced to a person and incidents can be investigated, in line with the NIST SP 800-53 Rev 5 AU family (AU-1). The settings that carry it out are in \<Audit and Accountability Management\>, and the steps people follow are in \<Procedures\> (AU).

It applies to DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database and the two Windows Server 2025 VMs they run on at ABC Technologies, and to everyone who administers or reviews them.

### AU.2 The organisation's position

Every security-relevant action in \<DocuView\> must leave a reliable record that names the person responsible. Records exist to support investigation and accountability, and are not used for any other purpose without the system owner's approval.

### AU.3 Control principles

1. **Complete:** the agreed events are recorded every time they occur.
2. **Attributable:** each record shows what happened, when, where, from where, the outcome and who was involved.
3. **Protected:** nobody can change or delete a record, except under the retention rule in section AU.4, and access to records is limited to those who review them.
4. **Reviewed:** records are examined regularly by someone who does not administer the system.
5. **Retained:** records are kept long enough to investigate an incident.

### AU.4 Mandatory requirements

1. **R1 Events:** the events in \<Audit and Accountability Management\> must be logged by each component it names.
2. **R2 Retention:** records must be kept for 12 months online and a further 12 months in an offline archive whose hash is recorded, with storage sized to match. After 24 months they may be deleted, only with the system owner's recorded approval.
3. **R3 Time:** time stamps must be in UTC to the nearest second, from ABC Technologies' time source, and within 1 second of UTC.
4. **R4 Protection:** auditors alone read audit records, and nobody may change or delete them, except as R2 allows.
5. **R5 Review:** the auditor must review records weekly and report findings to the security officer and system owner.
6. **R6 Logging failure:** a logging failure must alert the Windows server administrator and security officer within 1 hour. The system keeps running while it is investigated and restored.
7. **R7 Tampering:** suspected tampering must alert the security officer and auditor.
8. **R8 Content of records:** records must not contain passwords, keys, tokens or session IDs, and must hold only the personal data an investigation needs.
9. **R9 Other logs:** any other log that repeats audit information, such as an application or server log, is audit information under this policy: it is protected, limited to those who need it, and kept only for the period set in \<Audit and Accountability Management\>.

### AU.5 Responsibilities

**Table AU-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy, decides which events are logged, and receives review findings |
| Authorising official | Decides Medium and High risks |
| Auditor | Reviews records weekly and reports findings |
| Security officer | Receives findings and alerts, and handles incidents |
| Windows server administrator | Receives logging failure alerts, and restores logging on the VMs |
| Database administrator | Protects and retains the audit data in PostgreSQL |
| Developers | Build logging into the application |

### AU.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers or reviews \<DocuView\>, and whenever they change.
2. **Coordination:** the system owner agrees with ABC Technologies' security contact how logs from inherited services are shared, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR and the Data Protection Act 2018 for personal data in records, the Computer Misuse Act 1990 for misuse of the system and the use of records as evidence, ABC Technologies' policies and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 12 November 2026.

### AU.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### AU.8 Definitions

**Table AU-2: Definitions**

| Term | Meaning |
| --- | --- |
| Audit record | One entry that records an event: what happened, when, where, from where, the outcome and who was involved |
| Audit log | The store of audit records, today the table dbo.AuditLog in the \<DocuView\> database |
| Audit information | Audit records, any log that repeats them, and the tools and settings used to read or manage them |
| Auditor | The person who reviews audit records and does not administer the system |
| Chain hash | A value calculated from each record and the one before it, so that a change can be detected |
| Event | An action or occurrence that \<Audit and Accountability Management\> says must be logged |
| Logging failure | Any period in which agreed events are not recorded, for whatever reason |
| Retention period | How long records are kept before they may be deleted |
| Tampering | Any unauthorised change, deletion or addition of audit information |

### AU.9 References

**Table AU-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, Audit and Accountability (AU) family | The controls this policy meets |
| NIST SP 800-53B, Moderate baseline | The controls selected |
| NIST SP 800-92, Guide to Computer Security Log Management | Good practice for log management |
| \<Procedures\> (AU), Audit and Accountability Procedures | The steps people follow |
| \<Audit and Accountability Management\>, Audit and Accountability Management | The approved settings, events and parameter values |
| \<Security Operating Procedures\>, Security Operating Procedures, section 5.2 | The audit review steps and the list of unusual activity |
| \<Risk List\>, Risk List | Non-compliances, ratings and decisions |
| \<Policy\> (AC), Access Control Policy | The risk-based approach in \<Policy\>, section AC.7 |
| UK GDPR, Data Protection Act 2018, Computer Misuse Act 1990 | The laws this policy must be consistent with |

| **CHAPTER CA** |
| --- |

## CA Assessment, Authorization, and Monitoring

[CA.1 Purpose and scope](#ca1-purpose-and-scope) · [CA.2 The organisation's position](#ca2-the-organisations-position) · [CA.3 Control principles](#ca3-control-principles) · [CA.4 Mandatory requirements](#ca4-mandatory-requirements) · [CA.5 Responsibilities](#ca5-responsibilities) · [CA.6 Governance requirements](#ca6-governance-requirements) · [CA.7 Non-compliance and risk acceptance](#ca7-non-compliance-and-risk-acceptance) · [CA.8 Definitions](#ca8-definitions) · [CA.9 References](#ca9-references)

### CA.1 Purpose and scope

This policy sets the organisation's rules for assessing \<DocuView\>'s controls, authorising it to operate and monitoring it afterwards, in line with the NIST SP 800-53 Rev 5 CA family (CA-1). It stands alone, as each family has its own policy. The settings that carry it out are in \<Assessment, Authorization, and Monitoring Management\>, and the steps people follow are in \<Procedures\> (CA).

It applies to DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database, the two Windows Server 2025 VMs they run on at ABC Technologies, and their connections to other systems.

### CA.2 The organisation's position

\<DocuView\> must not hold production documents until the authorising official has authorised it. Authorisation rests on an honest assessment, including an independent one, and continues only while monitoring shows the risk stays acceptable.

### CA.3 Control principles

1. **Two levels:** the system owner self-assesses at Level 1, and an independent team assesses at Level 2.
2. **Authorise knowingly:** the authorising official accepts the remaining risk by name.
3. **Track what is open:** weaknesses stay on the plan until fixed.
4. **Know the connections:** each connection to another system is recorded and approved.

### CA.4 Mandatory requirements

1. **R1 Assessment:** controls must be assessed every 12 months, with results given to the system owner, authorising official and Head of Cyber.
2. **R2 Independence:** assessors must be independent, having had no part in building or running \<DocuView\>.
3. **R3 Connections:** each connection, including Jira, the Starters/Leavers system and the link between the VMs, must be recorded and approved, reviewed every 12 months, and use TLS.
4. **R4 Plan of action:** \<Plan of Action and Milestones\> must be updated monthly. Each open item must be fixed within the time set for its rating, counted from go-live: High items as the authorising official has decided, Medium within 180 days and Low within 365 days. Overdue items are reported to the authorising official each quarter.
5. **R5 Authorisation:** the authorising official must authorise \<DocuView\> before it holds production documents, and review the authorisation every 12 months.
6. **R6 Monitoring:** the security and privacy measures in \<Assessment, Authorization, and Monitoring Management\>, section 4.8, must be reported monthly to the system owner and quarterly to the authorising official.
7. **R7 Significant change:** a significant change must be assessed before it is made, and the authorising official decides whether \<DocuView\> must be re-assessed or re-authorised.
8. **R8 Authorisation package:** the authorising official receives the authorisation package listed in \<Assessment, Authorization, and Monitoring Management\>, section 4.5, and records each decision on TPL-18, with its terms, conditions and end date.
9. **R9 Inherited controls:** the controls inherited from ABC Technologies must be listed, and accepted by the authorising official, before \<DocuView\> operates.

### CA.5 Responsibilities

**Table CA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies, and receives assessment results |
| System owner | Owns this policy, runs Level 1, and keeps the plan up to date |
| Authorising official | Authorises \<DocuView\>, and decides Medium and High risks |
| Security assessor | Leads the independent Level 2 assessment |
| Security officer | Produces the monitoring report |
| Windows server administrator | Keeps connections to what is approved |
| ABC Technologies | Provides the inherited controls, and agrees the connections it owns |

### CA.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<DocuView\>, and whenever they change.
2. **Coordination:** the system owner agrees with ABC Technologies' security contact how inherited controls are provided, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR and the Data Protection Act 2018, ABC Technologies' policies and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 12 November 2026.

### CA.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### CA.8 Definitions

**Table CA-2: Definitions**

| Term | Meaning |
| --- | --- |
| Assessment | Testing and examining controls to decide whether they work as intended. Level 1 is the system owner's self-assessment; Level 2 is the independent assessment |
| Authorisation | The authorising official's decision, recorded on TPL-18, that \<DocuView\> may operate and that its remaining risk is accepted |
| Authorisation package | What the authorising official receives before deciding, listed in \<Assessment, Authorization, and Monitoring Management\>, section 4.5 |
| Continuous monitoring | Checking controls, risks and changes on a set schedule after authorisation, under the strategy in \<Assessment, Authorization, and Monitoring Management\>, section 4.8 |
| Independent assessor | An assessor who has had no part in designing, building, running or administering \<DocuView\>, and who confirms it on TPL-19 |
| Inherited control | A control provided by ABC Technologies, which \<DocuView\> relies on but does not run |
| Significant change | A change likely to alter \<DocuView\>'s security or privacy risk, as listed in \<Assessment, Authorization, and Monitoring Management\>, section 4.9 |

### CA.9 References

**Table CA-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, CA family, and SP 800-53B Moderate baseline | The controls this policy meets |
| NIST SP 800-37 Rev 2, Risk Management Framework | The assessment and authorisation process |
| NIST SP 800-137, Information Security Continuous Monitoring | The monitoring strategy |
| NIST SP 800-47 Rev 1, Managing the Security of Information Exchanges | Agreements for connections |
| \<Procedures\> (CA), \<Assessment, Authorization, and Monitoring Management\> and \<Security Assessment Report\> | The procedures, settings and assessment report |
| \<Risk List\> and \<Plan of Action and Milestones\> | Risks, decisions and remediation |
| UK GDPR, Data Protection Act 2018 | The laws this policy must be consistent with |

| **CHAPTER CM** |
| --- |

## CM Configuration Management

[CM.1 Purpose and scope](#cm1-purpose-and-scope) · [CM.2 The organisation's position](#cm2-the-organisations-position) · [CM.3 Control principles](#cm3-control-principles) · [CM.4 Mandatory requirements](#cm4-mandatory-requirements) · [CM.5 Responsibilities](#cm5-responsibilities) · [CM.6 Governance requirements](#cm6-governance-requirements) · [CM.7 Non-compliance and risk acceptance](#cm7-non-compliance-and-risk-acceptance) · [CM.8 Definitions](#cm8-definitions) · [CM.9 References](#cm9-references)

### CM.1 Purpose and scope

This policy sets the organisation's rules for controlling how \<DocuView\> is configured and changed, in line with the NIST SP 800-53 Rev 5 CM family (CM-1). It stands alone, as each family has its own policy. \<Configuration Management\> holds the design, and is the Configuration Management Plan that CM-9 requires. \<Procedures\> (CM) holds the steps.

It applies to DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database and the two Windows Server 2025 VMs they run on at ABC Technologies.

### CM.2 The organisation's position

\<DocuView\> must run from a known, recorded configuration, and every change must be approved, tested and traceable.

### CM.3 Control principles

1. **Known baseline:** the approved configuration is recorded and versioned.
2. **Controlled change:** no change happens without approval and testing.
3. **Least functionality:** anything not needed is turned off.
4. **Accurate inventory:** every component is recorded, and unauthorised ones are detected.

### CM.4 Mandatory requirements

1. **R1 Baselines:** baselines must be reviewed every 12 months and at each release, keeping the 3 previous configurations.
2. **R2 Change control:** changes need a Jira change request, approved by the system owner, security officer and Windows server administrator, and tested before release. Records are kept for 3 years.
3. **R3 Settings:** settings follow the CIS Benchmarks for Windows Server 2025 and PostgreSQL, with exceptions recorded.
4. **R4 Routes:** only these routes are open: HTTPS to the application, the database from the application VM only, and administration from ABC Technologies' network only. Everything else is off, and this is reviewed every 12 months.
5. **R5 Approved software:** an approved software list is kept and reviewed every 12 months. It is not technically enforced, a risk the authorising official accepted for 12 months on 6 November 2026 (NC-CM-15, NC-CM-16).
6. **R6 Installing software:** users may install software on the VMs only with approval.
7. **R7 Inventory:** the server inventory in \<System Security Plan\> and the software component inventory in \<Configuration Management\> are updated at each change, with each component's version, supplier and licence. ABC Technologies' tools detect unauthorised components monthly and alert the Windows server administrator.
8. **R8 Reproducible releases:** each release must be reproducible: code at a tag, and every image and component at a pinned version or digest recorded in the baseline.
9. **R9 Licences:** every component's licence must be known and permit \<DocuView\>'s use before it enters the baseline; the system owner records any licence decision in \<Decision Register\>.
10. **R10 Every layer:** secure settings apply to every layer: Windows Server, PostgreSQL, the application hosting and the application itself, as set in \<Configuration Management\>.
11. **R11 Impact analysis:** every change has a recorded security and privacy impact analysis against the criteria in \<Configuration Management\>, including the significant change test in \<Assessment, Authorization, and Monitoring Management\>, section 4.9.
12. **R12 Drift:** the running configuration is compared with the baseline every month, and any drift is reported to the security officer and corrected or approved through change control.

### CM.5 Responsibilities

**Table CM-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy and the plan, and approves changes |
| Authorising official | Decides Medium and High risks |
| Security officer | Approves changes, and represents security in change control |
| Windows server administrator | Approves changes, and manages VM settings and software |
| Database administrator | Manages PostgreSQL settings |
| Developers | Build, test and release changes |
| ABC Technologies | Provides detection tools and the Jira service desk |

### CM.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who changes or administers \<DocuView\>, and whenever they change.
2. **Coordination:** the system owner agrees with ABC Technologies' security contact how changes on its services are coordinated, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including the Copyright, Designs and Patents Act 1988 for software licences, ABC Technologies' policies and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 12 November 2026.

### CM.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### CM.8 Definitions

**Table CM-2: Definitions**

| Term | Meaning |
| --- | --- |
| Baseline | The approved, recorded configuration of a configuration item at a point in time, from which it can be rebuilt |
| Configuration item | Anything placed under configuration control: code, images, components, settings or documents |
| Change control board | The group that approves changes: the system owner, security officer and Windows server administrator |
| Component | A software package, image, runtime or database that \<DocuView\> is built from |
| Drift | Any difference between the running configuration and the baseline |
| Security impact analysis | The check, before a change, of its effect on security and privacy controls |
| Bill of materials | A machine-readable list of every component in a release |

### CM.9 References

**Table CM-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, CM family, and SP 800-53B Moderate baseline | The controls this policy meets |
| NIST SP 800-128, Security-Focused Configuration Management | The plan structure, board charter and impact analysis |
| CIS Benchmarks | Secure settings for Windows Server and PostgreSQL |
| Cyber Essentials | ABC Technologies' scheme: secure configuration and updates |
| \<Procedures\> (CM) and \<Configuration Management\> | The procedures and plan |
| \<Assessment, Authorization, and Monitoring Management\>, section 4.9 | What counts as a significant change |
| Copyright, Designs and Patents Act 1988 | Software licences |

| **CHAPTER CP** |
| --- |

## CP Contingency Planning

[CP.1 Purpose and scope](#cp1-purpose-and-scope) · [CP.2 The organisation's position](#cp2-the-organisations-position) · [CP.3 Control principles](#cp3-control-principles) · [CP.4 Mandatory requirements](#cp4-mandatory-requirements) · [CP.5 Responsibilities](#cp5-responsibilities) · [CP.6 Governance requirements](#cp6-governance-requirements) · [CP.7 Non-compliance and risk acceptance](#cp7-non-compliance-and-risk-acceptance) · [CP.8 Definitions](#cp8-definitions) · [CP.9 References](#cp9-references)

### CP.1 Purpose and scope

This policy sets the organisation's rules for keeping \<DocuView\> recoverable, in line with the NIST SP 800-53 Rev 5 CP family (CP-1). It stands alone, as each family has its own policy. The plan that carries it out is \<Contingency Planning Management\>, and the steps people follow are in \<Procedures\> (CP).

It applies to DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database, its backups, the secrets the applications need, and the two Windows Server 2025 VMs they run on at ABC Technologies.

### CP.2 The organisation's position

\<DocuView\>'s availability is rated Low, so a short outage can be tolerated. Losing its documents or audit records cannot, so encrypted backups and tested recovery are required before \<DocuView\> holds real documents.

### CP.3 Control principles

1. **P1 Know what matters:** recovery objectives come from a business impact analysis, not a guess.
2. **P2 Keep copies apart:** encrypted backups are held away from the main site, with one copy that an attacker on the network cannot change.
3. **P3 Test recovery:** a backup counts only once it has been restored and checked.
4. **P4 Plan ahead:** people know their part, and how to reach each other, before anything fails.
5. **P5 Coordinate:** this plan works with the incident response plan and ABC Technologies' plans.

### CP.4 Mandatory requirements

1. **R1 Recovery objectives:** recovery objectives must be set by a business impact analysis, reviewed every 12 months. Essential functions must be back within 72 hours, within a maximum tolerable downtime of 120 hours, losing no more than 24 hours of data.
2. **R2 Backups:** the database, which holds the documents and audit records, must be backed up daily with its transaction logs archived continuously; system configuration weekly; the secrets and documentation at each change.
3. **R3 Where and how:** backups must be encrypted, and held at a second ABC Technologies site that does not share the main site's hazards.
4. **R4 Restore tests:** a restore must be tested every 6 months, and after a change to the database or backups, and checked against the data before the backup.
5. **R5 Second site:** the VMs must be able to be rebuilt at that second site if the main one is lost.
6. **R6 Plan tests:** the plan must be tested every 12 months by tabletop exercise and restore test, coordinated with the incident response plan and ABC Technologies' plans.
7. **R7 Training:** people with a contingency role must be trained within 30 days of taking it and every 12 months.
8. **R8 The plan:** the plan must be approved by the system owner and authorising official, reviewed every 12 months and after a test or activation, shared with the people it names, and protected from disclosure and change.
9. **R9 Retention:** at least 14 daily, 8 weekly and 12 monthly backups must be kept, and one copy must be offline or immutable.
10. **R10 Keys and secrets:** the backup encryption key and the protected copy of the secrets must be held apart from the backups, and only the system owner and administrators may reach them.
11. **R11 Return and learning:** users return after a recovery only when the data, functions and controls have been checked. Each test or activation must end with an after-action report within 10 working days.

### CP.5 Responsibilities

**Table CP-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy and the plan, decides when to invoke it, declares recovery, and trains the role holders |
| Authorising official | Approves the plan, and decides Medium and High risks, including running in a reduced state |
| Security officer | Coordinates the plan with incident handling, keeps the activity log, confirms controls before users return, and writes after-action reports |
| Database administrator | Runs backups, tests restores and restores the database |
| Windows server administrator | Backs up system configuration, rebuilds the VMs and restores the secrets |
| ABC Technologies | Provides the second site, network services and telecommunications |

### CP.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Ownership:** the system owner manages this policy, the plan and the procedures.
2. **Approval:** the Head of Cyber approves this policy, as all policies; the system owner and authorising official approve the plan; and the system owner approves the procedures.
3. **Communication:** this policy and the procedures must be shared with everyone who administers \<DocuView\>, and whenever they change.
4. **Policy review:** every 12 months, and after a significant incident, audit finding, system change, contingency test or activation.
5. **Coordination:** the system owner agrees with ABC Technologies' security contact how the second site, network and telecommunications are provided, and records it.
6. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Article 32(1)(b) and (c), which require resilience and the ability to restore personal data in a timely manner, and the Data Protection Act 2018; ABC Technologies' policies; and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 9 November 2026.

### CP.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### CP.8 Definitions

**Table CP-2: Definitions**

| Term | Meaning |
| --- | --- |
| Business impact analysis | The analysis of how an outage harms the organisation over time, which sets the recovery objectives |
| Maximum tolerable downtime | The longest an outage can last before the harm is unacceptable |
| Recovery time objective | The longest a function can take to come back, which must be within the maximum tolerable downtime |
| Recovery point objective | The most recent point to which data must be recoverable, which sets how much data may be lost |
| Reconstitution | Checking the recovered system's data, functions and controls, and returning it to normal use |
| Second site | An ABC Technologies site, apart from the main one, that holds backups and can run rebuilt VMs |
| Immutable copy | A backup that cannot be changed or deleted for a set time, even by an administrator |
| After-action report | The record of a test or activation: what happened, against the objectives, and what will change |

### CP.9 References

**Table CP-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, CP family, and SP 800-53B Moderate baseline | The controls this policy meets |
| NIST SP 800-34 Rev. 1, Contingency Planning Guide for Federal Information Systems | The plan structure and business impact analysis |
| NIST SP 800-84, Guide to Test, Training, and Exercise Programs | Testing, exercises and after-action reports |
| UK GDPR Article 32, and the Data Protection Act 2018 | Resilience and timely restoration of personal data |
| \<Contingency Planning Management\> and \<Procedures\> (CP) | The plan and procedures |
| \<Incident Response Management\> | The incident response plan this plan works with |

| **CHAPTER IA** |
| --- |

## IA Identification and Authentication

[IA.1 Purpose and scope](#ia1-purpose-and-scope) · [IA.2 The organisation's position](#ia2-the-organisations-position) · [IA.3 Control principles](#ia3-control-principles) · [IA.4 Mandatory requirements](#ia4-mandatory-requirements) · [IA.5 Responsibilities](#ia5-responsibilities) · [IA.6 Governance requirements](#ia6-governance-requirements) · [IA.7 Non-compliance and risk acceptance](#ia7-non-compliance-and-risk-acceptance) · [IA.8 Definitions](#ia8-definitions) · [IA.9 References](#ia9-references)

### IA.1 Purpose and scope

This policy sets the organisation's rules for proving who is using \<DocuView\>, in line with the NIST SP 800-53 Rev 5 IA family (IA-1). The settings that carry it out are in \<Identification and Authentication Management\>, and the steps people follow are in \<Procedures\> (IA).

It applies to everyone who uses or administers DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database and the two Windows Server 2025 VMs they run on at ABC Technologies, and to every service account and secret they use.

### IA.2 The organisation's position

Every action in \<DocuView\> must be traceable to one known person. Access depends on a proven identity and a protected authenticator, at the assurance level set in \<Identification and Authentication Management\>, and privileged access needs stronger proof than ordinary access.

### IA.3 Control principles

1. **P1 Unique:** each person has one named identifier, which is never reused.
2. **P2 Proven:** a person's identity is established before an account is issued.
3. **P3 Strong:** authenticators are hard to guess or steal, and every sign-in needs more than a password.
4. **P4 Protected:** authenticators are never stored or sent in the clear, and secrets are not kept in source code.
5. **P5 Current:** authenticators change whenever they may be compromised.

### IA.4 Mandatory requirements

1. **R1 Who may have access:** only ABC Technologies' staff and contractors, who hold an Active Directory account and whose identity ABC Technologies' HR has checked. Non-organisational users are not allowed.
2. **R2 Identifiers:** a person's Active Directory account name is their identifier. It is unique and named, is never reused, and shows staff or contractor status. \<DocuView\> issues no identifiers of its own.
3. **R3 Sign-in:** every user must sign in through ABC Technologies' single sign-on service, AD FS. \<DocuView\> must hold no passwords and no accounts of its own. Password rules are those of ABC Technologies' corporate standard, which \<DocuView\> accepts (D-AC-21, D-AC-23).
4. **R4 Password changes:** follow ABC Technologies' corporate standard. Anyone who thinks their password is known must change it through ABC Technologies' service desk and tell the security officer.
5. **R5 Secrets:** service account secrets and the signing key must be held outside source code, changed every 12 months and when an administrator leaves, and never recorded in clear.
6. **R6 Multi-factor:** every user must sign in with multi-factor authentication, which AD FS provides (D-AC-23). This carries out the authorising official's decision that multi-factor sign-in is required (D-IA-07).
7. **R7 Signing in again:** after 30 minutes idle and after 8 hours. A change to a person's groups takes effect when they next sign in.
8. **R8 Assurance levels:** the identity and authenticator assurance levels in \<Identification and Authentication Management\>, section 4.4, must be met for each user group, and reviewed every 12 months.
9. **R9 Authenticator inventory:** every authenticator must be listed in \<Identification and Authentication Management\>, section 4.5, with its owner, storage and change period, and reviewed every 12 months.
10. **R10 Protection:** authenticators and tokens must travel only over encrypted connections, and \<DocuView\> must accept only a token that AD FS has signed. A global administrator must be able to end any user's sessions at once.
11. **R11 Loss:** a lost, stolen or exposed authenticator must be reported straight away to ABC Technologies' service desk and the security officer, and replaced or reset.

### IA.5 Responsibilities

**Table IA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy, authorises privileged roles and manages the members of their AD groups, and reviews the assurance levels and authenticator inventory |
| Authorising official | Accepts the assurance levels, and decides Medium and High risks, including multi-factor sign-in |
| Project access approver | Authorises access to their project, and manages the members of its AD groups |
| Global administrator | Ends sessions when asked. Issues no identifiers or passwords: \<DocuView\> has none |
| Windows server and database administrators | Hold and change the service secrets and signing key |
| ABC Technologies | Proves identity through pre-employment checks; provides the Active Directory accounts, AD FS sign-in with multi-factor authentication, and password and second factor resets; identifies devices on its network |
| Everyone with an account | Protects their authenticators and reports loss or suspected compromise |

### IA.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses or administers \<DocuView\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review and records the result. Breaches may lead to loss of access and disciplinary action.
3. **Coordination:** the system owner agrees with ABC Technologies' security contact how identity proofing, device identification and sign-in through AD FS are provided, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Article 32, which requires appropriate security of personal data, and the Computer Misuse Act 1990; ABC Technologies' policies; NIST SP 800-53 Rev 5; and NIST SP 800-63B Revision 4. The legal adviser reviewed it on 9 November 2026.

### IA.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### IA.8 Definitions

**Table IA-2: Definitions**

| Term | Meaning |
| --- | --- |
| Identifier | The name that identifies one person or service. For a person it is their Active Directory account name |
| Authenticator | Something used to prove an identity: a password, a second factor, a key or a secret |
| Multi-factor sign-in | Signing in with two different kinds of authenticator, such as a password and an app or key |
| Identity assurance level | How sure the organisation is that a person is who they claim, from identity proofing |
| Authenticator assurance level | How sure the organisation is that the person signing in holds the account |
| Replay resistance | Protection against reusing a captured sign-in or token |
| Single sign-on | Signing in once, to ABC Technologies' AD FS, which then vouches for the person to \<DocuView\>. \<DocuView\> never sees the password |

### IA.9 References

**Table IA-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, IA family, and SP 800-53B Moderate baseline | The controls this policy meets |
| NIST SP 800-63-4, Digital Identity Guidelines | Choosing assurance levels |
| NIST SP 800-63B Revision 4, Authentication and Authenticator Management | Password, multi-factor and session rules |
| NCSC password guidance | The UK view on password rules |
| UK GDPR Article 32, and the Computer Misuse Act 1990 | Security of personal data, and unauthorised access |
| \<Identification and Authentication Management\> and \<Procedures\> (IA) | The settings and procedures |

| **CHAPTER IR** |
| --- |

## IR Incident Response

[IR.1 Purpose and scope](#ir1-purpose-and-scope) · [IR.2 The organisation's position](#ir2-the-organisations-position) · [IR.3 Control principles](#ir3-control-principles) · [IR.4 Mandatory requirements](#ir4-mandatory-requirements) · [IR.5 Responsibilities](#ir5-responsibilities) · [IR.6 Governance requirements](#ir6-governance-requirements) · [IR.7 Non-compliance and risk acceptance](#ir7-non-compliance-and-risk-acceptance) · [IR.8 Definitions](#ir8-definitions) · [IR.9 References](#ir9-references)

### IR.1 Purpose and scope

This policy sets the organisation's rules for handling security incidents affecting \<DocuView\>, in line with the NIST SP 800-53 Rev 5 IR family (IR-1) and NIST SP 800-61 Revision 3. It stands alone, as each family has its own policy. The plan that carries it out is \<Incident Response Management\>, and the steps people follow are in \<Procedures\> (IR).

It applies to DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database, its backups and secrets, the two Windows Server 2025 VMs they run on at ABC Technologies, and everyone who uses or administers them.

### IR.2 The organisation's position

Incidents are reported at once, without blame. \<DocuView\> holds Restricted documents, and HR documents hold personal data, so a delay can cause harm and can breach the law.

### IR.3 Control principles

1. **P1 Report early:** a suspected incident is reported straight away.
2. **P2 Preserve evidence:** contain the harm, and do not clean up first.
3. **P3 One plan:** everyone follows the same plan, so handling is consistent.
4. **P4 Learn:** each incident improves the plan, training and controls.

### IR.4 Mandatory requirements

1. **R1 Reporting:** everyone must report a suspected incident to the security officer within 1 hour.
2. **R2 Severity and targets:** the security officer must set each incident's severity, and contain it within the target in \<Incident Response Management\>, section 4.6.
3. **R3 Others told:** the security officer must tell ABC Technologies' security contact and any affected supplier.
4. **R4 Personal data breaches:** the legal adviser must tell the ICO within 72 hours of the organisation becoming aware of a reportable breach, and tell the people affected without undue delay when the risk to them is high. Every breach must be recorded, with the reason if it is not reported.
5. **R5 Records:** incidents are tracked and recorded on TPL-10, and in Jira Service Desk once it is set up.
6. **R6 Evidence:** evidence must be preserved, hashed and its custody recorded before anything is changed.
7. **R7 Training:** people with an incident role must be trained within 30 days of taking it, every 12 months and after a plan change.
8. **R8 Testing:** the plan must be tested by tabletop exercise every 12 months, coordinated with the contingency plan.
9. **R9 The plan:** the plan must be approved by the Head of Cyber, reviewed every 12 months and after an incident, and protected from disclosure and change.
10. **R10 Crime:** a suspected crime or significant cyber attack must be reported by the system owner to the NCSC or to Report Fraud, the national police reporting service that replaced Action Fraud.

### IR.5 Responsibilities

**Table IR-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies, and the plan |
| System owner | Owns this policy, decides on recovery, and reports crime |
| Authorising official | Decides on the risk arising from an incident |
| Security officer | Owns the plan, leads incident handling, and keeps the register |
| Legal adviser | Decides on and makes reports to the ICO and to the people affected |
| Windows server and database administrators | Contain, recover and preserve evidence |
| Everyone | Reports suspected incidents at once |
| ABC Technologies | Receives reports, and helps through its security contact |

### IR.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Approval:** the Head of Cyber approves this policy, as all policies, and the plan; the system owner approves the procedures.
2. **Communication:** this policy and the procedures must be shared with everyone who administers \<DocuView\>, and whenever they change.
3. **Coordination:** the system owner agrees with ABC Technologies' security contact how incidents are shared, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Articles 33 and 34, the Data Protection Act 2018 and the Computer Misuse Act 1990; ABC Technologies' policies; and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 10 November 2026.

### IR.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### IR.8 Definitions

**Table IR-2: Definitions**

| Term | Meaning |
| --- | --- |
| Security incident | An event that harms, or may harm, the confidentiality, integrity or availability of \<DocuView\> or its data, or breaks a security policy |
| Personal data breach | A security incident leading to the accidental or unlawful loss, change, disclosure of, or access to personal data |
| Severity | The level, from Low to Critical, that sets how fast an incident is handled and who is told |
| Containment | Action that stops an incident spreading or causing more harm |
| Evidence | Records and copies kept to show what happened, with a hash and a record of custody |
| Playbook | Pre-agreed first actions for a common kind of incident |

### IR.9 References

**Table IR-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, IR family, and SP 800-53B Moderate baseline | The controls this policy meets |
| NIST SP 800-61 Revision 3 | Incident response as part of cyber risk management |
| ICO guide to personal data breaches | Reporting to the ICO and telling the people affected |
| NCSC incident management guidance | Reporting and handling cyber incidents in the UK |
| UK GDPR Articles 33 and 34; Data Protection Act 2018; Computer Misuse Act 1990 | The legal duties |
| \<Incident Response Management\> and \<Procedures\> (IR) | The plan and procedures |

| **CHAPTER MA** |
| --- |

## MA Maintenance

[MA.1 Purpose and scope](#ma1-purpose-and-scope) · [MA.2 The organisation's position](#ma2-the-organisations-position) · [MA.3 Control principles](#ma3-control-principles) · [MA.4 Mandatory requirements](#ma4-mandatory-requirements) · [MA.5 Responsibilities](#ma5-responsibilities) · [MA.6 Governance requirements](#ma6-governance-requirements) · [MA.7 Non-compliance and risk acceptance](#ma7-non-compliance-and-risk-acceptance) · [MA.8 Definitions](#ma8-definitions) · [MA.9 References](#ma9-references)

### MA.1 Purpose and scope

This policy sets the organisation's rules for maintaining \<DocuView\>, in line with the NIST SP 800-53 Rev 5 MA family (MA-1). It stands alone, as each family has its own policy. The settings, lists and routes that carry it out are in \<Maintenance Management\>, and the steps people follow are in \<Procedures\> (MA).

It applies to the hardware and hypervisor, the two Windows Server 2025 VMs, PostgreSQL, DV\_Web, DV\_Admin\_UI and DV\_API, including the maintenance functions built into \<DocuView\>. It applies to everyone who maintains them: administrators, developers, ABC Technologies' engineers and any supplier.

Maintenance means preventive and corrective work, repair and replacement, done on site or remotely. Fixing flaws (SI-2) and releasing new versions (CM-3) follow their own policies, but use the same change records.

### MA.2 The organisation's position

Maintenance gives people powerful access, often at short notice, and \<DocuView\> has maintenance functions of its own that can change or delete data. Maintenance must therefore be approved, done by known people with known tools over known routes, checked afterwards and recorded.

### MA.3 Control principles

1. **P1 Approve first:** no maintenance happens without approval.
2. **P2 Known people, tools and routes:** only those on the approved lists are used.
3. **P3 Protect data:** nothing leaves with \<DocuView\>'s data on it unless approved and protected.
4. **P4 Check and record:** controls are checked after the work, and every job is recorded and reviewed.

### MA.4 Mandatory requirements

1. **R1 Change record:** all maintenance must be scheduled and approved in a change record before work starts. Emergency maintenance follows the emergency change rule and is recorded within 1 working day.
2. **R2 Records:** every maintenance job must be recorded on TPL-12, with the fields set in \<Maintenance Management\>. The security officer reviews the records every month against the change records.
3. **R3 Check afterwards:** after every job, the administrator must run the checklist in \<Procedures\> (MA), and the security officer must review and sign the result.
4. **R4 Approved tools:** only tools on the approved list in \<Maintenance Management\> may be used. The list is reviewed every 12 months. Tools are inspected before use, and media holding diagnostic or test programs are scanned for malicious code first.
5. **R5 Built-in maintenance functions:** the maintenance pages built into \<DocuView\> may be used only under an approved change record, with a second person present, until they are removed.
6. **R6 Remote (nonlocal) maintenance:** remote maintenance must use only the routes in \<Maintenance Management\>, with multi-factor sign-in, be logged, and be ended as soon as the work is finished. The admin portal must be reachable only through the managed route.
7. **R7 Maintenance people:** only people on the approved list may maintain \<DocuView\> without an escort. They must be screened, have signed Part B of \<Security Operating Procedures\> and use a named account. Supplier accounts are temporary, limited to the job and disabled afterwards. Anyone else must be escorted and supervised by someone on the list.
8. **R8 Equipment removal:** the system owner must approve removing any equipment, and it must be sanitised first.
9. **R9 Data leaving for maintenance or support:** no copy of \<DocuView\> data, database dump, log or screenshot may leave the VMs for maintenance or support without the system owner's approval. It must be kept to the minimum, encrypted, recorded and deleted when no longer needed.
10. **R10 Timely maintenance:** support and parts for the hardware and hypervisor must be available within 24 hours of a failure. Software must stay on supported versions, with a replacement planned at least 6 months before support ends.
11. **R11 Schedule and notice:** preventive maintenance follows the schedule in \<Procedures\> (MA). Users are given 2 working days' notice of planned maintenance that affects them.
12. **R12 Session records:** the events of each remote maintenance session must be logged and reviewed weekly.

### MA.5 Responsibilities

**Table MA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy; approves the lists of people and tools, equipment removal and any data leaving for support |
| Security officer | Reviews maintenance records monthly and session logs weekly; reviews and signs the check after maintenance |
| Windows server administrator | Maintains the VMs, keeps the tool list and runs the check after maintenance |
| Database administrator | Maintains the database and runs the check after database maintenance |
| Developers | Maintain the applications through releases; never use the built-in maintenance pages outside R5 |
| Global administrator | The only role that can open the built-in maintenance pages, and does so only under R5 |
| ABC Technologies | Maintains the hardware and hypervisor, provides support and parts within 24 hours, provides the managed route, and sanitises equipment |

### MA.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who maintains \<DocuView\>, and whenever they change.
2. **Coordination:** the system owner agrees with ABC Technologies how its maintenance, routes and support are carried out and evidenced, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Article 32, and Article 28 where a supplier handles personal data during maintenance or support, and the Computer Misuse Act 1990; ABC Technologies' policies; and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 10 November 2026.

### MA.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### MA.8 Definitions

**Table MA-2: Definitions**

| Term | Meaning |
| --- | --- |
| Maintenance | Preventive or corrective work on a \<DocuView\> component, including repair and replacement |
| Remote (nonlocal) maintenance | Maintenance done over a network rather than in person at the component |
| Maintenance tool | Any program, device or function used to diagnose or maintain \<DocuView\> |
| Built-in maintenance function | A page or function inside \<DocuView\> that changes its data or set-up, such as Database Update or Fresh Start |
| Escort | A person on the approved list who supervises someone who is not |
| Change record | The approved record of a change or maintenance job, on TPL-6 or in Jira once it is set up |
| Security-critical component | A component that \<DocuView\>'s security depends on, listed in \<Maintenance Management\> |

### MA.9 References

**Table MA-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, MA family, and SP 800-53B Moderate baseline | The controls this policy meets |
| NIST SP 800-53A Rev 5 | How the controls are assessed |
| NIST SP 800-88 Revision 2 and IEEE 2883-2022 | Sanitising equipment and media |
| NCSC Secure System Administration | Trusted devices, multi-factor sign-in and monitoring for administration |
| UK GDPR Articles 28 and 32; Computer Misuse Act 1990 | The legal duties |
| \<Maintenance Management\>, \<Procedures\> (MA), \<Procedures\> (CM) and \<Security Operating Procedures\> | The settings, procedures, change control and rules people sign |

| **CHAPTER MP** |
| --- |

## MP Media Protection

[MP.1 Purpose and scope](#mp1-purpose-and-scope) · [MP.2 The organisation's position](#mp2-the-organisations-position) · [MP.3 Control principles](#mp3-control-principles) · [MP.4 Mandatory requirements](#mp4-mandatory-requirements) · [MP.5 Responsibilities](#mp5-responsibilities) · [MP.6 Governance requirements](#mp6-governance-requirements) · [MP.7 Non-compliance and risk acceptance](#mp7-non-compliance-and-risk-acceptance) · [MP.8 Definitions](#mp8-definitions) · [MP.9 References](#mp9-references)

### MP.1 Purpose and scope

This policy sets the organisation's rules for protecting media that hold \<DocuView\>'s information, in line with the NIST SP 800-53 Rev 5 MP family (MP-1). It stands alone, as each family has its own policy. The media inventory, values and methods that carry it out are in \<Media Protection Management\>, and the steps people follow are in \<Procedures\> (MP).

It applies to every place \<DocuView\> information is held outside the running application: the VMs' disks, database and key volumes, export files, application logs, backups, the audit archive, the secret store, support copies, incident evidence, the document set, users' managed devices and approved locations, managed printers, test PCs and paper. It applies to everyone who uses, administers or maintains \<DocuView\>, and to ABC Technologies for the media it handles.

### MP.2 The organisation's position

\<DocuView\> has no removable media of its own, but its documents leave the application as exports, downloads, backups, logs and printouts. Each copy must be protected as the documents themselves are, marked, kept only as long as needed and sanitised when it is no longer needed.

### MP.3 Control principles

1. **P1 Same protection:** every copy gets the protection of the information it holds.
2. **P2 Know where it is:** every place \<DocuView\> information is held is listed, and copies are kept only as long as needed.
3. **P3 Marked:** \<DocuView\> information is marked RESTRICTED wherever it goes.
4. **P4 Nothing left behind:** media are sanitised, by an approved method, before reuse, release or disposal.

### MP.4 Mandatory requirements

1. **R1 Media inventory:** every place \<DocuView\> information is held must be listed in \<Media Protection Management\>, with its protection and sanitising method, and the list reviewed every 12 months.
2. **R2 Access:** digital media may be reached only by the roles named in \<Media Protection Management\>. Only editors in a project may create exports of it.
3. **R3 Marking:** all \<DocuView\> information is marked RESTRICTED, with the document's own classification alongside. Printouts are marked by hand until \<DocuView\> marks them (PA-87). No media is exempt.
4. **R4 Storage:** digital media must be stored encrypted in controlled areas: ABC Technologies' data centres, or a managed device. Printouts are locked away when not in use.
5. **R5 Export copies:** an export copy on the server must be removed once downloaded, and within 24 hours at most. Until \<DocuView\> does this itself (PA-86), the Windows server administrator checks it each working day.
6. **R6 Users' copies:** exports and downloads may be saved only in approved ABC Technologies locations on a managed device, kept to the minimum, and deleted within 30 days once no longer needed (\<Security Operating Procedures\>, A28 and A30 to A35).
7. **R7 Transport:** media are physically transported only by exception, approved by the system owner, encrypted or sealed, tracked and recorded on TPL-13. Network copies, such as backups to the second site, are protected under SC-8 and CP-6 and must be encrypted first. Printouts do not leave the site without approval.
8. **R8 Sanitising:** media must be sanitised before reuse, release or disposal following NIST SP 800-88 Revision 2 and IEEE 2883-2022, using the method set for each media type in \<Media Protection Management\>. Cryptographic erase is used for encrypted virtual disks and backups. Paper is cross-cut shredded to DIN 66399 level P-4 or better.
9. **R9 Records:** each sanitising action is recorded on TPL-13 with the item, method, verification and certificate. The system owner checks a sample of ABC Technologies' certificates every 12 months.
10. **R10 Portable storage:** USB and other portable storage are blocked on users' devices unless an exception is approved. No USB device is passed through to the VMs.
11. **R11 Ownerless devices:** portable storage with no identifiable owner must not be used, and must be handed to the security officer.
12. **R12 Support copies:** data sent for maintenance or support follows \<Procedures\>, PRO-MA-7.

### MP.5 Responsibilities

**Table MP-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy and the media inventory; approves portable storage exceptions and physical transport; checks sanitising certificates |
| Windows server administrator | Protects the VM disks and export folder, and checks the export folder each working day |
| Database administrator | Protects the database volumes and backups |
| Security officer | Receives ownerless devices and reports media incidents |
| Everyone | Follows the rules for exports, downloads and printouts, and marks and shreds printouts |
| ABC Technologies | Stores, moves and sanitises physical disks and backup media, manages users' devices and blocks USB |

### MP.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses or administers \<DocuView\>, and whenever they change.
2. **Coordination:** the system owner agrees with ABC Technologies how it handles media and evidences that, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Articles 5(1)(f) and 32 and the Data Protection Act 2018; ABC Technologies' policies; and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 10 November 2026.

### MP.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### MP.8 Definitions

**Table MP-2: Definitions**

| Term | Meaning |
| --- | --- |
| Media | Anything that holds \<DocuView\> information outside the running application: disks, volumes, files, devices, backups and paper |
| Digital media | Media that need power to be read, including virtual disks, export files and managed devices |
| Export copy | A copy of documents made by \<DocuView\>'s export or download functions |
| Marking | The RESTRICTED label, with the document's own classification, on what \<DocuView\> shows or produces |
| Sanitising | Making information on media impossible to recover, by clearing, purging, cryptographic erase or destruction |
| Cryptographic erase | Sanitising encrypted media by destroying the keys, so the data can no longer be decrypted |
| Controlled area | A place where access is limited to authorised people: ABC Technologies' data centres and locked storage |

### MP.9 References

**Table MP-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, MP family, and SP 800-53B Moderate baseline | The controls this policy meets |
| NIST SP 800-88 Revision 2 and IEEE 2883-2022 | Sanitising media |
| NCSC Secure sanitisation of storage media | UK guidance on sanitising and disposal |
| DIN 66399 | Shredding levels for paper |
| UK GDPR Articles 5(1)(f) and 32; Data Protection Act 2018 | The legal duties |
| \<Media Protection Management\>, \<Procedures\> (MP) and \<Security Operating Procedures\> | The inventory and methods, the procedures, and the rules people sign |

| **CHAPTER PE** |
| --- |

## PE Physical and Environmental Protection

[PE.1 Purpose and scope](#pe1-purpose-and-scope) · [PE.2 The organisation's position](#pe2-the-organisations-position) · [PE.3 Control principles](#pe3-control-principles) · [PE.4 Mandatory requirements](#pe4-mandatory-requirements) · [PE.5 Responsibilities](#pe5-responsibilities) · [PE.6 Governance requirements](#pe6-governance-requirements) · [PE.7 Non-compliance and risk acceptance](#pe7-non-compliance-and-risk-acceptance) · [PE.8 Definitions](#pe8-definitions) · [PE.9 References](#pe9-references)

### PE.1 Purpose and scope

This policy sets the organisation's rules for the physical and environmental protection of \<DocuView\>, in line with the NIST SP 800-53 Rev 5 PE family (PE-1). It stands alone, as each family has its own policy. The values, inheritance matrix and site details that carry it out are in \<Physical and Environmental Protection Management\>, and the steps people follow are in \<Procedures\> (PE).

It applies to the data centre that hosts the two VMs, the second site that holds backups and is used for recovery, the offices where \<DocuView\> is used and printed, and the homes of people who work remotely.

### PE.2 The organisation's position

ABC Technologies runs the buildings and data centres, so \<DocuView\> inherits most of their protection. The organisation does not run the sites, but it must know that they meet its requirements. It treats each inherited control as not shown until ABC Technologies has evidenced it, and it protects the parts it does run: screens, printouts and home working.

### PE.3 Control principles

1. **P1 Inherit with evidence:** a physical control counts only once ABC Technologies has evidenced it.
2. **P2 Same protection everywhere:** the second site meets the same requirements as the main one.
3. **P3 Protect what users see:** screens and printouts are protected by the people who use them.
4. **P4 Report physical events:** physical incidents are handled as security incidents.

### PE.4 Mandatory requirements

1. **R1 Inheritance matrix:** each PE control must be listed in \<Physical and Environmental Protection Management\> with ABC Technologies' part, \<DocuView\>'s part and the evidence that closes it, and reviewed every 12 months.
2. **R2 Evidence:** ABC Technologies must evidence the data centres' physical and environmental protection, preferably by its ISO/IEC 27001 certificate, Statement of Applicability and audit findings for Annex A.7, or a SOC 2 report. The system owner reviews it every 12 months and after a change of site.
3. **R3 Requirements:** the data centres must meet the values in \<Physical and Environmental Protection Management\>, including temperature and humidity within the ASHRAE TC 9.9 recommended envelope.
4. **R4 Second site:** the second site must meet the same requirements as the main data centre.
5. **R5 Site inspection:** each data centre, the main site and the second site, is inspected once, at Level 2, by the independent assessor or ABC Technologies' auditor using TPL-20, and again after a change of site.
6. **R6 Printing:** \<DocuView\> documents may be printed only on ABC Technologies' managed printers with secure release, and collected at once.
7. **R7 Screens:** screens must be locked when left and placed so that others cannot read them.
8. **R8 Home working:** remote working is allowed only from home, unless the system owner approves another place, on ABC Technologies' managed devices and route. \<DocuView\> documents must not be printed at home unless approved, and must be worked on where others in the home cannot see them.
9. **R9 Physical incidents:** the loss or theft of a device or printout, unauthorised entry to a data centre, and fire, flood or power loss affecting \<DocuView\> must be reported to the security officer at once and handled under \<Incident Response Management\>.
10. **R10 Physical access compensation:** VM disks must be encrypted (PA-52), so that physical access to the hosts does not expose \<DocuView\> information.

### PE.5 Responsibilities

**Table PE-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy and the inheritance matrix; reviews ABC Technologies' evidence; approves remote work away from home and printing at home |
| Security officer | Assesses home working controls every 12 months; receives physical incident reports |
| Independent assessor | Completes the site inspection at Level 2 |
| Everyone | Protects screens and printouts, and reports physical incidents |
| ABC Technologies | Provides and evidences physical and environmental protection at both sites, the managed printers and the managed devices |

### PE.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses or administers \<DocuView\>, and whenever they change.
2. **Policy review:** every 12 months, and after a significant incident, audit finding or change of site.
3. **Coordination:** the system owner agrees with ABC Technologies how physical protection is evidenced at both sites, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, including the Regulatory Reform (Fire Safety) Order 2005 and UK GDPR Article 32; ABC Technologies' policies; and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 10 November 2026.

### PE.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### PE.8 Definitions

**Table PE-2: Definitions**

| Term | Meaning |
| --- | --- |
| Data centre | The ABC Technologies facility that hosts \<DocuView\>'s VMs |
| Second site | The ABC Technologies facility that holds backups and is used for recovery |
| Inherited control | A control that ABC Technologies provides and \<DocuView\> relies on |
| Inheritance matrix | The table in \<Physical and Environmental Protection Management\> showing who provides each PE control and what evidence closes it |
| Secure release | Printing that holds a job until the user releases it at the printer |
| Physical incident | Loss, theft, unauthorised entry, or a fire, flood or power event affecting \<DocuView\> |

### PE.9 References

**Table PE-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, PE family, and SP 800-53B Moderate baseline | The controls this policy meets |
| ISO/IEC 27001:2022, Annex A.7; AICPA SOC 2, CC6.4 | How ABC Technologies evidences physical controls |
| ASHRAE TC 9.9 thermal guidelines | Data centre temperature and humidity |
| NCSC home working guidance; NPSA physical security guidance | UK guidance for home working and sites |
| Regulatory Reform (Fire Safety) Order 2005; UK GDPR Article 32 | The legal duties |
| \<Physical and Environmental Protection Management\>, \<Procedures\> (PE), \<Incident Response Management\> and \<Security Operating Procedures\> | The values and matrix, procedures, incident plan and the rules people sign |

| **CHAPTER PL** |
| --- |

## PL Planning

[PL.1 Purpose and scope](#pl1-purpose-and-scope) · [PL.2 The organisation's position](#pl2-the-organisations-position) · [PL.3 Control principles](#pl3-control-principles) · [PL.4 Mandatory requirements](#pl4-mandatory-requirements) · [PL.5 Responsibilities](#pl5-responsibilities) · [PL.6 Governance requirements](#pl6-governance-requirements) · [PL.7 Non-compliance and risk acceptance](#pl7-non-compliance-and-risk-acceptance) · [PL.8 Definitions](#pl8-definitions) · [PL.9 References](#pl9-references)

### PL.1 Purpose and scope

This policy sets the organisation's rules for security and privacy planning for \<DocuView\>, in line with the NIST SP 800-53 Rev 5 PL family (PL-1). It stands alone, as each family has its own policy. The register of plans and the values that carry it out are in \<Planning Management\>, and the steps people follow are in \<Procedures\> (PL).

It applies to every system plan for \<DocuView\>: the System Security Plan, the privacy plan and the supply chain risk management plan, which NIST SP 800-18 Rev 2 calls the system plans. It also covers the plans and documents they rely on, the rules of behaviour, the security architecture and the choice and tailoring of the baseline.

### PL.2 The organisation's position

\<DocuView\>'s security and privacy are planned and written down before they are relied on. The plans describe what exists today and what is planned, without claiming compliance that has not been shown. Approving a plan does not authorise the system: only the authorising official's decision on TPL-18 does that.

### PL.3 Control principles

1. **P1 One current set:** the SSP is the single statement of how controls are met, and every plan it relies on is listed in one register.
2. **P2 Rules before access:** nobody gets access without signing the rules.
3. **P3 Plans change with the system:** plans change when the system, its risks or an assessment changes, and every review and change is recorded.
4. **P4 Plans are Restricted:** plans describe weaknesses and must be protected like the system itself.

### PL.4 Mandatory requirements

1. **R1 Register of plans:** every plan in force must be listed in \<Planning Management\>, section 4.2, with its owner, version, approver and next review.
2. **R2 Approval:** the System Security Plan must be approved by the system owner, with the Head of Cyber's concurrence, and accepted by the authorising official as an accurate record. The privacy plan must be approved by the legal adviser and the authorising official. The supply chain plan is approved by the system owner.
3. **R3 Review and change records:** each system plan must keep a plan review log (who reviewed, their role, the date, the outcome and actions) separate from its change history. Plans are reviewed every 12 months and after an assessment, significant change or problem found in use.
4. **R4 Sharing:** the SSP and its changes must be shared with the Head of Cyber, administrators and ABC Technologies' security contact, and each issue recorded in the plan review log.
5. **R5 Protection:** plans and assessment evidence are Restricted. They must be kept in the restricted SharePoint area (D-GEN-15), never in a code repository or a public location, and only people who need them may read or change them.
6. **R6 Rules of behaviour:** the Security Operating Procedures are the rules of behaviour. Part A applies to everyone, and Part B, the privileged rules, to administrators as well. Everyone signs before access, and the signature is recorded on TPL-21 and in the register of signatures.
7. **R7 Signing again:** everyone signs again every 12 months, and after a material change to the rules: a new or stricter rule, a changed consequence, new monitoring or a new privileged duty. The system owner decides whether a change is material and records it in the SyOps change history.
8. **R8 Social media:** \<DocuView\> information must not be placed on social media or external sites, and work credentials must not be used on them.
9. **R9 Architecture:** \<Security Architecture\> must state the security approach, trust zones, layers of defence, and assumptions and dependencies, and be reviewed every 12 months and after a significant change. Its changes must be reflected in the SSP, the privacy plan, the ConOps, the critical components list and procurement.
10. **R10 Baseline and tailoring:** NIST SP 800-53 Rev 5 Moderate, with the privacy baseline, is the baseline. It may be tailored only through \<Tailoring Register\>, with a rationale, a condition and a recorded decision.

### PL.5 Responsibilities

**Table PL-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies, and concurs with the SSP |
| Authorising official | Accepts the SSP as an accurate record, approves the privacy plan, accepts the tailoring register as a record, and makes the authorisation decision |
| System owner | Owns this policy, the plans and the register of plans; keeps the review logs, the signed rules and the register of signatures; decides whether a change to the rules is material |
| Legal adviser | Reviews this policy and approves the privacy plan |
| Administrators | Sign Parts A and B of the rules |
| Everyone | Signs Part A of the rules, and follows them |

### PL.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<DocuView\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-PlanConsistency.ps1, and records the result in the plan review log.
3. **Coordination:** the system owner coordinates the plans with the Head of Cyber, administrators, the legal adviser and ABC Technologies' security contact.
4. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR and the Data Protection Act 2018 for the privacy plan; ABC Technologies' policies; and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 11 November 2026.

### PL.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### PL.8 Definitions

**Table PL-2: Definitions**

| Term | Meaning |
| --- | --- |
| System plans | The System Security Plan, privacy plan and supply chain risk management plan, as in NIST SP 800-18 Rev 2 |
| Plan review log | A record of each review of a plan: who, their role, the date, the outcome and actions |
| Change history | A record of each change to a plan: version, date and what changed |
| Rules of behaviour | \<Security Operating Procedures\>: Part A for everyone, and Part B for privileged users |
| Material change | A change to the rules that adds or tightens a rule, changes a consequence, adds monitoring or adds a privileged duty |
| Tailoring | Deciding, with a rationale, that a baseline control or part does not apply, or applies in a changed form |

### PL.9 References

**Table PL-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, PL family, and SP 800-53B Moderate and privacy baselines | The controls this policy meets |
| NIST SP 800-18 Rev 2 (June 2026) | What a system plan contains, its approval, review and change records |
| NIST SP 800-37 Rev 2, tasks S-2 and S-6 | Tailoring and plan approval |
| UK GDPR and the Data Protection Act 2018 | The legal basis for the privacy plan |
| \<Planning Management\>, \<Procedures\> (PL), \<Security Operating Procedures\>, \<Security Architecture\> and \<Tailoring Register\> | The register and values, procedures, rules, architecture and tailoring |

| **CHAPTER PS** |
| --- |

## PS Personnel Security

[PS.1 Purpose and scope](#ps1-purpose-and-scope) · [PS.2 The organisation's position](#ps2-the-organisations-position) · [PS.3 Control principles](#ps3-control-principles) · [PS.4 Mandatory requirements](#ps4-mandatory-requirements) · [PS.5 Responsibilities](#ps5-responsibilities) · [PS.6 Governance requirements](#ps6-governance-requirements) · [PS.7 Non-compliance and risk acceptance](#ps7-non-compliance-and-risk-acceptance) · [PS.8 Definitions](#ps8-definitions) · [PS.9 References](#ps9-references)

### PS.1 Purpose and scope

This policy sets the organisation's rules for personnel security for \<DocuView\>, in line with the NIST SP 800-53 Rev 5 PS family (PS-1). It stands alone, as each family has its own policy. The designations, screening standard, time limits and register are in \<Personnel Security Management\>, and the steps people follow are in \<Procedures\> (PS).

It applies to everyone who uses, administers or develops \<DocuView\>, including external people and ABC Technologies' staff who hold a \<DocuView\> role.

### PS.2 The organisation's position

\<DocuView\> holds Restricted HR documents, so the people trusted with it matter as much as its technical controls. ABC Technologies employs most of them, so its screening, HR and disciplinary processes are used, and it must evidence them. \<DocuView\> adds what is specific to it: a risk designation for every role, a minimum it expects of screening, signed agreements, and time limits when people move or leave.

### PS.3 Control principles

1. **Check first:** people are screened and sign their agreements before getting access.
2. **Match the risk:** roles with more power carry a higher risk designation, and more is asked of them.
3. **Act on change:** access follows people's roles when they move or leave, and fastest where the risk is highest.
4. **Hold only what is needed:** \<DocuView\> records that a check was passed, never the result of the check.

### PS.4 Mandatory requirements

1. **R1 Risk designations:** every role in \<Roles and Responsibilities\> must have a risk designation in \<Personnel Security Management\>, either higher risk or standard. The designations must be reviewed every 12 months, and when a role's access changes.
2. **R2 Screening before access:** nobody may be given access to \<DocuView\> until ABC Technologies has confirmed that they passed its pre-employment screening. That screening must cover at least identity, the right to work, employment history and a basic criminal record check.
3. **R3 Rescreening:** screening must be confirmed again before someone moves into a higher risk role, and every 5 years for anyone in one.
4. **R4 Screening data:** \<DocuView\> must record only that screening was confirmed, by whom and when. Screening results and criminal record data stay with ABC Technologies and must never be stored in \<DocuView\> or its records.
5. **R5 Leavers:** a leaver's \<DocuView\> access must be disabled within 5 working days, on the condition in \<Access Control Management\>, P-AC-06. Their credentials must be revoked, any shared secret they knew must be changed, and the documents they managed must stay available.
6. **R6 Higher-risk leavers:** access must be disabled within 1 hour of notice when the person holds a higher risk role, is dismissed, or is suspected of misuse.
7. **R7 Movers:** a mover's access must be reviewed, and the system owner told, within 1 working day.
8. **R8 Access agreements:** everyone must sign ABC Technologies' confidentiality agreement and \<Security Operating Procedures\> before access, and sign again every 12 months and after a material change to the rules.
9. **R9 External people:** contracts with external people must state their security duties. Suppliers must report leavers and movers within 1 working day, and their compliance must be checked every 12 months.
10. **R10 Sanctions:** a breach of the rules is handled through ABC Technologies' disciplinary process. The system owner must be told within 1 working day of a formal sanction that involves \<DocuView\>.
11. **R11 Role descriptions:** the security and privacy duties of every \<DocuView\> role must be stated in \<Roles and Responsibilities\>, and ABC Technologies' job descriptions must refer to them.
12. **R12 Records and checking:** each of these steps must be recorded on the forms named in \<Procedures\> (PS). Test-PlanConsistency.ps1 (check L17) must show that every role has a designation, at each review.

### PS.5 Responsibilities

**Table PS-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Decides Medium and High risks |
| System owner | Owns this policy; keeps the designations, the personnel security register and the signed agreements; checks screening is confirmed before access; monitors external people |
| Global administrator | Ends a leaver's sessions, and acts within the time limits |
| Line managers | Report movers and leavers within 1 working day |
| Legal adviser | Reviews this policy and the laws it names |
| ABC Technologies | Screens people and holds the results; runs HR and disciplinary processes; holds exit interviews and recovers equipment; disables the network account of a leaver at once; provides job descriptions |

### PS.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<DocuView\> and every line manager of a \<DocuView\> user, and whenever they change.
2. **Coordination:** the system owner agrees with ABC Technologies how its screening, HR and disciplinary processes are used and evidenced, and records it (EV-PS-01 to EV-PS-03).
3. **Laws and standards:** this policy must be consistent with applicable law, ABC Technologies' policies and NIST SP 800-53 Rev 5. The laws that bear on it are below. ABC Technologies, as the employer, carries out the screening and holds its records, so these laws apply to it first. The legal adviser reviewed version \<ver\> on 12 November 2026, and confirms this list with the review of version \<ver\>.

**Table PS-2: Laws that bear on personnel security**

| Law | Why it matters here |
| --- | --- |
| UK GDPR, Article 10, and the Data Protection Act 2018, Schedule 1 | Criminal record data may be processed only under these conditions, which is why \<DocuView\> holds none (R4) |
| Rehabilitation of Offenders Act 1974 | Limits what may be asked about spent convictions, and so the level of criminal record check |
| Immigration, Asylum and Nationality Act 2006 | The employer's duty to check the right to work |
| Equality Act 2010 | Screening and sanctions must not discriminate |
| Employment Rights Act 1996, and the Acas Code of Practice on disciplinary and grievance procedures | How sanctions and dismissals are handled |

### PS.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### PS.8 Definitions

**Table PS-3: Definitions**

| Term | Meaning |
| --- | --- |
| Risk designation | How much harm the holder of a role could do, which sets the screening and attention the role receives |
| Higher risk role | A role with privileged technical access, or one that can see or change security records |
| Screening | The checks an employer makes on a person before and during employment |
| Access agreement | A signed undertaking: ABC Technologies' confidentiality agreement and the acknowledgement in \<Security Operating Procedures\>, section 10 |
| External person | Someone who works on \<DocuView\>, or assesses it, but is not employed by ABC Technologies, such as a contractor, a supplier's engineer or an independent assessor |
| Leaver, mover | Someone who leaves ABC Technologies or stops needing \<DocuView\>; someone who changes role |

### PS.9 References

**Table PS-4: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, PS family | The controls this policy meets |
| HMG Baseline Personnel Security Standard | The four checks used as the minimum in R2 |
| NPSA, Employment screening: a good practice guide; BS 7858:2019 | What a fuller screening standard covers, for comparison with ABC Technologies' own |
| \<Personnel Security Management\>, \<Procedures\> (PS), \<Roles and Responsibilities\>, \<Security Operating Procedures\> and \<Access Control Management\> | The designations and register, the procedures, the roles, the rules people sign and the account time limits |

| **CHAPTER PT** |
| --- |

## PT Personally Identifiable Information Processing and Transparency

[PT.1 Purpose and scope](#pt1-purpose-and-scope) · [PT.2 The organisation's position](#pt2-the-organisations-position) · [PT.3 Control principles](#pt3-control-principles) · [PT.4 Mandatory requirements](#pt4-mandatory-requirements) · [PT.5 Responsibilities](#pt5-responsibilities) · [PT.6 Governance requirements](#pt6-governance-requirements) · [PT.7 Non-compliance and risk acceptance](#pt7-non-compliance-and-risk-acceptance) · [PT.8 Definitions](#pt8-definitions) · [PT.9 References](#pt9-references)

### PT.1 Purpose and scope

This policy sets the organisation's rules for processing personal data in \<DocuView\>, in line with the NIST SP 800-53 Rev 5 PT family (PT-1) and UK data protection law. It stands alone, as each family has its own policy. The inventory, retention schedule and values that carry it out are in \<PII Processing Management\>, the impact assessment is \<Data Protection Impact Assessment\>, the privacy plan is \<Privacy Plan\>, and the steps people follow are in \<Procedures\> (PT).

It applies to all personal data in \<DocuView\>: HR documents, other project documents, the names held from sign-in, audit records, logs and export copies.

### PT.2 The organisation's position

ABC Technologies operates in the UK and is the controller of the personal data in \<DocuView\>. UK GDPR, the Data Protection Act 2018 and the Data (Use and Access) Act 2025 apply. \<DocuView\> holds HR documents that may contain special category data, so personal data gets the same care as any other Restricted information, and more where the law requires it.

### PT.3 Control principles

1. **P1 Lawful and known purpose:** personal data is processed only for a stated purpose, with a recorded lawful basis and, for special category data, a recorded condition.
2. **P2 Only what is needed, only as long as needed:** \<DocuView\> holds no more personal data than the purpose requires, for no longer than the retention schedule allows.
3. **P3 People's rights:** people can see, correct and ask to delete their data, and complain, as the law allows.
4. **P4 Assess before relying on it:** the impact assessment comes before production and before any significant change.

### PT.4 Mandatory requirements

1. **R1 Purposes:** personal data may be processed only for HR administration and managing project documents.
2. **R2 Basis and conditions:** each kind of personal data must have an Article 6 lawful basis recorded in \<PII Processing Management\>, section 4.3, confirmed by the legal adviser. Special category data must also have an Article 9 condition and, where needed, a Schedule 1 condition. Where a Schedule 1, Part 1 condition is relied on, an appropriate policy document must be in place. Consent is not used for employee data.
3. **R3 Inventory and record of processing:** \<PII Processing Management\>, section 4.3 must list every kind of personal data, and match ABC Technologies' record of processing (UK GDPR, Article 30; EV-PM-02).
4. **R4 Impact assessment:** \<Data Protection Impact Assessment\> must be completed and approved by the legal adviser, with the data protection officer's advice, before production and after any significant change in processing.
5. **R5 Special category data:** special category data may be held only in projects the business owner authorises, and those documents must be marked as such.
6. **R6 Retention:** personal data must be kept only for the period in \<PII Processing Management\>, section 4.7, then disposed of, with the disposal audited.
7. **R7 Rights and complaints:** requests from individuals must go to the legal adviser and be met by a reasonable and proportionate search of every project within one month. Complaints about how data is handled must be acknowledged within 30 days, investigated, and answered with the outcome.
8. **R8 Transparency:** ABC Technologies' employee privacy notice must name \<DocuView\> and its purposes, be reviewed every 12 months, and be linked from \<DocuView\>'s pages.
9. **R9 Breaches:** personal data breaches must be handled under \<Incident Response Management\>, section 4.8, including the 72-hour report to the ICO, harm to the people affected and the breach register.
10. **R10 Training and test data:** everyone who handles HR documents and all administrators must complete privacy training before access and every 12 months. Real personal data must not be used for testing, training or research.
11. **R11 Accuracy:** personal data must be kept accurate and up to date. Each project's personal data must be checked every 12 months, and anything inaccurate or out of date corrected or deleted.

### PT.5 Responsibilities

**Table PT-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Legal adviser | Owns the privacy plan and the impact assessment; confirms each lawful basis and condition and the appropriate policy document; handles requests, complaints and reports to the ICO |
| Data protection officer | Advises on the impact assessment and is the contact for individuals and the ICO, or the legal adviser records why none is required (D-PM-04) |
| System owner | Owns this policy and the inventory, and makes sure \<DocuView\> follows it |
| Business and information owner | Decides what personal data each project holds, authorises special category projects, and sets retention periods |
| ABC Technologies | Provides the employee privacy notice and the record of processing |

### PT.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<DocuView\>, and whenever they change.
2. **Policy review:** every 12 months, and after a significant incident, audit finding, change in the law or change in processing.
3. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-PersonalData.ps1 on a test stack, and records the result.
4. **Coordination:** the system owner works with the legal adviser, the data protection officer and ABC Technologies, and records what is agreed.
5. **Laws and standards:** this policy must be consistent with UK GDPR, the Data Protection Act 2018, the Data (Use and Access) Act 2025, ABC Technologies' policies and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 11 November 2026.

### PT.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### PT.8 Definitions

**Table PT-2: Definitions**

| Term | Meaning |
| --- | --- |
| Personal data | Any information about an identified or identifiable living person |
| Special category data | Data about health, ethnicity, religion, trade union membership, sex life, sexual orientation, genetics or biometrics (UK GDPR, Article 9) |
| Appropriate policy document | The document the Data Protection Act 2018, Schedule 1, Part 4 requires when relying on certain Schedule 1 conditions |
| Impact assessment | \<Data Protection Impact Assessment\>, the data protection impact assessment |
| Record of processing | ABC Technologies' record of processing activities under UK GDPR, Article 30 |
| Complaint | A complaint to the controller about how personal data is handled, under the Data (Use and Access) Act 2025 |

### PT.9 References

**Table PT-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, PT family and SP 800-53B privacy baseline | The controls this policy meets |
| UK GDPR; Data Protection Act 2018; Data (Use and Access) Act 2025 | The law |
| ICO guidance: keeping employment records (February 2025); data protection impact assessments | How the law applies to HR records |
| \<PII Processing Management\>, \<Data Protection Impact Assessment\>, \<Privacy Plan\>, \<Procedures\> (PT), \<Incident Response Management\> and \<Security Operating Procedures\> | The inventory, impact assessment, privacy plan, procedures, breach handling and the rules people sign |

| **CHAPTER RA** |
| --- |

## RA Risk Assessment

[RA.1 Purpose and scope](#ra1-purpose-and-scope) · [RA.2 The organisation's position](#ra2-the-organisations-position) · [RA.3 Control principles](#ra3-control-principles) · [RA.4 Mandatory requirements](#ra4-mandatory-requirements) · [RA.5 Responsibilities](#ra5-responsibilities) · [RA.6 Governance requirements](#ra6-governance-requirements) · [RA.7 Non-compliance and risk acceptance](#ra7-non-compliance-and-risk-acceptance) · [RA.8 Definitions](#ra8-definitions) · [RA.9 References](#ra9-references)

### RA.1 Purpose and scope

This policy sets the organisation's rules for understanding and responding to risk in \<DocuView\>, in line with the NIST SP 800-53 Rev 5 RA family (RA-1). It stands alone, as each family has its own policy. The values that carry it out are in \<Risk Assessment Management\>, the steps people follow are in \<Procedures\> (RA), and the risks themselves are in \<Risk List\>.

It applies to DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database, the backups and the two Windows Server 2025 VMs they run on at ABC Technologies.

### RA.2 The organisation's position

\<DocuView\> is not required to meet every control. Every non-compliance is identified and documented, its risk is understood, and a named person decides what happens to it. Finding a non-compliance does not by itself start a fix.

### RA.3 Control principles

1. **Risk-based:** decisions follow the rated risk, assessed by a stated method.
2. **Named decisions:** a named person decides each risk, at the level set for its rating.
3. **Keep looking:** vulnerabilities are looked for continually, not only at assessment.
4. **Exploited first:** a flaw being exploited in the wild is dealt with ahead of everything else.
5. **Know what matters most:** critical components get closest attention.

### RA.4 Mandatory requirements

1. **R1 Risk record:** \<Risk List\> is the record of risk assessment. It must use the method in its section 5, which follows NIST SP 800-30 Rev 1, and give each risk a status and the date it was last reviewed.
2. **R2 Risk review:** the risk assessment must be reviewed every 12 months, and after a significant change, incident or new test result, and shared with the system owner, the authorising official and the Head of Cyber.
3. **R3 Categorisation:** the system must keep a security categorisation under FIPS 199 and NIST SP 800-60, with its rationale, approved by the authorising official.
4. **R4 Organisational risk:** system risk decisions must respect ABC Technologies' risk management strategy and risk appetite once confirmed (D-PM-03).
5. **R5 Supply chain:** supply chain risk from packages, base images, suppliers and the VMs must be reviewed every 12 months, and recorded on TPL-23.
6. **R6 Scanning:** vulnerability scans must run monthly and at each release, with definitions updated before each scan, and credentialed scans of both VMs. The packages, \<DocuView\>'s own applications, the container images and their operating system packages must all be covered.
7. **R7 Response times:** each vulnerability must be fixed or mitigated within the time in \<Risk Assessment Management\>, section 4.6, for its severity, counted from the fix's release, or from detection if that is later. Critical and High within 14 days, Medium within 30 days, Low within 90 days or 30 days once a vendor update exists. Severity is the vendor's rating, or else the CVSS base score.
8. **R8 Exploited flaws:** a flaw listed in CISA's Known Exploited Vulnerabilities catalogue, or confirmed by its vendor as exploited, must be fixed or mitigated within 3 days as an emergency change. A fix that cannot meet any time goes to a risk decision under section RA.7.
9. **R9 Reports:** vulnerability reports must be received through ABC Technologies' security contact, which must be published with terms that authorise research in good faith, and flaws found in another party's component must be reported to its maintainer.
10. **R10 Critical components:** critical components must be identified by the method in \<Risk Assessment Management\>, section 4.9, and reviewed at each major release and significant change.

### RA.5 Responsibilities

**Table RA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies; confirms the risk thresholds against ABC Technologies' risk appetite |
| System owner | Owns this policy and the risk list, decides Low risks, holds the risk and supply chain reviews, and approves critical components |
| Authorising official | Approves the categorisation, and decides Medium and High risks |
| Information owner | Confirms the information types and their impact levels |
| Security officer | Reviews scan results, tracks them to closure, and receives vulnerability reports |
| Windows server administrator | Runs scans of the VMs |
| Developers | Check packages and images at each release, and fix flaws in \<DocuView\>'s code |
| ABC Technologies | Provides the security contact, and any shared scanning service |

### RA.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<DocuView\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-Vulnerability.ps1, and records the result.
3. **Coordination:** the system owner agrees with ABC Technologies' security contact how inherited protections and vulnerability reports are handled, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, ABC Technologies' policies, the Cyber Essentials requirements ABC Technologies holds, and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 11 November 2026.

### RA.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy. A vulnerability that cannot be fixed in time is recorded the same way, with its compensating measure.

### RA.8 Definitions

**Table RA-2: Definitions**

| Term | Meaning |
| --- | --- |
| Risk | The chance that a threat source exploits a weakness, combined with the harm that would cause (NIST SP 800-30 Rev 1) |
| Vulnerability | A weakness in \<DocuView\>, its components or its operation that a threat source could exploit |
| Severity | The vendor's rating of a vulnerability or, without one, its CVSS base score: 9.0 or more Critical, 7.0 to 8.9 High, 4.0 to 6.9 Medium, below 4.0 Low |
| Exploited flaw | A vulnerability in CISA's Known Exploited Vulnerabilities catalogue, or confirmed as exploited by its vendor or ABC Technologies |
| Critical component | A component whose failure or compromise would expose or lose the documents, or defeat a security control |
| Mitigate | Reduce a vulnerability's risk without the fix, for example by disabling the affected feature or blocking access to it |

### RA.9 References

**Table RA-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, RA family | The controls this policy meets |
| NIST SP 800-30 Rev 1 | The risk method |
| NIST SP 800-40 Rev 4 | Patch management as preventive maintenance |
| FIPS 199 and NIST SP 800-60 Volume II Rev 1 | Categorisation |
| Cyber Essentials, Requirements for IT Infrastructure \<ver\> | The 14-day limit ABC Technologies meets for high and critical updates |
| NCSC vulnerability management guidance | Updating by default, responding to exploitation, and owning the risk of not updating |
| CISA Known Exploited Vulnerabilities catalogue | The list of exploited flaws |
| \<Risk List\>, \<Risk Assessment Management\>, \<Procedures\> (RA), \<Plan of Action and Milestones\> and \<Supply Chain Risk Management\> | The risks, values, procedures, plan of action and supply chain plan |

| **CHAPTER SA** |
| --- |

## SA System and Services Acquisition

[SA.1 Purpose and scope](#sa1-purpose-and-scope) · [SA.2 The organisation's position](#sa2-the-organisations-position) · [SA.3 Control principles](#sa3-control-principles) · [SA.4 Mandatory requirements](#sa4-mandatory-requirements) · [SA.5 Responsibilities](#sa5-responsibilities) · [SA.6 Governance requirements](#sa6-governance-requirements) · [SA.7 Non-compliance and risk acceptance](#sa7-non-compliance-and-risk-acceptance) · [SA.8 Definitions](#sa8-definitions) · [SA.9 References](#sa9-references)

### SA.1 Purpose and scope

This policy sets the organisation's rules for buying and building \<DocuView\>, in line with the NIST SP 800-53 Rev 5 SA family (SA-1). It stands alone, as each family has its own policy. The values that carry it out are in \<System and Services Acquisition Management\>, and the steps people follow are in \<Procedures\> (SA).

It applies to \<DocuView\>'s in-house development and build environment, and to every product, component and service bought or used from outside, including source code hosting and package registries.

### SA.2 The organisation's position

\<DocuView\> is built in-house, so its developers carry most of these duties. Security and privacy are planned from the start, not added at the end. Where a rule here is not yet met, the gap is recorded in \<Plan of Action and Milestones\> rather than described as done.

### SA.3 Control principles

1. **A named framework:** development follows NIST SSDF \<ver\>, practice by practice.
2. **Known changes only:** only reviewed and approved changes reach a release.
3. **Test before release:** every security function is tested at each release, to a stated depth.
4. **Know what you depend on:** every third-party component and external service is known, assessed and supported.

### SA.4 Mandatory requirements

1. **R1 Framework:** \<DocuView\> must be developed under NIST SSDF \<ver\>, with each practice mapped to how it is met in \<System and Services Acquisition Management\>, section 4.2.
2. **R2 Resources:** the system owner must raise security and privacy costs in yearly budgeting, and record them.
3. **R3 Contracts:** contracts must use ABC Technologies' standard terms, with security and privacy requirements, documentation, responsibilities and acceptance criteria added.
4. **R4 Design information:** design and the functions, ports, protocols and services \<DocuView\> needs must be documented, and kept current with each change.
5. **R5 Documentation:** administrator and user guides covering secure installation, configuration, operation and use must be kept with the code and confirmed at each release.
6. **R6 Principles:** design must follow the NCSC secure design principles and NIST's privacy engineering objectives, as mapped in \<Security Architecture\>, section 7.5.
7. **R7 Change control:** code, configuration and documents must be held in Git, with each default branch protected, at least one approving review before a change merges, dependency alerts on, and release tags signed. Test scripts must be under version control. Until this is in place, the gap is tracked in PA-91.
8. **R8 Build and test:** each release must pass unit, integration and security tests covering every security function, to the depth in \<System and Services Acquisition Management\>, section 4.9. Builds must not turn package vulnerability checks off.
9. **R9 Third parties:** each new third-party component must be checked for origin, licence, support and known vulnerabilities before it is added. External services, including GitHub and the package and container registries, must state their controls and be reviewed every 12 months.
10. **R10 Support:** components must be replaced before support ends, with a replacement planned at least 6 months before. Any exception needs the authorising official's approval.

### SA.5 Responsibilities

**Table SA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Approves exceptions for unsupported components |
| System owner | Owns this policy, raises security costs, controls the repositories' settings, and reviews external services |
| Developers | Follow the framework, review each other's changes, test, fix flaws and keep the guides current |
| Security officer | Checks security at each stage, and reviews the tests and principles at each release |

### SA.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with developers and administrators, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-Development.ps1, and records the result.
3. **Coordination:** the system owner agrees contract terms with ABC Technologies, and records them.
4. **Laws and standards:** this policy must be consistent with applicable law, ABC Technologies' policies and NIST SP 800-53 Rev 5, and aligns with the UK Software Security Code of Practice. The legal adviser reviewed it on 11 November 2026.

### SA.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### SA.8 Definitions

**Table SA-2: Definitions**

| Term | Meaning |
| --- | --- |
| SSDF | NIST's Secure Software Development Framework, SP 800-218: practices to prepare the organisation, protect the software, produce well-secured software and respond to vulnerabilities |
| Default branch | The branch in each repository that releases are built from |
| Third-party component | Any package, library, base image or script \<DocuView\> uses but didn't write |
| External service | A service run by someone else that \<DocuView\> depends on, such as hosting, source code hosting or a package registry |
| Security function | A part of \<DocuView\> that enforces a control, such as sign-in, project access, audit or session time-out |

### SA.9 References

**Table SA-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, SA family | The controls this policy meets |
| NIST SP 800-218 (SSDF) \<ver\> | The development framework |
| NCSC secure design principles; NIST privacy engineering objectives | The engineering principles |
| OWASP ASVS 5.0 | The verification depth for the web applications |
| UK Software Security Code of Practice | Peer practice the policy aligns with |
| \<System and Services Acquisition Management\>, \<Procedures\> (SA), \<Security Architecture\>, \<Administrator Guide\> and \<User Guide\> | The values, procedures, design and guides |

| **CHAPTER SC** |
| --- |

## SC System and Communications Protection

[SC.1 Purpose and scope](#sc1-purpose-and-scope) · [SC.2 The organisation's position](#sc2-the-organisations-position) · [SC.3 Control principles](#sc3-control-principles) · [SC.4 Mandatory requirements](#sc4-mandatory-requirements) · [SC.5 Responsibilities](#sc5-responsibilities) · [SC.6 Governance requirements](#sc6-governance-requirements) · [SC.7 Non-compliance and risk acceptance](#sc7-non-compliance-and-risk-acceptance) · [SC.8 Definitions](#sc8-definitions) · [SC.9 References](#sc9-references)

### SC.1 Purpose and scope

This policy sets the organisation's rules for protecting \<DocuView\>'s communications, boundaries, keys and stored information, in line with the NIST SP 800-53 Rev 5 SC family (SC-1). It stands alone, as each family has its own policy. The values, cryptographic register and allow-lists that carry it out are in \<System and Communications Protection Management\>, and the steps people follow are in \<Procedures\> (SC).

It applies to DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database, their backups and keys, and the two Windows Server 2025 VMs they run on at ABC Technologies.

### SC.2 The organisation's position

Information in \<DocuView\> must be protected wherever it travels or rests. \<DocuView\> relies on ABC Technologies' network protections, and must also protect itself: its own listening addresses, host firewalls, transport encryption, keys and pages are \<DocuView\>'s responsibility. Where a rule here is not yet met, the gap is recorded in \<Plan of Action and Milestones\> rather than described as done.

### SC.3 Control principles

1. **Deny by default:** only the agreed flows are allowed, at ABC Technologies' firewalls and on each VM.
2. **Encrypt everything that moves:** every flow uses TLS, including those that stay inside a VM.
3. **Know every key:** every key and cryptographic use is recorded, owned, protected and changed on time.
4. **Separate:** administration and the API are kept apart from everyday use.

### SC.4 Mandatory requirements

1. **R1 Flows:** only the flows in \<System Security Plan\>, section 4.7, Table 10, and \<Security Architecture\>, Table 5, are allowed. Traffic is denied by default at ABC Technologies' firewalls and at each VM's host firewall, using the allow-lists in \<System and Communications Protection Management\>, section 4.2.
2. **R2 Listening addresses:** DV\_Web listens on TCP 443 only. The admin portal is reachable only over ABC Technologies' managed administration route. DV\_API listens only on the application VM's loopback address. The database accepts connections only from the application VM.
3. **R3 Transport:** every flow must use TLS under NCSC's profiles. TLS 1.3 is preferred, with hybrid post-quantum key exchange where the platform supports it. TLS 1.2 is allowed only with the GCM profiles. SSL, TLS 1.0 and 1.1, compression and TLS 1.3 early data (0-RTT) must be off.
4. **R4 Web sessions:** the apps must serve HTTPS only and redirect HTTP, send HSTS with a maximum age of at least 1 year, and mark every cookie Secure, HttpOnly and SameSite. Sessions end after 30 minutes idle and after 8 hours.
5. **R5 Database:** PostgreSQL must accept network connections only over TLS, with a minimum of TLS 1.2, and DV\_API must connect with full certificate and host name checking.
6. **R6 Cryptography:** only the algorithms in the cryptographic register may be used: NCSC's TLS profiles, XTS-AES 256 for disk encryption, PBKDF2-SHA512 with at least 600,000 iterations for passwords, and HMAC-SHA256 with a random key of at least 256 bits for tokens. US FIPS 140 validation is not required (D-SC-P02).
7. **R7 Keys:** every key must be in the register, with an owner, a protected store and a cryptoperiod based on NIST SP 800-57. Keys must never be held in source code, tickets, chat or documents. Each key is changed at the end of its cryptoperiod, when someone who held it leaves, and at once if it may be compromised. The data protection key rings are protected with Windows DPAPI and backed up with the server.
8. **R8 Certificates:** certificates are issued under ABC Technologies' certificate policy, use ECDSA P-256 or RSA 2048-bit with SHA-256, and are renewed at least 30 days before they expire. Only ABC Technologies' approved trust anchors are trusted.
9. **R9 Data at rest:** both VMs must use BitLocker with XTS-AES 256 and the TPM. Backups must be encrypted. Export copies must be deleted once downloaded. Recovery keys are held in ABC Technologies' protected store and tested every 12 months.
10. **R10 Mobile code:** pages may run only JavaScript and WebAssembly served by \<DocuView\>. Each app must send a page security policy with no inline scripts, no eval and no outside hosts, that limits where forms may be sent and upgrades insecure requests. Any exception is approved by the system owner and recorded.
11. **R11 Availability and remote access:** each app must limit request rates, on top of ABC Technologies' denial-of-service protection. Split tunnelling is not allowed. Outbound traffic from the VMs goes through ABC Technologies' authenticated proxy, or is blocked.
12. **R12 Change and checking:** a new flow, port, external service, key or certificate goes through change control and updates the register and allow-lists first. Test-Protection.ps1 is run at each release, after a significant change and at each review.

### SC.5 Responsibilities

**Table SC-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Decides Medium and High risks, and any exception to R3 or R6 |
| System owner | Owns this policy and the cryptographic register; approves new flows and mobile code exceptions; reviews the boundary with ABC Technologies every 12 months |
| Windows server administrator | Sets TLS, certificates, host firewall rules, BitLocker and key ring protection on the VMs |
| Database administrator | Sets TLS in PostgreSQL, with client rules that require it, and encrypts backups |
| Developers | Build secure sessions, cookies and page policies; keep keys out of the code; configure the key rings and rate limits; run Test-Protection.ps1 |
| Security officer | Checks the register and test results at each review |
| ABC Technologies | Provides firewalls, proxy, DNS, certificates and denial-of-service protection |

### SC.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers or develops \<DocuView\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-Protection.ps1 and checks the register, and records the result.
3. **Coordination:** the system owner agrees with ABC Technologies' security contact how inherited protections are provided, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, ABC Technologies' policies and NIST SP 800-53 Rev 5, and follows NCSC's guidance on TLS. The legal adviser reviewed it on 12 November 2026.

### SC.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### SC.8 Definitions

**Table SC-2: Definitions**

| Term | Meaning |
| --- | --- |
| Flow | A permitted connection between two parts of the system, or between \<DocuView\> and something outside it |
| Cryptoperiod | How long a key may be used before it must be changed |
| Data protection key ring | The keys ASP.NET Core uses to protect each app's cookies and antiforgery tokens |
| Mobile code | Code a page sends to run in the browser, such as JavaScript or WebAssembly |
| Loopback address | An address only reachable from the same machine, such as 127.0.0.1 |
| Trust anchor | A root certificate that the system trusts to issue other certificates |

### SC.9 References

**Table SC-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, SC family | The controls this policy meets |
| NCSC, Using TLS to protect data (updated 15 October 2026) | The TLS profiles |
| NIST SP 800-57 Part 1 Rev 5 | Cryptoperiods and key management |
| PostgreSQL 18 documentation, Secure TCP/IP Connections with SSL | Database TLS enforcement |
| Microsoft, ASP.NET Core Data Protection key encryption at rest | The key ring protection |
| \<System and Communications Protection Management\>, \<Procedures\> (SC), \<Security Architecture\> and \<System Security Plan\>, section 4.7 | The values, procedures, design and flows |

| **CHAPTER SI** |
| --- |

## SI System and Information Integrity

[SI.1 Purpose and scope](#si1-purpose-and-scope) · [SI.2 The organisation's position](#si2-the-organisations-position) · [SI.3 Control principles](#si3-control-principles) · [SI.4 Mandatory requirements](#si4-mandatory-requirements) · [SI.5 Responsibilities](#si5-responsibilities) · [SI.6 Governance requirements](#si6-governance-requirements) · [SI.7 Non-compliance and risk acceptance](#si7-non-compliance-and-risk-acceptance) · [SI.8 Definitions](#si8-definitions) · [SI.9 References](#si9-references)

### SI.1 Purpose and scope

This policy sets the organisation's rules for keeping \<DocuView\> free of known flaws and malicious code, watching it for misuse, and showing that its software and records have not been changed without authority, in line with the NIST SP 800-53 Rev 5 SI family (SI-1). It stands alone, as each family has its own policy. The values, detection use cases and retention table that carry it out are in \<System and Information Integrity Management\>, and the steps people follow are in \<Procedures\> (SI).

It applies to DV\_Web, DV\_Admin\_UI, DV\_API, the \<DocuView\> database, the documents and records it holds, and the two Windows Server 2025 VMs they run on at ABC Technologies.

### SI.2 The organisation's position

\<DocuView\> holds Restricted documents. It must be patched promptly, keep malicious files out, notice misuse quickly, and be able to prove that its software and records are unchanged. Where a rule here is not yet met, the gap is recorded in \<Plan of Action and Milestones\> rather than described as done.

### SI.3 Control principles

1. **One timetable:** every flaw is fixed to the same risk-based timetable.
2. **Nothing unchecked comes in:** every input and upload is validated, and every upload is scanned.
3. **Watch and respond:** defined events raise alerts that reach a named person.
4. **Prove integrity:** software and records are checked against a recorded baseline.
5. **Say little in errors:** detail goes only to those who need it.

### SI.4 Mandatory requirements

1. **R1 Flaw remediation:** flaws must be fixed to the one timetable in \<Risk Assessment Management\>, section 4.6: 3 days for a flaw known to be exploited, 14 days for Critical and High, 30 days for Medium, and 90 days for Low (30 once a vendor fix exists), counted from the fix's release or its detection if later. Updates are tested first and installed through change control.
2. **R2 Update status:** Test-Vulnerability.ps1 must run monthly and at each release, dependency alerts must be on for every repository, and Windows Update status must be reported from both VMs.
3. **R3 Malicious code:** Microsoft Defender must run on both VMs, with real-time protection, daily updates and a weekly full scan. Every upload must be passed to Defender through the Windows Antimalware Scan Interface (AMSI) before it is stored. A flagged file is refused, recorded in the audit trail and reported to the security officer.
4. **R4 Upload checks:** only the allowed document types may be uploaded. Each file's type and signature must match its extension, its size must be within the limit for the user's role, and its name must not contain a path.
5. **R5 Monitoring:** application, Windows and PostgreSQL logs must be forwarded to ABC Technologies' central logging and reviewed weekly. The detection use cases in \<System and Information Integrity Management\>, section 4.4, must raise alerts to the security officer.
6. **R6 Monitoring people:** users must be monitored only after the legal adviser's opinion (D-SI-07), only as far as needed, and with staff told what is monitored and why.
7. **R7 Advisories:** advisories must be received from NCSC (including Early Warning), CISA's Known Exploited Vulnerabilities catalogue (weekly), Microsoft, .NET and GitHub, and PostgreSQL, and passed to the people who act on them.
8. **R8 Integrity:** release packages, stored documents and audit records must be protected with SHA-256 and checked against the recorded baseline at start-up, at each release and monthly. An unexpected change is handled as an incident.
9. **R9 Input validation:** all API inputs, uploads and search terms must be validated on the server, and database queries must use parameters.
10. **R10 Errors:** users and API callers must receive general error messages. Exception detail goes only to the logs, for administrators and developers.
11. **R11 Retention:** information must be kept and disposed of under \<DocuView\>'s retention schedule (\<PII Processing Management\>, section 4.7): audit records for 12 months online and 12 archived, application logs for 30 days, and export copies deleted once downloaded.
12. **R12 Checking:** Test-Integrity.ps1 must run at each release, after a significant change and at each review.

### SI.5 Responsibilities

**Table SI-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Decides Medium and High risks |
| System owner | Owns this policy and the detection use cases |
| Security officer | Reviews logs and alerts, runs the advisory process, and leads the response to detections |
| Windows server administrator | Patches the VMs, runs Defender and forwards Windows logs |
| Database administrator | Patches PostgreSQL and forwards its logs |
| Developers | Update packages, build upload scanning, validation and safe errors, and run Test-Integrity.ps1 |
| Legal adviser | Advises on monitoring users (D-SI-07) and on retention periods |
| ABC Technologies | Monitors network traffic, provides central logging, and registers \<DocuView\>'s addresses with NCSC Early Warning |

### SI.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers or develops \<DocuView\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-Integrity.ps1, and records the result.
3. **Coordination:** the system owner agrees with ABC Technologies' security contact how monitoring, logging and firmware updates are provided, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, ABC Technologies' policies and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 12 November 2026.

### SI.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### SI.8 Definitions

**Table SI-2: Definitions**

| Term | Meaning |
| --- | --- |
| Flaw | A weakness in software or firmware that could be exploited, including a known vulnerability in a package |
| AMSI | The Windows Antimalware Scan Interface, through which an application asks the installed antivirus to scan data |
| Detection use case | A defined event or pattern, its source, threshold and the response to it |
| Integrity baseline | The recorded hashes of a known-good release, used to detect later change |
| Advisory | A security alert, warning or directive from an outside source, or an internal note made from one |

### SI.9 References

**Table SI-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, SI family | The controls this policy meets |
| NIST SP 800-40 Rev 4 | Patch management |
| OWASP File Upload Cheat Sheet | Upload checks |
| NCSC Early Warning; CISA Known Exploited Vulnerabilities catalogue | Advisory sources |
| ICO, Employment practices and data protection: monitoring workers (October 2023) | Monitoring people |
| \<System and Information Integrity Management\>, \<Procedures\> (SI), \<Risk Assessment Management\>, \<PII Processing Management\> and \<Audit and Accountability Management\> | The values, procedures, timetable, retention schedule and audit settings |

| **CHAPTER SR** |
| --- |

## SR Supply Chain Risk Management

[SR.1 Purpose and scope](#sr1-purpose-and-scope) · [SR.2 The organisation's position](#sr2-the-organisations-position) · [SR.3 Control principles](#sr3-control-principles) · [SR.4 Mandatory requirements](#sr4-mandatory-requirements) · [SR.5 Responsibilities](#sr5-responsibilities) · [SR.6 Governance requirements](#sr6-governance-requirements) · [SR.7 Non-compliance and risk acceptance](#sr7-non-compliance-and-risk-acceptance) · [SR.8 Definitions](#sr8-definitions) · [SR.9 References](#sr9-references)

### SR.1 Purpose and scope

This policy sets the organisation's rules for managing the risk that \<DocuView\> is harmed through what it is built from, where it is hosted, and who supplies it, in line with the NIST SP 800-53 Rev 5 SR family (SR-1). It stands alone, as each family has its own policy. The plan, supplier register and values are in \<Supply Chain Risk Management\>, and the steps people follow are in \<Procedures\> (SR).

It applies to the software packages, container images and browser files \<DocuView\> is built from, the tools that build it, the hosting, network and hardware ABC Technologies provides, and the services \<DocuView\> depends on.

### SR.2 The organisation's position

\<DocuView\> is mostly made of other people's code: DV\_API alone restores 59 packages. A compromise of any supplier could reach \<DocuView\>, so what comes in is chosen, checked, fixed and watched. Where a rule here is not yet met, the gap is recorded in \<Plan of Action and Milestones\> rather than described as done.

### SR.3 Control principles

1. **Know the supply chain:** every supplier is named, with its criticality.
2. **One way in:** every package comes through one checked source.
3. **Fix and verify:** a release is built from exactly the components recorded for it, and can be shown to be so.
4. **Hear about problems:** suppliers and advisories tell us when something goes wrong.
5. **Nothing left behind:** \<DocuView\> data is removed before anything leaves.

### SR.4 Mandatory requirements

1. **R1 Plan and team:** a supply chain plan with a supplier register must be kept in \<Supply Chain Risk Management\> and reviewed every 12 months by the supply chain team: the system owner, the security officer, a developer and ABC Technologies' IT service desk.
2. **R2 Tolerance:** no critical component may be used without a known source and a SHA-256 record.
3. **R3 Approved suppliers:** hardware, hosting and services must come from suppliers ABC Technologies has approved. A new critical supplier must be reviewed before use.
4. **R4 One package source:** every software package, including those pulled in by others, must be restored only from the offline feed, after the PRO-SR-1 check. nuget.org may be used only as a source of vulnerability data.
5. **R5 Fixed and trusted restores:** every project must use a lock file in locked mode, and restores must accept only packages signed by trusted signers.
6. **R6 Images and browser files:** container images must be pinned by digest, and any file a page loads from another host must carry an integrity check.
7. **R7 Monitoring components:** packages and images must be checked for known flaws monthly and at each release, with NuGet's audit on in every build.
8. **R8 Bill of materials:** each release must have a bill of materials that lists every component with its version, hash and licence.
9. **R9 Inspection:** each release must be inspected against its recorded SHA-256 values before installation, and when tampering is suspected. ABC Technologies must inspect hardware.
10. **R10 Supplier reviews and notices:** critical suppliers must be reviewed every 12 months on TPL-16. ABC Technologies must report a compromise to the security officer within 24 hours, and open-source suppliers' advisories must be watched (\<System and Information Integrity Management\>, section 4.3).
11. **R11 Authenticity:** a suspected counterfeit or look-alike component, hardware or software, must be refused and reported to the security officer, ABC Technologies and, where it applies, the package registry and the NCSC.
12. **R12 Disposal and checking:** components must be disposed of following \<Procedures\>, PRO-MP-3, and Test-SupplyChain.ps1 must run at each release, after a significant change and at each review.

### SR.5 Responsibilities

**Table SR-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Decides Medium and High risks |
| System owner | Owns this policy, the plan and the supplier register, and leads supplier reviews |
| Security officer | Receives notices of compromise and reports of counterfeits, and watches supplier advisories |
| Developers | Check and mirror packages, keep lock files, produce the bill of materials, and run Test-SupplyChain.ps1 |
| ABC Technologies | Approves suppliers, inspects hardware, trains its buyers, controls equipment under repair and disposes of equipment |

### SR.6 Governance requirements

The rules in section 2.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with developers and administrators, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-SupplyChain.ps1, and records the result.
3. **Coordination:** the supply chain team coordinates with ABC Technologies, and records what is agreed.
4. **Laws and standards:** this policy must be consistent with applicable law, ABC Technologies' policies and NIST SP 800-53 Rev 5. The legal adviser reviewed it on 12 November 2026.

### SR.7 Non-compliance and risk acceptance

The rule on non-compliance in section 2.1 applies to this policy.

### SR.8 Definitions

**Table SR-2: Definitions**

| Term | Meaning |
| --- | --- |
| Supplier | Anyone who provides a component or service \<DocuView\> depends on, including open-source projects and package registries |
| Critical component | A component whose failure or compromise would harm \<DocuView\>'s confidentiality, integrity or availability (\<Risk Assessment Management\>, section 4.9) |
| Offline feed | The in-house offline package repository, whose packages are recorded with SHA-256 values |
| Lock file | A file that records the exact version and content hash of every package a project restores |
| Bill of materials | A list of every component in a release, with its version, supplier, hash and licence |
| Counterfeit | A component that is not what it claims to be, including a look-alike package |

### SR.9 References

**Table SR-3: References**

| Reference | Use |
| --- | --- |
| NIST SP 800-53 Rev 5, SR family | The controls this policy meets |
| NIST SP 800-161 Rev 1, update 1 | Supply chain risk management practice and the plan's content |
| UK Software Security Code of Practice (May 2025) | Third-party components and the build environment |
| NCSC supply chain security principles | Supplier reviews |
| CISA 2025 minimum elements for a software bill of materials | What the bill of materials holds |
| \<Supply Chain Risk Management\>, \<Procedures\> (SR), \<Risk Assessment Management\>, \<System and Information Integrity Management\> and \<Procedures\> (MP) | The plan, procedures, critical components, integrity baseline and disposal |
